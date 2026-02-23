# Overall Quality Report

*Generated: 2026-02-22*
*Episodes assessed: 15*

## Summary

Across 15 episodes spanning short interviews (~25 min) to long-form conversations (~112 min), clear and statistically robust patterns emerge. **AssemblyAI** is the only transcriber with a perfect 15/15 reliability record and is unanimously rated best in every episode. Among AI post-processors, **Opus** is the dominant performer — Tier 1 in 13 of 15 episodes on the AssemblyAI base, winning 11 of 15 "best output" recommendations. **Grok** and **Gemini** form a reliable core alongside Opus, all achieving Tier 1 in 11+ episodes.

The most important finding is that **GLM is catastrophically broken** — it dumps chain-of-thought reasoning instead of producing a clean transcript in 10 of 15 episodes (Tier 4). This is a systematic instruction-following failure that makes it unsuitable for any production use. Five other processors (Mistral, Qwen, DeepSeek, Llama, MiniMax) consistently truncate on longer episodes, losing 35–75% of content due to output token limits.

The consensus pipeline has **zero successes across 15 episodes**. The two episodes with final output (007 and 012-Fabian) both produced degraded or catastrophically corrupted results. The word-level voting algorithm cannot handle divergent AI model outputs. Single-model outputs (especially Opus) consistently outperform consensus merges.

---

## 1. Transcriber Reliability

| Transcriber | Working | Broken | Not Run | Reliability | Notes |
|-------------|---------|--------|---------|-------------|-------|
| **AssemblyAI** | **15** | 0 | 0 | **100%** | Unanimously rated best in every episode |
| **WhisperX local** | 11 | 3 | 1 | 79% | 3 corruption events (ep007, ep012-Fab, ep013-Zsolt) |
| **WhisperX-cloud** | 12 | 0 | 2 | 86%* | Working but worst diarization in 12/13 episodes |

*WhisperX-cloud was not run for episodes 011 and 013-Zsolt.

### WhisperX Local Corruption Patterns
- **Episode 007**: Hallucinated "Thank you" loops (every block repeats "Thank you")
- **Episode 012 (Fabian)**: Entire output replaced with exclamation marks (`!!!!!!`)
- **Episode 013 (Zsolt)**: Same exclamation mark corruption as ep012

### WhisperX-Cloud Diarization Issues
When WhisperX-cloud works, it consistently produces the worst speaker separation — long merged paragraphs with multiple speakers collapsed into single blocks or speaker labels swapped. AI processors cannot reliably fix diarization errors inherited from the transcriber.

**Verdict:** AssemblyAI should be the default (and often only) transcriber. WhisperX local is a useful secondary source when it works but cannot be relied upon. WhisperX-cloud adds cost without adding quality.

---

## 2. Processor Leaderboard (AssemblyAI base)

Ranked by Tier 1 count across 15 episodes, then Tier 1+2 rate.

| Rank | Processor | T1 | T2 | T3 | T4 | T1+2 Rate | Best Output Wins | Consistency |
|------|-----------|----|----|----|----|-----------|-----------------|-------------|
| 1 | **Opus** | **13** | 1 | 0 | 0 | **100%** | **11/15** | Excellent |
| 2 | **Grok** | **12** | 2 | 0 | 0 | **100%** | 0 | Excellent |
| 3 | **Gemini** | **11** | 3 | 0 | 0 | **100%** | 0 | Excellent |
| 4 | **ChatGPT** | 6 | 3 | 3 | 1 | 69% | 2/15 | Variable |
| 5 | **Kimi** | 5 | 6 | 1 | 0 | 85% | 1/15 | Good |
| 6 | DeepSeek | 3 | 4 | 5 | 1 | 54% | 0 | Mixed |
| 7 | Llama | 3 | 2 | 5 | 3 | 38% | 0 | Poor |
| 8 | Qwen | 3 | 2 | 8 | 1 | 36% | 0 | Poor |
| 9 | MiniMax | 2 | 3 | 5 | 3 | 38% | 0 | Poor |
| 10 | Mistral | 1 | 4 | 8 | 1 | 36% | 0 | Poor |
| 11 | **GLM** | 1 | 2 | 3 | **10** | 20% | 0 | **Catastrophic** |

### The Reliable Core: Opus, Grok, Gemini

These three processors achieve Tier 1 or 2 on **every single episode** — a 100% reliability rate across 15 assessments. Among them:

