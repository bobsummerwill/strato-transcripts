#!/bin/bash
# Process all MP4 files in the project root through the full pipeline

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Activate virtual environment and load API keys
source "$PROJECT_DIR/venv/bin/activate"
source "$PROJECT_DIR/setup_env.sh"

# Parse arguments to pass through to process_video.sh
EXTRA_ARGS=""
while [[ $# -gt 0 ]]; do
    EXTRA_ARGS="$EXTRA_ARGS $1"
    shift
done

cd "$PROJECT_DIR"

MP4_FILES=(*.mp4)

if [ ! -e "${MP4_FILES[0]}" ]; then
    echo "No MP4 files found in $PROJECT_DIR"
    exit 0
fi

echo "Found ${#MP4_FILES[@]} MP4 file(s) to process"
echo ""

for mp4 in "${MP4_FILES[@]}"; do
    echo "========================================"
    echo "Processing: $mp4"
    echo "========================================"
    "$SCRIPT_DIR/process_video.sh" "$mp4" $EXTRA_ARGS
    echo ""
done

echo "All videos processed."
