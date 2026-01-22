# Video Processing Instructions

## Adding Cover Image Intro/Outro with Crossfades

This adds a static cover image at the beginning and end of a video with smooth crossfade transitions.

### Prerequisites

- ffmpeg installed
- Cover image matching video dimensions (e.g., 1280x720 for 720p video)
- Source video file

### Command

```bash
ffmpeg -y \
  -loop 1 -t 4 -framerate 30 -i "COVER_IMAGE.png" \
  -i "INPUT_VIDEO.mp4" \
  -loop 1 -t 4 -framerate 30 -i "COVER_IMAGE.png" \
  -filter_complex "[0:v]format=yuv420p,settb=AVTB[intro];[1:v]format=yuv420p,fps=30,settb=AVTB[main];[2:v]format=yuv420p,settb=AVTB[outro];[intro][main]xfade=transition=fade:duration=1:offset=3[v1];[v1][outro]xfade=transition=fade:duration=1:offset=VIDEO_DURATION_PLUS_3[vout];[1:a]adelay=3000|3000,apad=pad_dur=3[aout]" \
  -map "[vout]" -map "[aout]" \
  -c:v libx264 -preset medium -crf 18 \
  -c:a aac -b:a 192k \
  "OUTPUT_VIDEO.mp4"
```

### Parameters to Adjust

1. **COVER_IMAGE.png** - Path to your cover image
2. **INPUT_VIDEO.mp4** - Path to your source video
3. **OUTPUT_VIDEO.mp4** - Path for the output file
4. **VIDEO_DURATION_PLUS_3** - Original video duration in seconds + 3 (for the intro offset)
5. **framerate 30** - Match your video's frame rate
6. **duration=1** - Crossfade duration (1 second)
7. **offset=3** - When crossfade starts (3 seconds = after 3s of cover display)

### Getting Video Duration

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 INPUT_VIDEO.mp4
```

### Example

For a video with duration 5386.254333 seconds:

```bash
ffmpeg -y \
  -loop 1 -t 4 -framerate 30 -i "/path/to/cover.png" \
  -i "episode010-viktortron.mp4" \
  -loop 1 -t 4 -framerate 30 -i "/path/to/cover.png" \
  -filter_complex "[0:v]format=yuv420p,settb=AVTB[intro];[1:v]format=yuv420p,fps=30,settb=AVTB[main];[2:v]format=yuv420p,settb=AVTB[outro];[intro][main]xfade=transition=fade:duration=1:offset=3[v1];[v1][outro]xfade=transition=fade:duration=1:offset=5389.254333[vout];[1:a]adelay=3000|3000,apad=pad_dur=3[aout]" \
  -map "[vout]" -map "[aout]" \
  -c:v libx264 -preset medium -crf 18 \
  -c:a aac -b:a 192k \
  "episode010-viktortron-with-covers.mp4"
```

### Filter Explanation

- `-loop 1 -t 4` - Loop the image for 4 seconds (3s visible + 1s crossfade)
- `settb=AVTB` - Normalize timebase to avoid xfade errors
- `xfade=transition=fade:duration=1:offset=3` - 1-second fade starting at 3 seconds
- `adelay=3000|3000` - Delay audio by 3 seconds (3000ms per channel)
- `apad=pad_dur=3` - Pad 3 seconds of silence at the end

---

## Extracting Audio from Video

### Check Source Audio Bitrate

First, check what bitrate the reference audio files use:

```bash
ffprobe -v error -show_entries stream=bit_rate -of default=noprint_wrappers=1 REFERENCE.mp3
```

### Extract MP3 at Matching Quality

```bash
ffmpeg -y -i "INPUT_VIDEO.mp4" -vn -c:a libmp3lame -b:a 128k "OUTPUT.mp3"
```

### Parameters

- `-vn` - No video (audio only)
- `-c:a libmp3lame` - Use LAME MP3 encoder
- `-b:a 128k` - Bitrate (use 128k to match existing files in this project)

### Example

```bash
ffmpeg -y -i "episode010-viktortron-with-covers.mp4" -vn -c:a libmp3lame -b:a 128k "episode010-viktortron-with-covers.mp3"
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Get video duration | `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 VIDEO.mp4` |
| Get video dimensions | `ffprobe -v error -show_entries stream=width,height -of csv=s=x:p=0 VIDEO.mp4` |
| Get video framerate | `ffprobe -v error -show_entries stream=r_frame_rate -of default=noprint_wrappers=1:nokey=1 VIDEO.mp4` |
| Get audio bitrate | `ffprobe -v error -show_entries stream=bit_rate -of default=noprint_wrappers=1 AUDIO.mp3` |
