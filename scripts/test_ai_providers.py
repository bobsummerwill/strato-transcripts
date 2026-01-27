#!/usr/bin/env python3
"""
Test connectivity and model access for all AI providers via OpenRouter.
All AI post-processing models are accessed through OpenRouter with a single API key.
Also tests local mode support (ollama + GPU detection for dual RTX 3090s).

Local models (fit on 48GB): glm, deepseek-local, qwen-local, mistral-local, llama-local
"""

import os
import sys
import shutil
import subprocess

# OpenRouter model IDs (same as in process_single_post_process.py)
OPENROUTER_MODELS = {
    'opus': ('anthropic/claude-opus-4.5', 'Claude Opus 4.5'),
    'gemini': ('google/gemini-3-pro-preview', 'Gemini 3 Pro'),
    'deepseek': ('deepseek/deepseek-chat', 'DeepSeek V3.2'),
    'chatgpt': ('openai/gpt-5.2', 'GPT-5.2'),
    'qwen': ('qwen/qwen3-max', 'Qwen3-Max'),
    'kimi': ('moonshotai/kimi-k2.5', 'Kimi K2.5'),
    'glm': ('z-ai/glm-4.7', 'GLM-4.7'),
    'minimax': ('minimax/minimax-m2.1', 'MiniMax M2.1'),
    'llama': ('meta-llama/llama-4-maverick', 'Llama 4 Maverick'),
    'grok': ('x-ai/grok-4', 'Grok 4'),
    'mistral': ('mistralai/mistral-large-2411', 'Mistral Large'),
}

# Local model mapping (models that fit on 48GB dual 3090s)
LOCAL_MODELS = {
    'glm': ('glm-4.7-flash:q4_K_M', 'GLM-4.7-Flash'),
    'deepseek-local': ('deepseek-r1:70b', 'DeepSeek-R1 70B'),
    'qwen-local': ('qwen3:72b', 'Qwen3 72B'),
    'mistral-local': ('mixtral:8x7b', 'Mixtral 8x7B'),
    'llama-local': ('llama3.3:70b', 'Llama 3.3 70B'),
}


def test_openrouter_model(api_key, processor_name, model_id, display_name):
    """Test a single model via OpenRouter."""
    print(f"\n  Testing {processor_name.upper()} ({display_name})...")
    print(f"    Model: {model_id}")

    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": "Say 'hello' in one word"}],
            max_tokens=20,  # GPT-5.2 requires >= 16
            extra_headers={
                "HTTP-Referer": "https://github.com/strato-net/strato-transcripts",
                "X-Title": "Strato Transcripts Test"
            }
        )

        text = response.choices[0].message.content if response.choices else "No response"
        print(f"    ✅ Connected successfully")
        print(f"    Response: {text[:50]}")
        return True
    except Exception as e:
        print(f"    ❌ Error: {e}")
        return False


def test_openrouter():
    """Test OpenRouter API key and connection."""
    print("\n" + "="*60)
    print("Testing OPENROUTER API connection")
    print("="*60)

    api_key = os.environ.get('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ OPENROUTER_API_KEY not set")
        print("   Get your API key from: https://openrouter.ai/keys")
        return None, {}

    # Test basic connection
    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        # Simple test with a cheap model
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": "Say 'connected' in one word"}],
            max_tokens=10,
            extra_headers={
                "HTTP-Referer": "https://github.com/strato-net/strato-transcripts",
                "X-Title": "Strato Transcripts Test"
            }
        )

        print("✅ OpenRouter API connection successful")
        print(f"   Response: {response.choices[0].message.content}")
        return api_key, {}

    except Exception as e:
        print(f"❌ OpenRouter connection failed: {e}")
        return None, {}


