# Overall Quality Report

*Generated: 2026-02-23*
*Episodes assessed: 15*
*Processors: opus, gemini, grok*
*Transcribers: AssemblyAI, WhisperX (local), WhisperX-cloud*

## Summary

Across 15 episodes of the Early Days of Ethereum podcast, a total of 121 processor outputs were assessed (15 episodes x 3 transcribers x 3 processors, minus unavailable combinations). Of these, 99 achieved Tier 1 (complete, >90% of max word count), 13 achieved Tier 2 (mostly complete but condensed or poorly formatted), and 9 were Tier 4 (unusable due to corrupted WhisperX local transcriber bases in episodes 007, 012-Fabian, and 013-Zsolt). No Tier 3 outputs were produced. The overall Tier 1 rate for usable outputs is 88%.

**AssemblyAI** is the clear winner among transcriber bases, producing the best diarization, highest word counts, and cleanest formatting across all 15 episodes. It never suffered corruption. WhisperX (local) is a solid secondary option when it works but suffered catastrophic corruption in 3 of 14 episodes (21% failure rate). WhisperX-cloud consistently produced the worst diarization, with severely merged speaker blocks that only Opus could reliably decompose.

Among AI processors, **Opus** delivers the most consistent quality across all transcriber bases, with a unique ability to reconstruct speaker turns from poorly diarized input. It achieves Tier 1 in 97% of usable outputs and is the recommended primary processor for 13 of 15 episodes. **Grok** is the most faithful/verbatim processor with the highest word counts and a perfect Tier 1 record on the AssemblyAI base, but introduces factual name substitution errors and fails to decompose merged speaker blocks. **Gemini** excels at proper noun identification and name enrichment but suffers from aggressive condensation on longer episodes (dropping to 31-59% retention) and occasionally strips timestamps.

---

## 1. Transcriber Reliability

| Transcriber | Episodes Available | Fully Usable | Corrupted/Broken | Best Diarization Count | Avg Quality Grade |
|---|---|---|---|---|---|
| **AssemblyAI** | 15/15 | **15** (100%) | 0 | **15/15** | A |
| **WhisperX (local)** | 14/15 | **11** (79%) | 3 (ep007, ep012-Fabian, ep013-Zsolt) | 0/15 | B- |
| **WhisperX-cloud** | 14/15 | **14** (100%) | 0 | 0/15 | C+ |

**Notes:**
- Episode 011 (Ryan Taylor) only had AssemblyAI transcription; no WhisperX outputs existed.
- WhisperX local corruption manifested as hallucinated "Thank you" loops (ep007: 93 words) or exclamation mark strings (ep012-Fabian: 405 words, ep013-Zsolt: 254 words).
- WhisperX-cloud was never corrupted but consistently produced the worst diarization with merged multi-speaker blocks, sometimes collapsing 5+ minutes of dialogue into a single paragraph.

### Diarization Quality Summary

| Transcriber | Avg Speakers Detected | Speaker Accuracy | Turn Granularity | Typical Issues |
|---|---|---|---|---|
| **AssemblyAI** | 2-4 (correct) | Excellent | Fine-grained (100-350+ turns) | Minor phonetic ASR errors on proper nouns |
| **WhisperX (local)** | 3-5 (sometimes extra) | Good | Moderate (60-200 turns) | Occasionally merges short interjections; sometimes inverts speaker labels |
| **WhisperX-cloud** | 3-7 (often wrong count) | Poor | Coarse (25-94 turns) | Massive multi-speaker blocks; speakers frequently merged; wall-of-text paragraphs |

### Transcriber Verdict

**AssemblyAI is the unambiguous primary transcriber.** It produced the best diarization in all 15 episodes, never suffered corruption, and consistently yielded the highest word counts. WhisperX (local) is a useful secondary source when it functions but its 21% corruption rate is a significant reliability concern. WhisperX-cloud should only be used as a tertiary source; its poor diarization degrades downstream processor output quality, particularly for Gemini and Grok which cannot decompose merged speaker blocks.

