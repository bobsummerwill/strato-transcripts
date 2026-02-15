# YouTube Download

Download YouTube videos as MP4 files into the project root directory.

## Usage

```
/youtube-download <url> <output_name>
```

## Arguments

- `<url>` - YouTube video URL (e.g., `https://www.youtube.com/watch?v=...`)
- `<output_name>` - Output filename without extension (e.g., `devcon1-christoph-jentzsch-slockit`)

## Instructions

When the user invokes this command:

1. **Ensure yt-dlp is available and up to date**:
   ```bash
   # Check for latest binary at /tmp/yt-dlp first, fall back to system
   if [ -x /tmp/yt-dlp ]; then
     YT_DLP=/tmp/yt-dlp
   elif command -v yt-dlp &>/dev/null; then
     YT_DLP=$(command -v yt-dlp)
   else
     echo "yt-dlp not found, downloading..."
     curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /tmp/yt-dlp
     chmod +x /tmp/yt-dlp
     YT_DLP=/tmp/yt-dlp
   fi
   $YT_DLP --version
   ```

2. **If yt-dlp version is older than 90 days**, update it:
   ```bash
   curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /tmp/yt-dlp
   chmod +x /tmp/yt-dlp
   YT_DLP=/tmp/yt-dlp
   ```

3. **Download the video as MP4**:
   ```bash
   $YT_DLP -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
     --no-part \
     -o "<project_root>/<output_name>.mp4" \
     "<url>"
   ```
   The `--no-part` flag prevents yt-dlp from creating `.part` and `.ytdl` temp files.

4. **Verify the download**:
   ```bash
   ls -lh <project_root>/<output_name>.mp4
   ```

5. **Report results**:
   - File path and size
   - Note that the file is `.gitignore`d (large binary) and should not be committed

## Examples

```bash
# Download a DevCon talk
/youtube-download https://www.youtube.com/watch?v=uy6P5_WQoUI devcon1-christoph-jentzsch-slockit

# Download an episode
/youtube-download https://www.youtube.com/watch?v=abc123 episode015-guest-name
```

## Troubleshooting

- **403 Forbidden**: yt-dlp is likely outdated. Download the latest binary to `/tmp/yt-dlp`
- **Missing JS runtime warning**: Can be ignored; yt-dlp falls back to other extraction methods
- **Merge required**: yt-dlp automatically merges separate video+audio streams using ffmpeg
- **venv interference**: If pip install fails due to active venv, download the binary directly instead
