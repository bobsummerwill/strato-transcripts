# AI Providers for Transcript Post-Processing

All 11 AI models are accessed through **OpenRouter** with a single API key.
Get your key from: https://openrouter.ai/keys

**Local Mode**: 5 models run locally via ollama on dual RTX 3090s (48GB).

## Hosted Models (OpenRouter)

| Processor | Model | OpenRouter ID | Context | Weights |
|-----------|-------|---------------|---------|---------|
| **opus** | Claude Opus 4.5 | `anthropic/claude-opus-4.5` | 200K | Closed |
| **gemini** | Gemini 3 Pro | `google/gemini-3-pro-preview` | 1M | Closed |
| **chatgpt** | GPT-5.2 | `openai/gpt-5.2` | 400K | Closed |
| **grok** | Grok 4 | `x-ai/grok-4` | 256K | Closed |
| **qwen** | Qwen3-Max | `qwen/qwen3-max` | 256K | Closed |
| **kimi** | Kimi K2.5 | `moonshotai/kimi-k2.5` | 256K | Open (1T) |
| **mistral** | Mistral Large | `mistralai/mistral-large-2411` | 256K | Open (675B) |
| **minimax** | MiniMax M2.1 | `minimax/minimax-m2.1` | 4M | Open (230B) |
| **llama** | Llama 4 Maverick | `meta-llama/llama-4-maverick` | 1M | Open (400B) |
| **deepseek** | DeepSeek V3.2 | `deepseek/deepseek-chat` | 128K | Open (671B) |
| **glm** | GLM-4.7 | `z-ai/glm-4.7` | 203K | Open (30B) |

## Local Models (ollama, fit on 48GB)

| Processor | Model | ollama ID | VRAM | Notes |
|-----------|-------|-----------|------|-------|
| **glm** | GLM-4.7-Flash | `glm-4.7-flash:q4_K_M` | ~19GB | Same as hosted, just local |
| **deepseek-local** | DeepSeek-R1 70B | `deepseek-r1:70b` | ~40GB | Distilled (not V3.2) |
| **qwen-local** | Qwen3 72B | `qwen3:72b` | ~45GB | Dense (not Max) |
| **mistral-local** | Mixtral 8x7B | `mixtral:8x7b` | ~27GB | MoE 47B (not Large) |
| **llama-local** | Llama 3.3 70B | `llama3.3:70b` | ~40GB | Llama 3.3 (not Llama 4) |

### Local-Only Models

The `-local` suffix models are **different model families** that fit on 48GB:
- `deepseek-local` → DeepSeek-R1 70B (reasoning distilled, not V3.2 671B)
- `qwen-local` → Qwen3 72B (dense, not Qwen3-Max)
- `mistral-local` → Mixtral 8x7B (47B MoE, not Mistral Large 675B)
- `llama-local` → Llama 3.3 70B (not Llama 4 Maverick 400B)

These are only available with `--mode local` and have no hosted equivalent.

### Why Full-Size Open Models Don't Fit Locally

MoE (Mixture of Experts) models need VRAM for ALL weights, not just active:
- **Kimi K2.5**: 1T total, 32B active → still needs ~373GB
- **Mistral Large**: 675B total, 41B active → still needs ~400GB
- **Llama 4 Maverick**: 400B total, 17B active → still needs ~243GB
- **DeepSeek V3.2**: 671B total, 37B active → still needs ~386GB

**GLM-4.7-Flash** is the exception: 30B total, 3B active → only ~19GB at Q4

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
python3 scripts/process_single_post_process.py transcript.txt --processors grok

# Multiple processors
python3 scripts/process_single_post_process.py transcript.txt --processors opus,gemini,grok

# All processors
python3 scripts/process_single_post_process.py transcript.txt --processors opus,gemini,deepseek,chatgpt,qwen,kimi,glm,minimax,llama,grok,mistral

# Explicit hosted mode
python3 scripts/process_single_post_process.py transcript.txt --processors grok --mode hosted
```

### Process Transcripts (Local Mode)
```bash
# Run GLM locally via ollama (requires 2x RTX 3090)
python3 scripts/process_single_post_process.py transcript.txt --processors glm --mode local

# Run large local models (70B+)
python3 scripts/process_single_post_process.py transcript.txt --processors deepseek-local --mode local
python3 scripts/process_single_post_process.py transcript.txt --processors qwen-local --mode local
python3 scripts/process_single_post_process.py transcript.txt --processors llama-local --mode local
python3 scripts/process_single_post_process.py transcript.txt --processors mistral-local --mode local

