#!/usr/bin/env python3
"""
GPU Performance Benchmarking Suite
Measures throughput, latency, and bandwidth
Supports both NVIDIA (CUDA) and AMD (ROCm) GPUs
"""
import torch
import time
import argparse
import json
from datetime import datetime

# Import unified GPU utilities
try:
    from gpu_utils import GPUVendor, detect_gpu_vendor, get_gpu_temperature
    HAS_GPU_UTILS = True
except ImportError:
    HAS_GPU_UTILS = False

def get_compute_backend():
    """Determine if using CUDA or ROCm"""
    if hasattr(torch.version, 'hip') and torch.version.hip is not None:
        return 'rocm', torch.version.hip
    elif torch.version.cuda is not None:
        return 'cuda', torch.version.cuda
    else:
        return 'unknown', 'unknown'

class GPUBenchmark:
    def __init__(self, gpu_id=0):
        self.device = torch.device(f'cuda:{gpu_id}')
        self.gpu_id = gpu_id
        torch.cuda.set_device(self.device)

        # Detect compute backend (CUDA or ROCm)
        self.backend, self.backend_version = get_compute_backend()

        # Detect vendor
        if HAS_GPU_UTILS:
            self.vendor = detect_gpu_vendor()
        else:
            self.vendor = 'nvidia' if self.backend == 'cuda' else 'amd'

        props = torch.cuda.get_device_properties(self.device)
        self.gpu_name = props.name
        self.total_memory = props.total_memory / 1024**3

        # Get GPU UUID for identification
        try:
            import subprocess
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=uuid', '--format=csv,noheader', '-i', str(gpu_id)],
                capture_output=True, text=True
            )
            self.gpu_uuid = result.stdout.strip() if result.returncode == 0 else None
        except Exception:
            self.gpu_uuid = None

        # Build GPU properties dict (works for both NVIDIA and AMD)
        self.gpu_props = {
            'id': gpu_id,
            'name': props.name,
            'uuid': self.gpu_uuid,
            'total_memory_gb': self.total_memory,
            'multiprocessor_count': props.multi_processor_count,
            'max_threads_per_multiprocessor': props.max_threads_per_multi_processor,
            'warp_size': props.warp_size,
        }

        # Add vendor-specific naming
        if self.backend == 'rocm':
            self.gpu_props['gcn_arch'] = f"{props.major}.{props.minor}"
            self.gpu_props['compute_units'] = props.multi_processor_count
            capability_label = "GCN Arch"
        else:
            self.gpu_props['cuda_capability'] = f"{props.major}.{props.minor}"
            capability_label = "CUDA Capability"

        vendor_str = self.vendor.value.upper() if hasattr(self.vendor, 'value') else str(self.vendor).upper()
        print(f"GPU {gpu_id}: {self.gpu_name}")
        print(f"Vendor: {vendor_str} ({self.backend.upper()} {self.backend_version})")
        print(f"{capability_label}: {props.major}.{props.minor}")
        print(f"Total Memory: {self.total_memory:.2f} GB")
        print(f"Multiprocessors/CUs: {props.multi_processor_count}")

    def benchmark_matmul(self, sizes=[1024, 2048, 4096, 8192], iterations=100):
        """Benchmark matrix multiplication performance"""
        print(f"\n{'='*80}")
        print("Matrix Multiplication Benchmark")
        print(f"{'='*80}\n")

        results = []

        for size in sizes:
            print(f"Testing {size}x{size} matrices...")

            # Warmup
            A = torch.randn(size, size, device=self.device, dtype=torch.float32)
            B = torch.randn(size, size, device=self.device, dtype=torch.float32)
            for _ in range(10):
                _ = torch.matmul(A, B)
            torch.cuda.synchronize()

            # Benchmark
            times = []
            for _ in range(iterations):
                start = time.perf_counter()
                C = torch.matmul(A, B)
                torch.cuda.synchronize()
                end = time.perf_counter()
                times.append(end - start)

            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)

            # Calculate FLOPS (2*N^3 operations for NxN matrix multiplication)
            operations = 2 * size**3
            gflops = (operations / avg_time) / 1e9

            result = {
                'size': size,
                'avg_time_ms': avg_time * 1000,
                'min_time_ms': min_time * 1000,
                'max_time_ms': max_time * 1000,
                'gflops': gflops
            }
            results.append(result)

            print(f"  Size: {size}x{size}")
            print(f"  Average time: {avg_time*1000:.3f} ms")
            print(f"  Min time: {min_time*1000:.3f} ms")
            print(f"  Max time: {max_time*1000:.3f} ms")
            print(f"  Performance: {gflops:.2f} GFLOPS")
            print()

            del A, B, C
            torch.cuda.empty_cache()

        return results

    def benchmark_memory_bandwidth(self, sizes=[1, 10, 100, 1000], iterations=100):
        """Benchmark memory bandwidth"""
        print(f"\n{'='*80}")
        print("Memory Bandwidth Benchmark")
        print(f"{'='*80}\n")

        results = []

        for size_mb in sizes:
            size_elements = int(size_mb * 1024 * 1024 / 4)  # float32 = 4 bytes
            print(f"Testing {size_mb} MB transfer...")

            # Warmup
            data = torch.randn(size_elements, device='cpu', dtype=torch.float32)
            for _ in range(10):
                _ = data.to(self.device)
            torch.cuda.synchronize()

            # Benchmark host to device
            times_h2d = []
            for _ in range(iterations):
                data_cpu = torch.randn(size_elements, device='cpu', dtype=torch.float32)
                torch.cuda.synchronize()

                start = time.perf_counter()
                data_gpu = data_cpu.to(self.device)
                torch.cuda.synchronize()
                end = time.perf_counter()

                times_h2d.append(end - start)

            avg_time_h2d = sum(times_h2d) / len(times_h2d)
            bandwidth_h2d = (size_mb / avg_time_h2d) / 1024  # GB/s

            # Benchmark device to host
            times_d2h = []
            data_gpu = torch.randn(size_elements, device=self.device, dtype=torch.float32)
            for _ in range(iterations):
                torch.cuda.synchronize()

                start = time.perf_counter()
                data_cpu = data_gpu.to('cpu')
                torch.cuda.synchronize()
                end = time.perf_counter()

                times_d2h.append(end - start)

            avg_time_d2h = sum(times_d2h) / len(times_d2h)
            bandwidth_d2h = (size_mb / avg_time_d2h) / 1024  # GB/s

            result = {
                'size_mb': size_mb,
                'h2d_bandwidth_gbps': bandwidth_h2d,
                'd2h_bandwidth_gbps': bandwidth_d2h,
                'h2d_time_ms': avg_time_h2d * 1000,
                'd2h_time_ms': avg_time_d2h * 1000
            }
            results.append(result)

            print(f"  Size: {size_mb} MB")
            print(f"  Host to Device: {bandwidth_h2d:.2f} GB/s ({avg_time_h2d*1000:.3f} ms)")
            print(f"  Device to Host: {bandwidth_d2h:.2f} GB/s ({avg_time_d2h*1000:.3f} ms)")
            print()

            del data_gpu
            torch.cuda.empty_cache()

        return results

    def benchmark_compute_throughput(self, iterations=1000):
        """Benchmark various compute operations"""
        print(f"\n{'='*80}")
        print("Compute Throughput Benchmark")
        print(f"{'='*80}\n")

        size = 10000000  # 10M elements
        results = {}

        operations = {
            'Addition': lambda x, y: x + y,
            'Multiplication': lambda x, y: x * y,
            'Division': lambda x, y: x / y,
            'Sqrt': lambda x, y: torch.sqrt(x),
            'Exp': lambda x, y: torch.exp(x),
            'Sin': lambda x, y: torch.sin(x),
        }

        A = torch.randn(size, device=self.device, dtype=torch.float32)
        B = torch.randn(size, device=self.device, dtype=torch.float32)

        for op_name, op_func in operations.items():
            print(f"Testing {op_name}...")

            # Warmup
            for _ in range(10):
                _ = op_func(A, B)
            torch.cuda.synchronize()

            # Benchmark
            times = []
            for _ in range(iterations):
                start = time.perf_counter()
                result = op_func(A, B)
                torch.cuda.synchronize()
                end = time.perf_counter()
                times.append(end - start)

            avg_time = sum(times) / len(times)
            throughput = (size / avg_time) / 1e9  # Giga operations per second

            results[op_name] = {
                'avg_time_us': avg_time * 1e6,
                'throughput_gops': throughput
            }

            print(f"  Average time: {avg_time*1e6:.2f} μs")
            print(f"  Throughput: {throughput:.2f} GOPS")
            print()

        del A, B
        torch.cuda.empty_cache()

        return results

    def run_full_benchmark(self, save_results=True):
        """Run complete benchmark suite"""
        print(f"\n{'#'*80}")
        print(f"GPU Performance Benchmark Suite")
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'#'*80}\n")

        timestamp = datetime.now()

        # Build test metadata with correct backend info
        test_metadata = {
            'timestamp': timestamp.isoformat(),
            'date': timestamp.strftime('%Y-%m-%d'),
            'time': timestamp.strftime('%H:%M:%S'),
            'pytorch_version': torch.__version__,
            'compute_backend': self.backend,
        }

        # Add backend-specific version
        if self.backend == 'rocm':
            test_metadata['rocm_version'] = self.backend_version
        else:
            test_metadata['cuda_version'] = self.backend_version

        all_results = {
            'gpu_info': self.gpu_props,
            'test_metadata': test_metadata,
            'benchmark_results': {
                'matmul': self.benchmark_matmul(),
                'memory_bandwidth': self.benchmark_memory_bandwidth(),
                'compute_throughput': self.benchmark_compute_throughput()
            }
        }

        if save_results:
            # Create GPU-specific filename with GPU index
            gpu_name_safe = self.gpu_name.replace(' ', '_').replace('/', '-')
            filename = f"benchmark_GPU{self.gpu_id}_{gpu_name_safe}_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(all_results, f, indent=2)
            print(f"\nResults saved to: {filename}")

        return all_results

def main():
    parser = argparse.ArgumentParser(description='GPU Performance Benchmarking Tool')
    parser.add_argument('--test', choices=['matmul', 'memory', 'compute', 'all'], default='all',
                        help='Benchmark type (default: all)')
    parser.add_argument('--save', action='store_true', help='Save results to JSON file')
    parser.add_argument('--gpu', type=int, default=0, help='GPU ID to benchmark (default: 0)')

    args = parser.parse_args()

    benchmark = GPUBenchmark(gpu_id=args.gpu)

    if args.test == 'all':
        benchmark.run_full_benchmark(save_results=args.save)
    elif args.test == 'matmul':
        benchmark.benchmark_matmul()
    elif args.test == 'memory':
        benchmark.benchmark_memory_bandwidth()
    elif args.test == 'compute':
        benchmark.benchmark_compute_throughput()

if __name__ == "__main__":
    main()
