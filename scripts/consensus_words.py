#!/usr/bin/env python3
"""Word-level alignment + consensus for multiple ASR word streams.

Motivation:
- Time-bucketing ("start times within X") drifts badly when ASRs insert/delete words.
- We instead align sequences using anchors + local DP, then build consensus.

This is designed to work with whisperx-cloud + assemblyai without local compute.

Input word format (per word):
  {
    "text": str,
    "start": float,   # seconds
    "end": float,     # seconds
    "speaker": str,   # optional
    "confidence": float  # optional
  }

Output consensus word format:
  {
    "text": str,
    "start": float,
    "end": float,
    "speaker": str,
    "agreement": float,
    "sources": {"provider": {"text": str, "start": float, "end": float, ...}, ...}
  }
"""

from __future__ import annotations

from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Dict, List, Optional, Tuple


def norm_token(t: str) -> str:
    # Lowercase and strip common punctuation. Keep apostrophes within tokens.
    return (t or "").lower().strip().strip(".,!?;:\"()[]{}")


def words_to_tokens(words: List[dict]) -> List[str]:
    return [norm_token(w.get("text", "")) for w in words]


@dataclass(frozen=True)
class Anchor:
    i: int  # pivot index
    j: int  # other index


def _find_anchors(
    pivot_words: List[dict],
    other_words: List[dict],
    *,
    time_tol_s: float = 0.6,
) -> List[Anchor]:
    """Find candidate anchor pairs where tokens match and timestamps are close."""

    pivot_tok = words_to_tokens(pivot_words)
    other_tok = words_to_tokens(other_words)

    # Index other by coarse time bucket to limit comparisons.
    buckets: Dict[int, List[int]] = {}
    for j, w in enumerate(other_words):
        b = int(float(w.get("start", 0.0)) / time_tol_s)
        buckets.setdefault(b, []).append(j)

    anchors: List[Anchor] = []
    for i, pw in enumerate(pivot_words):
        t = float(pw.get("start", 0.0))
        tok = pivot_tok[i]
        if not tok:
            continue
        b0 = int(t / time_tol_s)
        candidates = []
        for b in (b0 - 1, b0, b0 + 1):
            candidates.extend(buckets.get(b, []))

        best_j: Optional[int] = None
        best_dt = 1e9
        for j in candidates:
            if other_tok[j] != tok:
                continue
            dt = abs(float(other_words[j].get("start", 0.0)) - t)
            if dt <= time_tol_s and dt < best_dt:
                best_dt = dt
                best_j = j
        if best_j is not None:
            anchors.append(Anchor(i=i, j=best_j))

    # Reduce to an increasing sequence (LIS) to avoid crossing alignments.
    # Since anchors are generated in increasing i order, we compute LIS on j.
    if not anchors:
        return []

    js = [a.j for a in anchors]
    # Patience LIS
    piles: List[int] = []
    parent: List[int] = [-1] * len(js)
    pile_idx: List[int] = [0] * len(js)
    pile_tops: List[int] = []  # store index of anchor at pile top

    import bisect

    for idx, j in enumerate(js):
        k = bisect.bisect_left(piles, j)
        if k == len(piles):
            piles.append(j)
            pile_tops.append(idx)
        else:
            piles[k] = j
            pile_tops[k] = idx
        pile_idx[idx] = k
        if k > 0:
            # find previous anchor index that ended pile k-1 with smallest j
            prev_top = None
            prev_j = None
            for p in range(idx - 1, -1, -1):
                if pile_idx[p] == k - 1:
                    prev_top = p
                    prev_j = js[p]
                    break
            if prev_top is not None and prev_j is not None and prev_j < j:
                parent[idx] = prev_top

    # Reconstruct from last pile top
    last = pile_tops[-1]
    seq: List[Anchor] = []
    while last != -1:
        seq.append(anchors[last])
        last = parent[last]
    seq.reverse()

    # Deduplicate identical j (can happen). Keep first.
    out: List[Anchor] = []
    seen_j = set()
    for a in seq:
        if a.j in seen_j:
            continue
        seen_j.add(a.j)
        out.append(a)
    return out


