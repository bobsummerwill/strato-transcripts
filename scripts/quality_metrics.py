#!/usr/bin/env python3
"""Lightweight transcript quality metrics.

This is intentionally heuristic (no model calls). It helps spot common
format/retention/timestamp issues quickly.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MdMetrics:
    timestamp_count: int
    header_count: int
    speakers: int
    non_monotonic_timestamps: int
    format_violations: int


@dataclass(frozen=True)
class TxtMetrics:
    word_count: int


TS_RE = re.compile(r"\[(\d{1,2}):(\d{2})\]")
HEADER_RE = re.compile(r"^\*\*\[\d{1,2}:\d{2}\]\s*SPEAKER_\d+:\*\*\s+\S")
HEADER_ANYWHERE_RE = re.compile(r"\*\*\[\d{1,2}:\d{2}\]\s*SPEAKER_\d+:\*\*")
SPEAKER_RE = re.compile(r"SPEAKER_\d+")
WORD_RE = re.compile(r"\b\w+\b")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _timestamps_seconds(md_text: str) -> list[int]:
    return [int(m) * 60 + int(s) for m, s in TS_RE.findall(md_text)]


def compute_md_metrics(md_path: Path) -> MdMetrics:
    t = _read_text(md_path)
    ts = _timestamps_seconds(t)

    nonmono = 0
    prev = -1
    for x in ts:
        if x < prev:
            nonmono += 1
        prev = x

    format_bad = 0
    for line in t.splitlines():
        if TS_RE.search(line) and not HEADER_RE.match(line):
            format_bad += 1

    return MdMetrics(
        timestamp_count=len(ts),
        header_count=len(HEADER_ANYWHERE_RE.findall(t)),
        speakers=len(set(SPEAKER_RE.findall(t))),
        non_monotonic_timestamps=nonmono,
        format_violations=format_bad,
    )


def compute_txt_metrics(txt_path: Path) -> TxtMetrics:
    t = _read_text(txt_path)
    return TxtMetrics(word_count=len(WORD_RE.findall(t)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", help="Episode basename (e.g. episode008-michael-parenti)")
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
    args = ap.parse_args()

    ep = args.episode
    transcribers = [t.strip() for t in args.transcribers.split(",") if t.strip()]
    processors = [p.strip() for p in args.processors.split(",") if p.strip()]

    inter_dir = Path("intermediates") / ep
    out_dir = Path("outputs") / ep

    print("BASELINES (intermediate)")
    baselines: dict[str, tuple[TxtMetrics, MdMetrics]] = {}
    for tr in transcribers:
        txt = inter_dir / f"{ep}_{tr}.txt"
        md = inter_dir / f"{ep}_{tr}.md"
        baselines[tr] = (compute_txt_metrics(txt), compute_md_metrics(md))
        tm, mm = baselines[tr]
        print(
            f"{tr:13} txt_words={tm.word_count:5} md_ts={mm.timestamp_count:4} md_headers={mm.header_count:4} "
            f"speakers={mm.speakers} nonmono={mm.non_monotonic_timestamps} fmt_bad={mm.format_violations}"
        )

    print("\nOUTPUT METRICS")
    print(
        "transcriber     processor  out_words  ret%    ts_out/ts_in  md_headers  speakers  nonmono  fmt_bad"
    )
    for tr in transcribers:
        base_txt, base_md = baselines[tr]
        for pr in processors:
            out_txt = out_dir / f"{ep}_{tr}_{pr}.txt"
            out_md = out_dir / f"{ep}_{tr}_{pr}.md"
            if not out_txt.exists() or not out_md.exists():
                continue
            tm = compute_txt_metrics(out_txt)
            mm = compute_md_metrics(out_md)
            ret = (tm.word_count / (base_txt.word_count or 1)) * 100
            ts_ratio = mm.timestamp_count / (base_md.timestamp_count or 1)
            print(
                f"{tr:13} {pr:9} {tm.word_count:8} {ret:6.1f} "
                f"{mm.timestamp_count:4}/{base_md.timestamp_count:<4} ({ts_ratio:5.2f}) "
                f"{mm.header_count:9} {mm.speakers:8} {mm.non_monotonic_timestamps:7} {mm.format_violations:7}"
            )


if __name__ == "__main__":
    main()

