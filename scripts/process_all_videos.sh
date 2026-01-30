#!/bin/bash
# Process all MP4 files in the project root through the full pipeline

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Detect and activate appropriate virtual environment
detect_venv() {
    if command -v nvidia-smi &> /dev/null && nvidia-smi &> /dev/null; then
        [ -d "$PROJECT_DIR/venv-nvidia" ] && echo "venv-nvidia" && return
    fi
    if command -v rocminfo &> /dev/null && rocminfo &> /dev/null 2>&1; then
        [ -d "$PROJECT_DIR/venv-amd" ] && echo "venv-amd" && return
    fi
    [ -d "$PROJECT_DIR/venv-intel" ] && echo "venv-intel" && return
    [ -d "$PROJECT_DIR/venv-cpu" ] && echo "venv-cpu" && return
    [ -d "$PROJECT_DIR/venv" ] && echo "venv" && return
    echo ""
}

VENV_NAME=$(detect_venv)
if [ -z "$VENV_NAME" ]; then
    echo "Error: No virtual environment found. Run install_packages_and_venv.sh first."
    exit 1
fi

echo "Using venv: $VENV_NAME"
source "$PROJECT_DIR/$VENV_NAME/bin/activate"
source "$PROJECT_DIR/setup_env.sh"

# Set HSA override for AMD GPUs (needed for RX 6000 series)
[ "$VENV_NAME" = "venv-amd" ] && export HSA_OVERRIDE_GFX_VERSION=10.3.0

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