def _dp_align_tokens(pivot_tokens: List[str], other_tokens: List[str]) -> List[Tuple[Optional[int], Optional[int]]]:
    """Classic edit-distance alignment for small ranges.

    Returns list of (pivot_idx, other_idx) pairs including insertions/deletions.
    """
    m, n = len(pivot_tokens), len(other_tokens)
    # costs
    ins = 1
    dele = 1
    sub = 1
    match = 0

    # DP tables
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    bt = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i * dele
        bt[i][0] = (i - 1, 0)
    for j in range(1, n + 1):
        dp[0][j] = j * ins
        bt[0][j] = (0, j - 1)

    for i in range(1, m + 1):
        pi = pivot_tokens[i - 1]
        for j in range(1, n + 1):
            oj = other_tokens[j - 1]
            c_sub = dp[i - 1][j - 1] + (match if pi == oj and pi else sub)
            c_del = dp[i - 1][j] + dele
            c_ins = dp[i][j - 1] + ins
            c = min(c_sub, c_del, c_ins)
            dp[i][j] = c
            if c == c_sub:
                bt[i][j] = (i - 1, j - 1)
            elif c == c_del:
                bt[i][j] = (i - 1, j)
            else:
                bt[i][j] = (i, j - 1)

    # backtrace
    pairs: List[Tuple[Optional[int], Optional[int]]] = []
    i, j = m, n
    while i > 0 or j > 0:
        pi, pj = bt[i][j]
        if pi is None or pj is None:
            break
        if pi == i - 1 and pj == j - 1:
            pairs.append((i - 1, j - 1))
            i, j = pi, pj
        elif pi == i - 1 and pj == j:
            pairs.append((i - 1, None))
            i, j = pi, pj
        else:
            pairs.append((None, j - 1))
            i, j = pi, pj

    pairs.reverse()
    return pairs


def align_word_lists(
    pivot_words: List[dict],
    other_words: List[dict],
    *,
    anchor_time_tol_s: float = 0.6,
    max_chunk_words: int = 1200,
) -> Dict[int, Optional[int]]:
    """Align other_words to pivot_words.

    Returns mapping pivot_idx -> other_idx (or None).

    We use anchors (matching tokens near same time) to split into chunks, then
    do DP alignment per chunk. Chunk sizes are bounded.
    """

    pivot_tokens = words_to_tokens(pivot_words)
    other_tokens = words_to_tokens(other_words)

    anchors = _find_anchors(pivot_words, other_words, time_tol_s=anchor_time_tol_s)

    # Always include boundaries
    boundaries: List[Anchor] = [Anchor(-1, -1)] + anchors + [Anchor(len(pivot_words), len(other_words))]

    mapping: Dict[int, Optional[int]] = {i: None for i in range(len(pivot_words))}

    for k in range(len(boundaries) - 1):
        a0 = boundaries[k]
        a1 = boundaries[k + 1]
        pi0, pj0 = a0.i + 1, a0.j + 1
        pi1, pj1 = a1.i, a1.j

        if pi1 < pi0 or pj1 < pj0:
            continue

        # If chunk is enormous, fall back to time-window greedy to avoid O(mn).
        if (pi1 - pi0) * (pj1 - pj0) > max_chunk_words * max_chunk_words:
            # Greedy by time within tolerance
            j = pj0
            for i in range(pi0, pi1):
                t = float(pivot_words[i].get("start", 0.0))
                best = None
                best_dt = 1e9
                while j < pj1 and float(other_words[j].get("start", 0.0)) < t - anchor_time_tol_s:
                    j += 1
                for jj in range(j, min(pj1, j + 12)):
                    dt = abs(float(other_words[jj].get("start", 0.0)) - t)
                    if dt <= anchor_time_tol_s and dt < best_dt and other_tokens[jj] and other_tokens[jj] == pivot_tokens[i]:
                        best = jj
                        best_dt = dt
                if best is not None:
                    mapping[i] = best
            continue

        pairs = _dp_align_tokens(pivot_tokens[pi0:pi1], other_tokens[pj0:pj1])
        for p_idx, o_idx in pairs:
            if p_idx is None:
                continue
            pivot_i = pi0 + p_idx
            other_j = None if o_idx is None else pj0 + o_idx
            mapping[pivot_i] = other_j

    # Force anchors as exact matches
    for a in anchors:
        mapping[a.i] = a.j

    return mapping


