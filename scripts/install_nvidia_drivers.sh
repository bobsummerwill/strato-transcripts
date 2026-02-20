#!/bin/bash
# ==============================================================================
# NVIDIA Driver & CUDA Runtime Installation
# ==============================================================================
#
# This script installs NVIDIA drivers and CUDA runtime libraries on Ubuntu 24.04 LTS.
# Works with any NVIDIA GPU (RTX 3090, 4090, 5070, etc.).
#
# Usage:
#   sudo ./install_nvidia_drivers.sh
#   sudo reboot
#
# ==============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=================================${NC}"
echo -e "${BLUE}NVIDIA Driver Installation${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}ERROR: This script must be run as root (use sudo)${NC}"
    exit 1
fi

# Step 1: Update system packages
echo -e "${YELLOW}[1/4] Updating system packages...${NC}"
apt update
apt upgrade -y
echo -e "${GREEN}✓ System packages updated${NC}"
echo ""

# Step 2: Install NVIDIA driver
echo -e "${YELLOW}[2/5] Installing NVIDIA driver...${NC}"
echo "This will automatically detect your GPU and install the latest compatible driver."
ubuntu-drivers install
echo -e "${GREEN}✓ NVIDIA driver installed${NC}"
echo ""

# Step 3: Install CUDA runtime libraries
# PyTorch bundles its own CUDA, but CTranslate2/faster-whisper (used by WhisperX)
# dynamically links against system libcublas.so.12 at runtime.
# Without these, you get: RuntimeError: Library libcublas.so.12 is not found
echo -e "${YELLOW}[3/5] Installing CUDA 12 runtime libraries...${NC}"
echo "CTranslate2 (WhisperX dependency) requires system CUDA libraries."

# Add NVIDIA CUDA repository if not already present
if ! dpkg -l cuda-keyring 2>/dev/null | grep -q "^ii"; then
    echo "Adding NVIDIA CUDA repository..."
    wget -q https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb -O /tmp/cuda-keyring.deb
    dpkg -i /tmp/cuda-keyring.deb
    rm -f /tmp/cuda-keyring.deb
    apt update
fi

# Install CUDA 12 runtime libraries (not the full toolkit — just what's needed)
apt install -y libcublas-12-8 libcurand-12-8 libcusparse-12-8 libcusolver-12-8
echo -e "${GREEN}✓ CUDA 12 runtime libraries installed${NC}"
echo ""

# Step 4: Check current nvidia-smi status (may not work until reboot)
echo -e "${YELLOW}[4/5] Checking current driver status...${NC}"
if command -v nvidia-smi &> /dev/null; then
    echo "nvidia-smi command is available."
    if nvidia-smi &> /dev/null; then
        echo -e "${GREEN}Driver is already loaded:${NC}"
        nvidia-smi
    else
        echo -e "${YELLOW}Driver installed but not loaded yet (reboot required)${NC}"
    fi
else
    echo -e "${YELLOW}nvidia-smi will be available after reboot${NC}"
fi
echo ""

# Step 5: Final instructions
echo -e "${BLUE}=================================${NC}"
echo -e "${GREEN}✓ Installation Complete!${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""
echo -e "${YELLOW}IMPORTANT: You MUST reboot for the driver to work.${NC}"
echo ""
echo "After reboot, verify the installation with:"
echo "  nvidia-smi"
echo ""
echo "Expected output should show:"
echo "  - Driver Version and CUDA Version"
echo "  - Your GPU name(s)"
echo ""
echo -e "${YELLOW}To reboot now, run:${NC}"
echo "  sudo reboot"
echo ""
echo "After reboot, continue with:"
echo "  ./install_packages_and_venv.sh"
echo ""
