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
# OPERATING SYSTEM SUPPORT:
#   - macOS Sonoma (14.x)
#   - Ubuntu 24.04 LTS
#   Note: Script will fail immediately on any other OS or version
#
# HARDWARE SUPPORT:
#   - NVIDIA GPUs: RTX 5070 Blackwell, RTX 50/40/30/20 series, GTX, Tesla
#   - CPU-only: Any system without NVIDIA GPU (including AMD GPUs via CPU)
#
# WHAT IT DOES:
#   1. Detects OS and version
#   2. Detects hardware (NVIDIA GPU vs CPU)
#   3. Installs system dependencies (ffmpeg, build tools, Python dev)
#   4. Creates isolated Python virtual environment
#   5. Installs WhisperX and dependencies
#   6. Installs PyTorch 2.9.0 (GPU or CPU)
#   7. Verifies PyTorch installation
#   8. Applies compatibility patches to WhisperX
#   9. Installs pyannote.audio 4.0+
#  10. Applies compatibility patches to SpeechBrain
#  11. Configures LD_LIBRARY_PATH for NVIDIA
#  12. Verifies package installations
#  13. Installs AI provider SDKs (transcription & post-processing)
#  14. Builds Ethereum glossaries
#  15. Sets up environment configuration file
#
# REQUIREMENTS:
#   - macOS Sonoma (14.x) OR Ubuntu 24.04 LTS
#   - Python 3.12
#   - macOS: Homebrew installed (script will check and guide installation)
#   - Ubuntu: sudo access for system package installation
#   - For NVIDIA (Ubuntu): Driver 565+ installed (run install_nvidia_drivers.sh first)
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
# Step 0: OS Detection and Validation
# ==============================================================================
# Detect the operating system and version.
# Only macOS Sonoma (14.x) and Ubuntu 24.04 LTS are supported.
# Script will exit immediately if run on any other OS or version.
# ==============================================================================
echo -e "${YELLOW}[0/15] Detecting operating system...${NC}"

OS_TYPE=""
OS_VERSION=""

