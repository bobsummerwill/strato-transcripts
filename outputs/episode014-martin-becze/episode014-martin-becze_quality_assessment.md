# Episode 014 (Martin Becze) — Quality Assessment Report

## 1. Transcriber Quality

| Transcriber | Word Count | Lines | Status | Diarization | Notes |
|-------------|-----------|-------|--------|-------------|-------|
| **AssemblyAI** | ~4,500 | ~165 | Excellent | 2 speakers (SPEAKER_00, SPEAKER_01), clean | Accurate speech recognition, proper sentence structure |
| **WhisperX-cloud** | ~4,500 | ~165 | Excellent | 2 speakers, clean | Good quality, comparable to AssemblyAI |
| **WhisperX local** | ~100 | ~60 | **CORRUPTED** | Structure present | "Thank you." hallucination loop — no actual content |

**Transcriber Verdict:** AssemblyAI and WhisperX-cloud both provide usable transcriptions for this ~25-minute interview. WhisperX local suffered catastrophic hallucination — the entire transcript is filled with repeated "Thank you." entries at regular intervals, with no actual speech content. This is the same corruption pattern seen in ep007, ep012-fabian, ep013, and the online-oracles recording.

---

## 2. AssemblyAI Transcriber — Detail

The AssemblyAI transcript is high quality:
- Clean 2-speaker diarization (SPEAKER_00 = Bob Summerwill, SPEAKER_01 = Martin Becze)
- Accurate timestamps throughout the ~25-minute interview
- Technical terminology well-captured: EVM, JavaScript, Node Ethereum, Namecoin, GoDNS, Ethereum JS, RLP, DHT, DevCon
- Guest name: "Becze" (close to correct pronunciation "betse")
- First commit history, Ripple interview context, early Ethereum JS development — all well-preserved
- Conversational filler ("like", "you know", "yeah") preserved naturally

---

## 3. AI Processor Quality — AssemblyAI Base

| Processor | Word Count | Lines | Completeness | Tier |
|-----------|-----------|-------|-------------|------|
| **assemblyai_grok** | 4,103 | ~150 | ~100% of max | **Tier 1** |
| **assemblyai_qwen** | 4,098 | ~150 | ~100% of max | **Tier 1*** |
| **assemblyai_gemini** | 3,842 | ~140 | ~94% of max | **Tier 1** |
| **assemblyai_opus** | 3,819 | ~140 | ~93% of max | **Tier 1** |

*\* Critical name error — see below*

### assemblyai_grok (Tier 1 — Complete, Excellent)
- **Word count:** 4,103 (highest among AssemblyAI-based outputs)
- **Coverage:** Complete from [00:02] to [25:34]
- **Name handling:** Correctly identifies "Martin Becze" and "Kumavis" throughout — no name substitution errors
- **Formatting:** Clean markdown with bold speaker/timestamp labels
- **Content fidelity:** Very faithful to the raw transcriber output, preserving conversational style and verbatim speech
- **Assessment:** Most complete and correctly named output in the AssemblyAI base

### assemblyai_qwen (Tier 1* — Complete, but CRITICAL Name Error)
- **Word count:** 4,098 (near-identical to Grok)
- **Coverage:** Complete from [00:02] to [25:34]
- **Name handling:** **CRITICAL ERROR** — substitutes "Martin Swende" for "Martin Becze" throughout the entire transcript. Bob Summerwill says "talking to Martin Becze" at [00:13] but Qwen outputs "talking to Martin Swende." Also substitutes "Dan Finlay" for "Kumavis" at [10:47], [24:26], and [24:41]. These are plausible Ethereum ecosystem names but are factually wrong for this interview
- **Content fidelity:** High verbatim quality in all other respects
- **Assessment:** Downgraded to Tier 1* (conditionally usable only with name corrections). The name substitution pattern — replacing unknown names with famous Ethereum names — is a systematic Qwen failure mode also seen in episode012-martin and episode014 (same person, different recording). **Do not publish without correcting all name references.**

### assemblyai_gemini (Tier 1 — Mostly Complete, Good Quality)
- **Word count:** 3,842
- **Coverage:** Complete throughout the interview
- **Name handling:** Good — "Martin Becze", correctly handles "Kumavis"
- **Formatting:** Clean markdown, good paragraph structure
- **Content fidelity:** Moderate editorial cleanup — smooths filler words, tightens prose
- **Assessment:** Good quality output with accurate names

### assemblyai_opus (Tier 1 — Mostly Complete, Excellent Quality)
- **Word count:** 3,819 (93% of max)
- **Coverage:** Complete from [00:02] to [25:34]
- **Name handling:** Excellent — "Martin Becze", "Kumavis", proper capitalization throughout
- **Formatting:** Clean markdown, well-structured paragraphs, removes filler words cleanly
- **Content fidelity:** Highest editorial quality — removes verbal stumbles, tightens prose while preserving meaning accurately
- **Assessment:** Best editorial quality with accurate names

---

## 4. AI Processor Quality — WhisperX Local Base

