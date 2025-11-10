#!/usr/bin/env python3
"""
Multi-provider AI transcript post-processor for Ethereum/blockchain content
Supports: Claude (Anthropic), ChatGPT-5 (OpenAI), Gemini (Google), DeepSeek, Moonshot, and Ollama (local)
Uses domain context to correct technical terms and speaker names

Now supports batch processing of multiple transcripts × processors internally
"""

import os
import sys
import json
import time
from pathlib import Path
import argparse

# ANSI color codes
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def success(msg):
    return f"{Colors.GREEN}✓{Colors.RESET} {msg}"

def failure(msg):
    return f"{Colors.RED}✗{Colors.RESET} {msg}"

def skip(msg):
    return f"{Colors.YELLOW}⊘{Colors.RESET} {msg}"


# ============================================================================
# Utility Functions
# ============================================================================

def validate_api_key(env_var):
    """
    Check if API key environment variable is set.
    
    Args:
        env_var: Name of environment variable to check
    
    Returns:
        Tuple of (key, error_message). If key exists, error_message is None.
        If key missing, key is None and error_message describes the issue.
    """
    key = os.environ.get(env_var, '').strip()
    if not key:
        return None, f"{env_var} not set"
    return key, None


def extract_transcriber_from_filename(filepath):
    """
    Extract transcriber name from intermediate filename.
    
    Args:
        filepath: Path to intermediate transcript file
    
    Returns:
        Tuple of (basename, transcriber_name) or (basename, None) if not found
    """
    filename = Path(filepath).stem
    
    for service in ['whisperx', 'assemblyai', 'deepgram', 'openai']:
        if f'_{service}_raw' in filename:
            basename = filename.replace(f'_{service}_raw', '')
            return basename, service
    
    # Fallback if no match
    return filename, "whisperx"


def save_processed_files(output_dir, basename, transcriber, processor, content):
    """
    Save processed transcript in both txt and md formats with consistent naming.
    TXT format: No timestamps (clean text only)
    MD format: With timestamps for reference
    
    Args:
        output_dir: Directory to save files  
        basename: Base filename without extension
        transcriber: Name of transcription service used
        processor: Name of AI processor used
        content: Processed transcript content
    
    Returns:
        Path object for the .txt file
    """
    import re
    
    output_path = Path(output_dir) / f"{basename}_{transcriber}_{processor}_processed.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Clean up content
    content_lines = [line.rstrip() for line in content.split('\n')]
    content_clean = '\n'.join(content_lines)
    
    # Save text version (NO timestamps)
    # Strip timestamps like [150.9s] from beginning of lines
    text_lines = []
    for line in content_clean.split('\n'):
        # Remove timestamp pattern [XXX.Xs] at start of line
        clean_line = re.sub(r'^\[[\d.]+s\] ', '', line)
        text_lines.append(clean_line)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_lines))
    
    # Save markdown version (WITH timestamps, convert SPEAKER_ labels to bold)
    md_path = output_path.with_suffix('.md')
    md_content = content_clean.replace('\n\nSPEAKER_', '\n\n**SPEAKER_')
    md_content = md_content.replace(':\n', ':**\n')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return output_path


