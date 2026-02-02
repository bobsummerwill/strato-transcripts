# GPU Monitor

Monitor GPU utilization, temperature, and memory in real-time.

## Usage

```
/gpu-monitor [options]
```

## Arguments

- `--interval <seconds>` - Update interval (default: 1)
- `--gpu <id>` - Specific GPU index (default: all)
- `--log <file>` - Log to file

## Instructions

When the user invokes this command:

1. **Quick status check**:
   ```bash
   # NVIDIA
   nvidia-smi

   # AMD
   rocm-smi

   # Intel
   xpu-smi discovery
   ```

2. **Continuous monitoring**:
   ```bash
   # NVIDIA
   watch -n 1 nvidia-smi

   # AMD
   watch -n 1 rocm-smi

   # Python monitor script
   cd gpu_benchmarks/scripts && python gpu_monitor.py
   ```

3. **Report metrics**:
   - GPU utilization %
   - Memory usage
   - Temperature
   - Power draw
   - Clock speeds

## Examples

```bash
# Quick status
/gpu-monitor

# Continuous with 2-second interval
/gpu-monitor --interval 2

# Log to file during workload
/gpu-monitor --log gpu_log.csv
```

## Monitored Metrics

| Metric | NVIDIA | AMD | Intel |
|--------|--------|-----|-------|
| Utilization | Yes | Yes | Yes |
| Temperature | Yes | Yes | Yes |
| Memory Used | Yes | Yes | Yes |
| Power Draw | Yes | Yes | Limited |
| Fan Speed | Yes | Yes | N/A |
| Clock Speed | Yes | Yes | Yes |

## CLI Commands Reference

```bash
# NVIDIA
nvidia-smi                          # Quick status
nvidia-smi -l 1                     # Loop every 1 second
nvidia-smi --query-gpu=utilization.gpu,temperature.gpu,memory.used --format=csv -l 1

# AMD
rocm-smi                            # Quick status
rocm-smi -d 0 --showtemp --showuse  # Detailed for GPU 0
watch -n 1 rocm-smi

# Intel
xpu-smi discovery                   # List devices
xpu-smi stats -d 0                  # Stats for device 0
```

## Use Cases

- Monitor during transcription workloads
- Verify GPU is being utilized
- Check for thermal throttling
- Debug performance issues
