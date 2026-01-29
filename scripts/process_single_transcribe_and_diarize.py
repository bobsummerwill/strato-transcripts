#!/usr/bin/env python3
"""
Unified transcription with speaker diarization.
Supports: WhisperX (local), WhisperX Cloud (Replicate), AssemblyAI.
"""

import sys
import os
import argparse
import time
from pathlib import Path

# Import shared utilities
from common import (Colors, success, failure, skip, validate_api_key,
                    load_vocabulary, save_transcript_dual_format, cleanup_gpu_memory)


# ============================================================================
# Utility Functions
# ============================================================================


def format_timestamp(seconds):
    """
    Format seconds into MM:SS or H:MM:SS format (rounded to nearest second).
    
    Args:
        seconds: Time in seconds (float or int)
    
    Returns:
        Formatted timestamp string like "00:00", "01:23", or "1:02:34"
    """
    total_seconds = round(seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def merge_consecutive_speaker_segments(segments, speaker_key="speaker"):
    """
    Merge consecutive segments from the same speaker into single paragraphs.
    
    Args:
        segments: List of segment dicts with 'speaker', 'start', 'text' keys
        speaker_key: Key name for speaker in segments (default: 'speaker')
    
    Returns:
        List of merged segment dicts, each representing a continuous speaker turn
    """
    if not segments:
        return []
    
    merged = []
    current_speaker = None
    current_start = None
    current_texts = []
    
    for segment in segments:
        speaker = segment.get(speaker_key, "UNKNOWN")
        text = segment.get("text", "").strip()
        start_time = segment.get("start", 0)
        
        if not text:
            continue
        
        if speaker != current_speaker:
            # Save previous speaker's accumulated text
            if current_speaker is not None and current_texts:
                merged.append({
                    'speaker': current_speaker,
                    'start': current_start,
                    'text': ' '.join(current_texts)
                })
            # Start new speaker
            current_speaker = speaker
            current_start = start_time
            current_texts = [text]
        else:
            # Same speaker, accumulate text
            current_texts.append(text)
    
    # Don't forget the last speaker
    if current_speaker is not None and current_texts:
        merged.append({
            'speaker': current_speaker,
            'start': current_start,
            'text': ' '.join(current_texts)
        })
    
    return merged


def save_transcript_files(output_dir, basename, service_name, segments, speaker_key="speaker"):
    """
    Save transcript in both txt and md formats with consistent naming.
    Consecutive segments from the same speaker are merged into paragraphs.
    TXT format: No timestamps, no markdown - just "SPEAKER_XX: text"
    MD format: With rounded timestamps - "**[MM:SS] SPEAKER_XX:** text"

    Args:
        output_dir: Directory to save files
        basename: Base filename without extension
        service_name: Name of transcription service (whisperx, deepgram, etc.)
        segments: List of segment dicts with 'speaker', 'start', 'text' keys
        speaker_key: Key name for speaker in segments (default: 'speaker')

    Returns:
        Path object for the .txt file
    """
    # Create episode-specific subdirectory, but avoid nesting if output_dir already ends with basename
    output_dir_path = Path(output_dir)
    if output_dir_path.name == basename:
        episode_dir = output_dir_path
    else:
        episode_dir = output_dir_path / basename
    episode_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = episode_dir / f"{basename}_{service_name}.txt"
    
    # Merge consecutive segments from same speaker into paragraphs
    merged_segments = merge_consecutive_speaker_segments(segments, speaker_key)
    
    # Save text version (NO timestamps, NO markdown)
    # Format: SPEAKER_XX: text
    with open(output_path, 'w', encoding='utf-8') as f:
        for segment in merged_segments:
            speaker = segment['speaker']
            text = clean_text(segment['text'])
            if text:
                f.write(f"{speaker}: {text}\n\n")
    
    # Save markdown version (WITH timestamps)
    # Format: **[MM:SS] SPEAKER_XX:** text
    md_path = output_path.with_suffix('.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        for segment in merged_segments:
            speaker = segment['speaker']
            start_time = segment['start']
            text = clean_text(segment['text'])
            timestamp = format_timestamp(start_time)
            if text:
                f.write(f"**[{timestamp}] {speaker}:** {text}\n\n")
    
    return output_path


def clean_text(text):
    """
    Clean up text by removing spaces before punctuation marks.
    
    Args:
        text: Raw text that may have spaces before punctuation
    
    Returns:
        Cleaned text with spaces before punctuation removed
    """
    import re
    # Remove spaces before punctuation marks (. , ! ? : ; ' ")
    text = re.sub(r'\s+([.,!?;:\'\"])', r'\1', text)
    return text


def save_raw_transcript_from_text(output_dir, basename, service_name, formatted_text):
    """
    Save pre-formatted transcript text in both txt and md formats.
    Consecutive segments from the same speaker are merged into paragraphs.
    TXT format: No timestamps, no markdown - "SPEAKER_XX: text"
    MD format: With rounded timestamps - "**[MM:SS] SPEAKER_XX:** text"

    Args:
        output_dir: Directory to save files
        basename: Base filename without extension
        service_name: Name of transcription service
        formatted_text: Pre-formatted text with speaker labels and timestamps
                       Format: "SPEAKER_XX:\n[123.4s] text\n[125.0s] more text\n"

    Returns:
        Path object for the .txt file
    """
    import re

    # Create episode-specific subdirectory, but avoid nesting if output_dir already ends with basename
    output_dir_path = Path(output_dir)
    if output_dir_path.name == basename:
        episode_dir = output_dir_path
    else:
        episode_dir = output_dir_path / basename
    episode_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = episode_dir / f"{basename}_{service_name}.txt"
    
    # Parse the formatted text into segments
    # Format: SPEAKER_XX: header, then [XXX.Xs] text lines
    segments = []
    current_speaker = None
    
    for line in formatted_text.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # Check for speaker header: "SPEAKER_XX:"
        speaker_match = re.match(r'^(SPEAKER_\d+):$', line)
        if speaker_match:
            current_speaker = speaker_match.group(1)
            continue
        
        # Check for timestamped line: "[XXX.Xs] text"
        time_match = re.match(r'^\[([\d.]+)s\]\s*(.+)', line)
        if time_match and current_speaker:
            timestamp_seconds = float(time_match.group(1))
            text = time_match.group(2).strip()
            if text:
                segments.append({
                    'speaker': current_speaker,
                    'start': timestamp_seconds,
                    'text': text
                })
    
    # Merge consecutive segments from same speaker into paragraphs
    merged_segments = merge_consecutive_speaker_segments(segments)
    
    # Save text version (NO timestamps, NO markdown)
    # Format: SPEAKER_XX: text
    with open(output_path, 'w', encoding='utf-8') as f:
        for segment in merged_segments:
            text = clean_text(segment['text'])
            f.write(f"{segment['speaker']}: {text}\n\n")
    
    # Save markdown version (WITH timestamps)
    # Format: **[MM:SS] SPEAKER_XX:** text
    md_path = output_path.with_suffix('.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        for segment in merged_segments:
            timestamp = format_timestamp(segment['start'])
            text = clean_text(segment['text'])
            f.write(f"**[{timestamp}] {segment['speaker']}:** {text}\n\n")
    
    return output_path


# ============================================================================
# Main Entry Point
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio with speaker diarization using multiple providers",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("audio_file", help="Path to audio file")
    parser.add_argument(
        "--transcribers",
        required=True,
        help="Comma-separated list of transcription services (whisperx,whisperx-cloud,assemblyai)"
    )
    parser.add_argument("--output-dir", default="intermediates", help="Output directory")
    parser.add_argument("--force-cpu", action="store_true", help="Force CPU for WhisperX")
    
    args = parser.parse_args()
    
    # Validate audio file
    audio_path = Path(args.audio_file)
    if not audio_path.exists():
        print(f"Error: Audio file not found: {audio_path}")
        sys.exit(1)
    
    # Parse transcribers
    transcribers = [t.strip() for t in args.transcribers.split(',')]
    valid_transcribers = {'whisperx', 'whisperx-cloud', 'assemblyai'}
    
    for transcriber in transcribers:
        if transcriber not in valid_transcribers:
            print(f"Error: Unknown transcriber '{transcriber}'")
            print(f"Valid options: {', '.join(sorted(valid_transcribers))}")
            sys.exit(1)
    
    print("="*70)
    print("Unified Transcription Pipeline")
    print("="*70)
    print(f"Audio file: {audio_path}")
    print(f"Transcribers: {', '.join(transcribers)}")
    print(f"Output directory: {args.output_dir}")
    print("="*70)
    print()
    
    # Process each transcriber
    pipeline_start = time.time()
    results = []
    skipped = 0
    
    for i, transcriber in enumerate(transcribers, 1):
        print(f"[{i}/{len(transcribers)}] Transcribing with {transcriber}...")
        print("-" * 70)
        
        transcriber_start = time.time()
        
        # Check API keys using utility
        skip_reason = None
        if transcriber == 'assemblyai':
            _, skip_reason = validate_api_key('ASSEMBLYAI_API_KEY')
        elif transcriber == 'whisperx':
            _, skip_reason = validate_api_key('HF_TOKEN')
        elif transcriber == 'whisperx-cloud':
            _, skip_reason = validate_api_key('REPLICATE_API_TOKEN')
        
        if skip_reason:
            print(skip(f"{transcriber}: {skip_reason}"))
            results.append((transcriber, None, 'skipped'))
            skipped += 1
            print()
            continue
        
        try:
            if transcriber == 'whisperx':
                output_path = transcribe_whisperx(
                    str(audio_path),
                    args.output_dir,
                    args.force_cpu
                )
            elif transcriber == 'whisperx-cloud':
                output_path = transcribe_whisperx_cloud(str(audio_path), args.output_dir)
            elif transcriber == 'assemblyai':
                output_path = transcribe_assemblyai(str(audio_path), args.output_dir)
            
            elapsed = time.time() - transcriber_start
            results.append((transcriber, output_path, 'success', elapsed))
            print(success(f"{transcriber} complete ({elapsed:.1f}s): {output_path}"))
            
        except Exception as e:
            elapsed = time.time() - transcriber_start
            print(failure(f"{transcriber} failed ({elapsed:.1f}s): {e}"))
            results.append((transcriber, None, 'failed', elapsed))
        
        print()
    
    # Summary
    pipeline_elapsed = time.time() - pipeline_start
    
    print("="*70)
    print("Transcription Summary")
    print("="*70)
    successful = sum(1 for r in results if len(r) > 2 and r[2] == 'success')
    failed = sum(1 for r in results if len(r) > 2 and r[2] == 'failed')
    
    print(f"Total: {len(results)}")
    print(success(f"Successful: {successful}") if successful > 0 else f"Successful: 0")
    if failed > 0:
        print(failure(f"Failed: {failed}"))
    if skipped > 0:
        print(skip(f"Skipped: {skipped}"))
    print(f"Total time: {pipeline_elapsed:.1f}s ({pipeline_elapsed/60:.1f}min)")
    print()
    
    if successful > 0:
        print("Output files:")
        for result in results:
            if len(result) >= 3 and result[2] == 'success':
                transcriber, path = result[0], result[1]
                elapsed = result[3] if len(result) > 3 else 0
                print(f"  {transcriber}: {path} ({elapsed:.1f}s)")
    
    # Exit with error if all failed
    if successful == 0:
        print(failure("\nError: All transcriptions failed"))
        sys.exit(1)


def transcribe_whisperx(audio_path, output_dir, force_cpu=False):
    """WhisperX local transcription with speaker diarization"""
    import time
    import subprocess
    import tempfile
    import warnings
    import pandas as pd
    import whisperx
    import torch
    from pyannote.audio import Pipeline
    import gc

    # ------------------------------------------------------------------------
    # PyTorch 2.6+ compatibility: allowlist OmegaConf globals for weights-only
    # checkpoint loading used by pyannote.
    #
    # PyTorch 2.6 changed torch.load(weights_only) default to True. Some
    # pyannote checkpoints/configs reference OmegaConf classes and will fail to
    # load unless those globals are allowlisted.
    #
    # This keeps weights-only loading enabled (safer than weights_only=False)
    # while unblocking trusted checkpoints from HuggingFace.
    # ------------------------------------------------------------------------
    try:
        import typing
        from omegaconf.base import ContainerMetadata
        from omegaconf.dictconfig import DictConfig
        from omegaconf.listconfig import ListConfig

        # add_safe_globals was introduced for the new safe unpickling path.
        if hasattr(torch, "serialization") and hasattr(torch.serialization, "add_safe_globals"):
            torch.serialization.add_safe_globals([
                ContainerMetadata,
                DictConfig,
                ListConfig,
                typing.Any,
            ])
    except Exception:
        # Best-effort: if omegaconf isn't installed / API differs, we'll fail
        # later with a clearer error from torch/pyannote.
        pass

    # ------------------------------------------------------------------------
    # PyTorch 2.6+ fallback: pyannote/whisperx checkpoints may not be compatible
    # with weights_only=True safe loading (it can error on common globals like
    # builtins and typing types). When working with trusted HuggingFace
    # checkpoints, forcing weights_only=False is the pragmatic fix.
    #
    # SECURITY NOTE: torch.load(weights_only=False) can execute arbitrary code
    # contained in a malicious checkpoint. This is ONLY acceptable if you trust
    # the checkpoint source (e.g., official pyannote models on HuggingFace).
    # ------------------------------------------------------------------------
    try:
        from packaging.version import Version

        torch_version = Version(torch.__version__.split("+")[0])
        allow_unsafe = os.environ.get("WHISPERX_ALLOW_UNSAFE_TORCH_LOAD", "1").strip().lower() not in (
            "0",
            "false",
            "no",
        )

        if allow_unsafe and torch_version >= Version("2.6.0"):
            _orig_torch_load = torch.load

            def _torch_load_compat(*args, **kwargs):
                # Force-disable weights-only safe loading, even if a downstream
                # library explicitly requests it.
                kwargs["weights_only"] = False
                return _orig_torch_load(*args, **kwargs)

            torch.load = _torch_load_compat
            print("  ⚠ PyTorch>=2.6 detected: forcing torch.load(weights_only=False) for pyannote/whisperx checkpoints")
    except Exception:
        pass

    # ========================================================================
    # GPU CLEANUP - Clears PyTorch cache to free VRAM
    # ========================================================================
    cleanup_gpu_memory(force_cpu)
    if torch.cuda.is_available() and not force_cpu:
        print("  ✓ GPU memory cleared")

    # Suppress pyannote warnings
    warnings.filterwarnings('ignore', category=UserWarning,
                          module='pyannote.audio.utils.reproducibility',
                          message='.*TensorFloat-32.*')

    # Configure TF32 optimizations for Ampere/Ada/Blackwell RTX GPUs
    # Uses new PyTorch 2.9+ API (old allow_tf32 API deprecated)
    torch.backends.cudnn.conv.fp32_precision = 'tf32'
    torch.backends.cuda.matmul.fp32_precision = 'tf32'

    # Get HuggingFace token
    hf_token = os.environ.get('HF_TOKEN')
    if not hf_token:
        raise ValueError("HF_TOKEN environment variable not set")

    # Setup device
    if force_cpu:
        device = "cpu"
    else:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    
    model_name = "large-v3"
    compute_type = "float16" if device == "cuda" else "int8"
    batch_size = 32 if device == "cuda" else 8  # Optimized for 12GB+ GPUs like RTX 5070
    
    print(f"  Device: {device}")
    print(f"  Model: {model_name}")
    print(f"  Compute type: {compute_type}")
    print(f"  Batch size: {batch_size}")
    
    start = time.time()
    
    # Step 1: Transcribe with OOM retry
    print("  → Transcribing...")
    
    model = None
    model_a = None
    audio = None
    result = None

    try:
        print("  → Loading model...")
        model = whisperx.load_model(model_name, device, compute_type=compute_type, language="en")
        print("  → Model loaded successfully")
        print("  → Loading audio...")
        audio = whisperx.load_audio(audio_path)
        print("  → Audio loaded successfully")
        result = model.transcribe(audio, batch_size=batch_size, language='en')
        
        # Align
        model_a, metadata = whisperx.load_align_model(language_code="en", device=device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
        
    except RuntimeError as e:
        if "out of memory" in str(e).lower() and device == "cuda":
            print(f"  ⚠ OOM with batch_size={batch_size}, retrying with batch_size=4...")

            # Clear memory and retry - now using gentle cleanup
            if model is not None:
                del model
                model = None
            if model_a is not None:
                del model_a
                model_a = None
            cleanup_gpu_memory(force_cpu)  # Clear GPU memory
            time.sleep(3)

            # Retry with smaller batch size
            try:
                print("  → Loading model (retry with batch_size=4)...")
                model = whisperx.load_model(model_name, device, compute_type=compute_type, language="en")
                if audio is None:
                    audio = whisperx.load_audio(audio_path)
                result = model.transcribe(audio, batch_size=4, language='en')

                # Align
                model_a, metadata = whisperx.load_align_model(language_code="en", device=device)
                result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
            except RuntimeError as e2:
                print(f"  ⚠ Still OOM with batch_size=4, retrying with batch_size=1...")
                
                # Clear memory again
                if model is not None:
                    del model
                    model = None
                if model_a is not None:
                    del model_a
                    model_a = None
                cleanup_gpu_memory(force_cpu)
                time.sleep(3)
                
                # Final retry with batch_size=1
                print("  → Loading model (final retry with batch_size=1)...")
                model = whisperx.load_model(model_name, device, compute_type=compute_type, language="en")
                if audio is None:
                    audio = whisperx.load_audio(audio_path)
                result = model.transcribe(audio, batch_size=1, language='en')
                # Align with smaller batch
                model_a, metadata = whisperx.load_align_model(language_code="en", device=device)
                result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
        else:
            raise
    
    # Verify we have a result before proceeding
    if result is None:
        raise RuntimeError("Transcription failed - no result obtained")
    
    # Step 2: Diarize
    print("  → Diarizing...")
    
    # Convert MP3 to WAV if needed
    audio_path_obj = Path(audio_path)
    temp_wav = None
    diarize_path = audio_path
    
    if audio_path_obj.suffix.lower() == '.mp3':
        temp_wav = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
        temp_wav.close()
        
        cmd = ['ffmpeg', '-i', audio_path, '-ar', '16000', '-ac', '1', '-y', temp_wav.name]
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            diarize_path = temp_wav.name
        except subprocess.CalledProcessError:
            if temp_wav:
                os.unlink(temp_wav.name)
            temp_wav = None
    
    try:
        diarize_model = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            token=hf_token
        ).to(torch.device(device))
        
        diarize_segments = diarize_model(diarize_path)
        
        # Step 3: Assign speakers
        print("  → Assigning speakers...")
        annotation = diarize_segments.speaker_diarization
        
        diarize_list = []
        for segment, _, speaker in annotation.itertracks(yield_label=True):
            diarize_list.append({
                'start': segment.start,
                'end': segment.end,
                'speaker': speaker
            })
        
        diarize_df = pd.DataFrame(diarize_list)
        result_with_speakers = whisperx.assign_word_speakers(diarize_df, result)
        
        # Count speakers
        speakers = set()
        for segment in result_with_speakers["segments"]:
            if "speaker" in segment:
                speakers.add(segment["speaker"])
        
        print(f"  → Detected {len(speakers)} speakers")
        
        # Step 4: Save using utility function
        output_path = save_transcript_files(
            output_dir,
            audio_path_obj.stem,
            "whisperx",
            result_with_speakers["segments"]
        )
        
        elapsed = time.time() - start
        print(f"  → Completed in {elapsed:.1f}s ({elapsed/60:.1f} min)")
        
        # Clean up GPU memory after transcription (gentle cleanup)
        print("  → Cleaning up GPU memory...")
        cleanup_gpu_memory(force_cpu)
        
        return output_path
        
    finally:
        if temp_wav and os.path.exists(temp_wav.name):
            os.unlink(temp_wav.name)


def transcribe_whisperx_cloud(audio_path, output_dir):
    """WhisperX cloud transcription via Replicate with speaker diarization"""
    import replicate
    import time
    import json
    from pathlib import Path
    
    api_token = os.environ.get('REPLICATE_API_TOKEN')
    if not api_token:
        raise ValueError("REPLICATE_API_TOKEN environment variable not set")
    
    audio_path_obj = Path(audio_path)
    
    print(f"  Uploading and transcribing via Replicate...")
    print(f"  Model: WhisperX Large-v3")
    
    start_time = time.time()
    
    try:
        # Run WhisperX on Replicate - uses WhisperX + Pyannote diarization from Replicate model
        prediction = replicate.run(
            "victor-upmeet/whisperx:84d2ad2d6194fe98a17d2b60bef1c7f910c46b2f6fd38996ca457afd9c8abfcb",
            input={
                "audio_file": open(audio_path, "rb"),  # File upload for WhisperX + Pyannote diarization
                "model": "large-v3",
                "language": "en",
                "diarization": True,
                "huggingface_access_token": os.environ.get('HF_TOKEN', ''),
                "batch_size": 8
            }
        )
        
        elapsed = time.time() - start_time
        print(f"  Transcribed in {elapsed:.1f}s")

        # Debug: Print prediction to understand format
        print(f"Debug prediction type: {type(prediction)}")
        print(f"Debug prediction sample: {str(prediction)[:500]}...")
        # Additional debug
        print(f"Full prediction: {prediction}")

        # Parse the output
        segments = []

        # Assuming prediction is a dict with 'segments' list
        pred_segments = prediction.get('segments', [])

        if pred_segments:
            for seg in pred_segments:
                start = float(seg.get('start', 0))
                end = float(seg.get('end', 0))
                speaker = seg.get('speaker', 'SPEAKER_00')
                if speaker and not speaker.startswith('SPEAKER_'):
                    speaker = f'SPEAKER_{int(speaker):02d}'
                text = seg.get('text', '').strip()

                segments.append({
                    'start': start,
                    'end': end,
                    'speaker': speaker,
                    'text': text
                })

        if not segments:
            raise ValueError("No transcription segments returned from Replicate")
        
        # Count speakers
        speakers = set(seg['speaker'] for seg in segments if seg['speaker'].startswith('SPEAKER_'))
        print(f"  Detected {len(speakers)} speakers")
        
        # Save using utility function (same format as local whisperx)
        output_path = save_transcript_files(
            output_dir,
            audio_path_obj.stem,
            "whisperx-cloud",
            segments
        )
        
        return output_path
        
    except Exception as e:
        raise RuntimeError(f"WhisperX Cloud transcription failed: {e}")


def transcribe_assemblyai(audio_path, output_dir):
    """AssemblyAI cloud transcription with speaker diarization"""
    import time
    import assemblyai as aai
    
    api_key = os.environ.get('ASSEMBLYAI_API_KEY')
    if not api_key:
        raise ValueError("ASSEMBLYAI_API_KEY environment variable not set")
    
    aai.settings.api_key = api_key
    audio_file_path = Path(audio_path)
    
    # Load custom vocabulary (people names + technical terms)
    custom_vocab = load_vocabulary()
    print(f"  Loaded {len(custom_vocab)} custom terms")
    
    print(f"  Uploading and transcribing...")
    
    config = aai.TranscriptionConfig(
        speaker_labels=True,
        speakers_expected=None,
        format_text=True,  # Auto-format for readability
        punctuate=True,
        disfluencies=False,  # Remove filler words (um, uh, etc.)
        word_boost=custom_vocab,  # Boost accuracy for Ethereum people/terms
        boost_param='high'  # Aggressively boost custom vocabulary
    )
    
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(str(audio_file_path), config=config)
    
    print(f"  Processing...")
    while transcript.status not in [aai.TranscriptStatus.completed, aai.TranscriptStatus.error]:
        time.sleep(5)
    
    if transcript.status == aai.TranscriptStatus.error:
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    
    # Format output - build sentences like WhisperX WITH timestamps
    output_lines = []
    current_speaker = None
    
    if transcript.utterances:
        for utterance in transcript.utterances:
            speaker_num = ord(utterance.speaker) - ord('A')
            speaker_label = f"SPEAKER_{speaker_num:02d}"
            start_time = utterance.start / 1000.0  # Convert ms to seconds
            
            if speaker_label != current_speaker:
                if output_lines:
                    output_lines.append('')
                output_lines.append(f'{speaker_label}:')
                current_speaker = speaker_label
            
            # Split text into sentences
            text = utterance.text.strip()
            import re
            sentences = re.split(r'([.!?])\s+', text)
            
            # Rejoin punctuation with sentences and add timestamps
            current_sentence = ''
            for i, part in enumerate(sentences):
                if part in '.!?':
                    current_sentence += part
                    if current_sentence.strip():
                        # Add timestamp to sentence
                        output_lines.append(f'[{start_time:.1f}s] {current_sentence.strip()}')
                    current_sentence = ''
                elif part.strip():
                    current_sentence += part + ' '
            
            # Add any remaining text with timestamp
            if current_sentence.strip():
                output_lines.append(f'[{start_time:.1f}s] {current_sentence.strip()}')
    else:
        output_lines.append('SPEAKER_00:')
        output_lines.append('[0.0s] ' + transcript.text)
    
    # Count speakers
    num_speakers = len(set(utterance.speaker for utterance in transcript.utterances)) if transcript.utterances else 1
    print(f"  Detected {num_speakers} speakers")

    # Save word-level timing data as JSON for precise subtitle alignment
    import json
    if transcript.words:
        word_data = []
        for word in transcript.words:
            word_data.append({
                'text': word.text,
                'start': word.start / 1000.0,  # Convert ms to seconds
                'end': word.end / 1000.0,
                'speaker': f"SPEAKER_{ord(word.speaker) - ord('A'):02d}" if hasattr(word, 'speaker') and word.speaker else None
            })

        # Create output directory, but avoid nesting if output_dir already ends with basename
        output_dir_path = Path(output_dir)
        if output_dir_path.name == audio_file_path.stem:
            output_path = output_dir_path
        else:
            output_path = output_dir_path / audio_file_path.stem
        output_path.mkdir(parents=True, exist_ok=True)

        json_path = output_path / f"{audio_file_path.stem}_assemblyai_words.json"
        with open(json_path, 'w') as f:
            json.dump(word_data, f, indent=2)
        print(f"  Saved word-level timing: {json_path}")

    # Save using utility function
    formatted_text = '\n'.join(output_lines) + '\n'
    return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "assemblyai", formatted_text)


if __name__ == "__main__":
    main()
