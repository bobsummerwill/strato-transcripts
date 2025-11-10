# AI Post-Processing Provider Options

This guide explains the different AI providers available for transcript post-processing and helps you choose the best option for your needs.

## Quick Comparison

| Provider | Type | Cost | Quality | Speed | Privacy |
|----------|------|------|---------|-------|---------|
| **GPT-4o** (OpenAI) | Cloud | $$$ | Excellent | Fast | Low |
| **Claude 3.5** (Anthropic) | Cloud | $$$ | Excellent | Fast | Low |
| **Gemini 2.0** (Google) | Cloud | $$ | Excellent | Fast | Low |
| **DeepSeek** | Cloud | $ | Very Good | Fast | Low |
| **Moonshot Kimi** | Cloud | $$ | Very Good | Fast | Low |
| **Local LLM** (Ollama) | Local | FREE | Good-Excellent | Medium | Complete |

## Cloud Providers (API Required)

### 1. OpenAI (GPT-4o)
**Best for: Latest GPT-4o model, version-locked for reproducibility**

- **Models**: `gpt-4o-2024-11-20` (latest dated snapshot)
- **Cost**: ~$2.50-$5.00 per 1M input tokens
- **Quality**: Excellent reasoning, great at following instructions
- **Version-locked**: Uses dated snapshot for reproducible results
- **Setup**:
  ```bash
  export OPENAI_API_KEY="sk-..."
  python3 post_process_transcript.py transcript.txt --provider openai
  ```
- **Get API key**: https://platform.openai.com/api-keys

### 2. Anthropic (Claude 3.5 Sonnet)
**Best for: Long context, reasoning, safety**

- **Models**: `claude-3-5-sonnet-20241022` (October 22, 2024 release)
- **Cost**: ~$3.00 per 1M input tokens
- **Quality**: Excellent, particularly good at nuanced editing
- **Version-locked**: Uses dated snapshot for reproducible results
- **Setup**:
  ```bash
  export ANTHROPIC_API_KEY="sk-ant-..."
  python3 post_process_transcript.py transcript.txt --provider anthropic
  ```
- **Get API key**: https://console.anthropic.com/

### 3. Google (Gemini 2.0)
**Best for: Cutting-edge experimental features, competitive pricing**

- **Models**: `gemini-2.0-flash-exp`, `gemini-1.5-pro`, `gemini-1.5-flash`
- **Cost**: ~$0.075-$1.25 per 1M input tokens (very affordable)
- **Quality**: Excellent, Gemini 2.0 is very competitive
- **Setup**:
  ```bash
  export GOOGLE_API_KEY="..."
  python3 post_process_transcript.py transcript.txt --provider gemini
  ```
- **Get API key**: https://makersuite.google.com/app/apikey

### 4. DeepSeek (Online API)
**Best for: Cost-effectiveness, technical content**

- **Models**: `deepseek-chat`
- **Cost**: ~$0.14 per 1M input tokens (VERY CHEAP!)
- **Quality**: Very good, surprisingly competitive with GPT-4
- **Setup**:
  ```bash
  export DEEPSEEK_API_KEY="sk-..."
  python3 post_process_transcript.py transcript.txt --provider deepseek
  ```
- **Get API key**: https://platform.deepseek.com/

### 5. Moonshot Kimi K2-Instruct (Chinese Provider)
**Best for: Largest context windows (256K), no chunking needed**

- **Models**: `kimi-k2-instruct` (256K context window - LARGEST!)
- **Cost**: ~$0.50-1.00 per 1M input tokens (affordable)
- **Quality**: Very good, excellent for technical content
- **Context**: 256K context window (handles full transcripts without chunking)
- **Setup**:
  ```bash
  export MOONSHOT_API_KEY="sk-..."
  python3 post_process_transcript.py transcript.txt --provider moonshot
  ```
- **Get API key**: https://platform.moonshot.cn/
- **Note**: Chinese provider, OpenAI-compatible API, Kimi K2-Instruct-0905 has the largest context window of any provider

## Local Options (FREE, Private)

### 6. Ollama (Local LLM)
**Best for: Privacy, unlimited usage, no API costs**

