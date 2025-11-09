#!/usr/bin/env python3
"""
Extract people names from EarlyDaysOfEthereum project
Creates a comprehensive list of Ethereum ecosystem contributors
"""

import os
import re
from pathlib import Path
from collections import Counter

def extract_from_people_directory():
    """Extract names from _people directory filenames and YAML frontmatter"""
    people_dir = Path("../EarlyDaysOfEthereum/source/_people")
    
    if not people_dir.exists():
        print(f"Warning: {people_dir} not found")
        print("Make sure EarlyDaysOfEthereum is cloned in the parent directory")
        return []
    
    names = []
    
    for md_file in people_dir.glob("*.md"):
        # Extract name from filename (e.g., "vitalik-buterin.md" -> "Vitalik Buterin")
        name = md_file.stem.replace("-", " ").title()
        names.append(name)
        
        # Also try to extract from YAML frontmatter
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Look for name: field in YAML
                name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
                if name_match:
                    yaml_name = name_match.group(1).strip().strip('"\'')
                    if yaml_name and yaml_name not in names:
                        names.append(yaml_name)
        except Exception as e:
            print(f"Warning: Could not parse {md_file}: {e}")
    
    return names

def extract_from_articles():
    """Extract frequently mentioned names from articles"""
    articles_dir = Path("../EarlyDaysOfEthereum/source/_articles")
    
    if not articles_dir.exists():
        print(f"Warning: {articles_dir} not found")
        return []
    
    # Pattern to match capitalized names (at least 2 words)
    name_pattern = re.compile(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b')
    
    all_names = []
    
    for md_file in articles_dir.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Find all potential names
                matches = name_pattern.findall(content)
                all_names.extend(matches)
        except Exception as e:
            print(f"Warning: Could not parse {md_file}: {e}")
    
    # Count frequency and filter (keep names that appear at least 3 times)
    name_counts = Counter(all_names)
    frequent_names = [name for name, count in name_counts.items() if count >= 3]
    
    return frequent_names

def extract_from_local_transcripts():
    """Extract speaker names from existing transcripts"""
    outputs_dir = Path("outputs")
    
    if not outputs_dir.exists():
        return []
    
    names = []
    
    # Look for people mentioned in filenames
    for txt_file in outputs_dir.glob("*_transcript_with_speakers.txt"):
        # Extract from filename (e.g., "alex-van-de-sande-interview")
        filename = txt_file.stem.replace("_transcript_with_speakers", "")
        
        # Split by common separators
        parts = re.split(r'[-_]', filename)
        
        # Look for interview/episode patterns
        if 'interview' in parts:
            idx = parts.index('interview')
            if idx > 0:
                name_parts = parts[:idx]
                name = ' '.join(name_parts).title()
                if name and len(name) > 3:
                    names.append(name)
    
    return names

def main():
    print("="*60)
    print("Ethereum People Name Extractor")
    print("="*60)
    
    # Extract from various sources
    print("\n1. Extracting from _people directory...")
    people_names = extract_from_people_directory()
    print(f"   Found {len(people_names)} names")
    
    print("\n2. Extracting from articles...")
    article_names = extract_from_articles()
    print(f"   Found {len(article_names)} frequent names")
    
    print("\n3. Extracting from local transcripts...")
    transcript_names = extract_from_local_transcripts()
    print(f"   Found {len(transcript_names)} names")
    
    # Combine and deduplicate
    all_names = set(people_names + article_names + transcript_names)
    
    # Sort alphabetically
    sorted_names = sorted(all_names)
    
    # Save to file
    output_file = Path("intermediates/ethereum_people.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        for name in sorted_names:
            f.write(f"{name}\n")
    
    print(f"\n✓ Saved {len(sorted_names)} unique names to {output_file}")
    
    # Show top 20 as preview
    print("\nPreview (first 20 names):")
    for name in sorted_names[:20]:
        print(f"  - {name}")
    
    if len(sorted_names) > 20:
        print(f"  ... and {len(sorted_names) - 20} more")

if __name__ == "__main__":
    main()
