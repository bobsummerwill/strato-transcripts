#!/usr/bin/env python3
"""
Context Window Limit Testing Tool
==================================
Tests actual context window limits for AI providers to determine:
- Real usable token limits
- Whether chunking is needed
- Optimal prompt sizes for quality

COMPLETE PROVIDER MATRIX:

POST-PROCESSING PROVIDERS (AI TEXT CORRECTION):
- Opus (Claude Opus 4.5 via Anthropic) - PREMIUM REASONING, 150K context
- Sonnet (Claude Sonnet 4.5 via Anthropic) - BALANCED QUALITY, 150K context
- Gemini (Gemini 3.0 Pro via Google) - TECHNICAL EXCELLENCE, 128K context
- DeepSeek (DeepSeek-V3.2 via DeepSeek) - COST-EFFECTIVE, 128K context

TRANSCRIPTION PROVIDERS (ASR + DIARIZATION):
- WhisperX (local GPU/CPU) - NO context limit, FREE, processes audio directly
- WhisperX-Cloud (Replicate) - NO context limit, $2.88/hr, 2-3 min
- AssemblyAI (cloud) - NO context limit, $1.08/hr, 3-4 min

USAGE EXAMPLES:
Test all major providers:
    python3 scripts/test_context_limits.py --providers sonnet,opus,gemini,deepseek

Test specific model:
    python3 scripts/test_context_limits.py --providers opus

Post-processing providers listed above do have context limits.
Transcription (ASR) providers have no context limits since they process audio.
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
        return len(text.split()) * 1.3  # Rough estimate
    except Exception as e:
        print_warning(f"tiktoken error: {e}, using rough estimate")
        return len(text.split()) * 1.3


def generate_test_payload(target_tokens, model="gpt-4"):
    """Generate text payload of approximately target_tokens size"""
    # Use repetitive but varied text to avoid compression
    base_text = """The quick brown fox jumps over the lazy dog. This is a test of the context
