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
                    load_vocabulary, cleanup_gpu_memory,
                    ensure_nvidia_lib_path)


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
    Save transcript as markdown with timestamps.
    Consecutive segments from the same speaker are merged into paragraphs.
    Format: **[MM:SS] SPEAKER_XX:** text

    Args:
        output_dir: Directory to save files
        basename: Base filename without extension
        service_name: Name of transcription service (whisperx, deepgram, etc.)
        segments: List of segment dicts with 'speaker', 'start', 'text' keys
        speaker_key: Key name for speaker in segments (default: 'speaker')

    Returns:
        Path object for the .md file
    """
    # Create episode-specific subdirectory, but avoid nesting if output_dir already ends with basename
    output_dir_path = Path(output_dir)
    if output_dir_path.name == basename:
        episode_dir = output_dir_path
    else:
        episode_dir = output_dir_path / basename
    episode_dir.mkdir(parents=True, exist_ok=True)
    
    # Merge consecutive segments from same speaker into paragraphs
    merged_segments = merge_consecutive_speaker_segments(segments, speaker_key)
    
    # Save markdown version (WITH timestamps)
    # Format: **[MM:SS] SPEAKER_XX:** text
    md_path = episode_dir / f"{basename}_{service_name}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        for segment in merged_segments:
            speaker = segment['speaker']
            start_time = segment['start']
            text = clean_text(segment['text'])
            timestamp = format_timestamp(start_time)
            if text:
                f.write(f"**[{timestamp}] {speaker}:** {text}\n\n")
    
    return md_path


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
    Save pre-formatted transcript text as markdown with timestamps.
    Consecutive segments from the same speaker are merged into paragraphs.
    Format: **[MM:SS] SPEAKER_XX:** text

    Args:
        output_dir: Directory to save files
        basename: Base filename without extension
        service_name: Name of transcription service
        formatted_text: Pre-formatted text with speaker labels and timestamps
                       Format: "SPEAKER_XX:\n[123.4s] text\n[125.0s] more text\n"

    Returns:
        Path object for the .md file
    """
    import re

    # Create episode-specific subdirectory, but avoid nesting if output_dir already ends with basename
    output_dir_path = Path(output_dir)
    if output_dir_path.name == basename:
        episode_dir = output_dir_path
    else:
        episode_dir = output_dir_path / basename
    episode_dir.mkdir(parents=True, exist_ok=True)
    
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
    
    # Save markdown version (WITH timestamps)
    # Format: **[MM:SS] SPEAKER_XX:** text
    md_path = episode_dir / f"{basename}_{service_name}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        for segment in merged_segments:
            timestamp = format_timestamp(segment['start'])
            text = clean_text(segment['text'])
            f.write(f"**[{timestamp}] {segment['speaker']}:** {text}\n\n")
    
    return md_path


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
    parser.add_argument("--force", action="store_true", help="Reprocess even if output exists")
    parser.add_argument("--force-cpu", action="store_true", help="Force CPU for WhisperX (disables GPU)")
    parser.add_argument("--consensus", action="store_true",
                        help="Consensus mode: keep ALL words (ums, ahs) and save word-level JSON for alignment")
    
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
                    args.force_cpu,
                    consensus_mode=args.consensus
                )
            elif transcriber == 'whisperx-cloud':
                output_path = transcribe_whisperx_cloud(str(audio_path), args.output_dir, consensus_mode=args.consensus)
            elif transcriber == 'assemblyai':
                output_path = transcribe_assemblyai(str(audio_path), args.output_dir, consensus_mode=args.consensus)
            
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


