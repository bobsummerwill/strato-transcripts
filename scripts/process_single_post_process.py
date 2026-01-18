#!/usr/bin/env python3
"""
AI transcript post-processor for Ethereum/blockchain content.
Batch process transcripts with multiple AI providers.
Supports: opus, gemini, deepseek, chatgpt.
"""

import os
import sys
import json
import time
from pathlib import Path
import argparse

# Import shared utilities
from common import (Colors, success, failure, skip, validate_api_key,
                    load_people_list, load_terms_list, cleanup_gpu_memory)


# ============================================================================
# Utility Functions
# ============================================================================


def extract_transcriber_from_filename(filepath):
    """Parse transcriber name from intermediate filename."""
    filename = Path(filepath).stem

    # CHECK LONGER NAMES FIRST to avoid substring matching issues
    # (whisperx-cloud must be checked before whisperx)
    for service in ['whisperx-cloud', 'assemblyai', 'whisperx']:
        if f'_{service}' in filename:
            basename = filename.replace(f'_{service}', '')
            return basename, service

    return filename, "whisperx"


def save_processed_files(output_dir, basename, transcriber, processor, content):
    """Save txt (clean) and md (with timestamps).
    
    Input format from AI: **[MM:SS] SPEAKER_XX:** paragraph text
    Output MD: Same as input (preserved)
    Output TXT: SPEAKER_XX: paragraph text (no timestamps, no markdown)
    """
    import re
    
    # Create episode-specific subdirectory
    episode_dir = Path(output_dir) / basename
    episode_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = episode_dir / f"{basename}_{transcriber}_{processor}.txt"
    
    # Clean up content (remove trailing whitespace)
    content_lines = [line.rstrip() for line in content.split('\n')]
    content_clean = '\n'.join(content_lines)
    
    # Save markdown version (preserve the AI's output format)
    md_path = output_path.with_suffix('.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content_clean)
    
    # Save text version (NO timestamps, NO markdown)
    # Transform: **[MM:SS] SPEAKER_XX:** text -> SPEAKER_XX: text
    text_lines = []
    for line in content_clean.split('\n'):
        clean_line = line
        # Remove **[MM:SS] SPEAKER_XX:** pattern and convert to SPEAKER_XX:
        clean_line = re.sub(r'\*\*\[[\d:]+\]\s*(SPEAKER_\d+):\*\*', r'\1:', clean_line)
        # Also handle old format: **SPEAKER_XX:** with [timestamp] on line
        clean_line = re.sub(r'\*\*(SPEAKER_\d+):\*\*', r'\1:', clean_line)
        # Remove standalone timestamps like [MM:SS] or [XXX.Xs]
        clean_line = re.sub(r'^\[[\d:.]+\]\s?', '', clean_line)
        text_lines.append(clean_line)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_lines))
    
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

PRIMARY OBJECTIVE: Create a clean, readable transcript that preserves ALL dialogue and content.

CRITICAL CONTENT PRESERVATION RULES

1. **PRESERVE COMPLETE CONTENT** - Do NOT summarize, condense, or skip any dialogue
   - Every discussion point must be retained
   - Every technical explanation must be preserved
   - Every example and anecdote must remain
   
2. **OUTPUT LENGTH REQUIREMENT** - Your output should be approximately the SAME length as the input
   - If input has ~15,000 words, output should have ~13,000-17,000 words (90-110%)
   - Significantly shorter output means you've removed too much content
   - This is non-negotiable - check your word count before finalizing

3. **PRESERVE EXACT TIMESTAMPS** - CRITICAL: Do NOT modify, recalculate, or regenerate timestamps
   - Copy timestamps EXACTLY as they appear in the input transcript
   - If input has [00:32], output must have [00:32] - not [00:30] or [00:35]
   - If input has [42:57], output must have [42:57] - preserve the exact values
   - The timestamps are from speech recognition and represent ACTUAL audio positions
   - Format: [MM:SS] with 2 digits each (already correct in input)
   - Do NOT compress or recalculate based on estimated speech duration
   - Only ONE timestamp per speaker paragraph (at the beginning)

