#!/usr/bin/env python3
"""Generate per-episode transcript QUALITY_ASSESSMENT reports.

This script computes lightweight (no-LLM) metrics for:
  - word-count retention (word count vs intermediate baseline)
  - timestamp preservation (timestamp counts vs baseline)
  - basic format sanity (non-monotonic timestamps, header formatting violations)

It writes:
  outputs/<episode>/QUALITY_ASSESSMENT.md
and optionally a combined:
  outputs/ALL_EPISODES_QUALITY_ASSESSMENT.md

Design goals:
  - deterministic, fast, no external services
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# When executed as `python3 scripts/generate_quality_assessments.py`, Python sets
# `sys.path[0]` to `.../scripts`, which prevents `import scripts.<module>` from
# resolving unless we add the repo root to sys.path.
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.quality_metrics import (
    MdMetrics,
    TxtMetrics,
    compute_md_metrics,
    compute_txt_metrics,
)


WORD_RE = re.compile(r"\b\w+\b")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _episode_display_title(ep: str) -> str:
    # Match older file headings that upper-case and replace hyphens with spaces.
    return ep.replace("-", " ").upper()


def _md_word_count_stripping_timestamps(md_path: Path) -> int:
    """Baseline word count computed from intermediate .md with timestamps stripped.

    The pipeline uses `**[MM:SS] SPEAKER_XX:** ...` headers; strip those tokens
    and count words from the remaining text.
    """
    t = _read_text(md_path)
    # Remove markdown header prefix but keep content.
    # Example: **[00:01] SPEAKER_00:** Hello -> Hello
    t = re.sub(r"\*\*\[\d{1,2}:\d{2}(?::\d{2})?\]\s*SPEAKER_\d+:\*\*\s*", "", t)
    return len(WORD_RE.findall(t))


@dataclass(frozen=True)
class ComboMetrics:
    transcriber: str
    processor: str
    out_words: int
    retention: float
    ts_out: int
    ts_in: int
    md_headers: int
    speakers: int
    nonmono: int
    fmt_bad: int


def _format_pct(x: float) -> str:
    return f"{x * 100:5.1f}%"


def _generate_episode_report(
    *,
    episode: str,
    transcribers: list[str],
    processors: list[str],
    generated_date: str,
) -> dict[str, object]:
    """Generate one episode report.

    Returns:
      {"report": <str>, ...summary fields...}
    """

    inter_dir = Path("intermediates") / episode
    out_dir = Path("outputs") / episode

    # Baselines
    baselines: dict[str, tuple[int, MdMetrics]] = {}
    for tr in transcribers:
        md = inter_dir / f"{episode}_{tr}.md"
        if not md.exists():
            continue
        baselines[tr] = (_md_word_count_stripping_timestamps(md), compute_md_metrics(md))

    # Collect combos
    combos: list[ComboMetrics] = []
    for tr in transcribers:
        if tr not in baselines:
            continue
        base_words, base_md = baselines[tr]

        for pr in processors:
            out_md = out_dir / f"{episode}_{tr}_{pr}.md"
            if not out_md.exists():
                continue
            tm: TxtMetrics = compute_txt_metrics(out_md)
            mm: MdMetrics = compute_md_metrics(out_md)
            retention = (tm.word_count / (base_words or 1))
            combos.append(
                ComboMetrics(
                    transcriber=tr,
                    processor=pr,
                    out_words=tm.word_count,
                    retention=retention,
                    ts_out=mm.timestamp_count,
                    ts_in=base_md.timestamp_count,
                    md_headers=mm.header_count,
                    speakers=mm.speakers,
                    nonmono=mm.non_monotonic_timestamps,
                    fmt_bad=mm.format_violations,
                )
            )

    supported = len(combos)
    expected = len(baselines) * len(processors)

    # Choose recommendations (heuristic)
    def ts_ratio(c: ComboMetrics) -> float:
        return (c.ts_out / c.ts_in) if c.ts_in else 1.0

    def ts_delta(c: ComboMetrics) -> int:
        return abs(c.ts_out - c.ts_in) if c.ts_in else 0

    def fmt_ok(c: ComboMetrics) -> bool:
        return c.nonmono == 0 and c.fmt_bad == 0

    def retention_ok_strict(c: ComboMetrics) -> bool:
        return 0.90 <= c.retention <= 1.10

    def retention_ok_loose(c: ComboMetrics) -> bool:
        # Match the pipeline validator (85–115%) while still flagging <90% as a warning.
        return 0.85 <= c.retention <= 1.15

    def ts_exact(c: ComboMetrics) -> bool:
        return c.ts_out == c.ts_in

    def ts_near(c: ComboMetrics) -> bool:
        # Allow tiny count drift; useful when providers drop/add a single turn.
        r = ts_ratio(c)
        return ts_delta(c) <= 1 and 0.95 <= r <= 1.05

    def ts_not_exploded_or_dropped(c: ComboMetrics) -> bool:
        r = ts_ratio(c)
        return 0.80 <= r <= 1.20

    def rank_key(c: ComboMetrics) -> tuple[int, int, int, int, float]:
        # Prefer strict retention, good format, non-exploded timestamps, then closeness.
        return (
            1 if retention_ok_strict(c) else 0,
            1 if fmt_ok(c) else 0,
            1 if ts_not_exploded_or_dropped(c) else 0,
            -ts_delta(c),
            c.retention,
        )

    stages = [
        lambda c: ts_exact(c) and fmt_ok(c) and retention_ok_strict(c),
        lambda c: ts_exact(c) and retention_ok_loose(c),
        lambda c: ts_near(c) and fmt_ok(c) and retention_ok_strict(c),
        lambda c: ts_near(c) and retention_ok_loose(c),
        lambda c: ts_not_exploded_or_dropped(c) and fmt_ok(c) and retention_ok_loose(c),
        lambda c: retention_ok_loose(c),
        lambda c: True,
    ]

    recommended: list[ComboMetrics] = []
    for pred in stages:
        pool = [c for c in combos if pred(c)]
        if pool:
            pool.sort(key=rank_key, reverse=True)
            recommended = pool[:3]
            break

    # Collect systemic flags for aggregation
    critical_ts_explosions = [c for c in combos if c.ts_in and c.ts_out > int(c.ts_in * 1.2)]
    critical_ts_drops = [c for c in combos if c.ts_in and c.ts_out < int(c.ts_in * 0.8)]

    lines: list[str] = []
    lines.append("=" * 80)
    lines.append(f"QUALITY ASSESSMENT: {_episode_display_title(episode)}")
    lines.append("=" * 80)
    lines.append(f"Episode: {episode}")
    lines.append(f"Generated: {generated_date}")
    lines.append("")
    lines.append(
        f"Supported Combinations: {supported} (found) / {expected} (expected: {len(baselines)} transcribers × {len(processors)} post-processors)"
    )
    lines.append("")

    lines.append("=" * 80)
    lines.append("EXECUTIVE SUMMARY")
    lines.append("=" * 80)
    lines.append("")
    lines.append(
        "IMPORTANT PIPELINE NOTE:\n"
        "  Post-processing should run on the intermediate *.md transcripts\n"
        "  so post-processors can preserve the original timestamps."
    )
    lines.append("")

    # Key findings
    if combos:
        ret_ok = sum(1 for c in combos if 0.9 <= c.retention <= 1.1)
        ts_exact = sum(1 for c in combos if c.ts_out == c.ts_in)
        lines.append("KEY FINDINGS:")
        lines.append("")
        lines.append(f"1) WORD-COUNT RETENTION: {ret_ok}/{supported} outputs are within 90–110% of baseline")
        lines.append(f"2) TIMESTAMP PRESERVATION: {ts_exact}/{supported} outputs have an exact timestamp count match")
        if critical_ts_explosions:
            lines.append(f"3) CRITICAL: {len(critical_ts_explosions)} outputs show timestamp explosion (likely regenerated timestamps)")
        if critical_ts_drops:
            lines.append(f"4) WARNING: {len(critical_ts_drops)} outputs show major timestamp loss")
        lines.append("")

    # Recommendations
    if recommended:
        lines.append("RECOMMENDED FOR THIS EPISODE:")
        for c in recommended:
            lines.append(
                f"  • {c.transcriber} + {c.processor}\n"
                f"      - timestamps: {c.ts_out}/{c.ts_in}\n"
                f"      - retention: {_format_pct(c.retention)}"
            )
        lines.append("")

    lines.append("=" * 80)
    lines.append("INPUT (INTERMEDIATE) TRANSCRIPTS")
    lines.append("=" * 80)
    lines.append("")
    lines.append(
        "Word counts (baseline for retention; computed from the intermediate .md\n"
        "transcripts with timestamps stripped):"
    )
    for tr in transcribers:
        if tr not in baselines:
            continue
        md = inter_dir / f"{episode}_{tr}.md"
        base_words, base_md = baselines[tr]
        lines.append(f"  • {md.name:45} {base_words:6,} words")
    lines.append("")
    lines.append("Timestamp/header counts in intermediate .md (GROUND TRUTH timing):")
    for tr in transcribers:
        if tr not in baselines:
            continue
        md = inter_dir / f"{episode}_{tr}.md"
        _, base_md = baselines[tr]
        lines.append(
            f"  • {md.name:45} {base_md.timestamp_count:4} timestamps ({base_md.header_count} timestamped headers)"
        )
    lines.append("")

    lines.append("=" * 80)
    lines.append("OUTPUT (POST-PROCESSED) WORD COUNT ANALYSIS")
    lines.append("=" * 80)
    lines.append("")
    lines.append("Legend:")
    lines.append("  retention = output_words / input_words")
    lines.append("  timestamps = output timestamp count / input timestamp count")
    lines.append("")

    for tr in transcribers:
        if tr not in baselines:
            continue
        base_words, base_md = baselines[tr]
        lines.append(f"{tr.upper()} (input: {base_words:,} words; {base_md.timestamp_count} timestamps)")
        lines.append("  processor     words    retention   timestamps")

        rows = [c for c in combos if c.transcriber == tr]
        rows.sort(key=lambda c: (c.processor,))
        for c in rows:
            warn = ""
            if c.ts_in:
                if c.ts_out != c.ts_in:
                    delta = c.ts_out - c.ts_in
                    if abs(delta) >= 5 or (c.ts_out > int(c.ts_in * 1.2) or c.ts_out < int(c.ts_in * 0.8)):
                        warn = "   ⚠ CRITICAL" if c.ts_out > int(c.ts_in * 1.2) else "   ⚠"
                    else:
                        warn = "   ⚠"

            lines.append(
                f"  {c.processor:10} {c.out_words:6,}   {_format_pct(c.retention):>8}   {c.ts_out}/{c.ts_in}{warn}"
            )
        lines.append("")

    lines.append("=" * 80)
    lines.append("QUALITY FLAGS / REVIEW NOTES")
    lines.append("=" * 80)
    lines.append("")
    lines.append("1) Timestamp count changes are the primary red flag")
    lines.append(
        "   Any output with far more timestamps than the input is not preserving the\n"
        "   diarization paragraphing and is likely regenerating timestamps."
    )
    lines.append("")
    if critical_ts_explosions:
        lines.append("   CRITICAL failures observed:")
        for c in sorted(critical_ts_explosions, key=lambda x: (x.transcriber, x.processor)):
            lines.append(f"     - {c.transcriber} + {c.processor}: {c.ts_out} timestamps vs {c.ts_in} input")
        lines.append("")

    # Include extra automated checks so the report is actionable.
    bad_format = [c for c in combos if c.nonmono or c.fmt_bad]
    if bad_format:
        lines.append("2) Format / ordering issues")
        for c in sorted(bad_format, key=lambda x: (x.transcriber, x.processor)):
            bits = []
            if c.nonmono:
                bits.append(f"nonmono={c.nonmono}")
            if c.fmt_bad:
                bits.append(f"fmt_bad={c.fmt_bad}")
            lines.append(f"     - {c.transcriber} + {c.processor}: {', '.join(bits)}")
        lines.append("")

    lines.append("RECOMMENDATION:")
    lines.append("  • Use intermediate .md files as the canonical timestamped transcript.")
    lines.append("  • Use post-processed .md outputs for corrected wording / readability.")
    lines.append("")

    lines.append("=" * 80)
    lines.append("MANUAL SPOT-CHECK NOTES (CONTENT QUALITY)")
    lines.append("=" * 80)
    lines.append("")
    lines.append(
        "This file is generated from automated metrics only.\n"
        "Add manual notes here if you spot entity errors, hallucinations, or other\n"
        "content issues specific to this episode."
    )
    lines.append("")

    lines.append("=" * 80)
    lines.append("PROJECT IMPROVEMENT RECOMMENDATIONS (TO REDUCE MANUAL EDITING)")
    lines.append("=" * 80)
    lines.append("")
    lines.append("1) Deterministic timestamp preservation (recommended architecture)")
    lines.append("   Do NOT ask the model to 'preserve timestamps' in free-form text.")
    lines.append("   Instead: parse -> correct text only -> reassemble with original timestamps.")
    lines.append("")
    lines.append("2) Entity constraints + validation")
    lines.append("   Reject outputs that introduce new PERSON entities not present in input/allowlist.")
    lines.append("")
    lines.append("3) Validation + auto-retry")
    lines.append("   Enforce exact timestamp sequence match, non-decreasing timestamps, and header format.")
    lines.append("")
    lines.append("=" * 80)

    return {
        "report": "\n".join(lines) + "\n",
        "episode": episode,
        "supported": supported,
        "expected": expected,
        "recommended": [(c.transcriber, c.processor) for c in recommended],
        "critical_ts_explosions": [(c.transcriber, c.processor) for c in critical_ts_explosions],
        "critical_ts_drops": [(c.transcriber, c.processor) for c in critical_ts_drops],
    }


def _discover_episodes(transcribers: list[str]) -> list[str]:
    eps: set[str] = set()
    inter_root = Path("intermediates")
    if not inter_root.exists():
        return []
    for d in inter_root.iterdir():
        if not d.is_dir():
            continue
        ep = d.name
        # Require at least one baseline md.
        if any((d / f"{ep}_{tr}.md").exists() for tr in transcribers):
            eps.add(ep)
    return sorted(eps)


def _write_all_episodes_report(summaries: list[dict[str, object]], generated_date: str) -> None:
    out_path = Path("outputs") / "ALL_EPISODES_QUALITY_METRICS.md"
    lines: list[str] = []
    lines.append("=" * 80)
    lines.append("COMPREHENSIVE QUALITY ASSESSMENT: ALL EPISODES (AUTOGENERATED)")
    lines.append("=" * 80)
    lines.append("Project: Stratomercata Transcripts")
    lines.append(f"Generated: {generated_date}")
    lines.append(f"Episodes Evaluated: {len(summaries)}")
    lines.append("")

    # Aggregate recommendation counts
    rec_counts: dict[tuple[str, str], int] = {}
    explosion_counts: dict[tuple[str, str], int] = {}
    drop_counts: dict[tuple[str, str], int] = {}

    for s in summaries:
        for tr, pr in s.get("recommended", []):
            rec_counts[(tr, pr)] = rec_counts.get((tr, pr), 0) + 1
        for tr, pr in s.get("critical_ts_explosions", []):
            explosion_counts[(tr, pr)] = explosion_counts.get((tr, pr), 0) + 1
        for tr, pr in s.get("critical_ts_drops", []):
            drop_counts[(tr, pr)] = drop_counts.get((tr, pr), 0) + 1

    lines.append("=" * 80)
    lines.append("EXECUTIVE SUMMARY")
    lines.append("=" * 80)
    lines.append("")
    lines.append(
        "This aggregate report is derived from per-episode automated metrics.\n"
        "It summarizes which combinations most often preserve timestamps and retain content."
    )
    lines.append("")

    lines.append("Most frequently recommended (top-3 per episode):")
    for (tr, pr), n in sorted(rec_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:20]:
        lines.append(f"  • {tr} + {pr}: {n}/{len(summaries)} episodes")
    if not rec_counts:
        lines.append("  (no recommendations produced; check inputs/outputs exist)")
    lines.append("")

    if explosion_counts:
        lines.append("Timestamp explosion (CRITICAL):")
        for (tr, pr), n in sorted(explosion_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:20]:
            lines.append(f"  • {tr} + {pr}: {n}/{len(summaries)} episodes")
        lines.append("")

    if drop_counts:
        lines.append("Major timestamp loss (WARNING):")
        for (tr, pr), n in sorted(drop_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:20]:
            lines.append(f"  • {tr} + {pr}: {n}/{len(summaries)} episodes")
        lines.append("")

    lines.append("=" * 80)
    lines.append("PER-EPISODE LINKS")
    lines.append("=" * 80)
    lines.append("")
    for s in summaries:
        ep = s["episode"]
        lines.append(f"- outputs/{ep}/QUALITY_ASSESSMENT.md")
    lines.append("")
    lines.append("=" * 80)

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--episodes",
        default="all",
        help="Comma-separated episode basenames, or 'all' (default)",
    )
    ap.add_argument(
        "--transcribers",
        default="assemblyai,whisperx-cloud,whisperx",
        help="Comma-separated transcribers",
    )
    ap.add_argument(
        "--processors",
        default="opus,gemini,deepseek,chatgpt",
        help="Comma-separated processors",
    )
    ap.add_argument(
        "--write-all-episodes",
        action="store_true",
        help="Also regenerate outputs/ALL_EPISODES_QUALITY_METRICS.md",
    )
    ap.add_argument(
        "--output-filename",
        default="QUALITY_METRICS.md",
        help="Episode-level output filename (default: QUALITY_METRICS.md)",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing outputs/<episode>/QUALITY_ASSESSMENT.md files",
    )
    args = ap.parse_args()

    transcribers = [t.strip() for t in args.transcribers.split(",") if t.strip()]
    processors = [p.strip() for p in args.processors.split(",") if p.strip()]

    if args.episodes.strip().lower() == "all":
        episodes = _discover_episodes(transcribers)
    else:
        episodes = [e.strip() for e in args.episodes.split(",") if e.strip()]

    generated_date = dt.date.today().strftime("%B %d, %Y")
    summaries: list[dict[str, object]] = []

    for ep in episodes:
        out_path = Path("outputs") / ep / args.output_filename
        s = _generate_episode_report(
            episode=ep,
            transcribers=transcribers,
            processors=processors,
            generated_date=generated_date,
        )

        # Write unless skipping existing.
        if out_path.exists() and not args.force:
            print(f"Skip (exists): {out_path}")
        else:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(str(s["report"]), encoding="utf-8")
            print(f"Wrote {out_path}")

        summaries.append({k: v for k, v in s.items() if k != "report"})

    if args.write_all_episodes:
        _write_all_episodes_report(summaries, generated_date)
        print("Wrote outputs/ALL_EPISODES_QUALITY_METRICS.md")


if __name__ == "__main__":
    main()
