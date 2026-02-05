# GPU Benchmark Results

Compute benchmark history across all tested GPUs.

**Last Updated:** 2026-02-04

---

## Summary Table

### PyTorch Compute Benchmarks

| GPU | UUID (partial) | VRAM | MatMul 8K | MatMul 4K | H2D GB/s | D2H GB/s | Backend |
|-----|----------------|------|-----------|-----------|----------|----------|---------|
| RTX 3090 (FTW3 Ultra) | `d64aca9a...` | 24 GB | **26,937** | 25,870 | 11.8 | 4.7 | CUDA 13.0 |
| RTX 3090 (XC3 Ultra) | `0ee51b66...` | 24 GB | 26,725 | 25,722 | 12.0 | 4.5 | CUDA 13.0 |
| RTX 5070 | - | 12 GB | 22,981 | 21,553 | 9.3 | 3.0 | CUDA 12.8 |
| RX 6750 XT | - | 12 GB | 11,060 | 11,375 | 0.7 | 0.5 | ROCm 6.2 |
| Intel MTL iGPU | - | 28 GB* | - | 1,712 | 4.1 | 1.5 | XPU (IPEX) |

*Intel MTL VRAM is shared system memory

### vkpeak Vulkan Compute Benchmarks (2026-02-02)

| Device | GPU | FP32 Scalar | FP32 Vec4 | FP16 Tensor | INT8 Tensor | D2D BW |
|--------|-----|-------------|-----------|-------------|-------------|--------|
| 0 | RTX 3090 (FTW3 Ultra) | 24,807 | 24,532 | 159,937 | 318,061 | 310 GB/s |
| 1 | RTX 3090 (XC3 Ultra) | **27,878** | **27,233** | **165,151** | **324,715** | **333 GB/s** |
| 2 | AMD Ryzen 9 9950X3D iGPU | 565 | 542 | N/A | N/A | 33 GB/s |

---

## Detailed Results by GPU

### NVIDIA GeForce RTX 3090 (EVGA FTW3 Ultra)

**UUID:** `GPU-d64aca9a-d2ed-af21-2b47-abeaa19cef7a`
**Subsystem ID:** 3842:3982
**VRAM:** 23.55 GB
**CUDA Capability:** 8.6
**SMs:** 82
**Tested:** 2026-02-04

#### PyTorch Benchmark
| Matrix Size | Time (ms) | GFLOPS |
|-------------|-----------|--------|
| 1024x1024 | 0.126 | 17,068 |
| 2048x2048 | 0.735 | 23,377 |
| 4096x4096 | 5.313 | 25,870 |
| 8192x8192 | 40.82 | **26,937** |

#### vkpeak Benchmark
| Metric | Value | Unit |
|--------|-------|------|
| FP32 Scalar | 24,807 | GFLOPS |
| FP32 Vec4 | 24,532 | GFLOPS |
| FP16 Matrix | 159,937 | GFLOPS |
| INT8 Matrix | 318,061 | GIOPS |
| BF16 Matrix | 80,217 | GFLOPS |
| D2D Bandwidth | 310 | GB/s |

---

### NVIDIA GeForce RTX 3090 (EVGA XC3 Ultra)

**UUID:** `GPU-0ee51b66-aca4-285d-105f-9f2dd6f58879`
**Subsystem ID:** 3842:3987
**VRAM:** 23.56 GB
**CUDA Capability:** 8.6
**SMs:** 82
**Tested:** 2026-02-04

#### PyTorch Benchmark
| Matrix Size | Time (ms) | GFLOPS |
|-------------|-----------|--------|
| 1024x1024 | 0.114 | 18,774 |
| 2048x2048 | 0.741 | 23,191 |
| 4096x4096 | 5.343 | 25,722 |
| 8192x8192 | 41.14 | 26,725 |

#### vkpeak Benchmark
| Metric | Value | Unit |
|--------|-------|------|
| FP32 Scalar | 27,878 | GFLOPS |
| FP32 Vec4 | 27,233 | GFLOPS |
| FP16 Matrix | 165,151 | GFLOPS |
| INT8 Matrix | 324,715 | GIOPS |
| BF16 Matrix | 82,110 | GFLOPS |
| D2D Bandwidth | 333 | GB/s |

**Note:** Both cards perform nearly identically in PyTorch benchmarks (~26.8 TFLOPS).

---

### NVIDIA GeForce RTX 5070 (Blackwell)

**VRAM:** 11.49 GB
**CUDA Capability:** 12.0
**SMs:** 48
**Tested:** 2026-01-23

#### PyTorch Benchmark
| Matrix Size | Time (ms) | GFLOPS |
|-------------|-----------|--------|
| 1024x1024 | 0.130 | 16,542 |
| 2048x2048 | 0.780 | 22,028 |
| 4096x4096 | 6.377 | 21,553 |
| 8192x8192 | 47.84 | 22,981 |

#### Memory Bandwidth
| Size | H2D (GB/s) | D2H (GB/s) |
|------|------------|------------|
| 1 MB | 9.6 | 7.0 |
| 10 MB | 10.9 | 3.8 |
| 100 MB | 9.2 | 2.9 |
| 1000 MB | 9.3 | 3.0 |

