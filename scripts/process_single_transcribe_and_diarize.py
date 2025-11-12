#!/usr/bin/env python3
"""
Unified transcription script with speaker diarization
Supports multiple providers: WhisperX (local), Deepgram, AssemblyAI, Sonix, Speechmatics
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
        help="Comma-separated list of transcription services (whisperx,deepgram,assemblyai,sonix,speechmatics)"
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
    valid_transcribers = {'whisperx', 'deepgram', 'assemblyai', 'sonix', 'speechmatics', 'novita'}
    
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
        elif transcriber == 'sonix':
            _, skip_reason = validate_api_key('SONIX_API_KEY')
        elif transcriber == 'speechmatics':
            _, skip_reason = validate_api_key('SPEECHMATICS_API_KEY')
        elif transcriber == 'whisperx':
            _, skip_reason = validate_api_key('HF_TOKEN')
        elif transcriber == 'novita':
            _, skip_reason = validate_api_key('NOVITA_API_KEY')
        
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
            elif transcriber == 'sonix':
                output_path = transcribe_sonix(str(audio_path), args.output_dir)
            elif transcriber == 'speechmatics':
                output_path = transcribe_speechmatics(str(audio_path), args.output_dir)
            elif transcriber == 'novita':
                output_path = transcribe_novita(str(audio_path), args.output_dir)
            
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
        filler_words=True,  # Detect filler words (um, uh, ah, etc.)
        # Nova-3 uses 'keyterm' not 'keywords' - boost blockchain/crypto term accuracy
        keyterm=[
            "Ethereum", "Bitcoin", "blockchain", "cryptocurrency", "smart contract",
            "DeFi", "NFT", "token", "wallet", "consensus", "proof of stake",
            "proof of work", "mining", "validator", "gas", "gwei", "wei",
            "Solidity", "EVM", "dApp", "Web3", "MetaMask", "staking"
        ],
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


def transcribe_sonix(audio_path, output_dir):
    """Sonix cloud transcription with speaker diarization and enhanced parameters"""
    import time
    import requests
    import json
    
    api_key = os.environ.get('SONIX_API_KEY')
    if not api_key:
        raise ValueError("SONIX_API_KEY environment variable not set")
    
    audio_file_path = Path(audio_path)
    
    print(f"  Uploading to Sonix with enhanced parameters...")
    print(f"    - Speaker identification enabled")
    print(f"    - Custom blockchain/crypto vocabulary")
    print(f"    - Entity detection enabled")
    print(f"    - Auto punctuation enabled")
    
    # Upload file with enhanced parameters
    headers = {'Authorization': f'Bearer {api_key}'}
    
    with open(audio_file_path, 'rb') as f:
        files = {'file': (audio_file_path.name, f, 'audio/mpeg')}
        data = {
            'language': 'en',
            'name': audio_file_path.stem,
            'enable_speaker_identification': 'true',
            'enable_entity_detection': 'true',
            'enable_auto_punctuation': 'true',
            'profanity_filter': 'false',
            'custom_vocab': ','.join([
                'Ethereum', 'blockchain', 'cryptocurrency', 'Bitcoin',
                'DeFi', 'NFT', 'smart contract', 'dApp', 'Web3',
                'Solidity', 'EVM', 'Geth', 'Whisper', 'Swarm', 'Mist',
                'proof-of-stake', 'proof-of-work', 'consensus',
                'validator', 'mining', 'gas', 'gwei', 'wei',
                'MetaMask', 'wallet', 'token', 'DAO', 'IPFS',
                'ENS', 'layer-2', 'rollup', 'sharding', 'staking',
                'DevCon', 'EthCC', 'testnet', 'mainnet', 'fork',
                'PyEthereum', 'cpp-ethereum', 'go-ethereum'
            ])
        }
        
        response = requests.post(
            'https://api.sonix.ai/v1/media',
            headers=headers,
            files=files,
            data=data
        )
        response.raise_for_status()
        media_id = response.json()['id']
    
    print(f"  Transcribing (ID: {media_id})...")
    
    # Poll for completion
    start_time = time.time()
    while True:
        response = requests.get(
            f'https://api.sonix.ai/v1/media/{media_id}',
            headers=headers
        )
        response.raise_for_status()
        status = response.json()['status']
        
        if status == 'completed':
            break
        elif status == 'failed':
            raise RuntimeError("Sonix transcription failed")
        
        time.sleep(5)
    
    elapsed = time.time() - start_time
    print(f"  Transcribed in {elapsed:.1f}s")
    
    # Get transcript with speakers
    response = requests.get(
        f'https://api.sonix.ai/v1/media/{media_id}/transcript',
        headers=headers
    )
    response.raise_for_status()
    
    # Debug: Check content type and response
    print(f"  Response status: {response.status_code}")
    print(f"  Content-Type: {response.headers.get('Content-Type', 'unknown')}")
    
    try:
        transcript_data = response.json()
    except json.JSONDecodeError as e:
        print(f"  Response text preview: {response.text[:500]}")
        raise RuntimeError(f"Failed to parse Sonix transcript as JSON: {e}")
    
    # Format output
    formatted_lines = []
    current_speaker = None
    output_lines = []
    
    for word in transcript_data.get('words', []):
        speaker = word.get('speaker', 0)
        speaker_label = f"SPEAKER_{speaker:02d}"
        start = word.get('start', 0)
        text = word.get('text', '')
        
        if speaker_label != current_speaker:
            if output_lines:
                output_lines.append('')
            output_lines.append(f'{speaker_label}:')
            current_speaker = speaker_label
        
        formatted_lines.append(f"[{start:.1f}s] {speaker_label}: {text}")
    
    # Count speakers
    speakers = set(word.get('speaker', 0) for word in transcript_data.get('words', []))
    print(f"  Detected {len(speakers)} speakers")
    
    # Reconstruct sentences from words
    # Group consecutive words by speaker
    sentences = []
    current_sentence = []
    current_speaker = None
    current_start = 0
    
    for word in transcript_data.get('words', []):
        speaker = word.get('speaker', 0)
        speaker_label = f"SPEAKER_{speaker:02d}"
        
        if speaker_label != current_speaker:
            if current_sentence:
                sentences.append((current_start, current_speaker, ' '.join(current_sentence)))
            current_sentence = [word.get('text', '')]
            current_speaker = speaker_label
            current_start = word.get('start', 0)
        else:
            current_sentence.append(word.get('text', ''))
    
    if current_sentence:
        sentences.append((current_start, current_speaker, ' '.join(current_sentence)))
    
    # Format final output
    output_lines = []
    last_speaker = None
    for start, speaker, text in sentences:
        if speaker != last_speaker:
            if output_lines:
                output_lines.append('')
            output_lines.append(f'{speaker}:')
            last_speaker = speaker
        output_lines.append(f'[{start:.1f}s] {text}')
    
    formatted_text = '\n'.join(output_lines) + '\n'
    return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "sonix", formatted_text)


def transcribe_speechmatics(audio_path, output_dir):
    """Speechmatics cloud transcription with speaker diarization"""
    import time
    import requests
    import json
    
    api_key = os.environ.get('SPEECHMATICS_API_KEY')
    if not api_key:
        raise ValueError("SPEECHMATICS_API_KEY environment variable not set")
    
    audio_file_path = Path(audio_path)
    
    print(f"  Uploading to Speechmatics...")
    
    # Prepare configuration
    config = {
        "type": "transcription",
        "transcription_config": {
            "language": "en",
            "diarization": "speaker",
            "operating_point": "enhanced"
        }
    }
    
    # Upload and transcribe
    headers = {'Authorization': f'Bearer {api_key}'}
    
    with open(audio_file_path, 'rb') as f:
        files = {
            'data_file': (audio_file_path.name, f, 'audio/mpeg'),
            'config': (None, json.dumps(config), 'application/json')
        }
        
        start_time = time.time()
        response = requests.post(
            'https://asr.api.speechmatics.com/v2/jobs',
            headers=headers,
            files=files
        )
        response.raise_for_status()
        job_id = response.json()['id']
    
    print(f"  Transcribing (Job ID: {job_id})...")
    
    # Poll for completion
    while True:
        response = requests.get(
            f'https://asr.api.speechmatics.com/v2/jobs/{job_id}',
            headers=headers
        )
        response.raise_for_status()
        job_data = response.json()['job']
        
        if job_data['status'] == 'done':
            break
        elif job_data['status'] in ['rejected', 'deleted']:
            raise RuntimeError(f"Speechmatics job {job_data['status']}")
        
        time.sleep(5)
    
    elapsed = time.time() - start_time
    print(f"  Transcribed in {elapsed:.1f}s")
    
    # Get transcript
    response = requests.get(
        f'https://asr.api.speechmatics.com/v2/jobs/{job_id}/transcript?format=json-v2',
        headers=headers
    )
    response.raise_for_status()
    transcript_data = response.json()
    
    # Collect all words with speaker info (Speechmatics returns word-level data)
    words_by_speaker = []
    for result in transcript_data.get('results', []):
        for alternative in result.get('alternatives', []):
            content = alternative.get('content', '').strip()
            if not content:
                continue
                
            speaker = alternative.get('speaker', 'SPEAKER_00')
            start = result.get('start_time', 0)
            word_type = alternative.get('type', 'word')
            
            # Normalize speaker label
            if not speaker.startswith('SPEAKER_'):
                speaker_label = f"SPEAKER_{speaker:02d}" if isinstance(speaker, int) else speaker
            else:
                speaker_label = speaker
            
            words_by_speaker.append({
                'speaker': speaker_label,
                'start': start,
                'content': content,
                'type': word_type
            })
    
    # Group consecutive words by speaker into phrases
    phrases = []
    current_phrase = []
    current_speaker = None
    current_start = 0
    
    for word_data in words_by_speaker:
        speaker = word_data['speaker']
        content = word_data['content']
        start = word_data['start']
        word_type = word_data['type']
        
        # Start new phrase on speaker change
        if speaker != current_speaker:
            if current_phrase:
                phrases.append({
                    'speaker': current_speaker,
                    'start': current_start,
                    'text': ' '.join(current_phrase)
                })
            current_phrase = [content]
            current_speaker = speaker
            current_start = start
        else:
            # Add to current phrase
            # Handle punctuation (don't add space before punctuation)
            if word_type == 'punctuation':
                if current_phrase:
                    current_phrase[-1] = current_phrase[-1] + content
                else:
                    current_phrase.append(content)
            else:
                current_phrase.append(content)
        
        # Break phrases at sentence endings for readability
        if content in ['.', '?', '!'] and len(current_phrase) > 10:
            phrases.append({
                'speaker': current_speaker,
                'start': current_start,
                'text': ' '.join(current_phrase)
            })
            current_phrase = []
            current_start = start
    
    # Add final phrase
    if current_phrase:
        phrases.append({
            'speaker': current_speaker,
            'start': current_start,
            'text': ' '.join(current_phrase)
        })
    
    # Format output
    output_lines = []
    last_speaker = None
    
    for phrase in phrases:
        speaker = phrase['speaker']
        if speaker != last_speaker:
            if output_lines:
                output_lines.append('')
            output_lines.append(f'{speaker}:')
            last_speaker = speaker
        output_lines.append(f'[{phrase["start"]:.1f}s] {phrase["text"]}')
    
    # Count unique speakers
    speakers = set(phrase['speaker'] for phrase in phrases)
    print(f"  Detected {len(speakers)} speakers")
    
    formatted_text = '\n'.join(output_lines) + '\n'
    return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "speechmatics", formatted_text)


def transcribe_novita(audio_path, output_dir):
    """Novita AI transcription with speaker diarization using Qwen2.5-Omni"""
    import time
    import requests
    import json
    
    api_key = os.environ.get('NOVITA_API_KEY')
    if not api_key:
        raise ValueError("NOVITA_API_KEY environment variable not set")
    
    audio_file_path = Path(audio_path)
    
    print(f"  Model: Qwen2.5-Omni")
    print(f"  Uploading and transcribing...")
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    start_time = time.time()
    
    # Read audio file and encode to base64 for API
    import base64
    with open(audio_file_path, 'rb') as f:
        audio_data = base64.b64encode(f.read()).decode('utf-8')
    
    # Novita AI API request
    # Using their audio transcription endpoint with Qwen2.5-Omni model
    payload = {
        "model": "qwen2.5-omni",
        "audio": audio_data,
        "language": "en",
        "enable_speaker_diarization": True,
        "format": "json"
    }
    
    try:
        response = requests.post(
            'https://api.novita.ai/v3/async/audio/transcription',
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        task_id = response.json().get('task_id')
        
        if not task_id:
            raise RuntimeError("No task_id received from Novita AI")
        
        print(f"  Task ID: {task_id}")
        
        # Poll for completion
        while True:
            time.sleep(5)
            status_response = requests.get(
                f'https://api.novita.ai/v3/async/task/{task_id}',
                headers=headers,
                timeout=30
            )
            status_response.raise_for_status()
            status_data = status_response.json()
            
            status = status_data.get('status')
            if status == 'completed':
                elapsed = time.time() - start_time
                print(f"  Transcribed in {elapsed:.1f}s")
                transcript_data = status_data.get('result', {})
                break
            elif status in ['failed', 'cancelled']:
                error_msg = status_data.get('error', 'Unknown error')
                raise RuntimeError(f"Novita AI transcription {status}: {error_msg}")
            elif status not in ['pending', 'processing']:
                raise RuntimeError(f"Unexpected status: {status}")
    
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Novita AI API error: {e}")
    
    # Format output from Novita AI response
    output_lines = []
    current_speaker = None
    
    # Parse transcript data (adjust based on actual Novita AI response format)
    segments = transcript_data.get('segments', [])
    
    if not segments and 'text' in transcript_data:
        # Fallback: no diarization, single speaker
        print("  Warning: No speaker diarization available, using single speaker")
        output_lines.append('SPEAKER_00:')
        output_lines.append('[0.0s] ' + transcript_data['text'])
        speakers_count = 1
    else:
        # Process segments with speaker information
        speakers = set()
        for segment in segments:
            speaker_id = segment.get('speaker', 0)
            speaker_label = f"SPEAKER_{speaker_id:02d}"
            speakers.add(speaker_label)
            
            start = segment.get('start', 0.0)
            text = segment.get('text', '').strip()
            
            if speaker_label != current_speaker:
                if output_lines:
                    output_lines.append('')
                output_lines.append(f'{speaker_label}:')
                current_speaker = speaker_label
            
            output_lines.append(f'[{start:.1f}s] {text}')
        
        speakers_count = len(speakers)
    
    print(f"  Detected {speakers_count} speakers")
    
    # Save using utility function
    formatted_text = '\n'.join(output_lines) + '\n'
    return save_raw_transcript_from_text(output_dir, audio_file_path.stem, "novita", formatted_text)


if __name__ == "__main__":
    main()