def transcribe_whisperx(audio_path, output_dir, force_cpu=False, consensus_mode=False):
    """WhisperX local transcription with speaker diarization

    Args:
        consensus_mode: If True, saves word-level JSON for alignment. If False (default),
                       only saves cleaned transcript without JSON.
    """
    import time
    import subprocess
    import tempfile
    import warnings
    import pandas as pd
    import gc

    # CUDA library path setup for pip-installed NVIDIA packages
    ensure_nvidia_lib_path()

    # ========================================================================
    # CRITICAL: Apply PyTorch patches BEFORE importing whisperx/pyannote
    # These libraries load model checkpoints on import, so patches must be first
    # ========================================================================
    import torch
    from packaging.version import Version
    torch_version = Version(torch.__version__.split("+")[0])

    # PyTorch 2.6+ changed weights_only default to True, breaking pyannote checkpoints
    if torch_version >= Version("2.6.0") and not hasattr(torch, '_whisperx_patched'):
        _orig_torch_load = torch.load
        def _torch_load_compat(*args, **kwargs):
            kwargs["weights_only"] = False
            return _orig_torch_load(*args, **kwargs)
        torch.load = _torch_load_compat
        torch._whisperx_patched = True
        print("  ⚠ PyTorch>=2.6: patched torch.load for pyannote compatibility")

    # TF32 settings - PyTorch 2.9+ uses new API
    if torch_version >= Version("2.9.0"):
        torch.backends.cudnn.conv.fp32_precision = 'tf32'
        torch.backends.cuda.matmul.fp32_precision = 'tf32'
    else:
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True

    # NOW import whisperx/pyannote (after patches applied)
    import whisperx
    from pyannote.audio import Pipeline

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
        
        # NOTE: We skip whisperx.align() entirely. Alignment drops most segments
        # on some audio files and produces hallucinated filler text ("you", "Thank you").
        # Since we now use segment-level speaker matching (not word-level), alignment
        # is unnecessary. Raw transcription segments have correct timestamps already.
        
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
                # Skip alignment (see note above)
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
                # Skip alignment (see note above)
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
        
        # Step 3: Assign speakers via segment-level overlap
        # NOTE: We skip whisperx.assign_word_speakers() because it corrupts text
        # by replacing words with '!!!' during word-level speaker reconstruction.
        # Instead, we match each transcript segment to the diarization speaker
        # with the most temporal overlap. This preserves the original text perfectly.
        print("  → Assigning speakers (segment-level matching)...")
        
        # Extract annotation from pipeline output (may be wrapped in DiarizeOutput)
        if hasattr(diarize_segments, 'speaker_diarization'):
            annotation = diarize_segments.speaker_diarization
        elif hasattr(diarize_segments, 'itertracks'):
            annotation = diarize_segments
        else:
            # Try treating it as a dict-like
            annotation = diarize_segments.get('diarization', diarize_segments)
        
        diarize_list = []
        for segment, _, speaker in annotation.itertracks(yield_label=True):
            diarize_list.append({
                'start': segment.start,
                'end': segment.end,
                'speaker': speaker
            })
        
        # Assign speaker to each transcript segment by max overlap
        for seg in result["segments"]:
            seg_start = seg.get("start", 0)
            seg_end = seg.get("end", 0)
            best_speaker = "SPEAKER_00"
            best_overlap = 0
            for d in diarize_list:
                overlap = min(seg_end, d["end"]) - max(seg_start, d["start"])
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_speaker = d["speaker"]
            seg["speaker"] = best_speaker
        
        result_with_speakers = result
        
        # Count speakers
        speakers = set()
        for segment in result_with_speakers["segments"]:
            if "speaker" in segment:
                speakers.add(segment["speaker"])
        
        print(f"  → Detected {len(speakers)} speakers")

        # Create output directory (avoid nesting if output_dir already ends with episode name)
        output_dir_path = Path(output_dir)
        if output_dir_path.name == audio_path_obj.stem:
            episode_dir = output_dir_path
        else:
            episode_dir = output_dir_path / audio_path_obj.stem
        episode_dir.mkdir(parents=True, exist_ok=True)

        if consensus_mode:
            # Consensus mode: save BOTH word-level JSON AND md/txt transcripts
            import json
            word_data = []
            for segment in result_with_speakers["segments"]:
                speaker = segment.get("speaker", "UNKNOWN")
                # WhisperX provides word-level timing in the "words" field
                if "words" in segment:
                    for word in segment["words"]:
                        word_data.append({
                            'text': word.get('word', ''),
                            'start': word.get('start', 0),
                            'end': word.get('end', 0),
                            'speaker': speaker
                        })

            if word_data:
                json_path = episode_dir / f"{audio_path_obj.stem}_whisperx_consensus_words.json"
                with open(json_path, 'w') as f:
                    json.dump(word_data, f, indent=2)
                print(f"  → Saved consensus word-level data: {json_path}")
            else:
                raise RuntimeError("No word-level data available for consensus")

            # Save consensus transcripts with _consensus suffix to avoid overwriting clean transcripts
            output_path = save_transcript_files(
                output_dir,
                audio_path_obj.stem,
                "whisperx_consensus",
                result_with_speakers["segments"]
            )
        else:
            # Normal mode: save md/txt transcripts (no JSON)
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


