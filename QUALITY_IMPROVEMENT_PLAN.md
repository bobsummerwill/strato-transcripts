# Transcription Quality Improvement Implementation Plan

## Executive Summary

This document outlines a comprehensive strategy to improve transcription quality for Ethereum/blockchain podcast interviews by leveraging:
- **Local Resources**: ~/Projects/EarlyDaysOfEthereum (180+ people) + ~/Projects/ethereum-org-website
- **Domain Context**: Several hours of existing audio + corrected transcripts
- **Multi-Stage Pipeline**: WhisperX → Initial Prompt → GPT-4 Post-Processing

**Expected Improvement**: 20-40% better accuracy on technical terms, proper names, and blockchain concepts.

---

## Phase 1: Initial Prompt System (Week 1)

### Overview
Whisper's `initial_prompt` parameter has a **224 token limit** (~150-200 words). This provides hints to the model about expected content.

### Implementation Steps

#### 1.1 Extract Top Ethereum Terms
```bash
# Extract from EarlyDaysOfEthereum
grep -rh "Ethereum" ../EarlyDaysOfEthereum/source/_articles/ | \
  grep -oE '\b[A-Z][a-z]+(\s[A-Z][a-z]+)*\b' | \
  sort | uniq -c | sort -rn | head -50
```

#### 1.2 Create Curated Term List
**File**: `ethereum_initial_prompt.txt`

Categories to include:
- Top 15-20 technical terms
- 10-15 key people names  
- 5-10 important projects
- 5 common phrases

**Example Structure** (stays under 224 tokens):
```
Ethereum blockchain podcast interview. Technical terms: smart contracts, 
ERC-20, ERC-721, NFTs, DeFi, decentralized finance, Web3, MetaMask, 
Solidity, gas fees, validators, staking, proof-of-stake, consensus, 
Ethereum Virtual Machine, EVM, dApps, layer 2, rollups, sharding.

Key people: Vitalik Buterin, Gavin Wood, Joseph Lubin, Jeffrey Wilcke, 
Alex van de Sande, Taylor Gerring, Fabian Vogelsteller.

Projects: Ethereum Foundation, ConsenSys, Parity, OpenEthereum.
```

#### 1.3 Add Script Support
**File**: `transcribe_with_diarization.py`

Add parameters:
```python
parser.add_argument("--initial-prompt", 
                   help="Path to initial prompt file or prompt text")
parser.add_argument("--auto-prompt", action="store_true",
                   help="Use built-in Ethereum prompt automatically")
```

Implement in `transcribe_audio()`:
```python
def transcribe_audio(..., initial_prompt=None):
    # ...
    result = model.transcribe(audio, 
                             batch_size=batch_size,
                             language="en",
                             initial_prompt=initial_prompt)
```

#### 1.4 Testing
- Test with/without prompt on same audio
- Compare WER (Word Error Rate) on technical terms
- Measure improvement percentage

**Success Metric**: 15-25% improvement on technical term accuracy

---

## Phase 2: Comprehensive Glossary (Week 1-2)

### 2.1 People Names Extraction
**Script**: `extract_people.py`

```python
import os
from pathlib import Path

people_dir = Path("../EarlyDaysOfEthereum/source/_people")
names = []

for md_file in people_dir.glob("*.md"):
    # Extract name from filename
    name = md_file.stem.replace("-", " ").title()
    names.append(name)
    
    # Extract from YAML frontmatter if available
    with open(md_file) as f:
        content = f.read()
        # Parse YAML name field
        
# Output: ethereum_people.txt (alphabetically sorted)
```

**Output**: ~180+ names in `ethereum_people.txt`

### 2.2 Technical Terms Extraction
**Sources**:
- ethereum.org/en/glossary/
- ethereum.org/en/developers/docs/
- EarlyDaysOfEthereum articles

**Script**: `extract_terms.py`
- Parse markdown files
- Extract capitalized technical terms
- Build frequency map
- Filter by relevance

**Output**: `ethereum_technical_terms.txt` (~500 terms)

### 2.3 Project & Organization Names
**Sources**:
- ConsenSys, Ethereum Foundation, Parity Technologies
- DeFi protocols: Uniswap, Aave, Compound, MakerDAO
- Layer 2s: Arbitrum, Optimism, zkSync, StarkNet

**Output**: `ethereum_projects.txt` (~100 projects)

### 2.4 Consolidated Glossary
**File**: `ethereum_glossary.json`

