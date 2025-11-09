#!/usr/bin/env python3
"""
Multi-provider AI transcript post-processor for Ethereum/blockchain content
Supports: Claude (Anthropic), ChatGPT-5 (OpenAI), Gemini (Google), DeepSeek, and Ollama (local)
Uses domain context to correct technical terms and speaker names
"""

import os
import sys
import json
from pathlib import Path
import argparse

# Shared instruction template for all AI providers
SYSTEM_PROMPT = "You are an expert transcript editor specializing in Ethereum and blockchain technology."

INSTRUCTION_TEMPLATE = """You are an expert transcript editor specializing in Ethereum and blockchain technology.

Context - Ethereum Ecosystem Knowledge:
{context}

Raw Transcript (from speech recognition):
{transcript}

Your tasks:
1. Fix technical term spellings and capitalization (e.g., "etherium" → "Ethereum", "nfts" → "NFTs")
2. Correct proper names using the people list provided
3. Fix blockchain concept terminology to match standard usage
4. Identify and replace generic speaker labels (SPEAKER_00, SPEAKER_01, etc.) with actual names if you can determine them from context
5. Improve punctuation and sentence structure for readability
6. Add paragraph breaks at natural conversation transitions
7. Preserve all timestamps in [XX.Xs] format exactly as they appear
8. Maintain the speaker label format (lines starting with speaker name followed by colon)

Important: Only make changes where you are confident. If unsure about a speaker's identity or technical term, leave it as-is.

Output the corrected transcript maintaining the exact same format structure."""

def build_prompt(context, transcript):
    """Build the complete prompt from template"""
    return INSTRUCTION_TEMPLATE.format(context=context, transcript=transcript)

def load_glossary():
    """Load ethereum_glossary.json if available"""
    glossary_file = Path("ethereum_glossary.json")
    
    if glossary_file.exists():
        with open(glossary_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    return {
        "people": [],
        "technical_terms": [],
        "projects": [],
        "abbreviations": {}
    }

def load_people_list():
    """Load ethereum_people.txt if available"""
    people_file = Path("intermediates/ethereum_people.txt")
    
    if people_file.exists():
        with open(people_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    
    return []

def load_terms_list():
    """Load ethereum_technical_terms.txt if available"""
    terms_file = Path("intermediates/ethereum_technical_terms.txt")
    
    if terms_file.exists():
        with open(terms_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    
    return []

def build_context_summary():
    """Build a concise context summary from available resources"""
    context_parts = []
    
    # Add glossary info if available
    glossary = load_glossary()
    if glossary["people"]:
        context_parts.append(f"Key People ({len(glossary['people'])}): {', '.join(glossary['people'][:30])}")
    if glossary["technical_terms"]:
        context_parts.append(f"Technical Terms ({len(glossary['technical_terms'])}): {', '.join(glossary['technical_terms'][:50])}")
    if glossary["projects"]:
        context_parts.append(f"Projects ({len(glossary['projects'])}): {', '.join(glossary['projects'][:20])}")
    
    # Try to load from separate files if glossary doesn't exist
    if not glossary["people"]:
        people = load_people_list()
        if people:
            context_parts.append(f"Known People ({len(people)}): {', '.join(people[:30])}")
    
    if not glossary["technical_terms"]:
        terms = load_terms_list()
        if terms:
            context_parts.append(f"Technical Terms ({len(terms)}): {', '.join(terms[:50])}")
    
    return "\n\n".join(context_parts) if context_parts else "No additional context available."

def process_with_anthropic(transcript, api_key, context):
    """Process transcript using Anthropic Claude"""
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic package not installed. Install with: pip install anthropic")
        return None
    
    client = anthropic.Anthropic(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=8192,  # Maximum supported by Claude 3.5
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.content[0].text

def split_transcript_by_speakers(transcript, max_chunk_size=15000):
    """Split transcript into chunks at speaker boundaries"""
    lines = transcript.split('\n')
    chunks = []
    current_chunk = []
    current_size = 0
    
    for line in lines:
        line_size = len(line)
        
        # If adding this line would exceed max size and we have content, start new chunk
        if current_size + line_size > max_chunk_size and current_chunk:
            chunks.append('\n'.join(current_chunk))
            current_chunk = []
            current_size = 0
        
        current_chunk.append(line)
        current_size += line_size + 1  # +1 for newline
    
    # Add final chunk
    if current_chunk:
        chunks.append('\n'.join(current_chunk))
    
    return chunks

def process_with_openai(transcript, api_key, context, model="chatgpt-4o-latest"):
    """Process transcript using OpenAI GPT models (GPT-4, GPT-4o, ChatGPT-5)"""
    try:
        import openai
    except ImportError:
        print("Error: openai package not installed. Install with: pip install openai")
        return None
    
    client = openai.OpenAI(api_key=api_key)
    
    # ALWAYS chunk to ensure complete output - unconditional chunking prevents any truncation
    print(f"   Transcript size: {len(transcript)} chars - using chunking for complete output")
    print(f"   Splitting into chunks for processing...")
    
    chunks = split_transcript_by_speakers(transcript, max_chunk_size=15000)
    print(f"   Processing {len(chunks)} chunks...")
    
    corrected_chunks = []
    for i, chunk in enumerate(chunks, 1):
        print(f"   Processing chunk {i}/{len(chunks)}...", end=' ', flush=True)
        
        prompt = build_prompt(context, chunk)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=16384
        )
        
        corrected_chunks.append(response.choices[0].message.content)
        print("✓")
    
    # Combine chunks
    return '\n\n'.join(corrected_chunks)

def process_with_gemini(transcript, api_key, context, model="gemini-2.0-flash-exp"):
    """Process transcript using Google Gemini"""
    try:
        import google.generativeai as genai
    except ImportError:
        print("Error: google-generativeai package not installed. Install with: pip install google-generativeai")
        return None
    
    genai.configure(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    model_instance = genai.GenerativeModel(model)
    response = model_instance.generate_content(prompt)
    
    return response.text

def process_with_deepseek(transcript, api_key, context, model="deepseek-chat"):
    """Process transcript using DeepSeek API (OpenAI-compatible)"""
    try:
        import openai
    except ImportError:
        print("Error: openai package not installed. Install with: pip install openai")
        return None
    
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )
    prompt = build_prompt(context, transcript)
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=16384  # Maximum supported
    )
    
    return response.choices[0].message.content

def process_with_ollama(transcript, context, model="qwen2.5:32b"):
    """Process transcript using local Ollama"""
    try:
        import requests
    except ImportError:
        print("Error: requests package not installed. Install with: pip install requests")
        return None
    
    prompt = build_prompt(context, transcript)
    
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 16000
                }
            },
            timeout=600
        )
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama. Make sure it's running:")
        print("  1. Start Ollama: ollama serve")
        print("  2. Or install it: curl -fsSL https://ollama.com/install.sh | sh")
        return None
    except requests.exceptions.Timeout:
        print("Error: Ollama request timed out. Try a smaller model or increase timeout.")
        return None
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return None

