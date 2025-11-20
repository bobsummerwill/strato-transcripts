#!/usr/bin/env python3
import os

def create_combined_file():
    """Create episode007 combined file from the highest quality baseline"""

    # Read the WhisperX + Llama output file (highest rated at 9.4/10)
    with open('outputs/episode007-jacob-czepluch-whisperx-cloud_llama.md', 'r') as f:
        content = f.read()

    # Write to combined file
    with open('outputs/episode007-jacob-czepluch_combined.md', 'w') as f:
        f.write(content)

    print(f"Created episode007 combined file from WhisperX + Llama baseline")
    print(f"Size: {len(content)} characters")

if __name__ == "__main__":
    create_combined_file()
    create_combined_file()