---

## 2. Processor Leaderboard (AssemblyAI base)

Data compiled from all 15 episodes where AssemblyAI-based processor outputs exist. Episode 011 only has an Opus output.

| Processor | Tier 1 | Tier 2 | Tier 3 | Tier 4 | T1 Rate | Consistency |
|---|---|---|---|---|---|---|
| **Grok** | **14** | 0 | 0 | 0 | **100%** | Excellent |
| **Opus** | 14 | 1 | 0 | 0 | **93%** | Excellent |
| **Gemini** | 11 | 3 | 0 | 0 | **79%** | Good |

### Per-Episode Breakdown (AssemblyAI base)

| Episode | Opus Words | Opus Tier | Gemini Words | Gemini Tier | Grok Words | Grok Tier |
|---|---|---|---|---|---|---|
| 001 | 18,802 | T1 | 16,009 | T2 | 17,855 | T1 |
| 002 | 11,814 | T1 | 11,248 | T1 | 11,016 | T1 |
| 003 (Bob) | 11,554 | T1 | 11,777 | T1 | 11,805 | T1 |
| 004 (Taylor) | 10,256 | T1 | 10,261 | T1 | 10,082 | T1 |
| 005 (Anthony) | 14,308 | T1 | 14,639 | T1 | 14,978 | T1 |
| 006 (Christoph) | 14,828 | T1 | 15,145 | T1 | 14,955 | T1 |
| 007 (Jacob) | 2,868 | T1 | 2,747 | T1 | 2,830 | T1 |
| 008 (Michael) | 4,273 | T1 | 4,425 | T1 | 4,251 | T1 |
| 009 (Amir) | 9,196 | T1 | 8,884 | T1 | 8,655 | T1 |
| 010 (Viktor) | 10,896 | T1 | 11,497 | T1 | 10,909 | T1 |
| 011 (Ryan) | 12,102 | T1 | -- | -- | -- | -- |
| 012 (Fabian) | 18,837 | T1 | 11,175 | T2 | 18,474 | T1 |
| 012 (Martin) | 3,850 | T1 | 4,093 | T1 | 4,074 | T1 |
| 013 (Alex) | 4,603 | T1 | 4,633 | T1 | 4,593 | T1 |
| 013 (Zsolt) | 6,665 | T2 | 6,597 | T2 | 7,859 | T1 |

### Analysis

**Grok** achieves a perfect Tier 1 record across all 14 assessed episodes on the AssemblyAI base, making it the most reliable by tier count. It consistently produces the highest or near-highest word counts, reflecting its faithful/verbatim processing style. However, Grok introduces factual name substitution errors in several episodes: "Piper Merriam" instead of Gustav Simonsson (ep007), "Michael Perklin" instead of Michael Parenti (ep008), "Mike Hearn" instead of Mike Gogulski (ep008), and "Joseph Lubin" instead of Joseph Chow (ep012-Martin). These errors, while not affecting tier classification, are significant factual inaccuracies.

**Opus** achieves Tier 1 in 14 of 15 episodes on the AssemblyAI base. Its single Tier 2 (episode 013-Zsolt) is due to truncation at ~50 minutes of a 60-minute interview, missing the final 9 minutes. Opus consistently produces the cleanest formatting with proper speaker separation, the most accurate proper noun corrections (including Hungarian diacritics), and the best balance of editorial polish and content fidelity. Opus is the recommended "best output" in 13 of 15 episodes.

**Gemini** achieves Tier 1 in 11 of 14 assessed episodes. Its three Tier 2 results stem from aggressive condensation: episode 001 (85% of max), episode 012-Fabian (59% of max -- the most severe), and episode 013-Zsolt (81% of max). Gemini's condensation tendency worsens with episode length, making it unsuitable as a primary processor for oral history transcripts where verbatim preservation matters. However, Gemini excels at proper noun identification, adding full surnames from contextual knowledge (e.g., "Jeffrey Wilcke," "Lefteris Karapetsas," "Gustav Simonsson") and using code formatting for technical terms.

