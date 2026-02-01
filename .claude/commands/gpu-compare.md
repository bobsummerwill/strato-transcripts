# Compare GPU Results

Compare benchmark results across different GPUs and test runs.

## Usage

```
/gpu-compare [options]
```

## Arguments

- `--all` - Compare all saved results
- `--cards <list>` - Compare specific cards (comma-separated)
- `--output <file>` - Save comparison to file

## Instructions

When the user invokes this command:

1. **List available results**:
   ```bash
   ls gpu_benchmarks/results/benchmark_*.json
   ```

2. **Run comparison**:
   ```bash
   cd gpu_benchmarks/scripts && python compare_results.py
   ```

3. **Report comparison**:
   - Side-by-side performance metrics
   - Relative performance percentages
   - Best/worst for each metric

## Examples

```bash
# Compare all benchmark results
/gpu-compare --all

# Compare specific cards
/gpu-compare --cards "RTX 3090,RTX 5070,RX 6750 XT"

# Save comparison report
/gpu-compare --all --output comparison.json
```

## Comparison Metrics

| Metric | Unit | Higher is Better |
|--------|------|------------------|
| MatMul 8K | GFLOPS | Yes |
| MatMul 4K | GFLOPS | Yes |
| Memory H2D | GB/s | Yes |
| Memory D2H | GB/s | Yes |
| glmark2 | score | Yes |
| vkmark | score | Yes |

## Current Results Matrix

| Card | MatMul 8K | H2D | D2H |
|------|-----------|-----|-----|
| RTX 3090 #1 | 25,658 | ~25 | ~25 |
| RTX 3090 #2 | 24,586 | ~25 | ~25 |
| RTX 5070 | 22,981 | ~25 | ~25 |
| RX 6750 XT | 11,060 | 11.2 | 10.8 |
| Intel MTL | 1,712 (4K) | 4.1 | 1.5 |

## Output

Comparison saved to: `gpu_benchmarks/results/comparison_all_cards.json`