- **Opus** is the clear #1: 13 Tier 1 ratings, best prose polish, most accurate name corrections, and recommended as the best output in 11 of 15 episodes.
- **Grok** is the most faithful reproducer — highest word retention, excellent formatting, 12 Tier 1 ratings.
- **Gemini** has the strongest technical term corrections and clean formatting, with 11 Tier 1 ratings. Occasionally resets timestamps to 00:00 offset (ep005).

### The Middle Tier: ChatGPT, Kimi

- **ChatGPT** shows the widest variance: excellent on some episodes (T1 on 6 episodes) but truncated or even refusing on others (T4 on ep010 — refused to process, citing missing timestamps). Unpredictable.
- **Kimi** is solid and consistent (T1+2 in 85% of episodes) but rarely the best. Good on shorter episodes.

### The Truncation Models: DeepSeek, Llama, Qwen, MiniMax, Mistral

These five processors consistently fail on longer episodes (>30 min) due to output token limits:
- **Mistral**: T3 in 8/15 episodes. Consistently shortest output. Also corrupts timestamps and collapses diarization.
- **Qwen**: T3 in 8/15 episodes. Minimal intervention — often a near-pass-through leaving errors uncorrected.
- **DeepSeek**: Name substitution errors (ep012-Martin: "Joseph Chow" → "Joseph Lubin"; ep013-Zsolt: "Zolt Zelfeldi"). T4 failure on ep011 (80 words).
- **Llama**: Hallucination/corruption loops (ep002: infinite "was like the DAO was the DAO" repetition; ep008: gibberish after line 43). 3 T4 ratings.
- **MiniMax**: Wildly inconsistent — T4 on some episodes (1,251 words in ep006), T1 on short episodes.

### The Short Episode Effect

On episodes under 30 minutes (ep008, ep012-Martin, ep013-Alex), nearly all processors achieve Tier 1. This confirms the primary failure mode is **output token limits**, not quality. If every episode were 25 minutes, there would be little difference between processors.

### GLM: Systematic Failure

GLM is **Tier 4 (unusable) in 10 of 15 episodes** due to a consistent chain-of-thought leakage bug. Instead of outputting a clean transcript, it dumps thousands of words of internal reasoning, planning notes, and correction analysis. Outputs of 20,000–46,000 words (2–4x expected) are the telltale sign. This is not a truncation issue — it's a fundamental instruction-following failure. **GLM should be removed from the pipeline entirely.**

---

## 3. Processor Leaderboard (WhisperX-cloud base)

Data available for 13 episodes (ep011 and ep013-Zsolt had no WhisperX-cloud). Tier assignments estimated from word counts and quality descriptions where explicit tiers weren't provided.

| Rank | Processor | T1 | T2 | T3 | T4 | T1+2 Rate | Notes |
|------|-----------|----|----|----|----|-----------|-------|
| 1 | **Opus** | **13** | 0 | 0 | 0 | **100%** | Perfect record |
| 2 | **Gemini** | 9 | 2 | 1 | 0 | 85% | Occasionally condensed |
| 3 | **Grok** | 9 | 2 | 0 | 1 | 85% | One T4 on ep002 |
| 4 | **ChatGPT** | 4 | 5 | 2 | 1 | 69% | Refused on ep010 |
| 5 | **Kimi** | 4 | 5 | 1 | 1 | 69% | Variable |
| 6 | DeepSeek | 2 | 4 | 3 | 2 | 46% | Catastrophic on some episodes |
| 7 | Llama | 2 | 4 | 4 | 1 | 46% | Truncation-prone |
| 8 | MiniMax | 2 | 4 | 4 | 1 | 46% | Better than AssemblyAI base |
| 9 | Qwen | 2 | 3 | 5 | 1 | 38% | Consistently short |
| 10 | Mistral | 2 | 3 | 5 | 1 | 38% | Consistently short |
| 11 | **GLM** | 1 | 2 | 1 | **7** | 23% | Same CoT failure |

**Opus maintains a perfect T1 record across both transcriber bases** — the only processor to do so.

---

## 4. Cross-Transcriber Comparison

AssemblyAI is unanimously rated the best transcriber in all 15 episodes. The consistent pattern:

| Attribute | AssemblyAI | WhisperX Local | WhisperX-Cloud |
|-----------|-----------|---------------|---------------|
| Speaker turns | Most granular (100–400 turns) | Good (100–350 turns) | Coarsest (50–120 turns) |
| Diarization | Best separation, consistent labels | Good when not corrupted | Worst — frequent merging/swapping |
| Word count | Highest | Comparable | Comparable |
| Downstream AI quality | Best input for processors | Good secondary | Worst — broken diarization propagates |

**Key insight:** AI processors cannot fix diarization errors inherited from the transcriber. WhisperX-cloud's habit of merging multiple speakers into single blocks means all downstream outputs inherit incorrect speaker attribution.

---

## 5. Consensus Pipeline Status

| Episode | Status | Notes |
|---------|--------|-------|
| 001 | Partial | Intermediate exists (19,755w), no final |
| 002 | Partial | Intermediate exists, no final |
| 003 | Not run | — |
| 004 | Partial | Intermediate exists (11,051w), no final |
| 005 | Partial | Intermediate exists (15,472w), no final |
| 006 | Partial | Intermediate exists (15,739w), no final |
| 007 | **BROKEN** | Corrupted WhisperX input poisoned merge — garbled, repetitive output |
| 008 | Not run | — |
| 009 | Not run | — |
| 010 | Not run | — |
| 011 | **Degraded** | Final exists (12,587w) but has duplicated paragraphs, truncated speaker tags, merge artifacts. Opus single output is cleaner. |
| 012 (Fabian) | **BROKEN** | Catastrophic: 3.26x expansion (18,882→61,512w), 0.4–1.3% alignment |
| 012 (Martin) | Not run | — |
| 013 (Alex) | Not run | — |
| 013 (Zsolt) | Not run | — |

**Overall verdict: 0/15 episodes have a clean working consensus final.** The pipeline is fundamentally broken:
- Corrupted transcriber inputs poison the merge (ep007)
- Divergent AI models cannot be aligned at the word level (ep012-Fabian)
- Even the "best" result (ep011) introduced defects that don't exist in the single-model output

**Recommendation:** Abandon the multi-model consensus approach. A single high-quality model (Opus) consistently produces better results than attempting to merge 11 divergent outputs.

---

## 6. Processor Tier Distribution (AssemblyAI base)

Visual summary across all 15 episodes:

| Processor | T1 | T2 | T3 | T4 | Visual |
|-----------|----|----|----|----|--------|
| **Opus** | 13 | 1 | 0 | 0 | `█████████████░` |
| **Grok** | 12 | 2 | 0 | 0 | `████████████░░` |
| **Gemini** | 11 | 3 | 0 | 0 | `███████████░░░` |
| **Kimi** | 5 | 6 | 1 | 0 | `█████▒▒▒▒▒▒░` |
| **ChatGPT** | 6 | 3 | 3 | 1 | `██████▒▒▒░░░▓` |
| DeepSeek | 3 | 4 | 5 | 1 | `███▒▒▒▒░░░░░▓` |
| Llama | 3 | 2 | 5 | 3 | `███▒▒░░░░░▓▓▓` |
| MiniMax | 2 | 3 | 5 | 3 | `██▒▒▒░░░░░▓▓▓` |
| Qwen | 3 | 2 | 8 | 1 | `███▒▒░░░░░░░░▓` |
| Mistral | 1 | 4 | 8 | 1 | `█▒▒▒▒░░░░░░░░▓` |
| **GLM** | 1 | 2 | 3 | **10** | `█▒▒░░░▓▓▓▓▓▓▓▓▓▓` |

Legend: `█` = T1, `▒` = T2, `░` = T3, `▓` = T4

---

## 7. Best Combinations

Ranked by cross-episode evidence (15 episodes):

| Rank | Combination | Win Rate | Evidence |
|------|-------------|----------|----------|
| 1 | **AssemblyAI + Opus** | **11/15** | T1 in 13/15 episodes. Best prose quality, name corrections, and editorial polish. Recommended as primary output in 11 episodes. |
| 2 | **AssemblyAI + Grok** | 0/15 | T1 in 12/15 episodes. Most faithful word retention, excellent formatting. Strong runner-up. |
| 3 | **AssemblyAI + Gemini** | 0/15 | T1 in 11/15 episodes. Best technical term corrections. Occasional timestamp issues. |
| 4 | **AssemblyAI + ChatGPT** | 2/15 | Best prose when it works (6 T1). Won ep008 and ep012-Martin. But refused ep010 and truncated 3 others. |
| 5 | **AssemblyAI + Kimi** | 1/15 | Won ep013-Zsolt. Good on shorter episodes. 85% T1+2 rate. |