# ============================================================================
# Shared instruction template for all AI providers
# ============================================================================
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
    """Process transcript using Anthropic Claude 3.5 Sonnet with streaming"""
    try:
        import anthropic
    except ImportError:
        raise ImportError("anthropic package not installed. Install with: pip install anthropic")
    
    client = anthropic.Anthropic(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    print(f"      Transcript size: {len(transcript)} chars")
    print(f"      Processing: ", end='', flush=True)
    
    result = ""
    chunk_count = 0
    
    with client.messages.stream(
        model="claude-3-5-sonnet-20241022",
        max_tokens=64000,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            result += text
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)
    
    print(" ✓")
    return result

def split_transcript_by_speakers(transcript, max_chunk_size=15000):
    """Split transcript into chunks at speaker boundaries"""
    lines = transcript.split('\n')
    chunks = []
    current_chunk = []
    current_size = 0
    
    for line in lines:
        line_size = len(line)
        
        if current_size + line_size > max_chunk_size and current_chunk:
            chunks.append('\n'.join(current_chunk))
            current_chunk = []
            current_size = 0
        
        current_chunk.append(line)
        current_size += line_size + 1
    
    if current_chunk:
        chunks.append('\n'.join(current_chunk))
    
    return chunks

def process_with_openai(transcript, api_key, context):
    """Process transcript using OpenAI GPT-4o"""
    model = "gpt-4o-2024-11-20"
    try:
        import openai
    except ImportError:
        raise ImportError("openai package not installed. Install with: pip install openai")
    
    client = openai.OpenAI(api_key=api_key)
    
    print(f"      Transcript size: {len(transcript)} chars")
    print(f"      Chunking for complete output...")
    
    chunks = split_transcript_by_speakers(transcript, max_chunk_size=15000)
    print(f"      Processing {len(chunks)} chunks: ", end='', flush=True)
    
    corrected_chunks = []
    for i, chunk in enumerate(chunks, 1):
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
        print(".", end='', flush=True)
    
    print(" ✓")
    return '\n\n'.join(corrected_chunks)

def process_with_gemini(transcript, api_key, context):
    """Process transcript using Google Gemini 2.5 Pro"""
    model = "gemini-2.5-pro"
    try:
        import google.generativeai as genai
    except ImportError:
        raise ImportError("google-generativeai package not installed")
    
    genai.configure(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    print(f"      Transcript size: {len(transcript)} chars")
    print(f"      Processing: ", end='', flush=True)
    
    model_instance = genai.GenerativeModel(model)
    response = model_instance.generate_content(prompt)
    
    print("✓")
    return response.text

def process_with_deepseek(transcript, api_key, context):
    """Process transcript using DeepSeek Chat"""
    model = "deepseek-chat"
    try:
        import openai
    except ImportError:
        raise ImportError("openai package not installed")
    
    client = openai.OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    
    print(f"      Transcript size: {len(transcript)} chars")
    print(f"      Chunking for complete output...")
    
    chunks = split_transcript_by_speakers(transcript, max_chunk_size=15000)
    print(f"      Processing {len(chunks)} chunks: ", end='', flush=True)
    
    corrected_chunks = []
    for i, chunk in enumerate(chunks, 1):
        prompt = build_prompt(context, chunk)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=8192
        )
        
        corrected_chunks.append(response.choices[0].message.content)
        print(".", end='', flush=True)
    
    print(" ✓")
    return '\n\n'.join(corrected_chunks)

def process_with_moonshot(transcript, api_key, context):
    """Process transcript using Moonshot Kimi K2-Instruct"""
    model = "kimi-k2-instruct"
    try:
        import openai
    except ImportError:
        raise ImportError("openai package not installed")
    
    client = openai.OpenAI(api_key=api_key, base_url="https://api.moonshot.cn/v1")
    prompt = build_prompt(context, transcript)
    
    print(f"      Transcript size: {len(transcript)} chars")
    print(f"      Processing: ", end='', flush=True)
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=16384
    )
    
    print("✓")
    return response.choices[0].message.content

def process_with_ollama(transcript, context, ollama_process=None):
    """Process transcript using local Ollama - reuses existing process if provided"""
    import subprocess
    import time
    
    try:
        import requests
    except ImportError:
        raise ImportError("requests package not installed")
    
    model = "qwen2.5:32b"
    started_ollama = False
    
    try:
        # Check if Ollama is running (either passed in or already running)
        if ollama_process is None:
            try:
                response = requests.get("http://localhost:11434/api/tags", timeout=2)
                if response.status_code != 200:
                    raise Exception("Ollama not responding")
            except:
                print("      Starting Ollama service...")
                ollama_process = subprocess.Popen(
                    ['ollama', 'serve'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                started_ollama = True
                
                # Wait for service
                for i in range(10):
                    time.sleep(1)
                    try:
                        requests.get("http://localhost:11434/api/tags", timeout=1)
                        print("      ✓ Ollama started")
                        break
                    except:
                        continue
                else:
                    raise Exception("Ollama failed to start")
        
        # Process transcript
        prompt = build_prompt(context, transcript)
        print(f"      Transcript size: {len(transcript)} chars")
        print(f"      Processing: ", end='', flush=True)
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": True,
                "options": {"temperature": 0.3, "num_predict": 16000}
            },
            timeout=1800,
            stream=True
        )
        response.raise_for_status()
        
        result = ""
        chunk_count = 0
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                if "response" in chunk:
                    result += chunk["response"]
                    chunk_count += 1
                    if chunk_count % 50 == 0:
                        print(".", end='', flush=True)
                if chunk.get("done", False):
                    break
        
        print(" ✓")
        return result, ollama_process if started_ollama else None
        
    except Exception as e:
        print(f" ✗ Error: {e}")
        if started_ollama and ollama_process:
            ollama_process.terminate()
        return None, None

