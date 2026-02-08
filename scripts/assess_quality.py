#!/usr/bin/env python3
"""
Quality Assessment and Consensus Building for Transcript Pipeline

Analyzes quality at two levels:
1. Intermediate: Raw transcripts from 3 transcribers (whisperx, whisperx-cloud, assemblyai)
2. Output: Post-processed transcripts from 11 AI providers

Generates consensus transcripts by combining best elements from multiple sources.
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from difflib import SequenceMatcher
import statistics

# =============================================================================
# Constants
# =============================================================================

TRANSCRIBERS = ['whisperx', 'whisperx-cloud', 'assemblyai']
PROCESSORS = ['opus', 'gemini', 'deepseek', 'chatgpt', 'qwen', 'kimi', 'glm',
              'minimax', 'llama', 'grok', 'mistral']

# =============================================================================
# Utility Functions
# =============================================================================

def count_words(text):
    """Count words in text, excluding speaker labels and timestamps."""
    # Remove speaker labels like **[00:01] SPEAKER_00:**
    cleaned = re.sub(r'\*\*\[\d+:\d+\]\s+SPEAKER_\d+:\*\*', '', text)
    # Remove plain speaker labels like SPEAKER_00:
    cleaned = re.sub(r'SPEAKER_\d+:', '', cleaned)
    # Remove markdown formatting
    cleaned = re.sub(r'\*\*', '', cleaned)
    # Count words
    words = cleaned.split()
    return len(words)


def extract_text_content(text):
    """Extract just the spoken content, removing formatting."""
    # Remove speaker labels and timestamps
    cleaned = re.sub(r'\*\*\[\d+:\d+\]\s+SPEAKER_\d+:\*\*', '', text)
    cleaned = re.sub(r'SPEAKER_\d+:', '', cleaned)
    cleaned = re.sub(r'\*\*', '', cleaned)
    cleaned = re.sub(r'\[\d+:\d+\]', '', cleaned)
    # Normalize whitespace
    cleaned = ' '.join(cleaned.split())
    return cleaned.lower()


def similarity_ratio(text1, text2):
    """Compute similarity ratio between two texts (0-1)."""
    content1 = extract_text_content(text1)
    content2 = extract_text_content(text2)
    return SequenceMatcher(None, content1, content2).ratio()


def load_glossary():
    """Load ethereum_glossary.json if available."""
    glossary_path = Path("ethereum_glossary.json")
    if glossary_path.exists():
        with open(glossary_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"people": [], "technical_terms": [], "projects": []}


def find_glossary_terms(text, glossary):
    """Find glossary terms mentioned in text."""
    text_lower = text.lower()
    found = {
        'people': [],
        'technical_terms': [],
        'projects': []
    }

    for person in glossary.get('people', []):
        if person.lower() in text_lower:
            found['people'].append(person)

    for term in glossary.get('technical_terms', []):
        if term.lower() in text_lower:
            found['technical_terms'].append(term)

    for project in glossary.get('projects', []):
        if project.lower() in text_lower:
            found['projects'].append(project)

    return found


# =============================================================================
# Phase 1: Intermediate Quality Assessment
# =============================================================================

def assess_intermediate_quality(episode_dir):
    """
    Assess quality of raw transcripts from different transcribers.

    Returns dict with metrics for each transcriber.
    """
    episode_name = episode_dir.name
    results = {}

    for transcriber in TRANSCRIBERS:
        txt_file = episode_dir / f"{episode_name}_{transcriber}.txt"
        md_file = episode_dir / f"{episode_name}_{transcriber}.md"

        if not md_file.exists():
            continue

        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Basic metrics
        word_count = count_words(content)
        line_count = len(content.strip().split('\n'))

        # Speaker turn analysis
        speaker_turns = re.findall(r'SPEAKER_(\d+)', content)
        unique_speakers = len(set(speaker_turns))
        turn_count = len(speaker_turns)

        # Timestamp coverage
        timestamps = re.findall(r'\[(\d+):(\d+)\]', content)
        if timestamps:
            last_ts = int(timestamps[-1][0]) * 60 + int(timestamps[-1][1])
        else:
            last_ts = 0

        results[transcriber] = {
            'word_count': word_count,
            'line_count': line_count,
            'unique_speakers': unique_speakers,
            'speaker_turns': turn_count,
            'duration_seconds': last_ts,
            'file': str(md_file)
        }

    return results


def compare_intermediates(episode_dir):
    """
    Compare raw transcripts and compute agreement metrics.
    """
    episode_name = episode_dir.name
    contents = {}

    for transcriber in TRANSCRIBERS:
        md_file = episode_dir / f"{episode_name}_{transcriber}.md"
        if md_file.exists():
            with open(md_file, 'r', encoding='utf-8') as f:
                contents[transcriber] = f.read()

    if len(contents) < 2:
        return None

    # Compute pairwise similarity
    similarities = {}
    transcriber_list = list(contents.keys())
    for i, t1 in enumerate(transcriber_list):
        for t2 in transcriber_list[i+1:]:
            sim = similarity_ratio(contents[t1], contents[t2])
            similarities[f"{t1}_vs_{t2}"] = sim

    # Word count variance
    word_counts = {t: count_words(c) for t, c in contents.items()}
    if len(word_counts) > 1:
        wc_values = list(word_counts.values())
        wc_variance = statistics.stdev(wc_values) / statistics.mean(wc_values) if statistics.mean(wc_values) > 0 else 0
    else:
        wc_variance = 0

    return {
        'similarities': similarities,
        'word_counts': word_counts,
        'word_count_variance': wc_variance,
        'avg_similarity': statistics.mean(similarities.values()) if similarities else 0
    }


# =============================================================================
# Phase 2: Output Quality Assessment
# =============================================================================

def assess_output_quality(episode_dir, transcriber):
    """
    Assess quality of post-processed outputs for a given transcriber.

    Returns dict with metrics for each processor.
    """
    episode_name = episode_dir.name
    base_name = f"{episode_name}_{transcriber}"

    # Get input word count
    input_file = Path("intermediates") / episode_name / f"{base_name}.md"
    if input_file.exists():
        with open(input_file, 'r', encoding='utf-8') as f:
            input_word_count = count_words(f.read())
    else:
        input_word_count = None

    results = {}
    glossary = load_glossary()

    for processor in PROCESSORS:
        output_file = episode_dir / f"{base_name}_{processor}.txt"

        if not output_file.exists():
            continue

        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        word_count = count_words(content)

        # Word count ratio (target: 0.9-1.1)
        if input_word_count:
            wc_ratio = word_count / input_word_count
        else:
            wc_ratio = None

        # Check for preamble junk
        has_preamble = bool(re.match(r'^(Here is|Below is|I have)', content.strip(), re.IGNORECASE))

        # Format compliance
        has_proper_format = bool(re.search(r'\*\*\[\d+:\d+\]\s+SPEAKER_\d+:\*\*', content))

        # Glossary term coverage
        found_terms = find_glossary_terms(content, glossary)
        term_count = len(found_terms['people']) + len(found_terms['technical_terms'])

        results[processor] = {
            'word_count': word_count,
            'word_count_ratio': wc_ratio,
            'in_target_range': wc_ratio and 0.9 <= wc_ratio <= 1.1,
            'has_preamble': has_preamble,
            'has_proper_format': has_proper_format,
            'glossary_terms_found': term_count,
            'file': str(output_file)
        }

    return results, input_word_count


def compare_outputs(episode_dir, transcriber):
    """
    Compare post-processed outputs and compute agreement metrics.
    """
    episode_name = episode_dir.name
    base_name = f"{episode_name}_{transcriber}"
    contents = {}

    for processor in PROCESSORS:
        output_file = episode_dir / f"{base_name}_{processor}.txt"
        if output_file.exists():
            with open(output_file, 'r', encoding='utf-8') as f:
                contents[processor] = f.read()

    if len(contents) < 2:
        return None

    # Compute pairwise similarity (sample for efficiency)
    similarities = {}
    processor_list = list(contents.keys())

    # Compare each to all others (but limit for large sets)
    for i, p1 in enumerate(processor_list):
        for p2 in processor_list[i+1:]:
            sim = similarity_ratio(contents[p1], contents[p2])
            similarities[f"{p1}_vs_{p2}"] = sim

    # Word count stats
    word_counts = {p: count_words(c) for p, c in contents.items()}
    wc_values = list(word_counts.values())

    if len(wc_values) > 1:
        wc_mean = statistics.mean(wc_values)
        wc_stdev = statistics.stdev(wc_values)
        wc_variance = wc_stdev / wc_mean if wc_mean > 0 else 0
    else:
        wc_mean = wc_values[0] if wc_values else 0
        wc_stdev = 0
        wc_variance = 0

    # Find outliers (>2 stdev from mean)
    outliers = []
    if wc_stdev > 0:
        for p, wc in word_counts.items():
            if abs(wc - wc_mean) > 2 * wc_stdev:
                outliers.append(p)

    return {
        'word_counts': word_counts,
        'word_count_mean': wc_mean,
        'word_count_stdev': wc_stdev,
        'word_count_variance': wc_variance,
        'outliers': outliers,
        'avg_similarity': statistics.mean(similarities.values()) if similarities else 0,
        'min_similarity': min(similarities.values()) if similarities else 0,
        'max_similarity': max(similarities.values()) if similarities else 0
    }


# =============================================================================
# Provider Scoring
# =============================================================================

def score_provider(metrics):
    """
    Score a provider based on quality metrics.
    Higher score = better quality.
    """
    score = 0

    # Word count in target range: +30 points
    if metrics.get('in_target_range'):
        score += 30
    elif metrics.get('word_count_ratio'):
        # Partial credit for being close
        ratio = metrics['word_count_ratio']
        if 0.85 <= ratio <= 1.15:
            score += 20
        elif 0.8 <= ratio <= 1.2:
            score += 10

    # No preamble junk: +20 points
    if not metrics.get('has_preamble'):
        score += 20

    # Proper format: +20 points
    if metrics.get('has_proper_format'):
        score += 20

    # Glossary terms: up to +30 points
    terms = metrics.get('glossary_terms_found', 0)
    score += min(terms * 2, 30)

    return score


# =============================================================================
# Consensus Building - Selection (Simple)
# =============================================================================

def select_best_intermediate(episode_dir):
    """
    Select the best intermediate transcript based on quality metrics.

    Returns (best_transcriber, metrics)
    """
    metrics = assess_intermediate_quality(episode_dir)
    comparison = compare_intermediates(episode_dir)

    if not metrics:
        return None, None

    # Score each transcriber
    scores = {}
    for transcriber, m in metrics.items():
        score = 0
        # More words generally better (less truncation)
        score += m['word_count'] / 1000  # Normalize
        # More speaker turns = better diarization
        score += m['speaker_turns'] / 10
        # Prefer assemblyai for diarization quality
        if transcriber == 'assemblyai':
            score += 5
        scores[transcriber] = score

    best = max(scores, key=scores.get)
    return best, metrics[best]


def select_best_output(episode_dir, transcriber):
    """
    Select the best output transcript based on quality metrics.

    Returns (best_processor, metrics)
    """
    metrics, input_wc = assess_output_quality(episode_dir, transcriber)

    if not metrics:
        return None, None

    # Score each processor
    scores = {}
    for processor, m in metrics.items():
        scores[processor] = score_provider(m)

    best = max(scores, key=scores.get)
    return best, metrics[best]


# =============================================================================
# True Multi-Model Consensus Building
# =============================================================================

def parse_transcript_segments(content):
    """
    Parse a post-processed transcript into segments.

    Returns list of dicts: [{'timestamp': 'MM:SS', 'speaker': 'SPEAKER_XX', 'text': '...'}]
    """
    segments = []

    # Match pattern: **[MM:SS] SPEAKER_XX:** text
    # or just [MM:SS] SPEAKER_XX: text (txt format)
    pattern = r'\*?\*?\[(\d+:\d+)\]\s*(SPEAKER_\d+):?\*?\*?\s*(.*?)(?=\*?\*?\[\d+:\d+\]|\Z)'

    matches = re.findall(pattern, content, re.DOTALL)

    for timestamp, speaker, text in matches:
        # Clean up the text
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
        if text:
            segments.append({
                'timestamp': timestamp,
                'speaker': speaker,
                'text': text
            })

    return segments


def timestamp_to_seconds(ts):
    """Convert MM:SS to seconds."""
    parts = ts.split(':')
    return int(parts[0]) * 60 + int(parts[1])


def seconds_to_timestamp(secs):
    """Convert seconds to MM:SS."""
    secs = int(secs)
    return f"{secs // 60}:{secs % 60:02d}"


# =============================================================================
# Word-Level Alignment and Consensus
# =============================================================================

def load_word_level_json(episode_name, transcriber, intermediate_dir=Path("intermediates")):
    """
    Load word-level JSON for a transcriber.

    Returns list of word dicts: [{'text': str, 'start': float, 'end': float, 'speaker': str}]
    """
    episode_dir = intermediate_dir / episode_name

    # Try consensus_words.json first (from --consensus mode), then fall back to _words.json
    json_file = episode_dir / f"{episode_name}_{transcriber}_consensus_words.json"
    if not json_file.exists():
        json_file = episode_dir / f"{episode_name}_{transcriber}_words.json"

    if not json_file.exists():
        return None

    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def align_words_by_time(all_word_lists, time_tolerance=0.3):
    """
    Align words from multiple transcribers by time with sub-second precision.

    Groups words that start within time_tolerance seconds of each other.

    Args:
        all_word_lists: dict of {transcriber: [word_dicts]}
        time_tolerance: Maximum time difference for matching (default 0.3s)

    Returns:
        List of aligned word groups: [{'time': float, 'variants': {transcriber: word_dict}}]
    """
    if not all_word_lists:
        return []

    # Collect all words with their sources
    all_words = []
    for transcriber, words in all_word_lists.items():
        if words:
            for word in words:
                all_words.append({
                    'transcriber': transcriber,
                    'word': word
                })

    if not all_words:
        return []

    # Sort by start time
    all_words.sort(key=lambda x: x['word']['start'])

    # Group words within time tolerance
    aligned = []
    used = set()

    for i, item in enumerate(all_words):
        if i in used:
            continue

        group = {
            'time': item['word']['start'],
            'variants': {item['transcriber']: item['word']}
        }
        used.add(i)

        # Find matching words from other transcribers
        for j, other in enumerate(all_words):
            if j in used:
                continue
            if other['transcriber'] == item['transcriber']:
                continue
            if other['transcriber'] in group['variants']:
                continue

            time_diff = abs(other['word']['start'] - item['word']['start'])
            if time_diff <= time_tolerance:
                group['variants'][other['transcriber']] = other['word']
                used.add(j)

        aligned.append(group)

    return aligned


def build_word_level_consensus_text(aligned_words, glossary=None):
    """
    Build consensus text from aligned words.

    For each time position, vote on the word text among all transcribers.

    Args:
        aligned_words: Output from align_words_by_time()
        glossary: Optional glossary for term correction

    Returns:
        List of consensus word dicts: [{'text': str, 'start': float, 'end': float, 'speaker': str}]
    """
    consensus_words = []

    for group in aligned_words:
        variants = group['variants']

        if not variants:
            continue

        # Vote on text (case-insensitive comparison, preserve best case)
        text_votes = Counter()
        text_original = {}  # Preserve original casing
        for transcriber, word in variants.items():
            text_lower = word['text'].lower().strip('.,!?;:')
            text_votes[text_lower] += 1
            # Keep the version with more information (longer = likely has punctuation)
            if text_lower not in text_original or len(word['text']) > len(text_original[text_lower]):
                text_original[text_lower] = word['text']

        winner_lower = text_votes.most_common(1)[0][0]
        winner_text = text_original.get(winner_lower, winner_lower)

        # Vote on speaker
        speaker_votes = Counter()
        for transcriber, word in variants.items():
            speaker_votes[word['speaker']] += 1
        consensus_speaker = speaker_votes.most_common(1)[0][0]

        # Average the start/end times
        starts = [w['start'] for w in variants.values()]
        ends = [w['end'] for w in variants.values()]
        avg_start = sum(starts) / len(starts)
        avg_end = sum(ends) / len(ends)

        consensus_words.append({
            'text': winner_text,
            'start': avg_start,
            'end': avg_end,
            'speaker': consensus_speaker,
            'agreement': text_votes[winner_lower] / len(variants)
        })

    # Apply glossary corrections if available
    if glossary:
        consensus_words = apply_word_level_glossary(consensus_words, glossary)

    return consensus_words


def apply_word_level_glossary(words, glossary):
    """Apply glossary-based corrections to word list with timing."""
    # Build lowercase -> correct case mapping
    corrections = {}
    for person in glossary.get('people', []):
        corrections[person.lower()] = person
    for term in glossary.get('technical_terms', []):
        corrections[term.lower()] = term
    for project in glossary.get('projects', []):
        corrections[project.lower()] = project

    # Common Ethereum-specific corrections
    crypto_corrections = {
        'ether': 'Ether',
        'ethereum': 'Ethereum',
        'bitcoin': 'Bitcoin',
        'defi': 'DeFi',
        'nft': 'NFT',
        'nfts': 'NFTs',
        'dao': 'DAO',
        'daos': 'DAOs',
        'dapp': 'dApp',
        'dapps': 'dApps',
        'wei': 'Wei',
        'gwei': 'Gwei',
        'solidity': 'Solidity',
        'evm': 'EVM',
        'ipfs': 'IPFS',
        'devcon': 'Devcon',
        'vitalik': 'Vitalik',
        'buterin': 'Buterin',
    }
    corrections.update(crypto_corrections)

    for word in words:
        text_stripped = word['text'].lower().strip('.,!?;:')
        if text_stripped in corrections:
            # Preserve punctuation
            suffix = ''
            for char in word['text'][::-1]:
                if char in '.,!?;:':
                    suffix = char + suffix
                else:
                    break
            word['text'] = corrections[text_stripped] + suffix

    return words


def words_to_segments(consensus_words, max_gap=2.0):
    """
    Convert word-level consensus to speaker segments.

    Groups consecutive words by speaker with gap detection.

    Args:
        consensus_words: List of word dicts with timing
        max_gap: Maximum gap between words in same segment (seconds)

    Returns:
        List of segment dicts: [{'timestamp': 'MM:SS', 'speaker': str, 'text': str, 'start': float, 'end': float}]
    """
    if not consensus_words:
        return []

    segments = []
    current_segment = None

    for word in consensus_words:
        if current_segment is None:
            # Start new segment
            current_segment = {
                'speaker': word['speaker'],
                'start': word['start'],
                'end': word['end'],
                'words': [word['text']]
            }
        elif (word['speaker'] != current_segment['speaker'] or
              word['start'] - current_segment['end'] > max_gap):
            # Speaker change or gap - finish current segment
            current_segment['text'] = ' '.join(current_segment['words'])
            current_segment['timestamp'] = seconds_to_timestamp(current_segment['start'])
            del current_segment['words']
            segments.append(current_segment)

            # Start new segment
            current_segment = {
                'speaker': word['speaker'],
                'start': word['start'],
                'end': word['end'],
                'words': [word['text']]
            }
        else:
            # Continue current segment
            current_segment['end'] = word['end']
            current_segment['words'].append(word['text'])

    # Don't forget the last segment
    if current_segment and current_segment.get('words'):
        current_segment['text'] = ' '.join(current_segment['words'])
        current_segment['timestamp'] = seconds_to_timestamp(current_segment['start'])
        del current_segment['words']
        segments.append(current_segment)

    return segments


def build_intermediate_word_consensus(episode_name, intermediate_dir=Path("intermediates"), glossary=None,
                                       transcribers=None):
    """Build word-level transcriber consensus.

    IMPORTANT: This replaces the previous time-bucket alignment logic.

    Rationale:
    - Grouping words by start-time tolerance drifts when providers insert/delete words.
    - Drift cascades into duplicated spans and corrupt output.

    New approach:
    - Use a pivot transcript (default preference: whisperx-cloud, then assemblyai)
    - Align other word streams to pivot using anchors + local DP
    - Vote per pivot word slot with weights/confidence

    Current default scope:
    - Prefer whisperx-cloud + assemblyai only (do not assume local compute).

    Returns:
        (consensus_md, consensus_words, transcribers_used)
    """

    # Local import to avoid circular deps in other scripts.
    from consensus_words import build_consensus

    # Default to cloud-only providers unless explicitly overridden.
    default_transcribers = ["whisperx-cloud", "assemblyai"]
    transcribers_to_use = transcribers if transcribers else default_transcribers

    all_word_lists = {}
    for transcriber in transcribers_to_use:
        words = load_word_level_json(episode_name, transcriber, intermediate_dir)
        if words:
            all_word_lists[transcriber] = words

    if not all_word_lists:
        return None, None, []

    consensus_words = build_consensus(
        all_word_lists,
        provider_weights={"whisperx-cloud": 1.0, "assemblyai": 1.0},
        pivot_preference=["whisperx-cloud", "assemblyai"],
    )

    # Apply glossary corrections if available
    if glossary:
        consensus_words = apply_word_level_glossary(consensus_words, glossary)

    segments = words_to_segments(consensus_words)

    lines = []
    for seg in segments:
        lines.append(f"**[{seg['timestamp']}] {seg['speaker']}:**")
        lines.append(seg['text'])
        lines.append("")

    consensus_md = '\n'.join(lines)

    return consensus_md, consensus_words, list(all_word_lists.keys())


def align_segments_by_timestamp(all_outputs, tolerance_seconds=10):
    """
    Align segments from multiple outputs by timestamp with fuzzy matching.

    Uses the processor with most segments as reference, then finds matching
    segments from other processors within a time tolerance.

    Args:
        all_outputs: dict of {processor_name: [segments]}
        tolerance_seconds: Maximum time difference for matching (default 10s)

    Returns:
        List of aligned segment groups: [{'timestamp': 'MM:SS', 'variants': {proc: segment}}]
    """
    if not all_outputs:
        return []

    # Use processor with most segments as reference
    ref_proc = max(all_outputs.keys(), key=lambda p: len(all_outputs[p]))
    ref_segments = all_outputs[ref_proc]

    # Track which segments from each processor have been used
    used_segments = {proc: set() for proc in all_outputs}

    aligned = []
    for ref_idx, ref_seg in enumerate(ref_segments):
        ref_ts_secs = timestamp_to_seconds(ref_seg['timestamp'])

        group = {
            'timestamp': ref_seg['timestamp'],
            'variants': {ref_proc: ref_seg}
        }
        used_segments[ref_proc].add(ref_idx)

        # Find matching segments from other processors (fuzzy match)
        for proc, segments in all_outputs.items():
            if proc == ref_proc:
                continue

            best_match = None
            best_diff = float('inf')

            for idx, seg in enumerate(segments):
                if idx in used_segments[proc]:
                    continue

                seg_ts_secs = timestamp_to_seconds(seg['timestamp'])
                diff = abs(seg_ts_secs - ref_ts_secs)

                # Also check speaker matches for better alignment
                speaker_match = seg['speaker'] == ref_seg['speaker']

                if diff <= tolerance_seconds and diff < best_diff:
                    # Prefer same speaker within tolerance
                    if speaker_match or best_match is None:
                        best_match = (idx, seg)
                        best_diff = diff
                        if speaker_match and diff <= 3:  # Strong match
                            break

            if best_match:
                idx, seg = best_match
                group['variants'][proc] = seg
                used_segments[proc].add(idx)

        aligned.append(group)

    return aligned


def tokenize(text):
    """Tokenize text into words, preserving punctuation."""
    # Split on whitespace but keep contractions together
    tokens = re.findall(r"[\w']+|[.,!?;:]", text)
    return [t.lower() for t in tokens if t]


def word_consensus(word_lists, provider_weights=None):
    """
    Build consensus from multiple word lists using voting.

    Uses sequence alignment to handle insertions/deletions across outputs.

    Args:
        word_lists: dict of {processor: [words]}
        provider_weights: optional dict of {processor: weight}

    Returns:
        Consensus word list
    """
    if not word_lists:
        return []

    if len(word_lists) == 1:
        return list(word_lists.values())[0]

    # Use the longest list as reference
    ref_proc = max(word_lists.keys(), key=lambda p: len(word_lists[p]))
    ref_words = word_lists[ref_proc]

    if not ref_words:
        return []

    # For each position in reference, collect votes
    # This is a simplified approach - full alignment would use dynamic programming
    consensus = []

    # Build position-based voting
    max_len = max(len(words) for words in word_lists.values())

    for pos in range(max_len):
        votes = Counter()
        for proc, words in word_lists.items():
            if pos < len(words):
                word = words[pos]
                weight = provider_weights.get(proc, 1) if provider_weights else 1
                votes[word] += weight

        if votes:
            # Get most common word
            winner = votes.most_common(1)[0][0]
            consensus.append(winner)

    return consensus


def build_segment_consensus(variants, provider_weights=None, glossary=None):
    """
    Build consensus for a single segment from multiple processor outputs.

    Args:
        variants: dict of {processor: segment_dict}
        provider_weights: optional scoring weights
        glossary: optional glossary for term correction

    Returns:
        Consensus segment dict
    """
    if not variants:
        return None

    if len(variants) == 1:
        return list(variants.values())[0].copy()

    # Vote on speaker
    speaker_votes = Counter()
    for proc, seg in variants.items():
        weight = provider_weights.get(proc, 1) if provider_weights else 1
        speaker_votes[seg['speaker']] += weight

    consensus_speaker = speaker_votes.most_common(1)[0][0]

    # Vote on timestamp (use most common)
    ts_votes = Counter()
    for proc, seg in variants.items():
        ts_votes[seg['timestamp']] += 1
    consensus_ts = ts_votes.most_common(1)[0][0]

    # Build word-level consensus for text
    word_lists = {}
    for proc, seg in variants.items():
        word_lists[proc] = tokenize(seg['text'])

    consensus_words = word_consensus(word_lists, provider_weights)

    # Apply glossary corrections if available
    if glossary:
        consensus_words = apply_glossary_corrections(consensus_words, glossary)

    # Reconstruct text with proper capitalization
    consensus_text = reconstruct_text(consensus_words, variants)

    return {
        'timestamp': consensus_ts,
        'speaker': consensus_speaker,
        'text': consensus_text
    }


def apply_glossary_corrections(words, glossary):
    """Apply glossary-based corrections to word list."""
    # Build lowercase -> correct case mapping
    corrections = {}
    for person in glossary.get('people', []):
        corrections[person.lower()] = person
    for term in glossary.get('technical_terms', []):
        corrections[term.lower()] = term
    for project in glossary.get('projects', []):
        corrections[project.lower()] = project

    # Common Ethereum-specific corrections
    crypto_corrections = {
        'ether': 'Ether',
        'ethereum': 'Ethereum',
        'bitcoin': 'Bitcoin',
        'defi': 'DeFi',
        'nft': 'NFT',
        'nfts': 'NFTs',
        'dao': 'DAO',
        'daos': 'DAOs',
        'dapp': 'dApp',
        'dapps': 'dApps',
        'wei': 'Wei',
        'gwei': 'Gwei',
        'solidity': 'Solidity',
        'evm': 'EVM',
        'erc20': 'ERC-20',
        'erc721': 'ERC-721',
        'erc1155': 'ERC-1155',
        'ipfs': 'IPFS',
        'devcon': 'Devcon',
        'vitalik': 'Vitalik',
        'buterin': 'Buterin',
    }
    corrections.update(crypto_corrections)

    result = []
    for word in words:
        if word.lower() in corrections:
            result.append(corrections[word.lower()])
        else:
            result.append(word)

    return result


def reconstruct_text(consensus_words, variants):
    """
    Reconstruct readable text from consensus words.
    Tries to preserve original casing and punctuation from variants.
    """
    if not consensus_words:
        return ""

    # Get a reference text for casing hints
    ref_text = list(variants.values())[0]['text']
    ref_words_original = re.findall(r"[\w']+|[.,!?;:]", ref_text)

    # Build case map from reference
    case_map = {}
    for word in ref_words_original:
        case_map[word.lower()] = word

    # Reconstruct with proper casing
    result = []
    for i, word in enumerate(consensus_words):
        # Check if it's punctuation
        if word in '.,!?;:':
            if result:
                result[-1] = result[-1] + word
        else:
            # Apply casing from reference or capitalize sentence starts
            if word.lower() in case_map:
                word = case_map[word.lower()]
            elif i == 0 or (result and result[-1].endswith(('.', '!', '?'))):
                word = word.capitalize()
            result.append(word)

    return ' '.join(result)


def build_true_consensus(episode_name, transcriber, output_dir=Path("outputs"),
                         glossary=None):
    """
    Build true multi-model consensus for an episode using a specific transcriber.

    Loads all processor outputs, aligns them, and builds word-level consensus.

    Returns:
        Consensus transcript as string (md format)
    """
    episode_dir = output_dir / episode_name
    base_name = f"{episode_name}_{transcriber}"

    # Load all processor outputs
    all_outputs = {}
    provider_weights = {}

    for processor in PROCESSORS:
        # Prefer .md files (have timestamps) over .txt (no timestamps)
        md_file = episode_dir / f"{base_name}_{processor}.md"
        txt_file = episode_dir / f"{base_name}_{processor}.txt"

        content = None
        if md_file.exists():
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        elif txt_file.exists():
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read()

        if content:
            segments = parse_transcript_segments(content)
            if segments:
                all_outputs[processor] = segments
                # Weight by quality score
                metrics, _ = assess_output_quality(episode_dir, transcriber)
                if processor in metrics:
                    provider_weights[processor] = score_provider(metrics[processor])

    if not all_outputs:
        return None

    # Align segments by timestamp
    aligned = align_segments_by_timestamp(all_outputs)

    # Build consensus for each aligned segment group
    consensus_segments = []
    for group in aligned:
        consensus_seg = build_segment_consensus(
            group['variants'],
            provider_weights,
            glossary
        )
        if consensus_seg:
            consensus_segments.append(consensus_seg)

    # Format as markdown
    lines = []
    for seg in consensus_segments:
        lines.append(f"**[{seg['timestamp']}] {seg['speaker']}:**")
        lines.append(seg['text'])
        lines.append("")

    return '\n'.join(lines)


def generate_intermediate_consensus(episode_name, intermediate_dir=Path("intermediates"),
                                     consensus_dir=None, transcribers=None):
    """
    Generate word-level consensus from intermediate transcripts.

    Uses word-level JSON files (*_consensus_words.json) for precise sub-second alignment.
    Output goes to intermediates/<episode>/ alongside source files.

    Args:
        episode_name: Name of the episode
        intermediate_dir: Directory containing intermediate files
        consensus_dir: Unused, kept for backwards compatibility
        transcribers: Optional list of transcribers to use (default: all)

    Returns:
        Result dict with consensus info
    """
    glossary = load_glossary()

    results = {
        'episode': episode_name,
        'transcribers_used': [],
        'word_count': 0,
        'consensus_file': None,
        'has_word_level': False
    }

    # Build word-level consensus from intermediates
    consensus_md, consensus_words, transcribers_used = build_intermediate_word_consensus(
        episode_name, intermediate_dir, glossary, transcribers
    )

    if consensus_md:
        results['transcribers_used'] = transcribers_used
        results['word_count'] = count_words(consensus_md)
        results['has_word_level'] = True

        # Save consensus to intermediates (same dir as source files)
        episode_dir = intermediate_dir / episode_name
        episode_dir.mkdir(parents=True, exist_ok=True)

        # Save markdown version
        md_file = episode_dir / f"{episode_name}_intermediate_consensus.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(consensus_md)

        # Save txt version
        txt_content = re.sub(r'\*\*', '', consensus_md)
        txt_file = episode_dir / f"{episode_name}_intermediate_consensus.txt"
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(txt_content)

        # Save word-level JSON for downstream use
        if consensus_words:
            json_file = episode_dir / f"{episode_name}_intermediate_consensus_words.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(consensus_words, f, indent=2)

        results['consensus_file'] = str(md_file)

    return results


def generate_true_consensus_transcript(episode_name, output_dir=Path("outputs"),
                                        intermediate_dir=Path("intermediates"),
                                        consensus_dir=Path("consensus")):
    """
    Generate a TRUE consensus transcript by combining outputs from all processors.

    Strategy:
    1. First, try to build word-level consensus from intermediates
    2. Then build multi-model consensus from processor outputs
    3. Combine both for final gold standard
    """
    episode_out_dir = output_dir / episode_name
    episode_int_dir = intermediate_dir / episode_name

    if not episode_out_dir.exists():
        print(f"  Episode not found: {episode_name}")
        return None

    glossary = load_glossary()

    results = {
        'episode': episode_name,
        'transcriber_consensuses': {},
        'selected_transcriber': None,
        'consensus_file': None,
        'processors_merged': 0,
        'intermediate_consensus': None,
        'method': 'segment_level'  # or 'word_level'
    }

    # Try word-level intermediate consensus first
    if episode_int_dir.exists():
        int_results = generate_intermediate_consensus(episode_name, intermediate_dir, consensus_dir)
        if int_results.get('has_word_level'):
            results['intermediate_consensus'] = int_results
            results['method'] = 'word_level'
            print(f"    ✓ Word-level consensus from {len(int_results['transcribers_used'])} transcribers")

    # Build consensus for each transcriber's post-processed outputs
    best_consensus = None
    best_transcriber = None
    best_word_count = 0

    for transcriber in TRANSCRIBERS:
        consensus_text = build_true_consensus(
            episode_name, transcriber, output_dir, glossary
        )

        if consensus_text:
            word_count = count_words(consensus_text)
            results['transcriber_consensuses'][transcriber] = {
                'word_count': word_count
            }

            # Select transcriber with most content (usually best diarization)
            if word_count > best_word_count:
                best_word_count = word_count
                best_consensus = consensus_text
                best_transcriber = transcriber

    if best_consensus:
        results['selected_transcriber'] = best_transcriber

        # Count how many processors contributed
        txt_files = list(episode_out_dir.glob(f"{episode_name}_{best_transcriber}_*.txt"))
        md_files = list(episode_out_dir.glob(f"{episode_name}_{best_transcriber}_*.md"))
        results['processors_merged'] = max(len(txt_files), len(md_files))

        # Save consensus
        consensus_episode_dir = consensus_dir / episode_name
        consensus_episode_dir.mkdir(parents=True, exist_ok=True)

        md_file = consensus_episode_dir / f"{episode_name}_consensus.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(best_consensus)

        # Also save txt version (strip markdown)
        txt_content = re.sub(r'\*\*', '', best_consensus)
        txt_file = consensus_episode_dir / f"{episode_name}_consensus.txt"
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(txt_content)

        results['consensus_file'] = str(md_file)

    return results


def generate_all_true_consensus(output_dir=Path("outputs"), intermediate_dir=Path("intermediates"),
                                 consensus_dir=Path("consensus")):
    """
    Generate TRUE multi-model consensus transcripts for all episodes.
    """
    results = []
    episode_dirs = sorted([d for d in output_dir.iterdir() if d.is_dir()])

    for episode_dir in episode_dirs:
        episode_name = episode_dir.name
        result = generate_true_consensus_transcript(
            episode_name, output_dir, intermediate_dir, consensus_dir
        )
        if result:
            results.append(result)
            if result.get('consensus_file'):
                print(f"  {episode_name}: merged {result['processors_merged']} processors ({result['selected_transcriber']})")
            else:
                print(f"  {episode_name}: No consensus generated")

    return results


# =============================================================================
# Legacy Selection-Based Functions (kept for comparison)
# =============================================================================

def generate_consensus_transcript_selection(episode_name, output_dir=Path("outputs"),
                                             intermediate_dir=Path("intermediates"),
                                             consensus_dir=Path("consensus")):
    """
    Generate consensus by selecting the single best output (legacy method).
    Use generate_true_consensus_transcript() for actual multi-model consensus.
    """
    episode_out_dir = output_dir / episode_name
    episode_int_dir = intermediate_dir / episode_name

    if not episode_out_dir.exists():
        print(f"Episode not found: {episode_name}")
        return None

    results = {
        'episode': episode_name,
        'best_intermediate': None,
        'best_output': None,
        'consensus_file': None
    }

    # Select best intermediate
    if episode_int_dir.exists():
        best_int, int_metrics = select_best_intermediate(episode_int_dir)
        results['best_intermediate'] = {
            'transcriber': best_int,
            'metrics': int_metrics
        }

    # Select best output for each transcriber, then pick overall best
    best_overall = None
    best_score = -1

    for transcriber in TRANSCRIBERS:
        best_proc, metrics = select_best_output(episode_out_dir, transcriber)
        if best_proc and metrics:
            score = score_provider(metrics)
            if score > best_score:
                best_score = score
                best_overall = {
                    'transcriber': transcriber,
                    'processor': best_proc,
                    'metrics': metrics,
                    'score': score
                }

    if best_overall:
        results['best_output'] = best_overall

        # Create consensus directory and copy best file
        consensus_episode_dir = consensus_dir / episode_name
        consensus_episode_dir.mkdir(parents=True, exist_ok=True)

        src_file = episode_out_dir / f"{episode_name}_{best_overall['transcriber']}_{best_overall['processor']}.md"
        if src_file.exists():
            dst_file = consensus_episode_dir / f"{episode_name}_consensus.md"
            import shutil
            shutil.copy(src_file, dst_file)
            results['consensus_file'] = str(dst_file)

            # Also copy txt version
            src_txt = src_file.with_suffix('.txt')
            if src_txt.exists():
                dst_txt = dst_file.with_suffix('.txt')
                shutil.copy(src_txt, dst_txt)

    return results


def generate_all_consensus(output_dir=Path("outputs"), intermediate_dir=Path("intermediates"),
                           consensus_dir=Path("consensus")):
    """
    Generate TRUE multi-model consensus transcripts for all episodes.
    (Calls the true consensus builder, not just selection)
    """
    return generate_all_true_consensus(output_dir, intermediate_dir, consensus_dir)


def generate_quality_report(output_dir=Path("outputs"), intermediate_dir=Path("intermediates")):
    """
    Generate comprehensive quality report for all episodes.
    """
    report = {
        'summary': {
            'total_episodes': 0,
            'intermediate_analysis': {},
            'output_analysis': {},
            'provider_scores': defaultdict(list),
            'transcriber_scores': defaultdict(list)
        },
        'episodes': {}
    }

    # Find all episodes
    episode_dirs = sorted([d for d in output_dir.iterdir() if d.is_dir()])
    report['summary']['total_episodes'] = len(episode_dirs)

    for episode_dir in episode_dirs:
        episode_name = episode_dir.name
        episode_report = {
            'intermediates': {},
            'outputs': {},
            'best_intermediate': None,
            'best_outputs': {}
        }

        # Analyze intermediates
        int_dir = intermediate_dir / episode_name
        if int_dir.exists():
            episode_report['intermediates'] = assess_intermediate_quality(int_dir)
            best_int, _ = select_best_intermediate(int_dir)
            episode_report['best_intermediate'] = best_int

            for t, m in episode_report['intermediates'].items():
                report['summary']['transcriber_scores'][t].append(m['word_count'])

        # Analyze outputs for each transcriber
        for transcriber in TRANSCRIBERS:
            metrics, input_wc = assess_output_quality(episode_dir, transcriber)
            if metrics:
                episode_report['outputs'][transcriber] = metrics
                best_out, _ = select_best_output(episode_dir, transcriber)
                episode_report['best_outputs'][transcriber] = best_out

                # Track provider scores
                for processor, m in metrics.items():
                    score = score_provider(m)
                    report['summary']['provider_scores'][processor].append(score)

        report['episodes'][episode_name] = episode_report

    # Compute summary statistics
    for processor, scores in report['summary']['provider_scores'].items():
        report['summary']['provider_scores'][processor] = {
            'mean_score': statistics.mean(scores) if scores else 0,
            'count': len(scores)
        }

    return report


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Assess transcript quality and build consensus"
    )
    parser.add_argument('--episode', type=str, help='Specific episode to analyze')
    parser.add_argument('--report', action='store_true', help='Generate full quality report')
    parser.add_argument('--output', type=str, default='quality_report.json',
                        help='Output file for report')
    parser.add_argument('--summary', action='store_true', help='Print summary only')
    parser.add_argument('--consensus', action='store_true',
                        help='Generate consensus transcripts for all episodes')
    parser.add_argument('--intermediate-consensus', action='store_true',
                        help='Generate word-level consensus from intermediates only')
    parser.add_argument('--consensus-dir', type=str, default='consensus',
                        help='Output directory for consensus transcripts')
    parser.add_argument('--transcribers', type=str,
                        help='Comma-separated list of transcribers to use (default: all)')

    args = parser.parse_args()

    # Parse transcribers filter
    transcribers_filter = None
    if args.transcribers:
        transcribers_filter = [t.strip() for t in args.transcribers.split(',')]

    if args.intermediate_consensus:
        transcriber_info = f" (transcribers: {', '.join(transcribers_filter)})" if transcribers_filter else ""
        print(f"Generating word-level intermediate consensus{transcriber_info}...")
        print("="*60)
        intermediate_dir = Path("intermediates")

        if args.episode:
            # Single episode
            result = generate_intermediate_consensus(args.episode, intermediate_dir, Path(args.consensus_dir),
                                                      transcribers_filter)
            if result.get('consensus_file'):
                print(f"  {result['episode']}: merged {len(result['transcribers_used'])} transcribers ({', '.join(result['transcribers_used'])})")
                print(f"    → {result['consensus_file']}")
            else:
                print(f"  {args.episode}: No word-level data available")
        else:
            # All episodes
            episode_dirs = sorted([d for d in intermediate_dir.iterdir() if d.is_dir()])
            success_count = 0
            for episode_dir in episode_dirs:
                episode_name = episode_dir.name
                result = generate_intermediate_consensus(episode_name, intermediate_dir, Path(args.consensus_dir),
                                                          transcribers_filter)
                if result.get('consensus_file'):
                    print(f"  {episode_name}: merged {len(result['transcribers_used'])} transcribers ({result['word_count']} words)")
                    success_count += 1

            print("="*60)
            print(f"\nGenerated {success_count} intermediate consensus transcripts")
            print(f"Output directory: {args.consensus_dir}/")
        return

    if args.consensus:
        print("Generating consensus transcripts...")
        print("="*60)
        results = generate_all_consensus(consensus_dir=Path(args.consensus_dir))
        print("="*60)
        print(f"\nGenerated {len([r for r in results if r.get('consensus_file')])} consensus transcripts")
        print(f"Output directory: {args.consensus_dir}/")
        return

    if args.report or args.summary:
        print("Generating quality report...")
        report = generate_quality_report()

        if args.summary:
            print("\n" + "="*70)
            print("QUALITY ASSESSMENT SUMMARY")
            print("="*70)

            print(f"\nTotal episodes analyzed: {report['summary']['total_episodes']}")

            print("\n--- Provider Rankings (by mean score) ---")
            provider_scores = report['summary']['provider_scores']
            ranked = sorted(provider_scores.items(),
                          key=lambda x: x[1]['mean_score'], reverse=True)
            for i, (provider, stats) in enumerate(ranked, 1):
                print(f"  {i:2}. {provider:12} - Score: {stats['mean_score']:.1f} ({stats['count']} samples)")

            # Count best selections
            best_counts = Counter()
            for ep_data in report['episodes'].values():
                for transcriber, best_proc in ep_data.get('best_outputs', {}).items():
                    if best_proc:
                        best_counts[best_proc] += 1

            print("\n--- Times Selected as Best ---")
            for proc, count in best_counts.most_common():
                print(f"  {proc:12} - {count} times")

        if args.report:
            with open(args.output, 'w') as f:
                # Convert defaultdict to regular dict for JSON
                report['summary']['provider_scores'] = dict(report['summary']['provider_scores'])
                report['summary']['transcriber_scores'] = dict(report['summary']['transcriber_scores'])
                json.dump(report, f, indent=2, default=str)
            print(f"\nFull report saved to: {args.output}")

    elif args.episode:
        episode_dir = Path("outputs") / args.episode
        int_dir = Path("intermediates") / args.episode

        if not episode_dir.exists():
            print(f"Episode not found: {args.episode}")
            sys.exit(1)

        print(f"Analyzing episode: {args.episode}")
        print("="*60)

        # Intermediate analysis
        if int_dir.exists():
            print("\n--- Intermediate Transcripts ---")
            metrics = assess_intermediate_quality(int_dir)
            for t, m in metrics.items():
                print(f"  {t}:")
                print(f"    Words: {m['word_count']}, Speakers: {m['unique_speakers']}, Turns: {m['speaker_turns']}")

            best_int, _ = select_best_intermediate(int_dir)
            print(f"\n  Best intermediate: {best_int}")

        # Output analysis
        print("\n--- Post-Processed Outputs ---")
        for transcriber in TRANSCRIBERS:
            metrics, input_wc = assess_output_quality(episode_dir, transcriber)
            if not metrics:
                continue

            print(f"\n  From {transcriber} (input: {input_wc} words):")

            scored = [(p, m, score_provider(m)) for p, m in metrics.items()]
            scored.sort(key=lambda x: x[2], reverse=True)

            for proc, m, score in scored[:5]:  # Top 5
                ratio_str = f"{m['word_count_ratio']:.0%}" if m['word_count_ratio'] else "N/A"
                status = "OK" if m['in_target_range'] else ("LONG" if m['word_count_ratio'] and m['word_count_ratio'] > 1.1 else "SHORT")
                print(f"    {proc:12} - {m['word_count']:5} words ({ratio_str}) [{status}] Score: {score}")

            best_out, _ = select_best_output(episode_dir, transcriber)
            print(f"    Best: {best_out}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
