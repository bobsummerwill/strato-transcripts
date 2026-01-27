#!/usr/bin/env python3
"""
Convert WhisperX markdown transcript to SRT subtitle format.
Automatically detects speaker names from conversation context.
"""

import sys
import re
import json
from pathlib import Path

# Word corrections for common transcription errors
WORD_CORRECTIONS = {
    # Name corrections
    'samuel': 'Summerwill',
    'Samuel': 'Summerwill',
    'jakob': 'Jacob',
    'Jakob': 'Jacob',
    'vitalic': 'Vitalik',
    'Vitalic': 'Vitalik',
    'gavin would': 'Gavin Wood',
    'Gavin Would': 'Gavin Wood',
    'buterin': 'Buterin',
    'wilke': 'Wilcke',
    'Wilke': 'Wilcke',
    'lubin': 'Lubin',
    'hoskinson': 'Hoskinson',
    'di iorio': 'Di Iorio',
    'alisie': 'Alisie',
    'tual': 'Tual',
    'steiner': 'Steiner',
    # Project/event corrections
    'defcon': 'DevCon',
    'Defcon': 'DevCon',
    'def con': 'DevCon',
    'devcon': 'DevCon',
    'Devcon': 'DevCon',
    'etherium': 'Ethereum',
    'Etherium': 'Ethereum',
    'etheriam': 'Ethereum',
    'Etheriam': 'Ethereum',
    # Programming languages
    'c plus plus': 'C++',
    'c++': 'C++',
    'c plus': 'C++',
    'c sharp': 'C#',
    'csharp': 'C#',
    'javascript': 'JavaScript',
    'Javascript': 'JavaScript',
    'typescript': 'TypeScript',
    'Typescript': 'TypeScript',
    'golang': 'Go',
    'Golang': 'Go',
    'python': 'Python',
    'solidity': 'Solidity',
    'Solidity': 'Solidity',
    'rust': 'Rust',
    'vyper': 'Vyper',
    'Vyper': 'Vyper',
}

# Speaker colors in BGR format for ASS/SSA subtitles (ffmpeg compatible)
SPEAKER_COLORS = [
    ("blue", "FF0000"),
    ("orange", "00A5FF"),
    ("red", "0000FF"),
    ("green", "00FF00"),
    ("purple", "800080"),
    ("yellow", "00FFFF"),
    ("white", "FFFFFF"),
    ("grey", "808080"),
    ("teal", "808000"),
    ("lilac", "C8A2C8"),
    ("maroon", "000080"),
    ("rose", "7F00FF"),
    ("baby blue", "F0CF89"),
    ("burgundy", "200080"),
    ("violet", "EE82EE"),
    ("pink", "CBC0FF"),
    ("black", "000000"),
    ("turquoise", "D0E040"),
    ("beige", "DCF5F5"),
    ("brown", "2A2AA5"),
    ("gold", "00D7FF"),
]


def load_known_names(names_file):
    """Load known names from file."""
    names = set()
    # Common spelling variations
    variations = {
        'Jacob': 'Jakob',
        'Viktor': 'Victor',
        'Péter': 'Peter',
        'Paweł': 'Pawel',
        'Zsolt': 'Zoltan',
    }
    if names_file.exists():
        with open(names_file, 'r') as f:
            for line in f:
                name = line.strip()
                if name:
                    names.add(name)
                    # Also add first name only
                    first_name = name.split()[0]
                    if len(first_name) > 2:  # Avoid initials
                        names.add(first_name)
                        # Add spelling variations
                        for orig, var in variations.items():
                            if first_name == orig:
                                names.add(var)
                            elif first_name == var:
                                names.add(orig)
    return names


