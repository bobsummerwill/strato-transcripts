#!/usr/bin/env python3
"""
AI transcript post-processor for Ethereum/blockchain content.
Batch process transcripts with multiple AI providers via OpenRouter.
Supports: opus, gemini, deepseek, chatgpt, qwen, kimi, glm, glm5, minimax, llama, grok, mistral.

All models are accessed through OpenRouter (https://openrouter.ai) with a single API key.
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
# Model Configuration: Hosted (OpenRouter) + Local (ollama)
# ============================================================================
# 11 models via OpenRouter. 4 local options for 48GB (dual 3090s).
#
# HOSTED MODELS (OpenRouter):
# ┌───────────┬─────────────────────┬───────────────────────────────────┬─────────┐
# │ Processor │ Model               │ OpenRouter ID                     │ Context │
# ├───────────┼─────────────────────┼───────────────────────────────────┼─────────┤
# │ opus      │ Claude Opus 4.6     │ anthropic/claude-opus-4.6         │ 1M      │
# │ gemini    │ Gemini 3.1 Pro      │ google/gemini-3.1-pro-preview     │ 1M      │
# │ chatgpt   │ GPT-5.2             │ openai/gpt-5.2                    │ 400K    │
# │ grok      │ Grok 4              │ x-ai/grok-4                       │ 256K    │
# │ qwen      │ Qwen3-Max           │ qwen/qwen3-max                    │ 256K    │
# │ kimi      │ Kimi K2.5           │ moonshotai/kimi-k2.5              │ 256K    │
# │ mistral   │ Mistral Large       │ mistralai/mistral-large-2411      │ 256K    │
# │ minimax   │ MiniMax M2.1        │ minimax/minimax-m2.1              │ 4M      │
# │ llama     │ Llama 4 Maverick    │ meta-llama/llama-4-maverick       │ 1M      │
# │ deepseek  │ DeepSeek V3.2       │ deepseek/deepseek-chat            │ 128K    │
# │ glm       │ GLM-4.7             │ z-ai/glm-4.7                      │ 203K    │
# └───────────┴─────────────────────┴───────────────────────────────────┴─────────┘
#
# LOCAL MODELS (ollama, fit on 48GB):
# ┌────────────────┬─────────────────────┬────────────────────────┬─────────┐
# │ Processor      │ Model               │ ollama ID              │ VRAM    │
# ├────────────────┼─────────────────────┼────────────────────────┼─────────┤
# │ glm            │ GLM-4.7-Flash       │ glm-4.7-flash:q4_K_M   │ ~19GB   │
# │ deepseek-local │ DeepSeek-R1 70B     │ deepseek-r1:70b        │ ~40GB   │
# │ qwen-local     │ Qwen3 72B           │ qwen3:72b              │ ~45GB   │
# │ mistral-local  │ Mixtral 8x7B        │ mixtral:8x7b           │ ~27GB   │
# │ llama-local    │ Llama 3.3 70B       │ llama3.3:70b           │ ~40GB   │
# └────────────────┴─────────────────────┴────────────────────────┴─────────┘
#
# See AI_PROVIDERS.md for full documentation.
# ============================================================================

OPENROUTER_MODELS = {
    'opus': 'anthropic/claude-opus-4.6',           # Claude Opus 4.6 - 1M context
    'gemini': 'google/gemini-3.1-pro-preview',     # Gemini 3.1 Pro - 1M context
    'deepseek': 'deepseek/deepseek-chat',          # DeepSeek V3.2 - 128K context
    'chatgpt': 'openai/gpt-5.2',                   # GPT-5.2 - 400K context
    'qwen': 'qwen/qwen3-max',                      # Qwen3-Max - 256K context
    'kimi': 'moonshotai/kimi-k2.5',                # Kimi K2.5 - 256K context
    'glm': 'z-ai/glm-4.7',                         # GLM-4.7 - 203K context (reasoning model)
    'glm5': 'z-ai/glm-5',                          # GLM-5 - 203K context (flagship agentic model, 744B MoE)
    'minimax': 'minimax/minimax-m2.1',             # MiniMax M2.1 - 4M context
    'llama': 'meta-llama/llama-4-maverick',        # Llama 4 Maverick - 1M context
    'grok': 'x-ai/grok-4',                         # Grok 4 - 256K context
    'mistral': 'mistralai/mistral-large-2411',     # Mistral Large - 256K context
}

# Max output tokens per model (some models need higher limits)
OPENROUTER_MAX_TOKENS = {
    'opus': 128000,     # Opus 4.6 supports 128K output
    'gemini': 64000,    # Gemini supports 64K output
    'chatgpt': 16384,   # GPT-5.2 conservative default
    'grok': 32768,      # Grok uses internal reasoning, needs more tokens
    'glm': 65536,       # GLM 4.7 is a reasoning model, needs tokens for reasoning + output
    'glm5': 65536,      # GLM-5 flagship model
    'default': 8192,    # Default for others
}

# Local model mapping (ollama model names)
# Models that fit on 48GB (dual 3090s) - maximized for quality
# Note: These are DIFFERENT models than the hosted versions
LOCAL_MODELS = {
    'glm': 'glm-4.7-flash:q4_K_M',        # 30B MoE, 3B active, ~19GB VRAM
    'deepseek-local': 'deepseek-r1:70b',  # 70B distilled (not V3.2), ~40GB Q4
    'qwen-local': 'qwen3:72b',            # 72B dense (not Max), ~45GB Q4
    'mistral-local': 'mixtral:8x7b',       # 47B MoE (8x7B), ~27GB Q4
    'llama-local': 'llama3.3:70b',        # 70B Llama 3.3 (not Llama 4), ~40GB Q4
}

# Models that require OpenRouter (no local option for 48GB)
# MoE models require VRAM for ALL weights, not just active parameters
HOSTED_ONLY_MODELS = {
    # Proprietary (API-only)
    'opus', 'gemini', 'chatgpt', 'grok', 'qwen',
    # Open weights but too large for 48GB even at Q4
    'deepseek',   # 671B total → ~386GB Q4 (use deepseek-local for 32B distilled)
    'kimi',       # 1T total → ~373GB Q4
    'mistral',    # 675B total → ~400GB Q4 (use mistral-local for 12B Nemo)
    'minimax',    # 230B total → ~55GB Q4 min
    'llama',      # 400B total → ~243GB Q4
}

# Direct API endpoints (bypass OpenRouter for specific providers)
# Use when you have a direct API key - better reliability than OpenRouter for new models
DIRECT_API_CONFIG = {
    'kimi': {
        'base_url': 'https://api.moonshot.ai/v1',  # Global endpoint
        'model_id': 'kimi-latest',  # kimi-k2.5 uses reasoning_content, kimi-latest uses content
        'env_var': 'MOONSHOT_API_KEY',
        'max_tokens': 16384,
    },
}


# ============================================================================
# GPU Validation for Local Mode
# ============================================================================

def validate_dual_3090():
    """Validate dual RTX 3090 setup. Hard fail if not detected.

    Local mode requires exactly 2x RTX 3090 GPUs (48GB total VRAM)
    for running GLM-4.7-Flash locally via ollama.
    """
    try:
        import torch
    except ImportError:
        print("ERROR: PyTorch not installed. Local mode requires PyTorch with CUDA.")
        print("Install with: pip install torch")
        sys.exit(1)

    if not torch.cuda.is_available():
        print("ERROR: CUDA not available. Local mode requires 2x RTX 3090 GPUs.")
        sys.exit(1)

    gpu_count = torch.cuda.device_count()
    if gpu_count < 2:
        print(f"ERROR: Found {gpu_count} GPU(s). Local mode requires 2x RTX 3090 GPUs.")
        sys.exit(1)

    # Validate both GPUs are RTX 3090
    for i in range(2):
        name = torch.cuda.get_device_name(i)
        if "3090" not in name:
            print(f"ERROR: GPU {i} is '{name}'. Local mode requires RTX 3090.")
            sys.exit(1)

    gpu0 = torch.cuda.get_device_name(0)
    gpu1 = torch.cuda.get_device_name(1)
    print(f"✅ Validated: 2x RTX 3090 detected")
    print(f"   GPU 0: {gpu0}")
    print(f"   GPU 1: {gpu1}")


def check_ollama_available():
    """Check if ollama is installed and running."""
    import shutil
    import subprocess

    # Check if ollama binary exists
    if not shutil.which('ollama'):
        print("ERROR: ollama not installed.")
        print("Install from: https://ollama.ai")
        sys.exit(1)

    # Check if ollama server is running
    try:
        result = subprocess.run(
            ['ollama', 'list'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode != 0:
            print("ERROR: ollama server not running.")
            print("Start with: ollama serve")
            sys.exit(1)
    except subprocess.TimeoutExpired:
        print("ERROR: ollama server not responding.")
        print("Start with: ollama serve")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Could not connect to ollama: {e}")
        sys.exit(1)

    print("✅ ollama is available")


# ============================================================================
# Utility Functions
# ============================================================================


def extract_transcriber_from_filename(filepath):
    """Parse transcriber name from intermediate filename."""
    filename = Path(filepath).stem

    # CHECK LONGER NAMES FIRST to avoid substring matching issues
    # (whisperx-cloud must be checked before whisperx)
    # Also handle _consensus suffix from video captioning workflow
    for service in ['whisperx-cloud', 'assemblyai', 'whisperx']:
        # Check for consensus suffix first (e.g., _assemblyai_consensus)
        if f'_{service}_consensus' in filename:
            basename = filename.replace(f'_{service}_consensus', '')
            return basename, service
        if f'_{service}' in filename:
            basename = filename.replace(f'_{service}', '')
            return basename, service

    return filename, "whisperx"


def fix_glm_format(content, input_content):
    """
    Fix GLM output format by adding timestamps from input.

    GLM often outputs: SPEAKER_XX: text (missing timestamps and markdown)
    This function converts to: **[MM:SS] SPEAKER_XX:** text

    Args:
        content: GLM's output (may be missing timestamps)
        input_content: Original input transcript with timestamps

    Returns:
        Fixed content with proper formatting
    """
    import re

    # Check if already properly formatted
    if content.strip().startswith('**['):
        return content

    # Extract timestamps from input (format: **[MM:SS] SPEAKER_XX:** or [MM:SS] SPEAKER_XX:)
    input_timestamps = {}
    for match in re.finditer(r'\*?\*?\[(\d+:\d+)\]\s*(SPEAKER_\d+)', input_content):
        ts, speaker = match.groups()
        # Store first timestamp for each speaker turn
        key = f"{speaker}_{len([k for k in input_timestamps if k.startswith(speaker)])}"
        input_timestamps[key] = ts

    # Parse GLM output - look for SPEAKER_XX: at start of line
    lines = content.split('\n')
    fixed_lines = []
    speaker_counts = {}
    current_timestamp = "00:00"

    for line in lines:
        # Check if line starts with SPEAKER_XX:
        match = re.match(r'^(SPEAKER_\d+):\s*(.*)', line)
        if match:
            speaker, text = match.groups()

            # Track speaker turn count
            if speaker not in speaker_counts:
                speaker_counts[speaker] = 0
            else:
                speaker_counts[speaker] += 1

            # Try to find corresponding timestamp from input
            key = f"{speaker}_{speaker_counts[speaker]}"
            if key in input_timestamps:
                current_timestamp = input_timestamps[key]

            # Format with proper markdown and timestamp
            fixed_lines.append(f"**[{current_timestamp}] {speaker}:** {text}")
        elif line.strip():
            # Non-speaker line (continuation text)
            fixed_lines.append(line)
        else:
            # Empty line
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)


def save_processed_files(output_dir, basename, transcriber, processor, content, input_content=None):
    """Save txt (clean) and md (with timestamps).

    Input format from AI: **[MM:SS] SPEAKER_XX:** paragraph text
    Output MD: Same as input (preserved)
    Output TXT: SPEAKER_XX: paragraph text (no timestamps, no markdown)

    Args:
        output_dir: Output directory
        basename: Episode base name
        transcriber: Transcriber name (whisperx, assemblyai, etc.)
        processor: Processor name (opus, glm, etc.)
        content: AI-generated content
        input_content: Original input (used to fix GLM format issues)
    """
    import re

    # Fix GLM format if needed (GLM often omits timestamps)
    if processor in ('glm', 'glm5') and input_content and not content.strip().startswith('**['):
        content = fix_glm_format(content, input_content)

    # Create episode-specific subdirectory
    episode_dir = Path(output_dir) / basename
    episode_dir.mkdir(parents=True, exist_ok=True)

    md_path = episode_dir / f"{basename}_{transcriber}_{processor}.md"

    # Clean up content (remove trailing whitespace)
    content_lines = [line.rstrip() for line in content.split('\n')]
    content_clean = '\n'.join(content_lines)
    
    # Save markdown version (preserve the AI's output format)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content_clean)
    
    return md_path


# ============================================================================
# Shared instruction template for all AI providers
# ============================================================================
SYSTEM_PROMPT = "You are an expert transcript editor specializing in Ethereum and blockchain technology."

INSTRUCTION_TEMPLATE = """You are an expert transcript editor specializing in Ethereum and blockchain technology.

