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
    print("Testing OPENAI (chatgpt-4o-latest)")
    print("="*60)
    
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not set")
        return False
    
    try:
        import openai
        client = openai.OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="chatgpt-4o-latest",
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
    print("Testing ANTHROPIC (claude-sonnet-4-5)")
    print("="*60)
    
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not set")
        return False
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=10,
            messages=[{"role": "user", "content": "Say 'hello' in one word"}]
        )
        
        print(f"✅ Connected successfully")
        print(f"Response: {response.content[0].text}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_ollama():
    """Test Ollama connection"""
    print("\n" + "="*60)
    print("Testing OLLAMA (qwen2.5:32b)")
    print("="*60)
    
    try:
        import requests
        
        # Check if Ollama is running
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            if response.status_code != 200:
                print("❌ Ollama service not running")
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Ollama service not accessible")
            return False
        
        # Test generation
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:32b",
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
            return True
        else:
            print(f"❌ HTTP {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_deepseek():
    """Test DeepSeek connection"""
    print("\n" + "="*60)
    print("Testing DEEPSEEK (deepseek-chat)")
    print("="*60)
    
    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key or api_key == "" or api_key == "your_deepseek_api_key_here":
        print("⚠️  API key not configured - skipping")
        return "skipped"
    
    try:
        import openai
        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": "Say 'hello' in one word"}],
            max_tokens=10
        )
        
        print(f"✅ Connected successfully")
        print(f"Response: {response.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_moonshot():
    """Test Moonshot Kimi connection"""
    print("\n" + "="*60)
    print("Testing MOONSHOT (moonshot-v1-128k)")
    print("="*60)
    
    api_key = os.environ.get('MOONSHOT_API_KEY')
    if not api_key or api_key == "" or api_key == "your_moonshot_api_key_here":
        print("⚠️  API key not configured - skipping")
        return "skipped"
    
    try:
        import openai
        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.moonshot.cn/v1"
        )
        
        response = client.chat.completions.create(
            model="moonshot-v1-128k",
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
    
    # Test in order: deepseek, moonshot, gemini, anthropic, ollama, openai
    results['deepseek'] = test_deepseek()
    results['moonshot'] = test_moonshot()
    results['gemini'] = test_gemini()
    results['anthropic'] = test_anthropic()
    results['ollama'] = test_ollama()
    results['openai'] = test_openai()
    
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
