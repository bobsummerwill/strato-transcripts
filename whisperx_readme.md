# WhisperX Transcription Pipeline
# ==============================================================================
# Automated audio/video transcription with speaker diarization for Jekyll sites
# ==============================================================================
#
# WHAT THIS DOES:
# - Converts audio/video to text using OpenAI's Whisper AI model
# - Identifies speakers using pyannote.audio voice analysis
# - Maps generic speaker labels (SPEAKER_01) to actual names
# - Formats output as Jekyll-ready markdown
#
# PERFORMANCE:
# - RTX 5070 GPU: 79-minute audio in 5.2 minutes (~15x realtime)
# - Manual transcription: Same audio takes 8-13 hours
# - Speed improvement: ~95-150x faster than manual
# - Accuracy: 95%+ with good audio quality
#
# WHY USE THIS:
# - Free after GPU purchase (vs $1-2/hour cloud GPUs)
# - Processes while you work on other tasks
# - Consistent quality and formatting
# - Automatic speaker identification
#
# WHEN TO USE AUTOMATED SCRIPTS:
# - RTX 5070 Blackwell GPU: Use ./install_packages_and_venv.sh (see below)
# - Other NVIDIA GPUs: Manual setup or use automated scripts
# - CPU-only systems: Use ./install_packages_and_venv.sh --force-cpu
#
# ==============================================================================

---

## Quick Setup (Automated)

**For all systems (auto-detects hardware):**

```bash
# Step 1: Install NVIDIA drivers (skip if no NVIDIA GPU)
sudo ./install_nvidia_drivers.sh
sudo reboot

# Step 2: Setup Python environment
# Auto-detects hardware or use --force-cpu for CPU-only
./install_packages_and_venv.sh

# Step 3: Configure HuggingFace token
nano setup_env.sh  # Add your HF_TOKEN from https://huggingface.co/settings/tokens
```

**What it installs:**
- System dependencies (ffmpeg, build tools, Python dev)
- PyTorch nightly (CUDA 13.0 for NVIDIA, CPU-only otherwise)
- WhisperX, pyannote.audio, SpeechBrain
- Applies compatibility patches automatically
- Configures LD_LIBRARY_PATH (NVIDIA only)

---

## Usage

### HuggingFace Token Setup

Required for pyannote.audio models:

1. Get token: https://huggingface.co/settings/tokens
2. Accept model agreements:
   - https://huggingface.co/pyannote/speaker-diarization-3.1
   - https://huggingface.co/pyannote/segmentation-3.0
3. Configure in setup_env.sh (already done if you used automated scripts)

### Complete Pipeline

```bash
# Activate environment
source venv/bin/activate
export HF_TOKEN="hf_YourTokenHere"

# 1. Transcribe with speaker identification
python3 diarize_and_combine.py audio.mp3
# Output: audio_transcript_with_speakers.txt

# 2. Map speaker labels to names (edit map_speakers_to_names.py first)
python3 map_speakers_to_names.py audio_transcript_with_speakers.txt
# Output: audio_transcript_with_speakers_with_names.txt

# 3. Format for Jekyll
python3 format_transcript_for_markdown.py \
    audio_transcript_with_speakers_with_names.txt \
    formatted.txt
# Output: formatted.txt (ready for Jekyll)
```

### Speaker Mapping

Before running step 2, edit `map_speakers_to_names.py`:

```python
SPEAKER_MAP = {
    'SPEAKER_01': 'Bob Summerwill',     # Usually main guest (most segments)
    'SPEAKER_02': 'Kieren James-Lubin', # Usually host
    'SPEAKER_03': 'Jim Hormuzdiar',     # Usually co-host
}
```

**How to identify speakers:**
1. Read first few pages of `_transcript_with_speakers.txt`
2. Match speaking patterns to known participants
3. Script reports segment counts to help identify main speakers

---

## Performance

### Hardware Benchmarks

**RTX 5070 (12GB VRAM, Blackwell/sm_120):**
- 79-min audio: 5.2 minutes total (transcription + diarization)
- 58-min audio: 65 seconds (transcription only, ~53x realtime)
- GPU utilization: 90-95%
- VRAM usage: 8-10GB peak

**Manual transcription estimate:**
- 79-min audio: 8-13 hours
- **Speed improvement: ~95-150x faster**

### Hardware Requirements

**Minimum (CPU only):**
- 8GB RAM, 50GB disk space
- Expect hours of processing time

**Recommended (GPU):**
- NVIDIA: GTX 1660+ (6GB+ VRAM) or RTX 20/30/40/50 series
- AMD: RX 6600+ (8GB+ VRAM)
- 16GB RAM, 50GB disk space

**Optimal:**
- NVIDIA RTX 5070/4090 or AMD RX 7900 XTX
- 32GB RAM, SSD storage
- For RTX 5070: Use automated setup scripts

---

## Troubleshooting

