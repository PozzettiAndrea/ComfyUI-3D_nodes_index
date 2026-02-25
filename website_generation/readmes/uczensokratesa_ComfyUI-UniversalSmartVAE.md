# ComfyUI-UniversalSmartVAE
VRAM-safe VAE decoder for video latents in ComfyUI. Decodes 5D video latents in temporal batches to prevent GPU memory explosions.
# 🎬 UniversalSmartVAEDecode for ComfyUI

**UniversalSmartVAEDecode** is a VRAM-safe VAE decoder node for **video latents** in ComfyUI.

It solves a common problem when working with long video sequences (especially LTX-2):
decoding all frames at once often causes **VRAM explosions or crashes**.

This node decodes video latents **in temporal batches**, keeping GPU memory usage under control.

---

## ✨ Features

- ✅ Supports **5D video latents** `[B, C, F, H, W]`
- ✅ Temporal batching (`frames_per_batch`)
- ✅ Compatible with **LTX-2** and standard ComfyUI VAEs
- ✅ No spatial tiling, no heuristics, no guessing
- ✅ Clean VRAM release between batches
- ✅ Simple, maintainable, production-safe code

---

## 🚫 What this node does NOT do

This is a **deliberately conservative design**.

- ❌ No spatial tiling
- ❌ No scale-factor guessing
- ❌ No format “auto-magic”
- ❌ No experimental blending logic

If your workflow needs spatial tiling, that should be handled **before or after decoding**, not inside VAE decode.

---

## 🧠 Why this node exists

Standard ComfyUI VAE decoding often fails with:

- Long video sequences
- High resolutions
- LTX-style video latents
- Limited VRAM

Instead of decoding the full video at once, this node decodes **small frame batches**, dramatically reducing peak VRAM usage.

---

## 📥 Installation

Clone into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/uczensokratesa/ComfyUI-UniversalSmartVAE.git
## Why this node exists (Philosophy)

Standard VAE decoding in ComfyUI attempts to decode whole video latents at once.
For long sequences (hundreds+ frames), high resolutions, or VAEs like LTX-2,
this often leads to **VRAM spikes and out-of-memory crashes**.

This project addresses the problem with a **simple and robust strategy**:
decode in **temporal batches** instead of trying to decode all frames at once.

This design follows three core principles:

1. **Deterministic behaviour**  
   Avoid heuristics that guess latent scales, adaptive tiling or other magic.

2. **Fail early and clearly**  
   If input shapes are unsupported, produce a readable error instead of silent corruption.

3. **Stability first**  
   Prioritise working reliably for real workflows, rather than chasing every possible edge shape.
## What this node DOES and DOES NOT do

### ✅ Supported

- temporal batching of video latents
- safe VRAM usage for long videos
- normalization of common VAE output layouts
- compatibility with LTX-2 and standard ComfyUI VAEs

### ❌ Not supported / outside scope

- spatial tiling (splitting each frame into patches)
- overlap blending between tiles
- automatic detection of VAE downscale factors
- heuristic layout guessing

If you need spatial tiling, that should be done
separately (before decoding or after decoding),
not inside this node’s temporal batching logic.

## Stability & Compatibility Notes

- This node does not attempt to tile frames spatially.
  That class of problems requires a different set of algorithms
  and is not covered here to avoid complex edge-case bugs.

- LTX-2 VAEs sometimes return outputs in different layouts.
  This node normalizes typical variants to a common
  `[F, H, W, 3]` format, but unusual VAEs may require custom handling.

- The goal is **stability over feature breadth**:
  if something *can* go wrong, the node will fail with an error
  rather than produce corrupted output.

- If your workflow requires additional transformations,
  chain them in later nodes or use external scripts.
## How to use this node in ComfyUI

1. Connect your video latent tensor (5D) to `samples`
2. Connect your chosen VAE
3. Adjust `frames_per_batch` according to your GPU:
   - 8–16 GB VRAM: 2–4
   - 24+ GB VRAM: 4–8
4. Run the workflow[Sampler] → [UniversalSmartVAEDecode] → [Save Images / Preview]

## Acknowledgements

This node was developed as a collaborative effort:
- Project instigation and motivation: UczenSokratesa
- Batch decoding architecture and implementation: ChatGPT (GPT-5.x)
- Community inspiration: prior fixes from Gemini, Claude, Grok






