# Setup Environment

Set up the transcription pipeline environment with GPU support.

## Usage

```
/setup [gpu-type]
```

## Arguments

- `gpu-type` - One of: nvidia, amd, intel, cpu, all (default: nvidia)

## Instructions

When the user invokes this command:

1. **Check current GPU**:
   ```bash
   lspci | grep -i "vga\|3d\|display"
   ```

2. **Run installation script**:
   ```bash
   ./scripts/install_packages_and_venv.sh --<gpu-type>
   ```

3. **Create environment file**:
   ```bash
   cp setup_env.sh.example setup_env.sh
   echo "Edit setup_env.sh to add your API keys"
   ```

4. **Verify setup**:
   ```bash
   source setup_env.sh
   source venv-<gpu-type>/bin/activate
   python3 -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"
   ```

## Examples

```bash
# NVIDIA GPU setup
/setup nvidia

# AMD ROCm setup
/setup amd

# Intel XPU setup
/setup intel

# CPU-only fallback
/setup cpu

# Create all venvs (for eGPU workflows)
/setup all
```

## Required API Keys

Edit `setup_env.sh` after setup:

```bash
export HF_TOKEN="hf_..."              # Required: WhisperX diarization
export OPENROUTER_API_KEY="sk-or-..." # Required: AI post-processing
export ASSEMBLYAI_API_KEY="..."       # Optional: AssemblyAI transcription
export REPLICATE_API_TOKEN="..."      # Optional: Cloud WhisperX
```

## HuggingFace Model Agreements

Accept these before first use:
- https://huggingface.co/pyannote/speaker-diarization-3.1
- https://huggingface.co/pyannote/segmentation-3.0

## Virtual Environments

| venv | Backend | PyTorch | Use Case |
|------|---------|---------|----------|
| venv-nvidia/ | CUDA | 2.9.1+cu130 | NVIDIA discrete/eGPU |
| venv-amd/ | ROCm | 2.6.0+rocm6.2 | AMD discrete/eGPU |
| venv-intel/ | XPU | 2.5.1+IPEX | Intel integrated/Arc |
| venv-cpu/ | CPU | 2.9.1 | Fallback |

## Auto-Detection

Shell scripts auto-detect the correct venv (priority: nvidia > amd > intel > cpu):
```bash
./scripts/process_video.sh video.mp4      # Auto-selects venv
./scripts/process_all.sh                  # Auto-selects venv
./scripts/process_all_videos.sh           # Auto-selects venv
```

## torchcodec Workaround

The install script applies a workaround for pyannote-audio's torchcodec dependency:

1. **Problem**: torchcodec has ABI incompatibility with PyTorch 2.9.x causing segfaults
2. **Solution**: Patches `pyannote.audio/core/io.py` to use soundfile as fallback
3. **Result**: torchcodec is uninstalled; audio decoding uses soundfile instead

See [strato-transcripts#44](https://github.com/strato-net/strato-transcripts/issues/44) for details.

Upstream issue: [torchcodec#995](https://github.com/meta-pytorch/torchcodec/issues/995)
