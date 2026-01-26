# AMD GPU Support

This benchmark suite supports both NVIDIA and AMD GPUs. The tools automatically detect the GPU vendor and use the appropriate backend.

## Requirements for AMD GPUs

### 1. ROCm Installation

AMD GPUs require ROCm (Radeon Open Compute) to be installed:

```bash
# Ubuntu 22.04/24.04
# Follow official guide: https://rocm.docs.amd.com/

# Quick install (Ubuntu):
wget https://repo.radeon.com/amdgpu-install/latest/ubuntu/jammy/amdgpu-install_6.3.60300-1_all.deb
sudo apt install ./amdgpu-install_6.3.60300-1_all.deb
sudo amdgpu-install --usecase=rocm

# Verify installation
rocm-smi
```

### 2. PyTorch with ROCm

The setup script automatically installs the correct PyTorch version:

```bash
# Automatic setup (recommended)
./scripts/setup_environment.sh

# Manual install
python3 -m venv venv-amd
source venv-amd/bin/activate
pip install torch torchvision --index-url https://download.pytorch.org/whl/rocm6.3
```

## Supported AMD GPUs

### RX 7000 Series (RDNA 3)
- RX 7900 XTX
- RX 7900 XT
- RX 7900 GRE
- RX 7800 XT
- RX 7700 XT
- RX 7600/7600 XT

### RX 6000 Series (RDNA 2)
- RX 6900 XT
- RX 6800 XT / 6800
- RX 6700 XT
- RX 6600 XT / 6600

### Radeon PRO / Instinct
- Instinct MI300X/MI300A
- Instinct MI250X/MI250
- Instinct MI210/MI100
- Radeon PRO W7900/W7800

## Identified Manufacturers

The tool can identify specific GPU models from these AMD partners:

| Vendor ID | Manufacturer | Example Models |
|-----------|--------------|----------------|
| 1DA2 | Sapphire | NITRO+, PULSE, PURE |
| 1682 | XFX | SPEEDSTER MERC, QICK |
| 148C | PowerColor | RED DEVIL, HELLHOUND |
| 1043 | ASUS | ROG STRIX, TUF GAMING |
| 1458 | Gigabyte | AORUS, GAMING OC |
| 1462 | MSI | GAMING X TRIO |
| 1002 | AMD | Reference Design |

## Running Benchmarks on AMD

The same commands work for both NVIDIA and AMD:

```bash
# Identify GPU (auto-detects vendor)
python scripts/identify_gpu.py --save

# Run benchmarks
python scripts/gpu_benchmark.py --save

# Run stress test
python scripts/gpu_stress_test.py --duration 300 --save
```

## Output Differences

### Metadata
- NVIDIA: Reports `cuda_version` and `cuda_capability`
- AMD: Reports `rocm_version` and `gcn_arch`

### Monitoring
- NVIDIA: Uses `nvidia-smi` for temperature, power, utilization
- AMD: Uses `rocm-smi` for temperature, power, utilization

### Example AMD Output

```
GPU 0: AMD Radeon RX 7900 XTX
Vendor: AMD (ROCM 6.3)
GCN Arch: 11.0
Total Memory: 24.00 GB
Multiprocessors/CUs: 96
```

## Troubleshooting

### "ROCm not found"
```bash
# Check if ROCm is installed
rocm-smi --version

# Check if GPU is detected
rocm-smi -i
```

### "No GPU detected by PyTorch"
```bash
# Verify PyTorch ROCm build
python -c "import torch; print(torch.cuda.is_available())"
python -c "import torch; print(torch.version.hip)"

# Check ROCm environment
echo $ROCM_PATH
```

### "Permission denied" for GPU access
```bash
# Add user to render and video groups
sudo usermod -a -G render,video $USER
# Log out and back in
```

### Temperature/Power not showing
Some AMD GPUs may not expose all sensors via ROCm. The benchmark will show "N/A" for unavailable metrics.

## Performance Notes

1. **ROCm vs CUDA**: PyTorch on ROCm uses HIP (Heterogeneous-compute Interface for Portability) which translates CUDA calls. Performance is generally comparable.

2. **Memory Bandwidth**: AMD GPUs often have higher memory bandwidth due to wider memory buses.

3. **Compute Units vs SMs**: AMD "Compute Units" are roughly equivalent to NVIDIA "Streaming Multiprocessors" but internal architecture differs.

4. **Power Reporting**: AMD power reporting may differ from NVIDIA. Some cards report "socket power" vs "GPU power".
