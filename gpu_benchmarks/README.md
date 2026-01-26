# GPU Benchmarking Suite

Comprehensive GPU benchmarking, stress testing, and identification tools.

**Supports both NVIDIA (CUDA) and AMD (ROCm) GPUs.**

## Quick Start

### First-Time Setup

```bash
# Automatic setup - detects GPU vendor and installs correct PyTorch
./scripts/setup_environment.sh

# Or manual setup for NVIDIA:
python3 -m venv venv && source venv/bin/activate
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128

# Or manual setup for AMD:
python3 -m venv venv-amd && source venv-amd/bin/activate
pip install torch torchvision --index-url https://download.pytorch.org/whl/rocm6.3
```

### Running Benchmarks

```bash
# Activate environment
source ../venv/bin/activate

# Run interactive menu
./benchmark

# Or run tests directly
python scripts/test_all_gpus.py --benchmark --stress --duration 600 --compare
```

## Directory Structure

```
gpu_benchmarks/
├── benchmark              # Main launcher script (run this!)
├── scripts/               # All Python and shell scripts
│   ├── gpu_utils.py              # Unified GPU utilities (NVIDIA + AMD)
│   ├── identify_gpu.py           # GPU identification
│   ├── gpu_benchmark.py          # Performance benchmarking
│   ├── gpu_stress_test.py        # Stability testing
│   ├── test_all_gpus.py          # Batch testing (all GPUs)
│   ├── compare_results.py        # Results comparison
│   ├── gpu_monitor.py            # Real-time monitoring
│   ├── run_benchmark.sh          # Interactive menu
│   └── setup_environment.sh      # Auto-setup for NVIDIA/AMD
├── docs/                  # All documentation
│   ├── README.md                 # Detailed documentation
│   ├── QUICKSTART.md             # Quick reference
│   ├── AMD_SUPPORT.md            # AMD/ROCm setup and usage
│   ├── CARD_SWAPPING_WORKFLOW.md # Card-swapping guide
│   ├── GPU_IDENTIFICATION_GUIDE.md # ID guide with agent instructions
│   ├── MULTI_GPU_GUIDE.md        # Multi-GPU testing
│   └── CHANGES_MULTI_GPU.md      # Change log
└── results/               # Test results saved here
    └── archive/           # Archive old results here
```

## Usage

### Card Swapping Workflow (Your Use Case)

Testing 4 different cards by swapping them one at a time:

```bash
# For each card:
# 1. Shutdown, swap card, boot up
# 2. Run:
./benchmark

# Or directly:
python scripts/test_all_gpus.py --benchmark --stress --duration 600

# After testing all cards:
python scripts/compare_results.py --output results/comparison.txt
```

See [docs/CARD_SWAPPING_WORKFLOW.md](docs/CARD_SWAPPING_WORKFLOW.md) for complete guide.

### Identify GPU Model

```bash
python scripts/identify_gpu.py --gpu 0 --save
```

See [docs/GPU_IDENTIFICATION_GUIDE.md](docs/GPU_IDENTIFICATION_GUIDE.md) for details.

### Run Benchmark

```bash
# Full benchmark
python scripts/gpu_benchmark.py --save

# Specific test
python scripts/gpu_benchmark.py --test matmul --save
```

### Run Stress Test

```bash
# 10-minute test
python scripts/gpu_stress_test.py --duration 600 --save

# Quick test
python scripts/gpu_stress_test.py --duration 60 --test compute --save
```

### Monitor GPU

```bash
# Real-time dashboard
python scripts/gpu_monitor.py

# Simple status
gpustat -i 1
```

### Compare Results

```bash
python scripts/compare_results.py --output results/comparison.txt
```

## Documentation

- **[docs/QUICKSTART.md](docs/QUICKSTART.md)** - Quick reference guide
- **[docs/CARD_SWAPPING_WORKFLOW.md](docs/CARD_SWAPPING_WORKFLOW.md)** - Testing multiple cards by swapping
- **[docs/GPU_IDENTIFICATION_GUIDE.md](docs/GPU_IDENTIFICATION_GUIDE.md)** - GPU model identification
- **[docs/MULTI_GPU_GUIDE.md](docs/MULTI_GPU_GUIDE.md)** - Multi-GPU testing
- **[docs/README.md](docs/README.md)** - Full detailed documentation

## Results Organization

Results are automatically saved to current directory with GPU-specific filenames:

```
benchmark_GPU0_NVIDIA_GeForce_RTX_3090_20260122_143025.json
stress_test_GPU0_NVIDIA_GeForce_RTX_3090_20260122_143530.json
gpu_identification_GPU0_20260122_143010.json
```

**Best Practice:** Move results to `results/` directory after testing:

```bash
# Move current results
mv benchmark_*.json stress_test_*.json gpu_identification_*.json results/

# Archive old results
mv results/benchmark_*.json results/archive/
```

## Tools Overview

| Tool | Purpose | Usage |
|------|---------|-------|
| **identify_gpu.py** | Identify exact GPU model (EVGA FTW3, ASUS ROG, etc.) | `python scripts/identify_gpu.py --gpu 0` |
| **gpu_benchmark.py** | Performance benchmarking (GFLOPS, bandwidth) | `python scripts/gpu_benchmark.py --save` |
| **gpu_stress_test.py** | Stability testing (compute, memory) | `python scripts/gpu_stress_test.py --duration 600` |
| **test_all_gpus.py** | Batch test all GPUs | `python scripts/test_all_gpus.py --benchmark --stress` |
| **compare_results.py** | Compare results across GPUs | `python scripts/compare_results.py` |
| **gpu_monitor.py** | Real-time GPU monitoring | `python scripts/gpu_monitor.py` |
| **run_benchmark.sh** | Interactive menu | `./scripts/run_benchmark.sh` or `./benchmark` |

## Requirements

- Python 3.8+
- PyTorch with CUDA support
- NVIDIA GPU with drivers installed
- Virtual environment activated

Installed packages:
- torch
- gpustat
- py3nvml
- nvidia-ml-py3

## Quick Commands

```bash
# Activate environment
source ../venv/bin/activate

# Interactive menu
./benchmark

# Test current GPU
python scripts/test_all_gpus.py --benchmark --stress --duration 600 --compare

# Identify GPU
python scripts/identify_gpu.py --gpu 0

# Compare all results
python scripts/compare_results.py

# Monitor GPU
python scripts/gpu_monitor.py
```

## Support

For detailed instructions and troubleshooting, see the documentation in `docs/`.

---

**Your Current GPU:** EVGA GeForce RTX 3090 XC3 ULTRA GAMING (420W, Mid-tier)