def process_transcript(transcript_path, api_key, provider="anthropic", 
                      openai_model="chatgpt-4o-latest", 
                      gemini_model="gemini-2.0-flash-exp",
                      deepseek_model="deepseek-chat",
                      ollama_model="qwen2.5:32b"):
    """Main processing function"""
    
    print("="*60)
    print("Transcript Post-Processor")
    print("="*60)
    print(f"Input: {transcript_path}")
    print(f"Provider: {provider}")
    
    if provider == "openai":
        print(f"Model: {openai_model}")
    elif provider == "gemini":
        print(f"Model: {gemini_model}")
    elif provider == "deepseek":
        print(f"Model: {deepseek_model}")
    elif provider == "ollama":
        print(f"Model: {ollama_model}")
    
    # Load transcript
    print("\n1. Loading transcript...")
    transcript_file = Path(transcript_path)
    if not transcript_file.exists():
        print(f"Error: Transcript file not found: {transcript_path}")
        return None
    
    with open(transcript_file, 'r', encoding='utf-8') as f:
        transcript = f.read()
    
    print(f"   Loaded {len(transcript)} characters")
    
    # Build context
    print("\n2. Building context from glossary...")
    context = build_context_summary()
    print(f"   Context built: {len(context)} characters")
    
    # Process with AI
    print(f"\n3. Processing with {provider}...")
    
    if provider == "anthropic":
        corrected = process_with_anthropic(transcript, api_key, context)
    elif provider == "openai":
        corrected = process_with_openai(transcript, api_key, context, openai_model)
    elif provider == "gemini":
        corrected = process_with_gemini(transcript, api_key, context, gemini_model)
    elif provider == "deepseek":
        corrected = process_with_deepseek(transcript, api_key, context, deepseek_model)
    elif provider == "ollama":
        corrected = process_with_ollama(transcript, context, ollama_model)
    else:
        print(f"Error: Unknown provider: {provider}")
        return None
    
    if not corrected:
        print("Error: Processing failed")
        return None
    
    print("   ✓ Processing complete")
    
    # Strip trailing whitespace from each line
    corrected_lines = [line.rstrip() for line in corrected.split('\n')]
    corrected_clean = '\n'.join(corrected_lines)
    
    # Validate line count - original vs corrected
    original_line_count = len(transcript.split('\n'))
    corrected_line_count = len(corrected_lines)
    retention_pct = (corrected_line_count / original_line_count) * 100
    
    print(f"\n4. Validating output...")
    print(f"   Original lines: {original_line_count}")
    print(f"   Corrected lines: {corrected_line_count}")
    print(f"   Retention: {retention_pct:.1f}%")
    
    # Fail if more than 15% of lines are lost (allowing for reasonable AI cleanup & line consolidation)
    if corrected_line_count < original_line_count * 0.85:
        print(f"\n❌ ERROR: Severe content loss detected!")
        print(f"   Lost {original_line_count - corrected_line_count} lines ({100 - retention_pct:.1f}% loss)")
        print(f"   This indicates truncation or incomplete processing.")
        
        # Save partial file for inspection to outputs directory
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)
        base_name = transcript_file.stem.replace('_transcript_with_speakers', '').replace('_lv2_lq', '').replace('_lv2_hq', '')
        partial_path = output_dir / f"{base_name}_corrected_PARTIAL.txt"
        with open(partial_path, 'w', encoding='utf-8') as f:
            f.write(corrected_clean)
        print(f"   Saved PARTIAL output for inspection: {partial_path}")
        print(f"   File marked as PARTIAL - requires manual review.")
        return None
    
    # Save corrected transcript to outputs directory
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    
    # Clean up filename: remove model/quality suffixes and _transcript_with_speakers
    base_name = transcript_file.stem.replace('_transcript_with_speakers', '').replace('_lv2_lq', '').replace('_lv2_hq', '')
    output_path = output_dir / f"{base_name}_corrected.txt"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(corrected_clean)
    
    print(f"\n5. Saved corrected transcript to: {output_path}")
    
    # Also save markdown version
    md_output_path = output_path.with_suffix('.md')
    md_content = corrected_clean.replace('\n\nSPEAKER_', '\n\n**SPEAKER_')
    md_content = md_content.replace(':\n', ':**\n')
    with open(md_output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"   Also saved markdown to: {md_output_path}")
    
    print("\n" + "="*60)
    print(f"✓ Post-processing complete! ({retention_pct:.1f}% line retention)")
    print("="*60)
    
    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Post-process transcripts using AI to correct technical terms and speaker names",
        epilog="""
Examples:
  # Using Anthropic Claude
  python3 post_process_transcript.py transcript.txt --provider anthropic
  
  # Using OpenAI ChatGPT-5/GPT-4o
  python3 post_process_transcript.py transcript.txt --provider openai
  
  # Using Google Gemini 2.0
  python3 post_process_transcript.py transcript.txt --provider gemini
  
  # Using DeepSeek (very cost-effective)
  python3 post_process_transcript.py transcript.txt --provider deepseek
  
  # Using Ollama (local, FREE, private)
  python3 post_process_transcript.py transcript.txt --provider ollama --ollama-model qwen2.5:32b
  
  # With environment variables
  export OPENAI_API_KEY=sk-...
  python3 post_process_transcript.py transcript.txt --provider openai
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("transcript", help="Path to transcript file")
    parser.add_argument("--api-key", help="API key (not needed for Ollama)")
    parser.add_argument("--provider", 
                       choices=["anthropic", "openai", "gemini", "deepseek", "ollama"], 
                       default="anthropic",
                       help="AI provider (default: anthropic)")
    parser.add_argument("--openai-model", 
                       default="chatgpt-4o-latest",
                       choices=["chatgpt-4o-latest", "gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-4"],
                       help="OpenAI model (default: chatgpt-4o-latest)")
    parser.add_argument("--gemini-model",
                       default="gemini-2.0-flash-exp",
                       choices=["gemini-2.0-flash-exp", "gemini-1.5-pro", "gemini-1.5-flash"],
                       help="Gemini model (default: gemini-2.0-flash-exp)")
    parser.add_argument("--deepseek-model",
                       default="deepseek-chat",
                       choices=["deepseek-chat", "deepseek-reasoner"],
                       help="DeepSeek model (default: deepseek-chat)")
    parser.add_argument("--ollama-model",
                       default="qwen2.5:32b",
                       help="Ollama model (default: qwen2.5:32b)")
    
    args = parser.parse_args()
    
    # Get API key (not needed for Ollama)
    api_key = None
    
    if args.provider == "anthropic":
        api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            print("Error: Anthropic API key required")
            print("Set ANTHROPIC_API_KEY or use --api-key")
            sys.exit(1)
    elif args.provider == "openai":
        api_key = args.api_key or os.environ.get('OPENAI_API_KEY')
        if not api_key:
            print("Error: OpenAI API key required")
            print("Set OPENAI_API_KEY or use --api-key")
            sys.exit(1)
    elif args.provider == "gemini":
        api_key = args.api_key or os.environ.get('GOOGLE_API_KEY')
        if not api_key:
            print("Error: Google API key required")
            print("Set GOOGLE_API_KEY or use --api-key")
            print("Get key: https://makersuite.google.com/app/apikey")
            sys.exit(1)
    elif args.provider == "deepseek":
        api_key = args.api_key or os.environ.get('DEEPSEEK_API_KEY')
        if not api_key:
            print("Error: DeepSeek API key required")
            print("Set DEEPSEEK_API_KEY or use --api-key")
            print("Get key: https://platform.deepseek.com/")
            sys.exit(1)
    elif args.provider == "ollama":
        print("Using local Ollama - no API key required")
    
    # Process transcript
    result = process_transcript(
        args.transcript, api_key, args.provider,
        args.openai_model, args.gemini_model,
        args.deepseek_model, args.ollama_model
    )
    
    sys.exit(0 if result else 1)

if __name__ == "__main__":
    main()
