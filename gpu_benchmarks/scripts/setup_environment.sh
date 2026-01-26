#!/bin/bash
#
# GPU Benchmark Suite - Environment Setup
# Automatically detects GPU vendor (NVIDIA/AMD) and installs correct PyTorch
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

echo "========================================"
echo "GPU Benchmark Suite - Environment Setup"
echo "========================================"
echo

# Detect GPU vendor
detect_gpu_vendor() {
    if command -v nvidia-smi &> /dev/null; then
        if nvidia-smi -L 2>/dev/null | grep -q "NVIDIA"; then
            echo "nvidia"
            return
        fi
    fi

    if command -v rocm-smi &> /dev/null; then
        if rocm-smi -i 2>/dev/null | grep -q "GPU"; then
            echo "amd"
            return
        fi
    fi

    # Fallback to lspci
    if command -v lspci &> /dev/null; then
        if lspci | grep -i "nvidia" &> /dev/null; then
            echo "nvidia"
            return
        elif lspci | grep -iE "amd|ati|radeon" &> /dev/null; then
            echo "amd"
            return
        fi
    fi

    echo "unknown"
}

# Get PyTorch install URL based on vendor
get_pytorch_url() {
    local vendor=$1
    case $vendor in
        nvidia)
            # Latest CUDA version
            echo "https://download.pytorch.org/whl/cu128"
            ;;
        amd)
            # Latest ROCm version
            echo "https://download.pytorch.org/whl/rocm6.3"
            ;;
        *)
            # CPU only fallback
            echo "https://download.pytorch.org/whl/cpu"
            ;;
    esac
}

# Main setup
main() {
    echo "Detecting GPU vendor..."
    GPU_VENDOR=$(detect_gpu_vendor)
    echo "Detected: ${GPU_VENDOR^^}"
    echo

    # Set venv name based on vendor
    case $GPU_VENDOR in
        nvidia)
            VENV_NAME="venv"
            PYTORCH_URL=$(get_pytorch_url nvidia)
            echo "Will install PyTorch with CUDA support"
            ;;
        amd)
            VENV_NAME="venv-amd"
            PYTORCH_URL=$(get_pytorch_url amd)
            echo "Will install PyTorch with ROCm support"

            # Check if ROCm is properly installed
            if ! command -v rocm-smi &> /dev/null; then
                echo
                echo "WARNING: rocm-smi not found!"
                echo "Please ensure ROCm is installed: https://rocm.docs.amd.com/"
                echo
            fi
            ;;
        *)
            VENV_NAME="venv-cpu"
            PYTORCH_URL=$(get_pytorch_url cpu)
            echo "WARNING: No GPU detected, will install CPU-only PyTorch"
            ;;
    esac

    VENV_PATH="$PARENT_DIR/$VENV_NAME"
    echo
    echo "Virtual environment: $VENV_PATH"
    echo "PyTorch index URL: $PYTORCH_URL"
    echo

    # Create virtual environment
    if [ -d "$VENV_PATH" ]; then
        echo "Virtual environment already exists."
        read -p "Recreate it? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf "$VENV_PATH"
            python3 -m venv "$VENV_PATH"
        fi
    else
        echo "Creating virtual environment..."
        python3 -m venv "$VENV_PATH"
    fi

    # Activate and install packages
    echo "Activating virtual environment..."
    source "$VENV_PATH/bin/activate"

    echo "Upgrading pip..."
    pip install --upgrade pip

    echo "Installing PyTorch..."
    pip install torch torchvision --index-url "$PYTORCH_URL"

    echo "Installing additional dependencies..."
    if [ "$GPU_VENDOR" = "nvidia" ]; then
        pip install gpustat py3nvml nvidia-ml-py3
    elif [ "$GPU_VENDOR" = "amd" ]; then
        # AMD-specific packages (if available)
        pip install gpustat || true
    fi

    echo
    echo "========================================"
    echo "Setup Complete!"
    echo "========================================"
    echo
    echo "To activate the environment:"
    echo "  source $VENV_PATH/bin/activate"
    echo
    echo "To run benchmarks:"
    echo "  python scripts/gpu_benchmark.py --save"
    echo "  python scripts/gpu_stress_test.py --duration 60 --save"
    echo "  python scripts/identify_gpu.py --save"
    echo

    # Verify installation
    echo "Verifying PyTorch installation..."
    python -c "
import torch
print(f'PyTorch version: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'Device count: {torch.cuda.device_count()}')
    print(f'Device name: {torch.cuda.get_device_name(0)}')
    if hasattr(torch.version, 'hip') and torch.version.hip:
        print(f'ROCm version: {torch.version.hip}')
    elif torch.version.cuda:
        print(f'CUDA version: {torch.version.cuda}')
"
}

# Run main function
main "$@"
