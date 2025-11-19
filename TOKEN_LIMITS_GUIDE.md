# Token Limits and Context Windows - Complete Guide

## Understanding Context Window vs Output Tokens

### Context Window (Input)
- **What it is:** How much text the AI model can READ and process
- **Includes:** Your prompt + instructions + context + the transcript you're processing
- **Example:** A 128K context window can hold ~100,000 words of input text

### Output Tokens (Generation)
- **What it is:** How much text the AI model can WRITE in its response
- **Separate limit:** Independent from context window
- **Example:** 16K output tokens = ~12,000 words the model can generate

### Real-World Example
For an 87-minute Ethereum transcript (~30,000 words):
- **Input required:** ~40K tokens (instructions + context + transcript)
- **Output needed:** ~35K tokens (cleaned, formatted transcript)
- **GPT-4.1:** ✅ 128K context (plenty) + 32K output (fits perfectly)
- **ChatGPT-4o:** ✅ 128K context, but ❌ only 16K output (too small, gets truncated)

This is why you downgraded from ChatGPT-5 to GPT-4.1 - you needed the 32K output capacity.

---

## Transcription Services (Speech-to-Text)

Transcription services convert audio to text. These have different limits:

| Service | Max Audio Length | Max File Size | Diarization | Notes |
|---------|-----------------|---------------|-------------|-------|
| **WhisperX** (local) | Unlimited* | Unlimited* | ✅ Yes | *Limited by GPU/RAM, processes in chunks |
| **AssemblyAI** | ~12 hours | 2.2 GB | ✅ Yes | Automatic chunking for longer files |
| **Deepgram** | ~3 hours per request | 2 GB | ✅ Yes | Can be extended with streaming |
| **OpenAI Whisper** | 25 MB file | 25 MB | ❌ No | Not used in this project |

### For Long Transcripts (87 minutes = 1.45 hours)
All services handle your Ethereum transcripts fine:
- WhisperX: ✅ No problem (local processing)
- AssemblyAI: ✅ Well within 12-hour limit
- Deepgram: ✅ Well within 3-hour limit

---

## Post-Processing AI Services

These services clean up the raw transcript (fix capitalization, technical terms, etc.)

### Context Window Limits (INPUT)

How much transcript text each service can READ/process at once:

| Service | Model | Context Window | Can Handle 87-min Transcript? |
|---------|-------|----------------|------------------------------|
| **Claude Sonnet** | claude-sonnet-4-5 | 200K tokens (~150K words) | ✅ Yes, easily |
| **GPT-4.1** | gpt-4.1 | 128K tokens (~100K words) | ✅ Yes |
| **ChatGPT-4o** | chatgpt-4o-latest | 128K tokens (~100K words) | ✅ Yes |
| **Gemini** | gemini-2.5-pro | 2M tokens (~1.5M words) | ✅ Yes, massive capacity |
| **Llama** (Groq) | llama-3.3-70b | 128K tokens (~100K words) | ✅ Yes |
| **Qwen** (local) | qwen2.5:14b | 32K tokens (~24K words) | ⚠️ Marginal, may need chunking |

### Output Token Limits (GENERATION)

How much cleaned text each service can WRITE:

| Service | Model | Output Tokens | Can Output Full Transcript? |
|---------|-------|---------------|----------------------------|
| **Claude Sonnet** | claude-sonnet-4-5 | 64K tokens (~48K words) | ✅ Yes, plenty of headroom |
| **GPT-4.1** | gpt-4.1 | 32K tokens (~24K words) | ✅ Yes, fits 87-min transcript |
| **ChatGPT-4o** | chatgpt-4o-latest | 16K tokens (~12K words) | ❌ NO - This is why you switched! |
| **Gemini** | gemini-2.5-pro | 8K tokens (~6K words) | ❌ NO - Too small for long transcripts |
| **Llama** (Groq) | llama-3.3-70b | 32K tokens (~24K words) | ✅ Yes, same as GPT-4.1 |
| **Qwen** (local) | qwen2.5:14b | 32K tokens (~24K words) | ✅ Yes, if input fits |

### Your Transcript Requirements

For an 87-minute Ethereum episode (Christoph Jentzsch example):
- **Raw transcript:** ~30,000 words
- **Input tokens needed:** ~40K (includes instructions + context)
- **Output tokens needed:** ~35K-40K (cleaned transcript)

### Why You Chose GPT-4.1

