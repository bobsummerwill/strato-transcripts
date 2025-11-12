# Audio Transcription Pipeline with Multi-Provider AI Processing

Automated transcription with speaker identification using multiple transcription services (WhisperX local, Deepgram, AssemblyAI, Sonix, Speechmatics) and AI post-processing (Claude, GPT-4, Gemini, etc.) to correct technical terms and speaker names.

## Quick Start

```bash
# 1. Setup (one time)
./scripts/install_packages_and_venv.sh
cp setup_env.sh.example setup_env.sh
nano setup_env.sh  # Add your API keys

# 2. Process a single file
source venv/bin/activate && source setup_env.sh
./scripts/process_single.sh audio.mp3 \
  --transcribers whisperx \
  --processors openai

# 3. Process all MP3s in ~/Downloads
./scripts/process_all.sh --transcribers deepgram --processors anthropic
```

## Architecture

```
audio.mp3
    ↓
process_single.sh (orchestration)
    ↓
Phase 1: Transcription
    process_single_transcribe_and_diarize.py
    - Runs all transcribers internally (whisperx, deepgram, assemblyai, sonix, speechmatics, novita)
    - Outputs: intermediates/*_raw.txt
    ↓
Phase 2: Post-Processing  
    process_single_post_process.py
    - Runs all processors internally (anthropic, openai, gemini, etc.)
    - Outputs: outputs/*_corrected.txt
```

## Transcription Services

All services include speaker diarization (identifying who said what).

| Service | Model | Type | Cost/hour | Speed |
|---------|-------|------|-----------|-------|
| **WhisperX** | large-v3 | Local GPU | FREE | 5-10 min |
| **Kimi-Audio** | 7B-Instruct | Local GPU | FREE | ~1.5x RT |
| **Deepgram** | nova-3-general | Cloud API | $0.41 | 23 sec |
| **AssemblyAI** | Best | Cloud API | $1.44 | 3-4 min |
| **Sonix** | Standard | Cloud API | $10.00 | ~2 min |
| **Speechmatics** | Enhanced | Cloud API | $4.50 | ~1 min |
| **Novita AI** | qwen2.5-omni | Cloud API | TBD | TBD |

## AI Post-Processors

| Provider | Model | Type | Context | Cost | Features |
|----------|-------|------|---------|------|----------|
| **Anthropic** | Claude Sonnet 4.5 | Cloud API | 200K | $3/M tokens | Streaming, 64K output |
| **OpenAI** | GPT-4o | Cloud API | 128K | $2.50/M tokens | Reliable, fast |
| **Gemini** | Gemini 2.5 Pro | Cloud API | 128K | $1.25/M tokens | Best for long transcripts |
| **DeepSeek** | DeepSeek Chat | Cloud API | 64K | $0.14/M tokens | Cost-effective |
| **Qwen (Ollama)** | Qwen2.5:7b | Local | 32K | FREE | Local, private ⚠️ |

**Note on Qwen:** Alibaba's Qwen 2.5 model served locally via Ollama. The 32K context limit is suitable for transcripts up to ~40 minutes. Typical 60-90 minute transcripts (~45K tokens) may be truncated. For longer content, use cloud providers.

## Usage Examples

### Single File with One Transcriber/Processor

```bash
# WhisperX (local) + Claude
./scripts/process_single.sh interview.mp3 \
  --transcribers whisperx \
  --processors anthropic

# Deepgram (cloud) + GPT-4
./scripts/process_single.sh interview.mp3 \
  --transcribers deepgram \
  --processors openai
```

### Multiple Transcribers and Processors

```bash
# 2 transcribers × 3 processors = 6 combinations
./scripts/process_single.sh interview.mp3 \
  --transcribers whisperx,deepgram \
  --processors anthropic,openai,ollama
```

### Batch Processing

```bash
# Process all MP3s in ~/Downloads
./scripts/process_all.sh --transcribers deepgram --processors openai

# Use defaults (whisperx + openai)
./scripts/process_all.sh
```

## Setup

### Requirements

**Minimum (CPU):**
- 8GB RAM, 50GB disk
- Expect hours of processing

**Recommended (GPU):**
- NVIDIA GPU with 6GB+ VRAM (GTX 1660+, RTX 20/30/40/50 series)
- 16GB RAM, 50GB disk
- Process 1 hour audio in 5-10 minutes

### Installation

```bash
# Auto-detects hardware and installs dependencies
./scripts/install_packages_and_venv.sh

# For CPU-only on GPU system
./scripts/install_packages_and_venv.sh --force-cpu

# Configure API keys
cp setup_env.sh.example setup_env.sh
nano setup_env.sh  # Add your keys
```

