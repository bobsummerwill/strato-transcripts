#!/usr/bin/env python3
"""
Format transcript with speakers for markdown output
"""

import sys
import re

def format_for_markdown(input_file, output_file):
    """Convert transcript to markdown format"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    output_lines = []
    current_speaker = None
    current_text = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if this is a speaker line (ends with :)
        if line.endswith(':') and not line.startswith('['):
            # If we have accumulated text, output it
            if current_speaker and current_text:
                output_lines.append(f"\n**{current_speaker}:**")
                output_lines.extend(current_text)
                current_text = []
            
            # Set new speaker
            current_speaker = line[:-1]  # Remove the colon
        else:
            # This is a text line with timestamp
            current_text.append(line)
    
    # Output any remaining text
    if current_speaker and current_text:
        output_lines.append(f"\n**{current_speaker}:**")
        output_lines.extend(current_text)
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"Formatted transcript written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 format_transcript_for_markdown.py <input_file> <output_file>")
        sys.exit(1)
    
    format_for_markdown(sys.argv[1], sys.argv[2])
