#!/bin/bash
# ==============================================================================
# NVIDIA Driver & CUDA Runtime Installation
# ==============================================================================
#
# This script installs NVIDIA drivers and CUDA runtime libraries on Ubuntu 24.04 LTS.
# Works with any NVIDIA GPU (RTX 3090, 4090, 5070, etc.).
#
# Usage:
#   sudo ./scripts/install_nvidia_drivers.sh
#   sudo reboot
#
# ==============================================================================

set -euo pipefail

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

if [ "$#" -ne 0 ]; then
    echo -e "${RED}ERROR: This script does not accept arguments${NC}"
    echo "Usage:"
    echo "  sudo ./scripts/install_nvidia_drivers.sh"
    exit 1
fi

CURRENT_KERNEL=$(uname -r)
TOTAL_STEPS=5
step=1

# Fail early on systems without NVIDIA hardware.
if ! lspci | grep -iE "vga|3d|display" | grep -qi nvidia; then
    echo -e "${RED}ERROR: No NVIDIA GPU detected on the PCI bus${NC}"
    exit 1
fi

# Step 1: Refresh package indexes
echo -e "${YELLOW}[${step}/${TOTAL_STEPS}] Updating package indexes...${NC}"
apt update
echo -e "${GREEN}✓ Package indexes updated${NC}"
echo ""
step=$((step + 1))

# Step 2: Install NVIDIA driver
echo -e "${YELLOW}[${step}/${TOTAL_STEPS}] Installing NVIDIA driver from Ubuntu packages...${NC}"
echo "This will automatically detect your GPU and install the latest compatible Ubuntu driver."
ubuntu-drivers install
echo -e "${GREEN}✓ NVIDIA driver packages installed${NC}"
echo ""
step=$((step + 1))

# Step 3: Verify current kernel has a matching NVIDIA module
echo -e "${YELLOW}[${step}/${TOTAL_STEPS}] Verifying NVIDIA module for current kernel...${NC}"
echo "Current kernel: $CURRENT_KERNEL"

if modinfo -k "$CURRENT_KERNEL" nvidia &> /dev/null; then
    echo -e "${GREEN}✓ NVIDIA kernel module is available for $CURRENT_KERNEL${NC}"
else
    echo -e "${RED}ERROR: No NVIDIA kernel module found for $CURRENT_KERNEL${NC}"
    echo ""
    echo "The driver packages were installed, but they do not match the currently"
    echo "running kernel. This usually means either:"
    echo "  - a newer kernel was installed and you need to reboot into it, or"
    echo "  - the NVIDIA module for $CURRENT_KERNEL was not installed/built."
    echo ""
    echo "Check these commands after rebooting or fixing the kernel packages:"
    echo "  uname -r"
    echo "  modinfo -k \$(uname -r) nvidia"
    echo ""
    exit 1
fi
echo ""
step=$((step + 1))

# Step 4: Install CUDA runtime libraries.
# PyTorch bundles its own CUDA, but CTranslate2/faster-whisper (used by WhisperX)
# dynamically link against system CUDA libraries at runtime.
echo -e "${YELLOW}[${step}/${TOTAL_STEPS}] Installing CUDA runtime libraries...${NC}"
echo "Ubuntu remains the source of truth for NVIDIA drivers; the CUDA repo is pinned"
echo "so it cannot override driver packages."

apt install -y wget

if ! dpkg -l cuda-keyring 2>/dev/null | grep -q "^ii"; then
    echo "Adding NVIDIA CUDA repository keyring..."
    wget -q https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb -O /tmp/cuda-keyring.deb
    dpkg -i /tmp/cuda-keyring.deb
    rm -f /tmp/cuda-keyring.deb
fi

cat > /etc/apt/preferences.d/cuda-runtime-no-driver-overrides <<'EOF'
Package: nvidia-* libnvidia-* linux-modules-nvidia-* xserver-xorg-video-nvidia-* cuda-drivers* nvidia-firmware-* nvidia-kernel-*
Pin: origin developer.download.nvidia.com
Pin-Priority: -1
EOF

apt update

# Minimal CUDA runtime libraries needed by WhisperX/CTranslate2.
apt install -y libcublas-12-8 libcurand-12-8 libcusparse-12-8 libcusolver-12-8
echo -e "${GREEN}✓ CUDA runtime libraries installed without overriding driver packages${NC}"
echo ""
step=$((step + 1))

# Step 5: Check current nvidia-smi status (may not work until reboot)
echo -e "${YELLOW}[${step}/${TOTAL_STEPS}] Checking current driver status...${NC}"
if command -v nvidia-smi &> /dev/null; then
    echo "nvidia-smi command is available."
    if nvidia-smi &> /dev/null; then
        echo -e "${GREEN}Driver is already loaded:${NC}"
        nvidia-smi
    else
        echo -e "${YELLOW}Driver installed for the current kernel, but not loaded yet (reboot required)${NC}"
    fi
else
    echo -e "${YELLOW}nvidia-smi will be available after reboot${NC}"
fi
echo ""

# Final instructions
echo -e "${BLUE}=================================${NC}"
echo -e "${GREEN}✓ Installation Complete!${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""
echo -e "${YELLOW}IMPORTANT: You MUST reboot for the driver to work.${NC}"
echo ""
echo "After reboot, verify the installation with:"
echo "  uname -r"
echo "  modinfo -k \$(uname -r) nvidia"
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
echo "  ./scripts/install_packages.sh"
echo "  ./scripts/install_venv.sh --nvidia"
echo ""