---

## 3. Processor Leaderboard (WhisperX-cloud base)

Data compiled from 14 episodes where WhisperX-cloud-based processor outputs exist (ep011 had no WhisperX-cloud).

| Processor | Tier 1 | Tier 2 | Tier 3 | Tier 4 | T1 Rate | Consistency |
|---|---|---|---|---|---|---|
| **Opus** | **14** | 0 | 0 | 0 | **100%** | Excellent |
| **Gemini** | 9 | 4 | 0 | 0 | **69%** | Good |
| **Grok** | 8 | 5 | 0 | 0 | **62%** | Fair |

### Per-Episode Breakdown (WhisperX-cloud base)

| Episode | Opus Words | Opus Tier | Gemini Words | Gemini Tier | Grok Words | Grok Tier |
|---|---|---|---|---|---|---|
| 001 | 18,470 | T1 | 18,306 | T1 | 18,209 | T1 |
| 002 | 11,313 | T1 | 11,330 | T1 | 11,419 | T1 |
| 003 (Bob) | 11,583 | T1 | 12,106 | T1 | 11,988 | T1 |
| 004 (Taylor) | 9,909 | T1 | 10,283 | T1 | 10,196 | T2 |
| 005 (Anthony) | 13,349 | T1 | 13,898 | T1 | 14,157 | T1 |
| 006 (Christoph) | 14,772 | T1 | 14,927 | T1 | 14,782 | T1 |
| 007 (Jacob) | 2,729 | T1 | 2,704 | T1 | 2,732 | T2 |
| 008 (Michael) | 4,276 | T1 | 4,084 | T2 | 3,932 | T2 |
| 009 (Amir) | 8,549 | T1 | 8,280 | T1 | 8,374 | T1 |
| 010 (Viktor) | 11,284 | T1 | 11,135 | T1 | 11,420 | T2 |
| 012 (Fabian) | 18,116 | T1 | 5,837 | T2 | 18,232 | T1 |
| 012 (Martin) | 3,862 | T1 | 3,783 | T1 | 3,609 | T2 |
| 013 (Alex) | 4,551 | T1 | 4,521 | T1 | 4,450 | T1 |
| 013 (Zsolt) | 7,919 | T1 | 7,320 | T2 | 8,600 | T1 |

### Analysis

**Opus** achieves a perfect Tier 1 record across all 14 WhisperX-cloud episodes. Its standout capability is **speaker re-separation**: when given coarsely diarized input with merged multi-speaker blocks, Opus consistently reconstructs fine-grained speaker turns. In episode 006, Opus expanded 79 input turn boundaries to 340 output lines (4.3x increase). In episode 008, it expanded 52-line input to 280 lines. This capability makes Opus uniquely resilient to poor transcriber quality.

**Gemini** drops to Tier 2 in 4 episodes on the WhisperX-cloud base. In episode 012-Fabian, it condensed an 18,000-word conversation to just 5,837 words (31% of max) -- its most aggressive condensation. Gemini also fails to decompose merged speaker blocks, inheriting wall-of-text formatting from the source.

**Grok** drops to Tier 2 in 5 episodes on the WhisperX-cloud base. The primary cause is its failure to decompose merged speaker blocks: it typically preserves the coarse paragraph structure of the source, producing outputs with very few lines (e.g., 52 lines for a 25-minute conversation, 92 lines for a 70-minute conversation, 122 lines for a 69-minute conversation). Content is present but readability is severely compromised.

---

## 4. Cross-Transcriber Comparison

Comparing the same processor across different transcriber bases reveals how each processor handles varying input quality.

### Speaker Re-separation Capability

This is the most important processor differentiator when working with WhisperX-cloud input.

| Processor | Re-separation Rating | Typical Behavior | Example |
|---|---|---|---|
| **Opus** | **Excellent** | Actively decomposes merged blocks into individual speaker turns; output line count often 3-5x the input line count | ep006: 79 input lines -> 340 output lines; ep008: 52 -> 280 |
| **Gemini** | **Moderate** | Partially decomposes some blocks; output somewhat more granular than input but retains many merged passages | ep006: 79 input lines -> 196 output lines |
| **Grok** | **Poor** | Typically preserves the input structure verbatim; output line count matches or nearly matches input line count | ep006: 79 input lines -> 158 output lines; ep008: 52 -> 50 |