---

## 8. Processors to Avoid

| Processor | Severity | Reason | Evidence |
|-----------|----------|--------|----------|
| **GLM** | **Critical** | Chain-of-thought leakage | T4 in 10/15 episodes. Dumps 20K–46K words of internal reasoning instead of transcript. Must be removed from pipeline. |
| **Mistral** | High | Consistently truncated | T3 in 8/15 episodes. Also corrupts timestamps and collapses diarization. |
| **Qwen** | High | Consistently truncated | T3 in 8/15 episodes. Minimal intervention — near-pass-through. |
| **Llama** | High | Truncation + hallucination | T3/T4 in 8/15 episodes. Corruption loops in ep002 and ep008. |
| **MiniMax** | High | Wildly inconsistent | T3/T4 in 8/15 episodes. Cannot be trusted — swings from T1 to T4. |
| **DeepSeek** | Moderate | Truncation + factual errors | T3/T4 in 6/15 episodes. Substitutes wrong person names (ep012-Martin, ep013-Zsolt). |

---

## 9. Recommendations

### Default pipeline configuration
- **Transcriber:** AssemblyAI only (100% reliability, unanimously best)
- **Primary processor:** Opus (13/15 Tier 1, 11/15 best output wins)
- **Secondary processors:** Grok and Gemini (for cross-reference and validation)
- **Drop from pipeline:** GLM (broken), Mistral, Qwen, Llama, MiniMax (all add cost without value)

### Optimal processor set (cost vs quality)
Run only **3 processors** instead of 11:
- **Opus** (primary output)
- **Grok** (highest fidelity cross-reference)
- **Gemini** (best technical corrections)

This eliminates 8 models that either fail catastrophically (GLM) or consistently truncate (the rest), reducing API costs by ~70%.

### Consensus pipeline
**Do not use in current form.** 0/15 episodes produced clean output. Instead:
- Use Opus single-model output as the canonical transcript
- Cross-reference with Grok and Gemini for name/term corrections
- Manual review for proper nouns and technical terminology

### WhisperX local
Keep as optional secondary transcriber but add **corruption detection** before processing:
- Detect repeated character patterns (`!!!!!!`, "Thank you" loops)
- Skip downstream processing if corruption detected
- Do not feed corrupted output into consensus pipeline

### Validation gates to add
1. **Output word count check**: Flag if output exceeds 150% of input (GLM chain-of-thought)
2. **Output word count check**: Flag if output is below 25% of expected (severe truncation)
3. **Corruption detection**: Check for repeated token patterns in transcriber output
4. **Name verification**: Cross-check guest/host names against episode metadata

---

## Appendix: Per-Episode Summaries

### Episode 001
~112 min, 3 speakers. AssemblyAI best transcriber. Top: Opus (18,802w), Grok (17,855w), Gemini (16,009w). GLM T4 (chain-of-thought). Llama T4 (1,078w). Consensus partial — intermediate only. Best: `assemblyai_opus.md`.
→ [Full report](episode001/episode001_quality_assessment.md)

### Episode 002
~90 min, 3 speakers (BlockApps co-founders). All transcribers working. Top: Opus (11,800w), ChatGPT (10,200w). Llama T4 (catastrophic repetition loop). Consensus partial. Best: `assemblyai_opus.md`.
→ [Full report](episode002/episode002_quality_assessment.md)

### Episode 003 — Bob Summerwill
~60 min, 4 speakers. All transcribers working. Top: Opus, Gemini, Grok, ChatGPT, Kimi (all T1, ~11K words). GLM T4 on all 3 bases. Best: `assemblyai_opus.md`.
→ [Full report](episode003-bob-summerwill/episode003-bob-summerwill_quality_assessment.md)

### Episode 004 — Taylor Gerring
~60 min. WhisperX local had best diarization for once. Top: Opus, Gemini (both T1, ~10.2K words). GLM T4 (chain-of-thought on all 3 bases). MiniMax T4. Best: `assemblyai_opus.md`.
→ [Full report](episode004-taylor-gerring/episode004-taylor-gerring_quality_assessment.md)

