#!/bin/bash
# Test script to compare different WhisperX model configurations
# Usage: ./test_model_comparison.sh <audio_file>

if [ $# -eq 0 ]; then
    echo "Error: No audio file provided"
    echo "Usage: $0 <audio_file>"
    exit 1
fi

AUDIO_FILE="$1"

if [ ! -f "$AUDIO_FILE" ]; then
    echo "Error: Audio file not found: $AUDIO_FILE"
    exit 1
fi

echo "========================================"
echo "WhisperX Model Comparison Test"
echo "========================================"
echo "Audio file: $AUDIO_FILE"
echo ""
echo "This will run 2 high-quality GPU tests:"
echo "  1. large-v2 (current baseline)"
echo "  2. large-v3 (newest model)"
echo ""
echo "All tests use --high-quality mode with GPU"
echo "Note: VAD is always enabled in WhisperX by default"
echo "========================================"
echo ""

# Check if HF_TOKEN is set
if [ -z "$HF_TOKEN" ]; then
    echo "Warning: HF_TOKEN environment variable not set"
    echo "Make sure to set it before running: export HF_TOKEN=your_token"
    exit 1
fi

# Create results directory
RESULTS_DIR="comparison_results_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$RESULTS_DIR"

echo "Results will be saved to: $RESULTS_DIR"
echo ""

# Test 1: large-v2 (current baseline)
echo "========================================"
echo "TEST 1/2: large-v2 (baseline)"
echo "========================================"
time python3 transcribe_with_diarization.py "$AUDIO_FILE" \
    --high-quality \
    --model large-v2 \
    2>&1 | tee "$RESULTS_DIR/test1_large-v2.log"
echo ""

# Test 2: large-v3 (newest model)
echo "========================================"
echo "TEST 2/2: large-v3"
echo "========================================"
time python3 transcribe_with_diarization.py "$AUDIO_FILE" \
    --high-quality \
    --model large-v3 \
    2>&1 | tee "$RESULTS_DIR/test2_large-v3.log"
echo ""

# Summary
echo "========================================"
echo "COMPARISON COMPLETE"
echo "========================================"
echo ""
echo "Results saved to: $RESULTS_DIR"
echo ""
echo "Output files generated:"
ls -lh *_lv*_hq*_transcript_with_speakers.txt 2>/dev/null
echo ""
echo "Timing information is in the log files:"
ls -1 "$RESULTS_DIR"/*.log
echo ""
echo "========================================"
