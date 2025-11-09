# WhisperX Model Comparison Guide

## Overview

The transcription script has been enhanced to support:
- **Multiple Whisper models**: large-v2, large-v3, turbo, distil-large-v3
- **VAD filtering**: Voice Activity Detection to reduce hallucinations
- **Automatic output naming**: Files are named with model/settings for easy comparison

## New Command-Line Options

### Model Selection
```bash
--model {large-v2,large-v3,turbo,distil-large-v3}
```
- **large-v2** (default): Current baseline, proven reliability
- **large-v3**: Newest model, best accuracy especially for technical terms
- **turbo**: Speed/quality balance, much faster
- **distil-large-v3**: Distilled model, 5-7x faster with 97-98% accuracy

### VAD Filtering
```bash
--vad
```
Enable Voice Activity Detection filtering to reduce hallucinations and improve accuracy on files with silence/background noise.

## Running Comparison Tests

### Quick Test (Single Model)
```bash
# Test with large-v3 + VAD (recommended for best quality)
python3 transcribe_with_diarization.py audio.mp3 \
    --high-quality \
    --model large-v3 \
    --vad
```

### Side-by-Side Comparison (Automated)
```bash
# Run all 4 test configurations automatically
./test_model_comparison.sh audio.mp3
```

This will test:
1. **large-v2** (baseline) - Your current setup
2. **large-v2 + VAD** - Baseline with hallucination reduction
3. **large-v3** - Newest model
4. **large-v3 + VAD** - Best quality (recommended)

### Output Files

Files are automatically named with settings:
```
audio_lv2_hq_transcript_with_speakers.txt          # large-v2 high-quality
audio_lv2_hq_vad_transcript_with_speakers.txt      # large-v2 high-quality + VAD
audio_lv3_hq_transcript_with_speakers.txt          # large-v3 high-quality
audio_lv3_hq_vad_transcript_with_speakers.txt      # large-v3 high-quality + VAD
```

Legend:
- `lv2` = large-v2
- `lv3` = large-v3
- `hq` = high-quality mode
- `lq` = low-quality (fast) mode
- `vad` = VAD filtering enabled

## Comparing Results

### Method 1: Visual Diff Tools
```bash
# Using meld (GUI)
meld audio_lv2_hq_transcript_with_speakers.txt \
     audio_lv3_hq_vad_transcript_with_speakers.txt

# Using vimdiff
vimdiff audio_lv2_hq_transcript_with_speakers.txt \
        audio_lv3_hq_vad_transcript_with_speakers.txt
```

### Method 2: Command Line Diff
```bash
# Show differences
diff audio_lv2_hq_transcript_with_speakers.txt \
     audio_lv3_hq_vad_transcript_with_speakers.txt

# Show side-by-side comparison
diff -y audio_lv2_hq_transcript_with_speakers.txt \
        audio_lv3_hq_vad_transcript_with_speakers.txt | less
```

### Method 3: Word Count Comparison
```bash
# Compare lengths (can indicate hallucination differences)
wc -w audio_*_transcript_with_speakers.txt
```

## Timing Comparison

The test script saves timing logs in a timestamped directory:
```bash
comparison_results_20250108_163000/
├── test1_large-v2.log
├── test2_large-v2_vad.log
├── test3_large-v3.log
└── test4_large-v3_vad.log
```

Extract timing from logs:
```bash
grep "Total time:" comparison_results_*/test*.log
```

## Expected Results

### Speed (Approximate, 13-min audio)
- **large-v2 HQ**: ~2-3 minutes total
- **large-v2 HQ + VAD**: ~2-3 minutes total (VAD adds minimal overhead)
- **large-v3 HQ**: ~2-3 minutes total (similar to v2)
- **large-v3 HQ + VAD**: ~2-3 minutes total

### Quality Improvements

**large-v3 advantages**:
- Better handling of technical terminology
- Improved proper noun recognition
- Better with accents and challenging audio
- More accurate punctuation

**VAD filtering benefits**:
- Reduces hallucinations in silence
- Cleaner transcripts with less noise
- Better sentence boundaries
- May slightly reduce total word count (removes false positives)

## Recommendations

### For Maximum Accuracy (Your Use Case)
```bash
--high-quality --model large-v3 --vad
```
This is the **recommended configuration** for interview transcripts with technical blockchain/Ethereum content.

### For Speed Testing
```bash
--high-quality --model turbo --vad
```
If large-v3 is too slow, turbo provides excellent quality at 2-3x speed.

### For Production (After Testing)
Once you've verified large-v3 quality, update your workflow:
```bash
# Replace in your existing scripts
--model large-v3 --vad
```

## What Changed from Original

### Removed (Were Hallucinated)
- `beam_size` parameter (not exposed by WhisperX)
- `best_of` parameter (not exposed by WhisperX)
- `temperature` parameter (not exposed by WhisperX)

### Added (Proven to Work)
- Multiple model support (documented in WhisperX)
- VAD filtering (documented feature)
- Better batch sizing for quality
- float32 compute type for maximum precision

## Troubleshooting

### Out of Memory
If you get CUDA out of memory errors:
```bash
# Reduce batch size by editing transcribe_with_diarization.py
# Change: batch_size = 4 to batch_size = 2
```

### Model Download Issues
Models are auto-downloaded from HuggingFace. If download fails:
```bash
# Check internet connection
# Verify HuggingFace is accessible
```

### VAD Not Working
VAD is a WhisperX feature. If it errors:
```bash
# Try without VAD first to isolate the issue
python3 transcribe_with_diarization.py audio.mp3 --high-quality --model large-v3
```

## Next Steps

1. **Run the comparison test**:
   ```bash
   ./test_model_comparison.sh your_audio_file.mp3
   ```

2. **Review the outputs** and compare transcription quality

3. **Check timing logs** to see performance differences

4. **Choose your preferred configuration** based on quality vs. speed tradeoffs

5. **Update your workflow** to use the best configuration for your needs
