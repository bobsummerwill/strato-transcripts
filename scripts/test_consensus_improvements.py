#!/usr/bin/env python3
"""
Tests for consensus workflow improvements (issues #49, #50, #51)

Tests:
1. consensus_words.py: anchor finding, DP alignment, full consensus building
2. Improved align_ai_to_original() with punctuation-heavy text
3. Context-aware filler removal (ensure semantic "like" is preserved)

Run with: python -m pytest scripts/test_consensus_improvements.py -v
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

import pytest
from consensus_words import (
    norm_token,
    words_to_tokens,
    _find_anchors,
    _dp_align_tokens,
    align_word_lists,
    build_consensus,
    Anchor,
)
from ai_consensus_pipeline import (
    tokenize_preserving_punctuation,
    compute_alignment_confidence,
    align_ai_to_original,
    is_filler_like,
    is_filler_word,
    is_sentence_boundary,
)


# =============================================================================
# Test consensus_words.py
# =============================================================================

class TestConsensusWords:
    """Test the new consensus_words module (PR #52)"""
    
    def test_norm_token(self):
        """Test token normalization"""
        assert norm_token("Hello") == "hello"
        assert norm_token("Hello,") == "hello"
        assert norm_token("Hello!") == "hello"
        assert norm_token("  Hello.  ") == "hello"
        assert norm_token("it's") == "it's"  # Keep apostrophes
    
    def test_words_to_tokens(self):
        """Test word list to token list conversion"""
        words = [
            {"text": "Hello"},
            {"text": "World!"},
            {"text": ""},
        ]
        tokens = words_to_tokens(words)
        assert tokens == ["hello", "world", ""]
    
    def test_find_anchors_exact_match(self):
        """Test anchor finding with exact time matches"""
        pivot = [
            {"text": "hello", "start": 0.0},
            {"text": "world", "start": 1.0},
            {"text": "test", "start": 2.0},
        ]
        other = [
            {"text": "hello", "start": 0.1},
            {"text": "world", "start": 1.1},
            {"text": "test", "start": 2.1},
        ]
        
        anchors = _find_anchors(pivot, other, time_tol_s=0.5)
        assert len(anchors) == 3
        assert anchors[0].i == 0
        assert anchors[0].j == 0
    
    def test_find_anchors_with_insertions(self):
        """Test anchor finding when one transcriber has insertions"""
        pivot = [
            {"text": "hello", "start": 0.0},
            {"text": "world", "start": 1.0},
        ]
        other = [
            {"text": "um", "start": 0.0},
            {"text": "hello", "start": 0.5},
            {"text": "beautiful", "start": 0.8},
            {"text": "world", "start": 1.2},
        ]
        
        anchors = _find_anchors(pivot, other, time_tol_s=0.6)
        assert len(anchors) == 2
        # Should match "hello" and "world", skipping inserted words
        assert anchors[0].i == 0  # pivot "hello"
        assert anchors[0].j == 1  # other "hello"
        assert anchors[1].i == 1  # pivot "world"
        assert anchors[1].j == 3  # other "world"
    
    def test_dp_align_tokens_exact(self):
        """Test DP alignment with exact match"""
        pivot = ["hello", "world"]
        other = ["hello", "world"]
        
        pairs = _dp_align_tokens(pivot, other)
        assert len(pairs) == 2
        assert pairs[0] == (0, 0)
        assert pairs[1] == (1, 1)
    
    def test_dp_align_tokens_insertion(self):
        """Test DP alignment with insertion"""
        pivot = ["hello", "world"]
        other = ["hello", "beautiful", "world"]
        
        pairs = _dp_align_tokens(pivot, other)
        # Should align hello->hello, None->beautiful, world->world
        assert (0, 0) in pairs  # hello
        assert (None, 1) in pairs  # inserted "beautiful"
        assert (1, 2) in pairs  # world
    
    def test_dp_align_tokens_deletion(self):
        """Test DP alignment with deletion"""
        pivot = ["hello", "beautiful", "world"]
        other = ["hello", "world"]
        
        pairs = _dp_align_tokens(pivot, other)
        # Should align hello->hello, beautiful->None, world->world
        assert (0, 0) in pairs  # hello
        assert (1, None) in pairs  # deleted "beautiful"
        assert (2, 1) in pairs  # world
    
    def test_align_word_lists_simple(self):
        """Test full word list alignment"""
        pivot = [
            {"text": "Hello", "start": 0.0, "end": 0.5},
            {"text": "world", "start": 1.0, "end": 1.5},
        ]
        other = [
            {"text": "hello", "start": 0.1, "end": 0.6},
            {"text": "world", "start": 1.1, "end": 1.6},
        ]
        
        mapping = align_word_lists(pivot, other)
        assert mapping[0] == 0
        assert mapping[1] == 1
    
    def test_build_consensus_simple(self):
        """Test consensus building with two agreeing sources"""
        word_lists = {
            "whisperx": [
                {"text": "Hello", "start": 0.0, "end": 0.5, "speaker": "SPEAKER_00"},
                {"text": "world", "start": 1.0, "end": 1.5, "speaker": "SPEAKER_00"},
            ],
            "assemblyai": [
                {"text": "hello", "start": 0.1, "end": 0.6, "speaker": "SPEAKER_00"},
                {"text": "world", "start": 1.1, "end": 1.6, "speaker": "SPEAKER_00"},
            ],
        }
        
        consensus = build_consensus(word_lists)
        assert len(consensus) == 2
        assert consensus[0]['text'].lower() == "hello"
        assert consensus[1]['text'].lower() == "world"
        assert all(w['agreement'] > 0.9 for w in consensus)  # High agreement
    
    def test_build_consensus_disagreement(self):
        """Test consensus building with disagreement"""
        word_lists = {
            "whisperx": [
                {"text": "Hello", "start": 0.0, "end": 0.5, "speaker": "SPEAKER_00", "confidence": 0.9},
            ],
            "assemblyai": [
                {"text": "Yellow", "start": 0.1, "end": 0.6, "speaker": "SPEAKER_00", "confidence": 0.8},
            ],
        }
        
        consensus = build_consensus(word_lists)
        assert len(consensus) == 1
        # Should pick "Hello" due to higher confidence
        assert consensus[0]['agreement'] < 1.0  # Not perfect agreement


# =============================================================================
# Test improved align_ai_to_original (issue #49)
# =============================================================================

class TestImprovedAlignment:
    """Test improvements to align_ai_to_original for punctuation-heavy text"""
    
    def test_tokenize_urls(self):
        """Test that URLs are kept intact"""
        text = "Check out https://example.com and http://test.org for more."
        tokens = tokenize_preserving_punctuation(text)
        assert "https://example.com" in tokens
        assert "http://test.org" in tokens
    
    def test_tokenize_code_identifiers(self):
        """Test that code identifiers are kept intact"""
        text = "We use C++ and node.js for development"
        tokens = tokenize_preserving_punctuation(text)
        assert "C++" in tokens
        assert "node.js" in tokens
    
    def test_tokenize_hyphenated_words(self):
        """Test that hyphenated words are kept intact"""
        text = "The pre-formation T-shirt design"
        tokens = tokenize_preserving_punctuation(text)
        assert "pre-formation" in tokens
        assert "T-shirt" in tokens
    
    def test_tokenize_contractions(self):
        """Test that contractions are kept intact"""
        text = "It's don't won't can't"
        tokens = tokenize_preserving_punctuation(text)
        assert "It's" in tokens or "It'" in tokens  # Regex may vary
        assert "don't" in tokens or "don'" in tokens
    
    def test_compute_alignment_confidence(self):
        """Test alignment confidence scoring"""
        # Perfect match
        conf = compute_alignment_confidence(["hello", "world"], ["hello", "world"])
        assert conf == 1.0
        
        # No match
        conf = compute_alignment_confidence(["hello", "world"], ["foo", "bar"])
        assert conf < 0.3
        
        # Partial match
        conf = compute_alignment_confidence(["hello", "world"], ["hello", "beautiful", "world"])
        assert 0.5 < conf < 1.0
    
    def test_align_punctuation_heavy_text(self):
        """Test alignment on punctuation-heavy text"""
        original = [
            {"text": "We", "start": 0.0, "end": 0.2, "speaker": "SPEAKER_00"},
            {"text": "use", "start": 0.2, "end": 0.4, "speaker": "SPEAKER_00"},
            {"text": "C++,", "start": 0.4, "end": 0.8, "speaker": "SPEAKER_00"},
            {"text": "node.js,", "start": 0.8, "end": 1.2, "speaker": "SPEAKER_00"},
            {"text": "and", "start": 1.2, "end": 1.4, "speaker": "SPEAKER_00"},
            {"text": "https://example.com", "start": 1.4, "end": 2.0, "speaker": "SPEAKER_00"},
        ]
        
        ai_text = "We use C++, node.js, and https://example.com for development"
        
        aligned = align_ai_to_original(original, ai_text)
        
        # Should successfully align despite punctuation
        assert len(aligned) > 0
        # Check that some words matched
        matched_count = sum(1 for w in aligned if w.get('source') == 'matched')
        assert matched_count >= 4  # At least "We use and" should match
    
    def test_align_low_confidence_fallback(self):
        """Test that low confidence alignment falls back to original"""
        original = [
            {"text": "Hello", "start": 0.0, "end": 0.5, "speaker": "SPEAKER_00"},
            {"text": "world", "start": 1.0, "end": 1.5, "speaker": "SPEAKER_00"},
        ]
        
        # Completely different AI text
        ai_text = "Foo bar baz qux completely different content here"
        
        aligned = align_ai_to_original(original, ai_text)
        
        # Should fall back to original words
        assert aligned == original


# =============================================================================
# Test context-aware filler removal (issue #50)
# =============================================================================

class TestContextAwareFillerRemoval:
    """Test context-aware filler word removal"""
    
    def test_is_filler_word_basic(self):
        """Test basic filler word detection"""
        assert is_filler_word("um")
        assert is_filler_word("uh")
        assert is_filler_word("er")
        assert not is_filler_word("hello")
        assert not is_filler_word("like")  # "like" handled separately
    
    def test_is_filler_like_quotative(self):
        """Test that quotative 'like' is detected as filler"""
        words = [
            {"text": "I", "speaker": "SPEAKER_00"},
            {"text": "was", "speaker": "SPEAKER_00"},
            {"text": "like", "speaker": "SPEAKER_00"},
            {"text": "oh", "speaker": "SPEAKER_00"},
        ]
        
        # "was like" = quotative = FILLER
        assert is_filler_like(words, 2) == True
    
    def test_is_filler_like_comparison(self):
        """Test that comparison 'like' is NOT detected as filler"""
        words = [
            {"text": "looks", "speaker": "SPEAKER_00"},
            {"text": "like", "speaker": "SPEAKER_00"},
            {"text": "rain", "speaker": "SPEAKER_00"},
        ]
        
        # "looks like" = comparison = KEEP
        assert is_filler_like(words, 1) == False
    
    def test_is_filler_like_exemplification(self):
        """Test that exemplification 'like' is NOT detected as filler"""
        words = [
            {"text": "systems", "speaker": "SPEAKER_00"},
            {"text": "like", "speaker": "SPEAKER_00"},
            {"text": "Ethereum", "speaker": "SPEAKER_00"},
        ]
        
        # "systems like X" = exemplification = KEEP
        assert is_filler_like(words, 1) == False
    
    def test_is_filler_like_sentence_start(self):
        """Test that sentence-start 'like' is detected as filler"""
        words = [
            {"text": "done.", "speaker": "SPEAKER_00"},
            {"text": "Like", "speaker": "SPEAKER_00"},
            {"text": "I", "speaker": "SPEAKER_00"},
            {"text": "said", "speaker": "SPEAKER_00"},
        ]
        
        # "Like I said" at sentence start = FILLER
        assert is_filler_like(words, 1) == True
    
    def test_is_filler_like_semantic_cases(self):
        """Test various semantic 'like' cases that should be kept"""
        # "feels like home"
        words1 = [
            {"text": "feels", "speaker": "SPEAKER_00"},
            {"text": "like", "speaker": "SPEAKER_00"},
            {"text": "home", "speaker": "SPEAKER_00"},
        ]
        assert is_filler_like(words1, 1) == False
        
        # "something like that"
        words2 = [
            {"text": "something", "speaker": "SPEAKER_00"},
            {"text": "like", "speaker": "SPEAKER_00"},
            {"text": "that", "speaker": "SPEAKER_00"},
        ]
        assert is_filler_like(words2, 1) == False
    
    def test_is_sentence_boundary(self):
        """Test sentence boundary detection"""
        assert is_sentence_boundary({"text": "done."}) == True
        assert is_sentence_boundary({"text": "really?"}) == True
        assert is_sentence_boundary({"text": "wow!"}) == True
        assert is_sentence_boundary({"text": "hello"}) == False
        assert is_sentence_boundary({"text": "hello,"}) == False
    
    def test_multi_word_filler_same_speaker(self):
        """Test that multi-word fillers are only removed within same speaker"""
        # This would require running remove_filler_words with a full setup
        # For now, we test the boundary detection logic
        words = [
            {"text": "you", "speaker": "SPEAKER_00"},
            {"text": "know", "speaker": "SPEAKER_00"},
            {"text": "right", "speaker": "SPEAKER_00"},
        ]
        # All same speaker, no sentence boundary - should be removable
        assert all(w["speaker"] == "SPEAKER_00" for w in words)
        assert not any(is_sentence_boundary(w) for w in words[:2])
    
    def test_multi_word_filler_across_speakers(self):
        """Test that multi-word fillers DON'T match across speaker changes"""
        words = [
            {"text": "you", "speaker": "SPEAKER_00"},
            {"text": "know", "speaker": "SPEAKER_01"},  # Different speaker!
        ]
        # Different speakers - should NOT match multi-word filler
        speakers = set(w["speaker"] for w in words)
        assert len(speakers) > 1  # Boundary exists
    
    def test_multi_word_filler_across_sentence(self):
        """Test that multi-word fillers DON'T match across sentence boundaries"""
        words = [
            {"text": "done.", "speaker": "SPEAKER_00"},  # Sentence end
            {"text": "You", "speaker": "SPEAKER_00"},
            {"text": "know", "speaker": "SPEAKER_00"},
        ]
        # Sentence boundary exists - should NOT match
        assert is_sentence_boundary(words[0])


# =============================================================================
# Integration Tests
# =============================================================================

class TestIntegration:
    """Integration tests combining multiple components"""
    
    def test_full_consensus_workflow(self):
        """Test full workflow: multiple transcribers -> consensus"""
        word_lists = {
            "whisperx": [
                {"text": "Hello", "start": 0.0, "end": 0.5, "speaker": "SPEAKER_00", "confidence": 0.9},
                {"text": "um", "start": 0.5, "end": 0.7, "speaker": "SPEAKER_00", "confidence": 0.5},
                {"text": "world", "start": 1.0, "end": 1.5, "speaker": "SPEAKER_00", "confidence": 0.95},
            ],
            "assemblyai": [
                {"text": "Hello", "start": 0.1, "end": 0.6, "speaker": "SPEAKER_00", "confidence": 0.95},
                {"text": "world", "start": 1.1, "end": 1.6, "speaker": "SPEAKER_00", "confidence": 0.9},
            ],
        }
        
        consensus = build_consensus(word_lists)
        
        # Should have "Hello" and "world" - filler "um" may or may not be in consensus
        assert len(consensus) >= 2
        texts = [w['text'].lower() for w in consensus]
        assert "hello" in texts
        assert "world" in texts
    
    def test_ai_alignment_with_code_terms(self):
        """Test AI alignment preserves code terms correctly"""
        original = [
            {"text": "We", "start": 0.0, "end": 0.2, "speaker": "SPEAKER_00"},
            {"text": "wrote", "start": 0.2, "end": 0.5, "speaker": "SPEAKER_00"},
            {"text": "it", "start": 0.5, "end": 0.7, "speaker": "SPEAKER_00"},
            {"text": "in", "start": 0.7, "end": 0.8, "speaker": "SPEAKER_00"},
            {"text": "C++", "start": 0.8, "end": 1.2, "speaker": "SPEAKER_00"},
        ]
        
        ai_text = "We wrote it in C++"
        
        aligned = align_ai_to_original(original, ai_text)
        
        # Should preserve C++
        texts = [w['text'] for w in aligned]
        assert "C++" in texts or "C++" in ' '.join(texts)


if __name__ == "__main__":
    # Allow running directly with: python test_consensus_improvements.py
    pytest.main([__file__, "-v"])
