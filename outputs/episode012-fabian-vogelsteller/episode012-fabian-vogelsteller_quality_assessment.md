# Episode 012 (Fabian Vogelsteller) — Quality Assessment Report

## 1. Transcriber Comparison

| Transcriber | Status | Quality | Notes |
|-------------|--------|---------|-------|
| **WhisperX local** | **BROKEN** | Unusable | Output is entirely exclamation marks (`!!!!!!`) — complete corruption |
| **WhisperX-cloud** | Good | ~95% | Clean output, merges some speaker turns, preserves more natural speech fillers |
| **AssemblyAI** | Best | ~97% | Cleanest speaker separation, better proper name handling, more publication-ready |

**Verdict:** AssemblyAI is the clear winner. WhisperX local is completely unusable for this episode. WhisperX-cloud is serviceable but AssemblyAI produces cleaner diarization and more consistent results.

---

## 2. AI Processor Comparison (AssemblyAI base)

| Processor | Words | Completeness | Quality | Tier |
|-----------|-------|-------------|---------|------|
| **GLM5** | 17,665 | 100% (452 lines) | Excellent prose, faithful, complete | **Tier 1** |
| **Grok** | 18,474 | 100% (390 lines) | Excellent formatting, no issues | **Tier 1** |
| **Opus** | 18,837 | 100% | High quality, faithful to original | **Tier 1** |
| **GLM** | 19,191 | ~85% (394 lines) | Very good quality, slightly truncated | Tier 2 |
| **Kimi** | 12,009 | ~72% (276 lines) | Very good quality, truncated mid-conversation | Tier 2 |
| **ChatGPT** | 11,177 | Complete | Good quality, more condensed, better punctuation | Tier 2 |
| **Gemini** | 11,175 | Complete | Good quality, clean formatting | Tier 2 |
| **Llama** | 6,364 | ~39% (150 lines) | Severely truncated | Tier 3 |
| **Qwen** | 6,035 | ~39% (150 lines) | Severely truncated | Tier 3 |
| **Mistral** | 5,614 | ~36% (138 lines) | Severely truncated | Tier 3 |
| **DeepSeek** | 5,001 | Limited | Good within what exists, very condensed | Tier 3 |
| **MiniMax** | 3,386 | ~26% (98 lines) | Severely truncated, poorest output | **Tier 4** |

**Key finding:** The critical differentiator is **completeness**, not prose quality. All models produce decent English when they're generating text — the problem is that 5 of 11 models (Llama, Qwen, Mistral, DeepSeek, MiniMax) truncate severely, losing 60-75% of the transcript. This is likely a context window or output token limit issue.

**Top 3 processors:** GLM5, Grok, Opus — all produce complete, high-quality output.

---

## 3. Consensus Pipeline — BROKEN

The 6-phase AI consensus pipeline produced a **severely corrupted** final output:

| Metric | Value | Issue |
|--------|-------|-------|
| Input words | 18,882 | Healthy baseline |
| AI consensus output | 61,512 | **3.26x expansion** — catastrophic! |
| Consensus alignment | 0.4% - 1.3% | Virtually zero agreement between models |

### What went wrong

1. **12 divergent AI models** each applied different corrections with different word boundaries
2. **Loose time alignment tolerance** (0.5s) created massive alignment buckets where words couldn't be reliably matched
3. **Cascading corruption** — once alignment drifted in early sections, it propagated through the entire transcript
4. The output contains duplicated fragments, garbled word order, and broken sentences:
   ```
   you great, to great see to you . We, saw each other at DevConnect
   in November , I think ? That s not going to come out of my mouth .
   Great to see you . We saw each other at Devconnect in saw each other
   at DeadConnect .
   ```

**Root cause:** The word-level consensus voting algorithm fundamentally cannot work when the AI models disagree this much. With only 0.4-1.3% alignment between models, there's no meaningful consensus to build.

---

## 4. Whisperx-Cloud vs AssemblyAI (Detailed)

Word counts are remarkably similar across both transcriber bases, indicating comparable audio capture:

| Processor | AssemblyAI words | Whisperx-Cloud words |
|-----------|-----------------|---------------------|
| Opus | 18,837 | 18,116 |
| Grok | 18,474 | 18,232 |
| GLM | 19,191 | 19,063 |
| GLM5 | 17,665 | 18,982 |
| ChatGPT | 11,177 | 11,840 |
| Kimi | 12,009 | 11,916 |
| Gemini | 11,175 | 5,837 |
| Llama | 6,364 | 6,263 |
| Qwen | 6,035 | 6,020 |
| Mistral | 5,614 | 5,644 |
| MiniMax | 3,386 | 6,033 |
| DeepSeek | 5,001 | 2,478 |

**AssemblyAI advantages:** Cleaner speaker separation, better punctuation standardization, more publication-ready.
**Whisperx-Cloud advantages:** Preserves more natural speech patterns and conversational fillers, more faithful to actual spoken cadence.

---

## 5. Automated Quality Scores

From the AI quality assessment JSON (consensus pipeline metrics):

| Model | Quality Score | Input Preservation | Consensus Alignment |
|-------|--------------|-------------------|-------------------|
| Mistral | 0.60 | 1.00 | 0.004 |
| GLM | 0.40 | 0.41 | 0.007 |
| Kimi | 0.38 | 0.37 | 0.007 |
| GLM5 | 0.35 | 0.33 | 0.008 |
| Opus | 0.33 | 0.29 | 0.009 |
| Grok | 0.31 | 0.27 | 0.009 |
| DeepSeek | 0.31 | 0.27 | 0.010 |
| Llama | 0.31 | 0.27 | 0.010 |
| ChatGPT | 0.30 | 0.26 | 0.010 |
| MiniMax | 0.30 | 0.26 | 0.010 |
| Qwen | 0.30 | 0.25 | 0.013 |
| Gemini | 0.30 | 0.25 | 0.013 |

**Note:** These automated scores heavily weight `input_preservation` (how much of the original text was kept unchanged). Mistral scores highest (1.0 preservation) because it barely changed anything — this doesn't necessarily mean it produced the best transcript. The consensus alignment scores are catastrophically low across the board (0.4-1.3%), confirming the consensus pipeline failure.

---

## 6. Recommendations

### For the normal pipeline (Pipeline 1)
- **Best combo: AssemblyAI + Opus** (or Grok, or GLM5) — consistently complete, high-quality output
- Avoid Llama, Qwen, Mistral, MiniMax as post-processors — they truncate too aggressively
- ChatGPT and Gemini are decent middle ground (complete but more condensed)

### For the consensus pipeline (Pipeline 3)
- The current algorithm is fundamentally broken for this episode
- **Quick fix:** Add a validation gate — if consensus alignment < 5%, abort and fall back to the intermediate consensus (which was clean at 18,882 words)
- **Better fix:** Reduce from 12 to 3-5 high-quality models (Opus, Grok, GLM5) which produce similar-length outputs and would align better
- **Structural fix:** Tighten the time tolerance from 0.5s, and add word-count expansion limits (halt if output exceeds 150% of input)

### Overall best output for this episode
The individual `assemblyai_opus.md` transcript is the best available output — complete, well-formatted, and faithful to the original conversation.
