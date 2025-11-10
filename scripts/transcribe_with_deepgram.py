#!/usr/bin/env python3
"""
Deepgram transcription alternative to WhisperX
Uses Deepgram's Nova-2 model with speaker diarization
Most cost-effective cloud option: ~$0.0043/minute
"""

import os
import sys
from pathlib import Path
import argparse
import time

def transcribe_with_deepgram(audio_path, output_dir="intermediates"):
    """
    Transcribe audio using Deepgram with speaker diarization
    
    Args:
        audio_path: Path to audio file
        output_dir: Where to save transcript
    
    Returns:
        path to transcript file
    """
    try:
        from deepgram import DeepgramClient
    except ImportError:
        print("Error: deepgram-sdk package not installed")
        print("Install with: pip install deepgram-sdk")
        sys.exit(1)
    
    api_key = os.environ.get('DEEPGRAM_API_KEY')
    if not api_key:
        print("Error: DEEPGRAM_API_KEY not set")
        print("Set it with: export DEEPGRAM_API_KEY='your-key'")
        print("Get key from: https://console.deepgram.com/")
        sys.exit(1)
    
    audio_file_path = Path(audio_path)
    
    if not audio_file_path.exists():
        print(f"Error: Audio file not found: {audio_path}")
        sys.exit(1)
    
    file_size_mb = audio_file_path.stat().st_size / 1024 / 1024
    
    print("="*70)
    print("Deepgram Nova-2 Transcription with Speaker Diarization")
    print("="*70)
    print(f"Input: {audio_path}")
    print(f"Model: Nova-2 (latest)")
    print(f"File size: {file_size_mb:.2f} MB")
    print(f"Features: Speaker diarization, word-level timestamps")
    print()
    
    print("Uploading and transcribing...")
    print("(Deepgram processes very quickly - usually < 1 minute)")
    print()
    
    try:
        # Initialize Deepgram client
        deepgram = DeepgramClient(api_key=api_key)
        
        # Read audio file
        with open(audio_file_path, 'rb') as audio_file:
            buffer_data = audio_file.read()
        
        # Start timer
        start_time = time.time()
        
        # Transcribe with options as keyword arguments
        response = deepgram.listen.v1.media.transcribe_file(
            request=buffer_data,
            model="nova-2",
            smart_format=True,
            diarize=True,  # Enable speaker diarization
            punctuate=True,
            paragraphs=True,
            utterances=True,
        )
        
        elapsed = time.time() - start_time
        print(f"✓ Transcription complete in {elapsed:.1f} seconds")
        print()
        
        # Extract results (response is an object, not a dict)
        result = response.results
        channels = result.channels
        
        if not channels or not channels[0].alternatives:
            print("❌ Error: No transcription results returned")
            sys.exit(1)
        
        alternative = channels[0].alternatives[0]
        
        # Format output to match WhisperX style
        formatted_lines = []
        
        # Use utterances if available (better for diarization)
        if hasattr(result, 'utterances') and result.utterances:
            for utterance in result.utterances:
                start_time_sec = utterance.start
                speaker = int(getattr(utterance, 'speaker', 0))
                text = utterance.transcript.strip()
                
                # Format: [time]s SPEAKER_XX: text
                speaker_label = f"SPEAKER_{speaker:02d}"
                formatted_lines.append(f"[{start_time_sec:.1f}s] {speaker_label}: {text}")
        else:
            # Fallback to words with diarization
            words = getattr(alternative, 'words', [])
            if words:
                current_speaker = None
                current_text = []
                current_start = None
                
                for word in words:
                    speaker = int(getattr(word, 'speaker', 0))
                    
                    if speaker != current_speaker:
                        # New speaker, save previous
                        if current_text:
                            speaker_label = f"SPEAKER_{current_speaker:02d}"
                            text = " ".join(current_text)
                            formatted_lines.append(f"[{current_start:.1f}s] {speaker_label}: {text}")
                        
                        # Start new speaker segment
                        current_speaker = speaker
                        current_text = [word.word]
                        current_start = word.start
                    else:
                        current_text.append(word.word)
                
                # Save last segment
                if current_text:
                    speaker_label = f"SPEAKER_{current_speaker:02d}"
                    text = " ".join(current_text)
                    formatted_lines.append(f"[{current_start:.1f}s] {speaker_label}: {text}")
            else:
                # Ultimate fallback
                text = getattr(alternative, 'transcript', "")
                formatted_lines.append(f"[0.0s] SPEAKER_00: {text}")
        
        formatted = '\n'.join(formatted_lines)
        
        # Save to intermediates/ with _deepgram suffix
        original_stem = Path(audio_path).stem
        output_path = Path(output_dir) / f"{original_stem}_deepgram_transcript_with_speakers.txt"
        output_path.parent.mkdir(exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(formatted)
        
        # Also save markdown version
        md_path = output_path.with_suffix('.md')
        md_content = formatted.replace('SPEAKER_', '**SPEAKER_').replace(': ', ':** ')
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Saved transcript: {output_path}")
        print(f"Saved markdown: {md_path}")
        print()
        
        # Stats
        char_count = len(formatted)
        line_count = len(formatted_lines)
        
        # Get metadata
        metadata = getattr(result, 'metadata', None)
        duration_seconds = getattr(metadata, 'duration', 0) if metadata else 0
        duration_minutes = duration_seconds / 60.0 if duration_seconds else 0
        
        # Count unique speakers
        speakers = set()
        for line in formatted_lines:
            if "SPEAKER_" in line:
                speaker = line.split("SPEAKER_")[1].split(":")[0]
                speakers.add(speaker)
        num_speakers = len(speakers)
        
        print("Transcript stats:")
        print(f"  Lines: {line_count}")
        print(f"  Characters: {char_count}")
        print(f"  Speakers detected: {num_speakers}")
        if duration_minutes > 0:
            print(f"  Duration: {duration_minutes:.1f} minutes")
            estimated_cost = duration_minutes * 0.0043
            print(f"  Estimated cost: ${estimated_cost:.2f}")
        print()
        
        return output_path
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio using Deepgram Nova-2 with speaker diarization",
        epilog="""
Example:
  python3 transcribe_with_deepgram.py audio.mp3
  
Features:
  - Most cost-effective cloud option (~$0.0043 per minute)
  - Built-in speaker diarization (automatic detection)
  - Very fast processing (usually < 1 minute)
  - No file size limits
  - Word-level timestamps
  
Setup:
  1. Get API key from https://console.deepgram.com/
  2. Set environment variable:
     export DEEPGRAM_API_KEY='your-key'
  3. Install SDK:
     pip install deepgram-sdk
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("audio", help="Path to audio file (MP3, WAV, etc.)")
    parser.add_argument("--output-dir", default="intermediates",
                       help="Output directory (default: intermediates)")
    
    args = parser.parse_args()
    
    try:
        output_path = transcribe_with_deepgram(args.audio, args.output_dir)
        
        print("="*70)
        print("✓ Transcription complete!")
        print("="*70)
        print()
        print("Next steps:")
        print("  1. Review the transcript")
        print("  2. Post-process with AI:")
        print(f"     python3 scripts/post_process_transcript.py {output_path} --provider openai")
        print()
        
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
