# Vantage-DreamOmni2 — Multimodal DreamOmni2 (Qwen2.5-VL) Node for ComfyUI

**Vantage-DreamOmni2** brings the advanced multimodal reasoning power of **DreamOmni2 (Qwen2.5-VL - NF4 quantized)** into **ComfyUI**, enabling unified text–image understanding for **instruction-based generation and editing**.  
This extension bridges the gap between creative AI and intelligent visual control, allowing you to generate or modify images with both textual and visual guidance.

---

## Features

### 1. DreamOmni2 Text Encoder
A unified **multimodal instruction node** that fuses **text prompts** and **reference images** into a context-aware enhanced prompt using the **DreamOmni2** model.

#### Modes:
- **`generate` → Multimodal Instruction-based Generation**  
  Designed for *conceptual or subject-driven generation*.  
  - Excels in retaining **identity and pose consistency**.  
  - Understands and applies **abstract attributes** such as *texture, makeup, hairstyle, posture, or artistic style*.  
  - Can regenerate full scenes while maintaining fidelity to **reference identity or concept**.  
  - Outperforms most open-source models in handling creative, style-driven instructions.

- **`edit` → Multimodal Instruction-based Editing**  
  Tailored for *localized or attribute-guided modifications*.  
  - Preserves **non-edited regions** with high consistency.  
  - Allows reference-based edits for features that are **hard to describe textually**.  
  - Supports concrete and abstract references — from specific objects to subtle visual attributes.  
  - Achieves **commercial-grade precision** in visual edit alignment.

✨ In short — **Generation** focuses on intelligent recreation under concept guidance, while **Editing** ensures precision-controlled transformation without breaking source integrity.

---

### 2. Adaptive Image Stitch (Vantage)
An intelligent image compositor for creating adaptive grids from multiple images — ideal for visual comparisons, prompt-response grids, and result layouts.

- Combines up to 4 images  
- Preserves aspect ratio or enforces uniform alignment  
- Adjustable spacing width and color  
- Works seamlessly with image batches and multi-output nodes  

---

## Installation

Clone or download this repository into your **ComfyUI custom_nodes** directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/<yourusername>/Vantage-DreamOmni2.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> 💡 The node automatically downloads **`vantagewithai/DreamOmni2-nf4`** from Hugging Face the first time you run it, storing it in:
> ```
> ComfyUI/models/dreamomni2
> ```

---

## How It Works

1. **Text + Image Inputs → DreamOmni2 Text Encoder**  
   The node processes text and visual references together through **Qwen2.5-VL**, generating a contextually enhanced multimodal prompt.

2. **Enhanced Prompt → Image Generation / Editing Nodes**  
   The enhanced prompt carries both textual intent and visual cues, guiding downstream samplers for realistic, identity-consistent, or style-driven results.

3. **Output Management → Adaptive Image Stitch (Vantage)**  
   Combine outputs or compare variants using adaptive image stitching for clean, consistent presentation and input for Flux Latent.

---

## 📦 Requirements

```
bitsandbytes
accelerate
sentencepiece
safetensors
einops
numpy
```

---

## 🧰 Node Overview

| Node Name | Display Name | Category | Function |
|------------|---------------|-----------|-----------|
| `TextEncodeDreamOmni2` | DreamOmni2 Text Encoder | DreamOmni2 | Multimodal prompt encoding for generation & editing |
| `VantageAdaptiveImageGrid` | Adaptive Image Stitch - Vantage | vantage/tools | Adaptive compositing of multiple images |

---

## ⚡ Technical Notes

- Uses **DreamOmni2 (Qwen2.5-VL) NF4 quantized** model for lower VRAM usage and faster performance.  
- Automatically caches the model locally.  
- Compatible with `torch.float16` precision and `device_map="auto"`.  
- Ideal for **multimodal diffusion**, **style transfer**, and **editing pipelines**.

---

## 🪄 Credits

- Developed by **[Vantage with AI](https://www.youtube.com/@vantagewithai)**
- Powered by **DreamOmni2** from [DreamOmni Team](https://pbihao.github.io/projects/DreamOmni2/index.html)
- Powered by **Qwen2.5-VL** from [Alibaba Cloud / Qwen Team](https://huggingface.co/Qwen)

---

## 🧷 License

Released under the **MIT License**.  
Use, modify, and integrate freely within your ComfyUI workflows.

---

### ⭐ If you find this useful, please star the repo and share your workflows!

