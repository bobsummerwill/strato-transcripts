#!/bin/bash
# ==============================================================================
# Combined Install Script (wrapper)
# ==============================================================================
#
# DESCRIPTION:
#   Convenience wrapper that runs both install_packages.sh and install_venv.sh.
#   For finer control, run them separately:
#     sudo ./scripts/install_packages.sh    # System deps (needs sudo, run once)
#     ./scripts/install_venv.sh --nvidia    # Python venv (no sudo, per-GPU)
#
# USAGE:
#   ./install_packages_and_venv.sh --nvidia   # NVIDIA GPU
#   ./install_packages_and_venv.sh --amd      # AMD GPU via ROCm
#   ./install_packages_and_venv.sh --intel    # Intel GPU via XPU
#   ./install_packages_and_venv.sh --cpu      # CPU-only
#   ./install_packages_and_venv.sh --all      # All backends
#
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Step 1: Install system packages
echo "=== Installing system packages ==="
"$SCRIPT_DIR/install_packages.sh"

echo ""

# Step 2: Create Python venv(s)
echo "=== Setting up Python virtual environment ==="
"$SCRIPT_DIR/install_venv.sh" "$@"
