# Batch Whisper (3 Speakers, Timestamped) — ComfyUI Node

A lightweight ComfyUI extension node that runs OpenAI Whisper to transcribe up to 3 audio inputs, merges and sorts timestamped segments, and outputs a single timestamped transcript string.

- Node class: [`__init__.BatchWhisperNode`](__init__.py)  
- Implementation file: [__init__.py](__init__.py)  
- Core helpers: [`__init__.WhisperModelWrapper`](__init__.py), [`__init__.WhisperPatcher`](__init__.py), [`__init__.WHISPER_PATCHER_CACHE`](__init__.py), [`__init__.WHISPER_MODEL_SUBDIR`](__init__.py)

Installation
1. Drop the folder containing `__init__.py` into your ComfyUI extensions directory (e.g., ComfyUI/extensions/batch_whisper_extension).
2. Restart ComfyUI. The node will appear under the "Audio/Transcription" category as "Batch Whisper (3 Speakers, Timestamped)".

What this node does
- Accepts three audio inputs plus speaker name strings.
- Loads a Whisper model (selectable from the model list in the node) using a VRAM-safe patcher/cache.
- Saves each incoming waveform to a temporary WAV, transcribes with Whisper (word-level timestamps), and collects segments.
- Merges all segments, sorts by start time, and returns a timestamped transcript as a single STRING output.

Inputs
- audio1, audio2, audio3 (AUDIO): Audio objects produced by ComfyUI audio sources.
- speaker1, speaker2, speaker3 (STRING): Speaker labels to prefix each segment (defaults: Speaker1/2/3).
- model_name (enum): Whisper model selection; defaults to `large-v3-turbo`.
- language (optional): "auto" or a language selection; maps to Whisper language codes.
- prompt (optional STRING): Initial prompt passed to Whisper.

Output
- STRING: One combined transcript with speaker labels and timestamps formatted as:
  SpeakerName [start-end]: transcript text

Notes & behavior
- Model loading and offloading are handled by the VRAM-safe classes:
  - [`__init__.WhisperModelWrapper`](__init__.py) wraps a Whisper model instance and tracks weight memory.
  - [`__init__.WhisperPatcher`](__init__.py) manages loading/unloading and integrates with ComfyUI model management.
  - Patcher instances are cached in [`__init__.WHISPER_PATCHER_CACHE`](__init__.py) by model name to avoid repeated reloads.
- Temporary WAV files are written to the temp directory obtained from the included `folder_paths` helper. Temporary files are created per transcription call.
- If the Whisper model fails to load or transcription raises an exception for a particular input, the node injects an "[Error: ...]" segment for that speaker and continues.

Troubleshooting
- If you see memory errors, try a smaller model (e.g., `small`, `base`).
- If the node returns "Error: Whisper model failed to load.", ensure ComfyUI's device settings and PyTorch/CUDA are configured correctly.
- Check ComfyUI logs for messages produced by the node's logger.

References
- Node implementation: [`__init__.BatchWhisperNode`](__init__.py) — [__init__.py](__init__.py)  
- Model wrapper/patcher: [`__init__.WhisperModelWrapper`](__init__.py), [`__init__.WhisperPatcher`](__init__.py)  
- Cache constant: [`__init__.WHISPER_PATCHER_CACHE`](__init__.py)  
- Model subdirectory constant: [`__init__.WHISPER_MODEL_SUBDIR`](__init__.py)

License & credits
- Uses the open-source Whisper transcription code (whisper package). See upstream licenses for model and code terms.