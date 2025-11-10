# WhisperX Model Comparison Guide

## Overview

The transcription script has been enhanced to support:
- **Multiple Whisper models**: large-v2, large-v3, turbo, distil-large-v3
- **Automatic output naming**: Files are named with model/settings for easy comparison

**Note**: VAD (Voice Activity Detection) is always enabled in WhisperX by default - it runs automatically to reduce hallucinations and improve accuracy.

## New Command-Line Options

### Model Selection
```bash
--model {large-v2,large-v3,turbo,distil-large-v3}
```
- **large-v2** (default): Current baseline, proven reliability
- **large-v3**: Newest model, best accuracy especially for technical terms
- **turbo**: Speed/quality balance, much faster
- **distil-large-v3**: Distilled model, 5-7x faster with 97-98% accuracy

## Running Comparison Tests

### Quick Test (Single Model)
```bash
# Test with large-v3 (recommended for best quality)
python3 scripts/transcribe_with_diarization.py audio.mp3 --model large-v3
```

### Side-by-Side Comparison (Automated)
```bash
# Run both model tests automatically
./scripts/test_model_comparison.sh audio.mp3
```

This will test:
1. **large-v2** - Current baseline
2. **large-v3** - Newest model (recommended)

### Output Files

Files are automatically named with model info:
```
intermediates/audio_lv2_transcript_with_speakers.txt    # large-v2
intermediates/audio_lv3_transcript_with_speakers.txt    # large-v3
```

Legend:
- `lv2` = large-v2
- `lv3` = large-v3
- `turbo` = turbo model
- `dlv3` = distil-large-v3

## Comparing Results

### Method 1: Visual Diff Tools
```bash
# Using meld (GUI)
meld intermediates/audio_lv2_transcript_with_speakers.txt \
     intermediates/audio_lv3_transcript_with_speakers.txt

# Using vimdiff
vimdiff intermediates/audio_lv2_transcript_with_speakers.txt \
        intermediates/audio_lv3_transcript_with_speakers.txt
```

### Method 2: Command Line Diff
```bash
# Show differences
diff intermediates/audio_lv2_transcript_with_speakers.txt \
     intermediates/audio_lv3_transcript_with_speakers.txt

# Show side-by-side comparison
diff -y intermediates/audio_lv2_transcript_with_speakers.txt \
        intermediates/audio_lv3_transcript_with_speakers.txt | less
```

### Method 3: Word Count Comparison
```bash
# Compare lengths (can indicate hallucination differences)
wc -w intermediates/audio_*_transcript_with_speakers.txt
```

## Timing Comparison

The test script saves timing logs in a timestamped directory:
```bash
comparison_results_20250108_163000/
├── test1_large-v2.log
└── test2_large-v3.log
```

Extract timing from logs:
```bash
grep "Total time:" comparison_results_*/test*.log
```

## Expected Results

### Speed (Approximate, 60-min audio, int8 quantization)
- **large-v2**: ~8-9 minutes total (batch_size=16)
- **large-v3**: ~8-9 minutes total (similar speed to v2)
- **turbo**: ~3-4 minutes total (2-3x faster)

### Quality (All use int8 quantization)
- **int8 quantization**: 98-99% quality of float32
- **VRAM usage**: ~4GB (works on 6GB+ GPUs)
- **Quality**: Imperceptible difference from float32

**large-v3 advantages**:
- Better handling of technical terminology
- Improved proper noun recognition
- Better with accents and challenging audio
- More accurate punctuation
- Slightly more concise output (fewer hallucinations)

**VAD (built-in to WhisperX)**:
- Always enabled automatically
- Reduces hallucinations in silence
- Cleaner transcripts with less noise
- Better sentence boundaries

## Recommendations

### For Maximum Accuracy (Your Use Case)
```bash
--model large-v3
```
This is the **recommended configuration** for interview transcripts with technical blockchain/Ethereum content.

### For Speed vs Quality Balance
```bash
--model turbo
```
If you need faster processing, turbo provides excellent quality at 2-3x speed.

### For Throughput Optimization
```bash
--model large-v3 --batch-size 32
```
Larger batch sizes process faster (default is 16 for GPU, 8 for CPU).

### For Thorough Processing
```bash
--model large-v3 --batch-size 4
```
Smaller batch sizes are more thorough but slower.

## What Changed from Original

### Removed (Deprecated)
- **Quality modes**: Removed `--high-quality` and `--low-quality` flags
- **float32/float16**: Replaced with universal int8 quantization
- `beam_size` parameter (not exposed by WhisperX)
- `best_of` parameter (not exposed by WhisperX)
- `temperature` parameter (not exposed by WhisperX)
- `vad_filter` parameter (VAD is always enabled automatically in WhisperX)

### Added (Current Implementation)
- **int8 quantization**: Universal compute type (98-99% quality, 4GB VRAM)
- **Batch size control**: `--batch-size` flag for speed/thoroughness tuning
- **Multiple model support**: large-v2, large-v3, turbo, distil-large-v3
- **Simplified filenames**: No quality suffix, just model identifier

## Troubleshooting

### Out of Memory (Rare with int8)
If you still get CUDA out of memory errors with int8:
```bash
# Reduce batch size
python3 scripts/transcribe_with_diarization.py audio.mp3 --batch-size 8
```

### Model Download Issues
Models are auto-downloaded from HuggingFace. If download fails:
```bash
# Check internet connection
# Verify HuggingFace is accessible
```


## Next Steps

1. **Run the comparison test**:
   ```bash
   ./scripts/test_model_comparison.sh your_audio_file.mp3
   ```

2. **Review the outputs** in `intermediates/` and compare transcription quality

3. **Check timing logs** to see performance differences

4. **Choose your preferred configuration**:
   - **large-v3**: Best quality (recommended for production)
   - **turbo**: 2-3x faster with excellent quality
   - **Batch size tuning**: Adjust `--batch-size` for speed/thoroughness balance

5. **Update your workflow** to use the best configuration for your needs
