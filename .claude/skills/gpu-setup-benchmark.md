# GPU Installation and Benchmarking

This skill covers installing GPU drivers (NVIDIA, AMD, Intel) on Ubuntu, setting up Python environments for WhisperX transcription, and running PyTorch benchmarks.

## Quick Start

### 1. Install GPU Drivers
```bash
sudo ./scripts/install_nvidia_drivers.sh && sudo reboot  # NVIDIA
sudo ./scripts/install_amd_drivers.sh && sudo reboot     # AMD
sudo ./scripts/install_intel_drivers.sh && sudo reboot   # Intel
```

### 2. Create Python Environments
```bash
./scripts/install_packages_and_venv.sh --nvidia   # NVIDIA venv
./scripts/install_packages_and_venv.sh --amd      # AMD venv
./scripts/install_packages_and_venv.sh --intel    # Intel venv
./scripts/install_packages_and_venv.sh --cpu      # CPU-only venv
./scripts/install_packages_and_venv.sh --all      # All four venvs
```

### 3. Activate Based on Connected GPU
```bash
source setup_env.sh
source venv-nvidia/bin/activate   # NVIDIA eGPU connected
source venv-amd/bin/activate      # AMD eGPU connected
source venv-intel/bin/activate    # Intel iGPU fallback
source venv-cpu/bin/activate      # CPU-only fallback
```

---

## Python Virtual Environments

Each venv contains WhisperX with all patches and the correct PyTorch backend:

| venv | Backend | PyTorch Version | Use Case |
|------|---------|-----------------|----------|
| `venv-nvidia/` | CUDA | 2.9.1+cu130 | NVIDIA discrete/eGPU |
| `venv-amd/` | ROCm | 2.6.0+rocm6.2 | AMD discrete/eGPU |
| `venv-intel/` | XPU (IPEX) | 2.5.1 + IPEX 2.5.10 | Intel integrated/Arc |
| `venv-cpu/` | CPU | 2.9.1 | Fallback, any system |

**eGPU Workflow:** Pre-create all venvs with `--all`, then activate the matching one based on which GPU is currently connected.

---

## Driver Installation

### NVIDIA
```bash
sudo apt update && sudo apt upgrade -y
sudo ubuntu-drivers install
sudo reboot
# Verify: nvidia-smi
```

### AMD ROCm
```bash
# Add repository
sudo mkdir -p /etc/apt/keyrings
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo gpg --dearmor > /etc/apt/keyrings/rocm.gpg
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/latest $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update

# Install
sudo apt install -y amdgpu-dkms rocm-dev rocm-libs
sudo usermod -aG video,render $USER
sudo reboot
# Verify: rocminfo, rocm-smi
```

**Unofficial GPU Support (RX 6600/6700/6750 XT):**
```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0
```

**Secure Boot Issues:** If amdgpu fails with "Key was rejected", enroll MOK at boot.

### Intel XPU
```bash
# Add repository
sudo mkdir -p /etc/apt/keyrings
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | sudo gpg --dearmor > /etc/apt/keyrings/intel-graphics.gpg
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu noble unified" | sudo tee /etc/apt/sources.list.d/intel-gpu.list
sudo apt update

# Install
sudo apt install -y level-zero intel-opencl-icd libze-intel-gpu1
sudo apt install -y intel-oneapi-runtime-dpcpp-cpp intel-oneapi-runtime-mkl
sudo usermod -aG video,render $USER
sudo reboot
# Verify: clinfo -l
```

**Package Note:** Use `libze-intel-gpu1` (not `intel-level-zero-gpu`) when `intel-opencl-icd` is installed.

---

## Benchmarking

### Benchmark Scripts
- `gpu_benchmarks/scripts/gpu_benchmark.py` - NVIDIA/AMD (CUDA/ROCm)
- `gpu_benchmarks/scripts/gpu_benchmark_intel.py` - Intel XPU

### Run Benchmarks

**NVIDIA (single GPU):**
```bash
source venv-nvidia/bin/activate
cd gpu_benchmarks/scripts && python gpu_benchmark.py --gpu 0 --save
```

**NVIDIA (multi-GPU):**
```bash
source venv-nvidia/bin/activate
cd gpu_benchmarks/scripts
python gpu_benchmark.py --gpu 0 --save  # First GPU
python gpu_benchmark.py --gpu 1 --save  # Second GPU
```

**AMD:**
```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0  # for unofficial GPUs
source venv-amd/bin/activate
cd gpu_benchmarks/scripts && python gpu_benchmark.py --gpu 0 --save
```

**Intel:**
```bash
source venv-intel/bin/activate
cd gpu_benchmarks/scripts && python gpu_benchmark_intel.py --save
```

### GPU Identification by UUID

Each benchmark result includes the GPU UUID, which is unique to each physical card. This allows tracking the same card across different machines or slots.

**View GPU UUIDs:**
```bash
nvidia-smi --query-gpu=index,name,uuid --format=csv
```

**Lookup benchmark history by UUID:**
```bash
source venv-nvidia/bin/activate
python gpu_benchmarks/scripts/gpu_history.py                      # All GPUs
python gpu_benchmarks/scripts/gpu_history.py --uuid GPU-d64aca9a  # Specific card
```

