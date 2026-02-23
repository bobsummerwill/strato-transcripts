# Transcribe Audio

Transcribe audio files using local WhisperX (GPU) or cloud services (AssemblyAI, Replicate).

## Usage

```
/transcribe <audio_file> [options]
```

## Arguments

- `<audio_file>` - Path to audio file (mp3, wav, m4a, etc.)
- `--transcribers` - Comma-separated list: whisperx, assemblyai, whisperx-cloud (default: whisperx)
- `--force` - Reprocess even if output exists
- `--force-cpu` - Force CPU mode for WhisperX (slower)

## Instructions

When the user invokes this command:

1. **Validate the audio file exists** at the specified path

2. **Check environment setup**:
   ```bash
   source setup_env.sh && echo "Environment loaded"
   ```

3. **Run transcription**:
   ```bash
   python3 scripts/process_single_transcribe_and_diarize.py <audio_file> --transcribers <transcribers>
   ```

4. **Report results**:
   - Output: `intermediates/<episode>/<episode>_<transcriber>.md`

## Examples

```bash
# Local GPU transcription
/transcribe episode001.mp3

# Cloud transcription
/transcribe episode001.mp3 --transcribers assemblyai

# Multiple transcribers
/transcribe episode001.mp3 --transcribers whisperx,assemblyai

# Force reprocess
/transcribe episode001.mp3 --force
```

## Output Structure

```
intermediates/episode001/
  episode001_whisperx.md         # Markdown with timestamps
  episode001_assemblyai.md
```

## Troubleshooting

- **OOM errors**: Script auto-retries with smaller batch sizes (32 -> 4 -> 1)
- **CPU mode**: Use `--force-cpu` if GPU unavailable
- **Diarization needs HF_TOKEN**: Ensure `setup_env.sh` is sourced
