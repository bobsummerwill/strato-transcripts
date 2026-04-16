# Compatibility Workarounds Documentation

This document details all compatibility workarounds currently in place for the strato-transcripts pipeline, explaining why they're necessary, what upstream changes are needed to remove them, and estimated timelines.

**Last Updated**: April 15, 2026
**Validated Against**: torch 2.9.1+cu130, torchaudio 2.9.1+cu130, speechbrain 1.1.0, lightning 2.6.0/2.6.1, pyannote.audio 4.0.1/4.0.4, whisperx 3.8.5
**Status**: Three runtime workarounds remain required on currently released packages. The former SpeechBrain torchaudio patches were removed after validating SpeechBrain 1.1.0.

---

## Overview

The strato-transcripts pipeline currently requires three active compatibility workarounds to bridge version incompatibilities between:
- WhisperX 3.7.x-3.8.x (transcription service)
- pyannote.audio 4.0.1+ (speaker diarization)
- SpeechBrain 1.1.0 (audio processing, now fixed for torchaudio 2.9)
- PyTorch 2.9.1+ (GPU acceleration for RTX 50xx / Blackwell)

**All workarounds are legitimate compatibility bridges** - not hacks or accidental drift. They enable newer PyTorch/GPU support while released upstream packages still lag behind or ship conflicting constraints.

---

## Workaround #1: WhisperX HuggingFace Token Parameter

### The Problem

Released WhisperX 3.7.4 still uses the **deprecated** `use_auth_token` parameter when calling pyannote.audio models. Released WhisperX 3.8.5 partially migrates to `token`, but still leaves a `use_auth_token` path in `whisperx/asr.py`, so the install-time patch remains necessary on current wheels.

**Error without workaround**:
```python
TypeError: got an unexpected keyword argument 'use_auth_token'
```

### Our Solution

**Location**: `scripts/install_packages_and_venv.sh` (Step 8)

```bash
# Patch WhisperX to use new token parameter
sed 's/use_auth_token/token/g' whisperx/vads/pyannote.py
sed '412s/use_auth_token=None/token=None/' whisperx/asr.py
```

**Files Modified**:
- `whisperx/vads/pyannote.py` - Global replacement
- `whisperx/asr.py` - Line 412 only

### What Upstream Needs to Fix

**WhisperX** needs to update their code to use the new HuggingFace API:
```python
# Current (deprecated):
pipeline = Pipeline.from_pretrained(..., use_auth_token=token)

# Needed (new API):
pipeline = Pipeline.from_pretrained(..., token=token)
```

### When Can We Remove It?

| Milestone | Timeline | Likelihood |
|-----------|----------|------------|
| WhisperX 3.8.6+ fully removes `use_auth_token` | Unknown | **Medium** |
| WhisperX 4.x | 2026 | **High** |

**Estimated**: Remove only after a released wheel has no remaining `use_auth_token` call sites.

**Monitoring**:
```bash
# Check for new WhisperX releases
pip index versions whisperx
# Or visit: https://github.com/m-bain/whisperx/releases
```

### Upstream Issues & Pull Requests

