#!/usr/bin/env python3
"""
Map SPEAKER_XX labels to actual names based on context analysis
"""

import sys
import re
from pathlib import Path

# Speaker mapping based on content analysis
SPEAKER_MAP = {
    'SPEAKER_01': 'Bob Summerwill',    # 621 segments - guest, talks most
    'SPEAKER_05': 'Kieren James-Lubin', # 107 segments - introduces Bob, moderates
    'SPEAKER_03': 'Jim Hormuzdiar',     # 66 segments - mentions being old friends
    'SPEAKER_02': 'Victor Wong',        # 15 segments - occasional comments
    'SPEAKER_00': 'UNKNOWN',            # 1 segment - very brief
    'SPEAKER_04': 'UNKNOWN',            # 1 segment - very brief
    'UNKNOWN': 'UNKNOWN'                # Several brief segments
}

def map_speakers(input_path, output_path=None):
    """Map speaker labels to actual names"""
    
    input_path = Path(input_path)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)
    
    if output_path is None:
        output_path = input_path.parent / f"{input_path.stem}_with_names.txt"
    else:
        output_path = Path(output_path)
    
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace speaker labels with names
    for speaker_id, name in SPEAKER_MAP.items():
        content = content.replace(f"\n{speaker_id}:", f"\n{name}:")
    
    # Save output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✓ Mapped speakers to names")
    print(f"✓ Saved to: {output_path}")
    
    # Show mapping
    print("\nSpeaker mapping:")
    for speaker_id, name in SPEAKER_MAP.items():
        print(f"  {speaker_id} → {name}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input transcript file")
    parser.add_argument("--output", help="Output file path")
    
    args = parser.parse_args()
    
    map_speakers(args.input_file, args.output)
