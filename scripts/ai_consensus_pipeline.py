#!/usr/bin/env python3
"""
Multi-Phase AI Consensus Pipeline

Produces a single, superb-quality transcript by leveraging multiple AI post-processors
through consensus voting.

Pipeline:
  Phase 3: AI Correction Pass - Process with all 11 AI models, align back to word-level
  Phase 4: AI Consensus - Build consensus from 11 AI word lists
  Phase 5: Filler Removal - Filter out filler words
  Phase 6: Final Output - Generate .md and .txt files

Prerequisite: Run transcriber consensus first (Phases 1-2):
  python3 scripts/assess_quality.py --intermediate-consensus --episode <name>
"""

import argparse
import json
import os
import re
import sys
import time
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

# Import shared utilities
from common import Colors, success, failure, validate_api_key

# Import from assess_quality for reuse
from assess_quality import (
    load_glossary,
    align_words_by_time,
    build_word_level_consensus_text,
    words_to_segments,
    seconds_to_timestamp,
)

# =============================================================================
# Constants
# =============================================================================

AI_MODELS = [
    'opus', 'gemini', 'chatgpt', 'grok', 'deepseek',
    'kimi', 'qwen', 'glm', 'minimax', 'llama', 'mistral'
]

FILLER_WORDS = {
    'um', 'uh', 'er', 'ah', 'hmm', 'mm',
    'like',  # When used as filler, not comparison
    'you know', 'i mean', 'kind of', 'sort of',
    'actually', 'basically', 'literally',
    'right', 'yeah', 'yep', 'okay', 'ok',
}

# Single-word fillers only (multi-word handled separately)
SINGLE_WORD_FILLERS = {
    'um', 'uh', 'er', 'ah', 'hmm', 'mm',
    'actually', 'basically', 'literally',
    'yeah', 'yep', 'okay', 'ok',
}

# =============================================================================
# Text Tokenization
# =============================================================================

def tokenize_preserving_punctuation(text):
    """
    Tokenize text into words, handling URLs, code identifiers, hyphenated words, and contractions.

    Examples:
      "Hello, world!" -> ["Hello,", "world!"]
      "https://example.com" -> ["https://example.com"]
      "C++" -> ["C++"]
      "node.js" -> ["node.js"]
      "pre-formation" -> ["pre-formation"]
      "it's" -> ["it's"]
    """
    # Pattern that handles special cases - order matters!
    # More specific patterns must come first to avoid being consumed by generic \w+
    pattern = r"""
        https?://\S+|                              # URLs (highest priority)
        [A-Z]\+\+|                                 # C++, D++
        [A-Z]#|                                    # C#, F#
        [a-z]+\.[a-z]+|                            # node.js (lowercase dotted identifiers)
        \w+-\w+(?:-\w+)*|                          # Hyphenated words (pre-formation, T-shirt)
        \w+'\w*|                                   # Contractions (it's, don't)
        \w+|                                       # Regular words
        [.,!?;:()\[\]{}]                           # Standalone punctuation
    """
    tokens = re.findall(pattern, text, re.VERBOSE | re.IGNORECASE)
    return tokens


def normalize_for_matching(word):
    """Normalize word for matching (lowercase, strip punctuation)."""
    return word.lower().strip('.,!?;:"\'-()[]{}')


def strip_transcript_formatting(text):
    """
    Strip timestamp/speaker formatting from AI output, keeping only spoken content.

    Removes patterns like:
    - **[MM:SS] SPEAKER_XX:**
    - [MM:SS] SPEAKER_XX:
    - SPEAKER_XX:

    Returns clean text with only spoken words.
    """
    # Remove markdown bold timestamp/speaker patterns: **[00:00] SPEAKER_00:**
    text = re.sub(r'\*\*\[\d+:\d+\]\s*SPEAKER_\d+:\*\*', '', text)
    # Remove plain timestamp/speaker patterns: [00:00] SPEAKER_00:
    text = re.sub(r'\[\d+:\d+\]\s*SPEAKER_\d+:', '', text)
    # Remove standalone speaker labels: SPEAKER_00:
    text = re.sub(r'SPEAKER_\d+:', '', text)
    # Remove orphaned markdown bold markers
    text = re.sub(r'\*\*', '', text)
    # Normalize whitespace
    text = ' '.join(text.split())
    return text


# =============================================================================
# AI Text-to-Word Alignment (Core Algorithm)
# =============================================================================

def compute_alignment_confidence(orig_normalized, ai_normalized):
    """
    Compute alignment confidence using SequenceMatcher ratio.
    
    Returns a score between 0.0 and 1.0, where:
    - 1.0 = perfect match
    - 0.0 = no match
    """
    matcher = SequenceMatcher(None, orig_normalized, ai_normalized, autojunk=False)
    return matcher.ratio()


