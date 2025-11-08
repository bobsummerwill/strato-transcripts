#!/bin/bash
# ==============================================================================
# Batch Process All MP3 Files in ~/Downloads
# ==============================================================================
# - Transcribes with speaker diarization
# - Keeps speaker labels as SPEAKER_00, SPEAKER_01, etc
# - Generates markdown output for each file
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
OUTPUT_DIR="$PROJECT_DIR/outputs"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Batch MP3 Processing${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Activate environment
cd "$PROJECT_DIR"
source venv/bin/activate
source setup_env.sh

# Find all MP3 files
MP3_FILES=("$DOWNLOADS_DIR"/*.mp3)
TOTAL=${#MP3_FILES[@]}

if [ $TOTAL -eq 0 ]; then
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
declare -a TRANSCRIBE_TIMES
declare -a TOTAL_TIMES

# Overall timing
BATCH_START=$(date +%s)

# Process each file
COUNT=0
PROCESSED=0

for MP3_FILE in "${MP3_FILES[@]}"; do
    COUNT=$((COUNT + 1))
    BASENAME=$(basename "$MP3_FILE" .mp3)
    
    echo -e "${YELLOW}[$COUNT/$TOTAL] Processing: $BASENAME${NC}"
    
    # Output files
    TRANSCRIPT_FILE="${OUTPUT_DIR}/${BASENAME}_transcript_with_speakers.txt"
    MARKDOWN_FILE="${OUTPUT_DIR}/${BASENAME}_transcript.md"
    
    FILE_START=$(date +%s)
    
    # Transcribe with diarization (creates both .txt and .md)
    echo "  → Transcribing with speaker identification..."
    TRANSCRIBE_START=$(date +%s)
    python3 transcribe_with_diarization.py "$MP3_FILE" --output "$TRANSCRIPT_FILE"
    TRANSCRIBE_END=$(date +%s)
    TRANSCRIBE_DURATION=$((TRANSCRIBE_END - TRANSCRIBE_START))
    
    if [ -f "$TRANSCRIPT_FILE" ] && [ -f "$MARKDOWN_FILE" ]; then
        FILE_END=$(date +%s)
        FILE_DURATION=$((FILE_END - FILE_START))
        
        echo -e "${GREEN}  ✓ Complete${NC}"
        echo -e "     Text: $TRANSCRIPT_FILE"
        echo -e "     Markdown: $MARKDOWN_FILE"
        echo -e "     Time: $(format_duration $FILE_DURATION)"
        
        # Store timing data
        FILE_NAMES+=("$BASENAME")
        TRANSCRIBE_TIMES+=($TRANSCRIBE_DURATION)
        TOTAL_TIMES+=($FILE_DURATION)
        
        PROCESSED=$((PROCESSED + 1))
    else
        echo -e "${RED}  ✗ Error: Transcript files not created${NC}"
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
echo "  Processed: $PROCESSED"
echo "  Output location: $OUTPUT_DIR"
echo ""

if [ $PROCESSED -gt 0 ]; then
    echo -e "${BLUE}Timing Details:${NC}"
    echo ""
    
    # Calculate totals
    TOTAL_TRANSCRIBE=0
    TOTAL_FILE_TIME=0
    
    # Print per-file timing
    for i in "${!FILE_NAMES[@]}"; do
        echo -e "${YELLOW}${FILE_NAMES[$i]}${NC}"
        echo "  Processing time: $(format_duration ${TRANSCRIBE_TIMES[$i]})"
        echo ""
        
        TOTAL_TRANSCRIBE=$((TOTAL_TRANSCRIBE + ${TRANSCRIBE_TIMES[$i]}))
        TOTAL_FILE_TIME=$((TOTAL_FILE_TIME + ${TOTAL_TIMES[$i]}))
    done
    
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}Cumulative Totals:${NC}"
    echo "  Total processing time:    $(format_duration $TOTAL_TRANSCRIBE)"
    echo "  Batch overhead:           $(format_duration $((BATCH_DURATION - TOTAL_FILE_TIME)))"
    echo "  Overall batch time:       $(format_duration $BATCH_DURATION)"
    echo ""
fi

echo "Files created per MP3:"
echo "  - *_transcript_with_speakers.txt (raw transcript)"
echo "  - *_transcript.md (markdown formatted)"
echo ""