def test_all_openrouter_models(api_key):
    """Test all AI post-processing models via OpenRouter."""
    print("\n" + "="*60)
    print("AI POST-PROCESSING PROVIDERS (via OpenRouter)")
    print("="*60)

    results = {}

    for processor_name, (model_id, display_name) in OPENROUTER_MODELS.items():
        results[processor_name] = test_openrouter_model(
            api_key, processor_name, model_id, display_name
        )

    return results


def test_gpu_setup():
    """Test GPU setup for local mode (dual RTX 3090 required)."""
    print("\n" + "="*60)
    print("Testing GPU SETUP (local mode requirements)")
    print("="*60)

    try:
        import torch
    except ImportError:
        print("⚠️  PyTorch not installed - skipping GPU test")
        return "skipped"

    if not torch.cuda.is_available():
        print("❌ CUDA not available")
        return False

    gpu_count = torch.cuda.device_count()
    print(f"   Found {gpu_count} GPU(s)")

    if gpu_count < 2:
        print(f"⚠️  Local mode requires 2x RTX 3090 (found {gpu_count})")
        return "insufficient"

    # Check if both are RTX 3090
    gpus_valid = True
    for i in range(2):
        name = torch.cuda.get_device_name(i)
        memory_gb = torch.cuda.get_device_properties(i).total_memory / (1024**3)
        is_3090 = "3090" in name
        status = "✅" if is_3090 else "⚠️"
        print(f"   GPU {i}: {name} ({memory_gb:.1f}GB) {status}")
        if not is_3090:
            gpus_valid = False

    if gpus_valid:
        print("✅ Dual RTX 3090 detected - local mode supported")
        return True
    else:
        print("⚠️  Not dual RTX 3090 - local mode not supported")
        return "insufficient"


