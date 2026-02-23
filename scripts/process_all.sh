#!/bin/bash
# ==============================================================================
# Batch Process All MP3 Files in Project Root with Multi-Provider AI Pipeline
# ==============================================================================
# - Loops through all MP3 files in project root directory
# - Calls process_single.sh for each file
# - Outputs to ./outputs directory
# ==============================================================================

set -e

# Source shared utilities
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/shell_utils.sh"

# Defaults: WhisperX (local/FREE) + Claude Opus 4.6 (highest quality)
DEFAULT_TRANSCRIBERS="whisperx"
DEFAULT_PROCESSORS="opus"

# Parse arguments
TRANSCRIBERS="$DEFAULT_TRANSCRIBERS"
PROCESSORS="$DEFAULT_PROCESSORS"

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
        *)
            echo "Error: Unknown option: $1"
            echo ""
            echo "Usage: $0 [--transcribers <list>] [--processors <list>]"
            echo ""
            echo "Options:"
            echo "  --transcribers <list>    Comma-separated transcription services"
            echo "                           (whisperx, whisperx-cloud, assemblyai)"
            echo "                           Default: whisperx"
            echo ""
  echo "  --processors <list>      Comma-separated AI post-processors"
  echo "                           (opus, gemini, grok)"
            echo "                           Default: opus (Claude Opus 4.6)"
            echo ""
            echo "Examples:"
            echo "  # Use defaults (whisperx + opus)"
            echo "  $0"
            echo ""
            echo "  # AssemblyAI + Multiple processors"
            echo "  $0 --transcribers assemblyai --processors opus,gemini"
            echo ""
            echo "  # Multiple combinations"
            echo "  $0 --transcribers whisperx,assemblyai \\"
            echo "     --processors opus,gemini"
            exit 1
            ;;
    esac
done

# Directories
PROJECT_DIR="$(pwd)"
INTERMEDIATES_DIR="$PROJECT_DIR/intermediates"
OUTPUT_DIR="$PROJECT_DIR/outputs"

# Ensure directories exist
mkdir -p "$INTERMEDIATES_DIR"
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Batch MP3 Processing with AI Pipeline${NC}"
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Transcribers: ${YELLOW}${TRANSCRIBERS}${NC}"
echo -e "${BLUE}Processors: ${YELLOW}${PROCESSORS}${NC}"
echo ""

# Auto-detect and activate virtual environment
# Priority: nvidia > amd > intel > cpu
detect_and_activate_venv() {
    local venvs=("venv-nvidia" "venv-amd" "venv-intel" "venv-cpu")

    for venv in "${venvs[@]}"; do
        if [ -d "$PROJECT_DIR/$venv" ]; then
            echo -e "${GREEN}Using virtual environment: $venv${NC}"
            source "$PROJECT_DIR/$venv/bin/activate"
            return 0
        fi
    done

    echo -e "${RED}Error: No virtual environment found. Run install_packages_and_venv.sh first.${NC}"
    echo "Expected one of: ${venvs[*]}"
    exit 1
}

cd "$PROJECT_DIR"
detect_and_activate_venv
source setup_env.sh