def align_segment(orig_words, ai_tokens, orig_start_idx, ai_start_idx):
    """
    Align a single time segment using SequenceMatcher.
    
    Returns list of aligned words with timestamps.
    """
    aligned = []
    
    if not ai_tokens or not orig_words:
        return aligned
    
    # Create normalized versions for matching
    orig_normalized = [normalize_for_matching(w['text']) for w in orig_words]
    ai_normalized = [normalize_for_matching(t) for t in ai_tokens]
    
    # Find matching blocks
    matcher = SequenceMatcher(None, orig_normalized, ai_normalized, autojunk=False)
    matching_blocks = matcher.get_matching_blocks()
    
    last_orig_idx = 0
    last_ai_idx = 0
    last_time = orig_words[0]['start'] if orig_words else 0.0
    last_speaker = orig_words[0]['speaker'] if orig_words else 'SPEAKER_00'
    
    for match in matching_blocks:
        orig_match_start, ai_match_start, size = match.a, match.b, match.size
        
        if size == 0:
            continue
        
        # Handle AI-inserted words before this match
        if ai_match_start > last_ai_idx:
            next_time = orig_words[orig_match_start]['start'] if orig_match_start < len(orig_words) else (orig_words[-1]['end'] if orig_words else 0.0)
            num_inserted = ai_match_start - last_ai_idx
            time_per_word = (next_time - last_time) / (num_inserted + 1) if num_inserted > 0 else 0.1
            
            for i in range(last_ai_idx, ai_match_start):
                insert_time = last_time + (i - last_ai_idx + 1) * time_per_word
                aligned.append({
                    'text': ai_tokens[ai_start_idx + i],
                    'start': insert_time,
                    'end': insert_time + 0.1,
                    'speaker': last_speaker,
                    'source': 'ai_inserted'
                })
        
        # Handle matched words
        for i in range(size):
            orig_idx = orig_match_start + i
            ai_idx = ai_match_start + i
            
            if orig_idx < len(orig_words):
                orig_word = orig_words[orig_idx]
                aligned.append({
                    'text': ai_tokens[ai_start_idx + ai_idx],
                    'start': orig_word['start'],
                    'end': orig_word['end'],
                    'speaker': orig_word['speaker'],
                    'source': 'matched'
                })
                last_time = orig_word['end']
                last_speaker = orig_word['speaker']
        
        last_orig_idx = orig_match_start + size
        last_ai_idx = ai_match_start + size
    
    # Handle remaining AI words
    if last_ai_idx < len(ai_tokens):
        for i in range(last_ai_idx, len(ai_tokens)):
            aligned.append({
                'text': ai_tokens[ai_start_idx + i],
                'start': last_time + 0.1 * (i - last_ai_idx + 1),
                'end': last_time + 0.1 * (i - last_ai_idx + 2),
                'speaker': last_speaker,
                'source': 'ai_inserted'
            })
    
    return aligned


def align_ai_to_original(original_words, ai_text):
    """
    Map AI-corrected text back to original word timestamps with segment-level anchoring.
    
    Strategy to prevent drift on punctuation-heavy text:
    1. Split both original and AI text into time windows (30s chunks)
    2. Align within each window independently
    3. Compute alignment confidence - if too low, fall back to original words
    4. Use improved regex tokenizer that handles URLs, code identifiers, etc.

    Args:
        original_words: List[{text, start, end, speaker}] from consensus
        ai_text: Corrected text string from AI model

    Returns:
        List[{text, start, end, speaker, source}] with AI text + original timestamps
    """
    # Strip timestamp/speaker formatting from AI output
    ai_text_clean = strip_transcript_formatting(ai_text)

    # Tokenize AI output with improved tokenizer
    ai_tokens = tokenize_preserving_punctuation(ai_text_clean)

    if not ai_tokens or not original_words:
        return original_words  # Fallback to original if no AI output

    # Check overall alignment confidence
    orig_normalized = [normalize_for_matching(w['text']) for w in original_words]
    ai_normalized = [normalize_for_matching(t) for t in ai_tokens]
    
    overall_confidence = compute_alignment_confidence(orig_normalized, ai_normalized)
    
    # If confidence is very low, fall back to original words
    if overall_confidence < 0.4:
        print(f"      Warning: Low alignment confidence ({overall_confidence:.2%}), using original words")
        return original_words
    
    # Segment-level anchoring: split into 30-second time windows
    WINDOW_SIZE = 30.0  # seconds
    
    if not original_words:
        return []
    
    # Find time boundaries
    min_time = original_words[0]['start']
    max_time = original_words[-1]['end']
    
    # If transcript is short, just align it all at once
    if max_time - min_time <= WINDOW_SIZE:
        return align_segment(original_words, ai_tokens, 0, 0)
    
    # Split original words into time windows
    windows = []
    current_window = []
    window_start_time = min_time
    
    for word in original_words:
        if word['start'] >= window_start_time + WINDOW_SIZE and current_window:
            windows.append(current_window)
            current_window = []
            window_start_time = word['start']
        current_window.append(word)
    
    if current_window:
        windows.append(current_window)
    
    # Align AI tokens to time windows
    # Strategy: distribute AI tokens proportionally to each window based on word count
    aligned_words = []
    ai_idx = 0
    
    for window_words in windows:
        # Estimate how many AI tokens correspond to this window
        window_orig_count = len(window_words)
        window_ai_count = int(len(ai_tokens) * window_orig_count / len(original_words))
        
        # Get AI tokens for this window (with some overlap tolerance)
        window_ai_tokens = ai_tokens[ai_idx:ai_idx + window_ai_count + 5]  # +5 for tolerance
        
        # Align this segment
        if window_ai_tokens:
            segment_aligned = align_segment(window_words, window_ai_tokens, 0, ai_idx)
            aligned_words.extend(segment_aligned)
            
            # Advance AI token index by number of tokens consumed
            ai_idx += len([w for w in segment_aligned if w.get('source') in ['matched', 'ai_inserted']])
    
    return aligned_words if aligned_words else original_words


# =============================================================================
# Phase 3: AI Correction Pass
# =============================================================================

