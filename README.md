# STRATO Mercata Website

The official website for STRATO Mercata - a platform to easily earn on vaulted gold, silver & crypto with instant credit. Built by Ethereum veterans.

## About This Project

**STRATO Mercata** is a Jekyll-based static website that serves as the primary web presence for STRATO Mercata. The site features video content, team member profiles, and information about the platform's capabilities.

### What You'll Find Here

- **Team Profiles**: Biographies and profiles of STRATO Mercata team members
- **Video Content**: Show episodes, contest announcements, and platform demonstrations
- **Blog**: Platform updates, announcements, and educational content
- **Platform Information**: Details about trading, lending, and borrowing on real-world assets

---

## Jekyll Setup

This is a static site built with Jekyll 4.3+ and deployed via GitHub Pages.

### Project Structure

```
stratomercata-website/
├── _config.yml                # Jekyll configuration
├── Gemfile                    # Ruby dependencies
└── source/                    # Jekyll source directory
    ├── _layouts/              # Page templates (default, person, blog, video)
    ├── _includes/             # Reusable components (auto_link, embeds, SEO)
    ├── _blog/                 # Blog collection (Markdown files)
    ├── _people/               # People collection (Markdown files)
    ├── _videos/               # Video collection (Markdown files)
    ├── blog/index.html        # Blog listing page
    ├── people/index.html      # People listing page
    ├── videos/index.html      # Videos listing page
    ├── assets/css/            # Stylesheets
    ├── images/                # Image assets
    └── videos/raw-audio/      # Source audio files for transcription
```

### Configuration Philosophy

The `_config.yml` file contains production settings:
- **`baseurl: ""`**: Empty for custom domain at root
- **`url: "https://stratomercata.com"`**: Production domain

For local development, Jekyll's `serve` command automatically overrides the `url` setting to `http://localhost:4000`.

---

## Local Development

### Prerequisites

