#!/usr/bin/env python3
"""
vkpeak Vulkan Benchmark Wrapper
Runs vkpeak on all or specified GPUs and saves results to JSON
"""
import subprocess
import json
import argparse
import re
from datetime import datetime
from pathlib import Path


def parse_vkpeak_output(output: str) -> dict:
    """Parse vkpeak output into structured data"""
    results = {}

    for line in output.strip().split('\n'):
        line = line.strip()
        if not line or '=' not in line:
            continue

        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()

        if key == 'device':
            results['device_name'] = value
        elif key == 'driver':
            results['driver'] = value
        else:
            # Parse numeric values with units
            match = re.match(r'([\d.]+)\s*(GFLOPS|GIOPS|GBPS)', value)
            if match:
                results[key] = {
                    'value': float(match.group(1)),
                    'unit': match.group(2)
                }

    return results


def run_vkpeak(device_id: int, vkpeak_path: str = None) -> dict:
    """Run vkpeak on a specific device"""
    if vkpeak_path is None:
        script_dir = Path(__file__).parent
        vkpeak_path = script_dir.parent / "bin" / "vkpeak"

    try:
        result = subprocess.run(
            [str(vkpeak_path), str(device_id)],
            capture_output=True, text=True, timeout=300
        )
        # vkpeak outputs to stderr, not stdout
        output = result.stderr if result.stderr else result.stdout

        if result.returncode != 0:
            return {'error': output or 'Unknown error', 'device_id': device_id}

        parsed = parse_vkpeak_output(output)
        parsed['device_id'] = device_id
        return parsed
    except subprocess.TimeoutExpired:
        return {'error': 'Timeout', 'device_id': device_id}
    except FileNotFoundError:
        return {'error': f'vkpeak not found at {vkpeak_path}', 'device_id': device_id}


def get_device_list(vkpeak_path: str = None) -> list:
    """Get list of Vulkan devices by asking vkpeak for an invalid device"""
    if vkpeak_path is None:
        script_dir = Path(__file__).parent
        vkpeak_path = script_dir.parent / "bin" / "vkpeak"

    try:
        # Ask for device 999 to get the device list from error output
        result = subprocess.run(
            [str(vkpeak_path), "999"],
            capture_output=True, text=True, timeout=10
        )
        # Parse "Available devices:" section from stderr
        devices = []
        in_devices = False
        for line in result.stderr.split('\n'):
            if 'Available devices:' in line:
                in_devices = True
                continue
            if in_devices and '=' in line:
                match = re.match(r'(\d+)\s*=\s*(.+)', line.strip())
                if match:
                    devices.append({
                        'id': int(match.group(1)),
                        'name': match.group(2).strip()
                    })
        return devices
    except Exception as e:
        print(f"Error getting device list: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description='vkpeak Vulkan Benchmark Wrapper')
    parser.add_argument('--gpu', type=int, help='Specific GPU ID to benchmark (default: all)')
    parser.add_argument('--save', action='store_true', help='Save results to JSON file')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()

    timestamp = datetime.now()
    script_dir = Path(__file__).parent
    results_dir = script_dir.parent / "results"

    script_dir = Path(__file__).parent
    vkpeak_path = script_dir.parent / "bin" / "vkpeak"

    if args.gpu is not None:
        gpus = [args.gpu]
    else:
        devices = get_device_list(str(vkpeak_path))
        if not devices:
            print("No Vulkan devices found")
            return 1
        # Skip llvmpipe (software renderer)
        gpus = [d['id'] for d in devices if 'llvmpipe' not in d['name'].lower()]
        print(f"Found {len(devices)} Vulkan devices ({len(gpus)} hardware):")

    all_results = {
        'test_metadata': {
            'timestamp': timestamp.isoformat(),
            'date': timestamp.strftime('%Y-%m-%d'),
            'time': timestamp.strftime('%H:%M:%S'),
            'benchmark': 'vkpeak'
        },
        'devices': []
    }

    for gpu_id in gpus:
        print(f"\n{'='*60}")
        print(f"Benchmarking Vulkan device {gpu_id}...")
        print('='*60)

        result = run_vkpeak(gpu_id)
        all_results['devices'].append(result)

        if 'error' in result:
            print(f"Error: {result['error']}")
            continue

        # Print summary
        print(f"Device: {result.get('device_name', 'Unknown')}")
        print(f"Driver: {result.get('driver', 'Unknown')}")
        print()

        # Key metrics
        metrics = [
            ('fp32-scalar', 'FP32 Scalar'),
            ('fp32-vec4', 'FP32 Vec4'),
            ('fp16-matrix', 'FP16 Matrix (Tensor)'),
            ('int8-matrix', 'INT8 Matrix'),
            ('copy-h2d', 'Host to Device'),
            ('copy-d2h', 'Device to Host'),
            ('copy-d2d', 'Device to Device'),
        ]

        for key, label in metrics:
            if key in result:
                val = result[key]
                print(f"  {label:20}: {val['value']:>12.2f} {val['unit']}")

    if args.json:
        print(json.dumps(all_results, indent=2))

    if args.save:
        results_dir.mkdir(parents=True, exist_ok=True)
        filename = f"vkpeak_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
        filepath = results_dir / filename
        with open(filepath, 'w') as f:
            json.dump(all_results, f, indent=2)
        print(f"\nResults saved to: {filepath}")

    return 0


if __name__ == "__main__":
    exit(main())
