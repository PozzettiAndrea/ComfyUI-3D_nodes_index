# Prompt Camera Assistant (ComfyUI Node)

**Prompt Camera Assistant** is a custom **ComfyUI node** that provides a structured, extensible camera and lens library for generating **photography-accurate and cinema-aware AI prompts**.

The node allows users to select **Still or Video workflows**, then dynamically choose cameras, lenses, film stocks, exposure settings, and stylistic modifiers (bokeh, focus, motion blur) that are assembled into clean, consistent prompt text.

This project is designed for:

-   Prompt engineers
-   Generative photography & cinematography
-   ComfyUI power users
-   Workflow-driven AI creators

---

## Features

-   📷 **Still vs Video mode selection**
-   🎥 **Cinema camera support** (ARRI, RED, Blackmagic, Sony, Canon)
-   📸 **Still camera support** (DSLR, Mirrorless, Film)
-   🔍 **Lens types & focal behavior**
-   🎞 **Iconic film stocks** (negative, slide, instant, digital looks)
-   ⚙️ **Exposure controls** (aperture, ISO, shutter speed)
-   ✨ **Stylistic modifiers**
    -   Bokeh styles
    -   Focus styles
    -   Motion blur presets
-   🧩 Built as a **ComfyUI custom node**
-   🛠 Backend-driven dropdowns (clean UI, dynamic expansion)

---

## Why Camera & Lens Metadata in AI Prompts?

Modern diffusion and generative models respond strongly to **photographic language**:

-   Camera systems influence realism and tone
-   Lens types affect perspective and depth
-   Film stocks guide color science and contrast
-   Exposure terms shape lighting and motion

This node standardizes those inputs so users don’t need to memorize or manually type camera syntax.

---

## Project Structure

PromptCameraAssistant/
├── nodes.py
├── README.md

-   `nodes.py`  
    Contains:
    -   `PromptCameraLibrary` – the backend camera/lens/film data
    -   `PromptCameraAssistant` – the ComfyUI node definition

---

## Installation

1. Navigate to your ComfyUI custom nodes directory: ComfyUI/custom_nodes/

2. Clone this repository into ComfyUI's `custom_nodes` directory:

```
git clone https://github.com/bcasadei/ComfyUI-Prompt-Camera-Assistant.git
```

3. Restart ComfyUI

The node will appear under: CATEGORY: Prompt / Camera

---

## Node Overview

### PromptCameraAssistant

**Inputs**

-   Mode: Still / Video
-   Camera
-   Lens type
-   Film / Sensor look
-   Aperture (f-stop)
-   ISO
-   Shutter speed
-   Bokeh style
-   Focus style
-   Motion blur preset

**Output**

-   A formatted prompt string (or integrated into your workflow)

---

## Camera Library Coverage

### Still Cameras

-   DSLR
-   Mirrorless
-   Film

Includes:

-   Canon, Nikon, Sony, Fujifilm, Leica, Hasselblad, Pentax
-   Instant film (Polaroid)
-   Medium format systems

### Cinema Cameras

-   ARRI ALEXA series
-   RED DSMC / V-RAPTOR
-   Blackmagic Pocket & URSA
-   Sony FX & Venice
-   Canon Cinema EOS
-   Panasonic Varicam / EVA

---

## Film Stocks

### Color Negative

-   Kodak Portra 160 / 400 / 800
-   Kodak Gold 200
-   Fujifilm Pro 400H

### Slide (Transparency)

-   Kodachrome
-   Fujifilm Velvia 50 / 100
-   Fujifilm Provia 100F
-   Kodak Ektachrome E100

### Instant

-   Polaroid Originals / Polaroid Now

### Digital Looks

-   Clean digital
-   Cinema digital
-   Vintage digital CCD

---

## Design Philosophy

-   **Dropdown-first UX** (no free-text chaos)
-   **Real photographic language**
-   **Model-agnostic** (SD, Flux, Krea, future models)
-   **Expandable library** without breaking workflows
-   Focused on **visual outcome**, not camera specs trivia

---

## Roadmap (Optional)

-   Prompt string output node
-   Automatic prompt assembly templates
-   Per-model prompt tuning
-   Preset packs (cinematic, fashion, street, documentary)
-   UI grouping improvements

---

## License

MIT License  
Use freely, modify, fork, and build upon.

---

## Credits

Created by **Bill Casadei**  
Built for ComfyUI & generative photography workflows.

> NOTE: This project was created from the Comfy-Org cookiecutter template
> to simplify writing custom ComfyUI nodes and packaging them for distribution.
