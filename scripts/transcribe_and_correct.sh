#!/bin/bash
# Complete pipeline: Audio → WhisperX → AI Correction → Corrected Transcript
# Combines transcription with AI-powered post-processing (Claude or ChatGPT-5)

set -e  # Exit on error

# Check if audio file provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <audio_file> [options]"
    echo ""
    echo "Options:"
    echo "  --batch-size <n>     Batch size (default: 16 GPU, 8 CPU)"
    echo "  --provider <name>    AI provider (anthropic, openai, gemini, deepseek, ollama)"
    echo "                       Each provider uses its best model automatically"
    echo "  --skip-correction    Skip AI post-processing step"
    echo ""
    echo "Environment variables:"
    echo "  HF_TOKEN             HuggingFace token for WhisperX"
    echo "  ANTHROPIC_API_KEY    Anthropic API key (for Claude)"
    echo "  OPENAI_API_KEY       OpenAI API key (for ChatGPT-5/GPT-4o)"
    echo "  GOOGLE_API_KEY       Google API key (for Gemini)"
    echo "  DEEPSEEK_API_KEY     DeepSeek API key"
    echo "  (Ollama runs locally, no API key needed)"
    echo ""
    echo "Examples:"
    echo "  # Using OpenAI ChatGPT-5 (chatgpt-4o-latest)"
    echo "  $0 interview.mp3 --provider openai"
    echo ""
    echo "  # Using Gemini 1.5 Pro (best reasoning)"
    echo "  $0 interview.mp3 --provider gemini"
    echo ""
    echo "  # Using Ollama qwen2.5:32b (local, FREE, auto-managed)"
    echo "  $0 interview.mp3 --provider ollama"
    echo ""
    echo "  # Using DeepSeek Chat (very cost-effective)"
    echo "  $0 interview.mp3 --provider deepseek"
    echo ""
    echo "  # Transcription only (no correction)"
    echo "  $0 interview.mp3 --skip-correction"
    echo ""
    echo "  # Custom batch size for speed optimization"
    echo "  $0 interview.mp3 --batch-size 32"
    exit 1
fi

AUDIO_FILE="$1"
shift

# Default options
BATCH_SIZE=""
AI_PROVIDER="openai"  # Default to OpenAI ChatGPT-5
SKIP_CORRECTION=false

# Parse optional arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --batch-size)
            BATCH_SIZE="$2"
            shift 2
            ;;
        --provider)
            AI_PROVIDER="$2"
            shift 2
            ;;
        --skip-correction)
            SKIP_CORRECTION=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Check required tokens
if [ -z "${HF_TOKEN}" ]; then
    echo "Error: HF_TOKEN environment variable not set"
    echo "Get your token from: https://huggingface.co/settings/tokens"
    exit 1
fi

if [ "$SKIP_CORRECTION" = false ]; then
    if [ "$AI_PROVIDER" = "anthropic" ] && [ -z "${ANTHROPIC_API_KEY}" ]; then
        echo "Error: ANTHROPIC_API_KEY environment variable not set"
        echo "Get your key from: https://console.anthropic.com/"
        exit 1
    elif [ "$AI_PROVIDER" = "openai" ] && [ -z "${OPENAI_API_KEY}" ]; then
        echo "Error: OPENAI_API_KEY environment variable not set"
        echo "Get your key from: https://platform.openai.com/api-keys"
        exit 1
    elif [ "$AI_PROVIDER" = "gemini" ] && [ -z "${GOOGLE_API_KEY}" ]; then
        echo "Error: GOOGLE_API_KEY environment variable not set"
        echo "Get your key from: https://makersuite.google.com/app/apikey"
        exit 1
    elif [ "$AI_PROVIDER" = "deepseek" ] && [ -z "${DEEPSEEK_API_KEY}" ]; then
        echo "Error: DEEPSEEK_API_KEY environment variable not set"
        echo "Get your key from: https://platform.deepseek.com/"
        exit 1
    elif [ "$AI_PROVIDER" = "ollama" ]; then
        echo "Note: Using local Ollama (no API key needed)"
    fi
fi

# Check audio file exists
if [ ! -f "$AUDIO_FILE" ]; then
    echo "Error: Audio file not found: $AUDIO_FILE"
    exit 1
fi

echo "========================================================================"
echo "Complete Transcription Pipeline with AI Correction"
echo "========================================================================"
echo "Audio file: $AUDIO_FILE"
echo "Whisper model: large-v3 (hardcoded for best accuracy)"
echo "Compute type: float16 (optimal quality/VRAM balance)"
if [ -n "$BATCH_SIZE" ]; then
    echo "Batch size: $BATCH_SIZE"
fi
if [ "$SKIP_CORRECTION" = false ]; then
    echo "AI provider: $AI_PROVIDER"
    if [ "$AI_PROVIDER" = "openai" ]; then
        echo "  Model: chatgpt-4o-latest (auto-selected)"
    elif [ "$AI_PROVIDER" = "gemini" ]; then
        echo "  Model: gemini-1.5-pro (auto-selected)"
    elif [ "$AI_PROVIDER" = "deepseek" ]; then
        echo "  Model: deepseek-chat (auto-selected)"
    elif [ "$AI_PROVIDER" = "ollama" ]; then
        echo "  Model: qwen2.5:32b (auto-selected, auto-managed)"
    elif [ "$AI_PROVIDER" = "anthropic" ]; then
        echo "  Model: claude-3-5-sonnet (auto-selected)"
    fi
else
    echo "AI correction: DISABLED"
fi
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
# Format: filename_transcript_with_speakers.txt (no model indicator)
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

# Step 2: Post-process with AI (optional)
if [ "$SKIP_CORRECTION" = false ]; then
    echo "STEP 2: Post-processing with $AI_PROVIDER..."
    echo "------------------------------------------------------------------------"
    
    # Run post-processing (provider auto-selects best model)
    python3 scripts/post_process_transcript.py "$TRANSCRIPT_FULL" --provider "$AI_PROVIDER"
    
    if [ $? -ne 0 ]; then
        echo "Warning: Post-processing failed, but transcript is still available"
        CORRECTED=""
    else
        # Corrected files will be in outputs/ directory with provider name
        CORRECTED="outputs/${BASE_NAME}_${AI_PROVIDER}_corrected.txt"
        echo ""
        echo "✓ Corrected transcript: $CORRECTED"
    fi
else
    echo "STEP 2: Skipping post-processing (--skip-correction flag set)"
    CORRECTED=""
fi

echo ""
echo "========================================================================"
echo "✓ PIPELINE COMPLETE!"
echo "========================================================================"
echo ""
echo "Generated files:"
echo "  Intermediates (./intermediates/):"
echo "    - Raw transcript: $TRANSCRIPT_FULL"
if [ -n "$CORRECTED" ] && [ -f "$CORRECTED" ]; then
    echo "  Final Output (./outputs/):"
    echo "    - Corrected transcript: $CORRECTED"
    echo "    - Markdown version: ${CORRECTED%.txt}.md"
fi
echo ""
echo "========================================================================"
