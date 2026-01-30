#!/usr/bin/env python3
"""
Generate word-level JSON from existing transcript markdown files.

This creates estimated word timing by interpolating within segment boundaries.
Useful when word-level data wasn't captured during original transcription.

Usage:
    python generate_word_json_from_transcript.py <transcript.md> [--output <words.json>]

Example:
    python generate_word_json_from_transcript.py \
        intermediates/episode009/episode009_whisperx-cloud.md \
        --output intermediates/episode009/episode009_whisperx-cloud_words.json
"""

import argparse
import json
import re
from pathlib import Path
from typing import List, Dict


def parse_transcript(filepath: Path) -> List[Dict]:
    """Parse markdown transcript and extract timed segments."""
    segments = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern: **[MM:SS] SPEAKER:** text or **[H:MM:SS] SPEAKER:** text
    pattern = r'\*\*\[(\d+:?\d*:\d+)\]\s*([^:]+):\*\*\s*(.+?)(?=\*\*\[|\Z)'

    matches = re.findall(pattern, content, re.DOTALL)

    for timestamp, speaker, text in matches:
        # Parse timestamp to seconds
        parts = timestamp.split(':')
        if len(parts) == 2:
            seconds = int(parts[0]) * 60 + int(parts[1])
        else:
            seconds = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])

        # Clean up text
        text = ' '.join(text.split())

        segments.append({
            'start': seconds,
            'speaker': speaker.strip(),
            'text': text
        })

    return segments


def generate_word_json(segments: List[Dict]) -> List[Dict]:
    """
    Generate word-level JSON with estimated timing from segments.

    Uses segment boundaries to interpolate word timing.
    """
    word_data = []

    for i, seg in enumerate(segments):
        speaker = seg['speaker']
        text = seg['text']
        words = text.split()

        if not words:
            continue

        seg_start = seg['start']

        # Estimate segment end from next segment or add duration
        if i + 1 < len(segments):
            seg_end = segments[i + 1]['start']
        else:
            # Last segment - estimate 0.3s per word
            seg_end = seg_start + len(words) * 0.3

        # Ensure minimum duration
        duration = max(seg_end - seg_start, len(words) * 0.1)
        word_duration = duration / len(words)

        for j, word_text in enumerate(words):
            word_data.append({
                'text': word_text,
                'start': round(seg_start + j * word_duration, 3),
                'end': round(seg_start + (j + 1) * word_duration, 3),
                'speaker': speaker,
                'estimated': True
            })

    return word_data


def main():
    parser = argparse.ArgumentParser(
        description='Generate word-level JSON from existing transcript'
    )
    parser.add_argument('transcript', type=Path,
                        help='Path to transcript markdown file')
    parser.add_argument('--output', '-o', type=Path,
                        help='Output path for word JSON (default: auto-generated)')

    args = parser.parse_args()

    if not args.transcript.exists():
        print(f"Error: Transcript not found: {args.transcript}")
        return 1

    # Generate output path if not specified
    if args.output is None:
        stem = args.transcript.stem
        args.output = args.transcript.parent / f"{stem}_words.json"

    print(f"Parsing transcript: {args.transcript}")
    segments = parse_transcript(args.transcript)
    print(f"  Found {len(segments)} segments")

    print("Generating word-level timing...")
    word_data = generate_word_json(segments)
    print(f"  Generated {len(word_data)} words with estimated timing")

    # Ensure output directory exists
    args.output.parent.mkdir(parents=True, exist_ok=True)

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(word_data, f, indent=2)

    print(f"Saved: {args.output}")

    return 0


if __name__ == '__main__':
    exit(main())
