#!/bin/bash
# ==============================================================================
# Python Virtual Environment Setup Script for WhisperX Transcription
# ==============================================================================
#
# DESCRIPTION:
#   Creates isolated Python virtual environments for WhisperX transcription.
#   Supports multiple GPU backends with per-vendor venvs.
#   Does NOT require sudo — only Python/pip operations.
#
# PREREQUISITES:
#   - System packages installed (run install_packages.sh first)
#   - GPU drivers installed if applicable:
#     - NVIDIA: run install_nvidia_drivers.sh
#     - AMD: run install_amd_drivers.sh
#     - Intel: run install_intel_drivers.sh
#
# USAGE:
#   ./scripts/install_venv.sh --nvidia   # NVIDIA GPU (creates venv-nvidia)
#   ./scripts/install_venv.sh --amd      # AMD GPU via ROCm (creates venv-amd)
#   ./scripts/install_venv.sh --intel    # Intel GPU via XPU (creates venv-intel)
#   ./scripts/install_venv.sh --cpu      # CPU-only (creates venv-cpu)
#   ./scripts/install_venv.sh --all      # Create all four venvs
#
# eGPU WORKFLOW:
#   Pre-create all venvs, then activate the right one based on connected GPU:
#     source venv-nvidia/bin/activate   # NVIDIA eGPU connected
#     source venv-amd/bin/activate      # AMD eGPU connected
#     source venv-intel/bin/activate    # Intel iGPU fallback
#     source venv-cpu/bin/activate      # Pure CPU fallback
#
# POST-INSTALLATION:
#   1. Get HuggingFace token: https://huggingface.co/settings/tokens
#   2. Edit setup_env.sh and add your token
#   3. Accept model agreements:
#      - https://huggingface.co/pyannote/speaker-diarization-3.1
#      - https://huggingface.co/pyannote/segmentation-3.0
#
# ==============================================================================

set -e

# Terminal color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Project directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# ==============================================================================
# Parse Arguments
# ==============================================================================
GPU_MODE=""
INSTALL_ALL=false

show_usage() {
    echo "Usage: $0 [--nvidia|--amd|--intel|--cpu|--all]"
    echo ""
    echo "Options:"
    echo "  --nvidia    Create venv-nvidia with CUDA PyTorch"
    echo "  --amd       Create venv-amd with ROCm PyTorch"
    echo "  --intel     Create venv-intel with Intel XPU PyTorch"
    echo "  --cpu       Create venv-cpu with CPU-only PyTorch"
    echo "  --all       Create all four venvs"
    echo ""
    echo "At least one option is required."
    echo "System packages must be installed first: ./scripts/install_packages.sh"
}

for arg in "$@"; do
    case $arg in
        --nvidia) GPU_MODE="nvidia"; shift ;;
        --amd) GPU_MODE="amd"; shift ;;
        --intel) GPU_MODE="intel"; shift ;;
        --cpu|--force-cpu) GPU_MODE="cpu"; shift ;;
        --all) INSTALL_ALL=true; shift ;;
        *)
            echo -e "${RED}Error: Unknown option: $arg${NC}"
            show_usage
            exit 1
            ;;
    esac
done

if [ "$INSTALL_ALL" = false ] && [ -z "$GPU_MODE" ]; then
    echo -e "${RED}Error: No GPU mode specified${NC}"
    show_usage
    exit 1
fi

set_venv_dir() {
    local mode=$1
    case $mode in
        nvidia) VENV_DIR="$PROJECT_DIR/venv-nvidia" ;;
        amd)    VENV_DIR="$PROJECT_DIR/venv-amd" ;;
        intel)  VENV_DIR="$PROJECT_DIR/venv-intel" ;;
        cpu)    VENV_DIR="$PROJECT_DIR/venv-cpu" ;;
    esac
}

# ==============================================================================
# OS Detection
# ==============================================================================
OS_TYPE=""

