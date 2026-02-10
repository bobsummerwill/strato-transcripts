#!/bin/bash
# ==============================================================================
# System Package Installation Script
# ==============================================================================
#
# DESCRIPTION:
#   Installs system-level dependencies required by the WhisperX transcription
#   pipeline. These packages are the same regardless of GPU vendor.
#   Requires sudo on Ubuntu. Uses Homebrew on macOS.
#
# USAGE:
#   sudo ./scripts/install_packages.sh    # Ubuntu
#   ./scripts/install_packages.sh          # macOS (uses Homebrew)
#
# OPERATING SYSTEM SUPPORT:
#   - macOS Sonoma (14.x)
#   - Ubuntu 24.04 LTS
#
# See also: install_venv.sh (Python venv setup, no sudo required)
# ==============================================================================

set -e

# Terminal color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}System Package Installation${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ==============================================================================
# OS Detection and Validation
# ==============================================================================
echo -e "${YELLOW}[1/2] Detecting operating system...${NC}"

OS_TYPE=""

if [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macos"
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

    if ! command -v brew &> /dev/null; then
        echo -e "${RED}ERROR: Homebrew not installed${NC}"
        echo "Homebrew is required for macOS installations."
        echo "Install it from: https://brew.sh"
        exit 1
    fi
    echo -e "${GREEN}✓ Homebrew is installed${NC}"

elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="ubuntu"

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
# Install System Dependencies
# ==============================================================================
echo -e "${YELLOW}[2/2] Installing system dependencies...${NC}"

if [ "$OS_TYPE" = "macos" ]; then
    echo "Installing required packages via Homebrew:"
    echo "  - ffmpeg: Audio/video processing for WhisperX"
    echo "  - python@3.12: Python 3.12 interpreter"
    echo "  - git: Version control for installing packages from GitHub"

    brew list ffmpeg &>/dev/null || brew install ffmpeg
    brew list python@3.12 &>/dev/null || brew install python@3.12
    brew list git &>/dev/null || brew install git

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

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✓ System packages installed successfully${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Next step: Run install_venv.sh to create Python virtual environments"
echo "  ./scripts/install_venv.sh --nvidia   # NVIDIA GPU"
echo "  ./scripts/install_venv.sh --amd      # AMD GPU"
echo "  ./scripts/install_venv.sh --intel    # Intel GPU"
echo "  ./scripts/install_venv.sh --cpu      # CPU-only"
echo "  ./scripts/install_venv.sh --all      # All backends"
