# AI Providers for Transcript Post-Processing

All 3 hosted models are accessed through **OpenRouter** with a single API key.
Get your key from: https://openrouter.ai/keys

**Local Mode**: 5 models run locally via ollama on dual RTX 3090s (48GB).

## Hosted Models (OpenRouter)

| Processor | Model | OpenRouter ID | Context | Weights |
|-----------|-------|---------------|---------|---------|
| **opus** | Claude Opus 4.6 | `anthropic/claude-opus-4.6` | 1M | Closed |
| **gemini** | Gemini 3.1 Pro | `google/gemini-3.1-pro-preview` | 1M | Closed |
| **grok** | Grok 4 | `x-ai/grok-4` | 256K | Closed |

## Local Models (ollama, fit on 48GB)

| Processor | Model | ollama ID | VRAM | Notes |
|-----------|-------|-----------|------|-------|
| **glm** | GLM-4.7-Flash | `glm-4.7-flash:q4_K_M` | ~19GB | Same as hosted, just local |
| **deepseek-local** | DeepSeek-R1 70B | `deepseek-r1:70b` | ~40GB | Distilled (not V3.2) |
| **qwen-local** | Qwen3 72B | `qwen3:72b` | ~45GB | Dense (not Max) |
| **mistral-local** | Mixtral 8x7B | `mixtral:8x7b` | ~27GB | MoE 47B (not Large) |
| **llama-local** | Llama 3.3 70B | `llama3.3:70b` | ~40GB | Llama 3.3 (not Llama 4) |

## Setup

### 1. Get OpenRouter API Key
Sign up at https://openrouter.ai and create an API key.

### 2. Configure Environment
```bash
# Edit setup_env.sh and add your key
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"

# Source the environment
source setup_env.sh
```

### 3. Test Connection
```bash
python3 scripts/test_ai_providers.py
```

## Usage

### Process Transcripts (Hosted Mode - Default)
```bash
# Single processor
python3 scripts/process_single_post_process.py transcript.md --processors opus

# All hosted processors
python3 scripts/process_single_post_process.py transcript.md --processors opus,gemini,grok

# Explicit hosted mode
python3 scripts/process_single_post_process.py transcript.md --processors grok --mode hosted
```

### Process Transcripts (Local Mode)
```bash
# Run GLM locally via ollama (requires 2x RTX 3090)
python3 scripts/process_single_post_process.py transcript.md --processors glm --mode local

# Run large local models (70B+)
python3 scripts/process_single_post_process.py transcript.md --processors deepseek-local --mode local
python3 scripts/process_single_post_process.py transcript.md --processors qwen-local --mode local
python3 scripts/process_single_post_process.py transcript.md --processors llama-local --mode local
python3 scripts/process_single_post_process.py transcript.md --processors mistral-local --mode local

# Multiple local models (run sequentially)
python3 scripts/process_single_post_process.py transcript.md --processors glm,deepseek-local,llama-local --mode local
```

**Note**: Local mode requires:
- 2x NVIDIA RTX 3090 GPUs (48GB total VRAM)
- ollama installed and running (`ollama serve`)
- Models pulled (see Local Model Setup below)

### Test Context Limits
```bash
python3 scripts/test_context_limits.py --providers opus,gemini,grok
python3 scripts/test_context_limits.py --providers all
```

## Model Details

### Claude Opus 4.6 (`opus`)
- **Context**: 1M tokens, 128K output
- **Best For**: Premium quality, nuanced understanding
- **Notes**: Highest quality output, consistently Tier 1 across episodes

### Grok 4 (`grok`)
- **Context**: 256K tokens
- **Best For**: Complex reasoning, high benchmark performance
- **Notes**: Uses internal reasoning that consumes output tokens

### Gemini 3.1 Pro (`gemini`)
- **Context**: 1M tokens, 64K output
- **Best For**: Very long documents, technical content
- **Notes**: Dynamic thinking by default

## Recommendations

### For Typical Transcripts (60-90 min)
- **Word count**: ~10,000-15,000 words
- **Token count**: ~20,000-40,000 tokens
- **Total with prompts**: ~45,000 tokens

All 3 models have sufficient context for typical transcripts.

### Best Quality
1. **Claude Opus 4.6** - Consistently Tier 1 in 13/15 episodes
2. **Grok 4** - Strong benchmark performance
3. **Gemini 3.1 Pro** - Reliable, good for long content

## OpenRouter Benefits

- **Single API key** for all 3 models
- **Unified billing** across providers
- **Automatic failover** if a provider is down
- **Pay-as-you-go** with no monthly minimums

## Local Mode (--mode local)

Run models locally via ollama instead of OpenRouter API.

### Hardware Requirements
- **Required**: 2x NVIDIA RTX 3090 (48GB total VRAM)
- **Hard fail**: Script exits if hardware not detected

### Local Model Setup
```bash
# Install ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start ollama server
ollama serve

# Pull the models you want to use
ollama pull glm-4.7-flash:q4_K_M     # GLM-4.7-Flash (~19GB)
ollama pull deepseek-r1:70b           # DeepSeek-R1 70B (~40GB)
ollama pull qwen3:72b                 # Qwen3 72B (~45GB)
ollama pull mixtral:8x7b              # Mixtral 8x7B (~27GB)
ollama pull llama3.3:70b              # Llama 3.3 70B (~40GB)

# Test local mode
python3 scripts/process_single_post_process.py transcript.md --processors glm --mode local
python3 scripts/process_single_post_process.py transcript.md --processors deepseek-local --mode local
```

*Document last updated: February 2026*