if [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macos"
    # Get macOS version
    OS_VERSION=$(sw_vers -productVersion)
    OS_MAJOR=$(echo "$OS_VERSION" | cut -d. -f1)
    
    echo "Detected macOS version: $OS_VERSION"
    
    if [ "$OS_MAJOR" -ne 14 ]; then
        echo -e "${RED}ERROR: Unsupported macOS version${NC}"
        echo "This script requires macOS Sonoma (14.x)"
        echo "Your version: $OS_VERSION"
        exit 1
    fi
    
    echo -e "${GREEN}✓ macOS Sonoma detected${NC}"
    
    # Check for Homebrew
    if ! command -v brew &> /dev/null; then
        echo -e "${RED}ERROR: Homebrew not installed${NC}"
        echo "Homebrew is required for macOS installations."
        echo "Install it from: https://brew.sh"
        echo "Then run this script again."
        exit 1
    fi
    echo -e "${GREEN}✓ Homebrew is installed${NC}"
    
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="ubuntu"
    
    # Check if it's Ubuntu
    if [ ! -f /etc/os-release ]; then
        echo -e "${RED}ERROR: Cannot detect Linux distribution${NC}"
        exit 1
    fi
    
    source /etc/os-release
    
    if [ "$ID" != "ubuntu" ]; then
        echo -e "${RED}ERROR: Unsupported Linux distribution${NC}"
        echo "This script requires Ubuntu 24.04 LTS"
        echo "Your distribution: $ID $VERSION_ID"
        exit 1
    fi
    
    echo "Detected Ubuntu version: $VERSION_ID"
    
    if [ "$VERSION_ID" != "24.04" ]; then
        echo -e "${RED}ERROR: Unsupported Ubuntu version${NC}"
        echo "This script requires Ubuntu 24.04 LTS"
        echo "Your version: $VERSION_ID"
        exit 1
    fi
    
    echo -e "${GREEN}✓ Ubuntu 24.04 LTS detected${NC}"
    
else
    echo -e "${RED}ERROR: Unsupported operating system${NC}"
    echo "This script requires either:"
    echo "  - macOS Sonoma (14.x)"
    echo "  - Ubuntu 24.04 LTS"
    exit 1
fi

echo ""

# ==============================================================================
# Step 1: Hardware Detection
# ==============================================================================
# Detect if an NVIDIA GPU is present to determine which PyTorch variant to install.
# Uses nvidia-smi command which is only available with NVIDIA drivers installed.
# Sets HAS_NVIDIA flag used throughout script for conditional logic.
# Can be overridden with --force-cpu flag to force CPU-only installation.
# ==============================================================================
echo -e "${YELLOW}[1/15] Detecting hardware...${NC}"

if [ "$FORCE_CPU" = true ]; then
    HAS_NVIDIA=false
    echo -e "${YELLOW}--force-cpu flag detected${NC}"
    echo -e "${YELLOW}⚠ Forcing CPU-only mode (ignoring any NVIDIA GPU)${NC}"
    echo "Will install PyTorch 2.9.0 CPU-only version"
elif [ "$OS_TYPE" = "macos" ]; then
    HAS_NVIDIA=false
    echo -e "${YELLOW}⚠ macOS detected - using CPU/MPS mode${NC}"
    echo "Will install PyTorch 2.9.0 CPU-only version (Metal Performance Shaders supported)"
elif command -v nvidia-smi &> /dev/null && nvidia-smi &> /dev/null; then
    HAS_NVIDIA=true
    GPU_NAME=$(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo "NVIDIA GPU")
    echo -e "${GREEN}✓ Detected NVIDIA GPU: $GPU_NAME${NC}"
    echo "Will install PyTorch 2.9.0 with CUDA 13.0 support"
else
    HAS_NVIDIA=false
    echo -e "${YELLOW}⚠ No NVIDIA GPU detected - using CPU mode${NC}"
    echo "Will install PyTorch 2.9.0 CPU-only version"
fi
echo ""

# ==============================================================================
# Step 2: System Dependencies and AI Tools Installation
# ==============================================================================
# Install required system packages using appropriate package manager.
# macOS: Uses Homebrew (brew)
# Ubuntu: Uses apt package manager
# These are low-level dependencies needed to build Python packages and process audio.
# ==============================================================================
echo -e "${YELLOW}[2/15] Installing system dependencies...${NC}"

if [ "$OS_TYPE" = "macos" ]; then
    echo "Installing required packages via Homebrew:"
    echo "  - ffmpeg: Audio/video processing for WhisperX"
    echo "  - python@3.12: Python 3.12 interpreter"
    echo "  - git: Version control for installing packages from GitHub"
    
    # Install packages if not already present
    brew list ffmpeg &>/dev/null || brew install ffmpeg
    brew list python@3.12 &>/dev/null || brew install python@3.12
    brew list git &>/dev/null || brew install git
    
    # Set Python 3.12 from Homebrew as the python3 command
    echo "Setting up Python 3.12 from Homebrew..."
    export PATH="/opt/homebrew/opt/python@3.12/libexec/bin:$PATH"
    
    # Verify we're using the correct Python version
    DETECTED_PY_VERSION=$(python3 --version)
    echo "Using: $DETECTED_PY_VERSION"
    
    echo -e "${GREEN}✓ System dependencies installed${NC}"
    
elif [ "$OS_TYPE" = "ubuntu" ]; then
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
fi

    echo -e "${GREEN}✓ Ollama ready for local AI processing${NC}"
    echo "  • Pull models as needed: ollama pull <model>"
    echo "  • See available models: ollama list"
fi
echo ""

# ==============================================================================
# Step 4: Python Virtual Environment Creation
# ==============================================================================
# Create an isolated Python environment to avoid conflicts with system packages.
# If venv already exists, it's removed and recreated to ensure clean state.
# All subsequent Python packages will be installed into this venv.
# ==============================================================================
echo -e "${YELLOW}[4/15] Creating Python virtual environment...${NC}"
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
# Step 5: Install Base Packages
# ==============================================================================
# Installs WhisperX, AI provider SDKs, and dependencies from requirements.txt.
# WhisperX will pull PyTorch 2.8.0, which we'll upgrade in the next step.
# Includes transcription services (AssemblyAI, Deepgram, OpenAI)
# and post-processing services (Anthropic, Google Gemini, OpenAI).
# ==============================================================================
echo -e "${YELLOW}[5/15] Installing base packages...${NC}"
echo "Installing WhisperX, AI provider SDKs, and dependencies from requirements.txt"
echo "Note: WhisperX will pull PyTorch 2.8.0 (we'll upgrade to 2.9.0 next)"
echo "This may take 5-10 minutes..."
pip install -r "$PROJECT_DIR/requirements.txt"
echo -e "${GREEN}✓ Base packages installed${NC}"
echo ""

# ==============================================================================
# Step 6: PyTorch Upgrade to 2.9.0
# ==============================================================================
# Upgrades PyTorch from 2.8.0 (WhisperX default) to 2.9.0.
# PyTorch 2.9.0 provides:
#   - Ubuntu: Full Blackwell (sm_120) support with CUDA 13.0 for RTX 50-series
#   - macOS: Latest optimizations with MPS (Metal Performance Shaders) support
# Both platforms use PyTorch 2.9.0 for version consistency.
# Uses --force-reinstall to ensure correct variant is installed.
# ==============================================================================
echo -e "${YELLOW}[6/15] Upgrading PyTorch to 2.9.0...${NC}"
echo "Upgrading PyTorch 2.8.0 → 2.9.0 for consistency across platforms"

if [ "$OS_TYPE" = "ubuntu" ]; then
    echo "Platform: Ubuntu - installing with CUDA 13.0 support"
    echo "Provides full Blackwell (sm_120) support for RTX 50-series GPUs"
    echo "This may take 2-5 minutes depending on internet speed..."
    pip install --force-reinstall --index-url https://download.pytorch.org/whl/cu130 \
        torch==2.9.0 \
        torchvision==0.24.0 \
        torchaudio==2.9.0
    echo -e "${GREEN}✓ PyTorch 2.9.0+cu130 installed${NC}"
else
    echo "Platform: macOS - installing with MPS (Metal) support"
    echo "This may take 2-5 minutes depending on internet speed..."
    pip install --force-reinstall \
        torch==2.9.0 \
        torchaudio==2.9.0
    echo -e "${GREEN}✓ PyTorch 2.9.0 installed${NC}"
fi
echo ""

# ==============================================================================
# Step 7: PyTorch Verification
# ==============================================================================
# Verifies PyTorch installation and hardware accessibility.
# For NVIDIA: Confirms CUDA availability, GPU operations, and cuDNN functionality.
# For CPU/MPS: Confirms basic CPU tensor operations work correctly.
# Ensures the installation is ready for machine learning workloads.
# ==============================================================================
echo -e "${YELLOW}[7/15] Verifying PyTorch installation...${NC}"
echo "Verifying PyTorch installation and hardware access..."

python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'MPS available: {torch.backends.mps.is_available() if hasattr(torch.backends, \"mps\") else False}'); print(f'Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"CPU/MPS\"}')"

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
    
    if [ "$OS_TYPE" = "macos" ]; then
        echo "Testing MPS (Metal) availability..."
        python3 -c "import torch; print('✓ MPS available:', torch.backends.mps.is_available() if hasattr(torch.backends, 'mps') else False)"
    fi
    
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
# Note: sed syntax differs between macOS and Linux
# ==============================================================================
echo -e "${YELLOW}[8/15] Applying WhisperX patches...${NC}"
echo "Updating WhisperX to use 'token' parameter for HuggingFace authentication"
echo "Enables compatibility with pyannote.audio 4.x"

