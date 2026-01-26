#!/bin/bash
# ==============================================================================
# Intel GPU Driver Installation Script for XPU/oneAPI Support
# ==============================================================================
#
# This script installs Intel GPU compute drivers on Ubuntu 24.04 LTS.
# Enables PyTorch XPU support via Intel Extension for PyTorch (IPEX).
#
# Supports: Intel Arc GPUs, Intel Iris Xe, Intel UHD Graphics,
#           Meteor Lake, Raptor Lake, Alder Lake integrated graphics
#
# Tested with: Intel Meteor Lake-P [Intel Graphics] (integrated GPU)
#
# Usage:
#   sudo ./install_intel_drivers.sh
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
echo -e "${BLUE}Intel GPU Driver Installation${NC}"
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
# Remove any existing Intel GPU repo to avoid keyring conflicts during apt update
rm -f /etc/apt/sources.list.d/intel-gpu.list 2>/dev/null || true
rm -f /etc/apt/keyrings/intel-graphics.gpg 2>/dev/null || true
apt update
apt upgrade -y
echo -e "${GREEN}Done${NC}"
echo ""

# Step 2: Install prerequisites
echo -e "${YELLOW}[2/6] Installing prerequisites...${NC}"
apt install -y wget gnupg2 software-properties-common
echo -e "${GREEN}Done${NC}"
echo ""

# Step 3: Add Intel GPU repository
echo -e "${YELLOW}[3/6] Adding Intel GPU repository...${NC}"

# Download and install Intel GPG key
mkdir -p /etc/apt/keyrings
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | gpg --dearmor > /etc/apt/keyrings/intel-graphics.gpg

# Add Intel GPU repository
cat > /etc/apt/sources.list.d/intel-gpu.list << EOF
deb [arch=amd64 signed-by=/etc/apt/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu noble unified
EOF

apt update
echo -e "${GREEN}Done${NC}"
echo ""

# Step 4: Install Intel GPU compute packages
echo -e "${YELLOW}[4/6] Installing Intel GPU compute packages...${NC}"
echo "This may take several minutes..."

# Install Level Zero (GPU compute API)
apt install -y level-zero

# Install Intel compute runtime (OpenCL + Level Zero GPU driver)
# Note: libze-intel-gpu1 provides intel-level-zero-gpu and works with newer libigc2
apt install -y intel-opencl-icd libze-intel-gpu1

# Install oneAPI runtime libraries (for SYCL/DPC++ support)
apt install -y intel-oneapi-runtime-dpcpp-cpp intel-oneapi-runtime-mkl

echo -e "${GREEN}Done${NC}"
echo ""

# Step 5: Add user to required groups
echo -e "${YELLOW}[5/6] Adding user '$ACTUAL_USER' to video and render groups...${NC}"
usermod -aG video "$ACTUAL_USER"
usermod -aG render "$ACTUAL_USER"
echo -e "${GREEN}Done${NC}"
echo ""

# Step 6: Verify installation
echo -e "${YELLOW}[6/6] Checking installation status...${NC}"

echo "Detected Intel GPUs:"
lspci | grep -i "vga\|3d\|display" | grep -i intel || echo "No Intel GPU detected on PCI bus"
echo ""

echo "Installed Intel compute packages:"
dpkg -l | grep -E "level-zero|intel-opencl|libze-intel|intel-oneapi" | awk '{print "  " $2 " " $3}' || echo "  None found"
echo ""

# Check render devices
echo "Render devices:"
ls -la /dev/dri/ 2>/dev/null || echo "  No DRI devices found"
echo ""

# Final instructions
echo -e "${BLUE}=================================${NC}"
echo -e "${GREEN}Installation Complete!${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""
echo -e "${YELLOW}IMPORTANT: You MUST reboot for the driver to work.${NC}"
echo ""
echo "After reboot, verify the installation with:"
echo "  clinfo -l    # Should show Intel OpenCL devices"
echo ""
echo -e "${YELLOW}To reboot now, run:${NC}"
echo "  sudo reboot"
echo ""
echo -e "${BLUE}Setting up Python environment for Intel XPU:${NC}"
echo ""
echo "  # Create virtual environment"
echo "  python3 -m venv venv-intel"
echo "  source venv-intel/bin/activate"
echo ""
echo "  # Install PyTorch with Intel XPU support"
echo "  pip install torch==2.5.1 torchvision torchaudio \\"
echo "      intel-extension-for-pytorch==2.5.10+xpu \\"
echo "      --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/"
echo ""
echo -e "${BLUE}Verify PyTorch XPU support:${NC}"
echo ""
echo "  python -c \"import torch; import intel_extension_for_pytorch; print(f'XPU available: {torch.xpu.is_available()}')\""
echo ""
echo -e "${YELLOW}Note: PyTorch and IPEX versions must match (e.g., torch 2.5.1 + IPEX 2.5.x)${NC}"
echo ""
