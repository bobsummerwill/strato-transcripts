# Self-Assess Transcript Quality

Perform an extensive AI-driven quality assessment of all pipeline outputs for an episode, comparing transcribers, processors, and the consensus pipeline. Produces a detailed markdown report.

## Usage

```
/self-assess <episode-name>
```

## Arguments

- `<episode-name>` - Episode directory name (e.g., `episode012-fabian-vogelsteller`)

## Instructions

When the user invokes this command:

1. **Discover available files** for the episode:
   ```
   intermediates/<episode>/  — raw transcripts, word JSONs, consensus files
   outputs/<episode>/        — processed transcripts, final output
   ```
   List all `.md` and `.json` files in both directories.

2. **Assess transcriber quality** — Read the first 100 lines of each raw transcriber output:
   - `intermediates/<episode>/<episode>_whisperx.md` (WhisperX local)
   - `intermediates/<episode>/<episode>_whisperx-cloud_consensus.md` (WhisperX-cloud)
   - `intermediates/<episode>/<episode>_assemblyai.md` (AssemblyAI)
   - Check for corruption (garbled text, repeated characters, empty content)
   - Compare speaker diarization quality
   - Note which transcribers produced usable output

3. **Assess AI processor quality** — For EACH processor output in `outputs/<episode>/`:
   - Get word count (`wc -w`)
   - Read the first 150 lines and last 100 lines
   - Evaluate: completeness, formatting, speaker labels, prose quality, technical accuracy
   - Flag truncated outputs (compare word count to the longest output)
   - Categorize into quality tiers:
     - **Tier 1**: Complete output (>90% of max word count), excellent quality
     - **Tier 2**: Mostly complete or complete but condensed, good quality
     - **Tier 3**: Severely truncated (<50% of max word count)
     - **Tier 4**: Unusable (extreme truncation, corruption)

4. **Assess consensus pipeline** (if `*_final.md` exists):
   - Read first 200 lines and last 100 lines of the final output
   - Check for garbled text, duplication, word-order corruption
   - Read `*_ai_quality_assessment.json` for automated metrics
   - Compare consensus word count vs input word count (flag if >150% expansion)
   - Check consensus alignment scores (flag if <5%)

5. **Compare transcriber bases** — If outputs exist for multiple transcribers (e.g., both `*_assemblyai_opus.md` and `*_whisperx-cloud_opus.md`):
   - Compare word counts side by side
   - Note quality differences

6. **Generate report** — Write a comprehensive markdown report to:
   ```
   outputs/<episode>/<episode>_quality_assessment.md
   ```

   The report should include these sections:
   - **Transcriber Comparison** — Table with status, quality rating, notes
   - **AI Processor Comparison** — Table with word counts, completeness, quality tier
   - **Consensus Pipeline Assessment** — Status, metrics, what went wrong (if broken)
   - **Cross-Transcriber Comparison** — Side-by-side word counts if multiple bases exist
   - **Automated Quality Scores** — Table from the JSON assessment (if available)
   - **Recommendations** — Best transcriber+processor combo, consensus pipeline fixes

7. **Report results** to the user with a summary of key findings.

## Examples

```bash
# Assess episode 012
/self-assess episode012-fabian-vogelsteller

# Assess episode 009
/self-assess episode009-amir-taaki
```

## Output

The report is saved as:
```
outputs/<episode>/<episode>_quality_assessment.md
```

## Quality Tier Definitions

| Tier | Criteria |
|------|----------|
| **Tier 1** | Complete (>90% of max words), excellent prose, proper formatting |
| **Tier 2** | Mostly complete or well-condensed, good quality |
| **Tier 3** | Severely truncated (<50% of max words), limited value |
| **Tier 4** | Unusable — corruption, extreme truncation, or broken output |

## Key Metrics to Report

| Metric | What to Check |
|--------|--------------|
| Word count | Compare across all processors; flag outliers |
| Completeness | Does the transcript cover the full episode? |
| Speaker diarization | Are speaker labels preserved and consistent? |
| Technical accuracy | Are blockchain/Ethereum terms correct? |
| Prose quality | Grammar, coherence, readability |
| Consensus alignment | From JSON — should be >5% to be meaningful |
| Word count expansion | Consensus output vs input — should be <150% |
