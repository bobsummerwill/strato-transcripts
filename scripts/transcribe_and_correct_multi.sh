#!/bin/bash
# ==============================================================================
# Single MP3 Transcription with Multi-Provider AI Correction
# ==============================================================================
# - Transcribes audio once (common work)
# - Runs AI correction for specified providers (loop)
# - Outputs to ./intermediates and ./outputs directories
# ==============================================================================

set -e

# Check if audio file provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <audio_file> --providers <provider1,provider2,...> [options]"
    echo ""
    echo "Required:"
    echo "  <audio_file>             Path to MP3 audio file"
    echo "  --providers <list>       Comma-separated list of AI providers"
    echo "                           (anthropic, openai, gemini, deepseek, moonshot, ollama)"
    echo ""
    echo "Optional:"
    echo "  --batch-size <n>         Batch size for transcription (default: 16 GPU, 8 CPU)"
    echo ""
    echo "Examples:"
    echo "  # Generate OpenAI and Gemini corrections"
    echo "  $0 interview.mp3 --providers openai,gemini"
    echo ""
    echo "  # All providers"
    echo "  $0 interview.mp3 --providers anthropic,openai,gemini,deepseek,moonshot,ollama"
    echo ""
    echo "  # Single provider"
    echo "  $0 interview.mp3 --providers ollama"
    exit 1
fi

AUDIO_FILE="$1"
shift

# Parse arguments
PROVIDERS=""
BATCH_SIZE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --providers)
            PROVIDERS="$2"
            shift 2
            ;;
        --batch-size)
            BATCH_SIZE="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate providers parameter
if [ -z "$PROVIDERS" ]; then
    echo "Error: --providers parameter is required"
    echo "Example: $0 $AUDIO_FILE --providers openai,gemini"
    exit 1
fi

# Convert comma-separated list to array
IFS=',' read -ra PROVIDER_ARRAY <<< "$PROVIDERS"

# Check required environment variables
if [ -z "${HF_TOKEN}" ]; then
    echo "Error: HF_TOKEN environment variable not set"
    echo "Get your token from: https://huggingface.co/settings/tokens"
    exit 1
fi

# Check audio file exists
if [ ! -f "$AUDIO_FILE" ]; then
    echo "Error: Audio file not found: $AUDIO_FILE"
    exit 1
fi

echo "========================================================================"
echo "Transcription Pipeline with Multi-Provider AI Correction"
echo "========================================================================"
echo "Audio file: $AUDIO_FILE"
echo "Whisper model: large-v3 (hardcoded for best accuracy)"
echo "Compute type: float16 (optimal quality/VRAM balance)"
if [ -n "$BATCH_SIZE" ]; then
    echo "Batch size: $BATCH_SIZE"
fi
echo "AI providers: $PROVIDERS (${#PROVIDER_ARRAY[@]} total)"
for PROVIDER in "${PROVIDER_ARRAY[@]}"; do
    case "$PROVIDER" in
        openai)
            echo "  - OpenAI: chatgpt-4o-latest"
            ;;
        gemini)
            echo "  - Gemini: gemini-2.5-pro (latest)"
            ;;
        ollama)
            echo "  - Ollama: qwen2.5:32b (auto-managed)"
            ;;
        anthropic)
            echo "  - Anthropic: claude-sonnet-4-5 (latest)"
            ;;
        deepseek)
            echo "  - DeepSeek: deepseek-chat"
            ;;
        moonshot)
            echo "  - Moonshot: moonshot-v1-128k (128K context)"
            ;;
    esac
done
echo "========================================================================"
echo ""

# Step 1: Transcribe with WhisperX
echo "STEP 1: Transcribing with WhisperX (float16 quantization, large-v3)..."
echo "------------------------------------------------------------------------"

# Build command with optional batch size
CMD="python3 scripts/transcribe_with_diarization.py \"$AUDIO_FILE\""
if [ -n "$BATCH_SIZE" ]; then
    CMD="$CMD --batch-size $BATCH_SIZE"
fi

eval $CMD

if [ $? -ne 0 ]; then
    echo "Error: Transcription failed"
    exit 1
fi

# Find the generated transcript file in intermediates
BASE_NAME=$(basename "$AUDIO_FILE" | sed 's/\.[^.]*$//')
TRANSCRIPT="intermediates/${BASE_NAME}_transcript_with_speakers.txt"

if [ ! -f "$TRANSCRIPT" ]; then
    echo "Error: Could not find generated transcript: $TRANSCRIPT"
    exit 1
fi

TRANSCRIPT_FULL="$TRANSCRIPT"

echo ""
echo "✓ Transcription complete: $TRANSCRIPT_FULL"
echo ""

# Step 2: Post-process with each AI provider
echo "STEP 2: Post-processing with AI providers..."
echo "------------------------------------------------------------------------"

# Clean up any leftover Ollama processes from previous runs
echo "Cleaning up any leftover Ollama processes..."
ollama stop 2>/dev/null || true

