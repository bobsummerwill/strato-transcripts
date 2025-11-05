# RTX 5070 Blackwell GPU Support - Dependency Chain Explanation

## Overview

This document explains the chain of dependencies required to support the NVIDIA RTX 5070 Blackwell GPU for WhisperX transcription with speaker diarization.

## The Dependency Chain

### 1. RTX 5070 Blackwell Architecture
- **Compute Capability**: sm_120 (Blackwell architecture)
- **Release**: November 2024
- **Problem**: This is a brand new architecture that older software doesn't support

### 2. NVIDIA Driver Requirement
- **Minimum**: Driver 565+
- **Why**: Only these drivers include support for Blackwell architecture
- **Installation**: `./install_nvidia_drivers.sh` installs driver 565.57.01

### 3. PyTorch Nightly Requirement
- **Required**: PyTorch nightly builds (not stable 2.5.1)
- **Why**: Stable PyTorch 2.5.1 only supports up to sm_90 (Hopper/Ada architectures)
- **sm_120 Support**: Only available in nightly builds as of November 2024
- **Future**: Will be in stable PyTorch 2.6+ (expected Q1-Q2 2026)

### 4. CUDA Version: 12.8 (not 13.0)
- **Choice**: CUDA 12.8 (cu128) instead of CUDA 13.0 (cu130)
- **Why 12.8**:
  - More stable and mature
  - Better ecosystem compatibility
  - All cu12 packages work together seamlessly
  - Avoids library version mismatches
  
- **Why NOT 13.0**:
  - Still experimental/bleeding-edge
  - Mix of cu12 and cu13 packages causes conflicts
  - Missing .so.13 libraries (only .so.12 available)
  - Requires workarounds (symlinks) that are fragile

#### CUDA 13.0 Issues We Encountered:
```
Problem: PyTorch cu130 looks for libcupti.so.13
Reality: nvidia-cuda-cupti-cu12 only provides libcupti.so.12
Workaround needed: Creating symlinks .so.12 -> .so.13
```

This happened because:
- PyTorch nightly cu130 expects CUDA 13 libraries
- But pip packages still ship CUDA 12 libraries (nvidia-*-cu12)
- Creating a version mismatch nightmare

### 5. pyannote.audio 4.0.1+ Requirement
- **Required**: pyannote.audio >= 4.0.1
- **Why**: Compatibility with PyTorch nightly (2.10+)
- **Older versions**: pyannote.audio 3.x doesn't work with PyTorch 2.10+
- **WhisperX Issue**: WhisperX initially installs 3.x, we must upgrade to 4.0.1+

### 6. WhisperX Patching
- **Problem**: WhisperX uses deprecated `use_auth_token` parameter
- **Solution**: Patch to use `token` parameter instead
- **Compatibility**: Required for pyannote.audio 4.0.1+
- **Files Patched**:
  - `whisperx/vads/pyannote.py` (global replacement)
  - `whisperx/asr.py` (line 412)

### 7. LD_LIBRARY_PATH Configuration
- **Why Needed**: PyTorch nightly packages CUDA libraries separately
- **Problem**: System linker can't find nvidia/*/lib directories automatically
- **Solution**: Export LD_LIBRARY_PATH with all NVIDIA library paths
- **Directories Added**:
  ```
  - nvidia/cudnn/lib
  - nvidia/cuda_runtime/lib
  - nvidia/cuda_cupti/lib
  - nvidia/cuda_nvrtc/lib
  - nvidia/cublas/lib
  - nvidia/cufft/lib
  - nvidia/curand/lib
  - nvidia/cusolver/lib
  - nvidia/cusparse/lib
  - nvidia/cufile/lib
  - nvidia/nvjitlink/lib
  - nvidia/nvtx/lib
  ```

## Complete Dependency Chain