- Ruby 3.3+ or Ruby 3.4+ (install via [rbenv](https://github.com/rbenv/rbenv) or [rvm](https://rvm.io/))
- Bundler: `gem install bundler`

**Note for Ruby 3.4+**: The `Gemfile` includes compatibility gems (`base64`, `logger`, `bigdecimal`) required for Jekyll 3.10.0 on Ruby 3.4+.

### Setup & Run

```bash
# Install dependencies
bundle install

# Clean, build, and serve with incremental builds
bundle exec jekyll clean && bundle exec jekyll serve --incremental

# Access at http://localhost:4000
```

The development server includes:
- **Auto-regeneration**: Changes to source files trigger automatic rebuilds
- **Incremental builds**: Only changed files are rebuilt (faster)
- **LiveReload**: Browser refreshes automatically when files change

---

## Collections

The site uses three Jekyll collections:

### Blog (`_blog/`)
Platform updates, announcements, and educational content about STRATO Mercata.

### People (`_people/`)
Team member profiles with photos, bios, and social links.

Example frontmatter:
```yaml
---
name: Bob Summerwill
role: Head of Ecosystem
photo: /images/bobsummerwill.com/2025.08.26/bob-summerwill.jpeg
twitter: bobsummerwill
linkedin: bob-summerwill
---
```

### Videos (`_videos/`)
Show episodes, contests, and platform demonstrations with embedded YouTube videos and transcripts.

Example frontmatter:
```yaml
---
title: "STRATO Mercata Show: State of Blockchain"
date: 2025-10-08
hosts: ["Bob Summerwill", "Victor Wong", "Kieren James-Lubin"]
description: "Reflections on TOKEN2049 in Singapore"
embed:
  url: https://www.youtube.com/embed/VIDEO_ID
---
```

---

## Workflow: Adding Video Content with Transcripts

### Option 1: Automated Local Transcription (WhisperX)

For high-quality local transcription with speaker diarization using WhisperX on GPU.

#### Prerequisites

**System Requirements:**
- NVIDIA GPU (tested on RTX 5070)
- Ubuntu 24.04+ (or compatible Linux)
- Python 3.10+ (3.12 recommended, comes with Ubuntu 24.04)
- CUDA 12.1+ compatible setup
- FFmpeg

**🚨 IMPORTANT: Automated Setup Scripts**

```bash
# Step 1: Install NVIDIA drivers (RTX 5070 requires driver 565+)
# Skip this step if you don't have an NVIDIA GPU
sudo ./install_nvidia_drivers.sh
sudo reboot

# Step 2: Setup Python environment (after reboot)
# Auto-detects hardware (NVIDIA GPU vs CPU)
# For CPU-only on a GPU system, add --force-cpu
./install_packages_and_venv.sh

# Step 3: Configure HuggingFace token
nano setup_env.sh  # Add your HF_TOKEN
```

**What the scripts do:**
- Detect hardware (NVIDIA GPU vs CPU) or use `--force-cpu` flag
- Install system dependencies (ffmpeg, build tools, Python dev)
- Install PyTorch nightly (CUDA 13.0 for NVIDIA, CPU-only otherwise)
- Install WhisperX, pyannote.audio, SpeechBrain
- Apply WhisperX compatibility patches automatically
- Configure LD_LIBRARY_PATH (NVIDIA only)
- Run verification tests

**Note:** PyTorch nightly is used for all hardware to support RTX 5070 Blackwell (sm_120). Will switch to stable PyTorch 2.6+ when available (Q1-Q2 2026).

#### NVIDIA Driver Installation

1. **Install latest NVIDIA drivers (550+ required for RTX 50-series):**
```bash
# Check current driver version
nvidia-smi

# If driver is outdated, install latest:
sudo apt update
sudo apt install -y nvidia-driver-565  # or latest available
sudo reboot
```

2. **Verify CUDA is detected:**
```bash
nvidia-smi
# Should show CUDA Version: 13.0 or newer
```

3. **Install FFmpeg for audio extraction:**
```bash
sudo apt install -y ffmpeg
```

#### Python Environment Setup

1. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Install PyTorch NIGHTLY with CUDA 13.0 support (REQUIRED for RTX 5070):**
```bash
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu130
```

This installs:
- PyTorch 2.10.0.dev20251104+cu130 (or later nightly)
- torchvision 0.25.0.dev20251104+cu130
- torchaudio 2.10.0.dev20251104+cu130
- Bundled CUDA libraries including cuDNN 9.10.2.21, NCCL 2.27.5, cuBLAS, cuFFT, etc.

3. **Install remaining Python dependencies:**
```bash
pip install -r requirements-base.txt
```

**About Requirements Files:**

This project uses hardware-specific requirements files:
- **requirements-nvidia.txt** - PyTorch nightly with CUDA 13.0 for NVIDIA GPUs
- **requirements-cpu.txt** - PyTorch nightly CPU-only for non-NVIDIA systems
- **requirements-base.txt** - WhisperX, pyannote.audio, SpeechBrain (hardware-agnostic)
- **requirements-nvidia-lock.txt** - Complete dependency snapshot for NVIDIA systems
- **requirements-cpu-lock.txt** - Complete dependency snapshot for CPU systems

**Generating/Updating Lock Files:**

For NVIDIA systems:
```bash
pip install -r requirements-nvidia.txt
pip install -r requirements-base.txt
pip freeze > requirements-nvidia-lock.txt
```

For CPU systems:
```bash
pip install -r requirements-cpu.txt
pip install -r requirements-base.txt
pip freeze > requirements-cpu-lock.txt
```

4. **Apply WhisperX patches (REQUIRED):**

Edit `venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py`:
```bash
# Change all occurrences of use_auth_token to token:
sed -i 's/use_auth_token/token/g' venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py
```

Edit `venv/lib/python3.12/site-packages/whisperx/asr.py`:
```bash
# Line 412: change use_auth_token=None to token=None
sed -i '412s/use_auth_token=None/token=None/' venv/lib/python3.12/site-packages/whisperx/asr.py
```

5. **Verify GPU is working:**
```bash
python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"
```

Expected output:
```
PyTorch: 2.10.0.dev20251104+cu130
CUDA available: True
GPU: NVIDIA GeForce RTX 5070
```

6. **Set up environment variables:**
```bash
cp setup_env.sh.example setup_env.sh
# Edit setup_env.sh and add your Hugging Face token
chmod +x setup_env.sh
source setup_env.sh
```

Get a Hugging Face token at: https://huggingface.co/settings/tokens

You'll need to accept the terms for:
- pyannote/segmentation-3.0
- pyannote/speaker-diarization-3.1

#### Extract Audio and Transcribe

1. **Extract audio from video:**
```bash
ffmpeg -i "video-file.mp4" -q:a 0 -map a source/videos/raw-audio/output-audio.mp3
```

2. **Run transcription with speaker diarization:**
```bash
source setup_env.sh
source venv/bin/activate

# Set LD_LIBRARY_PATH (required for PyTorch nightly - see SETUP_RTX_5070.md Step 7.5)
export LD_LIBRARY_PATH=venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH

python3 transcribe_with_diarization.py source/videos/raw-audio/output-audio.mp3
```

This will:
- Detect and separate speakers automatically
- Generate transcript with speaker labels
- Create output file: `output-audio_transcript_with_speakers.txt`
- **Performance on RTX 5070:** ~65 seconds for 58-minute audio (transcription only)

3. **Optional: Map speakers to names:**
```bash
python3 map_speakers_to_names.py \
  source/videos/raw-audio/output-audio_transcript_with_speakers.txt \
  source/videos/raw-audio/output-audio_transcript_with_speakers_with_names.txt \
  --speaker-map "SPEAKER_00=Bob Summerwill,SPEAKER_01=Victor Wong"
```

#### Troubleshooting

**CUDA Compatibility Issues:**
If you see errors about CUDA capability sm_120 not being supported:
- **Solution:** Install PyTorch nightly with CUDA 13.0 (not stable releases)
- Run: `pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu130`
- Verify PyTorch version shows "2.10.0.dev" or newer: `pip show torch`

**NVIDIA Driver Issues:**
If `nvidia-smi` shows an older CUDA version (< 13.0):
- Install newer drivers: `sudo apt install nvidia-driver-565`
- Reboot: `sudo reboot`
- Verify: `nvidia-smi` should show CUDA 13.0+

**cuDNN Loading Errors:**
If you see "Unable to load libcudnn_cnn.so.9":
- **Solution:** Set LD_LIBRARY_PATH before running:
  ```bash
  export LD_LIBRARY_PATH=venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH
  ```
- PyTorch nightly bundles cuDNN 9.10.2 in the venv, just needs to be found
- Add this export to your shell profile for convenience

**pyannote.audio API Errors:**
If you see "TypeError: ... got an unexpected keyword argument 'use_auth_token'":
- **Solution:** Apply the WhisperX patches described in setup step 4
- This error means the manual patches weren't applied correctly
- The patches change `use_auth_token` to `token` for pyannote.audio 4.0.1 compatibility

**Version Compatibility Warnings:**
WhisperX 3.7.4 shows warnings about requiring PyTorch 2.8.0, but it works with PyTorch nightly 2.10.0. These warnings can be safely ignored as long as transcription completes successfully.

**RTX 5070 Performance:**
- Transcription (WhisperX large-v2): ~65 seconds for 58-minute audio
- GPU utilization: ~90-95% during transcription
- VRAM usage: ~8-10GB peak

For more details, see `whisperx_readme.md` and `USAGE.md`.

### Option 2: Manual Transcription (TurboScribe)

1. Upload the audio file to [TurboScribe](https://turboscribe.ai)
2. Select **Whale Transcription** mode
3. Enable **Speaker Recognition** in settings
4. Set number of speakers (usually 2-3)
5. Click **Transcribe**
6. Export transcript as **TXT** with **Section Timestamps**

### Save Audio File

Store the MP3 for future reference:
```
source/videos/raw-audio/show-name-YYYY-MM-DD.mp3
```

### 4. Create Video Page

Copy an existing video page as a template:

```bash
cp source/_videos/existing-video.md source/_videos/new-video-YYYY-MM-DD.md
```

Update the frontmatter with new details.

### 5. Add Transcript

1. Export transcript from TurboScribe as **TXT** with **Section Timestamps** enabled
2. Paste the content into the video page body
3. Transform speaker labels and timestamps

Example transformation:
```
[Speaker 1] (0:03 - 0:05)

becomes:

[[0:03]](https://www.youtube.com/watch?v=VIDEO_ID&t=3s) **Bob:**
```

Where `3s` is the starting timestamp in seconds.

### 6. Verify Locally

```bash
bundle exec jekyll clean && bundle exec jekyll serve --incremental
```

Visit http://localhost:4000/videos/ to verify the new video appears correctly.

---

## Deployment

### Netlify Deployment

Netlify provides zero-config Jekyll support with automatic PR preview deployments.

**Benefits:**
- Automatic PR preview deployments (each PR gets a unique preview URL)
- Faster build times
- Unlimited bandwidth on free tier
- Zero configuration needed (auto-detects Jekyll)

**Setup:**
1. Go to https://app.netlify.com
2. Click "Add new site" → "Import an existing project"
3. Choose GitHub and select your repository
4. Netlify auto-detects Jekyll settings
5. Click "Deploy site"

**PR Previews:**
- Enabled by default
- Each PR gets: `deploy-preview-{PR#}--{site}.netlify.app`
- Rebuilds automatically on every commit
- Preview URL posted as GitHub comment

**Ruby 3.4 Compatibility:**
The `Gemfile` includes all required compatibility gems for Netlify's Ruby 3.4 environment.

---

## Development Tips

### Auto-linking System

The site includes an auto-linking system (`source/_includes/auto_link.html`) that automatically converts mentions of people, blog posts, and videos to links:

```markdown
Bob Summerwill spoke about blockchain.
```

Automatically becomes:
```html
<a href="/people/bob-summerwill/">Bob Summerwill</a> spoke about blockchain.
```

The system processes content in priority order:
1. **Hidden People** - Removes/redacts links to hidden profiles
2. **Videos** - Links video titles to their pages
3. **Blog Posts** - Links blog post titles to their pages
4. **People** - Links person names (with conflict detection to avoid nested links)

### Relative URLs

Always use Jekyll's `relative_url` filter for internal links:

```liquid
[Link text]({{ '/people/bob-summerwill/' | relative_url }})
```

This ensures links work correctly in both local development and production.

### Image Paths

Images are organized by source and date:
```
source/images/bobsummerwill.com/2025.08.26/photo.jpeg
source/images/linkedin.com/2025.10.07/profile.png
source/images/stratomercata.com/2025.10.07/screenshot.png
```

Always use relative paths with the `relative_url` filter for images.

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

### Git Remote Setup

**Main repository:**
- `upstream` → https://github.com/stratomercata/stratomercata-website

**Your fork:**
- `origin` → https://github.com/YOUR_USERNAME/stratomercata-website

To sync your fork with upstream:
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0) - see the [LICENSE](LICENSE) file for details.

---

## Support

For questions or support:
- Open an [issue](https://github.com/stratomercata/stratomercata-website/issues)
- Contact [@bobsummerwill](https://x.com/bobsummerwill) on X/Twitter
- Visit [STRATO Mercata](https://www.stratomercata.com)
