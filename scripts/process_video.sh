#!/bin/bash
# ==============================================================================
# Full Video Processing Pipeline
# ==============================================================================
# 1. Extract MP3 from MP4
# 2. Run WhisperX transcription
# 3. Convert transcript to SRT subtitles
# 4. Burn subtitles into new MP4
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Activate virtual environment and load API keys
source "$PROJECT_DIR/venv/bin/activate"
source "$PROJECT_DIR/setup_env.sh"

# Default values
TRANSCRIBER="whisperx"
PROCESSOR=""
FORCE_CPU=""
TITLE=""

usage() {
    echo "Usage: $0 <video.mp4> [options]"
    echo ""
    echo "Options:"
    echo "  --transcriber <name>   Transcription service (default: whisperx)"
    echo "                         Options: whisperx, whisperx-cloud, assemblyai"
    echo "  --processor <name>     AI post-processor (optional)"
    echo "                         Options: opus, gemini, deepseek, chatgpt"
    echo "  --force-cpu            Force CPU mode for WhisperX"
    echo "  --title <text>         Title overlay at top of screen"
    echo ""
    echo "Example:"
    echo "  $0 video.mp4"
    echo "  $0 video.mp4 --transcriber assemblyai"
    echo "  $0 video.mp4 --transcriber whisperx --processor opus"
    echo "  $0 video.mp4 --transcriber assemblyai --title 'Episode 7 - Jacob Czepluch'"
    exit 1
}

if [ $# -eq 0 ]; then
    usage
fi

VIDEO_FILE="$1"
shift

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --transcriber)
            TRANSCRIBER="$2"
            shift 2
            ;;
        --processor)
            PROCESSOR="$2"
            shift 2
            ;;
        --force-cpu)
            FORCE_CPU="--force-cpu"
            shift
            ;;
        --title)
            TITLE="$2"
            shift 2
            ;;
        *)
            echo "Error: Unknown option: $1"
            usage
            ;;
    esac
done

if [ ! -f "$VIDEO_FILE" ]; then
    echo "Error: Video file not found: $VIDEO_FILE"
    exit 1
fi

# Get base name without extension
VIDEO_BASE=$(basename "$VIDEO_FILE" .mp4)
VIDEO_DIR=$(dirname "$VIDEO_FILE")

# Output paths
AUDIO_FILE="${VIDEO_DIR}/${VIDEO_BASE}.mp3"
INTERMEDIATE_DIR="${PROJECT_DIR}/intermediates/${VIDEO_BASE}"
TRANSCRIPT_FILE="${INTERMEDIATE_DIR}/${VIDEO_BASE}_${TRANSCRIBER}.md"
SRT_FILE="${INTERMEDIATE_DIR}/${VIDEO_BASE}_${TRANSCRIBER}.srt"
OUTPUT_VIDEO="${VIDEO_DIR}/${VIDEO_BASE}_captioned.mp4"

echo "========================================================================"
echo "Video Processing Pipeline"
echo "========================================================================"
echo "Input:       $VIDEO_FILE"
echo "Transcriber: $TRANSCRIBER"
[ -n "$PROCESSOR" ] && echo "Processor:   $PROCESSOR"
[ -n "$TITLE" ] && echo "Title:       $TITLE"
echo "========================================================================"
echo ""

# Step 1: Extract audio
echo "[1/4] Extracting audio..."
if [ -f "$AUDIO_FILE" ]; then
    echo "  Audio file already exists: $AUDIO_FILE"
else
    "$SCRIPT_DIR/extract_audio.sh" "$VIDEO_FILE" "$AUDIO_FILE"
fi
echo ""

# Step 2: Run transcription
echo "[2/4] Running transcription with $TRANSCRIBER..."
TRANSCRIBE_CMD="python3 $SCRIPT_DIR/process_single_transcribe_and_diarize.py \"$AUDIO_FILE\" --transcribers \"$TRANSCRIBER\""
if [ -n "$FORCE_CPU" ]; then
    TRANSCRIBE_CMD="$TRANSCRIBE_CMD $FORCE_CPU"
fi

if [ -f "$TRANSCRIPT_FILE" ]; then
    echo "  Transcript already exists: $TRANSCRIPT_FILE"
else
    eval $TRANSCRIBE_CMD
fi
echo ""

# Step 3: Run post-processor if specified
if [ -n "$PROCESSOR" ]; then
    echo "[2.5/4] Running post-processor: $PROCESSOR..."
    python3 "$SCRIPT_DIR/process_single_post_process.py" "$TRANSCRIPT_FILE" --processors "$PROCESSOR"
    # Use processed transcript for subtitles
    PROCESSED_FILE="${PROJECT_DIR}/outputs/${VIDEO_BASE}/${VIDEO_BASE}_${TRANSCRIBER}_${PROCESSOR}.md"
    if [ -f "$PROCESSED_FILE" ]; then
        TRANSCRIPT_FILE="$PROCESSED_FILE"
        SRT_FILE="${INTERMEDIATE_DIR}/${VIDEO_BASE}_${TRANSCRIBER}_${PROCESSOR}.srt"
    fi
    echo ""
fi

# Step 4: Convert to subtitles (ASS format for colors)
echo "[3/4] Converting transcript to subtitles..."
SUBTITLE_CMD="python3 \"$SCRIPT_DIR/transcript_to_srt.py\" \"$TRANSCRIPT_FILE\" \"$SRT_FILE\""
if [ -n "$TITLE" ]; then
    SUBTITLE_CMD="$SUBTITLE_CMD --title \"$TITLE\""
fi
eval $SUBTITLE_CMD
ASS_FILE="${SRT_FILE%.srt}.ass"
echo ""

# Step 5: Burn subtitles into video (use ASS for color support)
echo "[4/4] Burning subtitles into video..."
ffmpeg -y -loglevel error -stats -i "$VIDEO_FILE" -vf "ass='$ASS_FILE'" -c:a copy "$OUTPUT_VIDEO"

echo ""
echo "========================================================================"
echo "Pipeline Complete!"
echo "========================================================================"
echo "Audio:      $AUDIO_FILE"
echo "Transcript: $TRANSCRIPT_FILE"
echo "Subtitles:  $SRT_FILE"
echo "Output:     $OUTPUT_VIDEO"
echo "========================================================================"
