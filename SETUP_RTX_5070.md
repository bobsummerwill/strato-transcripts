# Complete RTX 5070 Setup Guide for WhisperX Transcription

**Complete setup guide for Ubuntu 24.04 LTS with NVIDIA RTX 5070 (Blackwell architecture)**

This guide walks you through setting up WhisperX transcription with speaker diarization on a brand new Ubuntu 24.04 LTS system with an NVIDIA GeForce RTX 5070 GPU.

---

## Table of Contents
- [Hardware Requirements](#hardware-requirements)
- [System Requirements](#system-requirements)
- [Step 1: Install NVIDIA Drivers](#step-1-install-nvidia-drivers)
- [Step 2: Install System Dependencies](#step-2-install-system-dependencies)
- [Step 3: Set Up Python Environment](#step-3-set-up-python-environment)
- [Step 4: Install PyTorch Nightly](#step-4-install-pytorch-nightly)
- [Step 5: Install Python Dependencies](#step-5-install-python-dependencies)
- [Step 6: Apply WhisperX Patches](#step-6-apply-whisperx-patches)
- [Step 7: Configure Environment](#step-7-configure-environment)
- [Step 8: Verify Installation](#step-8-verify-installation)
- [Running Transcription](#running-transcription)
- [Performance Benchmarks](#performance-benchmarks)
- [Troubleshooting](#troubleshooting)

---

## Hardware Requirements

- **GPU:** NVIDIA GeForce RTX 5070 (Blackwell architecture, sm_120)
- **RAM:** 16GB minimum, 32GB recommended
- **Storage:** 50GB free space for models and processing
- **CPU:** Modern multi-core processor (8+ cores recommended)

---

## System Requirements

- **OS:** Ubuntu 24.04 LTS (fresh install)
- **Kernel:** Linux 6.8+
- **Python:** 3.10+ (3.12 recommended, comes with Ubuntu 24.04)
  - Note: `python3-venv`, `python3-pip`, and `python3-dev` will be installed in Step 2
  - All paths in this guide assume Python 3.12 (Ubuntu 24.04 default)

---

## Step 1: Install NVIDIA Drivers

**CRITICAL:** The RTX 5070 uses Blackwell architecture and requires NVIDIA driver version 565 or newer. Earlier driver versions will not recognize the GPU.

### 1.1 Update System Packages

```bash
sudo apt update
sudo apt upgrade -y
```

### 1.2 Install Latest NVIDIA Driver

```bash
# Automatically detect GPU and install the latest recommended driver
sudo ubuntu-drivers install
```

**What this does:**
- Detects your RTX 5070 automatically
- Installs the latest compatible driver (565 or newer)
- No need to manually track version numbers

### 1.3 Reboot System (REQUIRED)

```bash
sudo reboot
```

**⚠️ IMPORTANT:** You MUST reboot after driver installation. The driver will not work until you reboot.

### 1.4 Verify Driver Installation

After reboot, verify the driver is working:

```bash
nvidia-smi
```

**Expected output:**
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 5070        Off |   00000000:01:00.0  On |                  N/A |
|  0%   39C    P0             18W /  250W |     691MiB /  12227MiB |      3%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```

**Critical checks:**
- ✅ Driver Version shows 565.xx or newer
- ✅ CUDA Version shows 12.8 or newer
- ✅ GPU is shown as "NVIDIA GeForce RTX 5070"

**❌ If nvidia-smi fails or shows wrong version:**
- Driver is not properly installed
- Try: `sudo ubuntu-drivers install`
- Then reboot again

---

## Step 2: Install System Dependencies

### 2.1 Install Build Tools and FFmpeg

```bash
# Build essentials for compiling Python packages
sudo apt install -y build-essential

# FFmpeg for audio/video processing
sudo apt install -y ffmpeg

# Python development headers
sudo apt install -y python3-dev python3-venv python3-pip

# Git (if not already installed)
sudo apt install -y git
```

### 2.2 Verify FFmpeg Installation

```bash
ffmpeg -version
```

Should show FFmpeg 6.x or newer.

---

## Step 3: Set Up Python Environment

### 3.1 Navigate to Project Directory

```bash
cd ~/Projects/stratomercata-website
# Or wherever you cloned the repository
```

### 3.2 Create Python Virtual Environment

```bash
# Create venv using Python 3.12
python3 -m venv venv
```

### 3.3 Activate Virtual Environment

```bash
source venv/bin/activate
```

Your prompt should now show `(venv)` prefix.

---

## Step 4: Install PyTorch Nightly

**🚨 CRITICAL:** The RTX 5070 uses Blackwell architecture (sm_120 compute capability) which is ONLY supported in PyTorch nightly builds with CUDA 12.8.

**❌ PyTorch stable releases (2.8.0, 2.9.0, 2.10.0 stable) will NOT work with RTX 5070.**

### 4.1 Install PyTorch Nightly with CUDA 12.8

```bash
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
```

**What this installs:**
- `torch==2.10.0.dev20251103+cu128` (or newer nightly)
- `torchvision==0.25.0.dev20251103+cu128`
- `torchaudio==2.10.0.dev20251103+cu128`

**Bundled CUDA 12.8 libraries** (no system CUDA installation needed):
- cuDNN 9.10.2.21
- NCCL 2.27.5
- cuBLAS 12.8.1.86
- cuFFT 11.3.0.4
- cuSPARSE 12.8.0.1
- cuSOLVER 11.7.1.2
- cuRAND 10.3.7.37
- All other CUDA runtime libraries

**Installation time:** ~2-5 minutes depending on internet speed.

**Note:** No system-wide CUDA installation required. All CUDA libraries are bundled in venv.

### 4.2 Verify PyTorch Installation

```bash
python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'CUDA version: {torch.version.cuda}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"
```

**Expected output:**
```
PyTorch: 2.10.0.dev20251103+cu128
CUDA available: True
CUDA version: 12.8
GPU: NVIDIA GeForce RTX 5070
```

**❌ If CUDA shows as unavailable or GPU not detected:**
1. Check nvidia-smi works properly
2. Verify driver version is 565+
3. Uninstall and reinstall PyTorch nightly
4. Try rebooting system

---

## Step 5: Install Python Dependencies

### 5.1 Install Requirements

```bash
pip install -r requirements-lock.txt
```

**Note:** This installs from the complete lock file with all 155+ packages pinned to exact versions, ensuring a reproducible build.

### 5.2 Understanding Requirements Files

This project uses two requirements files:

**requirements.txt** (minimal, for development):
- Contains only 6 direct dependencies
- Uses exact versions only where critical (PyTorch, pyannote.audio)
- Transitive dependencies resolved automatically by pip

**requirements-lock.txt** (complete lock file, for production):
- Contains all 155+ packages with exact versions
- Ensures reproducible builds
- Generated from `pip freeze` after installing requirements.txt

### 5.3 Generating/Updating Lock File (Optional)

If you need to regenerate or update the lock file:

```bash
# After installing from requirements.txt
pip freeze > requirements-lock.txt
```

This captures all installed packages with exact versions, ensuring reproducible builds.

For production deployments, install from the lock file:
```bash
pip install -r requirements-lock.txt
```

**What this installs:**

**Core Transcription:**
- `whisperx==3.7.4` - Whisper with word-level timestamps
- `faster-whisper==1.2.1` - Optimized Whisper inference
- `ctranslate2==4.6.0` - Fast transformer inference

**Speaker Diarization:**
- `pyannote.audio==4.0.1` - Speaker diarization (PyTorch 2.10+ compatible)
- `pyannote.core==6.0.1` - Core pyannote functionality
- `pyannote.database==6.1.0`
- `pyannote.metrics==4.0.0`
- `pyannote.pipeline==4.0.0`

**ML/AI Libraries:**
- `transformers==4.57.1` - Hugging Face transformers
- `pytorch-metric-learning==2.9.0`
- `speechbrain==1.0.3`
- `torch-audiomentations==0.12.0`

**Data Processing:**
- `pandas==2.2.3` - Required for speaker segment handling
- `numpy>=2.0.2` - Required by pyannote.audio 4.0.1
- `scipy==1.16.3`
- `scikit-learn==1.7.2`

**Audio Processing:**
- `soundfile==0.13.1`
- `ffmpeg-python==0.2.0`
- `julius==0.2.7`
- `asteroid-filterbanks==0.4.0`

**OpenTelemetry** (required by pyannote.audio 4.0.1):
- `opentelemetry-api>=1.34.0`
- `opentelemetry-exporter-otlp>=1.34.0`
- `opentelemetry-sdk>=1.34.0`

**Installation time:** ~5-10 minutes depending on internet speed.

---

## Step 6: Apply WhisperX Patches

**🚨 CRITICAL:** WhisperX 3.7.4 is not compatible with pyannote.audio 4.0.1's new API. Manual patches are REQUIRED for the system to work.

**Why patches are needed:** pyannote.audio 4.0.1 renamed the authentication parameter from `use_auth_token` to `token`. WhisperX 3.7.4 still uses the old parameter name.

### 6.1 Patch File #1: vads/pyannote.py

```bash
sed -i 's/use_auth_token/token/g' venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py
```

This replaces ALL occurrences of `use_auth_token` with `token` in the pyannote diarization module.

### 6.2 Patch File #2: asr.py (Line 412)

```bash
sed -i '412s/use_auth_token=None/token=None/' venv/lib/python3.12/site-packages/whisperx/asr.py
```

This updates line 412 in the ASR module to use the new parameter name.

### 6.3 Verify Patches Applied

```bash
# Check vads/pyannote.py has no use_auth_token references
grep -c "use_auth_token" venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py
# Should output: 0

# Check asr.py has no use_auth_token on line 412
sed -n '412p' venv/lib/python3.12/site-packages/whisperx/asr.py
# Should show: token=None (not use_auth_token=None)
```

**✅ If patches applied correctly:** Both commands show the new `token` parameter.

**❌ If patches failed:** re-run the sed commands above.

---

## Step 7: Configure Environment

### 7.1 Set up Environment Variables

Copy the example environment file:

```bash
cp setup_env.sh.example setup_env.sh
```

### 7.2 Get Hugging Face Token

1. Go to https://huggingface.co/settings/tokens
2. Create a new token (read access is sufficient)
3. Accept model agreements for:
   - https://huggingface.co/pyannote/speaker-diarization-3.1
   - https://huggingface.co/pyannote/segmentation-3.0

### 7.3 Edit setup_env.sh

```bash
nano setup_env.sh
```

Add your Hugging Face token:

```bash
#!/bin/bash
export HF_TOKEN="hf_YourActualTokenHere"
echo "Environment variables set"
echo "HF_TOKEN: ${HF_TOKEN:0:20}..."
```

Save and exit (Ctrl+X, Y, Enter).

### 7.4 Make Executable

```bash
chmod +x setup_env.sh
```

### 7.5 Set LD_LIBRARY_PATH (REQUIRED for cuDNN)

Add to your shell profile for permanent use:

```bash
echo 'export LD_LIBRARY_PATH=$HOME/Projects/stratomercata-website/venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

**What this does:** Tells the system where to find cuDNN 9.10.2 libraries that come bundled with PyTorch nightly.

---

## Step 8: Verify Installation

### 8.1 Load Environment

```bash
source setup_env.sh
source venv/bin/activate
export LD_LIBRARY_PATH=venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH
```

### 8.2 Test GPU Detection

```bash
python3 -c "import torch; x = torch.randn(100,100, device='cuda'); print('✅ GPU test passed:', x.matmul(x).sum().item())"
```

**Expected:** Should print "✅ GPU test passed: (some number)"

### 8.3 Test cuDNN Loading

```bash
python3 -c "import torch; import torch.backends.cudnn as cudnn; print('✅ cuDNN version:', cudnn.version()); print('✅ cuDNN enabled:', cudnn.is_available())"
```

**Expected output:**
```
✅ cuDNN version: 90102
✅ cuDNN enabled: True
```

### 8.4 Test WhisperX Import

```bash
python3 -c "import whisperx; print('✅ WhisperX imported successfully')"
```

### 8.5 Test pyannote.audio Import

```bash
python3 -c "from pyannote.audio import Pipeline; print('✅ pyannote.audio imported successfully')"
```

**✅ If all tests pass:** System is ready for transcription!

**❌ If any test fails:** See Troubleshooting section below.

---

## Running Transcription

### Complete Pipeline with Transcription + Diarization

```bash
# 1. Activate environment
source setup_env.sh
source venv/bin/activate
export LD_LIBRARY_PATH=venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH

# 2. Run transcription with speaker diarization
python3 transcribe_with_diarization.py path/to/audio.mp3
```

**What it does:**
1. Transcribes audio using WhisperX (Whisper large-v2 model)
2. Automatically converts MP3 to WAV if needed (avoids sample count issues)
3. Identifies speakers using pyannote.audio diarization
4. Assigns speakers to transcript segments
5. Saves formatted transcript with speaker labels

**Output file:** `path/to/audio_transcript_with_speakers.txt`

### Example Output Format

```
SPEAKER_00:
[0.0s] Hello everyone, welcome to the show.
[5.2s] Today we're talking about blockchain technology.

SPEAKER_01:
[12.5s] Thanks for having me.
[14.3s] I'm excited to discuss this topic.
```

---

## Performance Benchmarks

**Hardware:** NVIDIA GeForce RTX 5070 (12GB VRAM, Blackwell/sm_120)

### Actual Measured Performance

**79-minute audio file (episode003-bob-summerwill.mp3):**
- Transcription: 98.7 seconds (1.6 minutes) - **~48x realtime**
- Diarization: 208.6 seconds (3.5 minutes)
- Speaker assignment: ~6 seconds
- **Total pipeline: 314.7 seconds (5.2 minutes) - ~15x realtime**
- Speaker detection: 5 speakers, 839 segments
- Output: 72KB transcript file

**58-minute audio file (institutions_want_tokens.mp3):**
- Transcription: 65 seconds (1.1 minutes) - **~53x realtime**
- Diarization: Not tested

**GPU Performance During Processing:**
- GPU utilization: 90-95%
- VRAM usage: 8-10GB peak
- Temperature: Normal operating range
- No thermal throttling observed

**Comparison to Manual Transcription:**
- Manual transcription (estimated): ~8-13 hours for 79-minute audio
- RTX 5070 complete pipeline: 5.2 minutes
- **Speed improvement: ~95-150x faster than manual transcription**

---

## Troubleshooting

### Issue: nvidia-smi doesn't work or shows wrong driver

**Symptoms:**
- `nvidia-smi` command not found
- Shows driver < 565
- Shows CUDA < 12.8

**Solution:**
```bash
# Reinstall NVIDIA driver (same command as Step 1.2 with --reinstall flag)
sudo ubuntu-drivers install --reinstall
sudo reboot
```

### Issue: PyTorch can't find CUDA/GPU

**Symptoms:**
- `torch.cuda.is_available()` returns `False`
- Error: "CUDA not available"

**Solutions:**
1. Verify nvidia-smi works first
2. Reinstall PyTorch nightly:
   ```bash
   pip uninstall torch torchvision torchaudio -y
   pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
   ```
3. Reboot system
4. Check LD_LIBRARY_PATH is set

### Issue: "CUDA capability sm_120 not supported"

**Cause:** Using PyTorch stable instead of nightly.

**Solution:**
```bash
# Verify PyTorch version shows "dev" (nightly)
pip show torch | grep Version
# Should show: Version: 2.10.0.devYYYYMMDD+cu128

# If not nightly, reinstall:
pip uninstall torch torchvision torchaudio -y
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
```

### Issue: "Unable to load libcudnn_cnn.so.9"

**Cause:** LD_LIBRARY_PATH not set.

**Solution:**
```bash
export LD_LIBRARY_PATH=venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH

# Add to ~/.bashrc for permanent fix:
echo 'export LD_LIBRARY_PATH=$HOME/Projects/stratomercata-website/venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

### Issue: "TypeError: ... got an unexpected keyword argument 'use_auth_token'"

**Cause:** WhisperX patches not applied.

**Solution:**
```bash
# Re-apply patches
sed -i 's/use_auth_token/token/g' venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py
sed -i '412s/use_auth_token=None/token=None/' venv/lib/python3.12/site-packages/whisperx/asr.py

# Verify patches applied
grep -c "use_auth_token" venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py
# Should output: 0
```

### Issue: MP3 diarization fails with sample count mismatch

**Cause:** pyannote.audio strict sample validation with variable bitrate MP3s.

**Solution:** The script automatically converts MP3 to WAV. If it still fails:
```bash
# Manually convert MP3 to WAV first
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
python3 transcribe_with_diarization.py output.wav
```

### Issue: Out of memory errors

**Symptoms:**
- "CUDA out of memory"
- System crashes during processing

**Solutions:**
1. Close other GPU-using applications
2. Use smaller Whisper model (edit transcribe_with_diarization.py):
   ```python
   model = whisperx.load_model("medium", device, compute_type="float16")
   # Instead of "large-v2"
   ```
3. Process shorter audio files
4. Reduce batch size in transcribe_audio function

### Issue: Slow performance despite GPU

**Check:**
```bash
# Monitor GPU usage during transcription
watch -n 1 nvidia-smi
```

**Should show:**
- GPU Utilization: 90-95%
- Memory Usage: 8-10GB during processing

**If GPU utilization is low (<50%):**
- Check if using CPU fallback
- Verify CUDA is available in PyTorch
- Check for thermal throttling (overheating)

---

## Complete Setup Checklist

Use this checklist to verify everything is installed correctly:

- [ ] Ubuntu 24.04 LTS installed
- [ ] System packages updated (`sudo apt update && sudo apt upgrade`)
- [ ] NVIDIA driver 565+ installed
- [ ] System rebooted after driver installation
- [ ] `nvidia-smi` shows RTX 5070 and CUDA 12.8+
- [ ] FFmpeg installed (`ffmpeg -version` works)
- [ ] Python 3.12 venv created
- [ ] PyTorch 2.10.0.dev nightly installed
- [ ] `torch.cuda.is_available()` returns `True`
- [ ] All requirements.txt packages installed
- [ ] WhisperX patches applied (both files)
- [ ] Patches verified (no `use_auth_token` remaining)
- [ ] HF_TOKEN set in setup_env.sh
- [ ] LD_LIBRARY_PATH exported
- [ ] GPU test passes (can multiply tensors on cuda)
- [ ] cuDNN loads successfully
- [ ] WhisperX imports without errors
- [ ] pyannote.audio imports without errors
- [ ] Test transcription completes successfully

---

## Additional Notes

### Why No System CUDA Installation?

PyTorch nightly bundles all required CUDA libraries in the venv. You do NOT need to:
- Install CUDA toolkit system-wide
- Install cuDNN separately
- Set CUDA_HOME or similar variables

**Only requirement:** NVIDIA driver 565+ (provides kernel modules and basic GPU access)

### Why PyTorch Nightly?

RTX 5070 uses Blackwell architecture (compute capability sm_120) released in 2025. PyTorch stable releases were compiled before this architecture existed. Only nightly builds have sm_120 support compiled in.

### Version Compatibility Matrix

| Component | Version Required | Why |
|-----------|-----------------|-----|
| NVIDIA Driver | 565+ | RTX 50-series support |
| CUDA (bundled) | 12.8 | sm_120 compute capability |
| PyTorch | 2.10.0.dev nightly | sm_120 support |
| pyannote.audio | 4.0.1 | PyTorch 2.10+ compatibility |
| NumPy | 2.0+ | pyannote.audio 4.0.1 requirement |
| cuDNN (bundled) | 9.10.2 | Comes with PyTorch nightly |

### Future Updates

When PyTorch 2.10+ stable is released (estimated Q1 2026):
- Can switch from nightly to stable
- Patches may still be needed until WhisperX updates
- Setup will be simpler (no nightly index URL needed)

---

**Last Updated:** November 3, 2025
**Tested On:** Ubuntu 24.04 LTS with NVIDIA GeForce RTX 5070
**Python Version:** 3.12.3
**PyTorch Version:** 2.10.0.dev20251103+cu128
**Status:** ✅ Fully working, production-ready

---

## Support

For issues specific to this setup:
- Check the Troubleshooting section above
- Review README.md and whisperx_readme.md
- Open an issue on the repository

For general WhisperX issues:
- https://github.com/m-bain/whisperX

For pyannote.audio issues:
- https://github.com/pyannote/pyannote-audio
