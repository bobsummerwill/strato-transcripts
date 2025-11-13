#!/usr/bin/env python3
"""
AI transcript post-processor for Ethereum/blockchain content.
Supports: sonnet, chatgpt, gemini, llama, qwen.
Batch processes multiple transcripts × processors.
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
    """Check if API key environment variable is set. Returns (key, error_message)."""
    key = os.environ.get(env_var, '').strip()
    if not key:
        return None, f"{env_var} not set"
    return key, None


def extract_transcriber_from_filename(filepath):
    """Extract transcriber name from intermediate filename."""
    filename = Path(filepath).stem
    
    for service in ['whisperx', 'assemblyai', 'deepgram', 'openai']:
        if f'_{service}_raw' in filename:
            basename = filename.replace(f'_{service}_raw', '')
            return basename, service
    
    # Fallback if no match
    return filename, "whisperx"


def save_processed_files(output_dir, basename, transcriber, processor, content):
    """Save processed transcript in txt (no timestamps) and md (with timestamps) formats."""
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
    """Build complete prompt from template."""
    return INSTRUCTION_TEMPLATE.format(context=context, transcript=transcript)

def load_glossary():
    """Load ethereum_glossary.json if available."""
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
    """Load ethereum_people.txt, generating if needed."""
    people_file = Path("intermediates/ethereum_people.txt")
    
    # Generate if doesn't exist
    if not people_file.exists():
        extract_script = Path("scripts/extract_people.py")
        if extract_script.exists():
            import subprocess
            try:
                print("  Generating ethereum_people.txt...")
                subprocess.run(["python3", str(extract_script)], 
                             check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError:
                # Silent failure - file may not be critical
                pass
    
    if people_file.exists():
        with open(people_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    
    return []

def load_terms_list():
    """Load ethereum_technical_terms.txt, generating if needed."""
    terms_file = Path("intermediates/ethereum_technical_terms.txt")
    
    # Generate if doesn't exist
    if not terms_file.exists():
        extract_script = Path("scripts/extract_terms.py")
        if extract_script.exists():
            import subprocess
            try:
                print("  Generating ethereum_technical_terms.txt...")
                subprocess.run(["python3", str(extract_script)], 
                             check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError:
                # Silent failure - file may not be critical
                pass
    
    if terms_file.exists():
        with open(terms_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    
    return []

def build_context_summary():
    """Build context summary from available resources."""
    import subprocess
    
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
        # Generate people list if it doesn't exist
        people_file = Path("intermediates/ethereum_people.txt")
        if not people_file.exists():
            extract_script = Path("scripts/extract_people.py")
            if extract_script.exists():
                try:
                    print("  Generating ethereum_people.txt...")
                    subprocess.run(["python3", str(extract_script)], 
                                 check=True, capture_output=True, text=True, cwd=Path.cwd())
                except subprocess.CalledProcessError:
                    pass  # Silent failure - file may not be critical
        
        people = load_people_list()
        if people:
            context_parts.append(f"Known People ({len(people)}): {', '.join(people[:30])}")
    
    if not glossary["technical_terms"]:
        # Generate technical terms if it doesn't exist
        terms_file = Path("intermediates/ethereum_technical_terms.txt")
        if not terms_file.exists():
            extract_script = Path("scripts/extract_terms.py")
            if extract_script.exists():
                try:
                    print("  Generating ethereum_technical_terms.txt...")
                    subprocess.run(["python3", str(extract_script)], 
                                 check=True, capture_output=True, text=True, cwd=Path.cwd())
                except subprocess.CalledProcessError:
                    pass  # Silent failure - file may not be critical
        
        terms = load_terms_list()
        if terms:
            context_parts.append(f"Technical Terms ({len(terms)}): {', '.join(terms[:50])}")
    
    return "\n\n".join(context_parts) if context_parts else "No additional context available."

def process_with_anthropic(transcript, api_key, context):
    """Process transcript using Claude Sonnet 4.5 with streaming."""
    try:
        import anthropic
    except ImportError:
        raise ImportError("anthropic package not installed. Install with: pip install anthropic")
    
    client = anthropic.Anthropic(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    print(f"      Processing: ", end='', flush=True)
    
    result = ""
    chunk_count = 0
    
    with client.messages.stream(
        model="claude-sonnet-4-5",
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

def process_with_openai(transcript, api_key, context):
    """Process transcript using ChatGPT-4o-latest with streaming."""
    model = "chatgpt-4o-latest"
    try:
        import openai
    except ImportError:
        raise ImportError("openai package not installed. Install with: pip install openai")
    
    client = openai.OpenAI(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    print(f"      Processing: ", end='', flush=True)
    
    result = ""
    chunk_count = 0
    
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=16384,
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            result += chunk.choices[0].delta.content
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)
    
    print(" ✓")
    return result

def process_with_gemini(transcript, api_key, context):
    """Process transcript using Gemini 2.5 Pro with streaming."""
    model = "gemini-2.5-pro"
    try:
        import google.generativeai as genai
    except ImportError:
        raise ImportError("google-generativeai package not installed")
    
    genai.configure(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    print(f"      Processing: ", end='', flush=True)
    
    model_instance = genai.GenerativeModel(model)
    result = ""
    chunk_count = 0
    
    response = model_instance.generate_content(prompt, stream=True)
    
    for chunk in response:
        if chunk.text:
            result += chunk.text
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)
    
    print(" ✓")
    return result

def process_with_groq(transcript, api_key, context):
    """Process transcript using Llama 3.3 70B (via Groq) with streaming."""
    model = "llama-3.3-70b-versatile"
    try:
        import openai
    except ImportError:
        raise ImportError("openai package not installed")
    
    client = openai.OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
    prompt = build_prompt(context, transcript)
    
    print(f"      Model: {model}")
    print(f"      Processing: ", end='', flush=True)
    
    result = ""
    chunk_count = 0
    
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=8000,
        temperature=0.3,
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            result += chunk.choices[0].delta.content
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)
    
    print(" ✓")
    return result

def estimate_tokens(text):
    """Estimate tokens (words × 1.3)."""
    return int(len(text.split()) * 1.3)

def process_with_qwen(transcript, context, ollama_process=None):
    """Process transcript using Qwen 2.5 32B (via Ollama).
    
    NOTE: This function should only be called on GPU systems.
    CPU-only systems are filtered out in main() with a warning.
    """
    import subprocess
    import time
    
    try:
        import requests
        import json
    except ImportError:
        raise ImportError("requests package not installed")
    
    # Use 32B model (GPU-only)
    model = "qwen2.5:32b"
    print(f"      Model: {model} (GPU-accelerated)")
    
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
        
        # Estimate tokens and check for overflow
        estimated_tokens = estimate_tokens(prompt)
        print(f"      Transcript size: {len(transcript)} chars (~{estimated_tokens:,} tokens estimated)")
        
        # Qwen has 32K token limit - hard stop if exceeded
        if estimated_tokens > 32000:
            print(f"      ✗ OVERFLOW: {estimated_tokens:,} tokens exceeds Qwen's 32K limit")
            if started_ollama and ollama_process:
                ollama_process.terminate()
            raise Exception(f"Token overflow: {estimated_tokens} > 32000")
        
        # Warn if approaching limit
        if estimated_tokens > 28000:
            print(f"      ⚠️  CAUTION: ~{estimated_tokens:,} tokens approaching Qwen's 32K limit")
        
        print(f"      Processing: ", end='', flush=True)
        
        # Qwen 32B supports 32K context
        max_tokens = 32000
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": True,
                "options": {
                    "temperature": 0.3,
                    "num_predict": max_tokens,
                    "stop": []  # Override default stop sequences
                }
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
        
        # Validate output completeness
        input_words = len(transcript.split())
        output_words = len(result.split())
        
        # Check for severe truncation (output <40% of input = likely failure)
        if output_words < input_words * 0.4:
            print(f"\n      {failure('TRUNCATION DETECTED:')}")
            print(f"         Input:  {input_words:,} words (~{estimated_tokens:,} tokens)")
            print(f"         Output: {output_words:,} words (~{estimate_tokens(result):,} tokens)")
            print(f"         Output is only {output_words/input_words*100:.1f}% of input length")
            print(f"      → Qwen likely failed to complete the edit")
            if started_ollama and ollama_process:
                ollama_process.terminate()
            raise Exception(f"Output truncation: {output_words} words vs {input_words} words expected")
        
        # Warn for moderate truncation (40-70% of input)
        elif output_words < input_words * 0.7:
            print(f"\n      ⚠️  WARNING: Output shorter than expected")
            print(f"         Input:  {input_words:,} words")
            print(f"         Output: {output_words:,} words ({output_words/input_words*100:.1f}% of input)")
        
        return result, ollama_process if started_ollama else None
        
    except Exception as e:
        print(f" {failure(f'Error: {e}')}")
        if started_ollama and ollama_process:
            ollama_process.terminate()
        return None, None

def process_single_combination(transcript_path, provider, api_keys, context, ollama_process=None):
    """Process single transcript with single provider."""
    start_time = time.time()
    
    # Load transcript
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript = f.read()
    
    # Get output file paths for potential cleanup
    basename, transcriber = extract_transcriber_from_filename(transcript_path)
    output_txt = Path("outputs") / f"{basename}_{transcriber}_{provider}_processed.txt"
    output_md = Path("outputs") / f"{basename}_{transcriber}_{provider}_processed.md"
    
    # Process with appropriate provider
    corrected = None
    new_ollama_process = None
    
    try:
        if provider == "sonnet":
            corrected = process_with_anthropic(transcript, api_keys['sonnet'], context)
        elif provider == "chatgpt":
            corrected = process_with_openai(transcript, api_keys['chatgpt'], context)
        elif provider == "gemini":
            corrected = process_with_gemini(transcript, api_keys['gemini'], context)
        elif provider == "llama":
            corrected = process_with_groq(transcript, api_keys['llama'], context)
        elif provider == "qwen":
            corrected, new_ollama_process = process_with_qwen(transcript, context, ollama_process)
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"      {failure(f'Processing failed ({elapsed:.1f}s): {e}')}")
        
        # Clean up any partial files that may have been created
        for partial_file in [output_txt, output_md]:
            if partial_file.exists():
                try:
                    partial_file.unlink()
                    print(f"      → Deleted partial file: {partial_file.name}")
                except Exception as cleanup_error:
                    print(f"      ⚠ Could not delete {partial_file.name}: {cleanup_error}")
        
        return None, new_ollama_process, elapsed
    
    if not corrected:
        elapsed = time.time() - start_time
        print(f"      {failure(f'Processing failed ({elapsed:.1f}s): No output generated')}")
        
        # Clean up any partial files
        for partial_file in [output_txt, output_md]:
            if partial_file.exists():
                try:
                    partial_file.unlink()
                    print(f"      → Deleted partial file: {partial_file.name}")
                except Exception as cleanup_error:
                    print(f"      ⚠ Could not delete {partial_file.name}: {cleanup_error}")
        
        return None, new_ollama_process, elapsed
    
    # Save using utility function (basename/transcriber already extracted above)
    output_path = save_processed_files(
        "outputs",
        basename,
        transcriber,
        provider,
        corrected
    )
    
    elapsed = time.time() - start_time
    print(f"      ✓ Saved: {output_path} ({elapsed:.1f}s)")
    
    return output_path, new_ollama_process, elapsed

def main():
    parser = argparse.ArgumentParser(
        description="Post-process transcripts with multiple AI providers",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("transcripts", nargs='+', help="Transcript file path(s)")
    parser.add_argument("--processors", required=True,
                       help="Comma-separated list of processors (sonnet,chatgpt,gemini,llama,qwen)")
    
    args = parser.parse_args()
    
    # Clean up any dangling Ollama processes at startup
    try:
        import subprocess
        import requests
        
        # Check if Ollama is running
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=1)
            if response.status_code == 200:
                print("Stopping dangling Ollama process...")
                subprocess.run(['pkill', '-f', 'ollama serve'], 
                             stdout=subprocess.DEVNULL, 
                             stderr=subprocess.DEVNULL,
                             timeout=5)
                time.sleep(2)  # Give it time to stop
                print("✓ Cleared")
        except:
            pass  # Not running, nothing to clean up
    except Exception as e:
        # Non-fatal if cleanup fails
        print(f"⚠ Warning: Could not clean up dangling processes: {e}")
    
    # Parse processors
    processors = [p.strip() for p in args.processors.split(',')]
    valid_processors = {'sonnet', 'chatgpt', 'gemini', 'llama', 'qwen'}
    
    for proc in processors:
        if proc not in valid_processors:
            print(f"Error: Unknown processor '{proc}'")
            print(f"Valid options: {', '.join(sorted(valid_processors))}")
            sys.exit(1)
    
    # Check if Qwen requested on CPU-only system
    if 'qwen' in processors:
        try:
            import torch
            has_gpu = torch.cuda.is_available()
            
            if not has_gpu:
                # CPU-only system - skip Qwen with warning
                print()
                print(f"{Colors.YELLOW}⚠️  QWEN SKIPPED: GPU Required{Colors.RESET}")
                print()
                print("Qwen requires NVIDIA GPU with 12GB+ VRAM for transcript processing.")
                print("Current system: CPU-only")
                print()
                print("• Qwen 7B (CPU) is insufficient for complex transcript editing tasks")
                print("• Qwen 32B (GPU) would work excellently on RTX 5070 12GB or similar")
                print()
                print("Skipping Qwen processing - all other processors will continue normally.")
                print()
                
                # Remove qwen from processors list
                processors = [p for p in processors if p != 'qwen']
                
                if not processors:
                    print("Error: No processors remaining after skipping Qwen")
                    sys.exit(1)
        except ImportError:
            # If torch not available, can't use Qwen anyway
            print()
            print(f"{Colors.YELLOW}⚠️  QWEN SKIPPED: PyTorch not available{Colors.RESET}")
            print()
            processors = [p for p in processors if p != 'qwen']
            
            if not processors:
                print("Error: No processors remaining after skipping Qwen")
                sys.exit(1)
    
    # Check API keys using utility
    api_keys = {}
    skip_processors = []
    
    # Map processor names to their environment variable names
    key_mapping = {
        'sonnet': 'ANTHROPIC_API_KEY',     # Claude Sonnet 4.5 via Anthropic
        'chatgpt': 'OPENAI_API_KEY',       # ChatGPT-4o-latest via OpenAI
        'gemini': 'GOOGLE_API_KEY',        # Gemini 2.5 Pro via Google
        'llama': 'GROQ_API_KEY'            # Llama 3.3 70B via Groq
    }
    
    for proc in processors:
        if proc == 'qwen':
            # Qwen (local via Ollama) doesn't need an API key
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
    combo_times = []
    
    print("="*70)
    print(f"Processing {len(args.transcripts)} transcript(s) × {len(processors)} processor(s) = {total} combinations")
    print("="*70)
    print()
    
    ollama_process = None
    pipeline_start = time.time()
    
    try:
        for transcript_path in args.transcripts:
            if not Path(transcript_path).exists():
                print(f"✗ Transcript not found: {transcript_path}")
                failed_count += len(processors)
                continue
            
            for processor in processors:
                combo_num += 1
                print(f"[{combo_num}/{total}] {Path(transcript_path).name} + {processor}")
                
                result, new_ollama_process, elapsed = process_single_combination(
                    transcript_path, processor, api_keys, context, ollama_process
                )
                
                # Update Ollama process reference if it was started
                if new_ollama_process:
                    ollama_process = new_ollama_process
                
                if result:
                    success_count += 1
                    combo_times.append((Path(transcript_path).name, processor, elapsed))
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
    
    # Summary with timing
    pipeline_elapsed = time.time() - pipeline_start
    
    print("="*70)
    print("✓ Post-Processing Complete")
    print("="*70)
    print(f"Total combinations: {total}")
    print(f"Successful: {success_count}")
    print(f"Failed: {failed_count}")
    print(f"Skipped: {len(skip_processors) * len(args.transcripts)}")
    print()
    print(f"Total time: {pipeline_elapsed:.1f}s ({pipeline_elapsed/60:.1f}min)")
    
    if combo_times:
        print()
        print("Per-combination timing:")
        for transcript, processor, elapsed in combo_times:
            print(f"  {transcript} + {processor}: {elapsed:.1f}s")
        
        if len(combo_times) > 1:
            avg_time = sum(t[2] for t in combo_times) / len(combo_times)
            print(f"\n  Average: {avg_time:.1f}s per combination")
    
    print()
    print("Output files in: ./outputs/")
    print("="*70)
    
    sys.exit(0 if failed_count == 0 else 1)

if __name__ == "__main__":
    main()