# Find the actual site-packages directory (handles any Python version)
SITE_PACKAGES=$(python3 -c "import site; print(site.getsitepackages()[0])")
WHISPERX_VADS="$SITE_PACKAGES/whisperx/vads/pyannote.py"
WHISPERX_ASR="$SITE_PACKAGES/whisperx/asr.py"

if [ ! -f "$WHISPERX_VADS" ]; then
    echo -e "${RED}ERROR: WhisperX vads/pyannote.py not found at $WHISPERX_VADS${NC}"
    exit 1
fi

if [ ! -f "$WHISPERX_ASR" ]; then
    echo -e "${RED}ERROR: WhisperX asr.py not found at $WHISPERX_ASR${NC}"
    exit 1
fi

# Apply patches (handling sed differences between macOS and Linux)
if [ "$OS_TYPE" = "macos" ]; then
    sed -i '' 's/use_auth_token/token/g' "$WHISPERX_VADS"
    sed -i '' '412s/use_auth_token=None/token=None/' "$WHISPERX_ASR"
else
    sed -i 's/use_auth_token/token/g' "$WHISPERX_VADS"
    sed -i '412s/use_auth_token=None/token=None/' "$WHISPERX_ASR"
fi

# Verify patches
VADS_COUNT=$(grep -c "use_auth_token" "$WHISPERX_VADS" || true)
if [ "$VADS_COUNT" -ne 0 ]; then
    echo -e "${RED}ERROR: Patch verification failed for vads/pyannote.py${NC}"
    exit 1