def transcribe_whisperx_cloud(audio_path, output_dir, consensus_mode=False):
    """Cloud transcription via Replicate with speaker diarization and word-level timestamps.

    Uses thomasmol/whisper-diarization which provides Whisper Large V3 Turbo with
    word-level and sentence-level timestamps plus speaker diarization via Pyannote.

    Args:
        consensus_mode: If True, saves word-level JSON for alignment. If False (default),
                       only saves cleaned transcript without JSON.
    """
    import replicate
    import time
    import json
    from pathlib import Path

    api_token = os.environ.get('REPLICATE_API_TOKEN')
    if not api_token:
        raise ValueError("REPLICATE_API_TOKEN environment variable not set")

    audio_path_obj = Path(audio_path)

    # Load custom vocabulary for the prompt (improves accuracy for technical terms)
    custom_terms_path = Path(__file__).parent.parent / 'custom_terms.txt'
    prompt_vocab = ''
    if custom_terms_path.exists():
        with open(custom_terms_path) as f:
            terms = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        if terms:
            prompt_vocab = ', '.join(terms[:50])  # Limit to avoid overly long prompts

    print(f"  Uploading and transcribing via Replicate...")
    print(f"  Model: Whisper Large V3 Turbo + Pyannote diarization (thomasmol/whisper-diarization)")

    start_time = time.time()

    try:
        input_params = {
            'file': open(audio_path, 'rb'),
            'language': 'en',
            'group_segments': True,
        }
        if prompt_vocab:
            input_params['prompt'] = prompt_vocab

        prediction = replicate.run(
            "thomasmol/whisper-diarization:1495a9cddc83b2203b0d8d3516e38b80fd1572ebc4bc5700ac1da56a9b3ed886",
            input=input_params,
        )

        elapsed = time.time() - start_time
        print(f"  Transcribed in {elapsed:.1f}s")

        pred_segments = prediction.get('segments', [])
        if not pred_segments:
            raise ValueError("No transcription segments returned from Replicate")

        # Build segment list for transcript output
        segments = []
        for seg in pred_segments:
            start = float(seg.get('start', 0))
            end = float(seg.get('end', 0))
            speaker = seg.get('speaker', 'SPEAKER_00')
            if speaker and not speaker.startswith('SPEAKER_'):
                try:
                    speaker = f'SPEAKER_{int(speaker):02d}'
                except (ValueError, TypeError):
                    speaker = 'SPEAKER_UNKNOWN'
            text = seg.get('text', '').strip()
            segments.append({
                'start': start,
                'end': end,
                'speaker': speaker,
                'text': text,
            })

        speakers = set(seg['speaker'] for seg in segments if seg['speaker'].startswith('SPEAKER_'))
        print(f"  Detected {len(speakers)} speakers")

        # Create output directory (avoid nesting if output_dir already ends with episode name)
        output_dir_path = Path(output_dir)
        if output_dir_path.name == audio_path_obj.stem:
            episode_dir = output_dir_path
        else:
            episode_dir = output_dir_path / audio_path_obj.stem
        episode_dir.mkdir(parents=True, exist_ok=True)

        if consensus_mode:
            # Consensus mode: save word-level JSON AND md/txt transcripts
            word_data = []
            for seg in pred_segments:
                seg_speaker = seg.get('speaker', 'SPEAKER_00')
                if seg_speaker and not seg_speaker.startswith('SPEAKER_'):
                    try:
                        seg_speaker = f'SPEAKER_{int(seg_speaker):02d}'
                    except (ValueError, TypeError):
                        seg_speaker = 'SPEAKER_UNKNOWN'

                if 'words' in seg:
                    for word in seg['words']:
                        # Each word has its own speaker label from diarization
                        word_speaker = word.get('speaker', seg_speaker)
                        if word_speaker and not word_speaker.startswith('SPEAKER_'):
                            try:
                                word_speaker = f'SPEAKER_{int(word_speaker):02d}'
                            except (ValueError, TypeError):
                                word_speaker = 'SPEAKER_UNKNOWN'
                        word_data.append({
                            'text': word.get('word', word.get('text', '')),
                            'start': float(word.get('start', 0)),
                            'end': float(word.get('end', 0)),
                            'speaker': word_speaker,
                        })

            if word_data:
                json_path = episode_dir / f"{audio_path_obj.stem}_whisperx-cloud_consensus_words.json"
                with open(json_path, 'w') as f:
                    json.dump(word_data, f, indent=2)
                print(f"  Saved consensus word-level data: {json_path}")
            else:
                raise RuntimeError("No word-level timing available from Replicate model for consensus")

            output_path = save_transcript_files(
                output_dir,
                audio_path_obj.stem,
                "whisperx-cloud_consensus",
                segments,
            )
        else:
            output_path = save_transcript_files(
                output_dir,
                audio_path_obj.stem,
                "whisperx-cloud",
                segments,
            )

        return output_path

    except Exception as e:
        raise RuntimeError(f"WhisperX Cloud transcription failed: {e}")


