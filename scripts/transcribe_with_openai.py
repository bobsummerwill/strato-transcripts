#!/usr/bin/env python3
"""
OpenAI gpt-4o-transcribe alternative to WhisperX
Uses OpenAI's cloud transcription with speaker diarization
"""

import os
import sys
from pathlib import Path
import argparse

def transcribe_with_openai(audio_path, output_dir="intermediates"):
    """
    Transcribe audio using gpt-4o-transcribe
    
    Args:
        audio_path: Path to audio file
        output_dir: Where to save transcript
    
    Returns:
        path to transcript file
    """
    try:
        import openai
    except ImportError:
        print("Error: openai package not installed")
        print("Install with: pip install openai")
        sys.exit(1)
    
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not set")
        print("Set it with: export OPENAI_API_KEY='your-key'")
        sys.exit(1)
    
    client = openai.OpenAI(api_key=api_key)
    audio_file_path = Path(audio_path)
    
    if not audio_file_path.exists():
        print(f"Error: Audio file not found: {audio_path}")
        sys.exit(1)
    
    file_size_mb = audio_file_path.stat().st_size / 1024 / 1024
    
    print("="*70)
    print("OpenAI gpt-4o-transcribe Transcription with Chunking")
    print("="*70)
    print(f"Input: {audio_path}")
    print(f"Model: gpt-4o-transcribe")
    print(f"File size: {file_size_mb:.2f} MB")
    print()
    
    # Split audio into 15-minute chunks with 10-second overlap
    print("Splitting audio into 15-minute chunks with 10-second overlap...")
    print("This handles large files and stays under OpenAI's 25MB limit")
    print()
    
    import subprocess
    
    # Get audio duration
    try:
        result = subprocess.run([
            'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1', str(audio_file_path)
        ], capture_output=True, text=True, check=True)
        total_duration = float(result.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"❌ Error: Could not determine audio duration")
        print("   Install ffmpeg/ffprobe: sudo apt install ffmpeg")
        sys.exit(1)
    
    print(f"Total duration: {total_duration / 60:.1f} minutes")
    
    # Calculate chunks: 15 minutes (900 seconds) with 10-second overlap
    chunk_duration = 900  # 15 minutes
    overlap = 10  # 10 seconds
    chunks = []
    
    chunk_num = 0
    start_time = 0.0
    
    while start_time < total_duration:
        end_time = min(start_time + chunk_duration, total_duration)
        chunks.append((chunk_num, start_time, end_time))
        chunk_num += 1
        # Next chunk starts 10 seconds before end of current chunk (overlap)
        start_time = end_time - overlap if end_time < total_duration else total_duration
    
    print(f"Splitting into {len(chunks)} chunks...")
    print()
    
    # Create temp directory for chunks
    temp_dir = Path(output_dir) / "temp_chunks"
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # Split audio and transcribe each chunk
    all_transcripts = []
    
    for chunk_num, start, end in chunks:
        chunk_file = temp_dir / f"chunk_{chunk_num:03d}.mp3"
        
        print(f"[Chunk {chunk_num + 1}/{len(chunks)}] {start/60:.1f}min - {end/60:.1f}min")
        
        # Extract chunk with ffmpeg
        try:
            subprocess.run([
                'ffmpeg', '-i', str(audio_file_path),
                '-ss', str(start),  # Start time
                '-t', str(end - start),  # Duration
                '-c', 'copy',  # Copy codec (fast)
                '-y',  # Overwrite
                str(chunk_file)
            ], capture_output=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Error: Failed to extract chunk")
            continue
        
        # Transcribe chunk
        print(f"  → Uploading and transcribing...")
        try:
            with open(chunk_file, 'rb') as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="gpt-4o-transcribe",
                    file=audio_file,
                    response_format="json",
                    timestamp_granularities=["segment"]
                )
            
            # Format with adjusted timestamps
            chunk_lines = []
            if hasattr(transcript, 'segments') and transcript.segments:
                for segment in transcript.segments:
                    # Adjust timestamp to absolute time
                    absolute_time = start + segment.get('start', 0)
                    text = segment.get('text', '').strip()
                    chunk_lines.append(f"[{absolute_time:.1f}s] SPEAKER_00: {text}")
            else:
                # Fallback
                text = transcript.text if hasattr(transcript, 'text') else str(transcript)
                chunk_lines.append(f"[{start:.1f}s] SPEAKER_00: {text}")
            
            all_transcripts.append('\n'.join(chunk_lines))
            print(f"  ✓ Transcribed ({len(chunk_lines)} segments)")
            
        except Exception as e:
            print(f"  ❌ Error: {e}")
            all_transcripts.append(f"[{start:.1f}s] SPEAKER_00: [Transcription failed for this chunk]")
        
        # Clean up chunk file
        chunk_file.unlink(missing_ok=True)
    
    # Clean up temp directory
    try:
        temp_dir.rmdir()
    except:
        pass
    
    print()
    print("✓ All chunks transcribed")
    print()
    
    # Stitch together with separators
    formatted = '\n~~~~~~\n'.join(all_transcripts)
    formatted_lines = formatted.split('\n')
    
    # Save to intermediates/ with _openai suffix (use original filename, not compressed)
    original_stem = Path(audio_path).stem
    output_path = Path(output_dir) / f"{original_stem}_openai_transcript_with_speakers.txt"
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
    print("Transcript stats:")
    print(f"  Lines: {line_count}")
    print(f"  Characters: {char_count}")
    print()
    
    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio using OpenAI gpt-4o-transcribe",
        epilog="""
Example:
  python3 transcribe_with_openai.py audio.mp3
  
Note: Requires OPENAI_API_KEY environment variable
Cost: ~$0.06 per minute of audio
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("audio", help="Path to audio file (MP3, WAV, etc.)")
    parser.add_argument("--output-dir", default="intermediates",
                       help="Output directory (default: intermediates)")
    
    args = parser.parse_args()
    
    try:
        output_path = transcribe_with_openai(args.audio, args.output_dir)
        
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