4. **MERGE CONSECUTIVE SPEECH INTO PARAGRAPHS**
   - All speech from one speaker before another speaks = ONE paragraph
   - The timestamp is the START time of that speaker's turn
   - Separate sentences with spaces, NOT line breaks

WHAT TO FIX (Corrections Only)

✓ Technical term spellings and capitalization
  Examples: "etherium" → "Ethereum", "nfts" → "NFTs", "solidity" → "Solidity"
  
✓ Proper names using the people list provided
  Examples: Correct misspellings of "Vitalik", "Gavin Wood", etc.
  
✓ Blockchain terminology to match standard usage
  Examples: "ethereum" → "Ethereum", "bit coin" → "Bitcoin"
  
✓ Punctuation and sentence structure for readability
  Examples: Add periods, commas, capitalize sentences

WHAT TO REMOVE (Cleanup Only - Be Selective)

✓ Excessive filler words (when they impede readability)
  Remove: "um", "uh", "you know", "like" (when used excessively)
  Keep: Natural conversation flow - don't over-sanitize
  
✓ False starts and stammering
  Example: "I was— I mean I was going to say..." → "I was going to say..."
  
✓ Obvious repetitions
  Example: "the the contract" → "the contract"

WHAT TO PRESERVE (Critical - Never Remove)

✓ ALL substantive dialogue and discussion points
✓ ALL technical explanations, code examples, and demonstrations
✓ ALL speaker labels (SPEAKER_01, SPEAKER_02, etc. - do not add actual names)
✓ Timestamps (one per speaker paragraph)
✓ Natural conversation flow and authentic speaking patterns
✓ Context and background information
✓ Questions and answers
✓ Reactions and commentary

REQUIRED OUTPUT FORMAT

Each speaker turn is ONE paragraph with:
- Bold speaker label with timestamp: **[MM:SS] SPEAKER_XX:**
- All their speech in a single paragraph (sentences separated by spaces)
- Blank line before next speaker

CORRECT FORMAT EXAMPLE:
```
**[00:01] SPEAKER_00:** So, hello.

**[00:02] SPEAKER_01:** Hello, Bob.

**[00:03] SPEAKER_00:** So, yes, I'm Bob Samuel, recording here at DevCon Prague for Early Days of Ethereum. And I have here Jakob. We've known each other about three years or so now, I think. We did meet in Bogota for DevCon 6 for the first time where you introduced yourself.

**[00:38] SPEAKER_01:** Oh, yeah, thank you for the intro and good question. It was in Bogota. I think I knew about you or of you for longer than since then. But yeah, I think you were chatting with someone and talking about Florian Glatz, maybe, and talking about the old days. And I just jumped in because I know Florian.

**[01:08] SPEAKER_00:** I think it was like maybe August to December.
```

INCORRECT FORMAT TO AVOID:
```
**SPEAKER_01:**
[00:01] First line here.
[00:05] Second line here.
```
This is WRONG - do not put speaker and timestamp on separate lines, and do NOT have multiple timestamps per speaker turn.

VALIDATION CHECKLIST (Before Submitting)

1. ☐ Count words in input transcript
2. ☐ Count words in your output
3. ☐ Verify output is 90-110% of input length
4. ☐ Verify format: **[MM:SS] SPEAKER_XX:** followed by full paragraph
5. ☐ Verify ONE timestamp per speaker paragraph (at the start)
6. ☐ Verify no major discussion points were removed
7. ☐ Verify paragraphs are separated by blank lines

If your output is significantly shorter than input, you have removed too much content.
Go back and restore the missing dialogue.

