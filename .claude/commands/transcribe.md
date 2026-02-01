# Transcribe Audio

Transcribe audio files using local WhisperX (GPU) or cloud services (AssemblyAI, Replicate).

## Usage

```
/transcribe <audio_file> [options]
```

## Arguments

- `<audio_file>` - Path to audio file (mp3, wav, m4a, etc.)
- `--transcribers` - Comma-separated list: whisperx, assemblyai, whisperx-cloud (default: whisperx)
- `--consensus` - Consensus mode: generate ONLY word-level JSON for alignment
- `--force` - Reprocess even if output exists
- `--force-cpu` - Force CPU mode for WhisperX (slower)

## Modes

### Normal Mode (default)
- Produces clean transcripts (`.md` and `.txt`)
- Removes filler words (um, uh, etc.) from AssemblyAI
- **NO** JSON file generated
- Use for: final transcripts, post-processing, video captions

### Consensus Mode (`--consensus`)
- Produces **ONLY** `*_consensus_words.json` with word-level timing
- **NO** `.md` or `.txt` files (avoids confusion with normal output)
- Keeps ALL words including ums, ahs, disfluencies
- Use for: building consensus from multiple transcribers

## Instructions

When the user invokes this command:

1. **Validate the audio file exists** at the specified path

2. **Check environment setup**:
   ```bash
   source setup_env.sh && echo "Environment loaded"
   ```

3. **Run transcription**:
   ```bash
   # Normal mode (clean md/txt, no JSON)
   python3 scripts/process_single_transcribe_and_diarize.py <audio_file> --transcribers <transcribers>

   # Consensus mode (JSON only, no md/txt)
   python3 scripts/process_single_transcribe_and_diarize.py <audio_file> --transcribers <transcribers> --consensus
   ```

4. **Report results**:
   - Normal: `intermediates/<episode>/<episode>_<transcriber>.md`
   - Consensus: `intermediates/<episode>/<episode>_<transcriber>_consensus_words.json`

## Examples

```bash
# Normal transcription (clean md/txt)
/transcribe episode001.mp3

# Consensus mode (JSON only for alignment)
/transcribe episode001.mp3 --consensus

# Multiple transcribers for consensus building
/transcribe episode001.mp3 --transcribers whisperx,assemblyai --consensus

# Cloud transcription
/transcribe episode001.mp3 --transcribers assemblyai

# Force reprocess
/transcribe episode001.mp3 --force
```

## Output Structure

### Normal Mode
```
intermediates/episode001/
  episode001_whisperx.txt        # Plain text (cleaned)
  episode001_whisperx.md         # Markdown with timestamps
```

### Consensus Mode
```
intermediates/episode001/
  episode001_whisperx_consensus_words.json    # Word-level timing (JSON only)
  episode001_assemblyai_consensus_words.json  # Word-level timing (JSON only)
```

## Troubleshooting

- **OOM errors**: Script auto-retries with smaller batch sizes (32 -> 4 -> 1)
- **CPU mode**: Use `--force-cpu` if GPU unavailable
- **Diarization needs HF_TOKEN**: Ensure `setup_env.sh` is sourced