fi

echo -e "${GREEN}✓ WhisperX patches applied successfully${NC}"
echo ""

# ==============================================================================
# Step 9: pyannote.audio Installation
# ==============================================================================
# Installs pyannote.audio 4.0+, which provides PyTorch 2.9.0 compatibility.
# Version 4.0+ is required to work with PyTorch 2.9.0's API and features.
# ==============================================================================
echo -e "${YELLOW}[9/15] Installing pyannote.audio 4.0+...${NC}"
echo "Installing pyannote.audio 4.0+ for PyTorch 2.9.0 compatibility..."
pip install --upgrade "pyannote.audio>=4.0.1,<4.0.2"
echo -e "${GREEN}✓ pyannote.audio 4.0+ installed${NC}"
echo ""

# ==============================================================================
# Step 10: SpeechBrain Compatibility Patches
# ==============================================================================
# Updates SpeechBrain to work with torchaudio 2.9.0's API.
# Adds hasattr() check to gracefully handle different torchaudio versions.
# This ensures SpeechBrain can detect available audio backends across versions.
# ==============================================================================
echo -e "${YELLOW}[10/15] Applying SpeechBrain compatibility patches...${NC}"
echo "Updating SpeechBrain for torchaudio 2.9.0 compatibility"
echo "Adding version-agnostic audio backend detection"

SPEECHBRAIN_BACKEND="$SITE_PACKAGES/speechbrain/utils/torch_audio_backend.py"

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
# Step 11: LD_LIBRARY_PATH Configuration (project-specific via setup_env.sh)
# ==============================================================================
# Ensures setup_env.sh includes LD_LIBRARY_PATH for CUDA libraries
# Project-specific (only active when setup_env.sh is sourced)
# NOT added to ~/.bashrc to avoid global conflicts with other tools
# ==============================================================================
echo -e "${YELLOW}[11/15] Configuring LD_LIBRARY_PATH in setup_env.sh${NC}"
echo "Adding CUDA library paths to setup_env.sh (project-specific, not global)"

if [ -f "$PROJECT_DIR/setup_env.sh" ]; then
    # Check if LD_LIBRARY_PATH already configured
    if grep -q "LD_LIBRARY_PATH.*nvidia/cudnn" "$PROJECT_DIR/setup_env.sh"; then
        echo "✓ LD_LIBRARY_PATH already configured in setup_env.sh"
    else
        echo "Updating setup_env.sh to include LD_LIBRARY_PATH..."
        # Note: This should already be in the template, but this is a fallback
        echo "⚠ LD_LIBRARY_PATH not found - it should be in setup_env.sh.example template"
    fi
else
    echo "⚠ setup_env.sh not found - will be created in Step 14"
fi
echo ""

# ==============================================================================
# Step 12: Application Package Verification
# ==============================================================================
# Verifies WhisperX and pyannote.audio can be imported successfully.
# Import tests confirm all dependencies are properly installed and accessible.
# This validation ensures the environment is ready for transcription tasks.
# ==============================================================================
echo -e "${YELLOW}[12/15] Verifying package installations...${NC}"
echo "Testing imports to ensure all packages are properly installed and accessible"

