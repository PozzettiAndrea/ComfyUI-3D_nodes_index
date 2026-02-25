# 👑 ComfyUI-FRED-Nodes v2

Custom ComfyUI nodes by **Fred** — all-in-one utilities and quality-of-life tools for image workflows.  
This v2 repo is a clean rewrite of [ComfyUI-FRED-Nodes](https://github.com/Poukpalaova/ComfyUI-FRED-Nodes), with improved nodes, bug fixes, and simplified structure.

---

## ✨ Features
- Enhanced **image saving** with metadata + grid support
- Smart **image cropping/tiling** with ratio/mask awareness
- Integrated **quality metrics** (BRISQUE, blur, SNR, compression)
- Simplified **parameters panel** for samplers/schedulers
- Utility nodes for **text metadata (XMP)** and **wildcard concatenation**
- Face detection and cropping
- Robust image loading with caching, indexing, and previews

---

## 🧩 Nodes Overview
## 📏 FRED_AutoCropImage_Native_Ratio

Automatically crop and resize images to match Stable Diffusion aspect ratios, or custom sizes.
Supports mask preservation and overlay preview.

Key features:

Auto-find closest SDXL ratio or use custom width/height

Mask-preserve mode ensures subject is not cut off

Cropping from center or offset (X/Y %)

Optional resize with upscale/downscale modes

Multiple-of rounding (2, 4, 8, …)

Preview with mask overlay

## 🪟 FRED_AutoImageTile_from_Mask

Split an image into tiles based on a mask or bounding box.
Useful for processing specific regions with controlled overlap.

Key features:

Auto grid from mask/BBOX with confidence adjustment

Manual rows/cols if desired

Overlap in X/Y

Grid preview overlay (bbox + lines)

## 📊 FRED_ImageQualityInspector

Evaluate image quality using multiple metrics, optionally within a mask.

Metrics:

BRISQUE (no-reference perceptual quality)

Blur (Laplacian variance)

SNR (signal-to-noise ratio, dB)

Compression proxy (raw vs JPEG@95 size)

Modes:

Raw metrics (real units, e.g. dB, Lap variance)

Normalized 0–100 scores (100 = best)

## 💾 FRED_Image_Saver

Advanced image saver with dynamic naming tokens and metadata embedding.

Key features:

Save single images, grid images, or both

Filename/path tokens: %date, %time, %model_name, %seed, %lora_name_X, …

Metadata embedding:

Automatic1111 “parameters” text

Prompts, workflow JSON, ComfyUI version

Optional JSON sidecar files

Grid saving:

Auto rows/cols up to max

Optional row/column labels

Metadata includes grid info

Outputs last saved image and grid paths.

## 🖼️ FRED_LoadImage_V8

Robust image loader with indexing, preview, and error logging.

Key features:

Modes: no_folder (direct image) or image_from_folder

Index control: fixed / increment / decrement / randomize

Skip invalid files, with persistent error log (~/.fred_logs)

Cache of folder index for performance

Optional preview images written to temp folder

Outputs include folder path, filename text, counts, skipped report

## 🙂 FRED_CropFace

Detect and crop faces using RetinaFace (facexlib).

Key features:

Face detection (multi-face; choose by ID)

Expand bounding box with margins

Preview overlay with detected faces

Outputs cropped face, preview, bbox, pixel ratios

⚙️ FRED_Simplified_Parameters_Panel

Expose a compact UI panel for common sampling parameters.

Outputs:

scale, denoise, guidance, steps

proper NOISE object

sampler/scheduler objects + names

sigmas tensor

Great for quick prototyping or simplified workflows.

## 📝 FRED_Text_to_XMP

Generate and attach XMP metadata to images (or sidecar .xmp).

Key features:

Embed prompts, negatives, parameters into standard XMP fields

Keywords → dc:subject (Lightroom/Bridge searchable)

Ratings, title, description, creator fields

Modes: embed into PNG/JPEG/TIFF or sidecar only

Token support: %date, %time, %model_name, %seed, …

## 🎲 FRED_WildcardConcat_Dynamic

Dynamic wildcard concatenation for prompt building.

Key features:

Add/remove blocks dynamically

Each block: toggle, wildcard file, line mode (random/fixed), weight

Prefix and suffix support

Custom string delimiter between blocks

Output = concatenated string with tokens expanded

## 📖 Usage Tips

Each node outputs a help string for quick reference inside ComfyUI.

For tutorials, check the Wiki
 (todo: add link).

Add screenshots of each node UI for clarity.

## 🛠️ License

MIT License — free to use and modify.
If you use these nodes in your workflows, a ⭐ on this repo is always appreciated.

---

## 📦 Installation
Clone or download this repo into your ComfyUI `custom_nodes/` folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Poukpalaova/ComfyUI-FRED-Nodes_v2.git
