#!/usr/bin/env python3
"""
Unified transcription script with speaker diarization
Supports multiple providers: WhisperX (local), Deepgram, AssemblyAI, OpenAI
"""

import sys
import os
import argparse
import time
from pathlib import Path

# ANSI color codes
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def success(msg):
    return f"{Colors.GREEN}✓{Colors.RESET} {msg}"

def failure(msg):
    return f"{Colors.RED}✗{Colors.RESET} {msg}"

def skip(msg):
    return f"{Colors.YELLOW}⊘{Colors.RESET} {msg}"


# ============================================================================
# Utility Functions
# ============================================================================

def save_transcript_files(output_dir, basename, service_name, segments, speaker_key="speaker"):
    """
    Save transcript in both txt and md formats with consistent naming.
    
    Args:
        output_dir: Directory to save files
        basename: Base filename without extension
        service_name: Name of transcription service (whisperx, deepgram, etc.)
        segments: List of segment dicts with 'speaker', 'start', 'text' keys
        speaker_key: Key name for speaker in segments (default: 'speaker')
    
    Returns:
        Path object for the .txt file
    """
    output_path = Path(output_dir) / f"{basename}_{service_name}_raw.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save text version
    with open(output_path, 'w', encoding='utf-8') as f:
        current_speaker = None
        for segment in segments:
            speaker = segment.get(speaker_key, "UNKNOWN")
            if speaker != current_speaker:
                f.write(f"\n{speaker}:\n")
                current_speaker = speaker
            start_time = segment.get("start", 0)
            text = segment.get("text", "").strip()
            f.write(f"[{start_time:.1f}s] {text}\n")
    
    # Save markdown version
    md_path = output_path.with_suffix('.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        current_speaker = None
        for segment in segments:
            speaker = segment.get(speaker_key, "UNKNOWN")
            if speaker != current_speaker:
                f.write(f"\n**{speaker}:**\n")
                current_speaker = speaker
            start_time = segment.get("start", 0)
            text = segment.get("text", "").strip()
            f.write(f"[{start_time:.1f}s] {text}\n")
    
    return output_path


def save_raw_transcript_from_text(output_dir, basename, service_name, formatted_text):
    """
    Save pre-formatted transcript text in both txt and md formats.
    
    Args:
        output_dir: Directory to save files
        basename: Base filename without extension
        service_name: Name of transcription service
        formatted_text: Pre-formatted text with speaker labels and timestamps
    
    Returns:
        Path object for the .txt file
    """
    output_path = Path(output_dir) / f"{basename}_{service_name}_raw.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save text version
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(formatted_text)
    
    # Save markdown version (convert SPEAKER_ labels to bold)
    md_path = output_path.with_suffix('.md')
    md_content = formatted_text.replace('SPEAKER_', '**SPEAKER_').replace(':', ':**', 1)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
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
        help="Comma-separated list of transcription services (whisperx,deepgram,assemblyai,openai)"
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
    valid_transcribers = {'whisperx', 'deepgram', 'assemblyai', 'openai'}
    
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
        
        # Check API keys
        skip_reason = None
        if transcriber == 'deepgram':
            api_key = os.environ.get('DEEPGRAM_API_KEY', '').strip()
            if not api_key:
                skip_reason = "DEEPGRAM_API_KEY not set"
        elif transcriber == 'assemblyai':
            api_key = os.environ.get('ASSEMBLYAI_API_KEY', '').strip()
            if not api_key:
                skip_reason = "ASSEMBLYAI_API_KEY not set"
        elif transcriber == 'openai':
            api_key = os.environ.get('OPENAI_API_KEY', '').strip()
            if not api_key:
                skip_reason = "OPENAI_API_KEY not set"
        elif transcriber == 'whisperx':
            hf_token = os.environ.get('HF_TOKEN', '').strip()
            if not hf_token:
                skip_reason = "HF_TOKEN not set"
        
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
            elif transcriber == 'deepgram':
                output_path = transcribe_deepgram(str(audio_path), args.output_dir)
            elif transcriber == 'assemblyai':
                output_path = transcribe_assemblyai(str(audio_path), args.output_dir)
            elif transcriber == 'openai':
                output_path = transcribe_openai(str(audio_path), args.output_dir)
            
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
    
    # Suppress pyannote warnings
    warnings.filterwarnings('ignore', category=UserWarning,
                          module='pyannote.audio.utils.reproducibility',
                          message='.*TensorFloat-32.*')
    
    # Configure TF32
    torch.backends.cudnn.conv.fp32_precision = 'tf32'
    torch.backends.cuda.matmul.fp32_precision = 'tf32'
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    
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
    batch_size = 16 if device == "cuda" else 8
    
    print(f"  Device: {device}")
    print(f"  Model: {model_name}")
    print(f"  Compute type: {compute_type}")
    print(f"  Batch size: {batch_size}")
    
    start = time.time()
    
    # Step 1: Transcribe
    print("  → Transcribing...")
    model = whisperx.load_model(model_name, device, compute_type=compute_type, language="en")
    audio = whisperx.load_audio(audio_path)
    result = model.transcribe(audio, batch_size=batch_size, language='en')
    
    # Align
    model_a, metadata = whisperx.load_align_model(language_code="en", device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
    
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
        print(f"  Completed in {elapsed:.1f}s ({elapsed/60:.1f} min)")
        
        return output_path
        
    finally:
        if temp_wav and os.path.exists(temp_wav.name):
            os.unlink(temp_wav.name)


def transcribe_deepgram(audio_path, output_dir):
    """Deepgram cloud transcription with speaker diarization"""
    import time
    import re
    from deepgram import DeepgramClient
    
    api_key = os.environ.get('DEEPGRAM_API_KEY')
    if not api_key:
        raise ValueError("DEEPGRAM_API_KEY environment variable not set")
    
    audio_file_path = Path(audio_path)
    
    print(f"  Model: Nova-2")
    print(f"  Uploading and transcribing...")
    
    deepgram = DeepgramClient(api_key=api_key)
    
    with open(audio_file_path, 'rb') as audio_file:
        buffer_data = audio_file.read()
    
    start_time = time.time()
    
    response = deepgram.listen.v1.media.transcribe_file(
        request=buffer_data,
        model="nova-2",
        smart_format=True,
        diarize=True,
        punctuate=True,
        paragraphs=True,
        utterances=True,
    )
    
    elapsed = time.time() - start_time
    print(f"  Transcribed in {elapsed:.1f}s")
    
    # Format output
    result = response.results
    formatted_lines = []
    
    if hasattr(result, 'utterances') and result.utterances:
        for utterance in result.utterances:
            start = utterance.start
            speaker = int(getattr(utterance, 'speaker', 0))
            text = utterance.transcript.strip()
            speaker_label = f"SPEAKER_{speaker:02d}"
            formatted_lines.append(f"[{start:.1f}s] {speaker_label}: {text}")
    else:
        channels = result.channels
        if channels and channels[0].alternatives:
            alternative = channels[0].alternatives[0]
            text = getattr(alternative, 'transcript', "")
            formatted_lines.append(f"[0.0s] SPEAKER_00: {text}")
    
    # Reformat to WhisperX style
    current_speaker = None
    output_lines = []
    
    for line in formatted_lines:
        match = re.match(r'\[(\d+\.\d+)s\]\s+(SPEAKER_\d+):\s*(.+)', line)
        if match:
            timestamp, speaker, text = match.groups()
            if speaker != current_speaker:
                if output_lines:
                    output_lines.append('')
                output_lines.append(f'{speaker}:')
                current_speaker = speaker
            output_lines.append(f'[{timestamp}s] {text}')
    
    # Count speakers
    speakers = set()
    for line in formatted_lines:
        if "SPEAKER_" in line:
            speaker = line.split("SPEAKER_")[1].split(":")[0]
            speakers.add(speaker)
    
    print(f"  Detected {len(speakers)} speakers")
    
    # Save using utility function
    formatted_text = '\n'.join(output_lines) + '\n'
    return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "deepgram", formatted_text)


def transcribe_assemblyai(audio_path, output_dir):
    """AssemblyAI cloud transcription with speaker diarization"""
    import time
    import assemblyai as aai
    
    api_key = os.environ.get('ASSEMBLYAI_API_KEY')
    if not api_key:
        raise ValueError("ASSEMBLYAI_API_KEY environment variable not set")
    
    aai.settings.api_key = api_key
    audio_file_path = Path(audio_path)
    
    print(f"  Uploading and transcribing...")
    
    config = aai.TranscriptionConfig(
        speaker_labels=True,
        speakers_expected=None
    )
    
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(str(audio_file_path), config=config)
    
    print(f"  Processing...")
    while transcript.status not in [aai.TranscriptStatus.completed, aai.TranscriptStatus.error]:
        time.sleep(5)
    
    if transcript.status == aai.TranscriptStatus.error:
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    
    # Format output
    formatted_lines = []
    
    if transcript.utterances:
        for utterance in transcript.utterances:
            start_time = utterance.start / 1000.0
            speaker_num = ord(utterance.speaker) - ord('A')
            speaker_label = f"SPEAKER_{speaker_num:02d}"
            text = utterance.text.strip()
            formatted_lines.append(f"[{start_time:.1f}s] {speaker_label}: {text}")
    else:
        formatted_lines.append(f"[0.0s] SPEAKER_00: {transcript.text}")
    
    # Count speakers
    num_speakers = len(set(utterance.speaker for utterance in transcript.utterances)) if transcript.utterances else 1
    print(f"  Detected {num_speakers} speakers")
    
    # Save using utility function
    formatted_text = '\n'.join(formatted_lines)
    return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "assemblyai", formatted_text)