def identify_speakers(segments, known_names):
    """
    Identify speaker names from conversation context.

    Patterns detected:
    - "Hello, [Name]" / "Hi, [Name]" - the OTHER speaker is Name
    - "I'm [Name]" / "My name is [Name]" / "I am [Name]" - THIS speaker is Name
    - "I have here [Name]" / "This is [Name]" - the OTHER speaker is Name
    """
    speaker_names = {}
    all_speakers = set(seg['speaker'] for seg in segments)

    # Build patterns for known names (case insensitive matching)
    name_pattern = '|'.join(re.escape(name) for name in sorted(known_names, key=len, reverse=True))

    for i, segment in enumerate(segments):
        speaker = segment['speaker']
        text = segment['text']

        # Pattern: "I'm [Name]" or "I am [Name]" or "My name is [Name]"
        self_intro = re.search(
            rf"(?:I'm|I am|my name is|this is|I'm)\s+({name_pattern})",
            text, re.IGNORECASE
        )
        if self_intro:
            name = self_intro.group(1)
            # Find the canonical form from known_names
            for known in known_names:
                if known.lower() == name.lower() or known.lower().startswith(name.lower()):
                    speaker_names[speaker] = known
                    break
            else:
                speaker_names[speaker] = name.title()

        # Pattern: "Hello, [Name]" or "Hi, [Name]" - other speaker is Name
        greeting = re.search(
            rf"(?:Hello|Hi|Hey),?\s+({name_pattern})",
            text, re.IGNORECASE
        )
        if greeting:
            name = greeting.group(1)
            # Find other speaker(s)
            other_speakers = [s for s in all_speakers if s != speaker]
            if other_speakers:
                other = other_speakers[0]  # Assume 2-person conversation
                for known in known_names:
                    if known.lower() == name.lower() or known.lower().startswith(name.lower()):
                        speaker_names[other] = known
                        break
                else:
                    speaker_names[other] = name.title()

        # Pattern: "I have here [Name]" or "joining me is [Name]"
        intro_other = re.search(
            rf"(?:I have here|have here|joining (?:me|us) is|with me is|here is|here's)\s+({name_pattern})",
            text, re.IGNORECASE
        )
        if intro_other:
            name = intro_other.group(1)
            other_speakers = [s for s in all_speakers if s != speaker]
            if other_speakers:
                other = other_speakers[0]
                for known in known_names:
                    if known.lower() == name.lower() or known.lower().startswith(name.lower()):
                        speaker_names[other] = known
                        break
                else:
                    speaker_names[other] = name.title()

    # Second pass: look for any mentioned names that could identify unknown speakers
    for segment in segments:
        speaker = segment['speaker']
        text = segment['text']

        # Look for names mentioned as subjects being addressed or referred to
        # "And I have here Jakob" style (more flexible)
        flex_intro = re.search(r"(?:have here|here is|here's|this is|meet)\s+(\w+)", text, re.IGNORECASE)
        if flex_intro and speaker in speaker_names:
            potential_name = flex_intro.group(1)
            other_speakers = [s for s in all_speakers if s != speaker and s not in speaker_names]
            if other_speakers:
                other = other_speakers[0]
                # Try to match to known names with flexible matching
                for known in known_names:
                    known_first = known.split()[0].lower()
                    if (potential_name.lower() == known_first or
                        potential_name.lower().replace('k', 'c') == known_first or
                        potential_name.lower().replace('c', 'k') == known_first):
                        speaker_names[other] = known
                        break
                else:
                    # Use the name as-is if no match found
                    if potential_name[0].isupper() and len(potential_name) > 2:
                        speaker_names[other] = potential_name

    # Print detected names
    if speaker_names:
        print(f"Detected speaker names:")
        for spk, name in sorted(speaker_names.items()):
            print(f"  {spk} -> {name}")

    return speaker_names


def apply_word_corrections(word_timing):
    """Apply word corrections to timing data."""
    corrected = []
    for word_data in word_timing:
        text = word_data['text']
        # Strip punctuation for matching
        text_clean = text.rstrip('.,!?;:')
        punct = text[len(text_clean):]

        # Check for corrections
        if text_clean in WORD_CORRECTIONS:
            text = WORD_CORRECTIONS[text_clean] + punct
        elif text_clean.lower() in WORD_CORRECTIONS:
            text = WORD_CORRECTIONS[text_clean.lower()] + punct

        corrected.append({
            **word_data,
            'text': text
        })
    return corrected


def load_word_timing(filepath):
    """Load word-level timing JSON if available."""
    # Extract base name (e.g., "videoplayback" from "videoplayback_assemblyai_opus.md")
    base_name = filepath.stem.split('_')[0]

    # Find project root
    project_root = filepath.parent
    while project_root != project_root.parent:
        if (project_root / 'intermediates').exists():
            break
        project_root = project_root.parent

    # Look for word timing JSON in intermediates directory
    json_patterns = [
        project_root / 'intermediates' / base_name / f"{base_name}_assemblyai_words.json",
        project_root / 'intermediates' / base_name / f"{base_name}_whisperx_words.json",
        filepath.parent / f"{filepath.stem.replace('_opus', '').replace('_gemini', '').replace('_deepseek', '').replace('_chatgpt', '')}_words.json",
    ]

    for json_path in json_patterns:
        if json_path.exists():
            print(f"Found word-level timing: {json_path}")
            with open(json_path, 'r') as f:
                word_timing = json.load(f)
            # Apply corrections
            word_timing = apply_word_corrections(word_timing)
            return word_timing

    return None


