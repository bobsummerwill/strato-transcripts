#!/bin/bash
# ==============================================================================
# Single MP3 Transcription with Multi-Provider Pipeline
# ==============================================================================
# - Transcribes audio with specified transcription services
# - Runs AI correction with specified post-processors
# - Loops through ALL combinations (transcriber × processor)
# - Outputs to ./intermediates and ./outputs directories
# ==============================================================================

set -e

# Check if audio file provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <audio_file> --transcribers <t1,t2,...> --processors <p1,p2,...> [options]"
    echo ""
    echo "Required:"
    echo "  <audio_file>                Path to MP3 audio file"
    echo "  --transcribers <list>       Comma-separated transcription services"
    echo "                              (whisperx, deepgram, assemblyai, openai)"
    echo "  --processors <list>         Comma-separated AI post-processors"
    echo "                              (anthropic, openai, gemini, deepseek, moonshot, ollama)"
    echo ""
    echo "Optional:"
    echo "  --batch-size <n>            Batch size for WhisperX (default: 16 GPU, 8 CPU)"
    echo ""
    echo "Examples:"
    echo "  # Deepgram + Claude and Gemini"
    echo "  $0 interview.mp3 --transcribers deepgram --processors anthropic,gemini"
    echo ""
    echo "  # All transcribers × all processors (4 × 6 = 24 combinations!)"
    echo "  $0 interview.mp3 \\"
    echo "    --transcribers whisperx,deepgram,assemblyai,openai \\"
    echo "    --processors anthropic,openai,gemini,deepseek,moonshot,ollama"
    echo ""
    echo "  # WhisperX with Ollama only"
    echo "  $0 interview.mp3 --transcribers whisperx --processors ollama"
    exit 1
fi

AUDIO_FILE="$1"
shift

# Parse arguments
TRANSCRIBERS=""
PROCESSORS=""
BATCH_SIZE=""

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
        *)
            echo "Error: Unknown option: $1"
            exit 1
            ;;
    esac
done

# Require both transcribers and processors
if [ -z "$TRANSCRIBERS" ]; then
    echo "Error: --transcribers is required"
    echo "Specify one or more: whisperx, deepgram, assemblyai, openai"
    exit 1
fi

if [ -z "$PROCESSORS" ]; then
    echo "Error: --processors is required"
    echo "Specify one or more: anthropic, openai, gemini, deepseek, moonshot, ollama"
    exit 1
fi

# Convert comma-separated lists to arrays
IFS=',' read -ra TRANSCRIBER_ARRAY <<< "$TRANSCRIBERS"
IFS=',' read -ra PROCESSOR_ARRAY <<< "$PROCESSORS"

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

BASE_NAME=$(basename "$AUDIO_FILE" | sed 's/\.[^.]*$//')
TOTAL_COMBINATIONS=$((${#TRANSCRIBER_ARRAY[@]} * ${#PROCESSOR_ARRAY[@]}))

echo "========================================================================"
echo "Multi-Transcriber × Multi-Processor Pipeline"
echo "========================================================================"
echo "Audio file: $AUDIO_FILE"
echo "Transcribers: $TRANSCRIBERS (${#TRANSCRIBER_ARRAY[@]} services)"
for TRANSCRIBER in "${TRANSCRIBER_ARRAY[@]}"; do
    case "$TRANSCRIBER" in
        whisperx)
            echo "  - WhisperX: large-v3, float16 (local GPU)"
            ;;
        deepgram)
            echo "  - Deepgram: nova-2 (cloud, fastest)"
            ;;
        assemblyai)
            echo "  - AssemblyAI: universal-2 (cloud, high accuracy)"
            ;;
        openai)
            echo "  - OpenAI: whisper-1 (cloud)"
            ;;
    esac
done
echo "Processors: $PROCESSORS (${#PROCESSOR_ARRAY[@]} services)"
for PROCESSOR in "${PROCESSOR_ARRAY[@]}"; do
    case "$PROCESSOR" in
        openai)
            echo "  - OpenAI: gpt-4o-2024-11-20"
            ;;
        gemini)
            echo "  - Gemini: gemini-2.5-pro (2M context)"
            ;;
        ollama)
            echo "  - Ollama: qwen2.5:32b (local, FREE)"
            ;;
        anthropic)
            echo "  - Anthropic: claude-3-5-sonnet-20241022"
            ;;
        deepseek)
            echo "  - DeepSeek: deepseek-chat"
            ;;
        moonshot)
            echo "  - Moonshot: kimi-k2-instruct (256K context)"
            ;;
    esac