def build_consensus(
    word_lists: Dict[str, List[dict]],
    *,
    provider_weights: Optional[Dict[str, float]] = None,
    pivot_preference: Optional[List[str]] = None,
) -> List[dict]:
    """Build a consensus word stream from multiple providers.

    Strategy:
    - Choose pivot provider.
    - Align others to pivot.
    - For each pivot word slot, vote among available provider words.
    - Optionally include non-pivot insertions conservatively (not used by default).
    """

    if not word_lists:
        return []

    provider_weights = provider_weights or {}
    pivot_preference = pivot_preference or ["whisperx-cloud", "assemblyai"]

    # Choose pivot
    pivot_name = None
    for name in pivot_preference:
        if name in word_lists and word_lists[name]:
            pivot_name = name
            break
    if pivot_name is None:
        pivot_name = max(word_lists.keys(), key=lambda k: len(word_lists[k]) if word_lists[k] else 0)

    pivot_words = word_lists[pivot_name]

    # Align all others to pivot
    aligned: Dict[str, Dict[int, Optional[int]]] = {}
    for name, words in word_lists.items():
        if name == pivot_name:
            continue
        if not words:
            continue
        aligned[name] = align_word_lists(pivot_words, words)

    def w_weight(provider: str, w: dict) -> float:
        base = float(provider_weights.get(provider, 1.0))
        conf = w.get("confidence")
        if conf is None:
            return base
        try:
            return base * float(conf)
        except Exception:
            return base

    consensus: List[dict] = []

    for i, pw in enumerate(pivot_words):
        sources: Dict[str, dict] = {pivot_name: pw}
        candidates: List[Tuple[str, dict]] = [(pivot_name, pw)]
        for name, mapping in aligned.items():
            j = mapping.get(i)
            if j is None:
                continue
            ow = word_lists[name][j]
            sources[name] = ow
            candidates.append((name, ow))

        # Vote on token text (normalized), keep original token (prefer pivot casing if tie)
        tally: Dict[str, float] = {}
        orig: Dict[str, str] = {}
        for prov, w in candidates:
            t = (w.get("text") or "").strip()
            nt = norm_token(t)
            if not nt:
                continue
            tally[nt] = tally.get(nt, 0.0) + w_weight(prov, w)
            # store prettiest version (longer or from pivot)
            if nt not in orig or (prov == pivot_name) or (len(t) > len(orig[nt])):
                orig[nt] = t

        if not tally:
            continue

        winner_nt = max(tally.items(), key=lambda kv: kv[1])[0]
        winner_text = orig.get(winner_nt, winner_nt)

        # Speaker: prefer pivot, else majority
        speaker = pw.get("speaker") or "SPEAKER_00"
        if not speaker:
            speaker = "SPEAKER_00"

        # Times: take pivot times (stable). You can average later if desired.
        start = float(pw.get("start", 0.0))
        end = float(pw.get("end", start))

        # Agreement: weighted fraction supporting winner
        total_w = sum(tally.values())
        agree_w = tally[winner_nt]
        agreement = 0.0 if total_w <= 0 else agree_w / total_w

        consensus.append(
            {
                "text": winner_text,
                "start": start,
                "end": end,
                "speaker": speaker,
                "agreement": agreement,
                "sources": sources,
            }
        )

    return consensus
