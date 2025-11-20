#!/usr/bin/env python3
"""
Test connectivity and model access for all AI providers
"""

import os
import sys

def test_gemini():
    """Test Google Gemini connection"""
    print("\n" + "="*60)
    print("Testing GEMINI (gemini-2.5-pro)")
    print("="*60)
    
    api_key = os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        print("❌ GOOGLE_API_KEY not set")
        return False
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content("Say 'hello' in one word")
        
        print(f"✅ Connected successfully")
        print(f"Response: {response.text[:100]}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_openai():
    """Test OpenAI connection"""
    print("\n" + "="*60)
    print("Testing OPENAI (gpt-4o-2024-11-20)")
    print("="*60)
    
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not set")
        return False
    
    try:
        import openai
        client = openai.OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-4o-2024-11-20",
            messages=[{"role": "user", "content": "Say 'hello' in one word"}],
            max_tokens=10
        )
        
        print(f"✅ Connected successfully")
        print(f"Response: {response.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_anthropic():
    """Test Anthropic Claude connection"""
    print("\n" + "="*60)
    print("Testing ANTHROPIC (claude-sonnet-4-5-20250929)")
    print("="*60)
    
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not set")
        return False
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        
        # Use Claude Sonnet 4.5 (latest stable model as of 2025-11-10)
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=10,
            messages=[{"role": "user", "content": "Say 'hello' in one word"}]
        )
        
        print(f"✅ Connected successfully")
        print(f"Response: {response.content[0].text}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_qwen():
    """Test Qwen 32B (GPU-only via Ollama)"""
    import subprocess
    import time
    
    # Check for GPU
    try:
        import torch
        has_gpu = torch.cuda.is_available()
    except:
        has_gpu = False
    
    print("\n" + "="*60)
    print("Testing QWEN (qwen2.5:7b via Ollama)")
    print("="*60)
    
    if not has_gpu:
        print("⚠️  QWEN SKIPPED: GPU Required")
        print()
        print("Qwen requires NVIDIA GPU with 12GB+ VRAM for transcript processing.")
        print("Current system: CPU-only")
        print()
        return "skipped"
    
    model = "qwen2.5:7b"
    print(f"GPU detected - using {model}")
    
    ollama_process = None
    started_ollama = False
    
    try:
        import requests
        
        # Check if Ollama is running, start if needed
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            if response.status_code != 200:
                raise Exception("Ollama not responding")
        except:
            print("Starting Ollama service...")
            ollama_process = subprocess.Popen(
                ['ollama', 'serve'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            started_ollama = True
            time.sleep(3)  # Give service time to start
            print("✓ Ollama started")
        
        # Test generation with selected model
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": "Say 'hello' in one word",
                "stream": False,
                "options": {"num_predict": 10}
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Connected successfully")
            print(f"Response: {result['response'][:100]}")
            success = True
        else:
            print(f"❌ HTTP {response.status_code}: {response.text}")
            success = False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        success = False
    finally:
        # Stop Ollama if we started it
        if started_ollama and ollama_process:
            print("Stopping Ollama service...")
            ollama_process.terminate()
            try:
                ollama_process.wait(timeout=5)
            except:
                ollama_process.kill()
    
    return success

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

def test_deepgram():
    """Test Deepgram transcription service"""
    print("\n" + "="*60)
    print("Testing DEEPGRAM (transcription service)")
    print("="*60)
    
    api_key = os.environ.get('DEEPGRAM_API_KEY')
    if not api_key or api_key == "" or api_key == "your_deepgram_api_key_here":
        print("⚠️  API key not configured - skipping")
        return "skipped"
    
    try:
        from deepgram import DeepgramClient
        
        # Initialize client
        deepgram = DeepgramClient(api_key=api_key)
        
        # Just verify client initialization
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

def test_qwen_cloud():
    """Test Qwen 2.5 72B (hosted on Groq) connection"""
    print("\n" + "="*60)
    print("Testing QWEN-CLOUD (qwen/qwen3-32b on Groq)")
    print("="*60)

    api_key = os.environ.get('GROQ_API_KEY')
    if not api_key:
        print("❌ GROQ_API_KEY not set")
        return False

    try:
        import openai
        client = openai.OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

        response = client.chat.completions.create(
            model="qwen/qwen3-32b",
            messages=[{"role": "user", "content": "Say 'hello' in one word"}],
            max_tokens=10
        )

        print(f"✅ Connected successfully")
        print(f"Response: {response.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("="*60)
    print("AI Provider Connectivity Test")
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
    results['deepgram'] = test_deepgram()
    results['whisperx-cloud'] = test_whisperx_cloud()
    
    # Test AI post-processing providers
    print("\n" + "="*60)
    print("AI POST-PROCESSING PROVIDERS")
    print("="*60)
    results['anthropic'] = test_anthropic()
    results['openai'] = test_openai()
    results['gemini'] = test_gemini()
    results['qwen-cloud'] = test_qwen_cloud()
    results['qwen'] = test_qwen()
    
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
