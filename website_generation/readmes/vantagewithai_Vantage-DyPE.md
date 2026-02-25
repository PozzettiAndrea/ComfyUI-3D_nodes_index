
#  Vantage DyPE Node for ComfyUI  
### Dynamic Position Extrapolation for Ultra-High-Resolution Flux Models

---

## 🧠 Overview  

**Vantage DyPE** brings **DyPE (Dynamic Position Extrapolation)** directly into **ComfyUI**, allowing Flux-based diffusion transformer models to generate *native ultra-high-resolution images* — up to **8K** — without retraining or using any external upscalers.  

DyPE dynamically modulates the model’s **positional embeddings** during denoising, preserving geometry, proportion, and texture fidelity even when rendering far beyond the model’s original training resolution.

> ⚡ *Generate true 4K+ images natively in ComfyUI using your existing Flux models — fully training-free, stable, and VRAM-optimized.*

---

## ✨ Features  

- 🧩 Seamless **Flux Model Patching** (Krea, Kontext, Dev, etc.)  
- ⚙️ Native **High-Resolution Sampling** — supports 2K, 4K, 8K outputs  
- 🌀 Integrated **DyPE Positional Modulation** (Yarn / NTK / Base)  
- 🧮 Smart **Sigma (σ) Remapping** for large token grids  
- 🧠 **Adaptive Precision** switching (`fp16` / `bf16`)  
- 💾 **GGUF / Quantized Model Support** for low-VRAM setups  
- ⚡ **Performance Mode** — optimized memory & compute speed  
- 🔲 **Empty Latent Generator** — create quick zero-latent tensors for testing  

---

## 🧰Installation  

### 1️⃣ Locate Your Custom Nodes Folder  
Navigate to your ComfyUI installation directory and open:
```bash
ComfyUI/custom_nodes/
```

### 2️⃣ Clone or Copy the Node  
Clone this repo directly inside `custom_nodes`:
```bash
git clone https://github.com/vantagewithai/Vantage-DyPE.git
```

Or manually copy the `Vantage-DyPE` folder into:
```bash
ComfyUI/custom_nodes/Vantage-DyPE/
```

### 3️⃣ Restart ComfyUI  
After installation, restart ComfyUI.  
The node will appear under **Vantage → Model → / Patches**.

---

## ⚙️ Usage Guide  

1. **Load a Flux-based model** (Flux Krea, Flux Kontext, Flux Dev, etc.) using a:
   - **Diffusion Model Loader** *(for safetensors)*
   - **UNet Loader** *(for GGUF)*

2. **Model Format Support:**  
   - ✅ `.safetensors` (BF16 or FP8 scaled)  
   - ✅ `.gguf` (quantized)  

3. **If Using GGUF Models:**  
   - Enable the **UNet Loader Node**.  
   - Connect UNet Loader → LoRA Loader → Sampler.  
   - Disable the Diffusion Loader Node.

4. **Load Additional Models:**  
   - 🔥 **Flux Turbo Alpha LoRA** — enables 8-step fast sampling.  
   - 🎨 **VAE Model:** `sd-vae-ft-mse` (recommended).  
   - 🧠 **Encoders:** CLIP-L and T5-XXL (text conditioning).  

5. **Connect Model Output → Vantage DyPE Node.**  
   Configure:
   - `method`: Extrapolation method (`yarn` recommended)  
   - `enable_dype`: Enable/disable DyPE  
   - `dype_exponent`: Modulation strength (`2.0` default)  
   - `base_shift` / `max_shift`: Sigma remapping curve  
   - `adaptive_precision` / `performance_mode`: Precision & VRAM options  

6. **Connect DyPE Output → KSampler → VAE Decode.**  

> 💡 **Tip:** Keep both width and height divisible by **64** for stable geometry and best Flux attention alignment.

---

## 📏 Recommended Resolutions  

