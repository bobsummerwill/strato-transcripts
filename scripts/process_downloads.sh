#!/bin/bash
# ==============================================================================
# Batch Process All MP3 Files in ~/Downloads with Full AI Pipeline
# ==============================================================================
# - Loops through all MP3 files in ~/Downloads
# - Calls transcribe_and_correct.sh for each file (handles full pipeline)
# - Outputs to ./outputs directory
# ==============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Directories
PROJECT_DIR="/home/zombietiger/Projects/stratomercata-transcripts"
DOWNLOADS_DIR="/home/zombietiger/Downloads"
INTERMEDIATES_DIR="$PROJECT_DIR/intermediates"
OUTPUT_DIR="$PROJECT_DIR/outputs"

# Ensure directories exist
mkdir -p "$INTERMEDIATES_DIR"
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Batch MP3 Processing with AI Pipeline${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Activate environment
cd "$PROJECT_DIR"
source venv/bin/activate
source setup_env.sh

# Find all MP3 files
MP3_FILES=("$DOWNLOADS_DIR"/*.mp3)
TOTAL=${#MP3_FILES[@]}

if [ $TOTAL -eq 0 ] || [ ! -e "${MP3_FILES[0]}" ]; then
    echo -e "${RED}No MP3 files found in $DOWNLOADS_DIR${NC}"
    exit 1
fi

echo -e "${GREEN}Found $TOTAL MP3 files to process${NC}"
echo ""

# Timing function
format_duration() {
    local seconds=$1
    local hours=$((seconds / 3600))
    local minutes=$(((seconds % 3600) / 60))
    local secs=$((seconds % 60))
    
    if [ $hours -gt 0 ]; then
        printf "%dh %dm %ds" $hours $minutes $secs
    elif [ $minutes -gt 0 ]; then
        printf "%dm %ds" $minutes $secs
    else
        printf "%ds" $secs
    fi
}

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
    
    # Call transcribe_and_correct.sh with OpenAI provider from scripts directory
    if ./scripts/transcribe_and_correct.sh "$MP3_FILE" --provider openai; then
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
echo "    - *_transcript_with_speakers.txt (raw transcript)"
echo "    - *_transcript.md (raw markdown)"
echo "  Final Output (./outputs/):"
echo "    - *_corrected.txt (AI corrected)"
echo "    - *_corrected.md (AI corrected markdown)"
echo ""