if [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macos"
    OS_VERSION=$(sw_vers -productVersion)
    OS_MAJOR=$(echo "$OS_VERSION" | cut -d. -f1)
    if [ "$OS_MAJOR" -ne 14 ]; then
        echo -e "${RED}ERROR: Unsupported macOS version (requires Sonoma 14.x)${NC}"
        exit 1
    fi
    export PATH="/opt/homebrew/opt/python@3.12/libexec/bin:$PATH"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="ubuntu"
    if [ -f /etc/os-release ]; then
        source /etc/os-release
        if [ "$ID" != "ubuntu" ] || [ "$VERSION_ID" != "24.04" ]; then
            echo -e "${RED}ERROR: Unsupported OS (requires Ubuntu 24.04 LTS)${NC}"
            exit 1
        fi
    fi
else
    echo -e "${RED}ERROR: Unsupported operating system${NC}"
    exit 1
fi

# ==============================================================================
# Prerequisites Check
# ==============================================================================
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Python Venv Setup for WhisperX${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

echo -e "${YELLOW}Checking prerequisites...${NC}"

# Check python3-venv is available
if ! python3 -m venv --help &>/dev/null; then
    echo -e "${RED}ERROR: python3-venv not installed${NC}"
    echo "Run install_packages.sh first (requires sudo)"
    exit 1
fi

# Check ffmpeg
if ! command -v ffmpeg &>/dev/null; then
    echo -e "${RED}ERROR: ffmpeg not installed${NC}"
    echo "Run install_packages.sh first (requires sudo)"
    exit 1
fi

echo -e "${GREEN}✓ Prerequisites OK${NC}"
echo ""

# ==============================================================================
# GPU Mode Info
# ==============================================================================
show_mode_info() {
    local mode=$1
    case $mode in
        nvidia)
            echo -e "${BLUE}Mode: NVIDIA (CUDA)${NC}"
            echo "Will create: venv-nvidia"
            echo "PyTorch: 2.9.1+cu130"
            if command -v nvidia-smi &> /dev/null && nvidia-smi &> /dev/null; then
                GPU_NAME=$(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo "NVIDIA GPU")
                echo -e "${GREEN}✓ Detected: $GPU_NAME${NC}"
            else
                echo -e "${YELLOW}⚠ No NVIDIA GPU currently detected (eGPU may be disconnected)${NC}"
            fi
            ;;
        amd)
            echo -e "${BLUE}Mode: AMD (ROCm)${NC}"
            echo "Will create: venv-amd"
            echo "PyTorch: 2.6.0+rocm6.2"
            if command -v rocminfo &> /dev/null; then
                echo -e "${GREEN}✓ ROCm tools available${NC}"
            else
                echo -e "${YELLOW}⚠ ROCm not detected (run install_amd_drivers.sh first)${NC}"
            fi
            ;;
        intel)
            echo -e "${BLUE}Mode: Intel (XPU)${NC}"
            echo "Will create: venv-intel"
            echo "PyTorch: 2.5.1 + IPEX 2.5.10+xpu"
            if [ -f /usr/lib/x86_64-linux-gnu/libze_loader.so.1 ]; then
                echo -e "${GREEN}✓ Level Zero available${NC}"
            else
                echo -e "${YELLOW}⚠ Intel XPU runtime not detected (run install_intel_drivers.sh first)${NC}"
            fi
            ;;
        cpu)
            echo -e "${BLUE}Mode: CPU-only${NC}"
            echo "Will create: venv-cpu"
            echo "PyTorch: 2.9.1 (CPU)"
            echo "No GPU acceleration - fallback mode"
            ;;
    esac
}

if [ "$OS_TYPE" = "macos" ]; then
    if [ "$GPU_MODE" != "cpu" ] && [ "$INSTALL_ALL" = false ]; then
        echo -e "${YELLOW}⚠ macOS only supports CPU mode (with MPS acceleration)${NC}"
        GPU_MODE="cpu"
    fi
fi

if [ "$INSTALL_ALL" = true ]; then
    echo "Will create all venvs: venv-nvidia, venv-amd, venv-intel, venv-cpu"
    MODES_TO_INSTALL="nvidia amd intel cpu"
else
    show_mode_info "$GPU_MODE"
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
    echo ""
    echo "GPU benchmark dependencies:"
    echo "  - glmark2: OpenGL benchmark"
    echo "  - meson/ninja-build: Build system (for building vkmark from source)"
    echo "  - libvulkan-dev: Vulkan development headers"
    echo "  - libassimp-dev/libglm-dev: 3D model and math libraries"
    echo "  Note: vkpeak binary is included in gpu_benchmarks/bin/"

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
      python3-venv \
      glmark2 \
      meson \
      ninja-build \
      libvulkan-dev \
      libwayland-dev \
      libxcb1-dev \
      libxcb-icccm4-dev \
      libdrm-dev \
      libassimp-dev \
      libglm-dev

    echo -e "${GREEN}✓ System dependencies installed${NC}"
