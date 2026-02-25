ComfyUI-IndexTTS2
=================

Lightweight ComfyUI wrapper for IndexTTS 2 (voice cloning + emotion control). Nodes call the upstream inference code so behaviour stays matched with the original repo.

Original repo: https://github.com/index-tts/index-tts

![ComfyUI-IndexTTS2 nodes](images/overview.png)

## Updates
- 2025-10-13: Save Audio node now acts as an output node with an embedded player overlay for instant preview inside the graph (no need for downstream preview nodes).
- 2025-10-08: Default FP32 with optional FP16 toggle, output gain control, and a Save Audio helper node (wav/mp3 + quality parameters).
- 2025-09-22: Added IndexTTS2 Advanced node exposing sampling, speed, seed, and other generation controls.

## Install
- Clone this repository into `ComfyUI/custom_nodes/`
- Inside your ComfyUI Python environment:
  ```bash
  pip install wetext
  pip install -r requirements.txt
  ```

## Models
- Create `checkpoints/` in the repo root and copy the IndexTTS-2 release there (https://huggingface.co/IndexTeam/IndexTTS-2/tree/main). Missing files will be cached from Hugging Face automatically.

## Nodes
- **IndexTTS2 Simple** - speaker audio, text, optional emotion audio/vector; outputs audio + status string. Default FP32, optional FP16 toggle, output gain control.
- **IndexTTS2 Advanced** - Simple inputs plus overrides for sampling, speech speed, pauses, CFG, seed, FP16 toggle, and output gain.
- **IndexTTS2 Emotion Vector** – eight sliders (0.0–1.4, sum <= 1.5) producing an emotion vector.
- **IndexTTS2 Emotion From Text** – requires ModelScope and local QwenEmotion; turns short text into an emotion vector + summary.
- **IndexTTS2 Save Audio** - saves generated audio tensors to disk with wav/mp3 options and surfaces an inline player directly on the node after execution.

## Examples
- Speaker audio -> IndexTTS2 Simple -> Preview/Save Audio
- Speaker + emotion audio -> IndexTTS2 Simple -> Save
- Emotion Vector -> IndexTTS2 Simple -> Save
- Emotion From Text -> IndexTTS2 Simple -> Save

## Troubleshooting
- Windows only so far; DeepSpeed is disabled.
- Install `wetext` if the module is missing on first launch.
- Emotion vector sum must stay <= 1.5.