| Aspect | ChatGPT-5 | ChatGPT-4o | GPT-4.1 | Your Choice |
|--------|-----------|------------|---------|-------------|
| Context (input) | Unknown | 128K ✅ | 128K ✅ | All support input |
| Output tokens | Unknown | 16K ❌ | 32K ✅ | **GPT-4.1 wins** |
| Can complete 87-min transcript | Unknown | ❌ Truncates | ✅ Complete | **GPT-4.1** |
| Cost | Unknown | $2.50/$10 | $2.50/$10 | Same as 4o |

---

## Recommended Configurations by Transcript Length

### Short Transcripts (< 30 minutes, ~10K words output)
**All services work:**
- Budget: Llama (Groq) - fastest and cheapest
- Quality: Claude Sonnet - best for technical content
- Local: Qwen - free, private, GPU-only

### Medium Transcripts (30-60 minutes, ~10-20K words output)
**Most services work:**
- ✅ Claude Sonnet (64K output)
- ✅ GPT-4.1 (32K output)
- ✅ Llama via Groq (32K output)
- ⚠️ Gemini (8K output - may truncate)
- ❌ ChatGPT-4o (16K output - will truncate)

### Long Transcripts (60-120 minutes, ~20-40K words output)
**Limited options:**
- ✅ **Claude Sonnet** - Best choice (64K output, plenty of headroom)
- ✅ **GPT-4.1** - Good choice (32K output, tight but works)
- ✅ **Llama via Groq** - Budget choice (32K output, very fast)
- ❌ ChatGPT-4o - Will truncate
- ❌ Gemini - Will truncate
- ⚠️ Qwen - May struggle with input context

### Very Long Transcripts (120+ minutes, 40K+ words)
**Only one reliable option:**
- ✅ **Claude Sonnet ONLY** (64K output)
- All others will truncate or fail

---

## Token Estimation

### Quick Conversion
- **1 token ≈ 0.75 words** (English)
- **1,000 tokens ≈ 750 words**
- **10,000 tokens ≈ 7,500 words**

### Transcript Length to Token Count
| Audio Duration | Approx Words | Approx Tokens | Notes |
|----------------|--------------|---------------|-------|
| 10 minutes | ~1,500 words | ~2K tokens | Very short |
| 30 minutes | ~4,500 words | ~6K tokens | Short talk/interview |
| 60 minutes | ~9,000 words | ~12K tokens | Standard podcast |
| 87 minutes | ~13,000 words | ~17K tokens | Christoph episode |
| 120 minutes | ~18,000 words | ~24K tokens | Long podcast |

**Important:** Add ~20-30% overhead for:
- System instructions
- Context (people list, technical terms)
- Formatting (timestamps, speaker labels)

So your 87-minute transcript:
- Raw: ~17K tokens
- With overhead: ~22-24K tokens input
- Output needed: ~18-20K tokens (formatted)

---

## Practical Recommendations

### For Your Ethereum Transcript Project

**Current Setup (✅ Optimal):**
- **Transcription:** WhisperX (free, local, accurate)
- **Post-processing:** GPT-4.1 (32K output handles 87-min transcripts)

**Alternative Options:**
1. **Maximum Quality (costs more):**
   - Claude Sonnet - best for very long transcripts (64K output)
   
2. **Maximum Speed (good quality):**
   - Llama 3.3 70B via Groq - 300+ tokens/sec, 32K output
   
3. **Budget/Local (GPU required):**
   - Qwen 2.5 14B via Ollama - free but limited capacity

**Avoid for 87-minute transcripts:**
- ❌ ChatGPT-4o - only 16K output, will truncate
- ❌ Gemini 2.5 Pro - only 8K output, severe truncation

---

## Summary Table: Can It Handle Your 87-Minute Transcripts?

| Service | Context (Input) | Output Tokens | Verdict | Notes |
|---------|----------------|---------------|---------|-------|
| Claude Sonnet | 200K ✅ | 64K ✅ | **EXCELLENT** | Overkill but reliable |
| GPT-4.1 | 128K ✅ | 32K ✅ | **GOOD** | Perfect fit, current choice |
| ChatGPT-4o | 128K ✅ | 16K ❌ | **FAILS** | Truncates output |
| Gemini 2.5 Pro | 2M ✅✅ | 8K ❌ | **FAILS** | Huge input, tiny output |
| Llama 3.3 70B | 128K ✅ | 32K ✅ | **GOOD** | Fast, cost-effective |
| Qwen 2.5 14B | 32K ⚠️ | 32K ✅ | **MARGINAL** | May need input chunking |

**Your Choice of GPT-4.1 is the sweet spot for 87-minute Ethereum technical transcripts.**