### Common Issues

**"HF_TOKEN environment variable not set"**
```bash
export HF_TOKEN="hf_YourTokenHere"
echo 'export HF_TOKEN="hf_YourTokenHere"' >> ~/.bashrc  # Make permanent
```

**"Permission denied" for model access**
- Visit pyannote model pages and click "Agree and access repository"
- Links: https://huggingface.co/pyannote/speaker-diarization-3.1
- Wait 1-2 minutes for permissions to propagate

**"CUDA out of memory"**
- Use smaller Whisper model: Edit `diarize_and_combine.py` 
- Change `"large-v2"` to `"medium"` or `"small"`

**"CUDA capability sm_120 not supported"**
- Install PyTorch nightly: `pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu130`
- Or use automated setup scripts

**"Unable to load libcudnn_cnn.so.9"**
```bash
export LD_LIBRARY_PATH=venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH
```

**"TypeError: got unexpected keyword 'use_auth_token'"**
- Apply WhisperX patches:
```bash
sed -i 's/use_auth_token/token/g' venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py
sed -i '412s/use_auth_token=None/token=None/' venv/lib/python3.12/site-packages/whisperx/asr.py
```

**PyTorch can't find GPU**
- Verify: `python3 -c "import torch; print(torch.cuda.is_available())"`
- If False, reinstall PyTorch with correct CUDA version

### RTX 5070 Specific

**Requirements:**
- PyTorch 2.10.0.dev nightly (not stable)
- CUDA 13.0 support
- NVIDIA driver 565+
- WhisperX patches applied

**Why:** Blackwell architecture (sm_120) not in stable PyTorch yet

**When to switch:** PyTorch 2.6+ stable (expected Q1-Q2 2026)

**Verification:**
```bash
python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"
```

Expected output:
```
PyTorch: 2.10.0.dev20251104+cu130
CUDA: True
GPU: NVIDIA GeForce RTX 5070
```

---

## Tips & Best Practices

### Audio Quality
- **Good:** Clean podcast recordings, one speaker at a time
- **Bad:** Conference calls, overlapping speakers, noisy backgrounds
- **Tip:** Normalize audio levels with Audacity before processing

### Workflow
1. Test first 5 minutes before processing full audio
2. Keep all intermediate files (can re-run mapping without re-transcribing)
3. Expect 10-20% manual review of transcripts
4. GPU can batch process videos overnight

### Accuracy
- Whisper large-v2 model: 95%+ on clear audio
- Speaker diarization: 90%+ accuracy with distinct voices
- Technical terms/names need manual review
- Background noise significantly impacts quality

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
- Edit SPEAKER_MAP dictionary before running
- Reports segment counts to help identify speakers
- Output: `filename_with_names.txt`

**format_transcript_for_markdown.py**
- Converts to Jekyll-ready markdown format
- Adds ** ** around speaker names
- Preserves timestamps
- Output: Jekyll-compatible markdown

### Test Scripts

- `test_diarization.py` - Test speaker diarization only
- `test_diarization_hf.py` - Test HuggingFace authentication
- `test_cuda.py` / `test_rocm.py` - Test GPU availability

---

## Version Compatibility

**Tested:**
- Python: 3.8 - 3.12
- PyTorch: 2.0.0 - 2.2.0 (older GPUs), 2.10.0.dev (RTX 5070)
- CUDA: 11.8, 12.1, 13.0 (nightly)
- Ubuntu: 20.04, 22.04, 24.04
- Windows: 10, 11 (WSL2 recommended)

**GPU Support:**
- RTX 50-series (Blackwell): PyTorch 2.10.0.dev nightly + CUDA 13.0
- RTX 40-series (Ada Lovelace): PyTorch 2.0+ stable
- RTX 30-series (Ampere): PyTorch 2.0+ stable
- GTX 16-series (Turing): PyTorch 2.0+ stable

---

## Resources

**Documentation:**
- [WhisperX GitHub](https://github.com/m-bain/whisperX)
- [Whisper by OpenAI](https://github.com/openai/whisper)
- [pyannote.audio](https://github.com/pyannote/pyannote-audio)
- [HuggingFace](https://huggingface.co/)

**Getting Help:**
- Check [WhisperX Issues](https://github.com/m-bain/whisperX/issues)
- Check [pyannote Discussions](https://github.com/pyannote/pyannote-audio/discussions)
- File issues on this repository

---

## License

Scripts provided as-is for STRATO Mercata project. Modify as needed.

**Dependencies:**
- WhisperX: MIT License
- PyTorch: BSD License
- pyannote.audio: MIT License
- Whisper: MIT License

---

**Last Updated:** November 2025  
**Tested Hardware:** RTX 5070, RTX 3090, RX 7900 XTX  
**Test Case:** 79-minute audio, 6 speakers  
**Success Rate:** 95%+ transcription, 90%+ speaker ID
