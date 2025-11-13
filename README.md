# Audio Transcription Pipeline with Multi-Provider AI Processing

Automated transcription with speaker diarization plus AI post-processing to correct technical terms and speaker names.

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

# 4. Batch process all MP3s
./scripts/process_all.sh --transcribers deepgram --processors sonnet
```

## Transcription Services

All services include speaker diarization (identifying who said what).

| Service | Model | Type | Cost/hour | Speed |
|---------|-------|------|-----------|-------|
| **WhisperX** | large-v3 | Local GPU | FREE | 5-10 min |
| **Deepgram** | nova-3-general | Cloud API | $0.41 | 23 sec |
| **AssemblyAI** | Best | Cloud API | $1.44 | 3-4 min |
| **Rev.ai** | v3 Human | Cloud API | $1.50 | ~3 min |
| **Sonix** | Standard | Cloud API | $10.00 | ~2 min |
| **Speechmatics** | Enhanced | Cloud API | $4.50 | ~1 min |

## AI Post-Processors

| Processor | Model | Cloud Service | Context | Cost (Input/Output) | Best For |
|-----------|-------|---------------|---------|---------------------|----------|
| **sonnet** | Claude Sonnet 4.5 | Anthropic | 200K | $3/$15 per MTok | Complex technical content, long transcripts |
| **chatgpt** | ChatGPT-4o-latest | OpenAI | 128K | $2.50/$10 per MTok | Latest flagship model, best text processing |
| **gemini** | Gemini 2.5 Pro | Google | 128K | ~$1.25 per MTok | Very long transcripts, multilingual |
| **llama** | Llama 3.3 70B | Groq | 128K | $0.59/$0.79 per MTok | ⚡ BLAZING FAST (300+ tok/s), Meta's latest |
| **kimi** | K2 Thinking | Novita | 262K | $0.60/$2.50 per MTok | Advanced reasoning, cost-effective |
| **qwen3max** | Qwen 3 Max | Novita | 128K | $2.11/$8.45 per MTok | Flagship Qwen model, strong reasoning |
| **deepseek** | DeepSeek Chat | DeepSeek | 64K | $0.27/$1.12 per MTok | Budget-friendly, good quality |
| **qwen** | Qwen2.5:7b | Ollama (local) | 32K | FREE | Local, private, 12GB GPU ⚠️ |

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

Processors: `sonnet`, `chatgpt`, `gemini`, `llama`, `kimi`, `qwen3max`, `deepseek`, `qwen`

## License

GPL-3.0 - See [LICENSE](LICENSE) file.
