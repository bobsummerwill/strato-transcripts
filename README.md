# Audio Transcription Pipeline with Multi-Provider AI Processing

Transcription with speaker diarization plus AI post-processing for technical term correction.

## Quick Start

```bash
# 1. Setup environment (one time)
./scripts/install_packages_and_venv.sh --nvidia   # or --amd, --intel, --cpu
cp setup_env.sh.example setup_env.sh
nano setup_env.sh  # Add API keys

# 2. Activate and run
source setup_env.sh
source venv-nvidia/bin/activate  # Match your GPU vendor

# 3. Transcribe audio
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 --transcribers whisperx

# 4. Post-process transcript
python3 scripts/process_single_post_process.py intermediates/audio/audio_whisperx.md --processors opus

# Or use the combined shell script
./scripts/process_single.sh audio.mp3 --transcribers whisperx --processors opus
```

## Transcription Services

All services include speaker diarization (identifying who said what) and word-level timestamps.

| Service | Model | Type | Cost/hour | Speed | Word-Level JSON |
|---------|--------|------|-----------|-------|-----------------|
| **whisperx** | large-v3 | Local GPU | FREE | ~20 min/hr audio | Yes |
| **whisperx-cloud** | large-v3 | Replicate API | $2.88 | 2-3 min | Optional |
| **assemblyai** | Best | Cloud API | $1.08 | 3-4 min | Yes |

### Transcription Commands

```bash
# Local WhisperX (requires GPU)
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 --transcribers whisperx

# Force reprocess existing
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 --transcribers whisperx --force

# Force CPU mode (slower)
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 --transcribers whisperx --force-cpu

# Cloud transcription
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 --transcribers assemblyai

# Multiple transcribers
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 --transcribers whisperx-cloud,assemblyai
```

## AI Post-Processors

All 11 models accessed via **OpenRouter** (single API key). See [AI_PROVIDERS.md](AI_PROVIDERS.md) for details.

| Processor | Model | Context | Best For |
|-----------|-------|---------|----------|
| **opus** | Claude Opus 4.6 | 1M | Premium quality, complex reasoning |
| **gemini** | Gemini 3 Pro | 1M | Very long documents, technical |
| **chatgpt** | GPT-5.2 | 400K | General-purpose, balanced |
| **grok** | Grok 4 | 256K | #1 benchmark performance |
| **deepseek** | DeepSeek V3.2 | 128K | Cost-effective, good quality |
| **kimi** | Kimi K2.5 | 256K | Long-context, coding |
| **qwen** | Qwen3-Max | 256K | Agent workflows |
| **glm** | GLM-4.7 | 203K | Local-capable (~19GB VRAM) |
| **minimax** | MiniMax M2.1 | 4M | Extremely long documents |
| **llama** | Llama 4 Maverick | 1M | Open model, cost-effective |
| **mistral** | Mistral Large | 256K | European sovereignty |

### Post-Processing Commands

```bash
# Single processor
python3 scripts/process_single_post_process.py transcript.md --processors opus

# Multiple processors
python3 scripts/process_single_post_process.py transcript.md --processors opus,gemini,deepseek

# All processors
python3 scripts/process_single_post_process.py transcript.md --processors opus,gemini,deepseek,chatgpt,qwen,kimi,glm,minimax,llama,grok,mistral
```

## Word-Level Consensus Pipeline

Build ultra-high-quality transcripts using a 6-phase consensus pipeline that combines multiple transcribers and 11 AI models.

### Phase 1-2: Transcriber Consensus

```bash
# Step 1: Transcribe with multiple services (generates word-level JSON)
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 \
  --transcribers whisperx-cloud,assemblyai --consensus

# Step 2: Build consensus from transcriber outputs
python3 scripts/assess_quality.py --intermediate-consensus --episode <name>
```

Outputs to `intermediates/<episode>/`:
- `*_intermediate_consensus.md` - Merged transcript
- `*_intermediate_consensus.txt` - Plain text
- `*_intermediate_consensus_words.json` - Word-level data with agreement scores

### Phase 3-6: AI Consensus Pipeline

After transcriber consensus, run through 11 AI models for superior accuracy:

```bash
# Source API keys first
source setup_env.sh

# Run full AI pipeline (Phases 3-6)
python3 scripts/ai_consensus_pipeline.py --episode <name>
```

**Phases:**
- **Phase 3**: AI Correction Pass - 11 models correct technical terms, names, grammar
- **Phase 4**: AI Consensus - Voting across all AI outputs
- **Phase 5**: Filler Removal - Removes um, uh, basically, literally, etc.
- **Phase 6**: Final Output - Generates polished transcripts

