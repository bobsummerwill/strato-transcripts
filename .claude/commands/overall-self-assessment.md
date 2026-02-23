# Quality Report

Merge all per-episode self-assessments into a single cross-episode quality report. Aggregates transcriber reliability, processor rankings, and best-combo recommendations across the entire corpus.

## Usage

```
/quality-report
```

## Instructions

When the user invokes this command:

### 1. Discover all self-assessment reports

```
outputs/*/episode*_quality_assessment.md
```

List every report found. If fewer than 2 exist, warn the user and suggest running `/self-assess` on more episodes first.

### 2. Read every report

Read each `*_quality_assessment.md` in full. Extract the following structured data from each:

**Per episode, extract:**
- Episode name (from the `# Episode NNN (Guest Name)` heading)
- Transcriber statuses (WhisperX local, WhisperX-cloud, AssemblyAI — status and quality)
- AI processor table(s) — for each transcriber base: processor name, word count, completeness %, quality tier
- Consensus pipeline status (not run / working / broken, and key metrics if available)
- Recommended best combo
- Processors to avoid

### 3. Build aggregated tables

From the extracted data, compute:

**A. Transcriber Reliability Matrix**

For each transcriber, across all episodes:
- How many episodes had usable output
- How many were broken/missing
- Average quality rating where available

**B. Processor Leaderboard (AssemblyAI base)**

Since AssemblyAI is the most reliable transcriber, build a cross-episode processor ranking from AssemblyAI-based outputs:

For each processor, across all episodes:
- Average word count
- Average completeness %
- Tier distribution (how many Tier 1, Tier 2, Tier 3, Tier 4 across episodes)
- Consistency score: how often it lands in Tier 1 or Tier 2
- Notable issues (truncation, name errors, etc.)

Sort by consistency (Tier 1+2 rate), then by average completeness.

**C. Processor Leaderboard (WhisperX-cloud base)**

Same as above but for WhisperX-cloud-based outputs, where available.

**D. Cross-Transcriber Processor Comparison**

For processors that have outputs from both AssemblyAI and WhisperX-cloud:
- Average word count from each base
- Which base tends to produce more complete output for each processor

### 4. Generate insights

Synthesize the aggregated data into:

- **Overall best processors** — consistently Tier 1 across episodes and transcriber bases
- **Overall worst processors** — consistently Tier 3/4 or with recurring issues
- **Transcriber recommendation** — which transcriber to use by default
- **Recurring patterns** — e.g., WhisperX local corruption, specific models truncating on long episodes
- **Episode-specific outliers** — any episode where rankings differ significantly from the norm

### 5. Write the report

Save the merged report to:

```
outputs/quality_report.md
```

Use this structure:

```markdown
# Overall Quality Report

*Generated: YYYY-MM-DD*
*Episodes assessed: N*

## Summary

[2-3 paragraph executive summary of key findings]

## 1. Transcriber Reliability

[Table: transcriber × episode status matrix]
[Verdict paragraph]

## 2. Processor Leaderboard (AssemblyAI base)

[Table: processor ranked by consistency and completeness]
[Analysis paragraph]

## 3. Processor Leaderboard (WhisperX-cloud base)

[Table if data available, or note if insufficient data]

## 4. Cross-Transcriber Comparison

[Table: processor × transcriber average word counts]
[Which transcriber base produces better results]

## 5. Processor Tier Distribution

[Table: processor × tier counts across all episodes]
[Visual summary of consistency]

## 6. Best Combinations

[Ranked list of transcriber+processor combos with evidence]

## 7. Processors to Avoid

[List with reasons, supported by cross-episode evidence]

## 8. Recommendations

[Actionable recommendations for default pipeline configuration]
[Suggestions for further assessment]

## Appendix: Per-Episode Summaries

[One-paragraph summary of each episode's key findings with link to full report]
```

### 6. Report results

Print a concise summary to the user highlighting:
- Number of episodes analyzed
- Top 3 processor recommendations
- Bottom 3 processor warnings
- Any surprising findings

## Output

```
outputs/quality_report.md
```