All WhisperX local-based outputs are **unusable** due to the hallucinated source transcription:

| Processor | Word Count | Lines | Status |
|-----------|-----------|-------|--------|
| **whisperx_opus** | 108 | ~55 | All `[inaudible]` markers — AI identified corruption, produced nothing |
| **whisperx_gemini** | 181 | ~80 | All `[inaudible]` markers — identical failure pattern |
| **whisperx_grok** | 187 | ~80 | All `[inaudible]` markers — identical failure pattern |
| **whisperx_qwen** | 185 | ~80 | All `[inaudible]` markers — identical failure pattern |

**Verdict:** All four processors correctly identified the corrupted input and produced only `[inaudible]` markers or near-empty outputs. None recovered any usable content. All are Tier 4 (Unusable). The WhisperX local "Thank you." hallucination loop propagated through all processors identically.

---

## 5. AI Processor Quality — WhisperX-Cloud Base

| Processor | Word Count | Lines | Completeness | Tier |
|-----------|-----------|-------|-------------|------|
| **whisperx-cloud_grok** | 4,160 | ~150 | ~100% of max | **Tier 1** |
| **whisperx-cloud_qwen** | 3,918 | ~140 | ~94% of max | **Tier 1*** |
| **whisperx-cloud_opus** | 3,669 | ~135 | ~88% of max | **Tier 1** |
| **whisperx-cloud_gemini** | 3,670 | ~135 | ~88% of max | **Tier 1** |

*\* Same name substitution error as assemblyai_qwen*

### whisperx-cloud_grok (Tier 1 — Complete, Excellent)
- **Word count:** 4,160 (highest across all outputs)
- **Name handling:** Correct — "Martin Becze", "Kumavis"
- **Assessment:** Most complete output overall. Very verbatim, good name accuracy

### whisperx-cloud_qwen (Tier 1* — Complete, CRITICAL Name Error)
- **Word count:** 3,918
- **Name handling:** Same "Martin Swende" / "Dan Finlay" substitution errors as in the AssemblyAI base
- **Assessment:** Tier 1* — usable only with name correction

### whisperx-cloud_opus (Tier 1 — Good Quality)
- **Word count:** 3,669
- **Name handling:** Correct — "Martin Becze", "Kumavis"
- **Assessment:** Good editorial quality, accurate names

### whisperx-cloud_gemini (Tier 1 — Good Quality)
- **Word count:** 3,670 (virtually identical to opus)
- **Name handling:** Good — "Martin Becze", handles "Kumavis" correctly
- **Assessment:** Good quality, full coverage

---

## 6. Cross-Transcriber Comparison

| Processor | AssemblyAI Words | WhisperX-cloud Words | WhisperX Words |
|-----------|-----------------|---------------------|----------------|
| **Grok** | **4,103** | **4,160** | 187 (T4) |
| **Qwen** | 4,098* | 3,918* | 185 (T4) |
| **Gemini** | 3,842 | 3,670 | 181 (T4) |
| **Opus** | 3,819 | 3,669 | 108 (T4) |

*\* Name substitution errors*

**Observations:**
- This is a shorter interview (~25 minutes) so all word counts are lower than typical 60-90 minute episodes
- AssemblyAI and WhisperX-cloud perform comparably — neither base clearly dominates
- Grok produces the highest word counts in both bases
- Qwen produces high word counts but has systematic name substitution errors
- WhisperX local is catastrophically corrupted — all processors correctly identified this
- Opus provides the best editorial quality in both bases
- All AssemblyAI and WhisperX-cloud outputs are effectively Tier 1 (complete for a short episode)

---

## 7. Recommendations

### Best outputs for this episode
1. **whisperx-cloud_grok** (4,160 words, Tier 1) — Highest word count, correct names, good verbatim quality
2. **assemblyai_grok** (4,103 words, Tier 1) — Very complete with clean diarization and correct names
3. **assemblyai_opus** (3,819 words, Tier 1) — Best editorial quality with accurate names
4. **assemblyai_gemini** (3,842 words, Tier 1) — Good quality with accurate names

### For publication
- **Best balance:** `assemblyai_opus` — high editorial quality, correct names, good diarization
- **Most verbatim:** `whisperx-cloud_grok` or `assemblyai_grok`
- **Avoid:** All `_qwen` outputs unless "Martin Swende" → "Martin Becze" and "Dan Finlay" → "Kumavis" substitutions are manually corrected throughout

### Issues to address
- **Qwen name substitution (critical):** All qwen outputs call the guest "Martin Swende" (a different Ethereum developer) and substitute "Dan Finlay" for "Kumavis" (Aaron Davis). This is a systematic Qwen failure mode for this person's name — must be corrected before publication
- **WhisperX local corruption:** Permanent "Thank you." hallucination loop — skip this transcriber for this episode
- **Speaker identification:** All outputs use SPEAKER_00/SPEAKER_01 labels — should be replaced with "Bob Summerwill" / "Martin Becze" for publication
- **Name pronunciation note:** Martin clarifies at [00:29] the name is pronounced "betse" — outputs spell it "Becze"