### Graphics Benchmarks (OpenGL/Vulkan)
```bash
DRI_PRIME=1 glmark2   # discrete/eGPU
DRI_PRIME=1 vkmark    # discrete/eGPU
glmark2               # integrated GPU
vkmark                # integrated GPU
```

### Results
- Individual JSON: `gpu_benchmarks/results/benchmark_*.json`
- Summary: `gpu_benchmarks/results/comparison_all_cards.json`

---

## Benchmark Results Matrix

### What Each Benchmark Measures

| Benchmark | What It Measures | Why It Matters |
|-----------|------------------|----------------|
| **MatMul 8K/4K (GFLOPS)** | Matrix multiplication throughput using 8192x8192 (or 4096x4096) FP32 matrices | Core GPU compute performance; directly correlates with ML/AI workload speed |
| **Memory BW H2D (GB/s)** | Host-to-Device memory transfer speed | How fast data can be sent to the GPU; important for large model loading |
| **Memory BW D2H (GB/s)** | Device-to-Host memory transfer speed | How fast results can be retrieved; affects inference latency |
| **Compute (GFLOPS)** | Sustained FP32 compute throughput | Raw computational power for general workloads |
| **glmark2** | OpenGL rendering benchmark score | Graphics/visualization performance |
| **vkmark** | Vulkan rendering benchmark score | Modern graphics API performance |

### Tested GPU Cards

| Card | GPU | Model | UUID (partial) | VRAM | MatMul 8K | H2D GB/s |
|------|-----|-------|----------------|------|-----------|----------|
| #1 | RTX 3090 | EVGA FTW3 Ultra | `0ee51b66...` | 24 GB | 26,942 | 12.2 |
| #2 | RTX 3090 | EVGA (XC3?) | `d64aca9a...` | 24 GB | 25,924 | 12.2 |
| #3 | RTX 5070 | - | - | 12 GB | 22,981 | 9.3 |
| #4 | RX 6750 XT | - | - | 12 GB | 11,060 | 0.7 |
| #5 | Intel MTL | iGPU | - | 28 GB* | ~1,712 (4K) | 4.1 |

*Intel MTL VRAM is shared system memory
**RX 6750 XT requires `export HSA_OVERRIDE_GFX_VERSION=10.3.0` (unofficial ROCm support)
**UUIDs are burned into the GPU at manufacture and persist across machines/slots

### PyTorch Backend Support Status

| Backend | PyTorch Support | Official GPU Support | Notes |
|---------|-----------------|----------------------|-------|
| **CUDA** (NVIDIA) | Official, built-in | All GeForce/Quadro/RTX | `torch.cuda` device |
| **ROCm** (AMD) | Official wheels | MI series, RX 7900 | `torch.cuda` device (same API) |
| **ROCm** (AMD) | Official wheels | RX 6000 series | Needs `HSA_OVERRIDE_GFX_VERSION=10.3.0` |
| **XPU** (Intel) | Intel-maintained extension | Arc, Iris Xe, MTL/RPL/ADL | `torch.xpu` via IPEX package |

### Key Observations

- **NVIDIA RTX 3090** achieves ~25,000 GFLOPS on 8K matmul, best overall compute performance
- **NVIDIA RTX 5070** (12GB Blackwell) performs ~10% below RTX 3090 despite being newer generation
- **AMD RX 6750 XT** achieves ~11,000 GFLOPS via ROCm, roughly 45% of RTX 3090 performance
- **Intel MTL iGPU** achieves ~1,700 GFLOPS on 4K matmul (8K not tested due to memory constraints)
- **Intel vkmark** score (2,886) is notably higher than AMD (1,331), suggesting good Vulkan driver optimization
- **Memory bandwidth** on Intel iGPU is limited by system memory bus (~4 GB/s vs ~25 GB/s on discrete)

### Test Coverage

| Card | PyTorch | glmark2 | vkmark | Memory BW | Full Suite |
|------|---------|---------|--------|-----------|------------|
| #1 RTX 3090 | ✓ | - | - | ✓ | Partial |
| #2 RTX 3090 | ✓ | - | - | ✓ | Partial |
| #3 RTX 5070 | ✓ | - | - | ✓ | Partial |
| #4 RX 6750 XT | ✓ | ✓ | ✓ | ✓ | Full |
| #5 Intel MTL | ✓ (4K) | ✓ | ✓ | ✓ | Full |

---

## eGPU Notes

- Thunderbolt 3/4 enclosures (e.g., Razer Core X) work on Linux
- Check detection: `lspci | grep -i vga`
- Use `DRI_PRIME=1` to run apps on eGPU
- Pre-create all venvs so you can switch based on connected GPU

---

## Troubleshooting

### GPU Not Detected
```bash
lspci | grep -i "vga\|3d\|display"
ls -la /dev/dri/
```

### Permission Denied on /dev/dri
```bash
sudo usermod -aG video,render $USER
# Logout/login or reboot
```

### ROCm "invalid device function"
```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0
```

### Intel XPU Shows False
1. Ensure `libze-intel-gpu1` is installed (not `intel-level-zero-gpu`)
2. Check user is in render group
3. Reboot after package installation

### Check Installed Packages
```bash
dpkg -l | grep nvidia                              # NVIDIA
dpkg -l | grep -E "rocm|amdgpu"                    # AMD
dpkg -l | grep -E "level-zero|intel-opencl|libze"  # Intel
```