# Find all MP3 files
MP3_FILES=(*.mp3)
TOTAL=${#MP3_FILES[@]}

if [ $TOTAL -eq 0 ] || [ ! -e "${MP3_FILES[0]}" ]; then
    echo -e "${RED}No MP3 files found in project root directory${NC}"
    exit 1
fi

echo -e "${GREEN}Found $TOTAL MP3 files to process${NC}"
echo ""

# Timing arrays
declare -a FILE_NAMES
declare -a PROCESS_TIMES

# Overall timing
BATCH_START=$(date +%s)

# Process each file
COUNT=0
PROCESSED=0
FAILED=0

for MP3_FILE in "${MP3_FILES[@]}"; do
    COUNT=$((COUNT + 1))
    BASENAME=$(basename "$MP3_FILE" .mp3)
    
    echo -e "${YELLOW}========================================${NC}"
    echo -e "${YELLOW}[$COUNT/$TOTAL] Processing: $BASENAME${NC}"
    echo -e "${YELLOW}========================================${NC}"
    
    FILE_START=$(date +%s)
    
    # Call transcribe_and_correct_multi.sh with transcribers and processors
    if ./scripts/process_single.sh "$MP3_FILE" --transcribers "$TRANSCRIBERS" --processors "$PROCESSORS"; then
        FILE_END=$(date +%s)
        FILE_DURATION=$((FILE_END - FILE_START))
        
        echo -e "${GREEN}✓ Pipeline complete for $BASENAME${NC}"
        echo -e "  Time: $(format_duration $FILE_DURATION)"
        
        # Store timing data
        FILE_NAMES+=("$BASENAME")
        PROCESS_TIMES+=($FILE_DURATION)
        
        PROCESSED=$((PROCESSED + 1))
    else
        echo -e "${RED}✗ Pipeline failed for $BASENAME${NC}"
        FAILED=$((FAILED + 1))
    fi
    
    echo ""
done

BATCH_END=$(date +%s)
BATCH_DURATION=$((BATCH_END - BATCH_START))

# Summary report
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✓ Batch Processing Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${BLUE}Summary:${NC}"
echo "  Total files found: $TOTAL"
echo "  Processed successfully: $PROCESSED"
echo "  Failed: $FAILED"
echo "  Intermediates: $INTERMEDIATES_DIR"
echo "  Final output: $OUTPUT_DIR"
echo ""

if [ $PROCESSED -gt 0 ]; then
    echo -e "${BLUE}Timing Details:${NC}"
    echo ""
    
    # Calculate total
    TOTAL_FILE_TIME=0
    
    # Print per-file timing
    for i in "${!FILE_NAMES[@]}"; do
        echo -e "${YELLOW}${FILE_NAMES[$i]}${NC}"
        echo "  Pipeline time: $(format_duration ${PROCESS_TIMES[$i]})"
        echo ""
        
        TOTAL_FILE_TIME=$((TOTAL_FILE_TIME + ${PROCESS_TIMES[$i]}))
    done
    
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}Totals:${NC}"
    echo "  Total processing time:    $(format_duration $TOTAL_FILE_TIME)"
    echo "  Batch overhead:           $(format_duration $((BATCH_DURATION - TOTAL_FILE_TIME)))"
    echo "  Overall batch time:       $(format_duration $BATCH_DURATION)"
    echo ""
fi

echo "Files created per MP3:"
echo "  Intermediates (./intermediates/):"
IFS=',' read -ra TRANSCRIBER_ARRAY <<< "$TRANSCRIBERS"
for TRANSCRIBER in "${TRANSCRIBER_ARRAY[@]}"; do
    case "$TRANSCRIBER" in
        whisperx)
            echo "    - *_transcript_with_speakers.txt (whisperx)"
            ;;
        *)
            echo "    - *_${TRANSCRIBER}_transcript_with_speakers.txt"
            ;;
    esac
done
echo "  Final Output (./outputs/):"
IFS=',' read -ra PROCESSOR_ARRAY <<< "$PROCESSORS"
for TRANSCRIBER in "${TRANSCRIBER_ARRAY[@]}"; do
    for PROCESSOR in "${PROCESSOR_ARRAY[@]}"; do
        if [ "$TRANSCRIBER" = "whisperx" ]; then
            echo "    - *_${PROCESSOR}_corrected.txt"
        else
            echo "    - *_${TRANSCRIBER}_${PROCESSOR}_corrected.txt"
        fi
    done
done
echo ""
echo -e "${GREEN}Customize settings:${NC}"
echo "  Defaults: --transcribers whisperx --processors opus"
echo "  Example: $0 --transcribers assemblyai --processors opus,gemini"
echo ""