| Type | Resolution | Notes |
|------|-------------|-------|
| Square | 1024×1024 → 4096×4096 | Best structural accuracy |
| Landscape | 1920×1080 / 3840×2160 | Cinematic / 4K UHD |
| Portrait | 2160×3840 | Stable up to 3K vertical |
| Ultra | 4096×4096+ | Requires ≥24GB VRAM |

---

## ⚙️ Recommended Settings  

| Parameter | Recommended | Description |
|------------|-------------|-------------|
| **method** | `yarn` | Stable & accurate extrapolation |
| **dype_exponent** | `2.0` | Balanced between sharpness & stability |
| **base_shift** | `0.5` | Smooth low-resolution adaptation |
| **max_shift** | `1.15` | Ideal for 4K generation |
| **performance_mode** | `off` | Keep off for GGUF or quantized models |
| **adaptive_precision** | `on` | Enables dynamic fp16/bf16 switching |

---

## 🧩 Example Workflow  

1. Load model (Flux Krea / Kontext / Dev).  
2. Add **Flux Turbo Alpha LoRA** for fast 8-step sampling.  
3. Insert **Vantage DyPE Node** between model loader and sampler.  
4. Configure resolution and settings.  
5. Connect to sampler and VAE decode node.  
6. Run generation and enjoy native 4K output — *no upscaler needed!*  

---

## 📦 Recommended Dependencies  

- **ComfyUI (latest build)**  
- **PyTorch ≥ 2.2.0** with CUDA support  
- **Flux model (Krea / Kontext / Dev)**  
- **Flux Turbo Alpha LoRA (optional)**  
- **VAE:** `sd-vae-ft-mse`  
- **Encoders:** CLIP-L + T5-XXL  

---

## 🔗 Attribution & Credits  

### 📚 Research & Core Algorithm  
**DyPE: Dynamic Position Extrapolation for Ultra High Resolution Diffusion**  
By Hebrew University of Jerusalem  
👉 [Official DyPE GitHub Repository](https://github.com/guyyariv/DyPE)

### 🧩 Code Reference  
Some parts of this node’s implementation and integration logic are adapted from:  
👉 [ComfyUI-DyPE by wildminder](https://github.com/wildminder/ComfyUI-DyPE)

### 🎨 Flux Models  
By *Black Forest Labs*:  
- [Flux Krea](https://huggingface.co/black-forest-labs/FLUX-Krea)  
- [Flux Kontext](https://huggingface.co/black-forest-labs/FLUX-Kontext)

---

## 🧾 License  

This project is released under the **MIT License**.  
Attribution to the original DyPE research authors and ComfyUI-DyPE contributors is required in any forks, distributions, or derivative works.

---

## 📸 Example Results  

| Resolution | Model | Steps | Description |
|-------------|--------|--------|-------------|
| 3072×3072 | Flux Krea + DyPE + Turbo LoRA | 8 | Realistic portrait with perfect tone balance |
| 3840×2160 | Flux Krea + DyPE | 8 | Native UHD fidelity without upscaling |
| 4096×4096 | Flux Kontext + DyPE | 12 | Stable ultra-detailed render |

---

## 🧩 Troubleshooting  

| Issue | Possible Cause | Fix |
|--------|----------------|-----|
| Elongated / squashed images | Non-multiple of 64 resolution | Use width & height divisible by 64 |
| GPU memory overflow | Too high resolution or FP32 mode | Enable performance mode or lower res |
| Weak detail at edges | Low `dype_exponent` | Increase to 2.0–2.5 |
| Over-sharpening | High `dype_exponent` or aggressive sigma shift | Reduce to 1.5–2.0 |
| No output with GGUF | Incorrect loader wiring | Use UNet Loader → LoRA Loader path |

---

## 💬 Author  

Created by **Vantage with AI**  
🎥 [YouTube Channel](https://www.youtube.com/@VantageWithAI) — tutorials, model guides, and diffusion workflows.

> “Bringing true native 4K+ generation to ComfyUI.”  
> — *Vantage DyPE Node, 2025*

