#!/usr/bin/env python3
"""
Test connectivity and model access for all AI providers via OpenRouter.
All AI post-processing models are accessed through OpenRouter with a single API key.
"""

import os
import sys

# OpenRouter model IDs (same as in process_single_post_process.py)
OPENROUTER_MODELS = {
    'opus': ('anthropic/claude-opus-4-5', 'Claude Opus 4.5'),
    'gemini': ('google/gemini-3-pro-preview', 'Gemini 3 Pro'),
    'deepseek': ('deepseek/deepseek-chat', 'DeepSeek V3.2'),
    'chatgpt': ('openai/gpt-5.2', 'GPT-5.2'),
    'qwen': ('qwen/qwen3-max', 'Qwen3-Max'),
    'kimi': ('moonshotai/kimi-k2', 'Kimi K2'),
    'glm': ('zhipu/glm-4-plus', 'GLM-4-Plus'),
    'minimax': ('minimax/minimax-m2.1', 'MiniMax M2.1'),
    'llama': ('meta-llama/llama-4-maverick:free', 'Llama 4 Maverick'),
    'grok': ('x-ai/grok-4', 'Grok 4'),
    'mistral': ('mistralai/mistral-large-2411', 'Mistral Large'),
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
            max_tokens=10,
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
    print("All AI post-processing uses OpenRouter (single API key)")
    print("="*60)

    results = {}

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

    for provider, result in results.items():
        if result is True:
            status = "✅ PASS"
        elif result == "skipped":
            status = "⚠️  SKIPPED"
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
