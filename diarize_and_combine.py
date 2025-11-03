#!/usr/bin/env python3
"""
Run speaker diarization and combine with existing WhisperX transcript
"""

import sys
import re
from pathlib import Path
from pyannote.audio import Pipeline
import torch

def parse_whisperx_transcript(transcript_path):
    """Parse WhisperX transcript to extract segments"""
    segments = []
    
    with open(transcript_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('UNKNOWN'):
            continue
        
        # Match timestamp pattern [123.4s]
        match = re.match(r'\[(\d+\.?\d*)s\]\s*(.*)', line)
        if match:
            timestamp = float(match.group(1))
            text = match.group(2).strip()
            if text:
                segments.append({'time': timestamp, 'text': text})
    
    return segments

def get_speaker_at_time(time, diarization):
    """Find speaker active at given time"""
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        if turn.start <= time <= turn.end:
            return speaker
    return "UNKNOWN"

def process_audio(audio_path, transcript_path, hf_token, output_path=None):
    """
    Run diarization and combine with transcript
    """
    audio_path = Path(audio_path)
    transcript_path = Path(transcript_path)
    
    if not audio_path.exists():
        print(f"Error: Audio file not found: {audio_path}")
        sys.exit(1)
    
    if not transcript_path.exists():
        print(f"Error: Transcript not found: {transcript_path}")
        sys.exit(1)
    
    print(f"Audio: {audio_path}")
    print(f"Transcript: {transcript_path}")
    
    # Parse transcript
    print("\n" + "="*60)
    print("Step 1: Loading transcript...")
    print("="*60)
    
    segments = parse_whisperx_transcript(transcript_path)
    print(f"✓ Loaded {len(segments)} segments")
    
    # Run diarization
    print("\n" + "="*60)
    print("Step 2: Loading diarization model...")
    print("="*60)
    
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=hf_token
    )
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cuda":
        print(f"Using GPU: {torch.cuda.get_device_name(0)}")
        pipeline.to(torch.device("cuda"))
    else:
        print("Using CPU")
        pipeline.to(torch.device("cpu"))
    
    print("✓ Model loaded")
    
    print("\n" + "="*60)
    print("Step 3: Running diarization (this may take a while)...")
    print("="*60)
    
    import time
    start = time.time()
    diarization = pipeline(str(audio_path))
    elapsed = time.time() - start
    
    print(f"✓ Complete in {elapsed:.1f}s ({elapsed/60:.1f} min)")
    
    # Count speakers
    speakers = set()
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        speakers.add(speaker)
    print(f"Detected {len(speakers)} speakers: {sorted(speakers)}")
    
    # Combine
    print("\n" + "="*60)
    print("Step 4: Combining transcript with speakers...")
    print("="*60)
    
    output_segments = []
    for seg in segments:
        speaker = get_speaker_at_time(seg['time'], diarization)
        output_segments.append({
            'time': seg['time'],
            'speaker': speaker,
            'text': seg['text']
        })
    
    print(f"✓ Labeled {len(output_segments)} segments")
    
    # Save output
    if output_path is None:
        output_path = audio_path.parent / f"{audio_path.stem}_transcript_with_speakers.txt"
    else:
        output_path = Path(output_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        current_speaker = None
        for seg in output_segments:
            if seg['speaker'] != current_speaker:
                f.write(f"\n{seg['speaker']}:\n")
                current_speaker = seg['speaker']
            f.write(f"[{seg['time']:.1f}s] {seg['text']}\n")
    
    print(f"\n✓ Saved to: {output_path}")
    
    # Stats
    print("\n" + "="*60)
    print("Summary")
    print("="*60)
    for speaker in sorted(speakers):
        count = sum(1 for s in output_segments if s['speaker'] == speaker)
        print(f"  {speaker}: {count} segments")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_file", help="Audio file path")
    parser.add_argument("transcript_file", help="WhisperX transcript file")
    parser.add_argument("--token", required=True, help="HuggingFace token")
    parser.add_argument("--output", help="Output file path")
    
    args = parser.parse_args()
    
    process_audio(args.audio_file, args.transcript_file, args.token, args.output)
