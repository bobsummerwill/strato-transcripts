#!/usr/bin/env python3
"""
Context Window Limit Testing Tool (OpenRouter Edition)
=======================================================
Tests actual context window limits for AI providers via OpenRouter.

All post-processing providers are accessed through OpenRouter with a single API key.

PROVIDER MATRIX (3 POST-PROCESSING PROVIDERS via OpenRouter):
- opus: Claude Opus 4.6 - 1M context, 128K output
- gemini: Gemini 3.1 Pro - 1M context, 64K output
- grok: Grok 4 - 256K context

TRANSCRIPTION PROVIDERS (ASR + DIARIZATION - no context limits):
- WhisperX (local GPU/CPU), WhisperX-Cloud (Replicate), AssemblyAI

USAGE:
    python3 scripts/test_context_limits.py --providers opus,gemini,grok
    python3 scripts/test_context_limits.py --providers all
"""

import os
import sys
import argparse
import time
from pathlib import Path

# ANSI colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}{text}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.RESET}\n")

def print_success(text):
    print(f"{Colors.GREEN}✓{Colors.RESET} {text}")

def print_failure(text):
    print(f"{Colors.RED}✗{Colors.RESET} {text}")

def print_info(text):
    print(f"{Colors.BLUE}ℹ{Colors.RESET} {text}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠{Colors.RESET} {text}")


# OpenRouter model mapping and context limits
OPENROUTER_MODELS = {
    'opus': {
        'model_id': 'anthropic/claude-opus-4.6',
        'display_name': 'Claude Opus 4.6',
        'provider': 'Anthropic',
        'advertised': '1,000,000 tokens',
        'test_sizes': [10000, 50000, 100000, 200000, 500000, 1000000],
    },
    'gemini': {
        'model_id': 'google/gemini-3.1-pro-preview',
        'display_name': 'Gemini 3.1 Pro',
        'provider': 'Google',
        'advertised': '1,000,000 tokens',
        'test_sizes': [10000, 50000, 100000, 200000, 500000, 1000000],
    },
    'grok': {
        'model_id': 'x-ai/grok-4',
        'display_name': 'Grok 4',
        'provider': 'xAI',
        'advertised': '256,000 tokens',
        'test_sizes': [10000, 50000, 100000, 150000, 200000, 256000],
    },
    'qwen': {
        'model_id': 'qwen/qwen3.5-plus-02-15',
        'display_name': 'Qwen3.5 Plus',
        'provider': 'Alibaba',
        'advertised': '1,000,000 tokens',
        'test_sizes': [10000, 50000, 100000, 200000, 500000, 1000000],
    },
}

# Model quality priority for recommendations
MODEL_PRIORITY = {
    'anthropic/claude-opus-4.6': 100,
    'x-ai/grok-4': 95,
    'google/gemini-3.1-pro-preview': 90,
    'qwen/qwen3.5-plus-02-15': 85,
}


# ============================================================================
# Token Counting
# ============================================================================

def count_tokens_tiktoken(text, model="gpt-4"):
    """Count tokens using tiktoken (OpenAI's tokenizer)"""
    try:
        import tiktoken
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except ImportError:
        print_warning("tiktoken not installed, using rough estimate")
        return int(len(text.split()) * 1.3)
    except Exception as e:
        print_warning(f"tiktoken error: {e}, using rough estimate")
        return int(len(text.split()) * 1.3)


def generate_test_payload(target_tokens, model="gpt-4"):
    """Generate text payload of approximately target_tokens size"""
    base_text = """The quick brown fox jumps over the lazy dog. This is a test of the context
window limits for various AI language models. We are testing to determine the actual usable
token limits versus advertised specifications. Understanding these limits helps optimize
prompt engineering and determine when chunking strategies are necessary for long documents.
"""

    current_text = ""
    current_tokens = 0
    counter = 0

    while current_tokens < target_tokens:
        chunk = f"\n[Section {counter}] {base_text}"
        current_text += chunk
        current_tokens = count_tokens_tiktoken(current_text, model)
        counter += 1

    return current_text, current_tokens