def parse_transcript(filepath):
    """Parse markdown transcript and extract timed segments."""
    segments = []

    with open(filepath, 'r') as f:
        content = f.read()

    # Pattern: **[MM:SS] SPEAKER:** text or **[H:MM:SS] SPEAKER:** text
    pattern = r'\*\*\[(\d+:?\d*:\d+)\]\s*([^:]+):\*\*\s*(.+?)(?=\*\*\[|\Z)'

    matches = re.findall(pattern, content, re.DOTALL)

    for timestamp, speaker, text in matches:
        # Parse timestamp to seconds
        parts = timestamp.split(':')
        if len(parts) == 2:
            seconds = int(parts[0]) * 60 + int(parts[1])
        else:
            seconds = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])

        # Clean up text
        text = ' '.join(text.split())

        segments.append({
            'start': seconds,
            'speaker': speaker.strip(),
            'text': text
        })

    return segments


def format_srt_time(seconds):
    """Format seconds to SRT timestamp format: HH:MM:SS,mmm"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def split_text_to_lines(text, max_chars=42):
    """Split text into subtitle-friendly lines."""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 > max_chars and current_line:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word) + 1

    if current_line:
        lines.append(' '.join(current_line))

    return lines


def split_into_sentences(text):
    """Split text into sentences, keeping punctuation."""
    # Split on sentence-ending punctuation, keeping the delimiter
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Filter out empty strings and strip whitespace
    return [s.strip() for s in sentences if s.strip()]


def segments_to_srt(segments, speaker_names, word_timing=None, max_duration=8.0, chars_per_second=18):
    """Convert segments to ASS format with word-by-word timing synced to speech."""
    srt_entries = []
    index = 1

    # Assign colors to speakers based on order of appearance
    speaker_color_map = {}
    color_index = 0

    # If we have word-level timing, use it directly
    if word_timing:
        print("Using precise word-level timing from transcription")

        # Build speaker color map from word timing
        for word_data in word_timing:
            speaker_id = word_data.get('speaker') or 'SPEAKER_00'
            if speaker_id not in speaker_color_map:
                color_name, color_code = SPEAKER_COLORS[color_index % len(SPEAKER_COLORS)]
                speaker_color_map[speaker_id] = color_code
                full_name = speaker_names.get(speaker_id, speaker_id)
                speaker = full_name.split()[0] if ' ' in full_name else full_name
                print(f"  {speaker} -> {color_name}")
                color_index += 1

        # Create entries from word timing
        for word_data in word_timing:
            speaker_id = word_data.get('speaker') or 'SPEAKER_00'
            color = speaker_color_map[speaker_id]
            style_name = f"Speaker{speaker_id.replace('SPEAKER_', '')}"

            srt_entries.append({
                'index': index,
                'start': word_data['start'],
                'end': word_data['end'],
                'text': word_data['text'],
                'style': style_name,
                'color': color
            })
            index += 1

        return srt_entries, speaker_color_map

    # Fall back to proportional timing from segments
    print("Using estimated timing (no word-level data available)")

    for i, segment in enumerate(segments):
        start_time = segment['start']
        text = segment['text']
        speaker_id = segment['speaker']

        # Use detected name or fall back to speaker ID (first name only)
        full_name = speaker_names.get(speaker_id, speaker_id)
        speaker = full_name.split()[0] if ' ' in full_name else full_name

        # Assign color to speaker if not already assigned
        if speaker_id not in speaker_color_map:
            color_name, color_code = SPEAKER_COLORS[color_index % len(SPEAKER_COLORS)]
            speaker_color_map[speaker_id] = color_code
            print(f"  {speaker} -> {color_name}")
            color_index += 1

        color = speaker_color_map[speaker_id]
        style_name = f"Speaker{speaker_id.replace('SPEAKER_', '')}"

        # Calculate end time based on next segment
        if i + 1 < len(segments):
            next_start = segments[i + 1]['start']
            segment_end = next_start
        else:
            # Estimate based on text length for last segment
            segment_end = start_time + len(text) / chars_per_second

        # Split text into words
        words = text.split()

        if not words:
            continue

        # Calculate total character count for proportional timing
        total_chars = sum(len(w) for w in words)
        segment_duration = segment_end - start_time

        current_time = start_time

        for word in words:
            # Proportional timing based on word length
            word_ratio = len(word) / total_chars if total_chars > 0 else 1 / len(words)
            word_duration = segment_duration * word_ratio

            # Minimum display time
            word_duration = max(word_duration, 0.08)

            end_time = current_time + word_duration

            # Just the word, color applied via style
            subtitle_text = word

            srt_entries.append({
                'index': index,
                'start': current_time,
                'end': end_time,
                'text': subtitle_text,
                'style': style_name,
                'color': color
            })

            index += 1
            current_time = end_time

    return srt_entries, speaker_color_map


def write_srt(entries, output_path):
    """Write SRT entries to file with ASS color tags."""
    with open(output_path, 'w') as f:
        for entry in entries:
            f.write(f"{entry['index']}\n")
            f.write(f"{format_srt_time(entry['start'])} --> {format_srt_time(entry['end'])}\n")
            # Add ASS color tag for SRT fallback
            color = entry.get('color', 'FFFFFF')
            f.write(f"{{\\c&H{color}&}}{entry['text']}\n")
            f.write("\n")


def format_ass_time(seconds):
    """Format seconds to ASS timestamp format: H:MM:SS.cc"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centis = int((seconds % 1) * 100)
    return f"{hours}:{minutes:02d}:{secs:02d}.{centis:02d}"


