# Self-Assess Transcript Quality

Perform an extensive AI-driven quality assessment of all pipeline outputs for an episode, comparing transcribers and processors. Produces a detailed markdown report.

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
   intermediates/<episode>/  — raw transcripts, word JSONs
   outputs/<episode>/        — processed transcripts
   ```
   List all `.md` and `.json` files in both directories.

2. **Assess transcriber quality** — Read the first 100 lines of each raw transcriber output:
   - `intermediates/<episode>/<episode>_whisperx.md` (WhisperX local)
   - `intermediates/<episode>/<episode>_whisperx-cloud.md` (WhisperX-cloud)
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

4. **Compare transcriber bases** — If outputs exist for multiple transcribers (e.g., both `*_assemblyai_opus.md` and `*_whisperx-cloud_opus.md`):
   - Compare word counts side by side
   - Note quality differences

5. **Generate report** — Write a comprehensive markdown report to:
   ```
   outputs/<episode>/<episode>_quality_assessment.md
   ```

   The report should include these sections:
   - **Transcriber Comparison** — Table with status, quality rating, notes
   - **AI Processor Comparison** — Table with word counts, completeness, quality tier
   - **Cross-Transcriber Comparison** — Side-by-side word counts if multiple bases exist
   - **Recommendations** — Best transcriber+processor combo

6. **Report results** to the user with a summary of key findings.

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
