#!/usr/bin/env python3

def convert_seconds_to_mmss(seconds_decimal):
    """Convert decimal seconds to MM:SS format"""
    try:
        total_seconds = float(seconds_decimal)
        minutes = int(total_seconds // 60)
        seconds = int(round(total_seconds % 60))
        if seconds == 60:  # handle rounding up to 60 seconds
            minutes += 1
            seconds = 0
        return f"{minutes:02d}:{seconds:02d}"
    except (ValueError, TypeError):
        return "00:00"

def main():
    with open('outputs/episode006-christoph-jentzsch_combined.md', 'r') as f:
        content = f.read()

    # Replace all timestamp patterns [Xs.Ys] with [MM:SS]
    import re

    def replace_timestamp(match):
        seconds_str = match.group(1)
        mmss = convert_seconds_to_mmss(seconds_str)
        return f"[{mmss}]"

    # Pattern to match [digits.digits]s]
    pattern = r'\[([0-9]+\.[0-9]+)s\]'
    new_content = re.sub(pattern, replace_timestamp, content)

    with open('outputs/episode006-christoph-jentzsch_combined.md', 'w') as f:
        f.write(new_content)

    print("Timestamps converted successfully")

if __name__ == "__main__":
    main()
