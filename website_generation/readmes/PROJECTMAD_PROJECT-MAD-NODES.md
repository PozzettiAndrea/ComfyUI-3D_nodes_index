<div align="center">

# PROJECT-MAD-NODES

[![Version](https://img.shields.io/badge/version-1.2.2-red.svg)](https://registry.comfy.org/publishers/projectmad/nodes/project-mad-nodes)
[![Changelog](https://img.shields.io/badge/Changelog-View-orange?logo=readme&logoColor=white)](./CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)]()

**Advanced LoRA Scheduling and Visual Prompt Management for ComfyUI**

[Installation](#installation) | [Nodes](#nodes) | [Technical Docs](./docs/TECHNICAL.md) | [Troubleshooting](./docs/TROUBLESHOOTING.md)
</div>

---

> [!WARNING]
> **Compatibility Note: ComfyUI Nodes 2.0**
>
> **Visual Prompt Gallery** is currently **incompatible** with the new experimental "Nodes 2.0" (Vue-based) rendering system. If you have enabled new frontend in ComfyUI settings, gallery interface will not appear. **Multi Scheduled LoRA Loader** remains fully functional in both versions.

 ## Introduction

<table>
<tr>
<td width="50%" valign="top">

### 🟣 Dynamic LoRA Control

Traditional LoRA loaders apply **static strength** throughout generation. Multi Scheduled LoRA Loader lets you **draw curves** that control strength over time - fade-ins, fade-outs, complex patterns, or per block weighting.

</td>
<td width="50%" valign="top">

### 🔵 Visual Inspiration

Visual Prompt Gallery is an **integrated image browser** that extracts prompts from your reference images. Switch creations and styles instantly without leaving your workflow.

</td>
</tr>
</table>

---

## Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open **ComfyUI Manager** in your ComfyUI interface
2. Click **Install Custom Nodes**
3. Search for `PROJECT-MAD-NODES`
4. Click **Install** and restart ComfyUI

### Method 2: Manual Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/PROJECTMAD/PROJECT-MAD-NODES.git
```
---

## Requirements

| Requirement | Target | Details |
|-------------|--------|---------|
| [**ComfyUI**](https://github.com/Comfy-Org/ComfyUI) | Both | Latest version recommended |
| **Python** | Both | 3.10 or higher |
| **Internet** | Visual Prompt Gallery | Required once for ExifReader library (Visual Prompt Gallery only) |
| [**LoRA Manager**](https://github.com/willmiao/ComfyUI-Lora-Manager) | Multi Scheduled LoRA Loader | **Highly recommended** for better LoRA architecture and trigger words detection, but also showing image previews. LoRA Manager → **Fetch** (to build metadata) |

---

## Nodes

<table>
<tr>
<td align="center" width="50%">

### Multi Scheduled LoRA Loader

![Preview](/assets/multi_scheduled_lora_loader_preview.webp)

**Draw strength curves. Control timing. Stack multiple LoRAs.**

<sup>Category: `advanced/hooks/scheduling`</sup>

[**Full Documentation**](./docs/MULTI_SCHEDULED_LORA_LOADER.md)

</td>
<td align="center" width="50%">

### Visual Prompt Gallery

<img src="./assets/visual_prompt_gallery_(exif)_preview.gif" width="100%" alt="Visual Prompt Gallery">

**Browse references. Extract metadata. Switch styles instantly.**

<sup>Category: `utils`</sup>

[**Full Documentation**](./docs/VISUAL_PROMPT_GALLERY.md)

</td>
</tr>
</table>

---

## Quick Feature Overview

### Multi Scheduled LoRA Loader

| Feature | Description |
|---------|-------------|
| **Visual Curve Editor** | Draw schedules with an intuitive graphical interface |
| **Multi-LoRA Timeline** | Manage multiple LoRAs in a unified view |
| **Block Weight Control** | Fine-tune individual UNet blocks |
| **Architecture Detection** | Automatic SDXL, FLUX, SD1.5, SD3 identification |
| **Profile System** | Save and switch between configurations |
| **Undo/Redo** | Full history stack with keyboard shortcuts |

### Visual Prompt Gallery

| Feature | Description |
|---------|-------------|
| **Drag & Drop Import** | Drop images directly onto the node |
| **Multi-Format Extraction** | EXIF, PNG chunks, CivitAI, A1111 metadata |
| **Gallery View** | Resizable floating window with aspect modes |
| **Offline Capable** | Works without internet after first load |
| **Context Menu** | Right-click for fullscreen and management |

---

## Documentation Index

<table>
<tr>
<th width="33%">Node Guides</th>
<th width="33%">Technical Reference</th>
<th width="33%">Support</th>
</tr>
<tr>
<td valign="top">

- [Multi Scheduled LoRA Loader](./docs/MULTI_SCHEDULED_LORA_LOADER.md)
  - [Getting Started](./docs/MULTI_SCHEDULED_LORA_LOADER.md#getting-started)
  - [Curve Editor](./docs/MULTI_SCHEDULED_LORA_LOADER.md#curve-editor)
  - [Block Weights](./docs/MULTI_SCHEDULED_LORA_LOADER.md#block-weight-system)
  - [Profiles](./docs/MULTI_SCHEDULED_LORA_LOADER.md#profile-management)
  - [String Syntax](./docs/MULTI_SCHEDULED_LORA_LOADER.md#external-string-syntax)
  - [Outputs](./docs/MULTI_SCHEDULED_LORA_LOADER.md#outputs)
- [Visual Prompt Gallery](./docs/VISUAL_PROMPT_GALLERY.md)
  - [Getting Started](./docs/VISUAL_PROMPT_GALLERY.md#getting-started)
  - [Gallery Interface](./docs/VISUAL_PROMPT_GALLERY.md#gallery-interface)
  - [Metadata Formats](./docs/VISUAL_PROMPT_GALLERY.md#supported-metadata)
  - [Outputs](./docs/VISUAL_PROMPT_GALLERY.md#outputs)

</td>
<td valign="top">

- [Technical Reference](./docs/TECHNICAL.md)
  - [Node I/O](./docs/TECHNICAL.md#node-io)
  - [Operation Modes](./docs/TECHNICAL.md#operation-modes)
  - [External String Parsing](./docs/TECHNICAL.md#external-schedule-string-parsing)
  - [Block-weight vectors & presets](./docs/TECHNICAL.md#block-weight-vectors-and-presets)
  - [LoRA Manager (recommended)](./docs/TECHNICAL.md#recommended-dependency-lora-manager)
  - [Architecture Detection](./docs/TECHNICAL.md#architecture-detection)
  - [API Endpoints](./docs/TECHNICAL.md#api-endpoints)
  - [Block Mappings](./docs/TECHNICAL.md#block-mappings)
  - [Caching](./docs/TECHNICAL.md#caching)

</td>
<td valign="top">

- [Troubleshooting](./docs/TROUBLESHOOTING.md)
- [Changelog](./CHANGELOG.md)
- [License](./LICENSE)

</td>
</tr>
</table>

---

<div align="center">

**[Get Started with Multi Scheduled LoRA Loader](./docs/MULTI_SCHEDULED_LORA_LOADER.md)** | **[Get Started with Visual Prompt Gallery](./docs/VISUAL_PROMPT_GALLERY.md)**

---

<sub>PROJECT-MAD-NODES is released under the [MIT License](./LICENSE)</sub>

</div>