════════════════════════════════════════════════════════════════════════════════
CRITICAL: OUTPUT ONLY THE TRANSCRIPT - NO THINKING/REASONING/ANALYSIS
════════════════════════════════════════════════════════════════════════════════
If you are a reasoning model (GLM, DeepSeek-R1, Kimi, etc.):
- Do NOT output your chain-of-thought
- Do NOT output any analysis, planning, or step-by-step thinking
- Do NOT output numbered lists of what you will do
- Do NOT output any text that is not the final transcript
- Your ENTIRE response must be ONLY the cleaned transcript

MANDATORY FORMAT - EVERY speaker turn MUST look EXACTLY like this:
**[00:01] SPEAKER_XX:** Text here...

Your output MUST:
1. Start with **[ (asterisk asterisk open-bracket)
2. Have timestamp in MM:SS format inside brackets
3. Have SPEAKER_XX after the bracket
4. Have colon and closing asterisks: :**
5. Then the spoken text

WRONG FORMAT (do NOT use):
- SPEAKER_XX: Text...  (missing timestamp and bold)
- [00:01] SPEAKER_XX: Text...  (missing asterisks)
- **SPEAKER_XX:** Text...  (missing timestamp)

If your output starts with ANYTHING other than **[ you have FAILED.
════════════════════════════════════════════════════════════════════════════════

Context - Ethereum Ecosystem Knowledge:
{context}

Raw Transcript (from speech recognition):
{transcript}

PRIMARY OBJECTIVE: Create a clean, readable transcript that preserves ALL dialogue and content.

CRITICAL OUTPUT RULES - READ FIRST

**DO NOT** add any preamble, introduction, or meta-commentary. Examples of what NOT to write:
- "Here is the cleaned transcript..."
- "Below is Part 1 of the transcript..."
- "I have processed the transcript following the guidelines..."
- Any analysis, reasoning, or explanation of your changes
- Numbered steps or planning
- Chain-of-thought or thinking process

**START IMMEDIATELY** with the first speaker label: **[MM:SS] SPEAKER_XX:** followed by their speech.
Your output should contain ONLY the formatted transcript, nothing else.

CRITICAL CONTENT PRESERVATION RULES

1. **PRESERVE COMPLETE CONTENT** - Do NOT summarize, condense, or skip any dialogue
   - Every discussion point must be retained
   - Every technical explanation must be preserved
   - Every example and anecdote must remain
   
2. **OUTPUT LENGTH REQUIREMENT** - Your output should be approximately the SAME length as the input
   - If input has ~15,000 words, output should have ~13,000-17,000 words (90-110%)
   - Significantly shorter output means you've removed too much content
   - This is non-negotiable - check your word count before finalizing

3. **TIMESTAMPS** - Handle based on what's in the input:
   - IF the input HAS timestamps [MM:SS]: PRESERVE them EXACTLY as they appear
     - Do NOT modify, recalculate, or regenerate timestamps
     - If input has [00:32], output must have [00:32]
     - Only ONE timestamp per speaker paragraph (at the beginning)
   - IF the input has NO timestamps: Do NOT add any timestamps
     - Just output: **SPEAKER_XX:** followed by text
     - Do NOT generate fake timestamps

4. **MERGE CONSECUTIVE SPEECH INTO PARAGRAPHS**
   - All speech from one speaker before another speaks = ONE paragraph
   - The timestamp is the START time of that speaker's turn
   - Separate sentences with spaces, NOT line breaks

WHAT TO FIX (Corrections Only)

✓ Technical term spellings and capitalization
  Examples: "etherium" → "Ethereum", "nfts" → "NFTs", "solidity" → "Solidity"
  
✓ Proper names - MUST use EXACT spellings from the "Key People" list above
  - This list contains the CANONICAL spellings of all names
  - "Bob Somersall" → "Bob Summerwill" (check the list!)
  - "Viktor Tron" → "Viktor Trón" (if accented version in list)
  - IMPORTANT: "Kieran" → "Kieren" (Kieren James-Lubin, NOT Kieran)
  - When in doubt, use the EXACT spelling from the Key People list
  
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

Each speaker turn can be multiple paragraphs (natural breaks) with:
- Bold speaker label with timestamp: **[MM:SS] SPEAKER_XX:**
- First paragraph (sentences separated by spaces)
- Subsequent paragraphs have blank lines between them but omit the speaker prefix
- Blank line before next speaker

CORRECT FORMAT EXAMPLE:
```
**[00:01] SPEAKER_00:** So, hello.

**[00:02] SPEAKER_01:** Hello, Bob.

**[00:03] SPEAKER_00:** So, yes, I'm Bob Summerwill, recording here at DevCon Prague for Early Days of Ethereum. And I have here Jakob. We've known each other about three years or so now, I think.

We did meet in Bogota for DevCon 6 for the first time where you introduced yourself. That was a really memorable conference.

**[00:38] SPEAKER_01:** Oh, yeah, thank you for the intro and good question. It was in Bogota. I think I knew about you or of you for longer than since then.

But yeah, I think you were chatting with someone and talking about Florian Glatz, maybe, and talking about the old days. And I just jumped in because I know Florian.

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
4. ☐ Verify format: **[MM:SS] SPEAKER_XX:** followed by their speech (can be multiple paragraphs)
5. ☐ Verify ONE timestamp per speaker turn (at the start of their first paragraph)
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

def process_with_local_model(transcript, context, processor):
    """Process transcript using local ollama model.

    Supported local models (48GB dual 3090s):
      glm, deepseek-local, qwen-local, mistral-local, llama-local

    Args:
        transcript: The raw transcript text to process
        context: Context summary (glossary, people, terms)
        processor: Processor name from LOCAL_MODELS

    Returns:
        Processed transcript text
    """
    try:
        import ollama
    except ImportError:
        raise ImportError("ollama package not installed. Install with: pip install ollama")

    model_name = LOCAL_MODELS.get(processor)
    if not model_name:
        raise ValueError(f"Processor '{processor}' not available locally. Only 'glm' supports local mode.")

    prompt = build_prompt(context, transcript)

    print(f"      Processing locally with {model_name}: ", end='', flush=True)

    # Use ollama chat API
    response = ollama.chat(
        model=model_name,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        options={
            "num_ctx": 32768,  # Context window
        }
    )

    result = response['message']['content']
    print(" ✓")
    return result


def process_with_openrouter(transcript, api_key, context, processor):
    """Process transcript using any model via OpenRouter with streaming.

    OpenRouter provides unified access to all major AI models with a single API key.
    See OPENROUTER_MODELS for the mapping of processor names to model IDs.

    Args:
        transcript: The raw transcript text to process
        api_key: OpenRouter API key
        context: Context summary (glossary, people, terms)
        processor: Processor name (opus, gemini, deepseek, etc.)

    Returns:
        Processed transcript text
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("openai package not installed. Install with: pip install openai")

    # Get model ID for this processor
    model_id = OPENROUTER_MODELS.get(processor)
    if not model_id:
        raise ValueError(f"Unknown processor: {processor}")

    # Get max tokens for this model
    max_tokens = OPENROUTER_MAX_TOKENS.get(processor, OPENROUTER_MAX_TOKENS['default'])

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )
    prompt = build_prompt(context, transcript)

    print(f"      Processing: ", end='', flush=True)

    result = ""
    chunk_count = 0

    # OpenRouter uses standard OpenAI-compatible API
    stream = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        stream=True,
        # OpenRouter-specific headers can be passed via extra_headers if needed
        extra_headers={
            "HTTP-Referer": "https://github.com/strato-net/strato-transcripts",
            "X-Title": "Strato Transcripts"
        }
    )

    for chunk in stream:
        if chunk.choices:
            delta = chunk.choices[0].delta
            # Only capture content, NOT reasoning (reasoning models output thinking which pollutes transcripts)
            text = delta.content
            if text:
                result += text
                chunk_count += 1
                if chunk_count % 100 == 0:
                    print(".", end='', flush=True)

    print(" ✓")
    return result


def process_with_direct_api(transcript, api_key, context, processor):
    """Process transcript using direct provider API (bypasses OpenRouter).

    Some providers (like Moonshot/Kimi) work better with direct API access,
    especially for newly released models that may not be fully integrated
    with OpenRouter yet.

    Args:
        transcript: The raw transcript text to process
        api_key: Direct API key for the provider
        context: Context summary (glossary, people, terms)
        processor: Processor name (e.g., 'kimi')

    Returns:
        Processed transcript text
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("openai package not installed. Install with: pip install openai")

    config = DIRECT_API_CONFIG.get(processor)
    if not config:
        raise ValueError(f"No direct API config for processor: {processor}")

    client = OpenAI(
        api_key=api_key,
        base_url=config['base_url']
    )
    prompt = build_prompt(context, transcript)

    print(f"      Processing (direct API): ", end='', flush=True)

    result = ""
    chunk_count = 0

    stream = client.chat.completions.create(
        model=config['model_id'],
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=config['max_tokens'],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices:
            delta = chunk.choices[0].delta
            # Only capture content, NOT reasoning_content (that's chain-of-thought which pollutes transcripts)
            text = delta.content
            if text:
                result += text
                chunk_count += 1
                if chunk_count % 100 == 0:
                    print(".", end='', flush=True)

    print(" ✓")
    return result


def strip_ai_preamble(text):
    """Strip any thinking/preamble from AI output, keeping only the transcript.

    Many AI models (especially reasoning models like GPT-5, Gemini, Kimi) output
    their chain-of-thought before the actual transcript. This function finds
    the first proper transcript marker (**[) and removes everything before it.

    Args:
        text: Raw AI output that may contain preamble

    Returns:
        Cleaned transcript starting with **[MM:SS] SPEAKER_XX:**
    """
    import re

    # Look for the first proper transcript line: **[MM:SS] SPEAKER_
    # This pattern matches: **[00:00] SPEAKER_00:**
    match = re.search(r'\*\*\[\d+:\d+\]\s*SPEAKER_', text)

    if match:
        # Found a proper transcript start - strip everything before it
        cleaned = text[match.start():]
        stripped_chars = match.start()
        if stripped_chars > 0:
            # Log how much was stripped (useful for debugging)
            stripped_preview = text[:min(100, stripped_chars)].replace('\n', ' ')
            print(f"      [Stripped {stripped_chars} chars of preamble: \"{stripped_preview}...\"]")
        return cleaned

    # No proper transcript marker found - try alternative patterns
    # Some models might use [MM:SS] SPEAKER_ without the bold
    match = re.search(r'\[\d+:\d+\]\s*SPEAKER_', text)
    if match:
        cleaned = text[match.start():]
        stripped_chars = match.start()
        if stripped_chars > 0:
            print(f"      [Stripped {stripped_chars} chars of preamble (no bold)]")
        return cleaned

    # Last resort: look for SPEAKER_ at start of line
    match = re.search(r'^SPEAKER_', text, re.MULTILINE)
    if match:
        cleaned = text[match.start():]
        stripped_chars = match.start()
        if stripped_chars > 0:
            print(f"      [Stripped {stripped_chars} chars of preamble (no timestamp)]")
        return cleaned

    # Couldn't find any transcript markers - return as-is (validation will catch this)
    return text


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

def process_single_combination(transcript_path, provider, api_keys, context, mode='hosted'):
    """Process single transcript with single provider.

    Args:
        transcript_path: Path to transcript file
        provider: Processor name (opus, gemini, glm, etc.)
        api_keys: Dict with 'openrouter' key (only needed for hosted mode)
        context: Context summary for the prompt
        mode: 'hosted' (OpenRouter API) or 'local' (ollama)
    """
    start_time = time.time()

    # Load transcript
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript = f.read()

    # Get output file paths for potential cleanup
    basename, transcriber = extract_transcriber_from_filename(transcript_path)
    # Note: outputs are stored under outputs/<basename>/...
    output_md = Path("outputs") / basename / f"{basename}_{transcriber}_{provider}.md"

    # Process with local model, direct API, or OpenRouter based on mode and available keys
    corrected = None

    try:
        if mode == 'local':
            corrected = process_with_local_model(transcript, context, provider)
        elif provider in api_keys.get('direct', {}):
            # Use direct API if available (better for newly released models)
            corrected = process_with_direct_api(transcript, api_keys['direct'][provider], context, provider)
        else:
            corrected = process_with_openrouter(transcript, api_keys['openrouter'], context, provider)

        # Strip any thinking/preamble from the output (reasoning models often include this)
        if corrected:
            corrected = strip_ai_preamble(corrected)
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"      {failure(f'Processing failed ({elapsed:.1f}s): {e}')}")
        
        # Clean up any partial files that may have been created
        for partial_file in [output_md]:
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
        for partial_file in [output_md]:
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
    # Pass input transcript so GLM format can be fixed if needed
    output_path = save_processed_files(
        "outputs",
        basename,
        transcriber,
        provider,
        corrected,
        input_content=transcript
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
                       help="Comma-separated list of processors. Hosted: opus,gemini,deepseek,chatgpt,qwen,kimi,glm,glm5,minimax,llama,grok,mistral. Local-only: deepseek-local,qwen-local,mistral-local,llama-local")
    parser.add_argument("--mode", choices=['hosted', 'local'], default='hosted',
                       help="Run models via OpenRouter API (hosted, default) or locally via ollama (local)")
    parser.add_argument("--parallel", type=int, default=0, metavar='N',
                       help="Number of parallel workers (default: 0 = all jobs in parallel). Use 1 for sequential.")

    args = parser.parse_args()

    # Parse processors
    processors = [p.strip() for p in args.processors.split(',')]
    # All valid processor names (hosted + local-only)
    valid_processors = {
        # Hosted (OpenRouter) - full-size models
        'opus', 'gemini', 'deepseek', 'chatgpt', 'qwen', 'kimi', 'glm', 'glm5', 'minimax', 'llama', 'grok', 'mistral',
        # Local-only (ollama) - models that fit on 48GB
        'deepseek-local', 'qwen-local', 'mistral-local', 'llama-local',
    }

    for proc in processors:
        if proc not in valid_processors:
            print(f"Error: Unknown processor '{proc}'")
            print(f"Valid options: {', '.join(sorted(valid_processors))}")
            sys.exit(1)

    api_keys = {}

    # Handle local vs hosted mode
    if args.mode == 'local':
        print("\n" + "="*70)
        print("LOCAL MODE - Running models via ollama")
        print("="*70)

        # Validate hardware: require exactly 2x RTX 3090
        validate_dual_3090()

        # Validate ollama is available
        check_ollama_available()

        # Validate all requested processors support local mode
        unsupported = [p for p in processors if p not in LOCAL_MODELS]
        if unsupported:
            print(f"\nERROR: Processor(s) not available locally: {', '.join(unsupported)}")
            print(f"\nAvailable local models (fit on 48GB dual 3090s):")
            print(f"  glm            → GLM-4.7-Flash (~19GB)")
            print(f"  deepseek-local → DeepSeek-R1 70B (~40GB)")
            print(f"  qwen-local     → Qwen3 72B (~45GB)")
            print(f"  mistral-local  → Mixtral 8x7B (~27GB)")
            print(f"  llama-local    → Llama 3.3 70B (~40GB)")
            print(f"\nNote: Full-size models require too much VRAM:")
            print(f"  deepseek: ~386GB | kimi: ~373GB | mistral: ~400GB")
            print(f"  minimax: ~55GB   | llama: ~243GB")
            print(f"\nUse --mode hosted for: {', '.join(sorted(HOSTED_ONLY_MODELS))}")
            sys.exit(1)

        # Show which local models will be used
        print("\nLocal models via ollama:")
        for proc in processors:
            model_name = LOCAL_MODELS.get(proc, 'unknown')
            print(f"  {proc}: {model_name}")

    else:
        # Hosted mode (default) - use OpenRouter
        # Validate no local-only processors are requested
        local_only = [p for p in processors if p in LOCAL_MODELS and p not in OPENROUTER_MODELS]
        if local_only:
            print(f"\nERROR: Processor(s) only available in local mode: {', '.join(local_only)}")
            print(f"\nThese are local-only models for ollama inference:")
            print(f"  deepseek-local → DeepSeek-R1 70B (not V3.2)")
            print(f"  qwen-local     → Qwen3 72B (not Max)")
            print(f"  mistral-local  → Mixtral 8x7B (not Large)")
            print(f"  llama-local    → Llama 3.3 70B (not Llama 4)")
            print(f"\nUse --mode local to run these, or use the hosted equivalents:")
            print(f"  deepseek, qwen, mistral, llama (via OpenRouter)")
            sys.exit(1)

        openrouter_key, error = validate_api_key('OPENROUTER_API_KEY')
        if error:
            print(f"\nError: {error}")
            print("All processors require OPENROUTER_API_KEY to be set.")
            print("Get your API key from: https://openrouter.ai/keys")
            sys.exit(1)

        api_keys['openrouter'] = openrouter_key

        # Check for direct API keys (bypass OpenRouter for specific providers)
        api_keys['direct'] = {}
        for proc in processors:
            if proc in DIRECT_API_CONFIG:
                env_var = DIRECT_API_CONFIG[proc]['env_var']
                direct_key = os.environ.get(env_var)
                if direct_key:
                    api_keys['direct'][proc] = direct_key

        # Show which models will be used
        print("\nModels:")
        for proc in processors:
            if proc in api_keys.get('direct', {}):
                config = DIRECT_API_CONFIG[proc]
                print(f"  {proc}: {config['model_id']} (direct API via {config['env_var']})")
            else:
                model_id = OPENROUTER_MODELS.get(proc, 'unknown')
                print(f"  {proc}: {model_id} (OpenRouter)")
    
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

    # Build list of (transcript_path, processor) jobs
    jobs = []
    for transcript_path in args.transcripts:
        transcript_path = Path(transcript_path)

        # Prefer .md files (have timestamps) over .txt files
        if transcript_path.suffix == '.txt':
            md_path = transcript_path.with_suffix('.md')
            if md_path.exists():
                print(f"  → Using .md file (has timestamps): {md_path.name}")
                transcript_path = md_path

        if not transcript_path.exists():
            print(f"✗ Transcript not found: {transcript_path}")
            failed_count += len(processors)
            continue

        for processor in processors:
            jobs.append((transcript_path, processor))

    def run_job(job_info):
        tp, proc = job_info
        job_start = time.time()
        result, elapsed = process_single_combination(
            str(tp), proc, api_keys, context, mode=args.mode
        )
        return tp.name, proc, result, elapsed

    parallel_workers = args.parallel if args.parallel > 0 else len(jobs)
    if parallel_workers > 1:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        import threading

        print(f"Running {len(jobs)} jobs with {parallel_workers} parallel workers\n")

        lock = threading.Lock()
        with ThreadPoolExecutor(max_workers=parallel_workers) as executor:
            futures = {executor.submit(run_job, job): job for job in jobs}
            for future in as_completed(futures):
                tp_name, proc, result, elapsed = future.result()
                combo_num += 1
                with lock:
                    if result:
                        success_count += 1
                        combo_times.append((tp_name, proc, elapsed))
                        print(f"[{combo_num}/{total}] {tp_name} + {proc} ✓ ({elapsed:.1f}s)")
                    else:
                        failed_count += 1
                        print(f"[{combo_num}/{total}] {tp_name} + {proc} ✗")
    else:
        for tp, proc in jobs:
            combo_num += 1
            print(f"[{combo_num}/{total}] {tp.name} + {proc}")

            result, elapsed = process_single_combination(
                str(tp), proc, api_keys, context, mode=args.mode
            )

            if result:
                success_count += 1
                combo_times.append((tp.name, proc, elapsed))
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
