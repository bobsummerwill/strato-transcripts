# STRATO Mercata Website

The official website for STRATO Mercata - a platform to easily earn on vaulted gold, silver & crypto with instant credit. Built by Ethereum veterans.

## About This Project

**STRATO Mercata** is a Jekyll-based static website that serves as the primary web presence for STRATO Mercata. The site features video content, team member profiles, and information about the platform's capabilities.

### What You'll Find Here

- **Team Profiles**: Biographies and profiles of STRATO Mercata team members
- **Video Content**: Show episodes, contest announcements, and platform demonstrations
- **Blog**: Platform updates, announcements, and educational content
- **Platform Information**: Details about trading, lending, and borrowing on real-world assets

---

## Jekyll Setup

This is a static site built with Jekyll 4.3+ and deployed via GitHub Pages.

### Project Structure

```
stratomercata-website/
├── _config.yml                # Jekyll configuration
├── Gemfile                    # Ruby dependencies
└── source/                    # Jekyll source directory
    ├── _layouts/              # Page templates (default, person, blog, video)
    ├── _includes/             # Reusable components (auto_link, embeds, SEO)
    ├── _blog/                 # Blog collection (Markdown files)
    ├── _people/               # People collection (Markdown files)
    ├── _videos/               # Video collection (Markdown files)
    ├── blog/index.html        # Blog listing page
    ├── people/index.html      # People listing page
    ├── videos/index.html      # Videos listing page
    ├── assets/css/            # Stylesheets
    ├── images/                # Image assets
    └── videos/raw-audio/      # Source audio files for transcription
```

### Configuration Philosophy

The `_config.yml` file contains production settings:
- **`baseurl: ""`**: Empty for custom domain at root
- **`url: "https://stratomercata.com"`**: Production domain

For local development, Jekyll's `serve` command automatically overrides the `url` setting to `http://localhost:4000`.

---

## Local Development

### Prerequisites

