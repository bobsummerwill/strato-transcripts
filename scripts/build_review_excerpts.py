#!/usr/bin/env python3
"""Build excerpt packs to support manual transcript QA.

Goal
----
Generate small, human-readable excerpt packs (markdown) per episode that show:
  - selected speaker-turn excerpts from the intermediate transcript(s)
  - the corresponding excerpts from each available post-processed output
  - basic red-flag heuristics (entity/phrase novelty, retention, timestamp drift)

This is designed to make "manual inspection" feasible across many episodes.
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

from scripts.generate_quality_assessments import _discover_episodes  # type: ignore
from scripts.quality_metrics import compute_md_metrics, compute_txt_metrics


HEADER_RE = re.compile(r"^\*\*\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s*(SPEAKER_\d+):\*\*\s*(.*)$")
WORD_RE = re.compile(r"\b\w+\b")


@dataclass(frozen=True)
class Block:
    ts: str
    speaker: str
    text: str


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def parse_md_blocks(md_text: str) -> list[Block]:
    blocks: list[Block] = []
    cur_ts: str | None = None
    cur_speaker: str | None = None
    cur_lines: list[str] = []

    def flush() -> None:
        nonlocal cur_ts, cur_speaker, cur_lines
        if cur_ts and cur_speaker and cur_lines:
            text = " ".join([ln.strip() for ln in cur_lines if ln.strip()])
            blocks.append(Block(ts=cur_ts, speaker=cur_speaker, text=text.strip()))
        cur_ts, cur_speaker, cur_lines = None, None, []

    for line in md_text.splitlines():
        m = HEADER_RE.match(line.strip())
        if m:
            flush()
            cur_ts, cur_speaker = m.group(1), m.group(2)
            rest = m.group(3).strip()
            cur_lines = [rest] if rest else []
            continue

        if not line.strip():
            flush()
            continue

        if cur_ts is not None:
            cur_lines.append(line)

    flush()
    return blocks


CAP_SEQ_RE = re.compile(r"\b(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\b")


def cap_sequences(text: str) -> set[str]:
    # crude proxy for entities/proper-nouns (no spaCy dependency)
    return {m.group(0) for m in CAP_SEQ_RE.finditer(text)}


def sample_indices(n: int, k: int) -> list[int]:
    if n <= 0:
        return []
    if n <= k:
        return list(range(n))
    # deterministic “spread” sampling
    picks = [0, n // 4, n // 2, (3 * n) // 4, n - 1]
    out: list[int] = []
    for i in picks:
        if i not in out and 0 <= i < n:
            out.append(i)
    return out[:k]


def find_matching_block(blocks: list[Block], ts: str, speaker: str) -> Block | None:
    for b in blocks:
        if b.ts == ts and b.speaker == speaker:
            return b
    # fallback: same timestamp (speaker drift)
    for b in blocks:
        if b.ts == ts:
            return b
    return None


def md_word_count(md_text: str) -> int:
    # strip header prefixes
    t = re.sub(r"\*\*\[\d{1,2}:\d{2}(?::\d{2})?\]\s*SPEAKER_\d+:\*\*\s*", "", md_text)
    return len(WORD_RE.findall(t))


def build_episode_excerpt_pack(
    *,
    episode: str,
    transcribers: list[str],
    processors: list[str],
    k_blocks: int,
) -> str:
    inter_dir = Path("intermediates") / episode
    out_dir = Path("outputs") / episode

    lines: list[str] = []
    lines.append(f"# Manual Review Excerpts: `{episode}`")
    lines.append("")

    # Summarize what exists
    lines.append("## Files present")
    for tr in transcribers:
        md = inter_dir / f"{episode}_{tr}.md"
        if md.exists():
            lines.append(f"- intermediate: `{md}`")
    for tr in transcribers:
        for pr in processors:
            md = out_dir / f"{episode}_{tr}_{pr}.md"
            if md.exists():
                lines.append(f"- output: `{md}`")
    lines.append("")

    # Per transcriber blocks
    for tr in transcribers:
        inter_md_path = inter_dir / f"{episode}_{tr}.md"
        if not inter_md_path.exists():
            continue

        inter_md = _read_text(inter_md_path)
        inter_blocks = parse_md_blocks(inter_md)

        lines.append(f"---\n\n## Transcriber: `{tr}`\n")

        # Heuristic summary (retention and timestamp drift for each processor)
        base_words = md_word_count(inter_md)
        base_mm = compute_md_metrics(inter_md_path)
        base_caps = cap_sequences(inter_md)

        lines.append("### Quick heuristics")
        lines.append(f"- baseline words (md stripped): **{base_words:,}**")
        lines.append(f"- baseline timestamps: **{base_mm.timestamp_count}** (headers={base_mm.header_count})")
        lines.append("")

        for pr in processors:
            out_md_path = out_dir / f"{episode}_{tr}_{pr}.md"
            out_txt_path = out_dir / f"{episode}_{tr}_{pr}.txt"
            if not out_md_path.exists() or not out_txt_path.exists():
                continue
            out_mm = compute_md_metrics(out_md_path)
            out_tm = compute_txt_metrics(out_txt_path)
            retention = (out_tm.word_count / (base_words or 1))
            ratio = (out_mm.timestamp_count / (base_mm.timestamp_count or 1))

            out_caps = cap_sequences(_read_text(out_md_path))
            novel_caps = sorted(list(out_caps - base_caps))
            novelty = len(out_caps - base_caps)

            lines.append(f"- **{pr}**: retention={retention*100:0.1f}%, timestamps={out_mm.timestamp_count}/{base_mm.timestamp_count} (×{ratio:0.2f}), fmt_bad={out_mm.format_violations}, nonmono={out_mm.non_monotonic_timestamps}, novel_CAPS={novelty}")
            if novelty:
                lines.append(f"  - examples: {', '.join(novel_caps[:10])}")
        lines.append("")

        # Excerpts
        lines.append("### Excerpts (baseline vs outputs)")
        idxs = sample_indices(len(inter_blocks), k_blocks)
        if not idxs:
            lines.append("(No parseable timestamped blocks found in intermediate .md)\n")
            continue

        for idx in idxs:
            b = inter_blocks[idx]
            lines.append(f"#### [{b.ts}] {b.speaker} (block {idx+1}/{len(inter_blocks)})")
            lines.append("")
            lines.append("**Intermediate:**")
            lines.append("")
            lines.append(f"> {b.text}")
            lines.append("")

            for pr in processors:
                out_md_path = out_dir / f"{episode}_{tr}_{pr}.md"
                if not out_md_path.exists():
                    continue
                out_blocks = parse_md_blocks(_read_text(out_md_path))
                mb = find_matching_block(out_blocks, b.ts, b.speaker)
                lines.append(f"**{pr}:**")
                lines.append("")
                if mb is None:
                    lines.append("> (No matching timestamp found in output; likely timestamp regeneration or formatting drift.)")
                else:
                    lines.append(f"> {mb.text}")
                lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", default="all", help="Comma list or 'all'")
    ap.add_argument("--transcribers", default="assemblyai,whisperx-cloud,whisperx")
    ap.add_argument("--processors", default="opus,gemini,deepseek,chatgpt")
    ap.add_argument("--k", type=int, default=5, help="Number of blocks per transcriber")
    ap.add_argument("--combined", action="store_true", help="Also write outputs/REVIEW_EXCERPTS_ALL.md")
    args = ap.parse_args()

    transcribers = [t.strip() for t in args.transcribers.split(",") if t.strip()]
    processors = [p.strip() for p in args.processors.split(",") if p.strip()]

    if args.episodes.strip().lower() == "all":
        episodes = _discover_episodes(transcribers)
    else:
        episodes = [e.strip() for e in args.episodes.split(",") if e.strip()]

    combined_lines: list[str] = []
    if args.combined:
        combined_lines.append("# Manual Review Excerpts: ALL EPISODES")
        combined_lines.append("")

    for ep in episodes:
        pack = build_episode_excerpt_pack(
            episode=ep,
            transcribers=transcribers,
            processors=processors,
            k_blocks=args.k,
        )
        out_path = Path("outputs") / ep / "REVIEW_EXCERPTS.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(pack, encoding="utf-8")
        print(f"Wrote {out_path}")

        if args.combined:
            combined_lines.append("\n---\n")
            combined_lines.append(pack)

    if args.combined:
        out_path = Path("outputs") / "REVIEW_EXCERPTS_ALL.md"
        out_path.write_text("\n".join(combined_lines), encoding="utf-8")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