window limits for various AI language models. We are testing to determine the actual usable
token limits versus advertised specifications. Understanding these limits helps optimize
prompt engineering and determine when chunking strategies are necessary for long documents.
"""

    # Repeat until we reach target
    current_text = ""
    current_tokens = 0

    counter = 0
    while current_tokens < target_tokens:
        # Add variation to prevent compression
        chunk = f"\n[Section {counter}] {base_text}"
        current_text += chunk
        current_tokens = count_tokens_tiktoken(current_text, model)
        counter += 1

    return current_text, current_tokens


# ============================================================================
# Provider Testing Functions
# ============================================================================

def test_anthropic_context(test_sizes=[10000, 50000, 100000, 150000, 190000, 200000]):
    """Test Claude Sonnet 4.5 context limits"""
    try:
        import anthropic
    except ImportError:
        return {"error": "anthropic package not installed", "status": "skip"}

    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        return {"error": "ANTHROPIC_API_KEY not set", "status": "skip"}

    print_info("Testing Anthropic Claude Sonnet 4.5...")
    client = anthropic.Anthropic(api_key=api_key)

    results = {
        "provider": "Anthropic",
        "model": "claude-sonnet-4-5-20250929",
        "advertised": "200,000 tokens (standard), 1,000,000 (beta)",
        "tested": [],
        "max_working": 0,
        "status": "tested"
    }

    for size in test_sizes:
        print(f"  Testing {size:,} tokens...", end=" ", flush=True)
        payload, actual_tokens = generate_test_payload(size)

        try:
            start = time.time()
            response = client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=100,
                messages=[{
                    "role": "user",
                    "content": f"{payload}\n\nPlease respond with just: OK"
                }]
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
            print_failure(f"Failed - {error_msg[:100]}")
            results["tested"].append({
                "target": size,
                "actual": actual_tokens,
                "success": False,
                "error": error_msg[:200]
            })
            break  # Stop at first failure

    return results


def test_opus_context(test_sizes=[10000, 50000, 100000, 150000, 190000, 200000]):
    """Test Claude Opus 4.5 context limits"""
    try:
        import anthropic
    except ImportError:
        return {"error": "anthropic package not installed", "status": "skip"}

    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        return {"error": "ANTHROPIC_API_KEY not set", "status": "skip"}

    print_info("Testing Anthropic Claude Opus 4.5...")
    client = anthropic.Anthropic(api_key=api_key)

    results = {
        "provider": "Anthropic",
        "model": "claude-opus-4-5",
        "advertised": "200,000 tokens (advertised)",
        "tested": [],
        "max_working": 0,
        "status": "tested"
    }

    for size in test_sizes:
        print(f"  Testing {size:,} tokens...", end=" ", flush=True)
        payload, actual_tokens = generate_test_payload(size)

        try:
            start = time.time()
            response = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=100,
                messages=[{
                    "role": "user",
                    "content": f"{payload}\n\nPlease respond with just: OK"
                }]
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
                return {"error": "Claude Opus 4.5 model not available", "status": "skip"}
            print_failure(f"Failed - {error_msg[:100]}")
            results["tested"].append({
                "target": size,
                "actual": actual_tokens,
                "success": False,
                "error": error_msg[:200]
            })
            break  # Stop at first failure

    return results


def test_gemini_context(test_sizes=[10000, 50000, 100000, 120000, 128000]):
    """Test Gemini 3.0 Pro context limits"""
    try:
        import google.generativeai as genai
    except ImportError:
        return {"error": "google-generativeai package not installed", "status": "skip"}

    api_key = os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        return {"error": "GOOGLE_API_KEY not set", "status": "skip"}

    print_info("Testing Google Gemini 3.0 Pro...")
    genai.configure(api_key=api_key)

    results = {
        "provider": "Google",
        "model": "gemini-3.0-pro",
        "advertised": "128,000 tokens (some claim 1M)",
        "tested": [],
        "max_working": 0,
        "status": "tested"
    }

    model = genai.GenerativeModel('models/gemini-3-pro-preview')

    for size in test_sizes:
        print(f"  Testing {size:,} tokens...", end=" ", flush=True)
        payload, actual_tokens = generate_test_payload(size)

        try:
            start = time.time()
            response = model.generate_content(
                f"{payload}\n\nRespond with just: OK",
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=50,
                )
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
            time.sleep(1)

        except Exception as e:
            error_msg = str(e)
            print_failure(f"Failed - {error_msg[:100]}")
            results["tested"].append({
                "target": size,
                "actual": actual_tokens,
                "success": False,
                "error": error_msg[:200]
            })
            break

    return results


def test_deepseek_context(test_sizes=[10000, 50000, 100000, 120000, 128000]):
    """Test DeepSeek V3.2 context limits"""
    try:
        import openai
    except ImportError:
        return {"error": "openai package not installed", "status": "skip"}

    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key:
        return {"error": "DEEPSEEK_API_KEY not set", "status": "skip"}

    print_info("Testing DeepSeek V3.2...")
    client = openai.OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    results = {
        "provider": "DeepSeek",
        "model": "deepseek-chat",
        "advertised": "128,000 tokens",
        "tested": [],
        "max_working": 0,
        "status": "tested"
    }

    for size in test_sizes:
        print(f"  Testing {size:,} tokens...", end=" ", flush=True)
        payload, actual_tokens = generate_test_payload(size, "gpt-4")  # Use GPT-4 tokenizer approximation

        try:
            start = time.time()
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"{payload}\n\nRespond with just: OK"}
                ],
                max_tokens=50,
                temperature=0.1
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
            time.sleep(1)

        except Exception as e:
            error_msg = str(e)
            print_failure(f"Failed - {error_msg[:100]}")
            results["tested"].append({
                "target": size,
                "actual": actual_tokens,
                "success": False,
                "error": error_msg[:200]
            })
            break

    return results


# ============================================================================
# Report Generation
# ============================================================================

def generate_report(all_results):
    """Generate comprehensive test report"""
    report = []
    report.append("="*70)
    report.append("AI PROVIDER CONTEXT WINDOW TEST RESULTS")
    report.append("="*70)
    report.append(f"\nTest Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"\nFor typical 60-90 minute transcripts:")
    report.append("  Estimated tokens: 20,000 - 40,000 tokens")
    report.append("  Plus system prompts: ~5,000 tokens")
    report.append("  Total needed: ~45,000 tokens maximum")
    report.append("\n" + "="*70 + "\n")

    for result in all_results:
        if result["status"] == "skip":
            report.append(f"\n{result['provider']}: SKIPPED")
            report.append(f"  Reason: {result['error']}")
            continue

        report.append(f"\n{result['provider']}: {result['model']}")
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

        # Special notes
        if 'beta_access' in result:
            if result['beta_access']:
                report.append("\n  🎉 EXTENDED CONTEXT: 1M token beta access available!")
            else:
                report.append("\n  ℹ Extended context (1M tokens) not available on your tier")

    report.append("\n" + "="*70)
    report.append("\nRECOMMENDATIONS FOR YOUR TRANSCRIPTS:")
    report.append("="*70)

    # Find best provider
    best_providers = [r for r in all_results if r['status'] == 'tested' and r['max_working'] >= 50000]
    if best_providers:
        best = max(best_providers, key=lambda x: x['max_working'])
        report.append(f"\nBEST CHOICE: {best['provider']} ({best['model']})")
        report.append(f"  Context: {best['max_working']:,} tokens")
        report.append(f"  Perfect for your transcripts without chunking")
        report.append(f"  Maintains full context for best quality")

    # Alternative providers
    alternatives = [r for r in all_results if r['status'] == 'tested' and r['max_working'] >= 45000 and r['provider'] != (best['provider'] if best_providers else None)]
    if alternatives:
        report.append("\nALTERNATIVES:")
        for alt in alternatives:
            report.append(f"  - {alt['provider']}: {alt['max_working']:,} tokens")

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
        description="Test context window limits for AI providers"
    )
    parser.add_argument(
        "--providers",
        default="sonnet,opus,gemini,deepseek",
        help="Comma-separated list of providers to test (sonnet,opus,gemini,deepseek)"
    )
    parser.add_argument(
        "--output",
        default="intermediates/context_limits_report.txt",
        help="Output file for results"
    )

    args = parser.parse_args()

    print_header("AI Context Window Limit Testing")
    print_info("Testing all providers with real API calls")
    print_info("Estimated cost: ~$0.01-0.05 total")
    print()

    providers = [p.strip() for p in args.providers.split(',')]
    all_results = []

    # Test each provider
    for provider in providers:
        if provider == 'sonnet':
            result = test_anthropic_context()
        elif provider == 'opus':
            result = test_opus_context()
        elif provider == 'gemini':
            result = test_gemini_context()
        elif provider == 'deepseek':
            result = test_deepseek_context()
        else:
            print_warning(f"Unknown provider: {provider}")
            print_info(f"Valid providers: sonnet, opus, gemini, deepseek")
            continue

        all_results.append(result)
        print()

    # Generate report
    print_header("Generating Report")
    report = generate_report(all_results)

    # Save to file
    output_path = Path(args.output)
    with open(output_path, 'w') as f:
        f.write(report)

    print_success(f"Report saved to: {output_path}")
    print()

    # Display report
    print(report)


if __name__ == "__main__":
    main()