def transcribe_openai(audio_path, output_dir):
    """OpenAI cloud transcription (no native diarization)"""
    import subprocess
    from openai import OpenAI
    
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    
    client = OpenAI(api_key=api_key)
    audio_file_path = Path(audio_path)
    
    print(f"  Model: gpt-4o-transcribe")
    
    # Get audio duration
    try:
        result = subprocess.run([
            'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1', str(audio_file_path)
        ], capture_output=True, text=True, check=True)
        total_duration = float(result.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise RuntimeError("Could not determine audio duration. Install ffmpeg.")
    
    print(f"  Duration: {total_duration / 60:.1f} minutes")
    print(f"  Splitting into 15-minute chunks...")
    
    # Calculate chunks
    chunk_duration = 900
    overlap = 10
    chunks = []
    
    chunk_num = 0
    start_time = 0.0
    
    while start_time < total_duration:
        end_time = min(start_time + chunk_duration, total_duration)
        chunks.append((chunk_num, start_time, end_time))
        chunk_num += 1
        start_time = end_time - overlap if end_time < total_duration else total_duration
    
    print(f"  Processing {len(chunks)} chunks...")
    
    # Create temp directory
    temp_dir = Path(output_dir) / "temp_chunks"
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # Process chunks
    all_transcripts = []
    
    for chunk_num, start, end in chunks:
        chunk_file = temp_dir / f"chunk_{chunk_num:03d}.mp3"
        
        print(f"    [{chunk_num + 1}/{len(chunks)}] {start/60:.1f}-{end/60:.1f}min", end=" ")
        
        # Extract chunk
        subprocess.run([
            'ffmpeg', '-i', str(audio_file_path),
            '-ss', str(start), '-t', str(end - start),
            '-c', 'copy', '-y', str(chunk_file)
        ], capture_output=True, check=True)
        
        # Transcribe
        try:
            with open(chunk_file, 'rb') as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="gpt-4o-transcribe",
                    file=audio_file,
                    response_format="json",
                    timestamp_granularities=["segment"]
                )
            
            chunk_lines = []
            if hasattr(transcript, 'segments') and transcript.segments:
                for segment in transcript.segments:
                    absolute_time = start + segment.get('start', 0)
                    text = segment.get('text', '').strip()
                    chunk_lines.append(f"[{absolute_time:.1f}s] SPEAKER_00: {text}")
            else:
                text = transcript.text if hasattr(transcript, 'text') else str(transcript)
                chunk_lines.append(f"[{start:.1f}s] SPEAKER_00: {text}")
            
            all_transcripts.append('\n'.join(chunk_lines))
            print("✓")
            
        except Exception as e:
            print(f"✗ {e}")
            all_transcripts.append(f"[{start:.1f}s] SPEAKER_00: [Error]")
        
        # Cleanup
        chunk_file.unlink(missing_ok=True)
    
    # Cleanup temp directory
    try:
        temp_dir.rmdir()
    except:
        pass
    
    print(f"  Complete ({len(chunks)} chunks stitched)")
    
    # Save using utility function
    formatted = '\n~~~~~~\n'.join(all_transcripts)
    return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "openai", formatted)


if __name__ == "__main__":
    main()
