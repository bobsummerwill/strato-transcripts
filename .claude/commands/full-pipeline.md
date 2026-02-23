# Full Pipeline

Run the complete transcription and post-processing pipeline on an audio file.

## Usage

```
/full-pipeline <audio_file> [options]
```

## Arguments

- `<audio_file>` - Path to audio file (mp3, wav, m4a, etc.)
- `--transcribers` - Transcribers to use (default: whisperx)
- `--processors` - AI processors to use (default: opus)
- `--force` - Reprocess even if outputs exist

## Instructions

When the user invokes this command:

1. **Validate audio file exists**

2. **Source environment**:
   ```bash
   source setup_env.sh
   ```

3. **Run combined pipeline**:
   ```bash
   ./scripts/process_single.sh <audio_file> --transcribers <transcribers> --processors <processors> [--force]
   ```

   Or run steps separately:
   ```bash
   # Step 1: Transcribe
   python3 scripts/process_single_transcribe_and_diarize.py <audio_file> --transcribers <transcribers>

   # Step 2: Post-process
   python3 scripts/process_single_post_process.py intermediates/<episode>/<episode>_<transcriber>.md --processors <processors>
   ```

4. **Report results**:
   - Intermediate transcripts in `intermediates/`
   - Final outputs in `outputs/`
   - Total processing time

## Examples

```bash
# Basic pipeline (whisperx + opus)
/full-pipeline episode001.mp3

# Multiple transcribers and processors
/full-pipeline episode001.mp3 --transcribers whisperx,assemblyai --processors opus,gemini

# Force reprocess everything
/full-pipeline episode001.mp3 --force

# All processors
/full-pipeline episode001.mp3 --processors opus,grok,gemini
```

## Pipeline Steps

1. **Transcription** (WhisperX/AssemblyAI)
   - Speaker diarization
   - Word-level timestamps
   - Outputs to `intermediates/`

2. **Post-Processing** (AI models)
   - Technical term correction
   - Name/acronym fixes
   - Formatting improvements
   - Outputs to `outputs/`

## Output Structure

```
intermediates/
  episode001/
    episode001_whisperx.md
    episode001_whisperx_words.json

outputs/
  episode001/
    episode001_whisperx_opus.md
```

## Typical Processing Times

| Audio Length | WhisperX (GPU) | AssemblyAI | Post-Process |
|--------------|----------------|------------|--------------|
| 30 min | ~6 min | ~2 min | ~30 sec |
| 60 min | ~12 min | ~3 min | ~45 sec |
| 90 min | ~18 min | ~4 min | ~60 sec |

## Two Independent Pipelines

This project has two pipelines that don't interfere with each other:

| Pipeline | Output Pattern | Use Case |
|----------|----------------|----------|
| **1. Original (this)** | `{episode}_{transcriber}_{processor}.md` | Quick single-model output |
| **2. Video Caption** | `{episode}_{transcriber}.srt/.ass` | Burned-in subtitles |
