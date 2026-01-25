# AI Providers for Transcript Post-Processing

All 11 AI models are accessed through **OpenRouter** with a single API key.
Get your key from: https://openrouter.ai/keys

## Quick Reference

| Processor | Model | OpenRouter ID | Context | Output |
|-----------|-------|---------------|---------|--------|
| **opus** | Claude Opus 4.5 | `anthropic/claude-opus-4.5` | 200K | 64K |
| **gemini** | Gemini 3 Pro | `google/gemini-3-pro-preview` | 1M | 64K |
| **chatgpt** | GPT-5.2 | `openai/gpt-5.2` | 400K | 128K |
| **grok** | Grok 4 | `x-ai/grok-4` | 256K | 8K |
| **qwen** | Qwen3-Max | `qwen/qwen3-max` | 256K | 8K |
| **kimi** | Kimi K2 | `moonshotai/kimi-k2` | 256K | 16K |
| **mistral** | Mistral Large | `mistralai/mistral-large-2411` | 256K | 8K |
| **minimax** | MiniMax M2.1 | `minimax/minimax-m2.1` | 4M | 8K |
| **llama** | Llama 4 Maverick | `meta-llama/llama-4-maverick:free` | 1M | 8K |
| **glm** | GLM-4.7 | `z-ai/glm-4.7` | 203K | 8K |
| **deepseek** | DeepSeek V3.2 | `deepseek/deepseek-chat` | 128K | 8K |

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

### Process Transcripts
```bash
# Single processor
python3 scripts/process_single_post_process.py transcript.txt --processors grok

# Multiple processors
python3 scripts/process_single_post_process.py transcript.txt --processors opus,gemini,grok

# All processors
python3 scripts/process_single_post_process.py transcript.txt --processors opus,gemini,deepseek,chatgpt,qwen,kimi,glm,minimax,llama,grok,mistral
```

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
- **Notes**: Open model, free tier available

#### MiniMax M2.1 (`minimax`)
- **Context**: 4M tokens (200K recommended)
- **Best For**: Extremely long documents
- **Notes**: Lightning Attention for linear scaling

### Tier 3: Cost-Effective

#### DeepSeek V3.2 (`deepseek`)
- **Context**: 128K tokens
- **Best For**: Budget-conscious processing
- **Notes**: 685B params, very competitive pricing

#### Kimi K2 (`kimi`)
- **Context**: 256K tokens
- **Best For**: Coding, long-context tasks
- **Notes**: $0.15/1M cache hits

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
2. **Llama 4 Maverick** - Free tier available
3. **Kimi K2** - Aggressive cache pricing

## OpenRouter Benefits

- **Single API key** for all 11 models
- **Unified billing** across providers
- **Automatic failover** if a provider is down
- **Pay-as-you-go** with no monthly minimums
- **~5% markup** over direct API pricing

## Architecture Notes

### MoE (Mixture of Experts)
Many models use MoE where only a subset of parameters are active:
- Llama 4 Maverick: 400B total, 17B active
- Kimi K2: 1T total, 32B active
- MiniMax M2.1: 230B total, 10B active
- Mistral Large: 675B total, 41B active
- DeepSeek V3.2: 685B total

### Lightning Attention (MiniMax)
MiniMax uses hybrid architecture:
- 7/8 layers: Lightning Attention (linear complexity)
- 1/8 layers: Traditional Softmax attention
- Enables 4M context without quadratic cost

*Document last updated: January 2026*
