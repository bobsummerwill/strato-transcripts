# Museum of Ethereum — Quality Assessment Report

## 1. Episode Overview

This is a short live walkthrough of the ETHDenver museum installation, with Bob Summerwill leading the tour and a second Strato speaker asking follow-up questions throughout. The content is technically dense and name-heavy, with a lot of Ethereum historical references, person names, and product names such as Mist, Geth, ETC, EthSuisse, and ETHDenver.

Available files discovered for this episode:

| File | Type |
|------|------|
| `intermediates/museum-of-ethereum/museum-of-ethereum_assemblyai.md` | Raw transcript |
| `intermediates/museum-of-ethereum/museum-of-ethereum_whisperx-cloud.md` | Raw transcript |
| `outputs/museum-of-ethereum/museum-of-ethereum_assemblyai_opus.md` | Processed transcript |
| `outputs/museum-of-ethereum/museum-of-ethereum_assemblyai_gpt.md` | Processed transcript |
| `outputs/museum-of-ethereum/museum-of-ethereum_whisperx-cloud_opus.md` | Processed transcript |
| `outputs/museum-of-ethereum/museum-of-ethereum_whisperx-cloud_gpt.md` | Processed transcript |

No JSON artifacts were present for this episode.

---

## 2. Transcriber Comparison

| Transcriber | Word Count | Timestamps | Status | Diarization | Notes |
|-------------|-----------:|-----------:|--------|-------------|-------|
| **AssemblyAI** | 3,263 | 45 | Usable | 2 speakers | Cleaner speaker structure and more stable prose; deterministic normalization now fixes the raw intro name drift to `Bob Summerwill` and `Kieren James-Lubin` |
| **WhisperX-cloud** | 3,539 | 46 | Usable | 3 speakers + 1 unknown | Slightly fuller coverage to the end of the recording; deterministic normalization now fixes the raw intro drift to `Bob Summerwill` and `Kieren James-Lubin`, though other noise like `FDamber` remains |

**Transcriber verdict:** Both transcribers are usable. AssemblyAI is the cleaner base transcript. WhisperX-cloud is the more complete base transcript, but it introduces more recognition noise and more speaker fragmentation.

### AssemblyAI raw quality

- Strong overall readability and stable sentence flow.
- Good 2-speaker diarization for almost the entire file.
- The previous early intro-name errors are now corrected during transcript normalization:
  - `Bob Samuel` -> `Bob Summerwill`
  - `James Bond` -> `Kieren James-Lubin`
- Technical terms are mostly recoverable from context, but some phrases are rough in the middle of the tour.

### WhisperX-cloud raw quality

- Slightly longer and reaches `[22:01]`, whereas AssemblyAI ends at `[21:31]`.
- The previous intro-name drift is now corrected during normalization:
  - `Bob Samuil` -> `Bob Summerwill`
  - `James Logan` -> `Kieren James-Lubin`
- Other entity drift remains, notably `FDamber`.
- More speaker fragmentation, including `SPEAKER_UNKNOWN`.
- Still usable as a processor base because much of the technical content is present.

---

## 3. AI Processor Comparison

Longest processed output: **`museum-of-ethereum_whisperx-cloud_opus.md`** at **3,196 words**.

| Output | Word Count | Completeness | Tier | Notes |
|--------|-----------:|-------------:|------|-------|
| **assemblyai_opus** | 3,095 | 96.8% | **Tier 1** | Best editorial cleanup on the cleaner base transcript |
| **assemblyai_gpt** | 3,029 | 94.8% | **Tier 1** | Good cleanup, slightly more condensed than Opus |
| **whisperx-cloud_opus** | 3,196 | 100.0% | **Tier 1** | Most complete processed output |
| **whisperx-cloud_gpt** | 3,125 | 97.8% | **Tier 1** | Strong completeness, cleaner than raw WhisperX-cloud |

### assemblyai_opus

- Best overall editorial balance.
- Corrects `Bob Summerwill`.
- Preserves timestamps and speaker structure cleanly.
- Intro speaker name is now corrected to `Kieren James-Lubin`.
- Retains a few `Kieren` mentions without upgrading them to the full canonical name.

### assemblyai_gpt

- Similar overall quality to Opus, with slightly more condensation.
- Corrects `Bob Summerwill`.
- Intro speaker name is now corrected to `Kieren James-Lubin`.
- Keeps good readability and structure, but does not fully solve the canonical-name cleanup.

### whisperx-cloud_opus

- Most complete of all processed outputs by word count.
- Handles technical terminology well overall: `ETHDenver`, `Mist`, and `Geth` are preserved repeatedly.
- Corrects `Bob Summerwill`.
- Intro speaker name is now corrected to `Kieren James-Lubin`.
- Better completeness than the AssemblyAI-based outputs, but inherits more of the WhisperX-cloud base transcript's noise.

### whisperx-cloud_gpt

- Strong completeness and improved readability versus raw WhisperX-cloud.
- Corrects `Bob Summerwill`.
- Intro speaker name is now corrected to `Kieren James-Lubin`.
- Slightly more condensed than `whisperx-cloud_opus`, but still clearly Tier 1.

---

## 4. Cross-Transcriber Comparison

| Processor | AssemblyAI Base | WhisperX-cloud Base | Difference |
|-----------|----------------:|--------------------:|-----------:|
| **Opus** | 3,095 | 3,196 | WhisperX-cloud +101 |
| **GPT** | 3,029 | 3,125 | WhisperX-cloud +96 |

**Observations:**

- For both processors, the WhisperX-cloud-based output is longer and appears slightly more complete.
- For both processors, the AssemblyAI-based output is cleaner and less noisy to read.
- The main remaining weaknesses are residual ASR phrasing artifacts and partial canonical cleanup in body text, not the intro speaker name.
- All four processed outputs are comfortably above the 90% threshold, so all four are Tier 1.

---

## 5. Recommendations

### Best outputs for this episode

1. **Best editorial output:** `museum-of-ethereum_assemblyai_opus.md`
2. **Most complete output:** `museum-of-ethereum_whisperx-cloud_opus.md`
3. **Best GPT variant:** `museum-of-ethereum_whisperx-cloud_gpt.md`

### Publication guidance

- If the priority is readability and cleaner diarization, use **AssemblyAI + Opus**.
- If the priority is maximum coverage, use **WhisperX-cloud + Opus**.
- The intro speaker name is now fixed to `Kieren James-Lubin` across both transcriber bases.
- Canonical cleanup for in-body `Kieren` mentions may still need a final pass depending on the desired naming style.

### Final verdict

The pipeline is working well on this episode. The earlier intro-name problem is fixed, and the remaining weaknesses are smaller ASR wording artifacts rather than major name corruption or truncation. For practical use, **`assemblyai_opus` is the safest default** and **`whisperx-cloud_opus` is the completeness leader**.
