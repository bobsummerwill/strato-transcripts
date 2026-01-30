#!/usr/bin/env python3
"""
Align post-processed (corrected) transcript text with original word-level timestamps.

This script takes:
- Word-level JSON from pre-processor (whisperx, whisperx-cloud, assemblyai)
- Corrected markdown from post-processor (opus, gemini, etc.)

And produces:
- Aligned word JSON with corrected text and accurate timestamps
- For unchanged words: exact original timestamps
- For changed/inserted words: interpolated timestamps

Usage:
    python align_words_with_corrections.py <words_json> <corrected_md> [--output <aligned_json>]

Example:
    python align_words_with_corrections.py \
        intermediates/episode009/episode009_whisperx-cloud_words.json \
        outputs/episode009/episode009_whisperx-cloud_opus.md \
        --output intermediates/episode009/episode009_whisperx-cloud_opus_aligned_words.json
"""

import argparse
import json
import re
from pathlib import Path
from difflib import SequenceMatcher
from typing import List, Dict, Tuple, Optional


def load_word_json(json_path: Path) -> List[Dict]:
    """Load word-level timing data from JSON."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_corrected_markdown(md_path: Path) -> List[Dict]:
    """
    Parse corrected markdown into segments with speaker and text.

    Expected format: **[MM:SS] SPEAKER_XX:** text
    or: **SPEAKER_XX:** text (without timestamp)
    """
    segments = []

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match speaker segments with optional timestamps
    # **[00:03] SPEAKER_00:** text
    # **[00:03] Bob:** text
    # **Bob:** text
    pattern = r'\*\*(?:\[([^\]]+)\]\s*)?([^:*]+):\*\*\s*(.+?)(?=\n\n\*\*|\n\n$|$)'

    for match in re.finditer(pattern, content, re.DOTALL):
        timestamp_str = match.group(1)  # May be None
        speaker = match.group(2).strip()
        text = match.group(3).strip()

        # Parse timestamp if present
        timestamp = None
        if timestamp_str:
            # Handle MM:SS or HH:MM:SS format
            parts = timestamp_str.split(':')
            if len(parts) == 2:
                timestamp = int(parts[0]) * 60 + int(parts[1])
            elif len(parts) == 3:
                timestamp = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])

        segments.append({
            'speaker': speaker,
            'text': text,
            'timestamp': timestamp
        })

    return segments


def normalize_word(word: str) -> str:
    """Normalize word for comparison (lowercase, strip punctuation)."""
    return re.sub(r'[^\w\s]', '', word.lower()).strip()


def extract_words_from_segments(segments: List[Dict]) -> List[Tuple[str, str]]:
    """Extract (word, speaker) pairs from parsed segments."""
    words = []
    for seg in segments:
        speaker = seg['speaker']
        text = seg['text']
        for word in text.split():
            words.append((word, speaker))
    return words


def align_words(original_words: List[Dict], corrected_words: List[Tuple[str, str]]) -> List[Dict]:
    """
    Align corrected words with original word timestamps using sequence matching.

    Returns list of aligned words with:
    - text: corrected word text
    - start/end: timestamps (from original if matched, interpolated if not)
    - speaker: from corrected transcript
    - match_type: 'exact', 'fuzzy', or 'interpolated'
    """
    # Extract just the text from original words for matching
    orig_texts = [normalize_word(w.get('text', w.get('word', ''))) for w in original_words]
    corr_texts = [normalize_word(w[0]) for w in corrected_words]

    # Use SequenceMatcher to find matching blocks
    matcher = SequenceMatcher(None, orig_texts, corr_texts)

    aligned = []

    # Track which original words have been used
    orig_used = [False] * len(original_words)

    # Process matching blocks
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            # Exact match - use original timestamps
            for orig_idx, corr_idx in zip(range(i1, i2), range(j1, j2)):
                orig = original_words[orig_idx]
                corr_word, corr_speaker = corrected_words[corr_idx]
                orig_used[orig_idx] = True

                aligned.append({
                    'text': corr_word,
                    'start': orig.get('start', 0),
                    'end': orig.get('end', 0),
                    'speaker': corr_speaker,
                    'match_type': 'exact',
                    'original_text': orig.get('text', orig.get('word', ''))
                })

        elif tag == 'replace':
            # Words changed - try fuzzy matching, then interpolate
            orig_slice = original_words[i1:i2]
            corr_slice = corrected_words[j1:j2]

            if orig_slice and corr_slice:
                # Interpolate timestamps across the replacement
                start_time = orig_slice[0].get('start', 0)
                end_time = orig_slice[-1].get('end', orig_slice[-1].get('start', 0) + 0.5)
                duration = end_time - start_time
                word_duration = duration / len(corr_slice) if corr_slice else 0

                for k, (corr_word, corr_speaker) in enumerate(corr_slice):
                    aligned.append({
                        'text': corr_word,
                        'start': start_time + k * word_duration,
                        'end': start_time + (k + 1) * word_duration,
                        'speaker': corr_speaker,
                        'match_type': 'interpolated'
                    })

                for idx in range(i1, i2):
                    orig_used[idx] = True

        elif tag == 'insert':
            # New words in corrected - interpolate from surrounding context
            corr_slice = corrected_words[j1:j2]

            # Find surrounding timestamps
            prev_end = 0
            next_start = None

            if i1 > 0:
                prev_end = original_words[i1 - 1].get('end', 0)
            if i1 < len(original_words):
                next_start = original_words[i1].get('start', prev_end + 1)
            else:
                next_start = prev_end + len(corr_slice) * 0.3  # Estimate 0.3s per word

            duration = next_start - prev_end
            word_duration = duration / len(corr_slice) if corr_slice else 0

            for k, (corr_word, corr_speaker) in enumerate(corr_slice):
                aligned.append({
                    'text': corr_word,
                    'start': prev_end + k * word_duration,
                    'end': prev_end + (k + 1) * word_duration,
                    'speaker': corr_speaker,
                    'match_type': 'interpolated'
                })

        elif tag == 'delete':
            # Words removed from original - skip them
            for idx in range(i1, i2):
                orig_used[idx] = True

    return aligned


def save_aligned_json(aligned_words: List[Dict], output_path: Path):
    """Save aligned words to JSON."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(aligned_words, f, indent=2)

    # Print statistics
    exact = sum(1 for w in aligned_words if w.get('match_type') == 'exact')
    interpolated = sum(1 for w in aligned_words if w.get('match_type') == 'interpolated')
    total = len(aligned_words)

    print(f"Aligned {total} words:")
    print(f"  - Exact timestamp matches: {exact} ({100*exact/total:.1f}%)")
    print(f"  - Interpolated timestamps: {interpolated} ({100*interpolated/total:.1f}%)")
    print(f"Saved: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Align corrected transcript with original word timestamps'
    )
    parser.add_argument('words_json', type=Path,
                        help='Path to word-level JSON from pre-processor')
    parser.add_argument('corrected_md', type=Path,
                        help='Path to corrected markdown from post-processor')
    parser.add_argument('--output', '-o', type=Path,
                        help='Output path for aligned JSON (default: auto-generated)')

    args = parser.parse_args()

    # Validate inputs
    if not args.words_json.exists():
        print(f"Error: Word JSON not found: {args.words_json}")
        return 1

    if not args.corrected_md.exists():
        print(f"Error: Corrected markdown not found: {args.corrected_md}")
        return 1

    # Generate output path if not specified
    if args.output is None:
        # e.g., episode009_whisperx-cloud_opus.md -> episode009_whisperx-cloud_opus_aligned_words.json
        stem = args.corrected_md.stem
        args.output = args.corrected_md.parent / f"{stem}_aligned_words.json"

    print(f"Loading word timestamps: {args.words_json}")
    original_words = load_word_json(args.words_json)
    print(f"  Loaded {len(original_words)} words")

    print(f"Loading corrected transcript: {args.corrected_md}")
    corrected_segments = parse_corrected_markdown(args.corrected_md)
    print(f"  Loaded {len(corrected_segments)} segments")

    # Extract words from corrected segments
    corrected_words = extract_words_from_segments(corrected_segments)
    print(f"  Extracted {len(corrected_words)} words")

    print("Aligning words...")
    aligned_words = align_words(original_words, corrected_words)

    # Ensure output directory exists
    args.output.parent.mkdir(parents=True, exist_ok=True)

    save_aligned_json(aligned_words, args.output)

    return 0


if __name__ == '__main__':
    exit(main())
