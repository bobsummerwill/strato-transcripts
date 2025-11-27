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
./scripts/process_single.sh audio.mp3 --transcribers whisperx --processors chatgpt

# 3. Multiple combinations (2 transcribers × 3 processors = 6 outputs)
./scripts/process_single.sh audio.mp3 --transcribers whisperx,deepgram --processors sonnet,chatgpt,llama

# 4. Cloud WhisperX (paid but no local GPU required)
./scripts/process_single.sh audio.mp3 --transcribers whisperx-cloud --processors chatgpt

# 4. Batch process all MP3s
./scripts/process_all.sh --transcribers deepgram --processors sonnet
```

## Transcription Services

All services include speaker diarization (identifying who said what).

| Service | Model | Type | Cost/hour | Speed |
|---------|--------|------|-----------|-------|
| **WhisperX** | large-v3 | Local GPU | FREE | 5-10 min |
| **WhisperX-Cloud** | large-v3 | Cloud API | $2.88 | 2-3 min |
| **Deepgram** | nova-3-general | Cloud API | $0.27 | 23 sec |
| **AssemblyAI** | Best | Cloud API | $1.08 | 3-4 min |

## AI Post-Processors

| Processor | Model | Cloud Service | Context Limit | Cost (Input/Output) | Best For |
|-----------|------------|---------------|---------------|---------------------|----------|
| **opus** | Claude Opus 4.5 | Anthropic | **150K** | $15/$75 per MTok | **PREMIUM QUALITY** - Best reasoning, long context |
| **sonnet** | Claude Sonnet 4.5 | Anthropic | **150K** | $3/$15 per MTok | **BALANCED** - Excellent quality, reliable |
| **gemini** | Gemini 3.0 Pro | Google | **128K** | ~$1.25 per MTok | **TECHNICAL** - Superior technical preservation |
| **chatgpt** | GPT-4o | OpenAI | **120K** | $2.50/$10 per MTok | **GENERAL** - Solid all-around performance |
| **llama** | Llama 3.3 70B | Groq | **128K** | $0.59/$0.79 per MTok | ⚡ **ULTRAFAST** (300+ tok/s), Meta's latest |
| **qwen-cloud** | Qwen3 32B | Groq | **128K** | $0.08/$0.08 per MTok | 🔬 **MAXIMUM QUALITY** for technical content |
| **qwen** | Qwen2.5:14B | Ollama (local) | 32K | FREE | 🎮 **LOCAL GPU** (8GB+ VRAM), private/offline |

## Setup

**Requirements:**
- Minimum: 8GB RAM, 50GB disk (CPU-only, slow)
- Recommended: NVIDIA GPU 6GB+ VRAM, 16GB RAM, 50GB disk

**API Keys in `setup_env.sh`:**
```bash
export HF_TOKEN="hf_..."              # Required for WhisperX diarization
export DEEPGRAM_API_KEY="..."         # Optional transcription services
export ANTHROPIC_API_KEY="sk-ant-..."  # Optional AI processors
export OPENAI_API_KEY="sk-..."
export GROQ_API_KEY="gsk_..."
```

## Output Files

**Naming:** `{basename}_{transcriber}_{processor}_processed.{txt|md}`

Example: `interview_deepgram_llama_processed.txt`

Processors: `sonnet`, `chatgpt`, `gemini`, `llama`, `qwen-cloud`, `qwen`

## License

GPL-3.0 - See [LICENSE](LICENSE) file.
