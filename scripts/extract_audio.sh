#!/bin/bash
# Extract MP3 audio from MP4 video file

if [ -z "$1" ]; then
    echo "Usage: $0 <input.mp4> [output.mp3]"
    echo "  If output is not specified, uses input filename with .mp3 extension"
    exit 1
fi

INPUT="$1"

if [ ! -f "$INPUT" ]; then
    echo "Error: File not found: $INPUT"
    exit 1
fi

# Determine output filename
if [ -n "$2" ]; then
    OUTPUT="$2"
else
    OUTPUT="${INPUT%.mp4}.mp3"
fi

echo "Extracting audio from: $INPUT"
echo "Output file: $OUTPUT"

ffmpeg -i "$INPUT" -vn -acodec libmp3lame -q:a 2 "$OUTPUT"

if [ $? -eq 0 ]; then
    echo "Done: $OUTPUT"
else
    echo "Error: Audio extraction failed"
    exit 1
fi
