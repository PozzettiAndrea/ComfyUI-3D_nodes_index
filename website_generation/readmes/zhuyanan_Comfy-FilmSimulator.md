# Comfy-FilmSimulator (SmartHDR Edition)

ComfyUI node: realistic, adaptive film simulation for photographic and cinematic looks, now with full HDR support and DNG reading capabilities.

This repository provides a ComfyUI-compatible node implementation that simulates film stock response, grain, bloom/halation and tone mapping. It features advanced HDR processing, a native DNG reader, and high-quality AVIF/HEIC export.

---
## Features & Nodes

### 1. DNG Image Reader (Rawpy)
- **Category**: `SmartHDR`
- **Description**: High-fidelity DNG/RAW decoding using `rawpy`.
- **Key Features**:
  - Detailed metadata extraction (Camera model, Bayer pattern, White Balance).
  - Advanced White Balance modes (As Shot, Auto, Daylight, etc.).
  - Adjustable Physical Exposure Gain.
  - Linear/HDR output support.

### 2. Film Simulation V4.1 (HDR Capable)
- **Category**: `SmartHDR`
- **Description**: Professional-grade film simulation node with HDR workflow.
- **Key Features**:
  - **Adaptive Physical White Balance**: Real Kelvin-based color temperature adjustment.
  - **Auto Exposure**: Automatic luminance normalization to 18% gray.
  - **HDR Workflow**: Processes in high dynamic range linear space.
  - **Realistic Grain**: Coherent grain with crosstalk and luminance-based masking.
  - **Halation/Bloom**: Physically inspired light bleeding.
  - **SDR Preview**: Integrated filmic tone mapping for real-time SDR monitoring while preserving HDR data.

### 3. Save AVIF/HEIC HDR (Native)
- **Category**: `SmartHDR`
- **Description**: Saves images in high-bit depth HDR formats.
- **Key Features**:
  - Supports **AVIF** and **HEIC**.
  - **PQ (Perceptual Quantizer)** transfer function for genuine HDR display.
  - Rec.2020 color space conversion.
  - 10-bit and 12-bit encoding support (via `pillow-heif`).

---

## Installation (ComfyUI)

1. Install the required Python packages:

```bash
pip install numpy opencv-python rawpy pillow-heif torch
```

- Note: Install `torch` according to your platform/GPU configuration (see https://pytorch.org).

2. Install the node:
   - Copy all files (`__init__.py`, `dng_reader.py`, `film_sim.py`, `save_avif_hdr.py`, `films.json`) into a folder under your ComfyUI `custom_nodes` directory. Example:

```text
<ComfyUI root>/
  custom_nodes/
    Comfy-FilmSimulator/
      __init__.py
      dng_reader.py
      film_sim.py
      save_avif_hdr.py
      films.json
```

3. Restart ComfyUI. The nodes will appear under the `SmartHDR` category.

---

## Workflow Example

1. **Load**: Use `DNG Image Reader` to load a RAW file with `linear_output` enabled.
2. **Process**: Connect to `Film Simulation V4.1`. Set `is_linear_input` to True. Adjust `wb_temperature_K` and `exposure`.
3. **Save**: Connect the `hdr_image` output to `Save AVIF/HEIC HDR` to get a true HDR file, and use `preview_sdr` for standard ComfyUI previews.

---

## Preset Library (`films.json`)

Includes many classic stocks:
- **Color**: Kodak Portra (160, 400, 800), Fuji Pro 400H, Cinestill (400D, 800T), LomoChrome, etc.
- **B/W**: Kodak Tri-X 400, T-Max 100, Ilford HP5 Plus, Fuji Acros 100, etc.

---

## Development & Attribution

Maintainer: yanan.zhu@gmail.com
Repo: https://github.com/zhuyanan/Comfy-FilmSimulator

---

## License

This repository contains a `LICENSE` file — please refer to it for terms.