### Quality Retention Across Bases

| Metric | Opus | Gemini | Grok |
|---|---|---|---|
| AssemblyAI base -> Tier 1 rate | 93% (14/15) | 79% (11/14) | 100% (14/14) |
| WhisperX-cloud base -> Tier 1 rate | **100%** (14/14) | 69% (9/13) | 62% (8/13) |
| WhisperX local base -> Tier 1 rate | 100% (10/10)* | 100% (10/10)* | 100% (10/10)* |
| Quality drop on poor input | Minimal | Moderate-to-severe | Severe (formatting) |
| Primary failure mode | Rare truncation | Over-condensation | Wall-of-text inheritance |

*Excluding 3 episodes with corrupted WhisperX local, plus ep011 with no WhisperX. WhisperX local achieves universal Tier 1 when the transcriber produces valid output.

### Word Count Consistency Across Bases

| Processor | Avg Spread (AssemblyAI vs WhisperX-cloud) | Most Consistent Episode | Least Consistent Episode |
|---|---|---|---|
| **Opus** | ~3.5% | ep006 (1.3%) | ep013-Zsolt (19% due to truncation) |
| **Gemini** | ~8.2% | ep002 (0.7%) | ep012-Fabian (52% due to severe condensation) |
| **Grok** | ~3.0% | ep006 (1.2%) | ep012-Martin (11%) |

---

## 5. Processor Tier Distribution

Tier counts across all episodes and transcriber bases combined. Only opus, gemini, and grok are included.

### Full Tier Matrix

| Processor + Base | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total Assessed |
|---|---|---|---|---|---|
| **opus + assemblyai** | 14 | 1 | 0 | 0 | 15 |
| **opus + whisperx** | 10 | 0 | 0 | 3 | 13 |
| **opus + whisperx-cloud** | 14 | 0 | 0 | 0 | 14 |
| **gemini + assemblyai** | 11 | 3 | 0 | 0 | 14 |
| **gemini + whisperx** | 10 | 0 | 0 | 3 | 13 |
| **gemini + whisperx-cloud** | 9 | 4 | 0 | 0 | 13 |
| **grok + assemblyai** | 14 | 0 | 0 | 0 | 14 |
| **grok + whisperx** | 10 | 0 | 0 | 3 | 13 |
| **grok + whisperx-cloud** | 8 | 5 | 0 | 0 | 13 |
| **TOTAL** | **100** | **13** | **0** | **9** | **122** |

*Note: All 9 Tier 4 outputs are exclusively from corrupted WhisperX local bases (ep007, ep012-Fabian, ep013-Zsolt). All three processors correctly identified the corrupted input and produced minimal or empty output -- a correct behavior.*

### Processor Tier Summary (excluding Tier 4 corrupted inputs)

| Processor | Tier 1 | Tier 2 | Total Usable | Tier 1 Rate |
|---|---|---|---|---|
| **Opus** | **38** | 1 | 39 | **97.4%** |
| **Grok** | **32** | 5 | 37 | **86.5%** |
| **Gemini** | **30** | 7 | 37 | **81.1%** |

### Visual Tier Distribution (AssemblyAI base, 14-15 episodes per processor)

| Processor | T1 Rate | Visual |
|---|---|---|
| **Grok** | 100% | `██████████████` (14/14 T1) |
| **Opus** | 93% | `██████████████░` (14/15 T1, 1 T2) |
| **Gemini** | 79% | `███████████░░░` (11/14 T1, 3 T2) |

### Visual Tier Distribution (WhisperX-cloud base, 13-14 episodes per processor)