# ============================================================================
# OpenRouter Testing
# ============================================================================

def test_openrouter_context(api_key, processor_name):
    """Test context limits for a model via OpenRouter."""
    try:
        import openai
    except ImportError:
        return {"error": "openai package not installed", "status": "skip"}

    config = OPENROUTER_MODELS.get(processor_name)
    if not config:
        return {"error": f"Unknown processor: {processor_name}", "status": "skip"}

    model_id = config['model_id']
    display_name = config['display_name']
    provider = config['provider']
    test_sizes = config['test_sizes']

    print_info(f"Testing {display_name} ({model_id}) via OpenRouter...")

    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )

    results = {
        "provider": provider,
        "model": model_id,
        "display_name": display_name,
        "advertised": config['advertised'],
        "tested": [],
        "max_working": 0,
        "status": "tested"
    }

    for size in test_sizes:
        print(f"  Testing {size:,} tokens...", end=" ", flush=True)
        payload, actual_tokens = generate_test_payload(size, "gpt-4")

        try:
            start = time.time()
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"{payload}\n\nRespond with just: OK"}
                ],
                max_tokens=50,
                temperature=0.1,
                extra_headers={
                    "HTTP-Referer": "https://github.com/strato-net/strato-transcripts",
                    "X-Title": "Strato Transcripts Context Test"
                }
            )
            elapsed = time.time() - start

            print_success(f"{actual_tokens:,} tokens OK ({elapsed:.1f}s)")
            results["tested"].append({
                "target": size,
                "actual": actual_tokens,
                "success": True,
                "time": elapsed
            })
            results["max_working"] = actual_tokens
            time.sleep(1)  # Rate limit courtesy

        except Exception as e:
            error_msg = str(e)
            if 'model_not_found' in error_msg.lower() or 'does not exist' in error_msg.lower():
                return {"error": f"{display_name} not available via OpenRouter", "status": "skip"}
            print_failure(f"Failed - {error_msg[:100]}")
            results["tested"].append({
                "target": size,
                "actual": actual_tokens,
                "success": False,
                "error": error_msg[:200]
            })
            break  # Stop at first failure

    return results


# ============================================================================
# Report Generation
# ============================================================================