def process_single_combination(transcript_path, provider, api_keys, context, ollama_process=None):
    """Process a single transcript with a single provider"""
    # Load transcript
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript = f.read()
    
    # Process with appropriate provider
    corrected = None
    new_ollama_process = None
    
    try:
        if provider == "anthropic":
            corrected = process_with_anthropic(transcript, api_keys['anthropic'], context)
        elif provider == "openai":
            corrected = process_with_openai(transcript, api_keys['openai'], context)
        elif provider == "gemini":
            corrected = process_with_gemini(transcript, api_keys['gemini'], context)
        elif provider == "deepseek":
            corrected = process_with_deepseek(transcript, api_keys['deepseek'], context)
        elif provider == "moonshot":
            corrected = process_with_moonshot(transcript, api_keys['moonshot'], context)
        elif provider == "ollama":
            corrected, new_ollama_process = process_with_ollama(transcript, context, ollama_process)
    except Exception as e:
        print(f"      ✗ Processing failed: {e}")
        return None, new_ollama_process
    
    if not corrected:
        return None, new_ollama_process
    
    # Extract transcriber name and basename from input file
    basename, transcriber = extract_transcriber_from_filename(transcript_path)
    
    # Save using utility function
    output_path = save_processed_files(
        "outputs",
        basename,
        transcriber,
        provider,
        corrected
    )
    
    print(f"      ✓ Saved: {output_path}")
    
    return output_path, new_ollama_process

def main():
    parser = argparse.ArgumentParser(
        description="Post-process transcripts with multiple AI providers",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("transcripts", nargs='+', help="Transcript file path(s)")
    parser.add_argument("--processors", required=True,
                       help="Comma-separated list of processors (anthropic,openai,gemini,deepseek,moonshot,ollama)")
    
    args = parser.parse_args()
    
    # Parse processors
    processors = [p.strip() for p in args.processors.split(',')]
    valid_processors = {'anthropic', 'openai', 'gemini', 'deepseek', 'moonshot', 'ollama'}
    
    for proc in processors:
        if proc not in valid_processors:
            print(f"Error: Unknown processor '{proc}'")
            print(f"Valid options: {', '.join(sorted(valid_processors))}")
            sys.exit(1)
    
    # Check API keys using utility
    api_keys = {}
    skip_processors = []
    
    # Map processor names to their environment variable names
    key_mapping = {
        'anthropic': 'ANTHROPIC_API_KEY',
        'openai': 'OPENAI_API_KEY',
        'gemini': 'GOOGLE_API_KEY',
        'deepseek': 'DEEPSEEK_API_KEY',
        'moonshot': 'MOONSHOT_API_KEY'
    }
    
    for proc in processors:
        if proc == 'ollama':
            # Ollama doesn't need an API key
            continue
        
        env_var = key_mapping.get(proc)
        if env_var:
            key, error = validate_api_key(env_var)
            if error:
                print(f"⊘ Skipping {proc}: {error}")
                skip_processors.append(proc)
            else:
                api_keys[proc] = key
    
    # Remove skipped processors
    processors = [p for p in processors if p not in skip_processors]
    
    if not processors:
        print("\nError: No processors available (all API keys missing)")
        sys.exit(1)
    
    # Build context once
    print("\nBuilding context from glossary...")
    context = build_context_summary()
    print(f"✓ Context built: {len(context)} characters")
    print()
    
    # Process all combinations
    total = len(args.transcripts) * len(processors)
    success_count = 0
    failed_count = 0
    combo_num = 0
    
    print("="*70)
    print(f"Processing {len(args.transcripts)} transcript(s) × {len(processors)} processor(s) = {total} combinations")
    print("="*70)
    print()
    
    ollama_process = None
    
    try:
        for transcript_path in args.transcripts:
            if not Path(transcript_path).exists():
                print(f"✗ Transcript not found: {transcript_path}")
                failed_count += len(processors)
                continue
            
            for processor in processors:
                combo_num += 1
                print(f"[{combo_num}/{total}] {Path(transcript_path).name} + {processor}")
                
                result, new_ollama_process = process_single_combination(
                    transcript_path, processor, api_keys, context, ollama_process
                )
                
                # Update Ollama process reference if it was started
                if new_ollama_process:
                    ollama_process = new_ollama_process
                
                if result:
                    success_count += 1
                else:
                    failed_count += 1
                
                print()
    
    finally:
        # Clean up Ollama if we started it
        if ollama_process:
            print("Stopping Ollama service...")
            ollama_process.terminate()
            try:
                ollama_process.wait(timeout=5)
                print("✓ Ollama stopped")
            except:
                ollama_process.kill()
                print("✓ Ollama force stopped")
    
    # Summary
    print("="*70)
    print("✓ Post-Processing Complete")
    print("="*70)
    print(f"Total combinations: {total}")
    print(f"Successful: {success_count}")
    print(f"Failed: {failed_count}")
    print(f"Skipped: {len(skip_processors) * len(args.transcripts)}")
    print()
    print("Output files in: ./outputs/")
    print("="*70)
    
    sys.exit(0 if failed_count == 0 else 1)

if __name__ == "__main__":
    main()