| Processor | T1 Rate | Visual |
|---|---|---|
| **Opus** | 100% | `██████████████` (14/14 T1) |
| **Gemini** | 69% | `█████████░░░░` (9/13 T1, 4 T2) |
| **Grok** | 62% | `████████░░░░░` (8/13 T1, 5 T2) |

Legend: `█` = Tier 1, `░` = Tier 2

---

## 6. Best Combinations

Ranked by consistency, quality, and suitability for oral history transcripts.

### Rank 1: AssemblyAI + Opus

**Recommended as primary in: 13/15 episodes**

| Metric | Value |
|---|---|
| Tier 1 rate (AssemblyAI base) | 93% (14/15) |
| Avg completeness | 96.8% |
| Formatting quality | Excellent -- proper paragraph structure, timestamps, speaker headers on own lines |
| Name correction quality | Excellent -- most thorough and accurate, includes diacritics (e.g., "Zsolt Felfoldi") |
| Speaker re-separation | Excellent -- can reconstruct turns from poor input |
| Unique strength | Best balance of editorial polish and content fidelity |
| Known weakness | Rare truncation (ep013-Zsolt lost final 9 min); occasionally retains uncorrected names (e.g., "Bob Samuel") |

### Rank 2: AssemblyAI + Grok

**Recommended as primary in: 2/15 episodes (ep013-Zsolt for completeness, ep011 by pipeline score)**

| Metric | Value |
|---|---|
| Tier 1 rate (AssemblyAI base) | 100% (14/14) |
| Avg completeness | 97.1% |
| Formatting quality | Good -- clean but denser paragraphs, fewer line breaks |
| Name correction quality | Good but with factual substitution errors in ~4 episodes |
| Unique strength | Highest word counts; most faithful/verbatim rendering; never truncates |
| Known weakness | Introduces wrong-person name substitutions; inconsistent capitalization |

### Rank 3: AssemblyAI + Gemini

**Recommended as secondary/reference in all episodes**

| Metric | Value |
|---|---|
| Tier 1 rate (AssemblyAI base) | 79% (11/14) |
| Avg completeness | 95.4% (but drops to 59% on long episodes) |
| Formatting quality | Good -- clean, sometimes uses code formatting and contextual annotations |
| Name correction quality | Best -- adds full surnames, identifies obscure proper nouns (Gustav Simonsson, AlethZero, Codius) |
| Unique strength | Superior proper noun identification; scholarly formatting; best for name verification |
| Known weakness | Over-condenses long episodes (40-70% content removal on ep012-Fabian); sometimes strips timestamps |

### Rank 4: WhisperX-cloud + Opus

**Recommended as fallback when AssemblyAI is unavailable**

| Metric | Value |
|---|---|
| Tier 1 rate | 100% (14/14) |
| Unique strength | Opus successfully re-separates merged speaker blocks |
| Known weakness | Some residual diarization confusion from poor source |

### Rank 5: WhisperX (local) + Opus

**Recommended as secondary cross-reference when WhisperX local is not corrupted**

| Metric | Value |
|---|---|
| Tier 1 rate | 100% (10/10 non-corrupted episodes) |
| Unique strength | Sometimes detects more speakers than AssemblyAI (ep004: 5 vs 4); occasionally better on specific proper nouns (ep013-Alex: corrected "Lefteris" and "Rotki" where AssemblyAI+Opus missed them) |
| Known weakness | 21% corruption rate makes it unreliable |

---

## 7. Processors to Avoid

### WhisperX-cloud + Grok -- Avoid as primary

**Reason:** Grok does not decompose merged speaker blocks from WhisperX-cloud. Outputs inherit wall-of-text formatting with very few line breaks (sometimes <100 lines for a 60+ minute conversation). Content is technically present but readability is severely compromised. Tier 2 in 5 of 13 episodes.

**Affected episodes:** ep004 (92 lines), ep007 (36 lines), ep008 (50 lines), ep010 (122 lines), ep012-Martin (52 lines)

### WhisperX-cloud + Gemini -- Use with caution