def generate_report(all_results):
    """Generate comprehensive test report"""
    report = []
    report.append("="*70)
    report.append("AI PROVIDER CONTEXT WINDOW TEST RESULTS (via OpenRouter)")
    report.append("="*70)
    report.append(f"\nTest Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"\nFor typical 60-90 minute transcripts:")
    report.append("  Estimated tokens: 20,000 - 40,000 tokens")
    report.append("  Plus system prompts: ~5,000 tokens")
    report.append("  Total needed: ~45,000 tokens maximum")
    report.append("\n" + "="*70 + "\n")

    for result in all_results:
        if result["status"] == "skip":
            report.append(f"\n{result.get('provider', 'Unknown')}: SKIPPED")
            report.append(f"  Reason: {result['error']}")
            continue

        report.append(f"\n{result['provider']}: {result.get('display_name', result['model'])}")
        report.append(f"  Model: {result['model']}")
        report.append(f"  Advertised: {result['advertised']}")
        report.append(f"  Maximum Tested: {result['max_working']:,} tokens")

        # Calculate recommended safe limit (5% buffer)
        safe_limit = int(result['max_working'] * 0.95)
        report.append(f"  Recommended Safe Limit: {safe_limit:,} tokens (with 5% buffer)")

        # Determine if chunking needed
        if result['max_working'] >= 50000:
            report.append(f"  Chunking Needed: NO - Perfect for your transcripts!")
        elif result['max_working'] >= 45000:
            report.append(f"  Chunking Needed: BORDERLINE - Should work but close")
        else:
            report.append(f"  Chunking Needed: YES - Transcripts may need splitting")

        # Test details
        report.append("\n  Test Results:")
        for test in result['tested']:
            if test['success']:
                report.append(f"    ✓ {test['actual']:,} tokens - OK ({test['time']:.1f}s)")
            else:
                report.append(f"    ✗ {test['actual']:,} tokens - FAILED")

    report.append("\n" + "="*70)
    report.append("\nRECOMMENDATIONS FOR YOUR TRANSCRIPTS:")
    report.append("="*70)

    # Find best provider
    best_providers = [r for r in all_results if r['status'] == 'tested' and r['max_working'] >= 50000]
    if best_providers:
        best = max(best_providers, key=lambda x: (x['max_working'], MODEL_PRIORITY.get(x['model'], 0)))
        report.append(f"\nBEST CHOICE: {best['provider']} ({best.get('display_name', best['model'])})")
        report.append(f"  Context: {best['max_working']:,} tokens")
        report.append(f"  Perfect for your transcripts without chunking")
        report.append(f"  Maintains full context for best quality")

        # Alternative providers
        alternatives = [r for r in all_results if r['status'] == 'tested' and r['max_working'] >= 45000 and r['provider'] != best['provider']]
        if alternatives:
            report.append("\nALTERNATIVES:")
            for alt in sorted(alternatives, key=lambda x: -x['max_working']):
                report.append(f"  - {alt['provider']} ({alt.get('display_name', alt['model'])}): {alt['max_working']:,} tokens")

    # Chunking required
    chunking_needed = [r for r in all_results if r['status'] == 'tested' and r['max_working'] < 45000]
    if chunking_needed:
        report.append("\nREQUIRE CHUNKING (not ideal for quality):")
        for cn in chunking_needed:
            report.append(f"  - {cn['provider']}: {cn['max_working']:,} tokens")

    return "\n".join(report)


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Test context window limits for AI providers via OpenRouter"
    )
    parser.add_argument(
        "--providers",
        default="opus,gemini,grok",
        help="Comma-separated list of providers to test (opus,gemini,grok) or 'all'"
    )
    parser.add_argument(
        "--output",
        default="intermediates/context_limits_report.txt",
        help="Output file for results"
    )

    args = parser.parse_args()

    print_header("AI Context Window Limit Testing (via OpenRouter)")
    print_info("All providers accessed through OpenRouter with single API key")
    print_info("Estimated cost: ~$0.01-0.10 total")
    print()

    # Check OpenRouter API key
    api_key = os.environ.get('OPENROUTER_API_KEY')
    if not api_key:
        print_failure("OPENROUTER_API_KEY not set")
        print_info("Get your API key from: https://openrouter.ai/keys")
        sys.exit(1)

    print_success("OpenRouter API key found")
    print()

    # Parse providers
    if args.providers.lower() == 'all':
        providers = list(OPENROUTER_MODELS.keys())
    else:
        providers = [p.strip() for p in args.providers.split(',')]

    # Validate providers
    valid_providers = set(OPENROUTER_MODELS.keys())
    for p in providers:
        if p not in valid_providers:
            print_warning(f"Unknown provider: {p}")
            print_info(f"Valid providers: {', '.join(sorted(valid_providers))}")
            providers.remove(p)

    if not providers:
        print_failure("No valid providers to test")
        sys.exit(1)

    print_info(f"Testing {len(providers)} provider(s): {', '.join(providers)}")
    print()

    # Test each provider
    all_results = []
    for provider in providers:
        result = test_openrouter_context(api_key, provider)
        all_results.append(result)
        print()

    # Generate report
    print_header("Generating Report")
    report = generate_report(all_results)

    # Save to file
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(report)

    print_success(f"Report saved to: {output_path}")
    print()

    # Display report
    print(report)


if __name__ == "__main__":
    main()
