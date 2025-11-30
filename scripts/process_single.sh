#!/bin/bash
# ==============================================================================
# Single MP3 Transcription with Multi-Provider Pipeline
# ==============================================================================
# Minimal orchestration script - calls Python scripts for all heavy lifting
# ==============================================================================

set -e

# Source shared utilities
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/shell_utils.sh"

# Check if audio file provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <audio_file> --transcribers <t1,t2,...> --processors <p1,p2,...> [options]"
    echo ""
    echo "Required:"
    echo "  <audio_file>                Path to MP3 audio file"
    echo "  --transcribers <list>       Comma-separated transcription services"
    echo "                              (whisperx, whisperx-cloud, deepgram, assemblyai)"
    echo "  --processors <list>         Comma-separated AI post-processors"
    echo "                              (opus, gemini)"
    echo ""
    echo "Optional:"
    echo "  --batch-size <n>            Batch size for WhisperX (default: 16 GPU, 8 CPU)"
    echo "  --force-cpu                 Force CPU mode for WhisperX (fixes torchvision issues)"
    echo ""
    echo "Examples:"
    echo "  $0 interview.mp3 --transcribers deepgram --processors opus,gemini"
    echo "  $0 interview.mp3 --transcribers whisperx,deepgram --processors opus"
    echo "  $0 interview.mp3 --transcribers whisperx --processors gemini --force-cpu"
    exit 1
fi

AUDIO_FILE="$1"
shift

# Parse arguments
TRANSCRIBERS=""
PROCESSORS=""
BATCH_SIZE=""
FORCE_CPU=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --transcribers)
            TRANSCRIBERS="$2"
            shift 2
            ;;
        --processors)
            PROCESSORS="$2"
            shift 2
            ;;
        --batch-size)
            BATCH_SIZE="$2"
            shift 2
            ;;
        --force-cpu)
            FORCE_CPU="--force-cpu"
            shift
            ;;
        *)
            echo "Error: Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate required arguments
if [ -z "$TRANSCRIBERS" ]; then
    echo "Error: --transcribers is required"
    exit 1
fi

if [ -z "$PROCESSORS" ]; then
    echo "Error: --processors is required"
    exit 1
fi

if [ ! -f "$AUDIO_FILE" ]; then
    echo "Error: Audio file not found: $AUDIO_FILE"
    exit 1
fi

# Start overall timing
PIPELINE_START=$(date +%s)

# Show what we're doing
BASE_NAME=$(basename "$AUDIO_FILE" | sed 's/\.[^.]*$//')
IFS=',' read -ra TRANSCRIBER_ARRAY <<< "$TRANSCRIBERS"
IFS=',' read -ra PROCESSOR_ARRAY <<< "$PROCESSORS"
TOTAL_COMBINATIONS=$((${#TRANSCRIBER_ARRAY[@]} * ${#PROCESSOR_ARRAY[@]}))

echo "========================================================================"
echo "Multi-Transcriber × Multi-Processor Pipeline"
echo "========================================================================"
echo "Audio: $AUDIO_FILE"
echo "Transcribers: $TRANSCRIBERS (${#TRANSCRIBER_ARRAY[@]} services)"
echo "Processors: $PROCESSORS (${#PROCESSOR_ARRAY[@]} services)"
echo "Total combinations: $TOTAL_COMBINATIONS"
echo "========================================================================"
echo ""

# PHASE 1: Transcription (Python handles all transcribers internally)
echo "PHASE 1: Transcription"
echo "========================================================================"

PHASE1_START=$(date +%s)

TRANSCRIBE_CMD="python3 scripts/process_single_transcribe_and_diarize.py \"$AUDIO_FILE\" --transcribers \"$TRANSCRIBERS\""
if [ -n "$BATCH_SIZE" ]; then
    TRANSCRIBE_CMD="$TRANSCRIBE_CMD --batch-size $BATCH_SIZE"
fi
if [ -n "$FORCE_CPU" ]; then
    TRANSCRIBE_CMD="$TRANSCRIBE_CMD $FORCE_CPU"
fi

if ! eval $TRANSCRIBE_CMD; then
    echo "✗ Transcription phase failed"
    exit 1
fi

PHASE1_END=$(date +%s)
PHASE1_DURATION=$((PHASE1_END - PHASE1_START))

echo ""
echo "Phase 1 complete: $(format_duration $PHASE1_DURATION)"
echo ""

# Find generated transcript files (no _raw suffix)
TRANSCRIPT_FILES=()
for TRANSCRIBER in "${TRANSCRIBER_ARRAY[@]}"; do
    TRANSCRIPT_FILE="intermediates/${BASE_NAME}/${BASE_NAME}_${TRANSCRIBER}.txt"

    if [ -f "$TRANSCRIPT_FILE" ]; then
        TRANSCRIPT_FILES+=("$TRANSCRIPT_FILE")
    fi
done

if [ ${#TRANSCRIPT_FILES[@]} -eq 0 ]; then
    echo "Error: No transcript files were generated"
    exit 1
fi

# PHASE 2: Post-Processing (Python handles all processors internally)
echo "PHASE 2: Post-Processing"
echo "========================================================================"

PHASE2_START=$(date +%s)

# Pass transcript files with proper quoting to handle spaces
if ! python3 scripts/process_single_post_process.py "${TRANSCRIPT_FILES[@]}" --processors "$PROCESSORS"; then
    echo "✗ Post-processing phase failed"
    exit 1
fi

PHASE2_END=$(date +%s)
PHASE2_DURATION=$((PHASE2_END - PHASE2_START))

echo ""
echo "Phase 2 complete: $(format_duration $PHASE2_DURATION)"
echo ""

# Overall timing
PIPELINE_END=$(date +%s)
PIPELINE_DURATION=$((PIPELINE_END - PIPELINE_START))

echo "========================================================================"
echo "✓ PIPELINE COMPLETE!"
echo "========================================================================"
echo ""
echo "Timing Summary:"
echo "  Phase 1 (Transcription):   $(format_duration $PHASE1_DURATION)"
echo "  Phase 2 (Post-Processing): $(format_duration $PHASE2_DURATION)"
echo "  Total Pipeline Time:       $(format_duration $PIPELINE_DURATION)"
echo ""
echo "Output files:"
echo "  Transcripts: ./intermediates/"
echo "  Corrected:   ./outputs/"
echo "========================================================================"