**Reason:** Gemini's condensation tendency is amplified on the WhisperX-cloud base. In episode 012-Fabian, it produced only 5,837 words from an 18,000-word conversation (31% retention). It also fails to fully decompose merged speaker blocks, though to a lesser degree than Grok. Tier 2 in 4 of 13 episodes.

**Affected episodes:** ep008, ep012-Fabian, ep013-Zsolt, and partially ep010

### Grok on any base -- Verify proper names

**Reason:** Grok introduces factual name substitution errors where it replaces an unclear name with a plausible but incorrect person from the same domain. These errors are particularly dangerous because they appear authoritative:

| Episode | Grok Substitution | Correct Name |
|---|---|---|
| 007 (Jacob) | "Piper Merriam" | Gustav Simonsson |
| 008 (Michael) | "Michael Perklin" | Michael Parenti |
| 008 (Michael) | "Mike Hearn" | Mike Gogulski |
| 008 (Michael) | "Michael Goldstein" | Mike Gogulski |
| 012 (Martin) | "Joseph Lubin" | Joseph Chow |
| 012 (Fabian) | "Yann LeCun" | Yann Levreau |

### Gemini on long episodes (>60 min) -- Verify completeness

**Reason:** Gemini's condensation scales with episode length. On shorter episodes, condensation is minimal. On longer episodes, condensation becomes severe.

| Episode Duration Range | Gemini Avg Completeness | Examples |
|---|---|---|
| <30 min | ~97% | ep007 (94%), ep008 (100%), ep012-Martin (100%), ep013-Alex (100%) |
| 30-60 min | ~93% | ep009 (97%), ep010 (100%), ep013-Zsolt (81%) |
| 60-90 min | ~90% | ep003 (100%), ep004 (100%), ep005 (98%), ep011 (not assessed) |
| >90 min | ~72% | ep001 (85%), ep012-Fabian (59%) |

---

## 8. Recommendations

### Primary Pipeline

1. **Use AssemblyAI as the primary transcriber for all episodes.** It has a 100% reliability rate, the best diarization, and the highest word counts. There is no scenario where another transcriber outperforms AssemblyAI across all metrics.

2. **Use Opus as the primary AI processor.** It achieves Tier 1 in 97.4% of usable outputs, has the best formatting quality, the most accurate name corrections, and uniquely can reconstruct speaker turns from poorly diarized input. Its only weakness (rare truncation on one episode) is easily caught by comparing word counts.

3. **Use Grok as the secondary/completeness-check processor.** It produces the highest word counts and never truncates on the AssemblyAI base, making it a useful completeness check against Opus. Always verify proper names against the Opus output, as Grok introduces factual name substitution errors.

4. **Use Gemini as a reference for proper noun verification.** Gemini's ability to add full surnames and contextual annotations makes it invaluable for name verification, even if its condensation makes it unsuitable as a primary transcript source for long episodes.

### Transcriber Strategy

5. **Retain AssemblyAI as the sole production transcriber.** Its 100% reliability and best-in-class diarization make it the only transcriber needed for production workflows.

6. **Discontinue WhisperX (local) for production use** unless the corruption issue (hallucinated "Thank you" loops, exclamation mark strings) is resolved. A 21% failure rate is unacceptable. If local WhisperX must be used, implement a corruption check before processing.

7. **Retain WhisperX-cloud as an optional tertiary source** for cross-reference only. Its poor diarization means it should never be the primary source, but its content capture is complete and Opus can recover reasonable structure from it.

### Quality Assurance

8. **Implement word count comparison** between Opus and Grok outputs. If Grok's word count exceeds Opus by more than 15%, check for Opus truncation. If Opus's word count exceeds Gemini by more than 25%, check for Gemini over-condensation.

9. **Implement a proper noun verification step** using Gemini's output as a reference for full names and correct spellings, while using Opus's output as the base transcript.

10. **Flag Grok name substitutions** by comparing Grok's proper nouns against Opus and Gemini. Any name present in Grok but absent from both other processors should be manually verified against the audio.

11. **For episodes over 60 minutes**, always check that Opus reached the final timestamp. If truncated, supplement the missing section from the Grok output.

