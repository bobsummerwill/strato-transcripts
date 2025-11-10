# Audio/Video Transcription Pipeline with Speaker Diarization

Automated audio and video transcription using OpenAI's Whisper AI with speaker identification. Convert hours of audio into formatted transcripts in minutes using local GPU processing.

## What This Does

- **Transcribes** audio/video to text using OpenAI's Whisper AI model
- **Identifies speakers** using pyannote.audio voice analysis
- **Maps speakers** from generic labels (SPEAKER_01) to actual names
- **Formats output** as markdown with timestamps and speaker labels

## Why Use This

- **Free after GPU purchase** (vs $1-2/hour for cloud GPU services)
- **Process while you work** - GPU handles transcription in background
- **Consistent quality** - Same accuracy every time
- **Automatic speaker identification** - No manual speaker tagging needed
- **Offline processing** - No cloud dependencies after setup

---

## Quick Setup (Automated)

The fastest way to get started is using the automated setup scripts that detect your hardware and configure everything automatically.

### Step 1: Install NVIDIA Drivers (GPU users only)

```bash
# Skip this step if you don't have an NVIDIA GPU
sudo ./install_nvidia_drivers.sh
sudo reboot
```

This installs NVIDIA driver 565+ which is required for RTX 50-series GPUs (Blackwell architecture).

### Step 2: Setup Python Environment

```bash
# Auto-detects hardware (NVIDIA GPU vs CPU)
# For CPU-only on a GPU system, add --force-cpu
./install_packages_and_venv.sh
```

**What this script does:**
- Detects hardware (NVIDIA GPU vs CPU) or uses `--force-cpu` flag
- Installs system dependencies (ffmpeg, build tools, Python dev)
- Installs PyTorch 2.9.0 stable (CUDA 12.8 for NVIDIA, CPU-only otherwise)
- Installs WhisperX, pyannote.audio, SpeechBrain
- Applies WhisperX compatibility patches automatically
- Runs verification tests

### Step 3: Configure HuggingFace Token

```bash
nano setup_env.sh  # Add your HF_TOKEN
```

Get a HuggingFace token at: https://huggingface.co/settings/tokens

You'll need to accept the terms for:
- https://huggingface.co/pyannote/speaker-diarization-3.1
- https://huggingface.co/pyannote/segmentation-3.0

---

## System Requirements

### Minimum (CPU only)
- 8GB RAM
- 50GB disk space
- Expect hours of processing time

### Recommended (GPU)
- **NVIDIA GPU**: GTX 1660+ (6GB+ VRAM) or RTX 20/30/40/50 series
- 16GB RAM
- 50GB disk space

### Optimal
- **NVIDIA GPU**: RTX 5070/4090 or newer
- 32GB RAM
- SSD storage

**Note:** AMD GPUs are not supported for GPU acceleration. Systems with AMD GPUs will run in CPU-only mode.

---

## Usage

### Transcription Options

This project supports multiple transcription services:

| Service | Type | Cost (per hour) | Speed | Setup |
|---------|------|-----------------|-------|-------|
| **WhisperX** | Local | FREE | 5-10 min | Default (GPU required) |
| **Deepgram** | Cloud | $0.41 | 23 sec | API key required |
| **AssemblyAI** | Cloud | $1.44 | 3-4 min | API key required |
| **OpenAI** | Cloud | $5.75 | 4-5 min | ❌ No diarization |

#### WhisperX (Local - Default)
```bash
# Activate environment
source venv/bin/activate
source setup_env.sh

# Transcribe with speaker identification (forces English by default)
python3 scripts/transcribe_with_diarization.py audio.mp3
# Output: intermediates/audio_transcript_with_speakers.txt
```

#### Deepgram (Recommended Cloud - Fastest & Cheapest)
```bash
# Setup (one time)
export DEEPGRAM_API_KEY="your-key"  # Get from https://console.deepgram.com/

# Transcribe
python3 scripts/transcribe_with_deepgram.py audio.mp3
# Output: intermediates/audio_deepgram_transcript_with_speakers.txt
# Speed: ~23 seconds for 96-minute audio
# Cost: ~$0.41 per hour
```

