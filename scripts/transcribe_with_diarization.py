#!/usr/bin/env python3
"""
Complete WhisperX transcription pipeline with speaker diarization

Uses int8 quantization for optimal VRAM usage while maintaining 98-99% quality.
Works efficiently on GPUs with 6GB+ VRAM (RTX 3060, 4060, 5070, etc.)
"""

import sys
import os
import time
import subprocess
import tempfile
import warnings
from pathlib import Path
import pandas as pd
import whisperx
import torch
from pyannote.audio import Pipeline

# Suppress pyannote's TF32 reproducibility warning (we re-enable TF32 ourselves)
warnings.filterwarnings('ignore', category=UserWarning, 
                       module='pyannote.audio.utils.reproducibility',
                       message='.*TensorFloat-32.*')

# Configure TF32 using PyTorch 2.9+ API
# Enables TensorFloat-32 for better performance on Ampere+ GPUs (RTX 30/40/50 series)
# NOTE: pyannote.audio disables TF32 on import, so we re-enable it after the import
torch.backends.cudnn.conv.fp32_precision = 'tf32'
torch.backends.cuda.matmul.fp32_precision = 'tf32'
# Also set old API for compatibility (pyannote checks this)
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

def transcribe_audio(audio_path, device, batch_size=None):
    """Run WhisperX transcription with float16 quantization - hardcoded to English and large-v3
    
    Args:
        audio_path: Path to audio file
        device: Device to use (cuda/cpu)
        batch_size: Batch size (auto-determined if None)
    """
    # Always use large-v3 for best accuracy (~10% better than large-v2)
    model_name = "large-v3"
    print("\n" + "="*60)
    print("Step 1: Transcribing audio with WhisperX...")
    print("="*60)
    
    # Use float16 instead of int8 to avoid TF32 conflicts with pyannote.audio
    # float16 provides excellent quality with low VRAM usage (~6GB for large-v3)
    compute_type = "float16" if device == "cuda" else "int8"
    
    # Auto-determine batch size if not specified
    if batch_size is None:
        batch_size = 16 if device == "cuda" else 8
    
    device_type = "GPU" if device == "cuda" else "CPU"
    print(f"Device: {device_type}")
    print(f"Model: {model_name}")
    print(f"Compute type: {compute_type} (optimal quality/VRAM balance)")
    print(f"Batch size: {batch_size}")
    print("Language: en (hardcoded)")
    
    start = time.time()
    
    # Load model with English language hardcoded and int8 quantization
    model = whisperx.load_model(model_name, device, compute_type=compute_type, language="en")
    
    # Transcribe with explicit English language to prevent drift
    audio = whisperx.load_audio(audio_path)
    result = model.transcribe(audio, batch_size=batch_size, language='en')
    
    # Align whisper output using English
    model_a, metadata = whisperx.load_align_model(language_code="en", device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
    
    elapsed = time.time() - start
    print(f"✓ Transcription complete in {elapsed:.1f}s ({elapsed/60:.1f} min)")
    
    return result

def diarize_audio(audio_path, hf_token, device):
    """Run speaker diarization"""
    print("\n" + "="*60)
    print("Step 2: Running speaker diarization...")
    print("="*60)
    
    start = time.time()
    
    # Check if input is MP3 - if so, convert to WAV to avoid sample count issues
    audio_path_obj = Path(audio_path)
    temp_wav = None
    diarize_path = audio_path
    
    if audio_path_obj.suffix.lower() == '.mp3':
        print("Converting MP3 to WAV for diarization (avoids sample count mismatch)...")
        temp_wav = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
        temp_wav.close()
        
        # Convert MP3 to WAV using ffmpeg
        cmd = [
            'ffmpeg', '-i', audio_path,
            '-ar', '16000',  # 16kHz sample rate (standard for speech)
            '-ac', '1',       # Mono audio
            '-y',             # Overwrite output file
            temp_wav.name
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            diarize_path = temp_wav.name
            print(f"✓ Converted to WAV: {temp_wav.name}")
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to convert MP3 to WAV: {e}")
            print("Attempting diarization with original MP3...")
            if temp_wav:
                os.unlink(temp_wav.name)
            temp_wav = None
            diarize_path = audio_path
    
    try:
        # Load diarization pipeline from pyannote.audio
        diarize_model = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            token=hf_token
        ).to(torch.device(device))
        
        # Run diarization
        diarize_segments = diarize_model(diarize_path)
        
        elapsed = time.time() - start
        print(f"✓ Diarization complete in {elapsed:.1f}s ({elapsed/60:.1f} min)")
        
        return diarize_segments
        
    finally:
        # Clean up temporary WAV file
        if temp_wav and os.path.exists(temp_wav.name):
            os.unlink(temp_wav.name)
            print("Cleaned up temporary WAV file")

def assign_speakers(result, diarize_segments):
    """Assign speakers to transcript segments"""
    print("\n" + "="*60)
    print("Step 3: Assigning speakers to transcript...")
    print("="*60)
    
    # pyannote.audio 4.0 returns a DiarizeOutput dataclass with speaker_diarization attribute
    # Extract the Annotation object and convert to pandas DataFrame (required by WhisperX)
    annotation = diarize_segments.speaker_diarization
    
    diarize_list = []
    for segment, _, speaker in annotation.itertracks(yield_label=True):
        diarize_list.append({
            'start': segment.start,
            'end': segment.end,
            'speaker': speaker
        })
    
    # Create DataFrame with required columns
    diarize_df = pd.DataFrame(diarize_list)
    
    result_with_speakers = whisperx.assign_word_speakers(diarize_df, result)
    
    # Count speakers
    speakers = set()
    for segment in result_with_speakers["segments"]:
        if "speaker" in segment:
            speakers.add(segment["speaker"])
    
    print(f"✓ Detected {len(speakers)} speakers: {sorted(speakers)}")
    
    return result_with_speakers

def save_transcript(result, output_path):
    """Save formatted transcript as both .txt and .md to intermediates directory"""
    print("\n" + "="*60)
    print("Step 4: Saving transcripts to intermediates/...")
    print("="*60)
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save .txt file
    with open(output_path, 'w', encoding='utf-8') as f:
        current_speaker = None
        for segment in result["segments"]:
            speaker = segment.get("speaker", "UNKNOWN")
            
            if speaker != current_speaker:
                f.write(f"\n{speaker}:\n")
                current_speaker = speaker
            
            start_time = segment["start"]
            text = segment["text"].strip()
            f.write(f"[{start_time:.1f}s] {text}\n")
    
    print(f"✓ Text saved to: {output_path}")
    
    # Save .md file
    md_path = output_path.parent / f"{output_path.stem.replace('_transcript_with_speakers', '_transcript')}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        current_speaker = None
        for segment in result["segments"]:
            speaker = segment.get("speaker", "UNKNOWN")
            
            if speaker != current_speaker:
                f.write(f"\n**{speaker}:**\n")
                current_speaker = speaker
            
            start_time = segment["start"]
            text = segment["text"].strip()
            f.write(f"[{start_time:.1f}s] {text}\n")
    
    print(f"✓ Markdown saved to: {md_path}")
    
    # Print statistics
    speakers = {}
    for segment in result["segments"]:
        speaker = segment.get("speaker", "UNKNOWN")
        speakers[speaker] = speakers.get(speaker, 0) + 1
    
    print("\n" + "="*60)
    print("Summary")
    print("="*60)
    for speaker in sorted(speakers.keys()):
        print(f"  {speaker}: {speakers[speaker]} segments")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Complete WhisperX transcription with speaker diarization (English only, int8 quantization)",
        epilog="""
Processing options:
  Auto-detect GPU (default, uses CUDA if available)
  --force-cpu:     Force CPU processing even if GPU available
  --batch-size:    Override automatic batch size (default: 16 GPU, 8 CPU)
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("audio_file", help="Audio file path")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--token", help="HuggingFace token (overrides HF_TOKEN env var)")
    parser.add_argument("--force-cpu", action="store_true",
                       help="Force CPU processing even if GPU available")
    parser.add_argument("--batch-size", type=int, default=None,
                       help="Override automatic batch size (smaller=more thorough, larger=faster)")
    
    args = parser.parse_args()
    
    # Get token
    hf_token = args.token or os.environ.get('HF_TOKEN')
    if not hf_token:
        print("Error: HuggingFace token not provided.")
        print("Set HF_TOKEN environment variable or use --token argument")
        sys.exit(1)
    
    # Check audio file
    audio_path = Path(args.audio_file)
    if not audio_path.exists():
        print(f"Error: Audio file not found: {audio_path}")
        sys.exit(1)
    
    # Set output path - always to intermediates directory
    if args.output:
        output_path = Path(args.output)
    else:
        # Build filename without model indicator (always using large-v3)
        intermediates_dir = Path("intermediates")
        intermediates_dir.mkdir(exist_ok=True)
        output_path = intermediates_dir / f"{audio_path.stem}_transcript_with_speakers.txt"
    
    # Setup device based on flags
    if args.force_cpu:
        device = "cpu"
    else:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    
    print("="*60)
    print("WhisperX Transcription Pipeline with Diarization")
    print("="*60)
    print(f"Audio file: {audio_path}")
    print(f"Output file: {output_path}")
    print(f"Device: {device}" + (" (forced)" if args.force_cpu else ""))
    if device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Model: large-v3 (hardcoded for best accuracy)")
    print(f"Compute type: float16 (optimal quality/VRAM balance)")
    if args.batch_size:
        print(f"Batch size: {args.batch_size} (user override)")
    print("="*60)
    
    # Start total timer
    total_start = time.time()
    
    # Run pipeline
    try:
        # Step 1: Transcribe (English and large-v3 hardcoded, float16 quantization)
        result = transcribe_audio(str(audio_path), device, 
                                 batch_size=args.batch_size)
        
        # Step 2: Diarize
        diarize_segments = diarize_audio(str(audio_path), hf_token, device)
        
        # Step 3: Assign speakers
        result_with_speakers = assign_speakers(result, diarize_segments)
        
        # Step 4: Save
        save_transcript(result_with_speakers, output_path)
        
        # Total time
        total_elapsed = time.time() - total_start
        print("\n" + "="*60)
        print(f"✓ COMPLETE! Total time: {total_elapsed:.1f}s ({total_elapsed/60:.1f} min)")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
