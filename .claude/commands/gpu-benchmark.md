# GPU Benchmark

Run PyTorch GPU benchmarks to measure compute performance and memory bandwidth.

## Usage

```
/gpu-benchmark [options]
```

## Arguments

- `--save` - Save results to JSON file
- `--gpu <id>` - Specific GPU index (default: 0)
- `--intel` - Use Intel XPU benchmark script

## Instructions

When the user invokes this command:

1. **Detect GPU type**:
   ```bash
   lspci | grep -i "vga\|3d\|display"
   ```

2. **Activate appropriate venv**:
   ```bash
   # NVIDIA
   source venv-nvidia/bin/activate

   # AMD
   export HSA_OVERRIDE_GFX_VERSION=10.3.0  # for unofficial GPUs
   source venv-amd/bin/activate

   # Intel
   source venv-intel/bin/activate
   ```

3. **Run benchmark**:
   ```bash
   # NVIDIA/AMD
   cd gpu_benchmarks/scripts && python gpu_benchmark.py --save

   # Intel XPU
   cd gpu_benchmarks/scripts && python gpu_benchmark_intel.py --save
   ```

4. **Report results**:
   - MatMul GFLOPS (8K or 4K matrix)
   - Memory bandwidth (H2D and D2H)
   - Comparison to known cards

## Examples

```bash
# Run full benchmark suite
/gpu-benchmark --save

# Intel XPU benchmark
/gpu-benchmark --intel --save

# Specific GPU in multi-GPU system
/gpu-benchmark --gpu 1 --save
```

## Benchmark Tests

| Test | What It Measures |
|------|------------------|
| MatMul 8K/4K | Matrix multiplication throughput (GFLOPS) |
| Memory H2D | Host-to-Device transfer speed (GB/s) |
| Memory D2H | Device-to-Host transfer speed (GB/s) |
| Compute | Sustained FP32 throughput (GFLOPS) |

## Reference Results

| GPU | MatMul 8K | H2D GB/s | D2H GB/s |
|-----|-----------|----------|----------|
| RTX 3090 | ~25,000 | ~25 | ~25 |
| RTX 5070 | ~23,000 | ~25 | ~25 |
| RX 6750 XT | ~11,000 | ~11 | ~11 |
| Intel MTL | ~1,700 (4K) | ~4 | ~1.5 |

## Output

Results saved to: `gpu_benchmarks/results/benchmark_<GPU>_<timestamp>.json`