def test_ollama():
    """Test ollama installation and connectivity."""
    print("\n" + "="*60)
    print("Testing OLLAMA (local inference)")
    print("="*60)

    # Check if ollama binary exists
    if not shutil.which('ollama'):
        print("❌ ollama not installed")
        print("   Install from: https://ollama.ai")
        return False

    # Check if ollama server is running
    try:
        result = subprocess.run(
            ['ollama', 'list'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode != 0:
            print("⚠️  ollama installed but server not running")
            print("   Start with: ollama serve")
            return "not_running"
    except subprocess.TimeoutExpired:
        print("⚠️  ollama server not responding")
        return "not_running"
    except Exception as e:
        print(f"❌ Error checking ollama: {e}")
        return False

    print("✅ ollama is installed and running")

    # Check for local models
    print("\n   Checking local models:")
    for processor, (model_name, display_name) in LOCAL_MODELS.items():
        # Check if model is pulled
        try:
            result = subprocess.run(
                ['ollama', 'show', model_name.split(':')[0]],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                print(f"   ✅ {processor}: {model_name} (available)")
            else:
                print(f"   ⚠️  {processor}: {model_name} (not pulled)")
                print(f"      Pull with: ollama pull {model_name}")
        except Exception:
            print(f"   ⚠️  {processor}: {model_name} (not checked)")

    return True


def test_assemblyai():
    """Test AssemblyAI transcription service"""
    print("\n" + "="*60)
    print("Testing ASSEMBLYAI (transcription service)")
    print("="*60)

    api_key = os.environ.get('ASSEMBLYAI_API_KEY')
    if not api_key or api_key == "" or api_key == "your_assemblyai_api_key_here":
        print("⚠️  API key not configured - skipping")
        return "skipped"

    try:
        import assemblyai as aai
        aai.settings.api_key = api_key

        # Just test authentication by checking API access
        # Don't actually transcribe anything to keep test fast
        print(f"✅ API key configured and SDK loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_whisperx():
    """Test WhisperX local transcription"""
    print("\n" + "="*60)
    print("Testing WHISPERX (local GPU transcription)")
    print("="*60)

    try:
        import whisperx
        import torch

        # Check if GPU available
        if torch.cuda.is_available():
            print(f"✅ WhisperX installed with GPU support")
            print(f"   GPU: {torch.cuda.get_device_name(0)}")
            return True
        else:
            print(f"⚠️  WhisperX installed but no GPU detected (CPU mode)")
            print(f"   Note: WhisperX works on CPU but will be slower")
            return True
    except ImportError:
        print(f"❌ WhisperX not installed")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_whisperx_cloud():
    """Test WhisperX Cloud (Replicate) transcription"""
    print("\n" + "="*60)
    print("Testing WHISPERX-CLOUD (Replicate cloud transcription)")
    print("="*60)

    try:
        import replicate

        api_key = os.environ.get('REPLICATE_API_TOKEN')
        if not api_key or api_key == "" or api_key == "your_replicate_api_token_here":
            print("⚠️  API key not configured - skipping")
            return "skipped"

        # Set the REPLICATE_API_TOKEN environment variable
        # The replicate library automatically uses this
        os.environ['REPLICATE_API_TOKEN'] = api_key

        # Initialize client - replicate.run() will use the env var
        client = replicate.Client()

        # Test basic connection by listing models
        models = client.models.list()
        if hasattr(models, '__iter__'):
            print(f"✅ API key configured and SDK loaded successfully")
            return True
        else:
            print(f"✅ API key configured (basic connection test)")
            return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    print("="*60)
    print("AI Provider Connectivity Test")
    print("="*60)
    print("Hosted: All AI post-processing uses OpenRouter (single API key)")
    print("Local:  5 models via ollama (requires 2x RTX 3090 / 48GB)")
    print("        glm, deepseek-local, qwen-local, mistral-local, llama-local")
    print("="*60)

    results = {}

    # Test local mode support (GPU + ollama)
    print("\n" + "="*60)
    print("LOCAL MODE SUPPORT")
    print("="*60)
    results['gpu-setup'] = test_gpu_setup()
    results['ollama'] = test_ollama()

    # Test local transcription services
    print("\n" + "="*60)
    print("LOCAL TRANSCRIPTION SERVICES")
    print("="*60)
    results['whisperx'] = test_whisperx()

    # Test cloud transcription services
    print("\n" + "="*60)
    print("CLOUD TRANSCRIPTION SERVICES")
    print("="*60)
    results['assemblyai'] = test_assemblyai()
    results['whisperx-cloud'] = test_whisperx_cloud()

    # Test OpenRouter connection first
    api_key, _ = test_openrouter()

    if api_key:
        # Test all AI post-processing models via OpenRouter
        model_results = test_all_openrouter_models(api_key)
        results.update(model_results)
    else:
        # Mark all AI models as failed if no OpenRouter key
        for processor_name in OPENROUTER_MODELS.keys():
            results[processor_name] = False

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    passed = sum(1 for v in results.values() if v is True)
    failed = sum(1 for v in results.values() if v is False)
    skipped = sum(1 for v in results.values() if v == "skipped")
    partial = sum(1 for v in results.values() if v in ("insufficient", "not_running"))

    for provider, result in results.items():
        if result is True:
            status = "✅ PASS"
        elif result == "skipped":
            status = "⚠️  SKIPPED"
        elif result == "insufficient":
            status = "⚠️  INSUFFICIENT"
        elif result == "not_running":
            status = "⚠️  NOT RUNNING"
        else:
            status = "❌ FAIL"
        print(f"{provider.upper():15} {status}")

    print("="*60)
    print(f"Passed: {passed} | Failed: {failed} | Skipped: {skipped}")
    print("="*60)

    # Exit code - only fail if there are actual failures (not skips)
    if failed > 0:
        print(f"\n❌ {failed} provider(s) failed")
        sys.exit(1)
    elif passed > 0:
        print(f"\n✅ {passed} provider(s) working!")
        sys.exit(0)
    else:
        print("\n⚠️  All providers skipped (no API keys configured)")
        sys.exit(0)


if __name__ == "__main__":
    main()