echo "Testing WhisperX import..."
python3 -c "import whisperx; print('✓ WhisperX imported successfully')"

echo "Testing pyannote.audio import..."
python3 -c "from pyannote.audio import Pipeline; print('✓ pyannote.audio imported successfully')"

echo -e "${GREEN}✓ All packages verified and ready to use${NC}"
echo ""

# ==============================================================================
# Step 13: Verify AI Provider SDKs
# ==============================================================================
# Verifies that AI provider SDKs were installed from requirements.txt.
# These packages were already installed in Step 5 along with WhisperX.
# ==============================================================================
echo -e "${YELLOW}[13/15] Verifying AI provider SDKs...${NC}"
echo "Verifying packages installed from requirements.txt:"
echo "  Cloud transcription: assemblyai, deepgram-sdk, openai"
echo "  AI post-processing: anthropic, google-generativeai"
echo "  Utilities: requests"

# Test key imports
python3 -c "import assemblyai; print('✓ assemblyai')"
python3 -c "import deepgram; print('✓ deepgram-sdk')"
python3 -c "import openai; print('✓ openai')"
python3 -c "import anthropic; print('✓ anthropic')"
python3 -c "import google.generativeai; print('✓ google-generativeai')"
python3 -c "import requests; print('✓ requests')"

echo -e "${GREEN}✓ All AI provider SDKs verified${NC}"
echo ""

# ==============================================================================
# Step 14: Create Project Directories
# ==============================================================================
# Create intermediates and outputs directories for transcript processing.
# Ethereum glossaries (people/terms) are now generated on-demand during
# post-processing rather than at install time, as they're only needed then.
# ==============================================================================
echo -e "${YELLOW}[14/15] Creating project directories...${NC}"
echo "Creating project directory structure..."
mkdir -p "$PROJECT_DIR/intermediates"
mkdir -p "$PROJECT_DIR/outputs"
echo "✓ Created intermediates/ and outputs/ directories"
echo ""
echo "Note: Ethereum glossaries will be generated when needed during post-processing"
echo "      Run scripts/extract_people.py or extract_terms.py manually if desired"
echo ""

# ==============================================================================
# Step 15: Environment File Setup
# ==============================================================================
# Creates setup_env.sh from template if needed.
# This file stores the HuggingFace token for downloading pyannote models.
# User provides their token manually (see post-installation instructions).
# ==============================================================================
echo -e "${YELLOW}[15/15] Setting up environment configuration...${NC}"
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
if [ "$OS_TYPE" = "macos" ]; then
    echo "   nano setup_env.sh  (or use your preferred editor)"
else
    echo "   nano setup_env.sh"
fi
echo ""
echo "3. Accept model agreements:"
echo "   - https://huggingface.co/pyannote/speaker-diarization-3.1"
echo "   - https://huggingface.co/pyannote/segmentation-3.0"
echo ""
echo -e "${YELLOW}OPTIONAL: Get API keys for remote AI providers${NC}"
echo ""
echo "4. For cloud-based AI providers (if not using local Ollama):"
echo "   - OpenAI (GPT-4.1): https://platform.openai.com/api-keys"
echo "   - Anthropic (Claude): https://console.anthropic.com/"
echo "   - Google (Gemini): https://makersuite.google.com/app/apikey"
echo ""
echo -e "${GREEN}Ready to use!${NC}"
echo ""
echo "Basic Usage:"
echo "  source setup_env.sh"
echo "  source venv/bin/activate"
echo "  ./scripts/process_single.sh audio.mp3 --transcribers whisperx --processors openai"
echo ""
echo "Available transcribers: whisperx, deepgram, assemblyai"
echo "Available processors: sonnet, chatgpt, gemini, llama"
echo ""
echo "Batch Processing:"
echo "  ./scripts/process_all.sh --transcribers deepgram --processors anthropic"
echo ""
echo "See README.md and AI_PROVIDERS_GUIDE.md for complete documentation."
echo ""