done
echo "Total combinations: ${#TRANSCRIBER_ARRAY[@]} × ${#PROCESSOR_ARRAY[@]} = $TOTAL_COMBINATIONS"
echo "========================================================================"
echo ""

# Clean up any leftover Ollama processes
echo "Cleaning up any leftover Ollama processes..."
ollama stop 2>/dev/null || true

SUCCESS_COUNT=0
FAILED_COUNT=0
SKIPPED_COUNT=0
declare -a TRANSCRIPT_FILES

# STEP 1: Run all transcriptions
echo "========================================================================"
echo "PHASE 1: Transcription (${#TRANSCRIBER_ARRAY[@]} services)"
echo "========================================================================"
echo ""

for i in "${!TRANSCRIBER_ARRAY[@]}"; do
    TRANSCRIBER="${TRANSCRIBER_ARRAY[$i]}"
    STEP_NUM=$((i + 1))
    
    echo "STEP 1.$STEP_NUM: Transcribing with $TRANSCRIBER..."
    echo "------------------------------------------------------------------------"
    
    # Run appropriate transcription script
    case "$TRANSCRIBER" in
        whisperx)
            CMD="python3 scripts/transcribe_with_diarization.py \"$AUDIO_FILE\""
            if [ -n "$BATCH_SIZE" ]; then
                CMD="$CMD --batch-size $BATCH_SIZE"
            fi
            TRANSCRIPT_FILE="intermediates/${BASE_NAME}_transcript_with_speakers.txt"
            ;;
        deepgram)
            if [ -z "${DEEPGRAM_API_KEY:-}" ]; then
                echo "⊘ DEEPGRAM_API_KEY not set, skipping $TRANSCRIBER"
                SKIPPED_COUNT=$((SKIPPED_COUNT + ${#PROCESSOR_ARRAY[@]}))
                continue
            fi
            CMD="python3 scripts/transcribe_with_deepgram.py \"$AUDIO_FILE\""
            TRANSCRIPT_FILE="intermediates/${BASE_NAME}_deepgram_transcript_with_speakers.txt"
            ;;
        assemblyai)
            if [ -z "${ASSEMBLYAI_API_KEY:-}" ]; then
                echo "⊘ ASSEMBLYAI_API_KEY not set, skipping $TRANSCRIBER"
                SKIPPED_COUNT=$((SKIPPED_COUNT + ${#PROCESSOR_ARRAY[@]}))
                continue
            fi
            CMD="python3 scripts/transcribe_with_assemblyai.py \"$AUDIO_FILE\""
            TRANSCRIPT_FILE="intermediates/${BASE_NAME}_assemblyai_transcript_with_speakers.txt"
            ;;
        openai)
            if [ -z "${OPENAI_API_KEY:-}" ]; then
                echo "⊘ OPENAI_API_KEY not set, skipping $TRANSCRIBER"
                SKIPPED_COUNT=$((SKIPPED_COUNT + ${#PROCESSOR_ARRAY[@]}))
                continue
            fi
            CMD="python3 scripts/transcribe_with_openai.py \"$AUDIO_FILE\""
            TRANSCRIPT_FILE="intermediates/${BASE_NAME}_openai_transcript_with_speakers.txt"
            ;;
        *)
            echo "Error: Unknown transcriber: $TRANSCRIBER"
            FAILED_COUNT=$((FAILED_COUNT + ${#PROCESSOR_ARRAY[@]}))
            continue
            ;;
    esac
    
    # Run transcription
    if eval $CMD; then
        if [ -f "$TRANSCRIPT_FILE" ]; then
            echo "✓ Transcript: $TRANSCRIPT_FILE"
            TRANSCRIPT_FILES+=("$TRANSCRIPT_FILE")
        else
            echo "✗ Expected transcript not found: $TRANSCRIPT_FILE"
            FAILED_COUNT=$((FAILED_COUNT + ${#PROCESSOR_ARRAY[@]}))
        fi
    else
        echo "✗ Transcription failed for $TRANSCRIBER"
        FAILED_COUNT=$((FAILED_COUNT + ${#PROCESSOR_ARRAY[@]}))
    fi
    
    echo ""
done

# STEP 2: Run all post-processing combinations
echo "========================================================================"
echo "PHASE 2: Post-Processing (${#TRANSCRIPT_FILES[@]} transcripts × ${#PROCESSOR_ARRAY[@]} processors)"
echo "========================================================================"
echo ""

COMBO_NUM=0
for TRANSCRIPT_FILE in "${TRANSCRIPT_FILES[@]}"; do
    for PROCESSOR in "${PROCESSOR_ARRAY[@]}"; do
        COMBO_NUM=$((COMBO_NUM + 1))
        
        echo "STEP 2.$COMBO_NUM: Processing with $PROCESSOR..."
        echo "  Input: $TRANSCRIPT_FILE"
        echo "------------------------------------------------------------------------"
        
        # Check API keys for cloud providers
        SKIP_PROCESSOR=false
        
        case "$PROCESSOR" in
            anthropic)
                if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
                    echo "⊘ ANTHROPIC_API_KEY not set, skipping"
                    SKIP_PROCESSOR=true
                fi
                ;;
            openai)
                if [ -z "${OPENAI_API_KEY:-}" ]; then
                    echo "⊘ OPENAI_API_KEY not set, skipping"
                    SKIP_PROCESSOR=true
                fi
                ;;
            gemini)
                if [ -z "${GOOGLE_API_KEY:-}" ]; then
                    echo "⊘ GOOGLE_API_KEY not set, skipping"
                    SKIP_PROCESSOR=true
                fi
                ;;
            deepseek)
                if [ -z "${DEEPSEEK_API_KEY:-}" ]; then
                    echo "⊘ DEEPSEEK_API_KEY not set, skipping"
                    SKIP_PROCESSOR=true
                fi
                ;;
            moonshot)
                if [ -z "${MOONSHOT_API_KEY:-}" ]; then
                    echo "⊘ MOONSHOT_API_KEY not set, skipping"
                    SKIP_PROCESSOR=true
                fi
                ;;
        esac
        
        if [ "$SKIP_PROCESSOR" = true ]; then
            SKIPPED_COUNT=$((SKIPPED_COUNT + 1))
            echo ""
            continue
        fi
        
        # Start Ollama if needed
        OLLAMA_STARTED=false
        if [ "$PROCESSOR" = "ollama" ]; then
            echo "Starting Ollama server..."
            ollama serve > /dev/null 2>&1 &
            OLLAMA_PID=$!
            OLLAMA_STARTED=true
            sleep 3
            echo "Ollama server started (PID: $OLLAMA_PID)"
        fi
        
        # Run post-processing
        python3 scripts/post_process_transcript.py "$TRANSCRIPT_FILE" --provider "$PROCESSOR"
        POST_EXIT=$?
        
        # Stop Ollama if we started it
        if [ "$OLLAMA_STARTED" = true ]; then
            echo "Stopping Ollama..."
            ollama stop 2>/dev/null || true
            kill $OLLAMA_PID 2>/dev/null || true
            wait $OLLAMA_PID 2>/dev/null || true
        fi
        
        if [ $POST_EXIT -ne 0 ]; then
            echo "✗ Post-processing failed"
            FAILED_COUNT=$((FAILED_COUNT + 1))
        else
            echo "✓ Post-processing complete"
            SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        fi
        
        echo ""
    done
done

# Summary
echo "========================================================================"
echo "✓ PIPELINE COMPLETE!"
echo "========================================================================"
echo ""
echo "Results:"
echo "  Total combinations: $TOTAL_COMBINATIONS"
echo "  Successful: $SUCCESS_COUNT"
echo "  Failed: $FAILED_COUNT"
echo "  Skipped (no API keys): $SKIPPED_COUNT"
echo ""
echo "Output files in:"
echo "  Transcripts: ./intermediates/"
echo "  Corrected: ./outputs/"
echo "========================================================================"

# Exit with error if any combinations failed
if [ $FAILED_COUNT -gt 0 ]; then
    exit 1
fi

if [ $SUCCESS_COUNT -eq 0 ]; then
    echo "Error: No combinations were successfully processed"
    exit 1
fi