- Ruby 3.3+ or Ruby 3.4+ (install via [rbenv](https://github.com/rbenv/rbenv) or [rvm](https://rvm.io/))
- Bundler: `gem install bundler`

**Note for Ruby 3.4+**: The `Gemfile` includes compatibility gems (`base64`, `logger`, `bigdecimal`) required for Jekyll 3.10.0 on Ruby 3.4+.

### Setup & Run

```bash
# Install dependencies
bundle install

# Clean, build, and serve with incremental builds
bundle exec jekyll clean && bundle exec jekyll serve --incremental

# Access at http://localhost:4000
```

The development server includes:
- **Auto-regeneration**: Changes to source files trigger automatic rebuilds
- **Incremental builds**: Only changed files are rebuilt (faster)
- **LiveReload**: Browser refreshes automatically when files change

---

## Collections

The site uses three Jekyll collections:

### Blog (`_blog/`)
Platform updates, announcements, and educational content about STRATO Mercata.

### People (`_people/`)
Team member profiles with photos, bios, and social links.

Example frontmatter:
```yaml
---
name: Bob Summerwill
role: Head of Ecosystem
photo: /images/bobsummerwill.com/2025.08.26/bob-summerwill.jpeg
twitter: bobsummerwill
linkedin: bob-summerwill
---
```

### Videos (`_videos/`)
Show episodes, contests, and platform demonstrations with embedded YouTube videos and transcripts.

Example frontmatter:
```yaml
---
title: "STRATO Mercata Show: State of Blockchain"
date: 2025-10-08
hosts: ["Bob Summerwill", "Victor Wong", "Kieren James-Lubin"]
description: "Reflections on TOKEN2049 in Singapore"
embed:
  url: https://www.youtube.com/embed/VIDEO_ID
---
```

---

## Workflow: Adding Video Content with Transcripts

### 1. Extract Audio from Video

Download the video from Streamyard/YouTube, then extract audio:

```bash
ffmpeg -i "video-file.mp4" -q:a 0 -map a "output-audio.mp3"
```

### 2. Transcribe with TurboScribe

1. Upload the audio file to [TurboScribe](https://turboscribe.ai)
2. Select **Whale Transcription** mode
3. Enable **Speaker Recognition** in settings
4. Set number of speakers (usually 2-3)
5. Click **Transcribe**

### 3. Save Audio File

Store the MP3 for future reference:
```
source/videos/raw-audio/show-name-YYYY-MM-DD.mp3
```

### 4. Create Video Page

Copy an existing video page as a template:

```bash
cp source/_videos/existing-video.md source/_videos/new-video-YYYY-MM-DD.md
```

Update the frontmatter with new details.

### 5. Add Transcript

1. Export transcript from TurboScribe as **TXT** with **Section Timestamps** enabled
2. Paste the content into the video page body
3. Transform speaker labels and timestamps

Example transformation:
```
[Speaker 1] (0:03 - 0:05)

becomes:

[[0:03]](https://www.youtube.com/watch?v=VIDEO_ID&t=3s) **Bob:**
```

Where `3s` is the starting timestamp in seconds.

### 6. Verify Locally

```bash
bundle exec jekyll clean && bundle exec jekyll serve --incremental
```

Visit http://localhost:4000/videos/ to verify the new video appears correctly.

---

## Deployment

### Netlify Deployment

Netlify provides zero-config Jekyll support with automatic PR preview deployments.

**Benefits:**
- Automatic PR preview deployments (each PR gets a unique preview URL)
- Faster build times
- Unlimited bandwidth on free tier
- Zero configuration needed (auto-detects Jekyll)

**Setup:**
1. Go to https://app.netlify.com
2. Click "Add new site" → "Import an existing project"
3. Choose GitHub and select your repository
4. Netlify auto-detects Jekyll settings
5. Click "Deploy site"

**PR Previews:**
- Enabled by default
- Each PR gets: `deploy-preview-{PR#}--{site}.netlify.app`
- Rebuilds automatically on every commit
- Preview URL posted as GitHub comment

**Ruby 3.4 Compatibility:**
The `Gemfile` includes all required compatibility gems for Netlify's Ruby 3.4 environment.

---

## Development Tips

### Auto-linking System

The site includes an auto-linking system (`source/_includes/auto_link.html`) that automatically converts mentions of people, blog posts, and videos to links:

```markdown
Bob Summerwill spoke about blockchain.
```

Automatically becomes:
```html
<a href="/people/bob-summerwill/">Bob Summerwill</a> spoke about blockchain.
```

The system processes content in priority order:
1. **Hidden People** - Removes/redacts links to hidden profiles
2. **Videos** - Links video titles to their pages
3. **Blog Posts** - Links blog post titles to their pages
4. **People** - Links person names (with conflict detection to avoid nested links)

### Relative URLs

Always use Jekyll's `relative_url` filter for internal links:

```liquid
[Link text]({{ '/people/bob-summerwill/' | relative_url }})
```

This ensures links work correctly in both local development and production.

### Image Paths

Images are organized by source and date:
```
source/images/bobsummerwill.com/2025.08.26/photo.jpeg
source/images/linkedin.com/2025.10.07/profile.png
source/images/stratomercata.com/2025.10.07/screenshot.png
```

Always use relative paths with the `relative_url` filter for images.

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

### Git Remote Setup

**Main repository:**
- `upstream` → https://github.com/stratomercata/stratomercata-website

**Your fork:**
- `origin` → https://github.com/YOUR_USERNAME/stratomercata-website

To sync your fork with upstream:
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0) - see the [LICENSE](LICENSE) file for details.

---

## Support

For questions or support:
- Open an [issue](https://github.com/stratomercata/stratomercata-website/issues)
- Contact [@bobsummerwill](https://x.com/bobsummerwill) on X/Twitter
- Visit [STRATO Mercata](https://www.stratomercata.com)