```json
{
  "people": ["Vitalik Buterin", "Gavin Wood", ...],
  "technical_terms": ["smart contract", "ERC-20", ...],
  "projects": ["Ethereum Foundation", "ConsenSys", ...],
  "abbreviations": {
    "EVM": "Ethereum Virtual Machine",
    "PoS": "Proof of Stake",
    "DeFi": "Decentralized Finance"
  }
}
```

---

## Phase 3: GPT-4 Post-Processing Pipeline (Week 2-3)

### 3.1 Architecture

```
WhisperX Transcript
       ↓
[Load Glossary + Website Context]
       ↓
GPT-4 API (gpt-4-turbo-preview, 128K context)
       ↓
Corrected Transcript
```

### 3.2 Implementation
**Script**: `post_process_transcript.py`

```python
#!/usr/bin/env python3
"""
GPT-4 based transcript post-processor
Uses full website context to correct technical terms and speaker names
"""

import os
import json
from pathlib import Path
import anthropic  # or openai

def load_context_files():
    """Load website content as context"""
    # Read key pages from ethereum-org-website
    # Read articles from EarlyDaysOfEthereum
    # Concatenate (stay under 128K tokens)
    pass

def load_glossary():
    """Load ethereum_glossary.json"""
    pass

def process_transcript(transcript_path, api_key):
    """Main processing function"""
    
    # Load raw WhisperX transcript
    with open(transcript_path) as f:
        transcript = f.read()
    
    # Load context and glossary
    context = load_context_files()
    glossary = load_glossary()
    
    # Build GPT-4 prompt
    prompt = f"""You are an expert transcript editor specializing in Ethereum and blockchain technology.

Context (Ethereum Resources):
{context}

Known People: {', '.join(glossary['people'][:50])}
Technical Terms: {', '.join(glossary['technical_terms'][:100])}
Projects: {', '.join(glossary['projects'])}

Raw Transcript (from speech recognition):
{transcript}

Tasks:
1. Fix technical term spellings (e.g., "etherium" → "Ethereum")
2. Correct proper names using the people list
3. Fix blockchain concept terminology
4. Identify speakers by name if possible (not just SPEAKER_00)
5. Improve punctuation and capitalization
6. Add paragraph breaks for readability
7. Preserve timestamps [XX.Xs] format

Output the corrected transcript maintaining the same format.
"""
    
    # Call GPT-4
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=16000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    corrected = response.content[0].text
    
    # Save corrected transcript
    output_path = transcript_path.replace(".txt", "_corrected.txt")
    with open(output_path, 'w') as f:
        f.write(corrected)
    
    return output_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript", help="Path to transcript file")
    parser.add_argument("--api-key", help="Anthropic API key")
    args = parser.parse_args()
    
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    process_transcript(args.transcript, api_key)
```

### 3.3 Enhanced Features
- **Speaker Identification**: Match SPEAKER_XX to actual names
- **Terminology Standardization**: Consistent spelling across all transcripts
- **Acronym Expansion**: First use explanation
- **Confidence Scoring**: Flag uncertain corrections

### 3.4 Testing Strategy
1. Run on 2-3 sample transcripts
2. Manual review of corrections
3. Calculate accuracy improvement
4. Iterate on prompt engineering

**Success Metric**: 30-50% reduction in errors, proper speaker names identified

---

## Phase 4: Workflow Integration (Week 3)

### 4.1 Combined Pipeline Script
**File**: `transcribe_and_correct.sh`

```bash
#!/bin/bash
# Complete pipeline: Audio → WhisperX → GPT-4 → Corrected Transcript

AUDIO_FILE="$1"
HF_TOKEN="${HF_TOKEN}"
ANTHROPIC_KEY="${ANTHROPIC_API_KEY}"

# Step 1: Transcribe with WhisperX + initial prompt
python3 transcribe_with_diarization.py "$AUDIO_FILE" \
    --high-quality \
    --model large-v3 \
    --auto-prompt

# Step 2: Post-process with GPT-4
TRANSCRIPT="${AUDIO_FILE%.mp3}_lv3_hq_transcript_with_speakers.txt"
python3 post_process_transcript.py "$TRANSCRIPT" \
    --api-key "$ANTHROPIC_KEY"

echo "Complete! Corrected transcript: ${TRANSCRIPT%.txt}_corrected.txt"
```

### 4.2 Batch Processing
Process all existing transcripts:
```bash
for file in outputs/*_transcript_with_speakers.txt; do
    python3 post_process_transcript.py "$file"
done
```

---

## Phase 5: Fine-Tuning (Long-term, 3-6 months)

### 5.1 Data Preparation
**Requirements**: 10-50 hours of accurately transcribed audio

**Process**:
1. Use Phase 3 corrected transcripts as training data
2. Manual review and refinement of key sections
3. Format for Whisper fine-tuning