def load_intermediate_consensus(episode_name, intermediate_dir=Path("intermediates")):
    """Load intermediate consensus word-level JSON."""
    episode_dir = intermediate_dir / episode_name
    json_file = episode_dir / f"{episode_name}_intermediate_consensus_words.json"

    if not json_file.exists():
        return None, json_file

    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f), json_file


def words_to_text(words):
    """Convert word list to plain text for AI processing."""
    # Group by speaker segments
    segments = words_to_segments(words, max_gap=2.0)

    lines = []
    for seg in segments:
        lines.append(f"**[{seg['timestamp']}] {seg['speaker']}:** {seg['text']}")
        lines.append("")

    return '\n'.join(lines)


def process_with_ai_model(text, processor, api_key, context=""):
    """
    Process text with a single AI model via OpenRouter (or direct API for kimi).

    Returns the corrected text from the AI model.
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("openai package not installed. Install with: pip install openai")

    # Import model configs from post-processing script
    sys.path.insert(0, str(Path(__file__).parent))
    from process_single_post_process import (
        OPENROUTER_MODELS,
        OPENROUTER_MAX_TOKENS,
        SYSTEM_PROMPT,
        INSTRUCTION_TEMPLATE,
        strip_ai_preamble,
        DIRECT_API_CONFIG,
    )

    # Special handling for kimi: use direct Moonshot API if available
    # Kimi K2.5 via OpenRouter returns content in 'reasoning' field, not 'content'
    if processor == 'kimi':
        moonshot_key = os.environ.get('MOONSHOT_API_KEY', '').strip()
        if moonshot_key:
            config = DIRECT_API_CONFIG['kimi']
            client = OpenAI(
                api_key=moonshot_key,
                base_url=config['base_url']
            )
            prompt = INSTRUCTION_TEMPLATE.format(context=context, transcript=text)

            print(f"      Processing with {processor} (direct API): ", end='', flush=True)

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
                    text_chunk = delta.content
                    if text_chunk:
                        result += text_chunk
                        chunk_count += 1
                        if chunk_count % 100 == 0:
                            print(".", end='', flush=True)

            print(" done")
            result = strip_ai_preamble(result)
            return result

    model_id = OPENROUTER_MODELS.get(processor)
    if not model_id:
        raise ValueError(f"Unknown processor: {processor}")

    max_tokens = OPENROUTER_MAX_TOKENS.get(processor, OPENROUTER_MAX_TOKENS['default'])

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )

    prompt = INSTRUCTION_TEMPLATE.format(context=context, transcript=text)

    print(f"      Processing with {processor}: ", end='', flush=True)

    result = ""
    chunk_count = 0

    stream = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        stream=True,
        extra_headers={
            "HTTP-Referer": "https://github.com/strato-net/strato-transcripts",
            "X-Title": "Strato Transcripts"
        }
    )

    for chunk in stream:
        if chunk.choices:
            delta = chunk.choices[0].delta
            # Only capture content, NOT reasoning (reasoning models output thinking which pollutes transcripts)
            text_chunk = delta.content
            if text_chunk:
                result += text_chunk
                chunk_count += 1
                if chunk_count % 100 == 0:
                    print(".", end='', flush=True)

    print(" done")

    # Strip any thinking/preamble from the output (reasoning models often include this)
    result = strip_ai_preamble(result)

    return result


def run_ai_correction_pass(episode_name, processors, intermediate_dir=Path("intermediates")):
    """
    Phase 3: Process intermediate consensus with all AI models.

    For each AI model:
      1. Load intermediate consensus words
      2. Convert to text
      3. Send to AI for correction
      4. Align AI output back to word-level
      5. Save as {episode}_ai_{model}_words.json
    """
    print("\n" + "="*70)
    print("PHASE 3: AI Correction Pass")
    print("="*70)

    # Load intermediate consensus
    consensus_words, source_file = load_intermediate_consensus(episode_name, intermediate_dir)
    if not consensus_words:
        print(f"Error: Intermediate consensus not found: {source_file}")
        print("Run transcriber consensus first:")
        print(f"  python3 scripts/assess_quality.py --intermediate-consensus --episode {episode_name}")
        return False

    print(f"Loaded {len(consensus_words)} words from {source_file}")

    # Convert to text for AI processing
    text = words_to_text(consensus_words)
    print(f"Converted to {len(text)} characters of text")

    # Validate API key
    api_key, error = validate_api_key('OPENROUTER_API_KEY')
    if error:
        print(f"Error: {error}")
        print("Get your API key from: https://openrouter.ai/keys")
        return False

    # Build context
    from process_single_post_process import build_context_summary
    context = build_context_summary()

    # Process with each AI model
    episode_dir = intermediate_dir / episode_name
    success_count = 0

    for i, processor in enumerate(processors):
        print(f"\n[{i+1}/{len(processors)}] Processing with {processor}...")

        output_file = episode_dir / f"{episode_name}_ai_{processor}_words.json"

        # Skip if already exists
        if output_file.exists():
            print(f"      Skipping: {output_file.name} already exists")
            success_count += 1
            continue

        try:
            start_time = time.time()

            # Get AI correction
            corrected_text = process_with_ai_model(text, processor, api_key, context)

            # Align back to word-level
            aligned_words = align_ai_to_original(consensus_words, corrected_text)

            # Save
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(aligned_words, f, indent=2)

            elapsed = time.time() - start_time
            print(f"      {success(f'Saved {len(aligned_words)} words to {output_file.name} ({elapsed:.1f}s)')}")
            success_count += 1

        except Exception as e:
            print(f"      {failure(f'Failed: {e}')}")

    print(f"\nPhase 3 complete: {success_count}/{len(processors)} models processed")
    return success_count > 0


# =============================================================================
# Phase 4: AI Consensus
# =============================================================================

def build_ai_consensus(episode_name, intermediate_dir=Path("intermediates")):
    """
    Phase 4: Build consensus from all AI word lists.

    Uses the same alignment algorithm as transcriber consensus,
    but with larger time tolerance (0.5s) for AI outputs.
    """
    print("\n" + "="*70)
    print("PHASE 4: AI Consensus")
    print("="*70)

    episode_dir = intermediate_dir / episode_name

    # Load all AI word lists
    ai_word_lists = {}
    for model in AI_MODELS:
        json_file = episode_dir / f"{episode_name}_ai_{model}_words.json"
        if json_file.exists():
            with open(json_file, 'r', encoding='utf-8') as f:
                ai_word_lists[model] = json.load(f)
                print(f"  Loaded {len(ai_word_lists[model])} words from {model}")

    if not ai_word_lists:
        print("Error: No AI word lists found. Run Phase 3 first.")
        return False

    print(f"\nBuilding consensus from {len(ai_word_lists)} AI models...")

    # Align by time (larger tolerance for AI outputs)
    aligned = align_words_by_time(ai_word_lists, time_tolerance=0.5)
    print(f"  Aligned {len(aligned)} word positions")

    # Build consensus
    glossary = load_glossary()
    consensus_words = build_word_level_consensus_text(aligned, glossary)
    print(f"  Built consensus with {len(consensus_words)} words")

    # Calculate agreement statistics
    agreements = [w.get('agreement', 1.0) for w in consensus_words]
    avg_agreement = sum(agreements) / len(agreements) if agreements else 0
    high_agreement = sum(1 for a in agreements if a >= 0.8) / len(agreements) if agreements else 0

    print(f"  Average agreement: {avg_agreement:.1%}")
    print(f"  High agreement (>=80%): {high_agreement:.1%}")

    # Save
    output_file = episode_dir / f"{episode_name}_ai_consensus_words.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(consensus_words, f, indent=2)

    print(f"\n{success(f'Saved AI consensus to {output_file}')}")
    return True


# =============================================================================
# Phase 2.5: Transcriber Quality Assessment
# =============================================================================

TRANSCRIBERS = ['whisperx', 'whisperx-cloud', 'assemblyai']


def assess_transcriber_quality(episode_name, intermediate_dir=Path("intermediates")):
    """
    Assess each transcriber's quality by comparing to the intermediate consensus.

    Calculates:
    - Consensus alignment: How similar is the transcriber output to consensus
    - Word count and length ratio
    - Speaker detection: How well did it detect speakers
    - Word agreement: How often was this transcriber's word chosen in consensus

    Returns dict of {transcriber: {metrics}} sorted by quality score.
    """
    print("\n" + "="*70)
    print("Transcriber Quality Assessment")
    print("="*70)

    episode_dir = intermediate_dir / episode_name

    # Load intermediate consensus (output from transcriber consensus)
    consensus_file = episode_dir / f"{episode_name}_intermediate_consensus_words.json"
    if not consensus_file.exists():
        print(f"Error: Intermediate consensus not found: {consensus_file}")
        return None

    with open(consensus_file, 'r', encoding='utf-8') as f:
        consensus_words = json.load(f)

    consensus_text = ' '.join(normalize_for_matching(w['text']) for w in consensus_words)
    consensus_speakers = set(w.get('speaker', 'UNKNOWN') for w in consensus_words)

    print(f"Consensus: {len(consensus_words)} words, {len(consensus_speakers)} speakers\n")

    # Load and compare each transcriber
    results = {}

    for transcriber in TRANSCRIBERS:
        # Try consensus_words.json first, then _words.json
        json_file = episode_dir / f"{episode_name}_{transcriber}_consensus_words.json"
        if not json_file.exists():
            json_file = episode_dir / f"{episode_name}_{transcriber}_words.json"
        if not json_file.exists():
            continue

        with open(json_file, 'r', encoding='utf-8') as f:
            transcriber_words = json.load(f)

        transcriber_text = ' '.join(normalize_for_matching(w['text']) for w in transcriber_words)

        # 1. Consensus alignment: How similar is transcriber output to consensus?
        consensus_matcher = SequenceMatcher(None, consensus_text, transcriber_text)
        consensus_alignment = consensus_matcher.ratio()

        # 2. Length ratio: Is output length close to consensus?
        length_ratio = len(transcriber_words) / len(consensus_words) if consensus_words else 0
        if 0.9 <= length_ratio <= 1.1:
            length_score = 1.0
        else:
            length_score = max(0, 1.0 - abs(1.0 - length_ratio) * 0.5)

        # 3. Speaker detection: How many unique speakers did it find?
        transcriber_speakers = set(w.get('speaker', 'UNKNOWN') for w in transcriber_words)
        # Penalize if too few or too many speakers vs consensus
        speaker_diff = abs(len(transcriber_speakers) - len(consensus_speakers))
        speaker_score = max(0, 1.0 - speaker_diff * 0.2)

        # 4. Word agreement: Count words that match consensus
        # Use aligned words to see which were chosen
        agreement_count = 0
        for cword in consensus_words:
            ctext = normalize_for_matching(cword['text'])
            cstart = cword['start']
            # Find matching word in transcriber output (within 0.3s)
            for tword in transcriber_words:
                if abs(tword['start'] - cstart) <= 0.3:
                    if normalize_for_matching(tword['text']) == ctext:
                        agreement_count += 1
                    break

        agreement_ratio = agreement_count / len(consensus_words) if consensus_words else 0

        # 5. Timing quality: Check if timestamps are reasonable
        # Look for gaps or overlaps that shouldn't exist
        timing_issues = 0
        for i in range(1, len(transcriber_words)):
            gap = transcriber_words[i]['start'] - transcriber_words[i-1]['end']
            if gap < -0.5:  # Major overlap
                timing_issues += 1
            elif gap > 5.0:  # Major gap
                timing_issues += 1
        timing_score = max(0, 1.0 - timing_issues / max(1, len(transcriber_words)) * 10)

        # Combined quality score
        quality_score = (
            consensus_alignment * 0.35 +   # Primary: alignment with consensus
            agreement_ratio * 0.30 +       # Word-level agreement
            length_score * 0.15 +          # Reasonable length
            speaker_score * 0.10 +         # Speaker detection
            timing_score * 0.10            # Timing quality
        )

        results[transcriber] = {
            'word_count': len(transcriber_words),
            'consensus_alignment': consensus_alignment,
            'agreement_ratio': agreement_ratio,
            'length_score': length_score,
            'speaker_count': len(transcriber_speakers),
            'speaker_score': speaker_score,
            'timing_score': timing_score,
            'quality_score': quality_score,
        }

    if not results:
        print("No transcriber data found")
        return None

    # Sort by quality score
    sorted_results = sorted(results.items(), key=lambda x: x[1]['quality_score'], reverse=True)

    # Print results table
    print(f"{'Transcriber':<15} {'Words':>6} {'Align':>7} {'Agree':>7} {'Length':>7} {'Spkrs':>6} {'Timing':>7} {'Quality':>8}")
    print("-" * 75)

    for transcriber, metrics in sorted_results:
        print(f"{transcriber:<15} {metrics['word_count']:>6} "
              f"{metrics['consensus_alignment']:>6.1%} "
              f"{metrics['agreement_ratio']:>6.1%} "
              f"{metrics['length_score']:>6.1%} "
              f"{metrics['speaker_count']:>6} "
              f"{metrics['timing_score']:>6.1%} "
              f"{metrics['quality_score']:>7.1%}")

    # Recommendations
    print("\n" + "-" * 75)
    best = sorted_results[0][0] if sorted_results else None
    print(f"Best transcriber: {best}")

    if len(sorted_results) > 1:
        scores = [m['quality_score'] for _, m in sorted_results]
        score_spread = max(scores) - min(scores)
        if score_spread < 0.05:
            print("Note: All transcribers performed similarly (within 5%)")
        elif score_spread > 0.15:
            print(f"Note: Significant quality difference ({score_spread:.1%} spread)")

    # Save results
    output_file = episode_dir / f"{episode_name}_transcriber_quality_assessment.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'consensus_word_count': len(consensus_words),
            'consensus_speaker_count': len(consensus_speakers),
            'transcribers': dict(sorted_results),
            'best_transcriber': best,
        }, f, indent=2)

    print(f"\n{success(f'Saved quality assessment to {output_file}')}")

    return dict(sorted_results)


# =============================================================================
# Phase 4.5: AI Quality Assessment
# =============================================================================

def assess_ai_quality(episode_name, intermediate_dir=Path("intermediates")):
    """
    Assess each AI model's quality by comparing to the intermediate consensus
    (the input) and the final consensus (the output).

    Calculates:
    - Input preservation: How well did the AI preserve the original content
    - Consensus contribution: How often was this AI's word chosen in consensus
    - Format compliance: Did the AI follow the expected output format

    Returns dict of {model: {metrics}} sorted by quality score.
    """
    print("\n" + "="*70)
    print("AI Quality Assessment")
    print("="*70)

    episode_dir = intermediate_dir / episode_name

    # Load intermediate consensus (input to AI models)
    input_file = episode_dir / f"{episode_name}_intermediate_consensus_words.json"
    if not input_file.exists():
        print(f"Error: Intermediate consensus not found: {input_file}")
        return None

    with open(input_file, 'r', encoding='utf-8') as f:
        input_words = json.load(f)

    input_text = ' '.join(normalize_for_matching(w['text']) for w in input_words)

    # Load AI consensus (output from consensus building)
    consensus_file = episode_dir / f"{episode_name}_ai_consensus_words.json"
    if not consensus_file.exists():
        print(f"Error: AI consensus not found: {consensus_file}")
        return None

    with open(consensus_file, 'r', encoding='utf-8') as f:
        consensus_words = json.load(f)

    consensus_text = ' '.join(normalize_for_matching(w['text']) for w in consensus_words)

    print(f"Input (intermediate consensus): {len(input_words)} words")
    print(f"Output (AI consensus): {len(consensus_words)} words\n")

    # Load and compare each AI model
    results = {}

    for model in AI_MODELS:
        json_file = episode_dir / f"{episode_name}_ai_{model}_words.json"
        if not json_file.exists():
            continue

        with open(json_file, 'r', encoding='utf-8') as f:
            model_words = json.load(f)

        model_text = ' '.join(normalize_for_matching(w['text']) for w in model_words)

        # 1. Input preservation: How similar is AI output to input?
        # Higher = AI preserved more of the original content
        input_matcher = SequenceMatcher(None, input_text, model_text)
        input_preservation = input_matcher.ratio()

        # 2. Consensus alignment: How similar is AI output to final consensus?
        # Higher = AI output was closer to what the consensus chose
        consensus_matcher = SequenceMatcher(None, consensus_text, model_text)
        consensus_alignment = consensus_matcher.ratio()

        # 3. Length ratio: Is output length reasonable?
        # We want output close to input length (not too short, not too padded)
        length_ratio = len(model_words) / len(input_words) if input_words else 0
        # Score: 1.0 at ratio 1.0, decreasing as it deviates
        # Allow some expansion (up to 1.2x) without penalty
        if 0.8 <= length_ratio <= 1.2:
            length_score = 1.0
        else:
            length_score = max(0, 1.0 - abs(1.0 - length_ratio) * 0.5)

        # 4. Format compliance: Check if AI preserved speaker labels
        speakers_preserved = sum(1 for w in model_words if w.get('speaker', '').startswith('SPEAKER_'))
        format_score = min(1.0, speakers_preserved / len(model_words)) if model_words else 0

        # Combined quality score
        quality_score = (
            input_preservation * 0.3 +    # Preserve original content
            consensus_alignment * 0.4 +   # Align with consensus
            length_score * 0.2 +          # Reasonable length
            format_score * 0.1            # Follow format
        )

        results[model] = {
            'word_count': len(model_words),
            'input_preservation': input_preservation,
            'consensus_alignment': consensus_alignment,
            'length_score': length_score,
            'format_score': format_score,
            'quality_score': quality_score,
        }

    # Sort by quality score
    sorted_results = sorted(results.items(), key=lambda x: x[1]['quality_score'], reverse=True)

    # Print results table
    print(f"{'Model':<12} {'Words':>6} {'Input':>7} {'Consens':>8} {'Length':>7} {'Format':>7} {'Quality':>8}")
    print("-" * 65)

    for model, metrics in sorted_results:
        print(f"{model:<12} {metrics['word_count']:>6} "
              f"{metrics['input_preservation']:>6.1%} "
              f"{metrics['consensus_alignment']:>7.1%} "
              f"{metrics['length_score']:>6.1%} "
              f"{metrics['format_score']:>6.1%} "
              f"{metrics['quality_score']:>7.1%}")

    # Recommendations
    print("\n" + "-" * 65)
    top_5 = [m for m, _ in sorted_results[:5]]
    bottom_3 = [m for m, _ in sorted_results[-3:]]
    print(f"Top 5 models: {', '.join(top_5)}")
    print(f"Bottom 3 models: {', '.join(bottom_3)}")
    print(f"\nRecommended for cost-effective runs:")
    print(f"  --processors {','.join(top_5)}")

    # Save results
    output_file = episode_dir / f"{episode_name}_ai_quality_assessment.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'input_word_count': len(input_words),
            'consensus_word_count': len(consensus_words),
            'models': dict(sorted_results),
            'top_5': top_5,
            'bottom_3': bottom_3,
        }, f, indent=2)

    print(f"\n{success(f'Saved quality assessment to {output_file}')}")

    return dict(sorted_results)


# =============================================================================
# Phase 5: Filler Word Removal
# =============================================================================

def is_filler_like(words, idx):
    """
    Context-aware detection of "like" as filler vs semantic usage.
    
    Filler cases:
    - "I was like oh my god" (quotative)
    - "It's like you know" (hesitation)
    - "Like I said" (sentence start)
    - "He was like yeah" (quotative)
    
    Semantic cases (keep these):
    - "It looks like rain" (comparison/resemblance)
    - "Systems like Ethereum" (exemplification)
    - "Feels like home" (simile)
    - "Smells like victory" (comparison)
    
    Returns True if "like" is filler (should be removed).
    """
    if idx < 0 or idx >= len(words):
        return False
    
    word = words[idx]
    normalized = normalize_for_matching(word['text'])
    
    if normalized != 'like':
        return False
    
    # Check previous word (if exists)
    prev_word = None
    prev_norm = None
    if idx > 0:
        prev_word = words[idx - 1]
        prev_norm = normalize_for_matching(prev_word['text'])
    
    # Check next word (if exists)
    next_word = None
    next_norm = None
    if idx < len(words) - 1:
        next_word = words[idx + 1]
        next_norm = normalize_for_matching(next_word['text'])
    
    # Pattern: "was/were/is/am like" (quotative - FILLER)
    if prev_norm in ['was', 'were', 'is', 'am', "i'm", "he's", "she's", "they're", "we're"]:
        return True
    
    # Pattern: "like I/you/he/she/we/they" at sentence start (FILLER)
    # Check if previous word ends with sentence boundary
    if prev_word is None or any(prev_word['text'].endswith(p) for p in ['.', '!', '?']):
        if next_norm in ['i', 'you', 'he', 'she', 'we', 'they', 'it']:
            return True
    
    # Pattern: "looks/feels/sounds/seems/acts/smells like" (comparison - KEEP)
    if prev_norm in ['looks', 'feels', 'sounds', 'seems', 'acts', 'smells', 'tastes', 'appears']:
        return False
    
    # Pattern: "systems/things/projects/tools/frameworks like X" (exemplification - KEEP)
    # Check if previous word is a plural noun (rough heuristic)
    if prev_norm and prev_norm.endswith('s') and prev_norm not in ['was', 'is', 'this', 'has', 'does']:
        # Likely "things like X" - keep it
        return False
    
    # Pattern: "something/nothing/anything like" (comparison - KEEP)
    if prev_norm in ['something', 'nothing', 'anything', 'everything']:
        return False
    
    # Default: treat as filler if not clearly semantic
    # Conservative: if followed by a determiner or noun, likely semantic
    if next_norm in ['a', 'an', 'the', 'this', 'that', 'these', 'those']:
        return False
    
    # If we're not sure, lean toward keeping it (avoid over-removal)
    return False


def is_sentence_boundary(word):
    """Check if word ends with sentence-ending punctuation."""
    text = word.get('text', '')
    return any(text.endswith(p) for p in ['.', '!', '?'])


def is_filler_word(word_text):
    """Check if a word is a single-word filler (excluding 'like' which needs context)."""
    normalized = normalize_for_matching(word_text)
    return normalized in SINGLE_WORD_FILLERS


def remove_consecutive_duplicates(words):
    """
    Remove consecutive duplicate words that result from alignment disagreements.

    When AI models disagree on word boundaries, we can end up with:
    - "Bob Bob Summerwill" instead of "Bob Summerwill"
    - "recording recording" instead of "recording"
    - "pre-formation formation" instead of "pre-formation" (hyphenated suffix)
    - "T T-shirt" instead of "T-shirt" (hyphenated prefix)

    This function detects and removes such duplicates.
    """
    if not words:
        return words, 0

    result = [words[0]]
    removed = 0

    for i in range(1, len(words)):
        curr_word = words[i]
        prev_word = result[-1]

        # Normalize for comparison (lowercase, strip punctuation from ends)
        curr_norm = normalize_for_matching(curr_word['text'])
        prev_norm = normalize_for_matching(prev_word['text'])

        # Get raw text for hyphen checks
        curr_raw = curr_word['text'].lower()
        prev_raw = prev_word['text'].lower()

        # Check if same speaker and close in time
        same_context = (
            curr_word['speaker'] == prev_word['speaker'] and
            curr_word['start'] - prev_word['end'] < 1.0  # Within 1 second
        )

        # Check various duplicate patterns
        is_duplicate = False
        keep_current = False
        force_keep_previous = False

        if same_context:
            # Pattern 1: Exact duplicate (e.g., "Bob Bob")
            if curr_norm == prev_norm:
                is_duplicate = True

            # Pattern 2: Previous word ends with current word (e.g., "pre-formation" + "formation")
            # Check if prev contains hyphen and ends with curr - keep the longer previous word
            elif '-' in prev_raw and prev_norm.endswith(curr_norm) and len(curr_norm) >= 3:
                is_duplicate = True
                force_keep_previous = True  # Always keep the longer hyphenated word

            # Pattern 3: Current word starts with previous word (e.g., "T" + "T-shirt")
            # Check if curr contains hyphen and starts with prev
            elif '-' in curr_raw and curr_norm.startswith(prev_norm) and len(prev_norm) >= 1:
                is_duplicate = True
                keep_current = True  # Keep the longer word

        if is_duplicate:
            removed += 1
            # Keep the better word (but respect force flags)
            if not force_keep_previous and (keep_current or curr_word.get('agreement', 0) > prev_word.get('agreement', 0)):
                result[-1] = curr_word
        else:
            result.append(curr_word)

    return result, removed


def remove_filler_words(episode_name, intermediate_dir=Path("intermediates")):
    """
    Phase 5: Filter out filler words from AI consensus.
    """
    print("\n" + "="*70)
    print("PHASE 5: Filler Word Removal")
    print("="*70)

    episode_dir = intermediate_dir / episode_name

    # Load AI consensus
    input_file = episode_dir / f"{episode_name}_ai_consensus_words.json"
    if not input_file.exists():
        print(f"Error: AI consensus not found: {input_file}")
        print("Run Phase 4 first.")
        return False

    with open(input_file, 'r', encoding='utf-8') as f:
        words = json.load(f)

    print(f"Loaded {len(words)} words from AI consensus")

    # Filter out filler words
    filtered = []
    removed_count = 0

    for word in words:
        if is_filler_word(word['text']):
            removed_count += 1
        else:
            filtered.append(word)

    print(f"Removed {removed_count} filler words ({removed_count/len(words)*100:.1f}%)")

    # Remove consecutive duplicate words
    filtered, dup_count = remove_consecutive_duplicates(filtered)
    if dup_count > 0:
        print(f"Removed {dup_count} consecutive duplicate words")

    print(f"Remaining: {len(filtered)} words")

    # Save
    output_file = episode_dir / f"{episode_name}_final_words.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=2)

    print(f"\n{success(f'Saved final words to {output_file}')}")
    return True


# =============================================================================
# Phase 6: Final Output
# =============================================================================

def generate_final_output(episode_name, intermediate_dir=Path("intermediates"), output_dir=Path("outputs")):
    """
    Phase 6: Generate final .md and .txt from word-level data.
    """
    print("\n" + "="*70)
    print("PHASE 6: Final Output Generation")
    print("="*70)

    episode_dir = intermediate_dir / episode_name

    # Load final words
    input_file = episode_dir / f"{episode_name}_final_words.json"
    if not input_file.exists():
        print(f"Error: Final words not found: {input_file}")
        print("Run Phase 5 first.")
        return False

    with open(input_file, 'r', encoding='utf-8') as f:
        words = json.load(f)

    print(f"Loaded {len(words)} words")

    # Convert to segments
    segments = words_to_segments(words, max_gap=2.0)
    print(f"Grouped into {len(segments)} segments")

    # Create output directory
    episode_output_dir = output_dir / episode_name
    episode_output_dir.mkdir(parents=True, exist_ok=True)

    # Generate markdown
    md_lines = []
    for seg in segments:
        md_lines.append(f"**[{seg['timestamp']}] {seg['speaker']}:** {seg['text']}")
        md_lines.append("")

    md_content = '\n'.join(md_lines)
    md_file = episode_output_dir / f"{episode_name}_final.md"
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"  Generated: {md_file}")

    # Generate plain text (no timestamps, no markdown)
    txt_lines = []
    for seg in segments:
        txt_lines.append(f"{seg['speaker']}: {seg['text']}")
        txt_lines.append("")

    txt_content = '\n'.join(txt_lines)
    txt_file = episode_output_dir / f"{episode_name}_final.txt"
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(txt_content)

    print(f"  Generated: {txt_file}")

    # Also save final words JSON to outputs
    json_file = episode_output_dir / f"{episode_name}_final_words.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(words, f, indent=2)

    print(f"  Generated: {json_file}")

    # Summary statistics
    word_count = len(words)
    speaker_count = len(set(w['speaker'] for w in words))
    duration = words[-1]['end'] if words else 0

    print(f"\n{success('Final output generated!')}")
    print(f"  Words: {word_count}")
    print(f"  Speakers: {speaker_count}")
    print(f"  Duration: {int(duration//60)}:{int(duration%60):02d}")

    return True


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Multi-Phase AI Consensus Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full pipeline (Phases 3-6)
  python3 scripts/ai_consensus_pipeline.py --episode episode003-bob-summerwill

  # Run specific phase
  python3 scripts/ai_consensus_pipeline.py --episode episode003-bob-summerwill --phase 3

  # Run with subset of AI models (for testing)
  python3 scripts/ai_consensus_pipeline.py --episode episode003-bob-summerwill --processors opus,gemini,grok

  # Assess transcriber quality (after building intermediate consensus)
  python3 scripts/ai_consensus_pipeline.py --episode episode003-bob-summerwill --phase transcriber

  # Assess AI quality only (after Phase 4)
  python3 scripts/ai_consensus_pipeline.py --episode episode003-bob-summerwill --phase assess

Prerequisites:
  Run transcriber consensus first (Phases 1-2):
  python3 scripts/assess_quality.py --intermediate-consensus --episode <name>
        """
    )

    parser.add_argument('--episode', required=True,
                        help='Episode name (e.g., episode003-bob-summerwill)')
    parser.add_argument('--processors', default='all',
                        help='Comma-separated AI models or "all" (default: all)')
    parser.add_argument('--phase', choices=['transcriber', '3', '4', 'assess', '5', '6', 'all'], default='all',
                        help='Run specific phase or all (default: all). "transcriber" assesses transcriber quality, "assess" assesses AI quality.')
    parser.add_argument('--intermediate-dir', default='intermediates',
                        help='Directory for intermediate files (default: intermediates)')
    parser.add_argument('--output-dir', default='outputs',
                        help='Directory for final output (default: outputs)')

    args = parser.parse_args()

    # Parse processors
    if args.processors.lower() == 'all':
        processors = AI_MODELS
    else:
        processors = [p.strip() for p in args.processors.split(',')]
        for p in processors:
            if p not in AI_MODELS:
                print(f"Error: Unknown processor '{p}'")
                print(f"Valid processors: {', '.join(AI_MODELS)}")
                sys.exit(1)

    intermediate_dir = Path(args.intermediate_dir)
    output_dir = Path(args.output_dir)

    print("="*70)
    print("Multi-Phase AI Consensus Pipeline")
    print("="*70)
    print(f"Episode: {args.episode}")
    print(f"Processors: {', '.join(processors)}")
    print(f"Phase: {args.phase}")
    print("="*70)

    pipeline_start = time.time()

    # Run phases

    # Transcriber quality assessment (Phase 2.5 - after intermediate consensus is built)
    if args.phase == 'transcriber':
        assess_transcriber_quality(args.episode, intermediate_dir)
        # Exit early if only transcriber assessment was requested
        elapsed = time.time() - pipeline_start
        print(f"\n{'='*70}")
        print(f"Transcriber assessment completed in {elapsed:.1f}s")
        sys.exit(0)

    if args.phase in ['3', 'all']:
        if not run_ai_correction_pass(args.episode, processors, intermediate_dir):
            if args.phase == '3':
                sys.exit(1)

    if args.phase in ['4', 'all']:
        if not build_ai_consensus(args.episode, intermediate_dir):
            if args.phase == '4':
                sys.exit(1)

    # AI quality assessment (after Phase 4, before Phase 5)
    if args.phase in ['assess', 'all']:
        assess_ai_quality(args.episode, intermediate_dir)

    if args.phase in ['5', 'all']:
        if not remove_filler_words(args.episode, intermediate_dir):
            if args.phase == '5':
                sys.exit(1)

    if args.phase in ['6', 'all']:
        if not generate_final_output(args.episode, intermediate_dir, output_dir):
            if args.phase == '6':
                sys.exit(1)

    # Summary
    pipeline_elapsed = time.time() - pipeline_start

    print("\n" + "="*70)
    print(f"{success('Pipeline Complete!')}")
    print("="*70)
    print(f"Total time: {pipeline_elapsed:.1f}s ({pipeline_elapsed/60:.1f}min)")

    if args.phase == 'all' or args.phase == '6':
        print(f"\nFinal outputs:")
        print(f"  {output_dir}/{args.episode}/{args.episode}_final.md")
        print(f"  {output_dir}/{args.episode}/{args.episode}_final.txt")


if __name__ == "__main__":
    main()
