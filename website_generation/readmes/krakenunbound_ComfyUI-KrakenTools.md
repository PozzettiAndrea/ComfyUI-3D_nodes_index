# 🦑 ComfyUI-KrakenTools

High-utility nodes for ComfyUI with a focus on **Flux 1 Dev** workflows and **Ultimate SD Upscale** enhancement loops.

**Why this exists:** when your “final” resolution is relatively small (e.g., 736×1344 portraits), running *no* real upscale in Ultimate SD Upscale (USDU) often doesn’t add detail. The Kraken approach enforces a true enlarge pass (e.g., 1.5×–2×), then **downscales back** to your exact target with high-quality filtering — preserving micro-detail and cleaning seams.

## ✨ Nodes

- **🦑 Kraken Flux Empty Latent Image** (`KrakenFluxEmptyLatentImage`)
  - Builds a Flux-style latent and exposes canonical **preset** + **resolution** strings for downstream nodes.
  - Outputs a small UI preview so you always see the intended canvas size.

- **🦑 Kraken Upscale & Tile Calc** (`KrakenUpscaleTileCalc`)
  - Computes a uniform upscale factor to *cover* your target, aligns to model-friendly multiples, and suggests tile sizes + overlaps for USDU.
  - **New:** `min_upscale_policy` (auto/off/1.5x/2.0x/custom) guarantees USDU *actually* upscales, even when target==source.

- **🦑 Kraken Resolution Helper (Exact)** (`KrakenResolutionHelper`)
  - Exact-size finisher: **keep proportion** (contain + pad), **pad** (with anchors), **fill/crop** (cover), or **stretch**.
  - Downscales without cropping and **guarantees final WxH**. With `allow_upscale=False`, it will never enlarge in the final step.

## 🛠 Installation

1. Locate your ComfyUI `custom_nodes` directory.
2. Clone or copy this repo into it:
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/<your-user>/ComfyUI-KrakenTools.git
   ```
3. Restart ComfyUI.

### Requirements
- ComfyUI (latest)
- Python deps: `torch`, `numpy`, `Pillow` (bundled in ComfyUI)
- Ultimate SD Upscale node pack (for USDU) installed separately

## 🚀 Usage (portrait example 736×1344)

1. **Flux latent** → add `KrakenFluxEmptyLatentImage` and pick your preset (e.g., 736×1344).  
   Outputs: `LATENT`, `resolution` (e.g., "736 x 1344"), `preset_out` (e.g., "736x1344"), width/height, preview

2. **Upscale planning** → add `KrakenUpscaleTileCalc`  
   - `resolution_in` ← latent.`resolution`  
   - `preset_in` ← latent.`preset_out`  
   - `min_upscale_policy` = **auto** (2× for small canvases), or force **"2.0x"**

3. **USDU** → add *Ultimate SD Upscale* (regular node)  
   - `upscale_by` ← tile calc.`upscale_by`  
   - Tile/overlap settings ← tile calc outputs  
   - Denoise ~0.2–0.35

4. **Final sizing** → add `KrakenResolutionHelper`  
   - `image` ← USDU output  
   - `preset_in` ← tile calc.`target_resolution` (or latent.`preset_out`)  
   - `mode` = **keep proportion**, `interpolation` = **lanczos**, `allow_upscale` = **False**  
   - Output is **exact 736 × 1344** with extra micro-detail

## 🧭 Contributing
See **CONTRIBUTING.md**.

## 🪪 License
MIT © 2025 **The Kraken** — X: @KrakenUnbound · YouTube: /@KrakenUnbound