#### AssemblyAI (Cloud Alternative)
```bash
# Setup (one time)
export ASSEMBLYAI_API_KEY="your-key"  # Get from https://www.assemblyai.com/

# Transcribe
python3 scripts/transcribe_with_assemblyai.py audio.mp3
# Output: intermediates/audio_assemblyai_transcript_with_speakers.txt
# Speed: 3-4 minutes processing
# Cost: ~$1.44 per hour
```

### Basic Workflow

```bash
# 1. Extract audio from video (if needed)
ffmpeg -i "video.mp4" -q:a 0 -map a output.mp3

# 2. Transcribe with speaker identification
# Choose one of the methods above
python3 scripts/transcribe_with_deepgram.py output.mp3

# 3. AI Post-Process (fix technical terms & speaker names)
python3 scripts/post_process_transcript.py \
  intermediates/output_deepgram_transcript_with_speakers.txt \
  --provider anthropic

# Output: outputs/output_deepgram_anthropic_corrected.txt

# 3. Map speaker labels to names
python3 map_speakers_to_names.py \
  output_transcript_with_speakers.txt \
  output_with_names.txt \
  --speaker-map "SPEAKER_00=Bob Summerwill,SPEAKER_01=Victor Wong"

# 4. Format for markdown (optional)
python3 format_transcript_for_markdown.py \
  output_with_names.txt \
  output_formatted.md
```

### Language Configuration

**Preventing Language Drift:**

The transcription script now forces English language by default to prevent the AI from drifting into other languages during transcription. This is especially important for interviews with non-native English speakers where accents might confuse the auto-detection.

```bash
# Default: English (recommended for all English content)
python3 transcribe_with_diarization.py output.mp3

# Specify a different language if needed
python3 transcribe_with_diarization.py output.mp3 --language de  # German
python3 transcribe_with_diarization.py output.mp3 --language fr  # French
python3 transcribe_with_diarization.py output.mp3 --language es  # Spanish
```

Common language codes: `en` (English), `de` (German), `fr` (French), `es` (Spanish), `it` (Italian), `pt` (Portuguese), `zh` (Chinese), `ja` (Japanese), `ko` (Korean)

### Speaker Mapping

To identify speakers, read the first few pages of the `_transcript_with_speakers.txt` file and match speaking patterns to known participants. The script reports segment counts to help identify main speakers.

**Example speaker mapping:**
```bash
python3 map_speakers_to_names.py \
  input.txt \
  output.txt \
  --speaker-map "SPEAKER_00=Alice,SPEAKER_01=Bob,SPEAKER_02=Charlie"
```

### Batch Processing

Process multiple audio files at once:

```bash
./batch_transcribe_all.sh *.mp3
```

---

## Scripts Reference

### Core Scripts

**diarize_and_combine.py**
- Complete pipeline: transcription + speaker identification
- Auto-detects GPU or falls back to CPU
- Uses Whisper large-v2 model (best accuracy)
- Output: `filename_transcript_with_speakers.txt`

**map_speakers_to_names.py**
- Replaces SPEAKER_XX with actual names
- Supports --speaker-map command line argument
- Reports segment counts to help identify speakers
- Output: `filename_with_names.txt`

**format_transcript_for_markdown.py**
- Converts to markdown format with timestamps
- Adds bold formatting around speaker names
- Preserves timestamp information
- Output: Markdown-compatible text

**batch_transcribe_all.sh**
- Process multiple audio files in sequence
- Automatically handles file naming
- Useful for processing entire directories

### Utility Scripts

- `test_diarization.py` - Test speaker diarization only
- `test_diarization_hf.py` - Test HuggingFace authentication
- `test_cuda.py` - Test NVIDIA GPU availability
- `test_rocm.py` - Test AMD GPU availability

---

## RTX 5070 Blackwell GPU Support

