#!/bin/bash
# Extract MP3 audio from all MP4 files in the project root

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

MP4_FILES=(*.mp4)

if [ ! -e "${MP4_FILES[0]}" ]; then
    echo "No MP4 files found in $PROJECT_DIR"
    exit 0
fi

echo "Found ${#MP4_FILES[@]} MP4 file(s) to process"
echo ""

for mp4 in "${MP4_FILES[@]}"; do
    echo "Processing: $mp4"
    "$SCRIPT_DIR/extract_audio.sh" "$mp4"
    echo ""
done

echo "All done."