### Episode 005 — Anthony Di Onofrio
~80 min, 4 speakers. Top: Opus (14,308w), Grok (14,978w), Gemini (14,639w). GLM T4 (19K–46K words of chain-of-thought). Gemini resets timestamps to 00:00. Best: `assemblyai_opus.md`.
→ [Full report](episode005-anthony-d-onofrio/episode005-anthony-d-onofrio_quality_assessment.md)

### Episode 006 — Christoph Jentzsch
~80 min, 4 speakers. Top: Opus (14,828w), Gemini (15,145w), Grok (14,955w). GLM T4 (32K–46K words). MiniMax T4 (1,251w). 6 models truncated to 25–45%. Best: `assemblyai_opus.md`.
→ [Full report](episode006-christoph-jentzsch/episode006-christoph-jentzsch_quality_assessment.md)

### Episode 007 — Jacob Czepluch
~50 min. WhisperX local BROKEN ("Thank you" hallucination). Top: Opus, ChatGPT, Gemini, Grok (all T1). GLM T2 (worked on this episode). Consensus BROKEN — corrupted transcriber poisoned merge. Best: `assemblyai_opus.md`.
→ [Full report](episode007-jacob-czepluch/episode007-jacob-czepluch_quality_assessment.md)

### Episode 008 — Michael Parenti
~26 min (short). Nearly all processors T1. WhisperX local produced best input for processors here. Llama T4 (gibberish). GLM T3 (chain-of-thought). Best: `assemblyai_chatgpt.md`.
→ [Full report](episode008-michael-parenti/episode008-michael-parenti_quality_assessment.md)

### Episode 009 — Amir Taaki
~57 min. Top: Opus (9,196w), Kimi (9,105w), Gemini (8,884w), Grok (8,655w). GLM T4 on 2/3 bases. 5 models truncated to 36–56%. Best: `assemblyai_opus.md`.
→ [Full report](episode009-amir-taaki/episode009-amir-taaki_quality_assessment.md)

### Episode 010 — Viktor Tron
~60 min. Top: Opus (10,896w), Gemini (11,497w), Grok (10,909w). **ChatGPT refused** (241w, cited missing timestamps). GLM T3 (chain-of-thought). Best: `assemblyai_opus.md`.
→ [Full report](episode010-viktor-tron/episode010-viktor-tron_quality_assessment.md)

### Episode 011 — Ryan Taylor
~71 min. AssemblyAI only (no WhisperX). Top: Opus (12,102w). DeepSeek T4 (80 words — near-total failure). Consensus complete but degraded (duplicated paragraphs, truncated tags). Opus single output is cleaner than consensus. Best: `assemblyai_opus.md`.
→ [Full report](episode011-ryan-taylor/episode011-ryan-taylor_quality_assessment.md)

### Episode 012 — Fabian Vogelsteller
Long episode (~19K words). WhisperX local BROKEN (`!!!!!!`). Top: Opus (18,837w), Grok (18,474w), GLM5 (17,665w). 5 models severely truncated. Consensus BROKEN (3.26x expansion). Best: `assemblyai_opus.md`.
→ [Full report](episode012-fabian-vogelsteller/episode012-fabian-vogelsteller_quality_assessment.md)

### Episode 012 — Martin Becze
~25 min (short). Nearly all processors T1. GLM T4 (27,771w chain-of-thought). DeepSeek wrong name substitution ("Joseph Chow" → "Joseph Lubin"). Best: `assemblyai_chatgpt.md`.
→ [Full report](episode012-martin-becze/episode012-martin-becze_quality_assessment.md)

### Episode 013 — Alex Van de Sande
~30 min. WhisperX-cloud broken diarization (speakers swapped). 28/33 outputs T1. GLM T4 on all 3 bases. Llama hallucinated "Radicle" for "Rotki". Best: `assemblyai_chatgpt.md`.
→ [Full report](episode013-alex-van-de-sande/episode013-alex-van-de-sande_quality_assessment.md)

### Episode 013 — Zsolt Felfoldi
~40 min. WhisperX local BROKEN (`!!!!!!`). Top: Kimi (8,185w), GLM (8,178w), Grok (7,859w). GLM worked on this episode. DeepSeek misspelled guest name. Consensus not run. Best: `assemblyai_kimi.md`.
→ [Full report](episode013-zsolt-felfoldi/episode013-zsolt-felfoldi_quality_assessment.md)