Output the corrected transcript in the exact format specified above."""

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

def process_with_opus(transcript, api_key, context):
    """Process transcript using Claude Opus 4.5 with streaming."""
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
        model="claude-opus-4-5",
        max_tokens=64000,  # Opus 4.5 max output tokens
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            result += text
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)

    print(" ✓")
    return result

def process_with_gemini(transcript, api_key, context):
    """Process transcript using Gemini 3.0 Pro with streaming."""
    model = "models/gemini-3-pro-preview"
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

def process_with_deepseek(transcript, api_key, context):
    """Process transcript using DeepSeek-V3 with streaming."""
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("openai package not installed. Install with: pip install openai")

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    prompt = build_prompt(context, transcript)

    print(f"      Processing: ", end='', flush=True)

    result = ""
    chunk_count = 0

    stream = client.chat.completions.create(
        model="deepseek-chat",  # DeepSeek-V3.2 (latest)
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=8192,  # DeepSeek API limit
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


def process_with_chatgpt(transcript, api_key, context):
    """Process transcript using ChatGPT 5.2 (OpenAI) with streaming.

    Notes:
    - Uses the OpenAI Python SDK already present in requirements.
    - Prefers the Responses API for streaming, with a fallback to Chat Completions
      to maximize compatibility across OpenAI account/model settings.
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("openai package not installed. Install with: pip install openai")

    client = OpenAI(api_key=api_key)
    prompt = build_prompt(context, transcript)

    model = os.getenv("CHATGPT_MODEL", "gpt-5.2")
    # Keep default conservative; some accounts/models enforce tighter limits.
    max_output_tokens = int(os.getenv("CHATGPT_MAX_OUTPUT_TOKENS", "16384"))

    print(f"      Processing: ", end='', flush=True)

    result = ""
    chunk_count = 0

    # Preferred: Responses API streaming
    try:
        with client.responses.stream(
            model=model,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            max_output_tokens=max_output_tokens,
        ) as stream:
            for event in stream:
                # Event types vary slightly by SDK version; handle the common ones.
                if getattr(event, "type", None) == "response.output_text.delta":
                    delta = getattr(event, "delta", None)
                    if delta:
                        result += delta
                        chunk_count += 1
                        if chunk_count % 100 == 0:
                            print(".", end='', flush=True)
            # Ensure we drain and finalize cleanly.
            _ = stream.get_final_response()

        print(" ✓")
        return result
    except Exception:
        # Fallback: Chat Completions streaming
        pass

    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        # Some OpenAI models (incl. ChatGPT 5.x) require max_completion_tokens.
        max_completion_tokens=max_output_tokens,
        stream=True,
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            result += delta
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)

    print(" ✓")
    return result

def estimate_tokens(text):
    """Estimate tokens (words × 1.3)."""
    return int(len(text.split()) * 1.3)

def validate_output_quality(input_text, output_text, provider):
    """Validate output quality before saving."""
    import re
    
    issues = []
    
    # Check 1: Word count ratio (should be 85-115% of input)
    input_words = len(input_text.split())
    output_words = len(output_text.split())
    
    if input_words > 0:
        ratio = output_words / input_words
        if ratio < 0.85:
            issues.append(f"Content loss: only {ratio*100:.0f}% of original length ({output_words}/{input_words} words)")
        elif ratio > 1.15:
            issues.append(f"Content expansion: {ratio*100:.0f}% of original length ({output_words}/{input_words} words)")
    
    # Check 2: Timestamp preservation
    input_timestamps = len(re.findall(r'\[\d+:\d+\]', input_text))
    output_timestamps = len(re.findall(r'\[\d+:\d+\]', output_text))
    
    if input_timestamps > 0:
        ts_ratio = output_timestamps / input_timestamps
        if ts_ratio < 0.95:
            lost = input_timestamps - output_timestamps
            issues.append(f"Lost {lost} timestamps ({ts_ratio*100:.0f}% preserved)")
        elif ts_ratio > 1.05:
            added = output_timestamps - input_timestamps
            issues.append(f"Added {added} timestamps ({ts_ratio*100:.0f}% of original) - likely regenerated or over-segmented")
    
    # Check 3: Minimum output length (prevent empty/truncated outputs)
    if output_words < 100:
        issues.append(f"Output too short: only {output_words} words")
    
    # Check 4: Speaker label preservation
    input_speakers = len(re.findall(r'SPEAKER_\d+', input_text))
    output_speakers = len(re.findall(r'SPEAKER_\d+', output_text))
    
    if input_speakers > 0 and output_speakers == 0:
        issues.append("All speaker labels removed")
    
    return len(issues) == 0, issues

