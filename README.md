# Audio Transcription Pipeline with Multi-Provider AI Processing

Transcription with speaker diarization plus AI post-processing for technical term correction.

## Usage

```bash
# 1. Setup (one time)
./scripts/install_packages_and_venv.sh
cp setup_env.sh.example setup_env.sh
nano setup_env.sh  # Add API keys

# 2. Process single file
source venv/bin/activate && source setup_env.sh
./scripts/process_single.sh audio.mp3 --transcribers whisperx --processors opus

# 3. Multiple combinations (2 transcribers × 2 processors = 4 outputs)
./scripts/process_single.sh audio.mp3 --transcribers whisperx,assemblyai --processors opus,gemini

# 4. Cloud WhisperX (paid but no local GPU required)
./scripts/process_single.sh audio.mp3 --transcribers whisperx-cloud --processors opus

# 5. Batch process all MP3s
./scripts/process_all.sh --transcribers assemblyai --processors opus
```

## Transcription Services

All services include speaker diarization (identifying who said what).

| Service | Model | Type | Cost/hour | Speed |
|---------|--------|------|-----------|-------|
| **WhisperX** | large-v3 | Local GPU | FREE | 5-10 min |
| **WhisperX-Cloud** | large-v3 | Cloud API | $2.88 | 2-3 min |
| **AssemblyAI** | Best | Cloud API | $1.08 | 3-4 min |

## AI Post-Processors

| Processor | Model | Cloud Service | Context Limit | Cost (Input/Output) | Best For |
|-----------|------------|---------------|---------------|---------------------|----------|
| **opus** | Claude Opus 4.5 | Anthropic | **150K** | $15/$75 per MTok | **PREMIUM QUALITY** - Best reasoning, long context |
| **gemini** | Gemini 3.0 Pro | Google | **128K** | ~$1.25 per MTok | **TECHNICAL** - Superior technical preservation |
| **deepseek** | DeepSeek-V3.2 | DeepSeek | **128K** | $0.28/$0.42 per MTok | **COST-EFFECTIVE** - Great quality at lowest cost |

## Setup

**Requirements:**
- Minimum: 8GB RAM, 50GB disk (CPU-only, slow)
- Recommended: NVIDIA GPU 6GB+ VRAM, 16GB RAM, 50GB disk

**API Keys in `setup_env.sh`:**
```bash
export HF_TOKEN="hf_..."              # Required for WhisperX diarization
export ANTHROPIC_API_KEY="sk-ant-..." # For Claude Opus post-processing
export GOOGLE_API_KEY="..."           # For Gemini post-processing
export DEEPSEEK_API_KEY="..."         # For DeepSeek post-processing
export ASSEMBLYAI_API_KEY="..."       # Optional: AssemblyAI transcription
export REPLICATE_API_TOKEN="..."      # Optional: Cloud WhisperX
```

## Output Files

**Naming:** `{basename}_{transcriber}_{processor}.{txt|md}`

Example: `interview_assemblyai_opus.txt`

**Transcribers:** `whisperx`, `whisperx-cloud`, `assemblyai`

**Processors:** `opus`, `gemini`, `deepseek`

## License

GPL-3.0 - See [LICENSE](LICENSE) file.
