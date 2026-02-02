#!/usr/bin/env python3
"""
GPU Benchmark History Tool
Tracks benchmark results by GPU UUID across machines and slots
"""
import json
import glob
import argparse
from datetime import datetime
from pathlib import Path


def load_benchmarks(results_dir: str = None) -> list:
    """Load all benchmark JSON files"""
    if results_dir is None:
        script_dir = Path(__file__).parent
        results_dir = script_dir.parent / "results"

    benchmarks = []
    for f in glob.glob(str(results_dir / "benchmark*.json")):
        if "comparison" in f or "results_2026" in f:
            continue
        try:
            with open(f) as fp:
                data = json.load(fp)
                data['_file'] = Path(f).name
                benchmarks.append(data)
        except Exception as e:
            print(f"Warning: Could not load {f}: {e}")

    return benchmarks


def get_matmul_gflops(bench: dict, size: int = 8192) -> float:
    """Extract matmul GFLOPS for given size"""
    matmul = bench.get('benchmark_results', {}).get('matmul', [])
    for m in matmul:
        if m.get('size') == size:
            return m.get('gflops', 0)
    return 0


def get_memory_bandwidth(bench: dict, size_mb: int = 1000) -> tuple:
    """Extract H2D and D2H bandwidth for given size"""
    mem = bench.get('benchmark_results', {}).get('memory_bandwidth', [])
    for m in mem:
        if m.get('size_mb') == size_mb:
            return m.get('h2d_bandwidth_gbps', 0), m.get('d2h_bandwidth_gbps', 0)
    return 0, 0


def group_by_uuid(benchmarks: list) -> dict:
    """Group benchmarks by GPU UUID (or by GPU name if UUID not available)"""
    by_uuid = {}
    for b in benchmarks:
        uuid = b.get('gpu_info', {}).get('uuid')
        gpu_name = b.get('gpu_info', {}).get('name', 'Unknown')

        # If no UUID, use GPU name as fallback key
        if not uuid:
            key = f"no-uuid:{gpu_name}"
        else:
            key = uuid

        if key not in by_uuid:
            by_uuid[key] = []
        by_uuid[key].append(b)

    # Sort each group by date
    for uuid in by_uuid:
        by_uuid[uuid].sort(key=lambda x: x.get('test_metadata', {}).get('timestamp', ''))

    return by_uuid


def print_history(benchmarks: list, uuid_filter: str = None):
    """Print benchmark history, optionally filtered by UUID"""
    by_uuid = group_by_uuid(benchmarks)

    # Filter if requested
    if uuid_filter:
        filtered = {}
        for uuid, benches in by_uuid.items():
            if uuid_filter.lower() in uuid.lower():
                filtered[uuid] = benches
        by_uuid = filtered
        if not by_uuid:
            print(f"No benchmarks found matching UUID: {uuid_filter}")
            return

    print("=" * 100)
    print("GPU BENCHMARK HISTORY BY UUID")
    print("=" * 100)

    for uuid, benches in sorted(by_uuid.items()):
        gpu_name = benches[0].get('gpu_info', {}).get('name', 'Unknown')
        print(f"\n{'─' * 100}")
        print(f"GPU: {gpu_name}")
        if uuid.startswith("no-uuid:"):
            print(f"UUID: (not recorded)")
        else:
            print(f"UUID: {uuid}")
        print(f"Benchmarks: {len(benches)}")
        print(f"{'─' * 100}")

        print(f"\n{'Date':<12} {'Time':<10} {'MatMul 8K':<12} {'MatMul 4K':<12} {'H2D GB/s':<10} {'Backend':<15} {'File':<30}")
        print("-" * 100)

        for b in benches:
            meta = b.get('test_metadata', {})
            date = meta.get('date', 'Unknown')
            time = meta.get('time', 'Unknown')

            gf8k = get_matmul_gflops(b, 8192)
            gf4k = get_matmul_gflops(b, 4096)
            h2d, _ = get_memory_bandwidth(b, 1000)

            backend = meta.get('compute_backend', 'unknown')
            version = meta.get('cuda_version') or meta.get('rocm_version') or ''
            backend_str = f"{backend} {version}".strip()[:15]

            gf8k_str = f"{gf8k:.0f}" if gf8k else "N/A"
            gf4k_str = f"{gf4k:.0f}" if gf4k else "N/A"
            h2d_str = f"{h2d:.1f}" if h2d else "N/A"

            print(f"{date:<12} {time:<10} {gf8k_str:<12} {gf4k_str:<12} {h2d_str:<10} {backend_str:<15} {b['_file'][:30]:<30}")

        # Show performance trend if multiple benchmarks
        if len(benches) > 1:
            gflops_values = [get_matmul_gflops(b, 8192) for b in benches if get_matmul_gflops(b, 8192) > 0]
            if len(gflops_values) > 1:
                first, last = gflops_values[0], gflops_values[-1]
                change = ((last - first) / first) * 100
                trend = "↑" if change > 1 else "↓" if change < -1 else "→"
                print(f"\nPerformance trend: {first:.0f} → {last:.0f} GFLOPS ({change:+.1f}% {trend})")

    print("\n" + "=" * 100)


def print_summary(benchmarks: list):
    """Print summary of all unique GPUs"""
    by_uuid = group_by_uuid(benchmarks)

    print("\n" + "=" * 80)
    print("GPU SUMMARY (Best result per card)")
    print("=" * 80)

    summaries = []
    for uuid, benches in by_uuid.items():
        gpu_name = benches[0].get('gpu_info', {}).get('name', 'Unknown')
        best_gflops = max(get_matmul_gflops(b, 8192) for b in benches)
        if best_gflops == 0:
            best_gflops = max(get_matmul_gflops(b, 4096) for b in benches)
        vram = benches[0].get('gpu_info', {}).get('total_memory_gb', 0)

        summaries.append({
            'uuid': uuid,
            'name': gpu_name,
            'gflops': best_gflops,
            'vram': vram,
            'count': len(benches)
        })

    summaries.sort(key=lambda x: x['gflops'], reverse=True)

    print(f"\n{'Rank':<6} {'GPU':<35} {'UUID':<20} {'GFLOPS':<12} {'VRAM':<10} {'Tests':<6}")
    print("-" * 80)

    for i, s in enumerate(summaries, 1):
        uuid_short = s['uuid'][:18] + "..." if len(s['uuid']) > 20 else s['uuid']
        gf = f"{s['gflops']:.0f}" if s['gflops'] else "N/A"
        vram = f"{s['vram']:.1f} GB" if s['vram'] else "N/A"
        print(f"{i:<6} {s['name'][:33]:<35} {uuid_short:<20} {gf:<12} {vram:<10} {s['count']:<6}")

    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description='GPU Benchmark History Tool')
    parser.add_argument('--uuid', type=str, help='Filter by UUID (partial match)')
    parser.add_argument('--summary', action='store_true', help='Show summary only')
    parser.add_argument('--results-dir', type=str, help='Path to results directory')

    args = parser.parse_args()

    benchmarks = load_benchmarks(args.results_dir)

    if not benchmarks:
        print("No benchmark files found")
        return 1

    if args.summary:
        print_summary(benchmarks)
    else:
        print_history(benchmarks, args.uuid)
        print_summary(benchmarks)

    return 0


if __name__ == "__main__":
    exit(main())
