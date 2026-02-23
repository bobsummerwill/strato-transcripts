# Episode 013 (Zsolt Felfoldi) — Quality Assessment Report

## 1. Transcriber Comparison

| Transcriber | Status | Quality | Lines | Notes |
|-------------|--------|---------|-------|-------|
| **WhisperX local** | **BROKEN** | Unusable | 166 | Entirely corrupted — repeated exclamation marks (`!!!!!!`) replacing all content |
| **WhisperX-cloud** | Not available | N/A | — | No whisperx-cloud transcript exists for this episode |
| **AssemblyAI** | Excellent | ~97% | 294 | Clean diarization, accurate technical terms, publication-ready |

**Verdict:** AssemblyAI is the only usable transcriber for this episode. WhisperX local suffered the same complete corruption seen in episode012. No whisperx-cloud transcript was generated.

---

## 2. AI Processor Comparison (AssemblyAI base)

| Processor | Words | Completeness | Quality | Tier |
|-----------|-------|-------------|---------|------|
| **Kimi** | 8,185 | 100% | Excellent prose, complete | **Tier 1** |
| **GLM** | 8,178 | 100% | Excellent, faithful to original | **Tier 1** |
| **Grok** | 7,859 | 96% | Excellent formatting, no issues | **Tier 1** |
| **GLM5** | 7,744 | 95% | Excellent quality, complete | **Tier 1** |
| **ChatGPT** | 7,076 | 86% | Polished prose, professional presentation | Tier 2 |
| **Opus** | 6,665 | 81% | High quality, faithful | Tier 2 |
| **Gemini** | 6,597 | 81% | Clean formatting, good quality | Tier 2 |
| **MiniMax** | 6,180 | 75% | Acceptable quality | Tier 2 |
| **Llama** | 6,083 | 74% | Good within content, somewhat condensed | Tier 2 |
| **DeepSeek** | 5,945 | 73% | Name errors ("Zolt Zelfeldi"), grammatical issues | Tier 3 |
| **Qwen** | 5,684 | 69% | Condensed | Tier 3 |
| **Mistral** | 5,196 | 63% | Short, limited value | Tier 3 |

**Key finding:** Unlike episode012, no processor suffered severe truncation here. The spread is narrower (5,196–8,185 words). Kimi and GLM produced the longest and most complete outputs. DeepSeek stands out negatively for misspelling the guest's name.

**Top 3 processors:** Kimi, GLM, Grok — all complete with excellent quality.

---

## 3. AI Processor Comparison (WhisperX local base)

All WhisperX-based processor outputs are **unusable** — the corrupted input produced garbage output:

| Processor | Words | Status |
|-----------|-------|--------|
| Mistral | 1,958 | Mostly `[Unintelligible]` markers |
| MiniMax | 1,261 | Mostly `[Unintelligible]` markers |
| ChatGPT | 180 | `[Unintelligible]` throughout |
| Gemini | 180 | `[Unintelligible]` throughout |
| Opus | 180 | `[Unintelligible]` throughout |
| Kimi | 122 | `[Unintelligible]` throughout |
| Llama | 122 | `[Unintelligible]` throughout |
| DeepSeek | 122 | `[Unintelligible]` throughout |
| Qwen | 122 | `[Unintelligible]` throughout |
| Grok | 6 | Empty/near-empty |
| GLM5 | 6 | Empty/near-empty |

These confirm the WhisperX local transcription was completely corrupted before any AI processing.

---

## 4. AI Processor Comparison (WhisperX-cloud base)

| Processor | Words | Completeness | Quality | Tier |
|-----------|-------|-------------|---------|------|
| **Grok** | 8,600 | 100% | Excellent, most complete | **Tier 1** |
| **Opus** | 7,919 | 92% | High quality, faithful | **Tier 1** |
| **Gemini** | 7,320 | 85% | Clean formatting | Tier 2 |
| **Llama** | 7,273 | 85% | Good quality | Tier 2 |
| **GLM** | 7,138 | 83% | Very good | Tier 2 |
| **ChatGPT** | 6,804 | 79% | Polished prose | Tier 2 |
| **Kimi** | 6,736 | 78% | Good quality | Tier 2 |
| **GLM5** | 6,666 | 77% | Good quality | Tier 2 |
| **MiniMax** | 6,545 | 76% | Acceptable | Tier 2 |
| **Mistral** | 5,894 | 69% | Condensed | Tier 3 |
| **Qwen** | 5,409 | 63% | Short | Tier 3 |
| **DeepSeek** | 1,483 | 17% | Severely truncated | **Tier 4** |

**Note:** WhisperX-cloud outputs are generally comparable to AssemblyAI. DeepSeek is the outlier — severely truncated at only 1,483 words (17% of max).

---

## 5. Cross-Transcriber Comparison

Side-by-side word counts for the same processor across different transcriber bases:

| Processor | AssemblyAI | WhisperX-cloud | WhisperX local |
|-----------|-----------|----------------|---------------|
| Grok | 7,859 | 8,600 | 6 |
| Opus | 6,665 | 7,919 | 180 |
| Kimi | 8,185 | 6,736 | 122 |
| GLM | 8,178 | 7,138 | — |
| ChatGPT | 7,076 | 6,804 | 180 |
| Gemini | 6,597 | 7,320 | 180 |
| GLM5 | 7,744 | 6,666 | 6 |
| Llama | 6,083 | 7,273 | 122 |
| MiniMax | 6,180 | 6,545 | 1,261 |
| Mistral | 5,196 | 5,894 | 1,958 |
| DeepSeek | 5,945 | 1,483 | 122 |
| Qwen | 5,684 | 5,409 | 122 |

**Observations:**
- AssemblyAI and WhisperX-cloud produce comparable results for most processors
- WhisperX-cloud Grok (8,600) is the single highest word count across all combinations
- WhisperX local is completely unusable across the board
- DeepSeek performs poorly on WhisperX-cloud (1,483 words) but reasonably on AssemblyAI (5,945)

---

## 6. Consensus Pipeline

**Status:** Not run — no `*_final.md`, `*_ai_quality_assessment.json`, or word-level consensus files exist for this episode. Only Pipeline 1 (single-model post-processing) was run.

---

## 7. Recommendations

### Best transcriber+processor combinations
1. **AssemblyAI + Kimi** (8,185 words) — most complete, excellent quality
2. **AssemblyAI + GLM** (8,178 words) — equally complete, excellent quality
3. **WhisperX-cloud + Grok** (8,600 words) — highest word count overall, excellent quality
4. **AssemblyAI + Grok** (7,859 words) — reliable, well-formatted

### Processors to avoid
- **DeepSeek** — misspells guest's name on AssemblyAI base, severely truncated on WhisperX-cloud
- **Mistral** — consistently produces the shortest outputs
- **Qwen** — consistently condensed

### Next steps
- The consensus pipeline (Phases 2-6) has not been run for this episode
- WhisperX local should be regenerated or skipped entirely (corruption pattern matches episode012)
- For publication, `assemblyai_kimi.md` or `assemblyai_glm.md` are the best available outputs