SUCCESS_COUNT=0
FAILED_COUNT=0
SKIPPED_COUNT=0

for i in "${!PROVIDER_ARRAY[@]}"; do
    PROVIDER="${PROVIDER_ARRAY[$i]}"
    STEP_NUM=$((i + 1))
    
    echo ""
    echo "STEP 2.$STEP_NUM: Post-processing with $PROVIDER..."
    echo "------------------------------------------------------------------------"
    
    # Check API keys for cloud providers (skip if undefined or empty)
    SKIP_PROVIDER=false
    
    if [ "$PROVIDER" = "anthropic" ]; then
        if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
            echo "⊘ ANTHROPIC_API_KEY not defined or empty, skipping $PROVIDER"
            SKIP_PROVIDER=true
        fi
    elif [ "$PROVIDER" = "openai" ]; then
        if [ -z "${OPENAI_API_KEY:-}" ]; then
            echo "⊘ OPENAI_API_KEY not defined or empty, skipping $PROVIDER"
            SKIP_PROVIDER=true
        fi
    elif [ "$PROVIDER" = "gemini" ]; then
        if [ -z "${GOOGLE_API_KEY:-}" ]; then
            echo "⊘ GOOGLE_API_KEY not defined or empty, skipping $PROVIDER"
            SKIP_PROVIDER=true
        fi
    elif [ "$PROVIDER" = "deepseek" ]; then
        if [ -z "${DEEPSEEK_API_KEY:-}" ]; then
            echo "⊘ DEEPSEEK_API_KEY not defined or empty, skipping $PROVIDER"
            SKIP_PROVIDER=true
        fi
    elif [ "$PROVIDER" = "moonshot" ]; then
        if [ -z "${MOONSHOT_API_KEY:-}" ]; then
            echo "⊘ MOONSHOT_API_KEY not defined or empty, skipping $PROVIDER"
            SKIP_PROVIDER=true
        fi
    fi
    
    # Skip if credentials are missing (don't count as failure)
    if [ "$SKIP_PROVIDER" = true ]; then
        SKIPPED_COUNT=$((SKIPPED_COUNT + 1))
        continue
    fi
    
    # Start Ollama if this provider needs it
    OLLAMA_STARTED=false
    if [ "$PROVIDER" = "ollama" ]; then
        echo "Starting Ollama server..."
        ollama serve > /dev/null 2>&1 &
        OLLAMA_PID=$!
        OLLAMA_STARTED=true
        # Give Ollama time to start
        sleep 3
        echo "Ollama server started (PID: $OLLAMA_PID)"
    fi
    
    # Run post-processing
    python3 scripts/post_process_transcript.py "$TRANSCRIPT_FULL" --provider "$PROVIDER"
    POST_PROCESS_EXIT=$?
    
    # Stop Ollama if we started it
    if [ "$OLLAMA_STARTED" = true ]; then
        echo "Stopping Ollama server..."
        ollama stop 2>/dev/null || true
        # Also kill the serve process if still running
        kill $OLLAMA_PID 2>/dev/null || true
        wait $OLLAMA_PID 2>/dev/null || true
        echo "Ollama server stopped"
    fi
    
    if [ $POST_PROCESS_EXIT -ne 0 ]; then
        echo "✗ Post-processing failed for $PROVIDER"
        FAILED_COUNT=$((FAILED_COUNT + 1))
    else
        CORRECTED="outputs/${BASE_NAME}_${PROVIDER}_corrected.txt"
        echo ""
        echo "✓ Corrected transcript: $CORRECTED"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    fi
done

echo ""
echo "========================================================================"
echo "✓ PIPELINE COMPLETE!"
echo "========================================================================"
echo ""
echo "Generated files:"
echo "  Intermediates (./intermediates/):"
echo "    - Raw transcript: $TRANSCRIPT_FULL"
echo "  Final Output (./outputs/):"
echo "    - Successfully processed: $SUCCESS_COUNT/${#PROVIDER_ARRAY[@]} providers"
if [ $SKIPPED_COUNT -gt 0 ]; then
    echo "    - Skipped (no credentials): $SKIPPED_COUNT providers"
fi
if [ $FAILED_COUNT -gt 0 ]; then
    echo "    - Failed (processing errors): $FAILED_COUNT providers"
fi
for PROVIDER in "${PROVIDER_ARRAY[@]}"; do
    OUTPUT_FILE="outputs/${BASE_NAME}_${PROVIDER}_corrected.txt"
    if [ -f "$OUTPUT_FILE" ]; then
        echo "      ✓ ${PROVIDER}: $OUTPUT_FILE"
    fi
done
echo ""
echo "========================================================================"

# Exit with error only if processing failed (not if providers were skipped)
if [ $FAILED_COUNT -gt 0 ]; then
    echo "Error: $FAILED_COUNT provider(s) failed during processing"
    exit 1
fi

# Exit successfully even if some providers were skipped
if [ $SUCCESS_COUNT -eq 0 ]; then
    echo "Warning: No providers were successfully processed"
    exit 1
fi
