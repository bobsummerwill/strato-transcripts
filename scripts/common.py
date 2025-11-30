#!/usr/bin/env python3
"""
Common utilities shared across transcription pipeline scripts.
Provides colors, formatters, validation, and file operations.
"""

import os
from pathlib import Path


# ============================================================================
# ANSI Color Codes and Formatters
# ============================================================================

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def success(msg):
    """Format success message with green checkmark."""
    return f"{Colors.GREEN}✓{Colors.RESET} {msg}"


def failure(msg):
    """Format failure message with red X."""
    return f"{Colors.RED}✗{Colors.RESET} {msg}"


def skip(msg):
    """Format skip message with yellow symbol."""
    return f"{Colors.YELLOW}⊘{Colors.RESET} {msg}"


# ============================================================================
# API Key Validation
# ============================================================================

def validate_api_key(env_var):
    """
    Validate API key. Returns (key, error_msg).
    
    Args:
        env_var: Environment variable name to check
    
    Returns:
        Tuple of (key, error_message). If key exists, error_message is None.
        If key missing, key is None and error_message describes the issue.
    """
    key = os.environ.get(env_var, '').strip()
    if not key:
        return None, f"{env_var} not set"
    return key, None


# ============================================================================
# Vocabulary Loading
# ============================================================================

def load_vocabulary():
    """
    Load Ethereum vocabulary from files.
    
    Returns:
        List of vocabulary terms (people names + technical terms)
    """
    vocab = []
    
    # Load technical terms
    terms_file = Path("intermediates/ethereum_technical_terms.txt")
    if terms_file.exists():
        with open(terms_file, 'r', encoding='utf-8') as f:
            vocab.extend([line.strip() for line in f if line.strip()])
    
    # Load people names
    people_file = Path("intermediates/ethereum_people.txt")
    if people_file.exists():
        with open(people_file, 'r', encoding='utf-8') as f:
            vocab.extend([line.strip() for line in f if line.strip()])
    
    return vocab


def load_people_list():
    """Load ethereum_people.txt, generating if needed."""
    people_file = Path("intermediates/ethereum_people.txt")
    
    # Generate if doesn't exist
    if not people_file.exists():
        extract_script = Path("scripts/extract_people.py")
        if extract_script.exists():
            import subprocess
            try:
                print("  Generating ethereum_people.txt...")
                subprocess.run(["python3", str(extract_script)], 
                             check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError:
                pass  # Silent failure
    
    if people_file.exists():
        with open(people_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    
    return []


def load_terms_list():
    """Load ethereum_technical_terms.txt, generating if needed."""
    terms_file = Path("intermediates/ethereum_technical_terms.txt")
    
    # Generate if doesn't exist
    if not terms_file.exists():
        extract_script = Path("scripts/extract_terms.py")
        if extract_script.exists():
            import subprocess
            try:
                print("  Generating ethereum_technical_terms.txt...")
                subprocess.run(["python3", str(extract_script)], 
                             check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError:
                pass  # Silent failure
    
    if terms_file.exists():
        with open(terms_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    
    return []


# ============================================================================
# GPU and Process Management
# ============================================================================

def cleanup_gpu_memory(force_cpu=False):
    """
    GPU memory cleanup to prevent CUDA OOM errors.
    Clears PyTorch cache and forces garbage collection.
    
    Args:
        force_cpu: If True, skip GPU-specific cleanup
    """
    import gc
    
    # Clear PyTorch GPU cache and force garbage collection
    if not force_cpu:
        try:
            import torch
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                torch.cuda.ipc_collect()
        except:
            pass
    
    # Python garbage collection
    gc.collect()


# ============================================================================
# File Saving Utilities
# ============================================================================

def save_transcript_dual_format(output_dir, basename, service_name, content, 
                                content_type="text"):
    """
    Save transcript in txt (clean) and md (with timestamps) formats.
    
    Args:
        output_dir: Directory to save files
        basename: Base filename without extension
        service_name: Name of service (whisperx, deepgram, etc.)
        content: Either pre-formatted text or list of segment dicts
        content_type: "text" or "segments"
    
    Returns:
        Path object for the .txt file
    """
    import re
    
    output_path = Path(output_dir) / f"{basename}_{service_name}_raw.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    if content_type == "text":
        # Pre-formatted text with timestamps
        # Save text version (NO timestamps)
        text_lines = []
        for line in content.split('\n'):
            clean_line = re.sub(r'^\[[\d.]+s\] ', '', line)
            text_lines.append(clean_line)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(text_lines))
        
        # Save markdown version (WITH timestamps, bold speaker labels)
        md_path = output_path.with_suffix('.md')
        md_lines = []
        for line in content.split('\n'):
            if re.match(r'^SPEAKER_\d+:', line):
                line = line.replace('SPEAKER_', '**SPEAKER_').replace(':', ':**', 1)
            md_lines.append(line)
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md_lines))
    
    elif content_type == "segments":
        # List of segment dicts with 'speaker', 'start', 'text' keys
        segments = content
        speaker_key = "speaker"
        
        # Save text version (NO timestamps)
        with open(output_path, 'w', encoding='utf-8') as f:
            current_speaker = None
            for segment in segments:
                speaker = segment.get(speaker_key, "UNKNOWN")
                if speaker != current_speaker:
                    f.write(f"\n{speaker}:\n")
                    current_speaker = speaker
                text = segment.get("text", "").strip()
                f.write(f"{text}\n")
        
        # Save markdown version (WITH timestamps)
        md_path = output_path.with_suffix('.md')
        with open(md_path, 'w', encoding='utf-8') as f:
            current_speaker = None
            for segment in segments:
                speaker = segment.get(speaker_key, "UNKNOWN")
                if speaker != current_speaker:
                    f.write(f"\n**{speaker}:**\n")
                    current_speaker = speaker
                start_time = segment.get("start", 0)
                text = segment.get("text", "").strip()
                f.write(f"[{start_time:.1f}s] {text}\n")
    
    return output_path