def write_ass(entries, output_path, speaker_colors, title=None):
    """Write ASS subtitle file with colored text and optional title overlay."""
    # Get video duration from last entry
    video_duration = max(e['end'] for e in entries) if entries else 3600

    with open(output_path, 'w') as f:
        # ASS header
        f.write("[Script Info]\n")
        f.write("Title: Transcript\n")
        f.write("ScriptType: v4.00+\n")
        f.write("PlayResX: 1920\n")
        f.write("PlayResY: 1080\n")
        f.write("\n")

        # Styles - create one style per speaker color
        f.write("[V4+ Styles]\n")
        f.write("Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n")

        # Title style - top of screen, white text, smaller font
        # Alignment 8 = top center
        f.write("Style: Title,Arial,48,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,3,2,8,10,10,20,1\n")

        for speaker_id, color in speaker_colors.items():
            # Color format for ASS is &HAABBGGRR (alpha, blue, green, red)
            style_name = f"Speaker{speaker_id.replace('SPEAKER_', '')}"
            f.write(f"Style: {style_name},Arial,72,&H00{color},&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,4,2,2,10,10,50,1\n")

        f.write("\n")

        # Events
        f.write("[Events]\n")
        f.write("Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")

        # Add persistent title overlay if provided
        if title:
            end_time = format_ass_time(video_duration)
            f.write(f"Dialogue: 1,0:00:00.00,{end_time},Title,,0,0,0,,{title}\n")

        for entry in entries:
            start = format_ass_time(entry['start'])
            end = format_ass_time(entry['end'])
            style = entry.get('style', 'Default')
            text = entry['text']
            f.write(f"Dialogue: 0,{start},{end},{style},,0,0,0,,{text}\n")


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Convert transcript to subtitles')
    parser.add_argument('input', help='Input transcript file (.md)')
    parser.add_argument('output', nargs='?', help='Output subtitle file (.srt)')
    parser.add_argument('--title', help='Title overlay text (shown at top of screen)')
    args = parser.parse_args()

    input_path = Path(args.input)

    # Find project root (where intermediates folder is)
    project_root = input_path.parent
    while project_root != project_root.parent:
        if (project_root / 'intermediates').exists():
            break
        project_root = project_root.parent

    # Load known names
    names_file = project_root / 'intermediates' / 'ethereum_people.txt'
    known_names = load_known_names(names_file)
    print(f"Loaded {len(known_names)} known names")

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix('.srt')

    print(f"Converting: {input_path}")

    segments = parse_transcript(input_path)
    print(f"Found {len(segments)} speaker segments")

    # Identify speaker names from context
    speaker_names = identify_speakers(segments, known_names)

    # Try to load word-level timing for precise alignment
    word_timing = load_word_timing(input_path)

    srt_entries, speaker_colors = segments_to_srt(segments, speaker_names, word_timing)
    print(f"Generated {len(srt_entries)} subtitle entries")

    # Write ASS format for proper color support
    ass_output = output_path.with_suffix('.ass')
    write_ass(srt_entries, ass_output, speaker_colors, title=args.title)
    print(f"Saved: {ass_output}")
    if args.title:
        print(f"Title overlay: {args.title}")

    # Also write SRT for compatibility
    write_srt(srt_entries, output_path)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