# Multiple local models (run sequentially)
python3 scripts/process_single_post_process.py transcript.txt --processors glm,deepseek-local,llama-local --mode local
```

**Note**: Local mode requires:
- 2x NVIDIA RTX 3090 GPUs (48GB total VRAM)
- ollama installed and running (`ollama serve`)
- Models pulled (see Local Model Setup below)

### Test Context Limits
```bash
python3 scripts/test_context_limits.py --providers opus,gemini,deepseek,chatgpt
python3 scripts/test_context_limits.py --providers all
```

## Model Details

### Tier 1: Premium Quality (Best Results)

#### Grok 4 (`grok`)
- **Ranking**: #1 on LMArena (1483 Elo)
- **Context**: 256K tokens
- **Best For**: Complex reasoning, highest benchmark performance
- **Notes**: Uses internal reasoning that consumes output tokens

#### Claude Opus 4.5 (`opus`)
- **Ranking**: Premium reasoning model
- **Context**: 200K tokens, 64K output
- **Best For**: Nuanced understanding, complex analysis
- **Notes**: Highest quality output

#### GPT-5.2 (`chatgpt`)
- **Ranking**: Strong all-around
- **Context**: 400K tokens, 128K output
- **Best For**: General-purpose, balanced performance

### Tier 2: Large Context (Long Documents)

#### Gemini 3 Pro (`gemini`)
- **Context**: 1M tokens, 64K output
- **Best For**: Very long documents, technical content
- **Notes**: Dynamic thinking by default

#### Llama 4 Maverick (`llama`)
- **Context**: 1M tokens
- **Best For**: Cost-effective processing of long documents
- **Notes**: Open model via Meta

#### MiniMax M2.1 (`minimax`)
- **Context**: 4M tokens (200K recommended)
- **Best For**: Extremely long documents
- **Notes**: Lightning Attention for linear scaling

### Tier 3: Cost-Effective

#### DeepSeek V3.2 (`deepseek`)
- **Context**: 128K tokens
- **Best For**: Budget-conscious processing
- **Notes**: 685B params, very competitive pricing

#### Kimi K2.5 (`kimi`)
- **Context**: 256K tokens
- **Best For**: Coding, long-context tasks, multimodal (text/image/video)
- **Notes**: $0.15/1M cache hits, can self-direct 100 sub-agents

### Tier 4: Specialized

#### Qwen3-Max (`qwen`)
- **Context**: 256K tokens
- **Best For**: Agent workflows, tool integration

#### GLM-4.7 (`glm`)
- **Context**: 203K tokens
- **Best For**: Chinese content, agentic tasks, coding
- **Notes**: Z.AI's latest flagship model via OpenRouter

#### Mistral Large (`mistral`)
- **Context**: 256K tokens
- **Best For**: European data sovereignty, efficient inference
- **Notes**: Open-weight model

## Recommendations

### For Typical Transcripts (60-90 min)
- **Word count**: ~10,000-15,000 words
- **Token count**: ~20,000-40,000 tokens
- **Total with prompts**: ~45,000 tokens

All 11 models have sufficient context for typical transcripts.

### Best Quality
1. **Grok 4** - #1 benchmark performance
2. **Claude Opus 4.5** - Premium reasoning
3. **GPT-5.2** - Strong all-around

### Best Value
1. **DeepSeek V3.2** - Low cost, good quality
2. **Llama 4 Maverick** - Open model, cost-effective
3. **Kimi K2.5** - Aggressive cache pricing

## OpenRouter Benefits

- **Single API key** for all 11 models
- **Unified billing** across providers
- **Automatic failover** if a provider is down
- **Pay-as-you-go** with no monthly minimums
- **~5% markup** over direct API pricing

## Local Mode (--mode local)

Run models locally via ollama instead of OpenRouter API.

### Hardware Requirements
- **Required**: 2x NVIDIA RTX 3090 (48GB total VRAM)
- **Hard fail**: Script exits if hardware not detected

### Available Local Models

| Processor | Model | VRAM | ollama pull command |
|-----------|-------|------|---------------------|
| `glm` | GLM-4.7-Flash | ~19GB | `ollama pull glm-4.7-flash:q4_K_M` |
| `deepseek-local` | DeepSeek-R1 70B | ~40GB | `ollama pull deepseek-r1:70b` |
| `qwen-local` | Qwen3 72B | ~45GB | `ollama pull qwen3:72b` |
| `mistral-local` | Mixtral 8x7B | ~27GB | `ollama pull mixtral:8x7b` |
| `llama-local` | Llama 3.3 70B | ~40GB | `ollama pull llama3.3:70b` |

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
python3 scripts/process_single_post_process.py transcript.txt --processors glm --mode local
python3 scripts/process_single_post_process.py transcript.txt --processors deepseek-local --mode local
```

## Architecture Notes

### MoE (Mixture of Experts)
Many models use MoE where only a subset of parameters are active:
- Llama 4 Maverick: 400B total, 17B active
- Kimi K2.5: 1T total, 32B active
- MiniMax M2.1: 230B total, 10B active
- Mistral Large: 675B total, 41B active
- DeepSeek V3.2: 685B total

### Lightning Attention (MiniMax)
MiniMax uses hybrid architecture:
- 7/8 layers: Lightning Attention (linear complexity)
- 1/8 layers: Traditional Softmax attention
- Enables 4M context without quadratic cost

*Document last updated: January 2026*
