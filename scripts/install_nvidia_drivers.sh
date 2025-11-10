#!/bin/bash
# ==============================================================================
# NVIDIA Driver Installation Script for RTX 5070
# ==============================================================================
#
# This script installs NVIDIA drivers on Ubuntu 24.04 LTS for RTX 5070 GPU.
# RTX 5070 requires driver version 565 or newer.
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
echo -e "${YELLOW}[2/4] Installing NVIDIA driver...${NC}"
echo "This will automatically detect your GPU and install the latest compatible driver."
ubuntu-drivers install
echo -e "${GREEN}✓ NVIDIA driver installed${NC}"
echo ""

# Step 3: Check current nvidia-smi status (may not work until reboot)
echo -e "${YELLOW}[3/4] Checking current driver status...${NC}"
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

# Step 4: Final instructions
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
echo "  - Driver Version: 565.xx or newer"
echo "  - CUDA Version: 12.8 or newer"
echo "  - GPU: NVIDIA GeForce RTX 5070"
echo ""
echo -e "${YELLOW}To reboot now, run:${NC}"
echo "  sudo reboot"
echo ""
echo "After reboot, continue with:"
echo "  ./install_packages_and_venv.sh"
echo ""
