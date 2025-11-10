#!/bin/bash
# ==============================================================================
# Python Environment Setup Script for WhisperX Transcription
# ==============================================================================
#
# DESCRIPTION:
#   Automated setup script that installs and configures WhisperX for audio
#   transcription with speaker diarization. Supports both NVIDIA GPU and
#   CPU-only systems with automatic hardware detection.
#
# HARDWARE SUPPORT:
#   - NVIDIA GPUs: RTX 5070 Blackwell, RTX 50/40/30/20 series, GTX, Tesla
#   - CPU-only: Any system without NVIDIA GPU (including AMD GPUs via CPU)
#
# WHAT IT DOES:
#   1. Detects hardware (NVIDIA GPU vs CPU)
#   2. Installs system dependencies (ffmpeg, build tools, Python dev)
#   3. Creates isolated Python virtual environment
#   4. Installs WhisperX and dependencies
#   5. Installs PyTorch 2.9.0 (GPU or CPU)
#   6. Verifies PyTorch installation
#   7. Applies compatibility patches to WhisperX
#   8. Installs pyannote.audio 4.0+
#   9. Applies compatibility patches to SpeechBrain
#  10. Configures LD_LIBRARY_PATH for NVIDIA
#  11. Verifies package installations
#  12. Installs AI provider SDKs (transcription & post-processing)
#  13. Builds Ethereum glossaries
#  14. Sets up environment configuration file
#
# REQUIREMENTS:
#   - Ubuntu 24.04 LTS (or compatible Debian-based system)
#   - Python 3.12
#   - For NVIDIA: Driver 565+ installed (run install_nvidia_drivers.sh first)
#   - sudo access for system package installation
#
# USAGE:
#   ./install_packages_and_venv.sh                    # Auto-detect hardware
#   ./install_packages_and_venv.sh --force-cpu        # Force CPU-only mode
#
# OPTIONS:
#   --force-cpu       Force CPU-only installation even if NVIDIA GPU is present
#                     Useful for testing or when you want CPU mode on GPU system
#
# POST-INSTALLATION:
#   1. Get HuggingFace token: https://huggingface.co/settings/tokens
#   2. Edit setup_env.sh and add your token
#   3. Accept model agreements:
#      - https://huggingface.co/pyannote/speaker-diarization-3.1
#      - https://huggingface.co/pyannote/segmentation-3.0
#
# TROUBLESHOOTING:
#   - If nvidia-smi fails: Reboot after driver installation
#   - If PyTorch can't detect GPU: Check CUDA installation and driver version
#   - If imports fail: Ensure virtual environment is activated
#
# ==============================================================================

set -e  # Exit immediately if any command fails

# Terminal color codes for formatted output
RED='\033[0;31m'       # Error messages
GREEN='\033[0;32m'     # Success messages
YELLOW='\033[1;33m'    # Warning/info messages
BLUE='\033[0;34m'      # Section headers
NC='\033[0m'           # No Color (reset)

# Project directories - resolved to absolute paths
# Script is in ./scripts/, so go up one level to project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"  # Project root (parent of scripts/)
VENV_DIR="$PROJECT_DIR/venv"                  # Virtual environment location

# Parse command-line arguments
FORCE_CPU=false
for arg in "$@"; do
    case $arg in
        --force-cpu)
            FORCE_CPU=true
            shift
            ;;
        *)
            echo -e "${RED}Error: Unknown option: $arg${NC}"
            echo "Usage: $0 [--force-cpu]"
            exit 1
            ;;
    esac
