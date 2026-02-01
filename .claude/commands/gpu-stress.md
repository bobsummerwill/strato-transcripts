# GPU Stress Test

Run sustained GPU stress tests to verify stability and thermal performance.

## Usage

```
/gpu-stress [options]
```

## Arguments

- `--duration <seconds>` - Test duration (default: 60)
- `--gpu <id>` - Specific GPU index (default: 0)
- `--save` - Save results to JSON

## Instructions

When the user invokes this command:

1. **Activate venv**:
   ```bash
   source venv-nvidia/bin/activate  # or venv-amd
   ```

2. **Run stress test**:
   ```bash
   cd gpu_benchmarks/scripts && python gpu_stress_test.py --duration <seconds> --save
   ```

3. **Monitor during test** (in separate terminal):
   ```bash
   watch -n 1 nvidia-smi  # NVIDIA
   watch -n 1 rocm-smi    # AMD
   ```

4. **Report results**:
   - Peak temperature
   - Sustained clock speeds
   - Power consumption
   - Any throttling detected

## Examples

```bash
# Quick 60-second stress test
/gpu-stress

# Extended 5-minute test
/gpu-stress --duration 300 --save

# Test specific GPU
/gpu-stress --gpu 1 --duration 120
```

## What It Tests

- **Thermal stability**: Can the GPU maintain clocks under load?
- **Power delivery**: Is power throttling occurring?
- **Memory stability**: Any errors during sustained load?
- **Cooling adequacy**: Temperature trends over time

## Output

Results saved to: `gpu_benchmarks/results/stress_test_<GPU>_<timestamp>.json`

## Safety Notes

- Monitor temperatures during test
- Ensure adequate cooling/airflow
- Stop test if temps exceed 90°C
- Use Ctrl+C to abort if needed