fi
echo ""

# ==============================================================================
# Determine which modes to install
# ==============================================================================
if [ "$INSTALL_ALL" = true ]; then
    MODES_TO_INSTALL="nvidia amd intel cpu"
    echo -e "${BLUE}Installing all GPU backends...${NC}"
else
    MODES_TO_INSTALL="$GPU_MODE"
fi
echo ""

# ==============================================================================
# Main Installation Loop
# ==============================================================================
for CURRENT_MODE in $MODES_TO_INSTALL; do

echo ""
echo -e "${BLUE}======================================================${NC}"
echo -e "${BLUE}Installing for: $CURRENT_MODE${NC}"
echo -e "${BLUE}======================================================${NC}"
echo ""

set_venv_dir "$CURRENT_MODE"

# ==============================================================================
# Step 1: Create Virtual Environment
# ==============================================================================
echo -e "${YELLOW}[1/10] Creating Python virtual environment...${NC}"
echo "Location: $VENV_DIR"
if [ -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Warning: venv directory already exists. Removing...${NC}"
    if ! rm -rf "$VENV_DIR" 2>/dev/null; then
        echo -e "${RED}ERROR: Cannot remove existing venv (permission denied)${NC}"
        echo "Try: rm -rf $VENV_DIR"
        exit 1
    fi
fi
python3 -m venv "$VENV_DIR"
echo -e "${GREEN}✓ Virtual environment created${NC}"
echo ""

source "$VENV_DIR/bin/activate"

# ==============================================================================
# Step 2: Install Base Packages
# ==============================================================================
echo -e "${YELLOW}[2/10] Installing base packages...${NC}"
echo "Installing WhisperX, AI provider SDKs, and dependencies from requirements.txt"
echo "Note: WhisperX will pull PyTorch 2.8.0 (we'll upgrade next)"
echo "This may take 5-10 minutes..."
pip install -r "$PROJECT_DIR/requirements.txt"
echo -e "${GREEN}✓ Base packages installed${NC}"
echo ""

# ==============================================================================
# Step 3: PyTorch Installation for Selected Backend
# ==============================================================================
echo -e "${YELLOW}[3/10] Installing PyTorch for $CURRENT_MODE backend...${NC}"
echo "This may take 2-5 minutes depending on internet speed..."

case $CURRENT_MODE in
    nvidia)
        echo "Installing PyTorch 2.9.1 with CUDA 13.0 support"
        pip install --force-reinstall --index-url https://download.pytorch.org/whl/cu130 \
            torch==2.9.1 \
            torchvision==0.24.1 \
            torchaudio==2.9.1

        # CTranslate2 (faster-whisper/WhisperX dependency) dynamically links against
        # libcublas.so.12. PyTorch 2.9.1+cu130 bundles CUDA 13 internally but doesn't
        # expose cublas12 on LD_LIBRARY_PATH. We need system CUDA 12 libs
        # (installed by install_nvidia_drivers.sh) or a fallback path.
        #
        # Add activation hook so LD_LIBRARY_PATH includes CUDA 12 lib dirs automatically.
        ACTIVATE_HOOK="$VENV_DIR/etc/conda/activate.d"  # reuse conda convention
        mkdir -p "$ACTIVATE_HOOK"
        cat > "$VENV_DIR/bin/activate_cuda.sh" << 'CUDA_HOOK_EOF'
# CUDA 12 library path for CTranslate2/faster-whisper
# Sourced automatically by setup_env.sh or manually before whisperx runs
CUDA12_PATHS=(
    "/usr/lib/x86_64-linux-gnu"           # System CUDA packages (libcublas-12-*)
    "/usr/local/cuda-12/lib64"            # CUDA toolkit default install
    "/usr/local/lib/ollama/cuda_v12"      # Ollama bundled CUDA 12
)
for _p in "${CUDA12_PATHS[@]}"; do
    if [ -d "$_p" ] && [[ ":$LD_LIBRARY_PATH:" != *":$_p:"* ]]; then
        if ls "$_p"/libcublas.so.12* &>/dev/null; then
            export LD_LIBRARY_PATH="$_p${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
            break
        fi
    fi