---

## Appendix: Per-Episode Summaries

### Episode 001 (Kieren James-Lubin, Jim Hermosdia, Victor Wong)
~116 min | 9 outputs assessed | All Tier 1 except assemblyai_gemini (Tier 2, 85% condensation). **Best: assemblyai_opus** (18,802 words). AssemblyAI provided the best 3-speaker diarization. Opus delivered the most complete and best-formatted output. Gemini over-condensed the AssemblyAI base but performed well on WhisperX bases. All transcribers corruption-free.
[Full report](episode001/episode001_quality_assessment.md)

### Episode 002 (BlockApps Co-founders)
~60 min | 9 outputs assessed | **All 9 outputs Tier 1** -- the cleanest episode across the entire series. **Best: assemblyai_opus** (11,814 words). Word counts tightly clustered (7% range). Both WhisperX variants had hallucinated speaker name artifacts ("Justin Delacruz, Ph.D.") but content was complete. Formatting quality was the main differentiator.
[Full report](episode002/episode002_quality_assessment.md)

### Episode 003 (Bob Summerwill)
~79 min | 9 outputs assessed | **All 9 outputs Tier 1.** **Best: assemblyai_opus** (11,554 words). Bob speaks clearly at a measured pace, resulting in excellent ASR quality across all transcribers. WhisperX-cloud had the worst diarization (Bob's speech frequently misattributed). All processors handled name corrections well.
[Full report](episode003-bob-summerwill/episode003-bob-summerwill_quality_assessment.md)

### Episode 004 (Taylor Gerring)
~71 min | 9 outputs assessed | 8 Tier 1, 1 Tier 2 (whisperx-cloud_grok -- wall-of-text, 92 lines). **Best: assemblyai_opus** (10,256 words). WhisperX local uniquely detected 5 speakers (vs 4 for AssemblyAI). Grok failed to decompose WhisperX-cloud's merged blocks. All transcribers struggled with "Meierskappel."
[Full report](episode004-taylor-gerring/episode004-taylor-gerring_quality_assessment.md)

### Episode 005 (Anthony D'Onofrio)
~73 min | 9 outputs assessed | **All 9 outputs Tier 1.** **Best: assemblyai_opus** (14,308 words). WhisperX-cloud had severely collapsed diarization (700+ word multi-speaker blocks). Gemini stripped timestamps from the WhisperX output. Grok preserved more raw errors ("metallic" for Vitalik). Content-rich episode with many proper nouns.
[Full report](episode005-anthony-d-onofrio/episode005-anthony-d-onofrio_quality_assessment.md)

### Episode 006 (Christoph Jentzsch)
~87 min | 9 outputs assessed | **All 9 outputs Tier 1.** **Best: assemblyai_opus** (14,828 words). Showcase episode for Opus's speaker re-separation capability (79 WhisperX-cloud input lines -> 340 output lines, a 4.3x increase). Grok had the tightest word count spread (1.2%) across bases. All processors handled the technically dense DAO/Slock.it content well.
[Full report](episode006-christoph-jentzsch/episode006-christoph-jentzsch_quality_assessment.md)

### Episode 007 (Jacob Czepluch)
~16 min | 6 usable outputs (3 Tier 4 from corrupted WhisperX local). **Best: assemblyai_gemini** (2,747 words) -- the only episode where Gemini is recommended over Opus, due to superior proper noun accuracy (Gustav Simonsson, AlethZero, ETHPrague). Grok introduced "Piper Merriam" factual error. WhisperX local completely corrupted ("Thank you" hallucinations).
[Full report](episode007-jacob-czepluch/episode007-jacob-czepluch_quality_assessment.md)

### Episode 008 (Michael Parenti)
~26 min | 9 outputs assessed | 6 Tier 1, 2 Tier 2 (whisperx-cloud gemini/grok poor formatting). **Best: assemblyai_opus** (4,273 words). Opus was the only processor to achieve Tier 1 across all three bases due to its speaker re-diarization capability. Gemini misidentified the guest as "Michael Polzl"; Grok as "Michael Perklin." Multiple name errors across processors.
[Full report](episode008-michael-parenti/episode008-michael-parenti_quality_assessment.md)

### Episode 009 (Amir Taaki)
~57 min | 9 outputs assessed | **All 9 outputs Tier 1** (though WhisperX-cloud gemini/grok had wall-of-text formatting with only 72 lines each). **Best: assemblyai_opus** (9,196 words, 800 lines). Opus excelled at recovering structure from WhisperX-cloud (332 lines vs 72 for Gemini/Grok). Critical test word "ahistorical" correctly rendered by Grok.
[Full report](episode009-amir-taaki/episode009-amir-taaki_quality_assessment.md)

### Episode 010 (Viktor Tron)
~69 min | 9 outputs assessed | 8 Tier 1, 1 Tier 2 (whisperx-cloud_grok -- 122 lines, wall-of-text). **Best: assemblyai_opus** (10,896 words). Gemini and Grok dropped timestamps on multiple outputs. Gemini's whisperx output had the best name annotations with bracketed clarifications. Opus was the only processor with timestamps on the AssemblyAI base.
[Full report](episode010-viktor-tron/episode010-viktor-tron_quality_assessment.md)

### Episode 011 (Ryan Taylor)
~71 min | **Only 1 output assessed** (assemblyai_opus, 12,102 words, Tier 1). No WhisperX transcriptions exist. No Gemini or Grok output files were generated despite pipeline quality scores existing. The single Opus output is publication-ready with excellent formatting and proper noun handling.
[Full report](episode011-ryan-taylor/episode011-ryan-taylor_quality_assessment.md)

### Episode 012 (Fabian Vogelsteller)
~116 min | 6 usable outputs (3 Tier 4 from corrupted WhisperX local). **Best: assemblyai_opus** (18,837 words). Gemini's most severe condensation: assemblyai_gemini reduced to 11,175 words (59%); whisperx-cloud_gemini to 5,837 words (31%). Grok introduced "Yann LeCun" error. WhisperX local corrupted (exclamation marks). All Opus and Grok outputs are Tier 1.
[Full report](episode012-fabian-vogelsteller/episode012-fabian-vogelsteller_quality_assessment.md)

### Episode 012 (Martin Becze)
~26 min | 9 outputs assessed | 8 Tier 1, 1 Tier 2 (whisperx-cloud_grok -- 52 lines, merged paragraphs). **Best: assemblyai_opus** (3,850 words). Grok (WhisperX base) systematically replaced "Joseph Chow" with "Joseph Lubin" -- a significant factual error. Opus had the tightest word count spread across bases (3%, 129 words). Gemini correctly identified "Codius."
[Full report](episode012-martin-becze/episode012-martin-becze_quality_assessment.md)

### Episode 013 (Alex Van de Sande)
~30 min | 9 outputs assessed | **All 9 outputs Tier 1.** **Best: whisperx_gemini or whisperx_opus** -- the only episode where WhisperX-based outputs outperformed AssemblyAI-based ones, because WhisperX processors correctly identified "Lefteris," "Rotki," and "Infura" where AssemblyAI+Opus missed these corrections. Short episode (30 min) helped all processors achieve full coverage.
[Full report](episode013-alex-van-de-sande/episode013-alex-van-de-sande_quality_assessment.md)

### Episode 013 (Zsolt Felfoldi)
~60 min | 6 usable outputs (3 Tier 4 from corrupted WhisperX local). 4 Tier 1, 2 Tier 2. Unusual episode: **whisperx-cloud_grok** had the highest word count (8,600) and **assemblyai_grok** (7,859 words) is the recommended AssemblyAI-base output. Opus (assemblyai) truncated at 50 minutes, missing the final 9 minutes on multi-client philosophy, EF growth, and Raiden. Best balance: whisperx-cloud_opus (7,919 words).
[Full report](episode013-zsolt-felfoldi/episode013-zsolt-felfoldi_quality_assessment.md)
