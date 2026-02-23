#!/usr/bin/env python3
"""Generate *draft* manual assessment sections for each episode.

This script does not call any LLMs. It attempts to approximate a human
"spot-check" by:
  - sampling a handful of speaker-turn blocks from intermediate .md
  - matching those blocks by timestamp in each output .md
  - scoring similarity + tracking entity/phrase novelty

It then prepends a MANUAL ASSESSMENT section to:
  outputs/<episode>/QUALITY_ASSESSMENT.md

Notes
-----
These drafts are intended to be edited/extended by a human, but they provide a
repeatable baseline of qualitative observations backed by the excerpt pack.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.build_review_excerpts import (
    Block,
    cap_sequences,
    md_word_count,
    parse_md_blocks,
    sample_indices,
    find_matching_block,
)
from scripts.generate_quality_assessments import _discover_episodes
from scripts.quality_metrics import compute_md_metrics, compute_txt_metrics


WORD_RE = re.compile(r"\b\w+\b")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def jaccard(a: str, b: str) -> float:
    sa = set(w.lower() for w in WORD_RE.findall(a))
    sb = set(w.lower() for w in WORD_RE.findall(b))
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / max(1, len(sa | sb))


@dataclass(frozen=True)
class ComboQual:
    transcriber: str
    processor: str
    retention: float
    ts_out: int
    ts_in: int
    ts_ratio: float
    fmt_bad: int
    nonmono: int
    novel_caps: int
    excerpt_similarity: float


def combo_score(c: ComboQual) -> float:
    # Higher is better.
    score = 0.0
    score += c.excerpt_similarity * 100
    score += max(0.0, 30 - abs(c.retention - 1.0) * 200)  # prefer ~1.0
    score += max(0.0, 30 - abs(c.ts_ratio - 1.0) * 200)
    score -= min(50.0, c.novel_caps)
    score -= min(100.0, c.fmt_bad)
    score -= min(50.0, c.nonmono * 10)
    return score


def build_draft_section(
    *,
    episode: str,
    transcribers: list[str],
    processors: list[str],
    k_blocks: int,
) -> str:
    inter_dir = Path("intermediates") / episode
    out_dir = Path("outputs") / episode

    lines: list[str] = []
    lines.append("=" * 80)
    lines.append("MANUAL ASSESSMENT (DRAFT; excerpt-based spot-check)")
    lines.append("=" * 80)
    lines.append("")
    lines.append(
        "This section is generated from a deterministic excerpt spot-check (5 blocks per transcriber)\n"
        "plus simple novelty/similarity heuristics. It is *not* a substitute for listening to audio,\n"
        "but it does catch common failure modes: summarization, hallucinated entities, timestamp drift,\n"
        "and formatting corruption."
    )
    lines.append("")
    lines.append(f"See excerpt pack: outputs/{episode}/REVIEW_EXCERPTS.md")
    lines.append("")

    for tr in transcribers:
        inter_md_path = inter_dir / f"{episode}_{tr}.md"
        if not inter_md_path.exists():
            continue

        base_md = _read_text(inter_md_path)
        base_blocks = parse_md_blocks(base_md)
        idxs = sample_indices(len(base_blocks), k_blocks)
        base_mm = compute_md_metrics(inter_md_path)
        base_words = md_word_count(base_md)
        base_caps = cap_sequences(base_md)

        combos: list[ComboQual] = []
        for pr in processors:
            out_md_path = out_dir / f"{episode}_{tr}_{pr}.md"
            if not out_md_path.exists():
                continue

            out_md = _read_text(out_md_path)
            out_blocks = parse_md_blocks(out_md)
            out_mm = compute_md_metrics(out_md_path)
            out_tm = compute_txt_metrics(out_md_path)

            # Similarity across sampled blocks (match by timestamp)
            sims: list[float] = []
            for i in idxs:
                b: Block = base_blocks[i]
                mb = find_matching_block(out_blocks, b.ts, b.speaker)
                if mb is None:
                    sims.append(0.0)
                else:
                    sims.append(jaccard(b.text, mb.text))
            sim = sum(sims) / max(1, len(sims))

            novel = len(cap_sequences(out_md) - base_caps)
            ts_ratio = (out_mm.timestamp_count / (base_mm.timestamp_count or 1))
            retention = out_tm.word_count / (base_words or 1)

            combos.append(
                ComboQual(
                    transcriber=tr,
                    processor=pr,
                    retention=retention,
                    ts_out=out_mm.timestamp_count,
                    ts_in=base_mm.timestamp_count,
                    ts_ratio=ts_ratio,
                    fmt_bad=out_mm.format_violations,
                    nonmono=out_mm.non_monotonic_timestamps,
                    novel_caps=novel,
                    excerpt_similarity=sim,
                )
            )

        if not combos:
            continue

        combos.sort(key=combo_score, reverse=True)
        best = combos[0]

        lines.append("-" * 80)
        lines.append(f"Transcriber: {tr}")
        lines.append("-")
        lines.append(
            f"Baseline: {base_words:,} words, {base_mm.timestamp_count} timestamps (fmt_bad={base_mm.format_violations}, nonmono={base_mm.non_monotonic_timestamps})"
        )
        lines.append("")
        lines.append("Top candidates (excerpt similarity / novelty / timestamp drift):")
        for c in combos[: min(3, len(combos))]:
            flag = ""
            if c.ts_in and (c.ts_ratio > 1.2 or c.ts_ratio < 0.8):
                flag = "  ⚠ timestamp drift"
            if c.retention < 0.85:
                flag += "  ⚠ condensation"
            if c.novel_caps > 40:
                flag += "  ⚠ entity novelty"
            lines.append(
                f"  • {c.processor:8} sim={c.excerpt_similarity:0.2f} ret={c.retention*100:0.1f}% ts={c.ts_out}/{c.ts_in} (×{c.ts_ratio:0.2f}) novel_caps={c.novel_caps} fmt_bad={c.fmt_bad}{flag}"
            )
        lines.append("")
        lines.append(f"Draft recommendation for this transcriber: {best.processor}")
        lines.append(
            "Rationale: chosen by highest excerpt similarity while avoiding obvious timestamp/format corruption and excessive entity novelty."
        )
        lines.append("")

    lines.append("=" * 80)
    lines.append("")
    return "\n".join(lines)


def prepend_manual_section(path: Path, manual_section: str) -> None:
    existing = _read_text(path) if path.exists() else ""
    # Remove any previous draft section to keep it idempotent.
    marker = "MANUAL ASSESSMENT (DRAFT; excerpt-based spot-check)"
    if marker in existing:
        # remove everything from the start of that section up to the next massive separator
        parts = existing.split("=" * 80)
        # naive: drop first 3 chunks (header + section); keep remainder
        # if formatting differs, we fall back to overwrite.
        existing = "".join(["=" * 80] + parts[3:]).lstrip() if len(parts) > 3 else ""
    path.write_text(manual_section + "\n" + existing.lstrip(), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", default="all")
    ap.add_argument("--transcribers", default="assemblyai,whisperx-cloud,whisperx")
    ap.add_argument("--processors", default="opus,gemini,deepseek,chatgpt")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument(
        "--assessment-filename",
        default="QUALITY_ASSESSMENT.md",
        help="Which per-episode assessment file to prepend (default: QUALITY_ASSESSMENT.md)",
    )
    args = ap.parse_args()

    transcribers = [t.strip() for t in args.transcribers.split(",") if t.strip()]
    processors = [p.strip() for p in args.processors.split(",") if p.strip()]

    if args.episodes.strip().lower() == "all":
        episodes = _discover_episodes(transcribers)
    else:
        episodes = [e.strip() for e in args.episodes.split(",") if e.strip()]

    for ep in episodes:
        out_path = Path("outputs") / ep / args.assessment_filename
        if out_path.exists():
            existing = _read_text(out_path)
            # Avoid overwriting/stacking on top of already hand-written assessments
            # (Episode 008 currently contains explicit manual inspection notes).
            if "These notes are based on manual inspection" in existing:
                print(f"Skip (already contains human manual notes): {out_path}")
                continue
        manual = build_draft_section(
            episode=ep,
            transcribers=transcribers,
            processors=processors,
            k_blocks=args.k,
        )
        prepend_manual_section(out_path, manual)
        print(f"Prepended manual draft to {out_path}")


if __name__ == "__main__":
    main()