### Why Special Setup is Needed

The RTX 5070 uses NVIDIA's new Blackwell architecture (compute capability sm_120) released in November 2024. This requires a specific dependency chain:

**The Dependency Chain:**
```
RTX 5070 Hardware (sm_120 architecture)
    ↓ requires
NVIDIA Driver 565+
    ↓ enables
CUDA 12.8 Support
    ↓ used by
PyTorch 2.9.0 Stable (cu128)
    ↓ required by
pyannote.audio 4.0.1+
    ↓ used by
WhisperX (with patches)
    ↓ enables
GPU-Accelerated Transcription
```

### PyTorch 2.9.0 Stable

This setup uses PyTorch 2.9.0 stable for the following reasons:

- Full Blackwell (sm_120) architecture support for RTX 50-series GPUs
- Stable, well-tested release suitable for production use
- Excellent compatibility with ecosystem packages (pyannote.audio 4.0.1+, WhisperX)
- Reliable performance on all NVIDIA GPU generations

### Why CUDA 12.8 (not 13.0)?

**CUDA 12.8 Benefits:**
- More stable and mature
- Better ecosystem compatibility
- All cu12 packages work together seamlessly
- No library version mismatches

**CUDA 13.0 Issues:**
- Still experimental/bleeding-edge
- Mix of cu12 and cu13 packages causes conflicts
- Missing .so.13 libraries (only .so.12 available)
- Requires fragile symlink workarounds

### Required Patches

WhisperX needs patches to work with pyannote.audio 4.0.1+:

```bash
# Automatically applied by install_packages_and_venv.sh
sed -i 's/use_auth_token/token/g' venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py
sed -i '412s/use_auth_token=None/token=None/' venv/lib/python3.12/site-packages/whisperx/asr.py
```

### LD_LIBRARY_PATH Configuration

**Required for cuDNN Library Loading**

The system linker needs `LD_LIBRARY_PATH` to locate cuDNN libraries at runtime. The installation script automatically configures this by adding to your `~/.bashrc`:

```bash
# Automatically configured by install_packages_and_venv.sh
export LD_LIBRARY_PATH=venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH
```

**Why is this needed?**
- PyTorch packages CUDA libraries (including cuDNN) as separate pip packages
- The system linker needs to know where to find `libcudnn_cnn.so.9` at runtime
- Without this, you'll see errors like: `Unable to load libcudnn_cnn.so.9.1.0`

**Note:** This is automatically added to your `~/.bashrc` by the installation script and is set in the batch processing script. You don't need to configure it manually.

## Manual Setup (Advanced)

If you prefer manual control or need to customize the setup:

### 1. System Dependencies

```bash
sudo apt update
sudo apt install -y ffmpeg build-essential python3-dev python3-pip python3-venv
```

### 2. NVIDIA Drivers (GPU only)

```bash
# Check current driver
nvidia-smi

# Install driver 565+ for RTX 50-series
sudo apt install -y nvidia-driver-565
sudo reboot
```

### 3. Python Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# For NVIDIA GPU (RTX 50-series and other Blackwell GPUs)
pip install torch==2.9.0 torchvision==0.24.0 torchaudio==2.9.0 --index-url https://download.pytorch.org/whl/cu128

