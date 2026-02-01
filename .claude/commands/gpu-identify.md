# GPU Identification

Identify and catalog GPU hardware with unique identifiers for tracking.

## Usage

```
/gpu-identify [options]
```

## Arguments

- `--gpu <id>` - Specific GPU index (default: all)
- `--save` - Save identification to JSON

## Instructions

When the user invokes this command:

1. **Check system GPUs**:
   ```bash
   lspci | grep -i "vga\|3d\|display"
   ```

2. **Run identification script**:
   ```bash
   source venv-nvidia/bin/activate  # or appropriate venv
   cd gpu_benchmarks/scripts && python identify_gpu.py --save
   ```

3. **Report GPU details**:
   - Model name
   - VRAM size
   - Driver version
   - Unique identifier (serial/UUID)
   - PCIe slot information

## Examples

```bash
# Identify all GPUs
/gpu-identify

# Identify and save
/gpu-identify --save

# Specific GPU in multi-GPU system
/gpu-identify --gpu 0
```

## Information Collected

| Field | Description |
|-------|-------------|
| Model | GPU model name (e.g., "NVIDIA GeForce RTX 3090") |
| VRAM | Total video memory |
| UUID | Unique GPU identifier |
| Driver | Installed driver version |
| CUDA/ROCm | Compute capability version |
| PCIe | Bus ID and slot info |
| Temp | Current temperature |

## Use Cases

- **Card tracking**: Identify which physical card is which
- **eGPU workflows**: Confirm which GPU is connected
- **Multi-GPU systems**: Map GPU indices to physical cards
- **RMA/warranty**: Record serial numbers

## Output

Results saved to: `gpu_benchmarks/results/gpu_identification_<GPU>_<timestamp>.json`