**Our Contribution:**
- **Issue [#1322](https://github.com/m-bain/whisperx/issues/1322)** - Deprecated `use_auth_token` breaks compatibility with pyannote.audio 4.x (logged by strato-transcripts, January 2026)
- **Pull Request [#1323](https://github.com/m-bain/whisperx/pull/1323)** - Fix `use_auth_token` → `token` migration (submitted by @bobsummerwill, January 2026) ✅
  - Fork: https://github.com/bobsummerwill/whisperX
  - Branch: `fix/use-auth-token-deprecation`
  - Changes: Updated `whisperx/vads/pyannote.py` and `whisperx/asr.py` to use new HuggingFace API

**Follow-up for remaining released-wheel gap:**
- **Issue [#1406](https://github.com/m-bain/whisperX/issues/1406)** - Released wheel still uses `use_auth_token` in `whisperx/asr.py` with pyannote 4.x (logged by strato-transcripts, April 2026)
- **Pull Request [#1407](https://github.com/m-bain/whisperX/pull/1407)** - Add `token` alias for Whisper model loading (submitted by @bobsummerwill, April 2026)
  - Branch: `fix/token-alias-load-model`
  - Scope: adds a `token` alias on WhisperX's API surface while preserving the downstream `faster-whisper` call path that still expects `use_auth_token`

**Local tracking:**
- **Issue [#97](https://github.com/strato-net/strato-transcripts/issues/97)** - Tracks when the install-time WhisperX patch can be removed after an upstream release picks up `m-bain/whisperX#1407`

**Status**: 🟡 **Partially fixed upstream, not fully fixed in released wheels**

---

## Resolved April 2026: SpeechBrain torchaudio 2.9+ Compatibility

### Historical Problem

SpeechBrain 1.0.3 called `torchaudio.list_audio_backends()` and `torchaudio.info()`, both removed in torchaudio 2.9.

**Error without workaround**:
```python
AttributeError: module 'torchaudio' has no attribute 'list_audio_backends'
```

### Resolution

After testing `speechbrain==1.1.0` in an isolated overlay against the current runtime (`torch 2.9.1+cu130`, `torchaudio 2.9.1+cu130`, `pyannote.audio 4.0.1`):
- `speechbrain` imported cleanly,
- `speechbrain.utils.torch_audio_backend` imported cleanly,
- `speechbrain.dataio.dataio` imported cleanly,
- `pyannote.audio.Pipeline` imported cleanly,
- `speechbrain.dataio.dataio.read_audio_info()` successfully returned metadata for a real MP3 file.

Because of that validation, the old monkey-patches to `speechbrain/utils/torch_audio_backend.py` and `speechbrain/dataio/dataio.py` were removed from `scripts/install_venv.sh`, and the installer now explicitly installs `speechbrain==1.1.0`.

### Upstream References

**Issue:**
- **[SpeechBrain #2977](https://github.com/speechbrain/speechbrain/issues/2977)** - UserWarning: torchaudio._backend.list_audio_backends has been deprecated (October 2025)

**Pull Request:**
- **[SpeechBrain #2988](https://github.com/speechbrain/speechbrain/pull/2988)** - "Bandaid fix for torchaudio 2.9+ compatibility" (merged Oct 29, 2025) ✅
  - Fixes issue #2977
  - Adds `hasattr()` checks before calling deprecated `list_audio_backends()`
  - Note: PR author describes this as "temporary bandaid" - full fix would require migrating to torchcodec

**Commit:**
- **[927530f](https://github.com/speechbrain/speechbrain/commit/927530fa95e238fbc396000618e839a4a986dd7d)** - Adds `hasattr` checks for `list_audio_backends()`
  - Author: Oscar Friedman
  - Co-author: Peter Plantinga
  - Date: October 29, 2025

**Source Code:**
- **[torch_audio_backend.py (develop)](https://github.com/speechbrain/speechbrain/blob/develop/speechbrain/utils/torch_audio_backend.py)** - Shows the fix implemented

**Status**: ✅ **Resolved in released SpeechBrain 1.1.0 and validated locally**

---

## Workaround #2: PyTorch 2.6+ weights_only Compatibility

### The Problem

PyTorch 2.6+ changed `torch.load(weights_only=True)` as the new **security default**. However:
1. pyannote checkpoint configs reference **OmegaConf classes** (DictConfig, ListConfig, ContainerMetadata)
2. These classes aren't in PyTorch's safe allowlist
3. Loading fails with `WeightsUnpickler` errors

**Error without workaround**:
```python
_pickle.UnpicklingError: Weights only load failed.
Unsupported global: GLOBAL omegaconf.dictconfig.DictConfig was not
an allowed global by default.
```

### Our Solution

**Location**: `scripts/process_single_transcribe_and_diarize.py` (lines 380-441)

**Two-stage approach**:

```python
# Stage 1: Try to allowlist OmegaConf (safer approach)
torch.serialization.add_safe_globals([
    ContainerMetadata,
    DictConfig,
    ListConfig,
    typing.Any,
])

# Stage 2: Fallback - force weights_only=False (less safe, but necessary)
if torch_version >= Version("2.6.0"):
    def _torch_load_compat(*args, **kwargs):
        kwargs["weights_only"] = False
        return _orig_torch_load(*args, **kwargs)

    torch.load = _torch_load_compat
```

**Security Note**: Can be disabled via:
```bash
export WHISPERX_ALLOW_UNSAFE_TORCH_LOAD=0
```

### What Upstream Needs to Fix

Either of these would let us remove the local-file patch:

- **Lightning** must default local filesystem checkpoint loads to `weights_only=False` when `weights_only` is unspecified, not just remote URL loads.
- **pyannote.audio** must stop depending on the old implicit default and pass `weights_only=False` explicitly wherever required.

### When Can We Remove It?

| Milestone | Timeline | Likelihood |
|-----------|----------|------------|
| Lightning release fixes local-file default | Unknown | **Medium** |
| pyannote.audio explicitly overrides `weights_only` everywhere needed | Unknown | **Medium** |
| PyTorch expands safe allowlist | Unlikely | **Very Low** |

**Estimated**: Unknown. This remains required on released Lightning 2.6.1.

**Monitoring**:
```bash
# Check for new pyannote releases
pip index versions pyannote.audio
# Or visit: https://github.com/pyannote/pyannote-audio/releases
```

### Upstream Issues

- **[pyannote/pyannote-audio #1908](https://github.com/pyannote/pyannote-audio/issues/1908)** - Not readily compatible with torch 2.6 (August 2025)
- **[WhisperX #1304](https://github.com/m-bain/whisperx/issues/1304)** - UnpicklingError (November 2025)
- **[pyannote/pyannote-audio #1825](https://github.com/pyannote/pyannote-audio/issues/1825)** - Can't load pyannote (January 2025)

**Status**: 🟡 Open - still required on released Lightning 2.6.x

### Security Considerations

This workaround uses `weights_only=False`, which **can execute arbitrary code** from malicious checkpoints.

**Why this is acceptable**:
1. Only loads **trusted HuggingFace official models** (pyannote.audio)
2. Checkpoints are cryptographically signed and verified
3. No user-uploaded or untrusted checkpoints
4. Can be disabled if security requirements are strict

**Risk Level**: **Low** (trusted source only)

---

## Workaround #3: pyannote.audio 4.0.1 Version Pin

### The Problem

This isn't a code patch - it's a **strategic version pin**:
- `pyannote.audio 4.0.2+` hard-pins `torch==2.8.0` and `torchaudio==2.8.0`
- We need `torch>=2.9.0` for **RTX 5070 Blackwell GPU support**
- If we install pyannote 4.0.2+, pip will **downgrade PyTorch to 2.8.0**, breaking Blackwell

**Conflict**:
```
pyannote.audio 4.0.2+ requires: torch==2.8.0  (exact)
RTX 5070 Blackwell requires: torch>=2.9.0    (Blackwell support added in 2.9)
→ INCOMPATIBLE
```

### Our Solution

**Location**: `requirements.txt` and `scripts/install_packages_and_venv.sh` (Step 9)

```bash
# Pin to last version before hard torch pin
pip install "pyannote.audio==4.0.1"
```

**Why 4.0.1 specifically**:
- Last release before the exact torch/torchaudio/torchcodec pins
- Can coexist with torch 2.9.1 in our manually managed venv
- Still requires the separate torchcodec fallback workaround described above

### What Upstream Needs to Fix

**pyannote.audio** needs to relax their torch dependency from exact pin to version range:

```python
# Current (4.0.2+) - BREAKS EVERYTHING:
dependencies = ["torch==2.8.0"]

# Needed (future) - ALLOWS UPGRADES:
dependencies = ["torch>=2.8.0,<3.0"]
```

### When Can We Remove It?

| Milestone | Timeline | Likelihood |
|-----------|----------|------------|
| pyannote.audio relaxes exact pins | Unknown | **Low** |
| torch/torchcodec compatibility story stabilizes enough for pyannote to unpin | 2026 | **Medium** |

**Estimated**: Unknown. Current released 4.0.4 still requires `torch>=2.8.0`, `torchaudio>=2.8.0`, and `torchcodec>=0.7.0`, but the project-level workaround remains necessary because current torchcodec still fails for our torch 2.9.1 runtime.

**Monitoring**:
```bash
# Check dependency requirements for new releases
pip show pyannote.audio
# Or check PyPI: https://pypi.org/project/pyannote.audio/
```

### Upstream Issues & Commits

**The Pin Commit:**
- **[Commit 121054b6](https://github.com/pyannote/pyannote-audio/commit/121054b60a9497a09b3312b6bc518160f3dfb959)** - "setup: pin torch/audio/codec versions (#1954)" (Nov 19, 2025)
  - Author: Hervé BREDIN
  - Released in: pyannote.audio 4.0.2
  - Changed from: `torch>=2.8.0` to `torch==2.8.0` (exact pin)
  - Reason: "to avoid segmentation fault" per torchcodec issue #995

**Related Issues:**
- **[torchcodec #995](https://github.com/meta-pytorch/torchcodec/issues/995)** - Version incompatibility causing segfaults (torchcodec 0.8 with torch 2.8.0)
- **[pyannote.audio #1320](https://github.com/pyannote/pyannote-audio/issues/1320)** - pip dependency mismatch issues
- **[pyannote.audio #1908](https://github.com/pyannote/pyannote-audio/issues/1908)** - Not readily compatible with torch 2.6 (weights_only issues)
- **[pyannote.audio #1952](https://github.com/pyannote/pyannote-audio/issues/1952)** - AttributeError with torch 2.9.1 (torchaudio.AudioMetaData missing)

**Our Contribution:**
- **Issue [#1976](https://github.com/pyannote/pyannote-audio/issues/1976)** - Exact torch==2.8.0 pin breaks compatibility with newer hardware and ecosystem (logged by strato-transcripts, January 2026)
  - Requests relaxing exact pins to version ranges to support Blackwell GPUs and security updates
  - Proposes `torch>=2.8.0,<3.0` instead of `torch==2.8.0`
- **Pull Request [#1977](https://github.com/pyannote/pyannote-audio/pull/1977)** - Relax torch/torchaudio/torchcodec version pins to ranges (submitted by @bobsummerwill, January 2026) ✅
  - Fork: https://github.com/bobsummerwill/pyannote-audio
  - Branch: `fix/relax-torch-version-pins`
  - Changes: Replaces exact pins with version ranges while maintaining torchcodec<0.8 constraint

**Status**: 🟢 **PR submitted by us** - Awaiting maintainer review and merge

### Tracking Note

The repo currently tracks the runtime torchcodec workaround in issue `#36`. Issue `#44` was a documentation-only duplicate and can be closed when this document is kept current.

---

## Quick Reference: Monitoring Commands

```bash
# Check all package versions at once
pip list | grep -E "(whisperx|pyannote|speechbrain|torch)"

# Check PyPI for new releases
pip index versions whisperx
pip index versions pyannote.audio
pip index versions speechbrain

# Check GitHub releases
# WhisperX: https://github.com/m-bain/whisperx/releases
# pyannote.audio: https://github.com/pyannote/pyannote-audio/releases
# SpeechBrain: https://github.com/speechbrain/speechbrain/releases
```

---

## Removal Checklist

When considering removing a workaround, verify:

### For Workaround #1 (WhisperX token):
```bash
# 1. Check WhisperX uses new token parameter
grep -r "use_auth_token" venv/lib/python*/site-packages/whisperx/
# Should return empty after fix

# 2. Test without patch
# Remove sed commands from install script and reinstall
```

### For resolved SpeechBrain upgrade:
```bash
# 1. Verify SpeechBrain version
python3 -c "import importlib.metadata as m; print(m.version('speechbrain'))"
# Should print 1.1.0 or newer

# 2. Test metadata read under torchaudio 2.9+
python3 -c "from speechbrain.dataio.dataio import read_audio_info; print('ok')"
```

### For Workaround #2 (PyTorch weights_only):
```bash
# 1. Test if pyannote loads without patch
python3 -c "
import torch
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization')
print('✓ Loaded without weights_only workaround')
"

# 2. Verify OmegaConf not in checkpoints
# Check pyannote release notes for checkpoint format changes
```

### For Workaround #3 (pyannote version pin):
```bash
# 1. Check pyannote dependency specification
pip show pyannote.audio | grep Requires
# Should show torch>=2.8.0,<3.0 (not torch==2.8.0)

# 2. Test installation
pip install --dry-run "pyannote.audio>=4.0.2"
# Should not downgrade torch to 2.8.0
```

---

## Quarterly Review Schedule

**Next Review**: July 2026

### Review Checklist

1. ✅ Check for new releases of all upstream packages
2. ✅ Review GitHub issues for status updates
3. ✅ Test if workarounds can be removed
4. ✅ Update this document with findings
5. ✅ Update version pins if safe to do so

**Set calendar reminder**:
```bash
# Add to crontab or calendar:
# Every 3 months: Review strato-transcripts workarounds
```

---

## Summary Table

| Workaround | Upstream Package | Status | Estimated Fix | Likelihood | Removal Priority |
|------------|------------------|--------|---------------|------------|------------------|
| #1: Token param | WhisperX | 🟡 Partial upstream progress, still required on released wheels | Unknown | Medium | High |
| #2: weights_only | Lightning / pyannote.audio | 🟡 Still required on released packages | Unknown | Medium | Low |
| #3: torch/codec pinning | pyannote.audio / torchcodec | 🟡 Still required on released packages | Unknown | Medium | High |

### Legend
- 🟢 **PR submitted** - Fix submitted, awaiting merge
- 🟡 **Open** - Issue known, no fix yet
- ✅ **Fixed** - Fix exists but not released
- 🔴 **Blocked** - Requires major architectural changes

---

## Conclusion

As of April 15, 2026:
- The SpeechBrain torchaudio workarounds were removed after validating SpeechBrain 1.1.0 on the current runtime.
- Three runtime workarounds remain active.
- Several issue comments and assumptions from early 2026 were too optimistic because they relied on unreleased upstream code.

These are still compatibility bridges, but they should be revalidated against released wheels rather than upstream `main` branches or issue comments.

---

**Maintainer**: Check this document quarterly and update status based on upstream releases.
