# Assess Transcript Quality

Assess quality of transcripts and compare outputs from different transcribers/processors.

## Usage

```
/quality [options]
```

## Arguments

- `--episode <name>` - Assess specific episode (default: all)
- `--transcribers <list>` - Comma-separated transcribers to use (default: all)
- `--intermediate-consensus` - Build word-level consensus from transcribers
- `--compare` - Compare multiple transcript versions
- `--stats` - Show detailed statistics

## Instructions

When the user invokes this command:

1. **Check available transcripts**:
   ```bash
   ls -la intermediates/
   ls -la outputs/
   ```

2. **Run quality assessment**:
   ```bash
   python3 scripts/assess_quality.py [--episode <episode-name>]
   ```

3. **Report findings**:
   - Word count comparisons
   - Speaker identification accuracy
   - Technical term consistency
   - Timestamp alignment quality

## Examples

```bash
# Assess all episodes
/quality

# Assess specific episode
/quality --episode episode004-taylor-gerring

# Compare transcriber outputs
/quality --compare --episode episode004-taylor-gerring

# Build consensus with specific transcribers only
/quality --intermediate-consensus --episode episode007 --transcribers assemblyai

# Build consensus from all available transcribers
/quality --intermediate-consensus --episode episode007
```

## Quality Metrics

| Metric | Description |
|--------|-------------|
| Word Count | Total words per transcriber/processor |
| Speaker Count | Number of unique speakers detected |
| Timestamp Coverage | Percentage of words with timestamps |
| Agreement Score | How often sources agree on words |

## Troubleshooting

- **Missing files**: Ensure transcription completed first
- **No consensus**: Need 2+ transcribers for comparison
- **Low agreement**: May indicate audio quality issues
