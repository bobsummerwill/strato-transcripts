# Video Caption

Generate captioned videos with burned-in subtitles from transcripts.

## Usage

```
/video-caption <video.mp4> [options]
```

## Arguments

- `<video.mp4>` - Input video file
- `--transcriber <name>` - Transcription service (default: whisperx)
  - Options: whisperx, whisperx-cloud, assemblyai
- `--processor <name>` - AI post-processor for transcript cleanup (optional)
  - Options: opus, gemini, deepseek, chatgpt, grok, etc.
- `--title <text>` - Title overlay at top of screen
- `--force-cpu` - Force CPU mode for WhisperX

## Instructions

When the user invokes this command:

1. **Validate video file exists**

2. **Run full pipeline**:
   ```bash
   source setup_env.sh
   ./scripts/process_video.sh <video.mp4> [options]
   ```

3. **Report results**:
   - Audio extracted: `<video>.mp3`
   - Transcript: `intermediates/<video>/<video>_<transcriber>.md`
   - Subtitles: `intermediates/<video>/<video>_<transcriber>.srt` and `.ass`
   - Captioned video: `<video>_captioned.mp4`

## Examples

```bash
# Basic captioning with WhisperX
/video-caption episode007.mp4

# With AI post-processing for better transcript
/video-caption episode007.mp4 --transcriber whisperx --processor opus

# With title overlay
/video-caption episode007.mp4 --title "Episode 7 - Jacob Czepluch"

# Using AssemblyAI for transcription
/video-caption episode007.mp4 --transcriber assemblyai --processor opus
```

## Pipeline Steps

1. **Extract Audio** - FFmpeg extracts MP3 from MP4
2. **Transcribe** - WhisperX/AssemblyAI with speaker diarization
3. **Post-Process** (optional) - AI fixes technical terms, names
4. **Generate Subtitles** - Convert to SRT/ASS with speaker colors
5. **Burn Subtitles** - FFmpeg renders subtitles into video

## Subtitle Features

- **Color-coded speakers** - Each speaker gets a unique color
- **Speaker names** - Auto-detected from conversation context
- **Word corrections** - Common names/terms auto-corrected
- **ASS format** - Rich styling with ffmpeg-compatible colors

## Speaker Colors

| Speaker | Color |
|---------|-------|
| Speaker 1 | Blue |
| Speaker 2 | Orange |
| Speaker 3 | Red |
| Speaker 4 | Green |
| Speaker 5+ | Purple, Yellow, etc. |

## Output Files

```
<video_dir>/
  episode007.mp4           # Original
  episode007.mp3           # Extracted audio
  episode007_captioned.mp4 # Final output

intermediates/episode007/
  episode007_whisperx.md   # Transcript
  episode007_whisperx.srt  # SRT subtitles
  episode007_whisperx.ass  # ASS subtitles (with colors)
```

## Requirements

- FFmpeg installed (`sudo apt install ffmpeg`)
- Virtual environment setup (auto-detected)
- HF_TOKEN for diarization (local WhisperX only)
- ASSEMBLYAI_API_KEY for cloud transcription
- OPENROUTER_API_KEY for post-processing (if using --processor)

## Auto-Detection

The script auto-detects the correct virtual environment:
```bash
./scripts/process_video.sh video.mp4  # Auto-selects venv
```

Priority order: venv-nvidia > venv-amd > venv-intel > venv-cpu

## Batch Processing

Process multiple videos:
```bash
./scripts/process_all_videos.sh /path/to/videos/
```

## Three Independent Pipelines

This project has three pipelines that don't interfere with each other:

| Pipeline | Output Pattern | Use Case |
|----------|----------------|----------|
| **1. Original** | `{episode}_{transcriber}_{processor}.md` | Quick single-model output |
| **2. Video Caption** | `{episode}_{transcriber}.srt/.ass` | Burned-in subtitles |
| **3. AI Consensus** | `{episode}_final.md` | Premium 11-model consensus |

All pipelines can run on the same episode without conflicts.