def transcribe_assemblyai(audio_path, output_dir, consensus_mode=False):
    """AssemblyAI cloud transcription with speaker diarization

    Args:
        consensus_mode: If True, keeps disfluencies (um, uh) and saves word-level JSON.
                       If False (default), removes disfluencies and skips JSON.
    """
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
    
    # In consensus mode, keep disfluencies (um, uh) for raw word alignment
    config = aai.TranscriptionConfig(
        speaker_labels=True,
        speakers_expected=None,
        format_text=True,  # Auto-format for readability
        punctuate=True,
        disfluencies=consensus_mode,  # Keep filler words only in consensus mode
        word_boost=custom_vocab,  # Boost accuracy for Ethereum people/terms
        boost_param='high'  # Aggressively boost custom vocabulary
    )

    if consensus_mode:
        print("  Consensus mode: keeping disfluencies (um, uh, etc.)")
    
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

    # Create output directory
    output_dir_path = Path(output_dir)
    if output_dir_path.name == audio_file_path.stem:
        episode_dir = output_dir_path
    else:
        episode_dir = output_dir_path / audio_file_path.stem
    episode_dir.mkdir(parents=True, exist_ok=True)

    if consensus_mode:
        # Consensus mode: save BOTH word-level JSON AND md/txt transcripts
        if not transcript.words:
            raise RuntimeError("No word-level data available from AssemblyAI for consensus")

        import json
        word_data = []
        for word in transcript.words:
            word_data.append({
                'text': word.text,
                'start': word.start / 1000.0,  # Convert ms to seconds
                'end': word.end / 1000.0,
                'speaker': f"SPEAKER_{ord(word.speaker) - ord('A'):02d}" if hasattr(word, 'speaker') and word.speaker else None
            })

        json_path = episode_dir / f"{audio_file_path.stem}_assemblyai_consensus_words.json"
        with open(json_path, 'w') as f:
            json.dump(word_data, f, indent=2)
        print(f"  Saved consensus word-level data: {json_path}")

        # Save consensus transcripts with _consensus suffix to avoid overwriting clean transcripts
        formatted_text = '\n'.join(output_lines) + '\n'
        md_path = save_raw_transcript_from_text(output_dir, audio_file_path.stem, "assemblyai_consensus", formatted_text)
        return md_path
    else:
        # Normal mode: save md/txt transcripts (no JSON)
        formatted_text = '\n'.join(output_lines) + '\n'
        return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "assemblyai", formatted_text)


if __name__ == "__main__":
    main()