done
unset _p CUDA12_PATHS
CUDA_HOOK_EOF
        echo -e "${GREEN}✓ PyTorch 2.9.1+cu130 installed${NC}"
        echo -e "${GREEN}✓ CUDA 12 activation hook created at $VENV_DIR/bin/activate_cuda.sh${NC}"
        ;;
    amd)
        echo "Installing PyTorch 2.6.0 with ROCm 6.2 support"
        pip install --force-reinstall --index-url https://download.pytorch.org/whl/rocm6.2 \
            torch==2.6.0 \
            torchvision==0.21.0 \
            torchaudio==2.6.0
        echo -e "${GREEN}✓ PyTorch 2.6.0+rocm6.2 installed${NC}"
        ;;
    intel)
        echo "Installing PyTorch 2.5.1 with Intel XPU support (IPEX)"
        pip install --force-reinstall \
            torch==2.5.1 \
            torchvision \
            torchaudio \
            intel-extension-for-pytorch==2.5.10+xpu \
            --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/
        echo -e "${GREEN}✓ PyTorch 2.5.1 + IPEX 2.5.10+xpu installed${NC}"
        ;;
    cpu)
        if [ "$OS_TYPE" = "macos" ]; then
            echo "Installing PyTorch 2.9.1 with MPS (Metal) support"
            pip install --force-reinstall \
                torch==2.9.1 \
                torchaudio==2.9.1
            echo -e "${GREEN}✓ PyTorch 2.9.1 (MPS) installed${NC}"
        else
            echo "Installing PyTorch 2.9.1 CPU-only"
            pip install --force-reinstall --index-url https://download.pytorch.org/whl/cpu \
                torch==2.9.1 \
                torchvision==0.24.1 \
                torchaudio==2.9.1
            echo -e "${GREEN}✓ PyTorch 2.9.1+cpu installed${NC}"
        fi
        ;;
esac
echo ""

# ==============================================================================
# Step 4: PyTorch Verification
# ==============================================================================
echo -e "${YELLOW}[4/10] Verifying PyTorch installation...${NC}"

case $CURRENT_MODE in
    nvidia)
        python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"No GPU detected\"}')"
        if python3 -c "import torch; exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
            python3 -c "import torch; x = torch.randn(100,100, device='cuda'); print('✓ GPU test passed:', x.matmul(x).sum().item())"
            python3 -c "import torch.backends.cudnn as cudnn; print('✓ cuDNN version:', cudnn.version()); print('✓ cuDNN enabled:', cudnn.is_available())"
            echo -e "${GREEN}✓ PyTorch verified - NVIDIA GPU ready${NC}"
        else
            echo -e "${YELLOW}⚠ No NVIDIA GPU currently detected (eGPU may be disconnected)${NC}"
        fi
        ;;
    amd)
        python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'ROCm available: {torch.cuda.is_available()}'); print(f'HIP version: {torch.version.hip if hasattr(torch.version, \"hip\") else \"N/A\"}')"
        if python3 -c "import torch; exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
            python3 -c "import torch; x = torch.randn(100,100, device='cuda'); print('✓ GPU test passed:', x.matmul(x).sum().item())"
            echo -e "${GREEN}✓ PyTorch verified - AMD GPU ready${NC}"
        else
            echo -e "${YELLOW}⚠ No AMD GPU currently detected${NC}"
        fi
        ;;
    intel)
        python3 -c "import torch; import intel_extension_for_pytorch as ipex; print(f'PyTorch: {torch.__version__}'); print(f'IPEX: {ipex.__version__}'); print(f'XPU available: {torch.xpu.is_available()}')" 2>/dev/null || \
        python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print('IPEX import failed')"
        if python3 -c "import torch; import intel_extension_for_pytorch; exit(0 if torch.xpu.is_available() else 1)" 2>/dev/null; then
            python3 -c "import torch; import intel_extension_for_pytorch; x = torch.randn(100,100, device='xpu'); print('✓ XPU test passed:', x.sum().item())"
            echo -e "${GREEN}✓ PyTorch verified - Intel XPU ready${NC}"
        else
            echo -e "${YELLOW}⚠ Intel XPU not available${NC}"
        fi
        ;;
    cpu)
        python3 -c "import torch; print(f'PyTorch: {torch.__version__}')"
        python3 -c "import torch; x = torch.randn(100,100); print('✓ CPU test passed:', x.matmul(x).sum().item())"
        if [ "$OS_TYPE" = "macos" ]; then
            python3 -c "import torch; print('✓ MPS available:', torch.backends.mps.is_available() if hasattr(torch.backends, 'mps') else False)"
        fi
        echo -e "${GREEN}✓ PyTorch verified - CPU ready${NC}"
        ;;