### API Keys

Add to `setup_env.sh`:

```bash
# Required for WhisperX (speaker diarization)
export HF_TOKEN="hf_..."  # https://huggingface.co/settings/tokens

# Optional: Cloud transcription services
export DEEPGRAM_API_KEY="..."       # https://console.deepgram.com/
export ASSEMBLYAI_API_KEY="..."     # https://www.assemblyai.com/
export SONIX_API_KEY="..."          # https://sonix.ai/
export SPEECHMATICS_API_KEY="..."  # https://www.speechmatics.com/
export OPENAI_API_KEY="sk-..."      # https://platform.openai.com/

# Optional: AI post-processors
export ANTHROPIC_API_KEY="sk-ant-..."  # https://console.anthropic.com/
export GOOGLE_API_KEY="..."            # https://makersuite.google.com/
export DEEPSEEK_API_KEY="sk-..."      # https://platform.deepseek.com/
export MOONSHOT_API_KEY="sk-..."      # https://platform.moonshot.cn/
```

## Output Files

### Intermediates (Phase 1)
```
intermediates/
  audio_whisperx_raw.txt         # WhisperX output
  audio_kimi_raw.txt             # Kimi-Audio output
  audio_deepgram_raw.txt          # Deepgram output
  audio_whisperx_raw.md           # Markdown version
```

### Final Outputs (Phase 2)
```
outputs/
  audio_whisperx_anthropic_processed.txt         # WhisperX + Claude
  audio_deepgram_openai_processed.txt            # Deepgram + GPT-4
  audio_whisperx_anthropic_processed.md          # Markdown versions
```

**Naming Convention:**
- **Intermediates:** `{basename}_{transcriber}_raw.{txt|md}`
- **Final Outputs:** `{basename}_{transcriber}_{processor}_processed.{txt|md}`

Where:
- `{basename}` = Original audio filename without extension
- `{transcriber}` = whisperx, kimi, deepgram, assemblyai, sonix, speechmatics, or novita
- `{processor}` = anthropic, openai, gemini, deepseek, or ollama

## GPU Support

### NVIDIA GPUs
- **RTX 50-series** (Blackwell): PyTorch 2.9+ with CUDA 12.8
- **RTX 40-series** (Ada): Full support
- **RTX 30-series** (Ampere): Full support  
- **GTX 16-series** (Turing): Full support

Setup installs appropriate PyTorch version automatically.

### AMD GPUs
Not supported for GPU acceleration. Systems with AMD GPUs run in CPU-only mode.

## Project Structure

```
stratomercata-transcripts/
├── README.md                                    # This file
├── setup_env.sh.example                         # API key template
├── requirements-*.txt                           # Dependencies
├── scripts/
│   ├── install_packages_and_venv.sh            # Setup script
│   ├── process_single.sh                       # Main: single file
│   ├── process_all.sh                          # Main: batch files
│   ├── process_single_transcribe_and_diarize.py  # Phase 1: Transcription
│   ├── process_single_post_process.py          # Phase 2: AI correction
│   ├── extract_people.py                       # Extract speaker names
│   └── extract_terms.py                        # Extract technical terms
├── intermediates/                               # Phase 1 outputs
└── outputs/                                     # Phase 2 outputs
```

## Resources

- [WhisperX](https://github.com/m-bain/whisperX) - GPU-accelerated Whisper with diarization
- [Deepgram](https://developers.deepgram.com/) - Cloud speech-to-text API
- [AssemblyAI](https://www.assemblyai.com/docs) - Cloud transcription API
- [Anthropic Claude](https://docs.anthropic.com/) - AI post-processing
- [OpenAI GPT-4](https://platform.openai.com/docs) - AI post-processing

## License

GNU General Public License v3.0 (GPL-3.0)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

See the [LICENSE](LICENSE) file for the full text.

**Dependencies:**
- **Core ML**: WhisperX (MIT), PyTorch (BSD-3-Clause), pyannote.audio (MIT)
- **Transcription**: faster-whisper (MIT), deepgram-sdk (MIT), assemblyai (MIT), openai (Apache-2.0)
- **AI Processing**: anthropic (MIT), google-generativeai (Apache-2.0), requests (Apache-2.0)
- **Audio**: ffmpeg (LGPL/GPL), torchaudio (BSD-3-Clause), pandas (BSD-3-Clause)
- **Model Hosting**: speechbrain (Apache-2.0), transformers (Apache-2.0), numpy (BSD-3-Clause)