# For other NVIDIA GPUs (older hardware)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# For CPU-only
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install required packages
pip install -r requirements-base.txt
```

### 4. Apply WhisperX Patches

```bash
sed -i 's/use_auth_token/token/g' venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py
sed -i '412s/use_auth_token=None/token=None/' venv/lib/python3.12/site-packages/whisperx/asr.py
```

### 5. Verify Installation

```bash
python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.cuda.is_available()}')"
python3 -c "import whisperx; print('WhisperX OK')"
python3 -c "from pyannote.audio import Pipeline; print('pyannote OK')"
```

---

## Requirements Files

This project uses hardware-specific requirements files:

- **requirements-nvidia.txt** - PyTorch 2.9.0 stable with CUDA 12.8 for NVIDIA GPUs
- **requirements-cpu.txt** - PyTorch 2.9.0 stable CPU-only for non-NVIDIA systems
- **requirements-base.txt** - WhisperX, pyannote.audio, SpeechBrain (hardware-agnostic)

The `install_packages_and_venv.sh` script automatically selects the correct file based on your hardware.

---

## Tips & Best Practices

### Workflow Recommendations

1. **Test first** - Process first 5 minutes to verify quality before running full audio
2. **Keep intermediates** - Save all `_transcript_with_speakers.txt` files to re-run mapping without re-transcribing
3. **Manual review** - Expect to manually review 10-20% of transcripts for accuracy
4. **Batch processing** - GPU can handle multiple videos overnight using batch script
5. **Audio preprocessing** - Normalize audio levels and remove noise before transcription

### Memory Management

- **Large files**: Process in chunks if running out of VRAM
- **Batch size**: Reduce if getting OOM errors
- **Model selection**: Use `medium` or `small` Whisper model for lower VRAM usage
- **Background apps**: Close other GPU applications during transcription

### Speaker Identification

- **Distinct voices**: Works best with clearly different voice characteristics
- **Segment counts**: Use reported counts to identify main speakers
- **Listen first**: Review first few minutes of audio to match voices to names
- **Update mapping**: Can re-run mapping with corrected names without re-transcribing

---

## Version Compatibility

**Tested:**
- Python: 3.8 - 3.12
- PyTorch: 2.0.0 - 2.9.0 (stable)
- CUDA: 11.8, 12.1, 12.8
- Ubuntu: 20.04, 22.04, 24.04
- Windows: 10, 11 (WSL2 recommended)

**GPU Support:**
- RTX 50-series (Blackwell): PyTorch 2.7+ stable + CUDA 12.8
- RTX 40-series (Ada Lovelace): PyTorch 2.0+ stable
- RTX 30-series (Ampere): PyTorch 2.0+ stable
- GTX 16-series (Turing): PyTorch 2.0+ stable

---

## Project Structure

```
stratomercata-transcripts/
├── README.md                              # This file
├── install_nvidia_drivers.sh              # NVIDIA driver installation (565+)
├── install_packages_and_venv.sh           # Automated setup script
├── setup_env.sh.example                   # HuggingFace token configuration template
├── requirements-nvidia.txt                # PyTorch nightly with CUDA 12.8
├── requirements-cpu.txt                   # PyTorch nightly CPU-only
├── requirements-base.txt                  # WhisperX and dependencies
├── diarize_and_combine.py                 # Main transcription script
├── map_speakers_to_names.py               # Speaker label mapping
├── format_transcript_for_markdown.py      # Markdown formatter
├── batch_transcribe_all.sh                # Batch processing script
├── transcribe_with_diarization.py         # Alternative transcription script
├── test_diarization.py                    # Diarization testing
├── test_diarization_hf.py                 # HuggingFace auth testing
├── test_cuda.py                           # NVIDIA GPU testing
```

---

## Resources

**Documentation:**
- [WhisperX GitHub](https://github.com/m-bain/whisperX)
- [Whisper by OpenAI](https://github.com/openai/whisper)
- [pyannote.audio](https://github.com/pyannote/pyannote-audio)
- [HuggingFace](https://huggingface.co/)
- [PyTorch](https://pytorch.org/)

**Getting Help:**
- Check [WhisperX Issues](https://github.com/m-bain/whisperX/issues)
- Check [pyannote Discussions](https://github.com/pyannote/pyannote-audio/discussions)
- File issues on this repository

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0).

**Dependencies:**
- WhisperX: MIT License
- PyTorch: BSD License
- pyannote.audio: MIT License
- Whisper: MIT License

---

**Last Updated:** November 2025  
**Tested Hardware:** RTX 5070 (NVIDIA), RTX 3090 (NVIDIA)  
**Test Case:** 79-minute audio, 6 speakers  
**Success Rate:** 95%+ transcription, 90%+ speaker identification