done

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Python Environment Setup for WhisperX${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ==============================================================================
# Step 1: Hardware Detection
# ==============================================================================
# Detect if an NVIDIA GPU is present to determine which PyTorch variant to install.
# Uses nvidia-smi command which is only available with NVIDIA drivers installed.
# Sets HAS_NVIDIA flag used throughout script for conditional logic.
# Can be overridden with --force-cpu flag to force CPU-only installation.
# ==============================================================================
echo -e "${YELLOW}[1/14] Detecting hardware...${NC}"

if [ "$FORCE_CPU" = true ]; then
    HAS_NVIDIA=false
    echo -e "${YELLOW}--force-cpu flag detected${NC}"
    echo -e "${YELLOW}⚠ Forcing CPU-only mode (ignoring any NVIDIA GPU)${NC}"
    echo "Will install PyTorch nightly CPU-only version"
elif command -v nvidia-smi &> /dev/null && nvidia-smi &> /dev/null; then
    HAS_NVIDIA=true
    GPU_NAME=$(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo "NVIDIA GPU")
    echo -e "${GREEN}✓ Detected NVIDIA GPU: $GPU_NAME${NC}"
    echo "Will install PyTorch nightly with CUDA 13.0 support"
else
    HAS_NVIDIA=false
    echo -e "${YELLOW}⚠ No NVIDIA GPU detected - using CPU mode${NC}"
    echo "Will install PyTorch nightly CPU-only version"
fi
echo ""

# ==============================================================================
# Step 2: System Dependencies and AI Tools Installation
# ==============================================================================
# Install required system packages and optional AI tools.
# System packages: Build tools, audio processing, Python development
# Optional AI tools: Ollama for local/private AI post-processing (FREE)
# Requires sudo access for system-wide installation.
# ==============================================================================
echo -e "${YELLOW}[2/14] Installing system dependencies and AI tools...${NC}"
echo "Installing required system packages:"
echo "  - build-essential: C/C++ compilers for building Python packages"
echo "  - ca-certificates: SSL/TLS certificates for secure connections"
echo "  - curl: HTTP client for API requests"
echo "  - ffmpeg: Audio/video processing for WhisperX"
echo "  - git: Version control for installing packages from GitHub"
echo "  - libcurl4-openssl-dev: cURL development libraries for Python packages"
echo "  - libssl-dev: SSL development libraries"
echo "  - python3-dev: Python headers for compiling extensions"
echo "  - python3-pip: Python package installer"
echo "  - python3-venv: Python virtual environment support"
sudo apt update
sudo apt install -y \
  build-essential \
  ca-certificates \
  curl \
  ffmpeg \
  git \
  libcurl4-openssl-dev \
  libssl-dev \
  python3-dev \
  python3-pip \
  python3-venv
echo -e "${GREEN}✓ System dependencies installed${NC}"

echo ""
echo "Installing Ollama for local AI post-processing (optional, FREE, private)..."
if command -v ollama &> /dev/null; then
    echo -e "${GREEN}✓ Ollama already installed${NC}"
    OLLAMA_VERSION=$(ollama --version 2>/dev/null || echo "unknown")
    echo "  Version: $OLLAMA_VERSION"
else
    echo "Downloading and installing Ollama..."
    if curl -fsSL https://ollama.com/install.sh | sh; then
        echo -e "${GREEN}✓ Ollama installed successfully${NC}"
    else
        echo -e "${YELLOW}⚠ Ollama installation failed (non-fatal)${NC}"
        echo "  You can install it manually later: curl -fsSL https://ollama.com/install.sh | sh"
    fi
fi

# Start Ollama service and pull default model
if command -v ollama &> /dev/null; then
    echo "Starting Ollama service..."
    # Start in background, redirect output to avoid clutter
    if ! pgrep -x "ollama" > /dev/null; then
        nohup ollama serve > /tmp/ollama.log 2>&1 &
        sleep 2  # Give service time to start
        echo "✓ Ollama service started"
    else
        echo "✓ Ollama service already running"
    fi
    
    echo "Pulling recommended Ollama model (qwen2.5:32b - fast and high-quality)..."
    echo "This may take several minutes depending on your internet speed..."
    if ollama pull qwen2.5:32b 2>&1 | grep -q "success"; then
        echo -e "${GREEN}✓ Model qwen2.5:32b downloaded and ready${NC}"
    else
        # Try anyway, sometimes it succeeds but doesn't output "success"
        echo -e "${YELLOW}⚠ Model pull completed (check with: ollama list)${NC}"
    fi
fi
echo ""

# ==============================================================================
# Step 3: Python Virtual Environment Creation
# ==============================================================================
# Create an isolated Python environment to avoid conflicts with system packages.
# If venv already exists, it's removed and recreated to ensure clean state.
# All subsequent Python packages will be installed into this venv.
# ==============================================================================
echo -e "${YELLOW}[3/14] Creating Python virtual environment...${NC}"
echo "Creating isolated Python environment to avoid conflicts with system packages"
echo "Location: $VENV_DIR"
if [ -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Warning: venv directory already exists. Removing...${NC}"
    # Try normal removal first, fall back to sudo only if permission denied
    if ! rm -rf "$VENV_DIR" 2>/dev/null; then
        echo -e "${YELLOW}Permission denied - trying with sudo...${NC}"
        echo "Note: This shouldn't be necessary. The venv may have been created with sudo previously."
        sudo rm -rf "$VENV_DIR"
    fi
fi
python3 -m venv "$VENV_DIR"
echo -e "${GREEN}✓ Virtual environment created${NC}"
echo ""

# Activate the virtual environment for all subsequent pip installations
source "$VENV_DIR/bin/activate"

# ==============================================================================
# Step 4: WhisperX Installation
# ==============================================================================
# Installs WhisperX and its base dependencies.
# WhisperX pulls in PyTorch 2.8.0 as its dependency.
# We install the optimal PyTorch version for this GPU in the next step.
# ==============================================================================
echo -e "${YELLOW}[4/14] Installing WhisperX and base packages...${NC}"
echo "Installing WhisperX and dependencies from requirements-base.txt"
echo "Note: WhisperX includes PyTorch 2.8.0 (we install 2.9.0 next for GPU optimization)"
echo "This may take 5-10 minutes..."
pip install -r "$PROJECT_DIR/requirements-base.txt"
echo -e "${GREEN}✓ WhisperX and base packages installed${NC}"
echo ""

# ==============================================================================
# Step 5: PyTorch Installation
# ==============================================================================
# Installs PyTorch 2.9.0 with CUDA 13.0 for optimal GPU performance.
# PyTorch 2.9.0 provides full Blackwell (sm_120) support for RTX 50-series GPUs.
# CUDA 13.0 offers the latest optimizations and performance improvements.
# ==============================================================================
echo -e "${YELLOW}[5/14] Installing PyTorch 2.9.0...${NC}"
echo "Installing PyTorch 2.9.0 stable with CUDA 13.0"
echo "Provides full Blackwell (sm_120) support for RTX 50-series GPUs"
echo "This may take 2-5 minutes depending on internet speed..."
if [ "$HAS_NVIDIA" = true ]; then
    echo "Installing from: requirements-nvidia.txt (PyTorch 2.9.0 + CUDA 13.0)"
    pip install --force-reinstall -r "$PROJECT_DIR/requirements-nvidia.txt"
else
    echo "Installing from: requirements-cpu.txt (PyTorch 2.9.0 CPU-only)"
    pip install --force-reinstall -r "$PROJECT_DIR/requirements-cpu.txt"
fi
echo -e "${GREEN}✓ PyTorch 2.9.0 installed${NC}"
echo ""

# ==============================================================================
# Step 6: PyTorch Verification
# ==============================================================================
# Verifies PyTorch installation and hardware accessibility.
# For NVIDIA: Confirms CUDA availability, GPU operations, and cuDNN functionality.
# For CPU: Confirms basic CPU tensor operations work correctly.
# Ensures the installation is ready for machine learning workloads.
# ==============================================================================
echo -e "${YELLOW}[6/14] Verifying PyTorch installation...${NC}"
echo "Verifying PyTorch installation and hardware access..."
python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"

if [ "$HAS_NVIDIA" = true ]; then
    if ! python3 -c "import torch; assert torch.cuda.is_available(), 'CUDA not available'" 2>/dev/null; then
        echo -e "${RED}ERROR: PyTorch cannot detect CUDA/GPU${NC}"
        exit 1
    fi
    
    echo "Testing GPU operations..."
    python3 -c "import torch; x = torch.randn(100,100, device='cuda'); print('✓ GPU test passed:', x.matmul(x).sum().item())"
    
    echo "Testing cuDNN..."
    python3 -c "import torch.backends.cudnn as cudnn; print('✓ cuDNN version:', cudnn.version()); print('✓ cuDNN enabled:', cudnn.is_available())"
    
    echo -e "${GREEN}✓ PyTorch verified - GPU ready${NC}"
else
    echo "Testing CPU operations..."
    python3 -c "import torch; x = torch.randn(100,100); print('✓ CPU test passed:', x.matmul(x).sum().item())"
    
    echo -e "${GREEN}✓ PyTorch verified - CPU ready${NC}"
fi
echo ""

# ==============================================================================
# Step 8: WhisperX Compatibility Patches
# ==============================================================================
# Updates WhisperX source code to use 'token' parameter for HuggingFace authentication.
# This enables compatibility with pyannote.audio 4.x API.
# Patches are applied with sed and verified.
# Files modified: vads/pyannote.py (global replace) and asr.py (line 412).
# ==============================================================================
echo -e "${YELLOW}[7/14] Applying WhisperX patches...${NC}"
echo "Updating WhisperX to use 'token' parameter for HuggingFace authentication"
echo "Enables compatibility with pyannote.audio 4.x"
WHISPERX_VADS="$VENV_DIR/lib/python3.12/site-packages/whisperx/vads/pyannote.py"
WHISPERX_ASR="$VENV_DIR/lib/python3.12/site-packages/whisperx/asr.py"

if [ ! -f "$WHISPERX_VADS" ]; then
    echo -e "${RED}ERROR: WhisperX vads/pyannote.py not found at $WHISPERX_VADS${NC}"
    exit 1
fi

if [ ! -f "$WHISPERX_ASR" ]; then
    echo -e "${RED}ERROR: WhisperX asr.py not found at $WHISPERX_ASR${NC}"
    exit 1
fi

# Apply patches
sed -i 's/use_auth_token/token/g' "$WHISPERX_VADS"
sed -i '412s/use_auth_token=None/token=None/' "$WHISPERX_ASR"

# Verify patches
VADS_COUNT=$(grep -c "use_auth_token" "$WHISPERX_VADS" || true)
if [ "$VADS_COUNT" -ne 0 ]; then
    echo -e "${RED}ERROR: Patch verification failed for vads/pyannote.py${NC}"
    exit 1
fi

echo -e "${GREEN}✓ WhisperX patches applied successfully${NC}"
echo ""

# ==============================================================================
# Step 8: pyannote.audio Installation
# ==============================================================================
# Installs pyannote.audio 4.0+, which provides PyTorch 2.9.0 compatibility.
# Version 4.0+ is required to work with PyTorch 2.9.0's API and features.
# ==============================================================================
echo -e "${YELLOW}[8/14] Installing pyannote.audio 4.0+...${NC}"
echo "Installing pyannote.audio 4.0+ for PyTorch 2.9.0 compatibility..."
pip install --upgrade "pyannote.audio>=4.0.0"
echo -e "${GREEN}✓ pyannote.audio 4.0+ installed${NC}"
echo ""

# ==============================================================================
# Step 9: SpeechBrain Compatibility Patches
# ==============================================================================
# Updates SpeechBrain to work with torchaudio 2.9.0's API.
# Adds hasattr() check to gracefully handle different torchaudio versions.
# This ensures SpeechBrain can detect available audio backends across versions.
# ==============================================================================
echo -e "${YELLOW}[9/14] Applying SpeechBrain compatibility patches...${NC}"
echo "Updating SpeechBrain for torchaudio 2.9.0 compatibility"
echo "Adding version-agnostic audio backend detection"

SPEECHBRAIN_BACKEND="$VENV_DIR/lib/python3.12/site-packages/speechbrain/utils/torch_audio_backend.py"

if [ ! -f "$SPEECHBRAIN_BACKEND" ]; then
    echo -e "${RED}ERROR: SpeechBrain torch_audio_backend.py not found at $SPEECHBRAIN_BACKEND${NC}"
    exit 1
fi

# Create the patch - adds hasattr() check for list_audio_backends()
cat > /tmp/speechbrain_patch.py << 'PATCH_EOF'
import sys

# Read the file
with open(sys.argv[1], 'r') as f:
    content = f.read()

# Check if already patched
if 'hasattr(torchaudio, \'list_audio_backends\')' in content:
    # Verify the structure is correct
    if 'if hasattr(torchaudio, \'list_audio_backends\'):\n        available_backends = torchaudio.list_audio_backends()\n        if len(available_backends)' in content.replace('    ', ' '*4):
        print("Already patched with correct structure")
        sys.exit(0)
    else:
        print("Patch exists but structure incorrect - re-patching")

# Apply the patch - find and replace the problematic section
original = """    elif torchaudio_major >= 2 and torchaudio_minor >= 1:
        available_backends = torchaudio.list_audio_backends()

        if len(available_backends) == 0:
            logger.warning(
                "SpeechBrain could not find any working torchaudio backend. Audio files may fail to load. Follow this link for instructions and troubleshooting: https://speechbrain.readthedocs.io/en/latest/audioloading.html"
            )"""

replacement = """    elif torchaudio_major >= 2 and torchaudio_minor >= 1:
        # list_audio_backends() is not available in torchaudio 2.9.0
        if hasattr(torchaudio, 'list_audio_backends'):
            available_backends = torchaudio.list_audio_backends()
            if len(available_backends) == 0:
                logger.warning(
                    "SpeechBrain could not find any working torchaudio backend. Audio files may fail to load. Follow this link for instructions and troubleshooting: https://speechbrain.readthedocs.io/en/latest/audioloading.html"
                )
        else:
            # Newer torchaudio versions don't have list_audio_backends()
            logger.info("Using torchaudio with default audio backend")"""

if original in content:
    content = content.replace(original, replacement)
    with open(sys.argv[1], 'w') as f:
        f.write(content)
    print("Patch applied successfully")
else:
    # Try alternative matching for hasattr case
    if 'hasattr(torchaudio, \'list_audio_backends\')' in content:
        print("Already patched")
    else:
        print("ERROR: Could not find pattern to patch")
        sys.exit(1)
PATCH_EOF

# Apply the patch
python3 /tmp/speechbrain_patch.py "$SPEECHBRAIN_BACKEND"

# Verify the patch
if grep -q "hasattr(torchaudio, 'list_audio_backends')" "$SPEECHBRAIN_BACKEND"; then
    echo -e "${GREEN}✓ SpeechBrain compatibility patch applied successfully${NC}"
else
    echo -e "${RED}ERROR: SpeechBrain patch verification failed${NC}"
    exit 1
fi

# Cleanup
rm -f /tmp/speechbrain_patch.py
echo ""

# ==============================================================================
# Step 10: LD_LIBRARY_PATH Configuration (NVIDIA Only)
# ==============================================================================
# Configures system linker to locate PyTorch's CUDA libraries.
# PyTorch packages CUDA libraries as separate pip packages in the venv.
# LD_LIBRARY_PATH tells the system where to find these libraries at runtime.
# Configuration persists across sessions by adding to ~/.bashrc.
# ==============================================================================
if [ "$HAS_NVIDIA" = true ]; then
    echo -e "${YELLOW}[10/14] Configuring LD_LIBRARY_PATH for NVIDIA...${NC}"
    echo "Adding all required CUDA library paths to ~/.bashrc"
    echo "Required for PyTorch CUDA operations (cuDNN, cuBLAS, NVRTC, and CUDA 13.0 runtime)"
    
    BASHRC="$HOME/.bashrc"
    # Add all CUDA library paths needed for PyTorch + pyannote operations
    CUDNN_LIB="$VENV_DIR/lib/python3.12/site-packages/nvidia/cudnn/lib"
    CUBLAS_LIB="$VENV_DIR/lib/python3.12/site-packages/nvidia/cublas/lib"
    CU13_LIB="$VENV_DIR/lib/python3.12/site-packages/nvidia/cu13/lib"
    LD_PATH_LINE="export LD_LIBRARY_PATH=$CUDNN_LIB:$CUBLAS_LIB:$CU13_LIB:\$LD_LIBRARY_PATH"

    # Remove any existing entry
    sed -i '/Added by install_packages_and_venv.sh/d' "$BASHRC"
    sed -i '/nvidia.*LD_LIBRARY_PATH/d' "$BASHRC"
    
    # Add new entry
    echo "" >> "$BASHRC"
    echo "# Added by install_packages_and_venv.sh for PyTorch CUDA libraries" >> "$BASHRC"
    echo "$LD_PATH_LINE" >> "$BASHRC"
    
    # Set for current session
    export LD_LIBRARY_PATH="$CUDNN_LIB:$CUBLAS_LIB:$CU13_LIB:$LD_LIBRARY_PATH"
    
    echo -e "${GREEN}✓ LD_LIBRARY_PATH configured${NC}"
else
    echo -e "${YELLOW}[10/14] Skipping LD_LIBRARY_PATH configuration${NC}"
    echo "Not needed for CPU-only installations"
fi
echo ""

# ==============================================================================
# Step 11: Application Package Verification
# ==============================================================================
# Verifies WhisperX and pyannote.audio can be imported successfully.
# Import tests confirm all dependencies are properly installed and accessible.
# This validation ensures the environment is ready for transcription tasks.
# ==============================================================================
echo -e "${YELLOW}[11/14] Verifying package installations...${NC}"
echo "Testing imports to ensure all packages are properly installed and accessible"

echo "Testing WhisperX import..."
python3 -c "import whisperx; print('✓ WhisperX imported successfully')"

echo "Testing pyannote.audio import..."
python3 -c "from pyannote.audio import Pipeline; print('✓ pyannote.audio imported successfully')"

echo -e "${GREEN}✓ All packages verified and ready to use${NC}"
echo ""

# ==============================================================================
# Step 12: AI Provider SDKs Installation
# ==============================================================================
# Installs Python SDKs for cloud AI transcription and post-processing services.
# Transcription: AssemblyAI, Deepgram, OpenAI Whisper API
# Post-processing: Anthropic Claude, Google Gemini, OpenAI GPT, DeepSeek
# Also includes requests library for HTTP operations.
# ==============================================================================
echo -e "${YELLOW}[12/14] Installing AI provider SDKs...${NC}"
echo "Installing Python packages for AI transcription and post-processing services:"
echo "  Transcription providers:"
echo "    - assemblyai: AssemblyAI cloud transcription with diarization"
echo "    - deepgram-sdk: Deepgram cloud transcription (fastest, cheapest)"
echo "    - openai: OpenAI Whisper API transcription"
echo "  Post-processing providers:"
echo "    - anthropic: Claude 3.5 Sonnet for transcript correction"
echo "    - google-generativeai: Gemini 2.5 Pro for transcript correction"
echo "    - openai: GPT-4o for transcript correction (reused from above)"
echo "  Utilities:"
echo "    - requests: HTTP client for API operations"
pip install \
  anthropic \
  assemblyai \
  deepgram-sdk \
  google-generativeai \
  openai \
  requests
echo -e "${GREEN}✓ AI provider SDKs installed${NC}"
echo ""

# ==============================================================================
# Step 13: Build Ethereum Glossaries
# ==============================================================================
# Extracts people names and technical terms for quality improvement.
# These glossaries are used by AI post-processing to correct transcripts.
# Runs extract_people.py and extract_terms.py if they exist.
# Failures are non-fatal as these are optional enhancements.
# ==============================================================================
echo -e "${YELLOW}[13/14] Building Ethereum glossaries and project directories...${NC}"
echo "Creating project directory structure..."
mkdir -p "$PROJECT_DIR/intermediates"
mkdir -p "$PROJECT_DIR/outputs"
echo "✓ Created intermediates/ and outputs/ directories"

echo "Extracting domain-specific terminology for transcript quality improvement"

if [ -f "$PROJECT_DIR/scripts/extract_people.py" ]; then
    echo "Running scripts/extract_people.py..."
    if python3 "$PROJECT_DIR/scripts/extract_people.py" 2>/dev/null; then
        echo -e "${GREEN}✓ People glossary created${NC}"
    else
        echo -e "${YELLOW}⚠ extract_people.py failed (EarlyDaysOfEthereum may not be available)${NC}"
        echo "You can run manually later: python3 extract_people.py"
    fi
else
    echo -e "${YELLOW}⚠ extract_people.py not found${NC}"
fi

if [ -f "$PROJECT_DIR/scripts/extract_terms.py" ]; then
    echo "Running scripts/extract_terms.py..."
    if python3 "$PROJECT_DIR/scripts/extract_terms.py" 2>/dev/null; then
        echo -e "${GREEN}✓ Technical terms glossary created${NC}"
    else
        echo -e "${YELLOW}⚠ extract_terms.py failed${NC}"
        echo "You can run manually later: python3 extract_terms.py"
    fi
else
    echo -e "${YELLOW}⚠ extract_terms.py not found${NC}"
fi

echo ""

# ==============================================================================
# Step 14: Environment File Setup
# ==============================================================================
# Creates setup_env.sh from template if needed.
# This file stores the HuggingFace token for downloading pyannote models.
# User provides their token manually (see post-installation instructions).
# ==============================================================================
echo -e "${YELLOW}[14/14] Setting up environment configuration...${NC}"
echo "Checking for setup_env.sh (required for HuggingFace authentication)"
if [ ! -f "$PROJECT_DIR/setup_env.sh" ]; then
    if [ -f "$PROJECT_DIR/setup_env.sh.example" ]; then
        cp "$PROJECT_DIR/setup_env.sh.example" "$PROJECT_DIR/setup_env.sh"
        echo -e "${GREEN}✓ Created setup_env.sh from example template${NC}"
        echo "You'll need to edit this file to add your HuggingFace token"
    else
        echo -e "${YELLOW}Warning: setup_env.sh.example not found${NC}"
        echo "You'll need to create setup_env.sh manually"
    fi
else
    echo "setup_env.sh already exists - skipping creation"
fi
echo ""

# Final success message
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✓ Installation Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${YELLOW}MANUAL CONFIGURATION REQUIRED:${NC}"
echo ""
echo "1. Get a HuggingFace token:"
echo "   https://huggingface.co/settings/tokens"
echo ""
echo "2. Edit setup_env.sh and add your token:"
echo "   nano setup_env.sh"
echo ""
echo "3. Accept model agreements:"
echo "   - https://huggingface.co/pyannote/speaker-diarization-3.1"
echo "   - https://huggingface.co/pyannote/segmentation-3.0"
echo ""
echo -e "${YELLOW}OPTIONAL: Get API keys for remote AI providers${NC}"
echo ""
echo "4. For cloud-based AI providers (if not using local Ollama):"
echo "   - OpenAI (ChatGPT-5): https://platform.openai.com/api-keys"
echo "   - Anthropic (Claude): https://console.anthropic.com/"
echo "   - Google (Gemini): https://makersuite.google.com/app/apikey"
echo "   - DeepSeek: https://platform.deepseek.com/"
echo ""
echo -e "${GREEN}Ready to use!${NC}"
echo ""
echo "Basic Usage:"
echo "  source setup_env.sh"
echo "  source venv/bin/activate"
echo "  python3 scripts/transcribe_with_diarization.py audio.mp3 --high-quality"
echo ""
echo "Complete Pipeline (transcribe + AI correction):"
echo "  ./scripts/transcribe_and_correct.sh audio.mp3 --provider openai"
echo "  ./scripts/process_downloads.sh  # Batch process all MP3s in ~/Downloads"
echo ""
echo "See README.md and AI_PROVIDERS_GUIDE.md for complete documentation."
echo ""
