# Build Word-Level Consensus

Build consensus transcripts from multiple transcribers AND AI post-processors using word-level alignment.

## Usage

```
/consensus [options]
```

## Arguments

**For Phases 1-2 (Transcriber Consensus)** - uses `assess_quality.py`:
- `--episode <name>` - Process specific episode (default: all episodes)
- `--transcribers <list>` - Comma-separated transcribers to use (default: all available)

**For Phases 3-6 (AI Consensus Pipeline)** - uses `ai_consensus_pipeline.py`:
- `--episode <name>` - Process specific episode (required)
- `--processors <list>` - Comma-separated AI models (default: all 11)
- `--phase <n>` - Run specific phase only (3, 4, 5, or 6)

## Full 6-Phase Pipeline

```
Phase 1-2: Transcriber Consensus (existing)
  whisperx + assemblyai → intermediate_consensus_words.json

Phase 3-6: AI Consensus Pipeline (new)
  intermediate_consensus → 11 AI models → AI consensus → final output
```

## Quick Start

```bash
# Full pipeline from scratch (all 3 transcribers)
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 \
  --transcribers whisperx,whisperx-cloud,assemblyai --consensus
python3 scripts/assess_quality.py --intermediate-consensus --episode <name>
python3 scripts/ai_consensus_pipeline.py --episode <name>
```

## Two-Step Workflow (Phases 1-2)

### Step 1: Transcribe in Consensus Mode
Run transcription with `--consensus` flag to generate word-level JSON files:
```bash
python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 \
  --transcribers whisperx,whisperx-cloud,assemblyai --consensus
```

This generates **ONLY** JSON files (no md/txt):
```
intermediates/episode001/
  episode001_whisperx_consensus_words.json
  episode001_assemblyai_consensus_words.json
```

### Step 2: Build Consensus
Run consensus generation to align and merge:
```bash
python3 scripts/assess_quality.py --intermediate-consensus --episode <name>
```

## Instructions

When the user invokes this command:

1. **Check for consensus word-level JSON files**:
   ```bash
   ls intermediates/*/*_consensus_words.json
   ```

2. **If missing, inform user to run transcription first**:
   ```bash
   python3 scripts/process_single_transcribe_and_diarize.py audio.mp3 \
     --transcribers whisperx,whisperx-cloud,assemblyai --consensus
   ```

3. **Run consensus generation**:
   ```bash
   python3 scripts/assess_quality.py --intermediate-consensus [--episode <episode-name>]
   ```

4. **Report results**:
   - Consensus transcript location
   - Word agreement scores
   - Speaker alignment statistics

## Examples

```bash
# Full workflow for an episode
/transcribe episode001.mp3 --transcribers whisperx,whisperx-cloud,assemblyai --consensus
/consensus --episode episode001

# Generate consensus for specific episode (if JSON already exists)
/consensus --episode episode004-taylor-gerring

# Generate consensus for all episodes
/consensus
```

## Output Structure

All outputs go to `intermediates/<episode>/`:
```
intermediates/episode001/
  # Phase 1: Raw transcriber outputs
  episode001_whisperx_consensus_words.json       # WhisperX raw words
  episode001_assemblyai_consensus_words.json     # AssemblyAI raw words

  # Phase 2: Merged consensus
  episode001_intermediate_consensus.md           # Final merged transcript
  episode001_intermediate_consensus.txt          # Plain text
  episode001_intermediate_consensus_words.json   # Merged word-level data
```

## How Consensus Works

1. **Word Alignment**: Aligns words from multiple transcribers (whisperx, assemblyai, etc.)
2. **Agreement Scoring**: Each word gets a confidence score based on how many sources agree
3. **Speaker Voting**: Speaker labels determined by majority vote across sources
4. **Timestamp Averaging**: Timestamps averaged from agreeing sources

## Requirements

- At least 2 transcribers for meaningful consensus
- Consensus word-level JSON files must exist (`*_consensus_words.json`)
- **Run transcription with `--consensus` flag first**

---

## AI Consensus Pipeline (Phases 3-6)

After building intermediate consensus (Phases 1-2), run the AI pipeline for superb quality.

**IMPORTANT**: Source API keys before running:
```bash
source setup_env.sh
```

Then run the pipeline:
```bash
python3 scripts/ai_consensus_pipeline.py --episode <name>
```

### Phase 3: AI Correction Pass

Processes intermediate consensus through all 11 AI models:
- opus, gemini, chatgpt, grok, deepseek
- kimi, qwen, glm, minimax, llama, mistral

Each model corrects technical terms, names, grammar while the alignment algorithm preserves word-level timestamps.

```bash
# Run Phase 3 only
python3 scripts/ai_consensus_pipeline.py --episode <name> --phase 3

# Run with specific models (for testing)
python3 scripts/ai_consensus_pipeline.py --episode <name> --processors opus,gemini,grok
```

Output: `intermediates/<episode>/<episode>_ai_{model}_words.json` (×11)

### Phase 4: AI Consensus

Builds consensus from 11 AI-corrected word lists using voting:
- Text: Majority vote (case-insensitive)
- Speaker: Majority vote
- Timestamps: Average

```bash
python3 scripts/ai_consensus_pipeline.py --episode <name> --phase 4
```

Output: `intermediates/<episode>/<episode>_ai_consensus_words.json`

### Phase 5: Filler Word Removal

Filters out filler words from consensus:
- um, uh, er, ah, hmm
- actually, basically, literally
- yeah, yep, okay, ok

```bash
python3 scripts/ai_consensus_pipeline.py --episode <name> --phase 5
```

Output: `intermediates/<episode>/<episode>_final_words.json`

### Phase 6: Final Output

Generates final transcript files:

```bash
python3 scripts/ai_consensus_pipeline.py --episode <name> --phase 6
```

Output:
```
outputs/<episode>/
  <episode>_final.md    # Markdown with timestamps
  <episode>_final.txt   # Plain text
  <episode>_final_words.json  # Word-level data
```

## Complete File Structure

```
intermediates/<episode>/
  # Phase 1: Raw transcriber outputs
  <episode>_whisperx_consensus_words.json
  <episode>_whisperx-cloud_consensus_words.json
  <episode>_assemblyai_consensus_words.json

  # Phase 2: Transcriber consensus
  <episode>_intermediate_consensus_words.json
  <episode>_intermediate_consensus.md
  <episode>_intermediate_consensus.txt

  # Phase 3: AI corrections (×11)
  <episode>_ai_opus_words.json
  <episode>_ai_gemini_words.json
  <episode>_ai_chatgpt_words.json
  ... (8 more)

  # Phase 4: AI consensus
  <episode>_ai_consensus_words.json

  # Phase 5: Filler removed
  <episode>_final_words.json

outputs/<episode>/
  # Phase 6: Final outputs
  <episode>_final.md
  <episode>_final.txt
  <episode>_final_words.json
```

## Cost Estimate

For a typical 60-90 min transcript (~20K tokens):
- 11 AI models × ~20K tokens = ~$3-5 per episode
- Opus alone is ~60% of cost ($1.80)

To reduce cost, use fewer models:
```bash
python3 scripts/ai_consensus_pipeline.py --episode <name> \
  --processors gemini,deepseek,grok,llama,mistral
```