def process_single_combination(transcript_path, provider, api_keys, context):
    """Process single transcript with single provider."""
    start_time = time.time()
    
    # Load transcript
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript = f.read()
    
    # Get output file paths for potential cleanup
    basename, transcriber = extract_transcriber_from_filename(transcript_path)
    # Note: outputs are stored under outputs/<basename>/...
    output_txt = Path("outputs") / basename / f"{basename}_{transcriber}_{provider}.txt"
    output_md = Path("outputs") / basename / f"{basename}_{transcriber}_{provider}.md"
    
    # Process with appropriate provider
    corrected = None
    
    try:
        if provider == "opus":
            corrected = process_with_opus(transcript, api_keys['opus'], context)
        elif provider == "gemini":
            corrected = process_with_gemini(transcript, api_keys['gemini'], context)
        elif provider == "deepseek":
            corrected = process_with_deepseek(transcript, api_keys['deepseek'], context)
        elif provider == "chatgpt":
            corrected = process_with_chatgpt(transcript, api_keys['chatgpt'], context)
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
        
        return None, elapsed
    
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
        
        return None, elapsed
    
    # Validate output quality
    valid, issues = validate_output_quality(transcript, corrected, provider)
    
    if not valid:
        print(f"      ⚠ Quality validation failed:")
        for issue in issues:
            print(f"        • {issue}")
        print(f"      → Saving output with quality warning")
    else:
        print(f"      ✓ Quality validation passed")
    
    # Save using utility function (basename/transcriber already extracted above)
    output_path = save_processed_files(
        "outputs",
        basename,
        transcriber,
        provider,
        corrected
    )
    
    elapsed = time.time() - start_time
    
    if valid:
        print(f"      ✓ Saved: {output_path} ({elapsed:.1f}s)")
    else:
        print(f"      ⚠ Saved: {output_path} ({elapsed:.1f}s) - REVIEW RECOMMENDED")
    
    return output_path, elapsed

def main():
    parser = argparse.ArgumentParser(
        description="Post-process transcripts with multiple AI providers",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("transcripts", nargs='+', help="Transcript file path(s)")
    parser.add_argument("--processors", required=True,
                       help="Comma-separated list of processors (opus,gemini,deepseek,chatgpt)")
    
    args = parser.parse_args()
    
    # Parse processors
    processors = [p.strip() for p in args.processors.split(',')]
    valid_processors = {'opus', 'gemini', 'deepseek', 'chatgpt'}
    
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
        'opus': 'ANTHROPIC_API_KEY',       # Claude Opus 4.5 via Anthropic
        'gemini': 'GOOGLE_API_KEY',        # Gemini 3.0 Pro via Google
        'deepseek': 'DEEPSEEK_API_KEY',    # DeepSeek-V3 via DeepSeek
        'chatgpt': 'OPENAI_API_KEY'        # ChatGPT 5.2 via OpenAI
    }
    
    for proc in processors:
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
    
    pipeline_start = time.time()
    
    for transcript_path in args.transcripts:
        if not Path(transcript_path).exists():
            print(f"✗ Transcript not found: {transcript_path}")
            failed_count += len(processors)
            continue
        
        for processor in processors:
            combo_num += 1
            print(f"[{combo_num}/{total}] {Path(transcript_path).name} + {processor}")
            
            result, elapsed = process_single_combination(
                transcript_path, processor, api_keys, context
            )
            
            if result:
                success_count += 1
                combo_times.append((Path(transcript_path).name, processor, elapsed))
            else:
                failed_count += 1
            
            print()
    
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