**Note:** Despite being newer architecture, the RTX 5070 has fewer SMs (48 vs 82) and lower FP32 throughput than RTX 3090 for large matrix operations.

---

### AMD Radeon RX 6750 XT

**VRAM:** 12.0 GB
**GCN Architecture:** 10.3 (RDNA2)
**Compute Units:** 20
**Tested:** 2026-01-24
**ROCm Version:** 6.2.41133

**Note:** Requires `export HSA_OVERRIDE_GFX_VERSION=10.3.0` for unofficial ROCm support.

#### PyTorch Benchmark
| Matrix Size | Time (ms) | GFLOPS |
|-------------|-----------|--------|
| 1024x1024 | 0.331 | 6,481 |
| 2048x2048 | 1.602 | 10,726 |
| 4096x4096 | 12.08 | 11,375 |
| 8192x8192 | 99.42 | 11,060 |

#### Memory Bandwidth
| Size | H2D (GB/s) | D2H (GB/s) |
|------|------------|------------|
| 1 MB | 1.3 | 1.5 |
| 10 MB | 2.1 | 2.4 |
| 100 MB | 0.7 | 0.3 |
| 1000 MB | 0.7 | 0.5 |

**Note:** Memory bandwidth is significantly lower than NVIDIA cards, likely due to ROCm overhead or PCIe configuration.

---

### Intel Meteor Lake iGPU

**Device:** Intel(R) Graphics (MTL)
**Shared Memory:** 28.5 GB
**Tested:** 2026-01-25
**Backend:** Intel Extension for PyTorch (IPEX) 2.5.10

#### PyTorch Benchmark
| Matrix Size | Time (ms) | GFLOPS |
|-------------|-----------|--------|
| 1024x1024 | 1.766 | 1,216 |
| 2048x2048 | 9.938 | 1,729 |
| 4096x4096 | 80.28 | 1,712 |
| 8192x8192 | - | (OOM) |

**Note:** 8K matrix not tested due to memory constraints on shared system memory.

#### Memory Bandwidth
| Size | H2D (GB/s) | D2H (GB/s) |
|------|------------|------------|
| 1 MB | 1.7 | 1.8 |
| 10 MB | 2.7 | 3.2 |
| 100 MB | 4.1 | 1.5 |

---

### AMD Ryzen 9 9950X3D iGPU (Vulkan only)

**Device:** RADV RAPHAEL_MENDOCINO
**Driver:** Mesa 25.0.7
**Tested:** 2026-02-02

#### vkpeak Benchmark
| Metric | Value | Unit |
|--------|-------|------|
| FP32 Scalar | 565 | GFLOPS |
| FP32 Vec4 | 542 | GFLOPS |
| FP16 Vec4 | 1,019 | GFLOPS |
| INT8 Dotprod | 2,264 | GIOPS |
| D2D Bandwidth | 33 | GB/s |

**Note:** This is the integrated graphics in the AMD CPU, not a discrete GPU. No tensor core support.

---

## Performance Comparison

### FP32 Compute (GFLOPS, higher is better)

```
RTX 3090 FTW3:  ████████████████████████████████████████ 26,937 (PyTorch)
RTX 3090 XC3:   ███████████████████████████████████████  26,725 (PyTorch)
RTX 5070:       ██████████████████████████████████       22,981 (PyTorch)
RX 6750 XT:     ████████████████                         11,060 (PyTorch)
Intel MTL:      ███                                       1,712 (PyTorch)
AMD iGPU:       █                                           565 (vkpeak)
```

### Tensor Core Performance (GFLOPS, vkpeak FP16 Matrix)

```
RTX 3090 FTW3:  ████████████████████████████████████████ 165,151
RTX 3090 XC3:   ██████████████████████████████████████   159,937
RX 6750 XT:     (no tensor cores)
Intel MTL:      (no tensor cores)
```

---

## Test Environment

| Component | Specification |
|-----------|--------------|
| CPU | AMD Ryzen 9 9950X3D 16-Core |
| GPU Slot 0 | RTX 3090 (FTW3 Ultra) - `d64aca9a` |
| GPU Slot 1 | RTX 3090 (XC3 Ultra) - `0ee51b66` |
| OS | Ubuntu 24.04 LTS |
| Kernel | 6.14.0-37-generic |
| NVIDIA Driver | 590.48.01 |
| CUDA | 13.0 |
| PyTorch | 2.9.1+cu130 |

---

## How to Run Benchmarks

### PyTorch Benchmark
```bash
source venv-nvidia/bin/activate
cd gpu_benchmarks/scripts
python gpu_benchmark.py --gpu 0 --save  # First GPU
python gpu_benchmark.py --gpu 1 --save  # Second GPU
```

### vkpeak Vulkan Benchmark
```bash
python3 gpu_benchmarks/scripts/vkpeak_benchmark.py --save  # All GPUs
python3 gpu_benchmarks/scripts/vkpeak_benchmark.py --gpu 0 --save  # Specific GPU
```

### View Benchmark History
```bash
python3 gpu_benchmarks/scripts/gpu_history.py  # All GPUs
python3 gpu_benchmarks/scripts/gpu_history.py --uuid GPU-0ee51b66  # By UUID
```
