#!/usr/bin/env python3
"""
Context Window Limit Testing Tool
==================================
Tests actual context window limits for AI providers to determine:
- Real usable token limits
- Whether chunking is needed
- Optimal prompt sizes for quality

POST-PROCESSING PROVIDERS TESTED:
- Anthropic (Claude Sonnet 4.5)
- OpenAI (GPT-4o)
- Google (Gemini 2.5 Pro)
- DeepSeek (Chat)
- Ollama (qwen2.5:32b local)

TRANSCRIPTION PROVIDERS (audio length limits, not context windows):
- WhisperX (local GPU) - No length limit
- Kimi-Audio (local GPU) - No length limit
- AssemblyAI (cloud) - No length limit
- Deepgram (cloud) - No length limit
- Sonix (cloud) - No length limit
- Speechmatics (cloud) - No length limit
- Novita AI (cloud) - No length limit
- OpenAI Whisper (cloud) - 25 MB file size limit

Usage:
    python3 scripts/test_context_limits.py
    python3 scripts/test_context_limits.py --providers anthropic,openai,deepseek
    python3 scripts/test_context_limits.py --quick  # Fast test with smaller increments
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
    
    # Test for 1M token access (beta)
    if results["max_working"] >= 190000:
        print_info("Testing for 1M token beta access...")
        try:
            payload, actual_tokens = generate_test_payload(500000)
            response = client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=100,
                messages=[{
                    "role": "user",
                    "content": f"{payload}\n\nRespond with: OK"
                }],
                extra_headers={"anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"}
            )
            print_success(f"1M token beta access: AVAILABLE")
            results["beta_access"] = True
        except Exception as e:
            print_info(f"1M token beta access: Not available ({str(e)[:50]})")
            results["beta_access"] = False
    
    return results


def test_openai_context(test_sizes=[10000, 50000, 100000, 120000, 128000]):
    """Test GPT-4o context limits"""
    try:
        import openai
    except ImportError:
        return {"error": "openai package not installed", "status": "skip"}
    
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        return {"error": "OPENAI_API_KEY not set", "status": "skip"}
    
    print_info("Testing OpenAI GPT-4o...")
    client = openai.OpenAI(api_key=api_key)
    
    results = {
        "provider": "OpenAI",
        "model": "gpt-4o-2025-08-06",
        "advertised": "128,000 tokens",
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
                model="gpt-4o-2025-08-06",
                max_tokens=50,
                messages=[{
                    "role": "user",
                    "content": f"{payload}\n\nRespond with just: OK"
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


def test_gemini_context(test_sizes=[10000, 50000, 100000, 120000, 128000]):
    """Test Gemini 2.5 Pro context limits"""
    try:
        import google.generativeai as genai
    except ImportError:
        return {"error": "google-generativeai package not installed", "status": "skip"}
    
    api_key = os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        return {"error": "GOOGLE_API_KEY not set", "status": "skip"}
    
    print_info("Testing Google Gemini 2.5 Pro...")
    genai.configure(api_key=api_key)
    
    results = {
        "provider": "Google",
        "model": "gemini-2.0-flash-exp",
        "advertised": "128,000 tokens (some claim 1M)",
        "tested": [],
        "max_working": 0,
        "status": "tested"
    }
    
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
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


def test_deepseek_context(test_sizes=[10000, 30000, 50000, 64000]):
    """Test DeepSeek context limits"""
    try:
        import openai
    except ImportError:
        return {"error": "openai package not installed", "status": "skip"}
    
    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key:
        return {"error": "DEEPSEEK_API_KEY not set", "status": "skip"}
    
    print_info("Testing DeepSeek Chat...")
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )
    
    results = {
        "provider": "DeepSeek",
        "model": "deepseek-chat",
        "advertised": "64,000 tokens",
        "tested": [],
        "max_working": 0,
        "status": "tested"
    }
    
    for size in test_sizes:
        print(f"  Testing {size:,} tokens...", end=" ", flush=True)
        payload, actual_tokens = generate_test_payload(size)
        
        try:
            start = time.time()
            response = client.chat.completions.create(
                model="deepseek-chat",
                max_tokens=50,
                messages=[{
                    "role": "user",
                    "content": f"{payload}\n\nRespond with just: OK"
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


def test_ollama_context(test_sizes=[2000, 4000, 8000, 16000, 32000]):
    """Test Ollama local model context limits"""
    try:
        import requests
    except ImportError:
        return {"error": "requests package not installed", "status": "skip"}
    
    print_info("Testing Ollama (local)...")
    
    results = {
        "provider": "Ollama",
        "model": "qwen2.5:32b",
        "advertised": "32,768 tokens (model dependent)",
        "tested": [],
        "max_working": 0,
        "status": "tested"
    }
    
    # Check if Ollama is running
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code != 200:
            return {"error": "Ollama not running", "status": "skip"}
    except Exception:
        return {"error": "Ollama not accessible at localhost:11434", "status": "skip"}
    
    for size in test_sizes:
        print(f"  Testing {size:,} tokens...", end=" ", flush=True)
        payload, actual_tokens = generate_test_payload(size)
        
        try:
            start = time.time()
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "qwen2.5:32b",
                    "prompt": f"{payload}\n\nRespond with just: OK",
                    "stream": False,
                    "options": {
                        "num_predict": 10
                    }
                },
                timeout=60
            )
            elapsed = time.time() - start
            
            if response.status_code == 200:
                print_success(f"{actual_tokens:,} tokens OK ({elapsed:.1f}s)")
                results["tested"].append({
                    "target": size,
                    "actual": actual_tokens,
                    "success": True,
                    "time": elapsed
                })
                results["max_working"] = actual_tokens
            else:
                raise Exception(f"HTTP {response.status_code}")
            
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
        default="anthropic,openai,gemini,deepseek,ollama",
        help="Comma-separated list of providers to test"
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Quick test with smaller increments"
    )
    parser.add_argument(
        "--output",
        default="context_limits_report.txt",
        help="Output file for results"
    )
    
    args = parser.parse_args()
    
    print_header("AI Context Window Limit Testing")
    print_info("This will make real API calls to test limits")
    print_info("Costs should be minimal (~$0.01-0.05 total)")
    print()
    
    # Get confirmation
    response = input(f"{Colors.YELLOW}Continue? (y/n): {Colors.RESET}")
    if response.lower() != 'y':
        print("Cancelled.")
        sys.exit(0)
    
    providers = [p.strip() for p in args.providers.split(',')]
    all_results = []
    
    # Test each provider
    for provider in providers:
        if provider == 'anthropic':
            result = test_anthropic_context()
        elif provider == 'openai':
            result = test_openai_context()
        elif provider == 'gemini':
            result = test_gemini_context()
        elif provider == 'deepseek':
            result = test_deepseek_context()
        elif provider == 'ollama':
            result = test_ollama_context()
        else:
            print_warning(f"Unknown provider: {provider}")
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