**Recommended Models:**
- `qwen2.5:72b` - Best quality, excellent reasoning (requires 48GB+ VRAM)
- `llama3.1:70b` - Great all-around performance (requires 48GB+ VRAM)
- `qwen2.5:32b` - Good quality, lower requirements (24GB VRAM)
- `deepseek-r1:70b` - Excellent reasoning (requires 48GB+ VRAM)

**Your GPU**: RTX 3090 Ti (24GB VRAM)
- Can run: 32B models comfortably
- Can run: 70B models with quantization (Q4)

**Setup**:
1. Install Ollama: https://ollama.ai/
2. Pull a model: `ollama pull qwen2.5:32b`
3. Run processing:
   ```bash
   python3 post_process_transcript.py transcript.txt --provider ollama --ollama-model qwen2.5:32b
   ```

**Advantages:**
- ✅ Completely FREE
- ✅ Complete privacy (data never leaves your machine)
- ✅ Unlimited usage
- ✅ No internet required after model download
- ✅ Fast on good GPU

**Disadvantages:**
- ❌ Initial model download is large (20-50GB)
- ❌ Requires good GPU
- ❌ May be slightly less capable than latest cloud models

## Recommendations

### For Best Quality (Money No Object)
1. **GPT-4o** (`--provider openai`) - Version-locked to gpt-4o-2024-11-20
2. **Claude 3.5** (`--provider anthropic`)
3. **Gemini 2.0** (`--provider gemini`)

### For Best Value (Cloud)
1. **Gemini 2.5 Pro** (`--provider gemini`) - Fast & competitive
2. **DeepSeek** (`--provider deepseek`) - Cheapest, surprisingly good

### For Privacy/Unlimited Use
1. **Ollama + qwen2.5:32b** - Best fit for your GPU
2. **Ollama + llama3.1:70b** - If you're willing to use quantized version

### For Your Use Case (Ethereum Transcripts)
**Recommended**: Start with **Ollama + qwen2.5:32b**
- FREE unlimited processing
- Good quality for technical content
- Fits your 24GB VRAM perfectly
- Complete privacy for sensitive interviews

**Fallback**: Use **Gemini 2.5 Pro** for cloud processing when needed
- Very affordable
- Excellent quality/cost ratio

## Cost Estimates

For a typical 1-hour interview transcript (~50,000 tokens):

| Provider | Cost per Transcript |
|----------|---------------------|
| GPT-4o | ~$0.25 |
| Claude 3.5 | ~$0.15 |
| Gemini 2.0 Flash | ~$0.004 |
| DeepSeek | ~$0.007 |
| Moonshot | ~$0.05 |
| **Ollama (Local)** | **$0.00** |

For 100 transcripts:
- GPT-4o: $25
- Claude: $15
- Gemini: $0.40
- DeepSeek: $0.70
- Moonshot: $5.00
- **Ollama: $0**

## Installation Requirements

### Cloud Providers
```bash
# OpenAI
pip install openai

# Anthropic
pip install anthropic

# Google Gemini
pip install google-generativeai

# DeepSeek (uses OpenAI-compatible API)
pip install openai

# Moonshot (uses OpenAI-compatible API)
pip install openai
```

### Local (Ollama)
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull recommended model for your GPU (24GB VRAM)
ollama pull qwen2.5:32b

# Test it
ollama run qwen2.5:32b "Hello, world!"
```

## Next Steps

1. **Choose your provider** based on the above recommendations
2. **Set up API key** (for cloud) or **install Ollama** (for local)
3. **Test with a sample transcript**:
   ```bash
   python3 post_process_transcript.py outputs/sample_transcript.txt --provider <your-choice>
   ```
4. **Review the results** and adjust as needed

## Advanced: Running Large Models on Your GPU

Your RTX 3090 Ti (24GB) can run:

**Comfortably:**
- 32B models (full precision): `qwen2.5:32b`, `llama3.1:32b`
- 70B models (Q4 quantization): `qwen2.5:70b-instruct-q4_K_M`

**With optimization:**
```bash
# Pull quantized version for better performance
ollama pull qwen2.5:70b-instruct-q4_K_M

# Use it
python3 post_process_transcript.py transcript.txt \
  --provider ollama \
  --ollama-model qwen2.5:70b-instruct-q4_K_M
```

## Support

If you encounter issues:
- Cloud providers: Check API key and rate limits
- Ollama: Ensure service is running (`ollama serve`)
- GPU issues: Check VRAM usage (`nvidia-smi`)