esac
echo ""

# ==============================================================================
# Step 5: WhisperX Compatibility Patches
# ==============================================================================
echo -e "${YELLOW}[5/10] Applying WhisperX patches...${NC}"
echo "Updating WhisperX to use 'token' parameter for HuggingFace authentication"

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

if [ "$OS_TYPE" = "macos" ]; then
    sed -i '' 's/use_auth_token/token/g' "$WHISPERX_VADS"
    sed -i '' '412s/use_auth_token=None/token=None/' "$WHISPERX_ASR"
else
    sed -i 's/use_auth_token/token/g' "$WHISPERX_VADS"
    sed -i '412s/use_auth_token=None/token=None/' "$WHISPERX_ASR"
fi

VADS_COUNT=$(grep -c "use_auth_token" "$WHISPERX_VADS" || true)
if [ "$VADS_COUNT" -ne 0 ]; then
    echo -e "${RED}ERROR: Patch verification failed for vads/pyannote.py${NC}"
    exit 1
fi

echo -e "${GREEN}✓ WhisperX patches applied${NC}"
echo ""

# ==============================================================================
# Step 6: pyannote.audio Installation
# ==============================================================================
echo -e "${YELLOW}[6/10] Installing pyannote.audio 4.0.1...${NC}"
pip install --upgrade "pyannote.audio==4.0.1"
echo -e "${GREEN}✓ pyannote.audio 4.0.1 installed${NC}"
echo ""

# ==============================================================================
# Step 7: SpeechBrain Compatibility Patches
# ==============================================================================
echo -e "${YELLOW}[7/10] Applying SpeechBrain compatibility patches...${NC}"

SPEECHBRAIN_BACKEND="$SITE_PACKAGES/speechbrain/utils/torch_audio_backend.py"

if [ ! -f "$SPEECHBRAIN_BACKEND" ]; then
    echo -e "${RED}ERROR: SpeechBrain torch_audio_backend.py not found${NC}"
    exit 1
fi

cat > /tmp/speechbrain_patch.py << 'PATCH_EOF'
import sys

with open(sys.argv[1], 'r') as f:
    content = f.read()

if 'hasattr(torchaudio, \'list_audio_backends\')' in content:
    print("Already patched")
    sys.exit(0)

original = """    elif torchaudio_major >= 2 and torchaudio_minor >= 1:
        available_backends = torchaudio.list_audio_backends()

        if len(available_backends) == 0:
            logger.warning(
                "SpeechBrain could not find any working torchaudio backend. Audio files may fail to load. Follow this link for instructions and troubleshooting: https://speechbrain.readthedocs.io/en/latest/audioloading.html"
            )"""

