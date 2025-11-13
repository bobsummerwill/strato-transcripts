#!/usr/bin/env python3
"""
Unified transcription script with speaker diarization
Supports multiple providers: WhisperX (local), Deepgram, AssemblyAI, Rev.ai
All providers include speaker diarization support.
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

def validate_api_key(env_var):
    """
    Check if API key environment variable is set.
    
    Args:
        env_var: Name of environment variable to check
    
    Returns:
        Tuple of (key, error_message). If key exists, error_message is None.
        If key missing, key is None and error_message describes the issue.
    """
    key = os.environ.get(env_var, '').strip()
    if not key:
        return None, f"{env_var} not set"
    return key, None


def save_transcript_files(output_dir, basename, service_name, segments, speaker_key="speaker"):
    """
    Save transcript in both txt and md formats with consistent naming.
    TXT format: No timestamps (clean text only)
    MD format: With timestamps for reference
    
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
    
    # Save text version (NO timestamps)
    with open(output_path, 'w', encoding='utf-8') as f:
        current_speaker = None
        for segment in segments:
            speaker = segment.get(speaker_key, "UNKNOWN")
            if speaker != current_speaker:
                f.write(f"\n{speaker}:\n")
                current_speaker = speaker
            text = segment.get("text", "").strip()
            f.write(f"{text}\n")
    
    # Save markdown version (WITH timestamps)
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
    TXT format: No timestamps (clean text only)
    MD format: With timestamps for reference
    
    Args:
        output_dir: Directory to save files
        basename: Base filename without extension
        service_name: Name of transcription service
        formatted_text: Pre-formatted text with speaker labels and timestamps
    
    Returns:
        Path object for the .txt file
    """
    import re
    
    output_path = Path(output_dir) / f"{basename}_{service_name}_raw.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save text version (NO timestamps)
    # Strip timestamps like [150.9s] from beginning of lines
    text_lines = []
    for line in formatted_text.split('\n'):
        # Remove timestamp pattern [XXX.Xs] at start of line
        clean_line = re.sub(r'^\[[\d.]+s\] ', '', line)
        text_lines.append(clean_line)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_lines))
    
    # Save markdown version (WITH timestamps, convert SPEAKER_ labels to bold)
    md_path = output_path.with_suffix('.md')
    md_lines = []
    for line in formatted_text.split('\n'):
        # Bold speaker labels: SPEAKER_XX: becomes **SPEAKER_XX:**
        if re.match(r'^SPEAKER_\d+:', line):
            line = line.replace('SPEAKER_', '**SPEAKER_').replace(':', ':**', 1)
        md_lines.append(line)
    md_content = '\n'.join(md_lines)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return output_path


def load_custom_vocabulary():
    """Load Ethereum-specific vocabulary from files for transcription services."""
    vocab = []
    
    # Load technical terms
    terms_file = Path("intermediates/ethereum_technical_terms.txt")
    if terms_file.exists():
        with open(terms_file, 'r', encoding='utf-8') as f:
            vocab.extend([line.strip() for line in f if line.strip()])
    
    # Load people names
    people_file = Path("intermediates/ethereum_people.txt")
    if people_file.exists():
        with open(people_file, 'r', encoding='utf-8') as f:
            vocab.extend([line.strip() for line in f if line.strip()])
    
    return vocab


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
        help="Comma-separated list of transcription services (whisperx,deepgram,assemblyai,revai)"
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
    valid_transcribers = {'whisperx', 'deepgram', 'assemblyai', 'revai'}
    
    for transcriber in transcribers:
        if transcriber not in valid_transcribers:
            print(f"Error: Unknown transcriber '{transcriber}'")
            print(f"Valid options: {', '.join(sorted(valid_transcribers))}")
            sys.exit(1)
    
    # Clean up any dangling Ollama processes at startup
    # This prevents GPU memory issues with WhisperX when Ollama is left running
    try:
        import subprocess
        import requests
        
        # Check if Ollama is running
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=1)
            if response.status_code == 200:
                print("Stopping dangling Ollama process...")
                subprocess.run(['pkill', '-f', 'ollama serve'], 
                             stdout=subprocess.DEVNULL, 
                             stderr=subprocess.DEVNULL,
                             timeout=5)
                time.sleep(2)  # Give it time to stop
                print("✓ Cleared")
        except:
            pass  # Not running, nothing to clean up
    except Exception as e:
        # Non-fatal if cleanup fails
        print(f"⚠ Warning: Could not clean up dangling processes: {e}")
    
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
        if transcriber == 'deepgram':
            _, skip_reason = validate_api_key('DEEPGRAM_API_KEY')
        elif transcriber == 'assemblyai':
            _, skip_reason = validate_api_key('ASSEMBLYAI_API_KEY')
        elif transcriber == 'revai':
            _, skip_reason = validate_api_key('REVAI_API_KEY')
        elif transcriber == 'whisperx':
            _, skip_reason = validate_api_key('HF_TOKEN')
        
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
            elif transcriber == 'revai':
                output_path = transcribe_revai(str(audio_path), args.output_dir)
            
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
    
    print(f"  Model: Nova-3 General")
    print(f"  Uploading and transcribing...")
    
    deepgram = DeepgramClient(api_key=api_key)
    
    with open(audio_file_path, 'rb') as audio_file:
        buffer_data = audio_file.read()
    
    start_time = time.time()
    
    # Load custom vocabulary (people names + technical terms)
    custom_vocab = load_custom_vocabulary()
    print(f"  Loaded {len(custom_vocab)} custom terms")
    
    # Model: nova-3-general (updated 2025-11-10)
    # Best accuracy for multi-speaker conversations and technical content
    # utterances=True: Returns transcript organized by speaker turns (continuous speech segments)
    #                  Each utterance = one speaker's uninterrupted speech with timestamps
    #                  This is how we get clean speaker separation
    response = deepgram.listen.v1.media.transcribe_file(
        request=buffer_data,
        model="nova-3-general",
        smart_format=True,
        diarize=True,
        punctuate=True,
        paragraphs=True,
        utterances=True,  # Returns speaker turns (see comment above)
        filler_words=False,  # Don't include filler words in transcript
        # Boost accuracy for Ethereum people/terms from vocabulary files
        # Deepgram may limit array size, using first 100 items
        keyterm=custom_vocab[:100],
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
    
    # Reformat to WhisperX style - split text into proper sentences WITH timestamps
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
            
            # Split text into sentences
            sentences = re.split(r'([.!?])\s+', text)
            
            # Rejoin punctuation with sentences and add timestamps
            current_sentence = ''
            for part in sentences:
                if part in '.!?':
                    current_sentence += part
                    if current_sentence.strip():
                        output_lines.append(f'[{timestamp}s] {current_sentence.strip()}')
                    current_sentence = ''
                elif part.strip():
                    current_sentence += part + ' '
            
            # Add any remaining text with timestamp
            if current_sentence.strip():
                output_lines.append(f'[{timestamp}s] {current_sentence.strip()}')
    
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
    
    # Load custom vocabulary (people names + technical terms)
    custom_vocab = load_custom_vocabulary()
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
    
    # Save using utility function
    formatted_text = '\n'.join(output_lines) + '\n'
    return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "assemblyai", formatted_text)


def transcribe_revai(audio_path, output_dir):
    """Rev.ai v3 cloud transcription with speaker diarization"""
    import time
    import requests
    import json
    
    api_key = os.environ.get('REVAI_API_KEY')
    if not api_key:
        raise ValueError("REVAI_API_KEY environment variable not set")
    
    audio_file_path = Path(audio_path)
    
    print(f"  Model: Rev.ai v3 Human")
    print(f"  Uploading and transcribing...")
    
    # Submit job with speaker diarization
    # Note: Not using custom vocabulary due to API limitations
    headers = {'Authorization': f'Bearer {api_key}'}
    
    with open(audio_file_path, 'rb') as f:
        files = {'media': (audio_file_path.name, f, 'audio/mpeg')}
        data = {
            'options': json.dumps({
                'language': 'en',
                'speaker_channels_count': None,  # Auto-detect speakers
                'remove_disfluencies': True,  # Remove filler words (um, uh, etc.)
                'filter_profanity': False
            })
        }
        
        response = requests.post(
            'https://api.rev.ai/speechtotext/v1/jobs',
            headers=headers,
            files=files,
            data=data
        )
        response.raise_for_status()
        job_id = response.json()['id']
    
    print(f"  Transcribing (Job ID: {job_id})...")
    
    # Poll for completion
    start_time = time.time()
    while True:
        response = requests.get(
            f'https://api.rev.ai/speechtotext/v1/jobs/{job_id}',
            headers=headers
        )
        response.raise_for_status()
        job_data = response.json()
        status = job_data['status']
        
        if status == 'transcribed':
            break
        elif status == 'failed':
            raise RuntimeError(f"Rev.ai transcription failed: {job_data.get('failure', 'Unknown error')}")
        
        time.sleep(5)
    
    elapsed = time.time() - start_time
    print(f"  Transcribed in {elapsed:.1f}s")
    
    # Get transcript in text format with timestamps and speaker labels
    response = requests.get(
        f'https://api.rev.ai/speechtotext/v1/jobs/{job_id}/transcript',
        headers={**headers, 'Accept': 'application/vnd.rev.transcript.v1.0+json'}
    )
    response.raise_for_status()
    transcript_data = response.json()
    
    # Format output - build sentences from words like WhisperX WITH timestamps
    output_lines = []
    current_speaker = None
    
    # Rev.ai returns monologues (continuous speech segments by one speaker)
    for monologue in transcript_data.get('monologues', []):
        speaker_num = monologue.get('speaker', 0)
        speaker_label = f"SPEAKER_{speaker_num:02d}"
        
        if speaker_label != current_speaker:
            if output_lines:
                output_lines.append('')
            output_lines.append(f'{speaker_label}:')
            current_speaker = speaker_label
        
        # Build sentences from words and punctuation
        current_sentence = []
        sentence_start_time = None
        
        for element in monologue.get('elements', []):
            if element.get('type') == 'text':
                value = element.get('value', '').strip()
                if value:
                    if sentence_start_time is None:
                        sentence_start_time = element.get('ts', 0)
                    current_sentence.append(value)
                    
                    # End sentence on period, question mark, or exclamation
                    if value.endswith(('.', '?', '!')):
                        sentence = ' '.join(current_sentence)
                        # Include timestamp for MD version
                        output_lines.append(f'[{sentence_start_time:.1f}s] {sentence}')
                        current_sentence = []
                        sentence_start_time = None
        
        # Add any remaining words as a sentence
        if current_sentence:
            sentence = ' '.join(current_sentence)
            if sentence_start_time is not None:
                output_lines.append(f'[{sentence_start_time:.1f}s] {sentence}')
            else:
                output_lines.append(sentence)
    
    # Count speakers
    speakers = set(f"SPEAKER_{m.get('speaker', 0):02d}" for m in transcript_data.get('monologues', []))
    print(f"  Detected {len(speakers)} speakers")
    
    formatted_text = '\n'.join(output_lines) + '\n'
    return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "revai", formatted_text)



if __name__ == "__main__":
    main()
