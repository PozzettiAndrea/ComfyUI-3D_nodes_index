# ComfyUI-Meld

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Registry-green)](https://registry.comfy.org/)

[Japanese README](README.ja.md)

**Turn your generated images into a powerful asset database.**

ComfyUI-Meld transforms chaotic workflows into an organized, reusable pipeline. It automatically captures prompts, settings, and lineage, ensuring no generation is ever lost.

With the Meld Image Manager, you can unify search, tagging, and lineage tracking directly within ComfyUI. Find your best result, inspect its DNA, and iterate instantly.

---

## Image Manager (Meld Image Manager)

The Image Manager is an integrated image management system added to ComfyUI's sidebar. It speeds up browsing, searching, and organizing generated images, and makes it smoother to reuse past work back in your workflows.

- **Gallery**: Browse and organize generated images quickly
- **Detail Viewer**: Inspect and edit prompts, models, generation settings, notes, and tags
- **Advanced Search**: Filter flexibly by prompt/tags/date/model name and more
- **Lineage Tracking**: Visualize parent-child relationships such as img2img
- **Workflow Integration**: One-click load images and assist restoring settings and workflows

By default, **output images are automatically registered** when a workflow execution completes. If you additionally use [Meld Save Image](./docs/en/nodes/MeldSaveImage.md), you can enhance management with features like automatic tagging and explicitly specifying a source (parent) image.

For detailed usage, shortcuts, and search syntax, see [`docs/en/ImageManager.md`](./docs/en/ImageManager.md).

---

## Included Nodes (10 total)

See `docs/en/nodes/` for details.

| Node | Role (Summary) |
| :--- | :--- |
| **[Meld Prompt Constructor](./docs/en/nodes/MeldPromptConstructor.md)** | Build prompts from text files with dynamic syntax and automatically split negatives |
| **[Meld Auto Exposure](./docs/en/nodes/MeldAutoExposure.md)** | Analyze luminance and apply automatic gamma correction toward a target brightness |
| **[Meld Save Image](./docs/en/nodes/MeldSaveImage.md)** | Save images and auto-register to Image Manager (metadata, pHash-based lineage, tagging) |
| **[Meld Unified Loader](./docs/en/nodes/MeldUnifiedLoader.md)** | Combine checkpoint loading and base generation parameters, output reusable `base_settings` |
| **[Meld Unified Flux Loader](./docs/en/nodes/MeldUnifiedFluxLoader.md)** | Flux-specific unified loader with Guidance input and fixed CFG handling |
| **[Meld Settings Unpacker](./docs/en/nodes/MeldSettingsUnpacker.md)** | Unpack a `BASE_SETTINGS` dict into seed/steps/cfg/resolution and other parameters |
| **[Meld Image Loader](./docs/en/nodes/MeldImageLoader.md)** | Load an image, extract prompt/settings from embedded metadata, and attempt model loading |
| **[Meld Image Loader Batch](./docs/en/nodes/MeldImageLoaderBatch.md)** | Load images from a directory sequentially by index (including metadata analysis/restoration) |
| **[Meld Instant Pixelate](./docs/en/nodes/MeldPixelate.md)** | Pixelate via downsample then nearest-neighbor upscale (mosaic / pixel art) |
| **[Meld Infinite Heart Generator](./docs/en/nodes/MeldPatternHeart.md)** | Decorate by auto-placing heart patterns on grids, edges, and more |

---

## Installation

### Recommended: ComfyUI Manager or Registry

In ComfyUI Manager's search, type **"Meld"** and install it.
Or run the following command from the CLI:

```bash
comfy node install HappyOnigiri/ComfyUI-Meld

```

### Manual Installation

Run the following commands under your `custom_nodes` directory, then restart ComfyUI:

```bash
git clone https://github.com/HappyOnigiri/ComfyUI-Meld.git
cd ComfyUI-Meld
pip install -r requirements.txt

```

---

## Specs & Requirements

- **Supported OS**: Windows / Linux / macOS
- **Python**: 3.10+ recommended
- **License**: Apache License 2.0 (commercial use and modifications allowed)

---

## Privacy

We extract **only generation-related information** (prompt/workflow/etc.) from image metadata, and do not read private EXIF data such as GPS. File loading is limited to **the directory you specify and its subdirectories** (we recommend managing permissions appropriately).

---

## Support & Feedback

We welcome all kinds of feedback, including bug reports, feature requests, and questions!
Please feel free to open an issue on GitHub.

* **Bug Report**: Please include error logs or screenshots if possible.
* **Feature Request**: We would love to hear your ideas for new features or improvements.

> **Notice:** Please note that the developer is Japanese. I will respond to your issues using **machine translation**. To ensure smooth communication, please try to use **simple English** and attach **screenshots or logs** whenever possible.

[Open GitHub Issues](https://github.com/HappyOnigiri/ComfyUI-Meld/issues)

---

## Contribution

**Pull Requests (PRs) are warmly welcomed, from typo fixes to new features!**

Your code doesn't have to be perfect. Please feel free to submit even if it's just "functional" for now.

---

**Developed by**: [HappyOnigiri](https://github.com/HappyOnigiri)

---
