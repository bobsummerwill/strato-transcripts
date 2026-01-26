#!/bin/bash
# ==============================================================================
# AMD ROCm Driver Installation Script
# ==============================================================================
#
# This script installs AMD ROCm drivers on Ubuntu 24.04 LTS for AMD GPUs.
# Supports both official ROCm GPUs (RX 7000 series, MI series) and unofficial
# GPUs (RX 6000 series) with HSA override.
#
# Tested with: RX 6750 XT (Navi 22) in Razer Core X eGPU enclosure
#
# Usage:
#   sudo ./install_amd_drivers.sh
#   sudo reboot
#
# Post-reboot for unofficial GPUs (RX 6600/6700/6750 XT):
#   export HSA_OVERRIDE_GFX_VERSION=10.3.0
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
echo -e "${BLUE}AMD ROCm Driver Installation${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}ERROR: This script must be run as root (use sudo)${NC}"
    exit 1
fi

# Get the actual user (not root)
ACTUAL_USER=${SUDO_USER:-$USER}

# Step 1: Update system packages
echo -e "${YELLOW}[1/6] Updating system packages...${NC}"
# Remove any existing ROCm repo to avoid stale config issues during apt update
rm -f /etc/apt/sources.list.d/rocm.list 2>/dev/null || true
apt update
apt upgrade -y
echo -e "${GREEN}Done${NC}"
echo ""

# Step 2: Install prerequisites
echo -e "${YELLOW}[2/6] Installing prerequisites...${NC}"
apt install -y wget gnupg2
echo -e "${GREEN}Done${NC}"
echo ""

# Step 3: Add AMD ROCm repository
echo -e "${YELLOW}[3/6] Adding AMD ROCm repository...${NC}"

# Download and install AMD GPG key
mkdir -p /etc/apt/keyrings
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | gpg --dearmor > /etc/apt/keyrings/rocm.gpg

# Detect Ubuntu version
UBUNTU_CODENAME=$(lsb_release -cs)
echo "Detected Ubuntu: $UBUNTU_CODENAME"

# Add ROCm repository (using pinned version for stability)
# Using 6.2.4 which matches PyTorch rocm6.2 wheel
ROCM_VERSION="6.2.4"
cat > /etc/apt/sources.list.d/rocm.list << EOF
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/$ROCM_VERSION $UBUNTU_CODENAME main
EOF
echo "Using ROCm version: $ROCM_VERSION"

# Set repository priority
cat > /etc/apt/preferences.d/rocm-pin-600 << EOF
Package: *
Pin: release o=repo.radeon.com
Pin-Priority: 600
EOF

apt update
echo -e "${GREEN}Done${NC}"
echo ""

# Step 4: Install ROCm packages
echo -e "${YELLOW}[4/6] Installing ROCm packages...${NC}"
echo "This may take several minutes..."

# Install AMDGPU kernel driver and minimal ROCm runtime
# Note: PyTorch ROCm wheels include their own runtime libraries,
# so we only need the kernel driver and HSA runtime
apt install -y amdgpu-dkms

# Install ROCm SMI for monitoring (optional but useful)
apt install -y rocm-smi-lib || echo "rocm-smi-lib not available, skipping"

echo -e "${GREEN}Done${NC}"
echo ""

# Step 5: Add user to required groups
echo -e "${YELLOW}[5/6] Adding user '$ACTUAL_USER' to video and render groups...${NC}"
usermod -aG video "$ACTUAL_USER"
usermod -aG render "$ACTUAL_USER"
echo -e "${GREEN}Done${NC}"
echo ""

# Step 6: Check for Secure Boot
echo -e "${YELLOW}[6/6] Checking Secure Boot status...${NC}"
if mokutil --sb-state 2>/dev/null | grep -q "SecureBoot enabled"; then
    echo -e "${YELLOW}WARNING: Secure Boot is ENABLED${NC}"
    echo ""
    echo "The amdgpu kernel module needs to be signed for Secure Boot."
    echo "During the DKMS installation, you should have been prompted to"
    echo "create a MOK (Machine Owner Key) password."
    echo ""
    echo "After reboot, the MOK Manager will appear:"
    echo "  1. Select 'Enroll MOK'"
    echo "  2. Select 'Continue'"
    echo "  3. Select 'Yes' to enroll the key"
    echo "  4. Enter the password you created during installation"
    echo "  5. Select 'Reboot'"
    echo ""
    echo "If the module fails to load after reboot, you may need to manually sign it:"
    echo "  See: https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot"
else
    echo -e "${GREEN}Secure Boot is disabled - no module signing required${NC}"
fi
echo ""

# Check current GPU status
echo -e "${BLUE}=================================${NC}"
echo -e "${BLUE}Current GPU Detection${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""

echo "Detected AMD GPUs:"
lspci | grep -i "vga\|3d\|display" | grep -i amd || echo "No AMD GPU detected on PCI bus"
echo ""

# Final instructions
echo -e "${BLUE}=================================${NC}"
echo -e "${GREEN}Installation Complete!${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""
echo -e "${YELLOW}IMPORTANT: You MUST reboot for the driver to work.${NC}"
echo ""
echo "After reboot, verify the installation with:"
echo "  rocminfo"
echo "  rocm-smi"
echo ""
echo -e "${YELLOW}For unofficial GPUs (RX 6600/6700/6750 XT - Navi 22/23):${NC}"
echo "Add this to your ~/.bashrc or run before using ROCm:"
echo ""
echo "  export HSA_OVERRIDE_GFX_VERSION=10.3.0"
echo ""
echo "This tells ROCm to treat your GPU as gfx1030 (officially supported)."
echo ""
echo -e "${YELLOW}To reboot now, run:${NC}"
echo "  sudo reboot"
echo ""
echo "After reboot, create a Python venv for ROCm:"
echo "  python3 -m venv venv-amd"
echo "  source venv-amd/bin/activate"
echo "  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2"
echo ""
