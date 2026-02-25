# ⚡ CornmeisterNL PowerPack for ComfyUI

A curated collection of **power‑user focused ComfyUI custom nodes**, designed to streamline prompt building, LoRA workflows, resolution management, metadata‑clean image saving, and model loading — with a strong focus on **CivitAI‑ready outputs** and **production‑grade usability**.

This project has grown organically from real daily use and is opinionated by design.

---

## ✨ Features Overview

### ⚡ Power Prompt Builder
Generate advanced image prompts using the OpenAI Responses API.
- Base prompt + instruction driven
- Supports GPT‑5.x family models
- Clean output mode (prompt only, no chatter)
- Ideal for Z‑Image / cinematic prompt styles

### ⚡ Power Text Concat
Concatenate multiple text inputs into a single prompt string.
- Optional trigger input
- Unlimited chained inputs
- Auto‑skips disabled or empty inputs
- Custom separator support

### ⚡ Power LoRA Configurator
Configure a single LoRA with:
- LoRA file selection
- Trigger word
- Model & CLIP strength

Outputs a reusable LoRA config object.

### ⚡ Power LoRA Selector
Select **exactly one active LoRA** from multiple configurators.
- Model + CLIP passthrough
- Trigger output for prompt injection
- Designed for fast character testing

### ⚡ Power Res
Resolution & latent generator with JSON‑based presets.
- Presets loaded from `presets/*.json`
- Manual override option
- Outputs:
  - LATENT
  - WIDTH
  - HEIGHT

### ⚡ Power Diffusion Model Loader
UNet‑based diffusion model loader.
- Reads from `models/unet`
- Outputs:
  - MODEL
  - model_name (string, usable for metadata)

### ⚡ Power Save Image
Production‑grade image saving node with **dual‑output strategy**.

#### Share Output (CivitAI‑ready)
- Clean PNG/JPEG
- Metadata stored as:
  - `parameters` (PNG tEXt chunk)
  - EXIF UserComment (JPEG)
- Fully compatible with CivitAI

#### Full Flow Archive (optional)
- PNG with embedded full ComfyUI workflow
- Separate `.txt` containing full workflow JSON
- Ideal for archival & reproducibility

#### Features
- Two output paths:
  - Share path
  - Full‑flow path
- Per‑save toggles
- Time macros supported:
  ```
  [time(%Y-%m-%d)]
  ```

---

## 📂 Installation

Clone or download into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Cornmeister/ComfyUI-CornmeisterNL-PowerPack.git
```

Restart ComfyUI.

You should see in the console:

```
⚡ [CornmeisterNL Powerpack] Backend loaded (v1.0.0)
```

---

## 🧠 Philosophy

- No unnecessary abstraction
- No forced pipes
- Everything optional unless truly required
- Nodes should **never break execution** when inputs are missing or disabled
- Metadata should be **share‑safe by default**, but full reproducibility must remain possible

---

## 🚀 Versioning

This repository follows **semantic versioning**:

- `v1.0.0` → First stable public release
- Patch versions → bugfixes
- Minor versions → new nodes or features
- Major versions → breaking changes

---

## 🧩 Requirements

- ComfyUI (recent)
- Python 3.10+
- Pillow
- Requests (for Power Prompt Builder)
- OpenAI API key (only if using prompt builder)

Set your API key as an environment variable:

```bash
OPENAI_API_KEY=sk-...
```

---

## 📜 License

MIT — do whatever you want, attribution appreciated.

---

## 👤 Author

**CornmeisterNL**  
Built by a power user, for power users.

⚡ Enjoy.
