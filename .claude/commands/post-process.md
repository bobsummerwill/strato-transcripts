# Post-Process Transcript

Run AI post-processing on transcripts to fix technical terms, names, and formatting.

## Usage

```
/post-process <transcript_file> [options]
```

## Arguments

- `<transcript_file>` - Path to transcript file (.md or .txt from intermediates/)
- `--processors` - Comma-separated list of AI processors (default: opus)
- `--mode` - `hosted` (OpenRouter API) or `local` (ollama) (default: hosted)

## Available Processors

### Hosted (OpenRouter API)
| Processor | Model | Context | Best For |
|-----------|-------|---------|----------|
| opus | Claude Opus 4.6 | 1M | Premium quality |
| gemini | Gemini 3 Pro | 1M | Long documents |
| chatgpt | GPT-5.2 | 400K | General purpose |
| grok | Grok 4 | 256K | #1 benchmark |
| deepseek | DeepSeek V3.2 | 128K | Cost-effective |
| kimi | Kimi K2.5 | 256K | Long-context |
| qwen | Qwen3-Max | 256K | Agent workflows |
| glm | GLM-4.7 | 203K | Also local-capable |
| minimax | MiniMax M2.1 | 4M | Extremely long |
| llama | Llama 4 Maverick | 1M | Open model |
| mistral | Mistral Large | 256K | European sovereignty |

### Local (ollama, requires 2x RTX 3090)
| Processor | Model | VRAM |
|-----------|-------|------|
| glm | GLM-4.7-Flash | ~19GB |
| deepseek-local | DeepSeek-R1 70B | ~40GB |
| qwen-local | Qwen3 72B | ~45GB |
| mistral-local | Mixtral 8x7B | ~27GB |
| llama-local | Llama 3.3 70B | ~40GB |

## Instructions

When the user invokes this command:

1. **Validate the transcript file exists**

2. **Check environment**:
   ```bash
   source setup_env.sh && echo "OPENROUTER_API_KEY: ${OPENROUTER_API_KEY:+SET}"
   ```

3. **Run post-processing**:
   ```bash
   python3 scripts/process_single_post_process.py <transcript_file> --processors <processors> [--mode <mode>]
   ```

4. **Report results**:
   - Output location: `outputs/<episode-name>/<episode-name>_<transcriber>_<processor>.md`
   - Processing time and token usage

## Examples

```bash
# Single high-quality processor
/post-process intermediates/episode001/episode001_whisperx.md --processors opus

# Multiple processors for comparison
/post-process intermediates/episode001/episode001_whisperx.md --processors opus,gemini,deepseek

# All processors
/post-process intermediates/episode001/episode001_whisperx.md --processors opus,gemini,deepseek,chatgpt,qwen,kimi,glm,minimax,llama,grok,mistral

# Local mode (requires 2x RTX 3090)
/post-process intermediates/episode001/episode001_whisperx.md --processors glm --mode local
```

## Output Structure

```
outputs/
  episode001/
    episode001_whisperx_opus.md
    episode001_whisperx_opus.txt
    episode001_whisperx_gemini.md
    ...
```