```
RTX 5070 Hardware (sm_120)
    ↓ requires
NVIDIA Driver 565+
    ↓ enables
CUDA 12.8 Support
    ↓ used by
PyTorch Nightly (cu128)
    ↓ required by
pyannote.audio 4.0.1+
    ↓ used by
WhisperX (with patches)
    ↓ enables
Audio Transcription + Speaker Diarization on RTX 5070
```

## Why This Specific Configuration?

### Option 1: PyTorch Stable + CUDA 12.8 ❌
- **Problem**: Stable PyTorch doesn't support sm_120
- **Result**: GPU won't be detected at all

### Option 2: PyTorch Nightly + CUDA 13.0 ❌
- **Problem**: Library version mismatches (cu12 vs cu13)
- **Result**: Runtime errors like `libcupti.so.13: cannot open shared object file`
- **Workaround**: Complex symlink management (fragile)

### Option 3: PyTorch Nightly + CUDA 12.8 ✅
- **Benefits**:
  - sm_120 support from nightly builds
  - Stable CUDA 12.8 with mature ecosystem
  - All cu12 packages work together
  - No version mismatch issues
  - No symlink workarounds needed
- **Result**: Everything works seamlessly

## Installation Process

The `install_packages_and_venv.sh` script handles this dependency chain:

1. **Detect Hardware** (RTX 5070 detected)
2. **Install System Deps** (ffmpeg, build-essential, etc.)
3. **Create Virtual Environment**
4. **Install PyTorch Nightly cu128** (from requirements-nvidia.txt)
5. **Verify PyTorch** (CUDA available, GPU detected, cuDNN working)
6. **Install WhisperX** (from requirements-base.txt)
7. **Patch WhisperX** (use_auth_token → token)
8. **Upgrade pyannote.audio** (to 4.0.1+)
9. **Reinstall PyTorch Nightly** (in case WhisperX downgraded it)
10. **Configure LD_LIBRARY_PATH** (add all nvidia/*/lib directories)
11. **Verify Imports** (whisperx and pyannote.audio work)

## Future: When to Switch to Stable PyTorch

Once PyTorch stable 2.6+ is released with Blackwell support (expected Q1-Q2 2026):

1. Update `requirements-nvidia.txt`:
   ```txt
   --index-url https://download.pytorch.org/whl/cu128
   torch>=2.6.0
   torchvision>=0.17.0
   torchaudio>=2.6.0
   ```

2. No more `--pre` flag needed
3. No more nightly builds
4. More stable, tested releases

## Troubleshooting

### GPU Not Detected
```bash
python3 -c "import torch; print(torch.cuda.is_available())"
# Should print: True
```
- Check: `nvidia-smi` works
- Check: Driver 565+ installed
- Check: PyTorch nightly cu128 installed

### Import Errors
```bash
python3 -c "from pyannote.audio import Pipeline"
```
- Check: LD_LIBRARY_PATH configured in ~/.bashrc
- Check: Virtual environment activated
- Check: pyannote.audio >= 4.0.1

### Library Not Found Errors
- Check: `~/.bashrc` has LD_LIBRARY_PATH export
- Run: `source ~/.bashrc`
- Check: All nvidia/*/lib directories exist in venv

## Key Files

- `requirements-nvidia.txt` - PyTorch nightly cu128 specification
- `install_packages_and_venv.sh` - Automated installation script
- `install_nvidia_drivers.sh` - NVIDIA driver 565+ installation
- `~/.bashrc` - LD_LIBRARY_PATH configuration (auto-added)

## Summary

The RTX 5070 requires a specific, carefully orchestrated dependency chain:
- **New GPU** → Needs new drivers (565+)
- **New drivers** → Enable CUDA 12.8
- **CUDA 12.8** → Supports PyTorch nightly
- **PyTorch nightly** → Has sm_120 support
- **sm_120 support** → Makes RTX 5070 work
- **All with CUDA 12.8** → Avoids cu12/cu13 conflicts

This configuration provides the most stable, compatible path to RTX 5070 support.