### 5.2 Fine-Tuning Approach
```python
# Using Hugging Face transformers
from transformers import WhisperForConditionalGeneration, Seq2SeqTrainer

model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v3")

# Load dataset of audio + corrected transcripts
# Fine-tune on Ethereum-specific content
# Evaluate WER improvements
```

### 5.3 Expected Outcomes
- Domain-specific model: "whisper-large-v3-ethereum"
- 40-60% improvement on technical terms
- Better out-of-box performance (less need for post-processing)

**Cost**: Moderate GPU time, manual review effort
**Benefit**: One-time investment, permanent quality improvement

---

## Priority & Timeline

### Immediate (This Week)
- ✅ Create this implementation plan
- [ ] Build initial_prompt extraction scripts
- [ ] Add --initial-prompt flag to transcribe_with_diarization.py
- [ ] Test on 1 sample transcript

### Short-term (Next 2 Weeks)
- [ ] Extract comprehensive glossary from local sources
- [ ] Build GPT-4 post-processing script
- [ ] Test on 3-5 transcripts
- [ ] Document improvements

### Medium-term (Next Month)
- [ ] Process all existing transcripts
- [ ] Refine prompts based on results
- [ ] Create batch workflow scripts
- [ ] Write comparison metrics

### Long-term (3-6 Months)
- [ ] Gather 20+ hours corrected audio
- [ ] Fine-tune Whisper model
- [ ] Deploy custom model
- [ ] Measure final improvements

---

## Resource Requirements

### Local Resources Available
- ✅ EarlyDaysOfEthereum: 180+ people, articles, context
- ✅ ethereum-org-website: Technical documentation
- ✅ Existing transcripts: Several hours of audio

### External Resources Needed
- API Key: Anthropic Claude (or OpenAI GPT-4)
  - Cost: ~$0.01-0.03 per transcript (estimate)
  - Alternative: Use local LLM (Ollama + llama3:70b)
- GPU Time: For fine-tuning (optional, long-term)

### Time Investment
- Phase 1-2: 10-15 hours (extraction + integration)
- Phase 3: 15-20 hours (GPT-4 pipeline + testing)
- Phase 4: 5 hours (workflow automation)
- Phase 5: 40+ hours (fine-tuning, optional)

**Total for Phases 1-4**: ~35-45 hours of development time

---

## Success Metrics

### Quantitative
- **Technical Term Accuracy**: Target 90%+ (from ~70%)
- **Proper Name Accuracy**: Target 95%+ (from ~60%)
- **WER Improvement**: 20-40% reduction
- **Speaker Identification**: 80%+ match to actual names

### Qualitative
- Transcripts read naturally
- Minimal manual correction needed
- Consistent terminology across all transcripts
- Suitable for publication

---

## Next Steps

1. **Review this plan** with stakeholders
2. **Prioritize features** (initial prompt vs GPT-4, etc.)
3. **Set up API keys** (Anthropic or OpenAI)
4. **Begin Phase 1** implementation
5. **Track progress** through GitHub issues

---

## Appendix: File Structure

```
stratomercata-transcripts/
├── transcribe_with_diarization.py  # Enhanced with --initial-prompt
├── post_process_transcript.py      # New: GPT-4 correction
├── extract_people.py               # New: Name extraction
├── extract_terms.py                # New: Term extraction
├── transcribe_and_correct.sh       # New: Complete pipeline
│
├── ethereum_initial_prompt.txt     # New: 224-token prompt
├── ethereum_glossary.json          # New: Full glossary
├── ethereum_people.txt             # New: Name list
├── ethereum_technical_terms.txt    # New: Term list
├── ethereum_projects.txt           # New: Project list
│
└── QUALITY_IMPROVEMENT_PLAN.md     # This document
```

---

## Questions & Decisions

### Decision Points
1. **API Choice**: Anthropic Claude vs OpenAI GPT-4?
   - Claude: Better at long context, newer models
   - GPT-4: More established, extensive docs
   
2. **Initial Prompt Strategy**: Auto vs Manual?
   - Auto: Use same prompt for all transcripts
   - Manual: Customize per interview/guest

3. **Processing Timing**: Real-time vs Batch?
   - Real-time: Correct each transcript as created
   - Batch: Process all existing + new together

### Open Questions
1. What's the acceptable error rate for publication?
2. Should corrected transcripts replace originals?
3. How to handle uncertain corrections?
4. Version control for transcript iterations?

---

*Document created: November 8, 2025*
*Last updated: November 8, 2025*
*Status: Draft - Awaiting approval to begin Phase 1*
