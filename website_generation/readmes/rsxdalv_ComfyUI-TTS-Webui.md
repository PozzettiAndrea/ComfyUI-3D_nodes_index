# ComfyUI: TTS WebUI (OpenAI-style) nodes

This package provides ComfyUI custom nodes that call a TTS WebUI OpenAI-style HTTP endpoint (POST /v1/audio/speech) and return in-memory AUDIO usable in ComfyUI workflows.

![workflow example](workflow.png)

## What it does

- Sends text + options to a TTS WebUI endpoint and requests WAV output.
- Converts the returned WAV bytes into a ComfyUI AUDIO object (torch.Tensor waveform + sample rate).
- Optionally saves the WAV to the ComfyUI output/audio folder and returns metadata JSON.

## Nodes included

- TTS WebUI via API — class `TTSWebUI_OpenAI_TTS` (generic, "jack of all trades")
- TTS Kokoro — class `TTS_KokoroNode`
- TTS Chatterbox — class `TTS_ChatterboxNode`
- TTS StyleTTS2 — class `TTS_StyleTTS2Node`
- TTS Kitten TTS — class `TTS_KittenTTSNode`
- TTS F5-TTS — class `TTS_F5TTSNode`
- TTS Preset — class `TTS_GlobalPresetNode`

All nodes share a minimal helper (`NodeTTSBase`) for HTTP and response handling. Each node builds its own JSON payload explicitly to avoid hidden cross-file magic. Common required inputs `text` and `api_base` are provided via a small `required_inputs()` helper on the base class to reduce duplication.

### Common required inputs

- text (STRING, multiline) — text to synthesize
- api_base (STRING) — base URL of your TTS WebUI (default: `http://127.0.0.1:7778`)

### Common optional inputs

- api_key (STRING, password) — API key for the TTS server (if required)
- timeout_sec (INT) — request timeout in seconds
- channels_first (BOOLEAN) — AUDIO layout: (C, N) if True else (N, C)
- also_save_wav (BOOLEAN) — if True, saves a WAV under output/audio and returns the path
- save_prefix (STRING) — filename prefix for saved WAVs
- return_metadata (BOOLEAN) — if True, returns a metadata JSON string

Model-specific nodes add their own inputs (e.g., voice, speed, alpha/beta, etc.) and build the corresponding payload under the hood.

### Advanced: raw payload override (generic node)

`TTSWebUI_OpenAI_TTS` has an `advanced_request_json` input to fully override the default payload. Example body sent to `/v1/audio/speech`:

```json
{
  "model": "kokoro",
  "input": "Hello from ComfyUI",
  "voice": "random",
  "speed": 1.0,
  "response_format": "wav",
  "params": {"temperature": 0.7}
}
```

## Installation / Requirements

1. Place this folder inside your ComfyUI `custom_nodes` directory.
2. Ensure the environment has these Python packages installed: `requests`, `numpy`, `torch`.
   - If your ComfyUI environment already has `torch` installed, no extra action is required.

## API key detection

If your TTS server requires an API key you can either:
- pass it into the `api_key` input, or
- set the environment variable `TTS_WEBUI_OPENAI_API_KEY` to your API key (preferred).

For backward compatibility the module will also check `SAI_API_KEY`. As a local-file fallback the helper also reads `tts_api_key.txt` or `sai_platform_key.txt` placed next to the custom node. When a key is found, requests include the header `Authorization: Bearer <key>`.

## Layout

- `nodes/` — one node per file (generic + per-model)
- `nodes/_base.py` — `NodeTTSBase` providing HTTP and finalize helpers and `required_inputs()`
- `utils/` — small helpers for audio I/O, paths, filenames
- `__init__.py` — package exports for ComfyUI

## Notes

This repository originally included a Stability API template. The TTS nodes are independent of that code; any legacy modules (`tts_base.py`, `tts_models.py`, `nodes/_shared.py`) are now deprecated and will raise a clear ImportError if imported.

---

License: see `LICENSE`

```