replacement = """    elif torchaudio_major >= 2 and torchaudio_minor >= 1:
        # list_audio_backends() is not available in torchaudio 2.9.1
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
    if 'hasattr(torchaudio, \'list_audio_backends\')' in content:
        print("Already patched")
    else:
        print("ERROR: Could not find pattern to patch")
        sys.exit(1)
PATCH_EOF

python3 /tmp/speechbrain_patch.py "$SPEECHBRAIN_BACKEND"
rm -f /tmp/speechbrain_patch.py

# SpeechBrain dataio.py patch
echo "Patching SpeechBrain dataio.py for torchaudio 2.9.x..."

SPEECHBRAIN_DATAIO="$SITE_PACKAGES/speechbrain/dataio/dataio.py"

if [ ! -f "$SPEECHBRAIN_DATAIO" ]; then
    echo -e "${RED}ERROR: SpeechBrain dataio.py not found${NC}"
    exit 1
fi

cat > /tmp/speechbrain_dataio_patch.py << 'PATCH_EOF'
import sys

filepath = sys.argv[1]

with open(filepath, 'r') as f:
    content = f.read()

if 'AudioMetaDataCompat' in content:
    print("Already patched")
    sys.exit(0)

compat_class = '''
# Compatibility shim for torchaudio 2.9.x which removed AudioMetaData
class AudioMetaDataCompat:
    """Compatibility class replacing torchaudio.backend.common.AudioMetaData."""
    def __init__(self, sample_rate, num_frames, num_channels, bits_per_sample=16, encoding="PCM_S"):
        self.sample_rate = sample_rate
        self.num_frames = num_frames
        self.num_channels = num_channels
        self.bits_per_sample = bits_per_sample
        self.encoding = encoding

'''

marker = "\ndef read_audio_info("
if marker not in content:
    print("ERROR: Could not find read_audio_info function")
    sys.exit(1)

content = content.replace(marker, compat_class + marker)

old_func_start = "def read_audio_info(\n    path, backend=None\n) -> \"torchaudio.backend.common.AudioMetaData\":"
new_func_start = "def read_audio_info(\n    path, backend=None\n) -> AudioMetaDataCompat:"

if old_func_start in content:
    content = content.replace(old_func_start, new_func_start)

old_body = '''    validate_backend(backend)

    _path_no_ext, path_ext = os.path.splitext(path)

    if path_ext == ".mp3":
        # Additionally, certain affected versions of torchaudio fail to
        # autodetect mp3.
        # HACK: here, we check for the file extension to force mp3 detection,
        # which prevents an error from occurring in torchaudio.
        info = torchaudio.info(path, format="mp3", backend=backend)
    else:
        info = torchaudio.info(path, backend=backend)

    # Certain file formats, such as MP3, do not provide a reliable way to
    # query file duration from metadata (when there is any).
    # For MP3, certain versions of torchaudio began returning num_frames == 0.
    #
    # https://github.com/speechbrain/speechbrain/issues/1925
    # https://github.com/pytorch/audio/issues/2524
    #
    # Accommodate for these cases here: if `num_frames == 0` then maybe something
    # has gone wrong.
    # If some file really had `num_frames == 0` then we are not doing harm
    # double-checking anyway. If I am wrong and you are reading this comment
    # because of it: sorry
    if info.num_frames == 0:
        channels_data, sample_rate = torchaudio.load(
            path, normalize=False, backend=backend
        )

        info.num_frames = channels_data.size(1)
        info.sample_rate = sample_rate  # because we might as well

    return info'''

new_body = '''    # torchaudio 2.9.x compatibility: use torchaudio.load() instead of removed torchaudio.info()
    if hasattr(torchaudio, 'info'):
        # Old torchaudio version - use original approach
        validate_backend(backend)
        _path_no_ext, path_ext = os.path.splitext(path)
        if path_ext == ".mp3":
            info = torchaudio.info(path, format="mp3", backend=backend)
        else:
            info = torchaudio.info(path, backend=backend)
        if info.num_frames == 0:
            channels_data, sample_rate = torchaudio.load(path, normalize=False, backend=backend)
            info.num_frames = channels_data.size(1)
            info.sample_rate = sample_rate
        return info
    else:
        # torchaudio 2.9.x: info() removed, use load() to get metadata
        # Note: backend parameter is ignored in torchaudio 2.9.x
        channels_data, sample_rate = torchaudio.load(path, normalize=False)
        return AudioMetaDataCompat(
            sample_rate=sample_rate,
            num_frames=channels_data.size(1),
            num_channels=channels_data.size(0),
        )'''

if old_body in content:
    content = content.replace(old_body, new_body)
    with open(filepath, 'w') as f:
        f.write(content)
    print("Patch applied successfully")
else:
    with open(filepath, 'w') as f:
        f.write(content)
    print("Partial patch applied (compat class added)")
PATCH_EOF

python3 /tmp/speechbrain_dataio_patch.py "$SPEECHBRAIN_DATAIO"
rm -f /tmp/speechbrain_dataio_patch.py

echo -e "${GREEN}✓ SpeechBrain patches applied${NC}"
echo ""

# ==============================================================================
# Step 8: Lightning Patch for PyTorch 2.6+ weights_only
# ==============================================================================
echo -e "${YELLOW}[8/10] Applying Lightning patch for PyTorch 2.6+...${NC}"

LIGHTNING_CLOUD_IO="$SITE_PACKAGES/lightning/fabric/utilities/cloud_io.py"

if [ ! -f "$LIGHTNING_CLOUD_IO" ]; then
    echo -e "${RED}ERROR: Lightning cloud_io.py not found${NC}"
    exit 1
fi

if grep -q "PyTorch 2.6+ compatibility patch" "$LIGHTNING_CLOUD_IO"; then
    echo "Already patched"
else
    sed -i 's/fs.open(path_or_url, "rb") as f:/fs.open(path_or_url, "rb") as f:\n        if weights_only is None:\n            weights_only = False  # PyTorch 2.6+ compatibility patch/' "$LIGHTNING_CLOUD_IO"
    if grep -q "PyTorch 2.6+ compatibility patch" "$LIGHTNING_CLOUD_IO"; then
        echo -e "${GREEN}✓ Lightning patch applied${NC}"
    else
        echo -e "${RED}ERROR: Lightning patch verification failed${NC}"
        exit 1
    fi
fi
echo ""

# ==============================================================================
# Step 9: pyannote.audio torchcodec Fallback Patch
# ==============================================================================
echo -e "${YELLOW}[9/10] Applying pyannote.audio torchcodec fallback patch...${NC}"

PYANNOTE_IO="$SITE_PACKAGES/pyannote/audio/core/io.py"

if [ ! -f "$PYANNOTE_IO" ]; then
    echo -e "${RED}ERROR: pyannote io.py not found${NC}"
    exit 1
fi

if grep -q "SoundfileFallbackDecoder" "$PYANNOTE_IO"; then
    echo "Already patched"
else
    cat > /tmp/pyannote_io_patch.py << 'PATCH_EOF'
import sys

filepath = sys.argv[1]

with open(filepath, 'r') as f:
    content = f.read()

if 'SoundfileFallbackDecoder' in content:
    print("Already patched")
    sys.exit(0)

old_import_block = '''try:
    import torchcodec
    from torchcodec import AudioSamples
    from torchcodec.decoders import AudioDecoder, AudioStreamMetadata
except Exception as e:
    warnings.warn(
        "\\ntorchcodec is not installed correctly so built-in audio decoding will fail. Solutions are:\\n"
        "* use audio preloaded in-memory as a {'waveform': (channel, time) torch.Tensor, 'sample_rate': int} dictionary;\\n"
        "* fix torchcodec installation. Error message was:\\n\\n"
        f"{e}"
    )'''

new_import_block = '''try:
    import torchcodec
    from torchcodec import AudioSamples
    from torchcodec.decoders import AudioDecoder, AudioStreamMetadata
    _TORCHCODEC_AVAILABLE = True
except Exception as e:
    _TORCHCODEC_AVAILABLE = False
    # Fallback classes using soundfile when torchcodec is not available
    import soundfile as sf
    import torch
    from dataclasses import dataclass

    @dataclass
    class AudioStreamMetadata:
        """Fallback metadata class matching torchcodec.decoders.AudioStreamMetadata interface."""
        sample_rate: int
        duration_seconds_from_header: float
        num_frames: int = 0
        num_channels: int = 1

    @dataclass
    class AudioSamples:
        """Fallback AudioSamples class matching torchcodec.AudioSamples interface."""
        data: "Tensor"  # (channel, time)
        sample_rate: int

    class SoundfileFallbackDecoder:
        """Fallback AudioDecoder using soundfile when torchcodec is unavailable."""

        def __init__(self, source):
            self._source = source
            self._waveform = None
            self._sample_rate = None
            self._loaded = False

        def _ensure_loaded(self):
            if not self._loaded:
                import numpy as np
                try:
                    data, sr = sf.read(self._source, dtype='float32')
                    waveform = torch.from_numpy(data)
                    if waveform.ndim == 1:
                        waveform = waveform.unsqueeze(0)
                    else:
                        waveform = waveform.T
                    self._waveform = waveform
                    self._sample_rate = sr
                except Exception as sf_error:
                    import subprocess
                    source_path = str(self._source)
                    cmd = ['ffmpeg', '-i', source_path, '-f', 'f32le', '-acodec', 'pcm_f32le',
                           '-ar', '16000', '-ac', '1', '-loglevel', 'error', '-']
                    result = subprocess.run(cmd, capture_output=True)
                    if result.returncode != 0:
                        raise RuntimeError(f"soundfile failed: {sf_error}; ffmpeg failed: {result.stderr.decode()}")
                    samples = np.frombuffer(result.stdout, dtype=np.float32)
                    self._waveform = torch.from_numpy(samples).unsqueeze(0)
                    self._sample_rate = 16000
                self._loaded = True
                if hasattr(self._source, 'seek'):
                    self._source.seek(0)

        @property
        def metadata(self) -> AudioStreamMetadata:
            self._ensure_loaded()
            num_channels, num_frames = self._waveform.shape
            return AudioStreamMetadata(
                sample_rate=self._sample_rate,
                duration_seconds_from_header=num_frames / self._sample_rate,
                num_frames=num_frames, num_channels=num_channels)

        def get_all_samples(self) -> AudioSamples:
            self._ensure_loaded()
            return AudioSamples(data=self._waveform, sample_rate=self._sample_rate)

        def get_samples_played_in_range(self, start: float, end: float) -> AudioSamples:
            self._ensure_loaded()
            start_sample = max(0, int(start * self._sample_rate))
            end_sample = min(self._waveform.shape[1], int(end * self._sample_rate))
            return AudioSamples(data=self._waveform[:, start_sample:end_sample], sample_rate=self._sample_rate)

    AudioDecoder = SoundfileFallbackDecoder'''

if old_import_block in content:
    content = content.replace(old_import_block, new_import_block)
    with open(filepath, 'w') as f:
        f.write(content)
    print("Patch applied successfully")
else:
    print("ERROR: Could not find expected import block to patch")
    sys.exit(1)
PATCH_EOF

    python3 /tmp/pyannote_io_patch.py "$PYANNOTE_IO"
    rm -f /tmp/pyannote_io_patch.py

    if grep -q "SoundfileFallbackDecoder" "$PYANNOTE_IO"; then
        echo -e "${GREEN}✓ pyannote.audio torchcodec fallback patch applied${NC}"
    else
        echo -e "${RED}ERROR: pyannote.audio patch verification failed${NC}"
        exit 1
    fi
fi

# Uninstall torchcodec (ABI incompatible)
echo "Removing torchcodec (ABI incompatible with PyTorch 2.9.1)..."
if pip show torchcodec &>/dev/null; then
    pip uninstall torchcodec -y
    echo -e "${GREEN}✓ torchcodec uninstalled (using soundfile fallback)${NC}"
else
    echo "torchcodec not installed - skipping"
fi
echo ""

# ==============================================================================
# Step 10: Verify and Finalize
# ==============================================================================
echo -e "${YELLOW}[10/10] Verifying package installations...${NC}"

echo "Testing WhisperX import..."
python3 -c "import whisperx; print('✓ WhisperX imported successfully')"

echo "Testing pyannote.audio import..."
python3 -c "from pyannote.audio import Pipeline; print('✓ pyannote.audio imported successfully')"

echo "Testing AI provider SDKs..."
python3 -c "import assemblyai; print('✓ assemblyai')"
python3 -c "import anthropic; print('✓ anthropic')"
python3 -c "import google.generativeai; print('✓ google-generativeai')"
python3 -c "import requests; print('✓ requests')"

echo -e "${GREEN}✓ All packages verified${NC}"
echo ""

# Create project directories
mkdir -p "$PROJECT_DIR/intermediates"
mkdir -p "$PROJECT_DIR/outputs"

# Setup env file
if [ ! -f "$PROJECT_DIR/setup_env.sh" ]; then
    if [ -f "$PROJECT_DIR/setup_env.sh.example" ]; then
        cp "$PROJECT_DIR/setup_env.sh.example" "$PROJECT_DIR/setup_env.sh"
        echo -e "${GREEN}✓ Created setup_env.sh from template${NC}"
    fi
fi

echo -e "${GREEN}✓ Completed installation for: $CURRENT_MODE${NC}"
echo ""

done  # End of main installation loop

# ==============================================================================
# Final Summary
# ==============================================================================
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✓ All Installations Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

echo -e "${BLUE}Installed venvs:${NC}"
for mode in $MODES_TO_INSTALL; do
    case $mode in
        nvidia) echo "  venv-nvidia/  - NVIDIA GPU (CUDA)" ;;
        amd)    echo "  venv-amd/     - AMD GPU (ROCm)" ;;
        intel)  echo "  venv-intel/   - Intel GPU (XPU)" ;;
        cpu)    echo "  venv-cpu/     - CPU-only fallback" ;;
    esac
done
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
echo -e "${GREEN}Ready to use!${NC}"
echo ""
echo "Usage:"
echo "  source setup_env.sh"
echo "  source venv-nvidia/bin/activate   # NVIDIA GPU"
echo "  source venv-amd/bin/activate      # AMD GPU"
echo "  source venv-intel/bin/activate    # Intel iGPU"
echo "  source venv-cpu/bin/activate      # CPU fallback"
echo ""
echo "Then run:"
echo "  ./scripts/process_single.sh audio.mp3 --transcribers whisperx --processors opus"