Final outputs to `outputs/<episode>/`:
- `*_final.md` - Final markdown transcript
- `*_final.txt` - Plain text
- `*_final_words.json` - Word-level data

### Quick Full Pipeline

```bash
# Complete pipeline from audio to final transcript
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 \
  --transcribers whisperx-cloud,assemblyai --consensus
python3 scripts/assess_quality.py --intermediate-consensus --episode <name>
source setup_env.sh && python3 scripts/ai_consensus_pipeline.py --episode <name>
```

## Output Structure

```
intermediates/
  <episode>/
    # Raw transcriber outputs
    <episode>_whisperx.txt              # Plain text transcript
    <episode>_whisperx.md               # Markdown with timestamps
    <episode>_whisperx_words.json       # Word-level timing data
    <episode>_assemblyai.txt
    <episode>_assemblyai.md
    <episode>_assemblyai_words.json

    # Consensus word files (--consensus mode)
    <episode>_whisperx_consensus_words.json
    <episode>_assemblyai_consensus_words.json

    # Phase 2: Transcriber consensus
    <episode>_intermediate_consensus.md
    <episode>_intermediate_consensus.txt
    <episode>_intermediate_consensus_words.json

    # Phase 3: AI corrections (×11 models)
    <episode>_ai_opus_words.json
    <episode>_ai_gemini_words.json
    ... (9 more)

    # Phase 4-5: AI consensus and filler removal
    <episode>_ai_consensus_words.json
    <episode>_final_words.json

outputs/
  <episode>/
    # Legacy: Single-model post-processing
    <episode>_whisperx_opus.txt
    <episode>_whisperx_opus.md

    # Phase 6: Final consensus outputs
    <episode>_final.md
    <episode>_final.txt
    <episode>_final_words.json
```

## Hardware Requirements

| Mode | RAM | GPU | Disk |
|------|-----|-----|------|
| **CPU-only** | 8GB | None | 50GB |
| **NVIDIA** | 16GB | 6GB+ VRAM | 50GB |
| **AMD ROCm** | 16GB | 6GB+ VRAM | 50GB |
| **Intel XPU** | 16GB | Arc/Iris | 50GB |

### Tested GPUs
- NVIDIA RTX 5070 (12GB) - PyTorch 2.9.1+cu130
- NVIDIA RTX 3090 (24GB) - PyTorch 2.9.1+cu130

## Setup

### 1. Install Dependencies

```bash
# For NVIDIA GPU
./scripts/install_packages_and_venv.sh --nvidia

# For AMD GPU (ROCm)
./scripts/install_packages_and_venv.sh --amd

# For Intel GPU (Arc/XPU)
./scripts/install_packages_and_venv.sh --intel

# CPU-only fallback
./scripts/install_packages_and_venv.sh --cpu

# Create all venvs (for eGPU workflows)
./scripts/install_packages_and_venv.sh --all
```

### 2. Configure API Keys

```bash
cp setup_env.sh.example setup_env.sh
nano setup_env.sh
```

Required keys in `setup_env.sh`:
```bash
export HF_TOKEN="hf_..."              # Required for WhisperX diarization
export OPENROUTER_API_KEY="sk-or-..." # Required for AI post-processing
export ASSEMBLYAI_API_KEY="..."       # Optional: AssemblyAI transcription
export REPLICATE_API_TOKEN="..."      # Optional: Cloud WhisperX
```

### 3. Accept HuggingFace Model Agreements

- https://huggingface.co/pyannote/speaker-diarization-3.1
- https://huggingface.co/pyannote/segmentation-3.0

## Package Versions

Key dependencies managed by `install_packages_and_venv.sh`:

| Package | Version | Notes |
|---------|---------|-------|
| PyTorch | 2.9.1+cu130 | CUDA 13.0 for Blackwell GPUs |
| torchaudio | 2.9.1+cu130 | Matches PyTorch |
| pyannote-audio | 4.0.1 | Last version without torch pin |
| whisperx | 3.7.6 | Speaker diarization |

The install script applies compatibility patches for:
- PyTorch 2.6+ `weights_only=True` default
- torchaudio 2.9.x API changes
- pyannote/torchcodec ABI compatibility

## Troubleshooting

### CUDA not detected
```bash
# Check CUDA availability
python3 -c "import torch; print(torch.cuda.is_available())"

# Verify driver
nvidia-smi
```

### OOM errors during transcription
The script automatically falls back to smaller batch sizes (32 -> 4 -> 1).

### `--force` vs `--force-cpu`
- `--force` - Reprocess even if output exists
- `--force-cpu` - Use CPU instead of GPU (slower)

## License

GPL-3.0 - See [LICENSE](LICENSE) file.
