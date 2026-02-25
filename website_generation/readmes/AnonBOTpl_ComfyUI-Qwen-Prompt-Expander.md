# 🔐 ComfyUI Qwen Prompt Expander

A privacy-focused, local AI prompt generator for ComfyUI.  
Turn short concepts (e.g., "woman in red dress") into professional, detailed Stable Diffusion prompts using advanced local LLMs like **Qwen 2.5** or **SmolLM2**.

**100% Offline. Zero API keys. Maximum Privacy.**

<img width="1812" height="890" alt="image" src="https://github.com/user-attachments/assets/d5bdef9a-4586-400b-bd3e-0c6c98184f28" />
<img width="1504" height="618" alt="{847B7FEB-0CEB-4AA6-82FA-2503F6F8BB3A}" src="https://github.com/user-attachments/assets/410aa8e4-2c9a-40f5-9be7-5a2cf7d7f139" />



![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)
![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)
![GPU: 6GB+](https://img.shields.io/badge/GPU-6GB%2B-orange.svg)

---

## ✨ Key Features

- **🧠 Local LLM Power:** Uses powerful models (Qwen, SmolLM2, Dolphin, Phi-3) running locally on your machine
- **🛡️ 100% Private:** No data leaves your computer. Works without internet (after initial model download)
- **📉 VRAM Friendly:** Supports **4-bit and 8-bit quantization**. Runs perfectly on **6GB VRAM cards** alongside SD 1.5!
- **🌍 Auto-Translation:** Built-in **Polish-to-English** translator (offline MarianMT) with GPU/CPU support
- **🧩 Embeddings Support:** Automatically detects and inserts embeddings from your ComfyUI models folder
- **🧹 Smart Memory Management:** Intelligent caching and configurable model unloading to prevent Out-Of-Memory (OOM) errors
- **✂️ Intelligent Token Management:** Automatic prompt trimming that preserves your subject and important details
- **♻️ Translation Cache:** Avoids re-translating the same text multiple times for faster workflows
- **🎨 Custom Model Support:** Use any HuggingFace model or local models
- **🔍 Built-in Diagnostics:** Test your setup before using the main node

---

## 🚀 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for **"Qwen Prompt Expander"**
3. Click **Install**
4. Restart ComfyUI

### Method 2: Manual Installation
1. Navigate to your ComfyUI `custom_nodes` directory
2. Clone this repository:
   ```bash
   git clone https://github.com/AnonBOTpl/ComfyUI-Qwen-Prompt-Expander.git
   ```
3. Install dependencies:

   **Portable Version (Windows):**
   ```cmd
   .\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-Qwen-Prompt-Expander\requirements.txt
   ```

   **Standard Version (Linux/Mac/Windows):**
   ```bash
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

---

## 🔍 First Time Setup - Run Diagnostics!

**Before using the main node, test your setup:**

1. Add Node: **🔍 Qwen Diagnostics**
2. Choose test model: `Qwen-0.5B (Smallest - ~1GB)` 
3. Set **Run Test** to `True`
4. Queue prompt and wait 2-5 minutes
5. Check the output report

**The diagnostic will:**
- ✅ Test internet connection
- ✅ Test HuggingFace Hub access
- ✅ Verify folder permissions
- ✅ Check disk space
- ✅ Download and test a small model
- ✅ Confirm your system is ready

**Expected output:** `🎉 ALL TESTS PASSED!`

If tests fail, the report will tell you exactly what to fix!

---

## 📥 Model Downloads

### Automatic Download (Default)
Models download automatically on first use. This requires:
- **Internet connection** (one-time, ~5-10 minutes)
- **10GB free disk space** (for all models)
- **Patience** ☕

**What happens:**
1. **First run:** Downloads model (~5-10 minutes)
2. **Future runs:** Loads from cache (~5 seconds)
3. **Offline use:** Works without internet after download!

**Where models are stored:**  
`ComfyUI/models/LLM/`

You can delete models to free space - they'll re-download if needed.

---

## 🎛️ Node Parameters Guide

### 1. Model Selection

**Model Source:** Choose how you want to select a model
- **Preset Models:** Tested and optimized models with size info
- **Custom HuggingFace ID:** Use any model from HuggingFace
- **Local Path:** Use models you've downloaded manually

**Preset Models Available:**
- `SmolLM2-1.7B` (~1.7B) - **Recommended** - Best balance of speed and quality
- `Qwen-0.5B` (~0.5B) - **Ultra Light** - Fastest, great for low-end GPUs
- `Qwen-1.5B` (~1.5B) - **Balanced** - High quality, moderate speed
- `Dolphin-2.9.4-Qwen` (~1.5B) - **Uncensored** - Creative, less restricted
- `TinyLlama-1.1B` (~1.1B) - **Fast** - Lightweight alternative
- `Phi-3-mini` (~3.8B) - **Quality** - Best quality, **needs 12GB VRAM!**
- `Llama-3.2-1B` (~1B) - **Meta** - Meta's latest small model

**Precision:** Controls model size in VRAM
- **4-bit (Ultra Light)**: ~1.2GB VRAM. Minimal quality loss. Best for 6GB GPUs
- **8-bit (Fast)**: ~1.8GB VRAM. Good balance of speed and quality
- **fp16 (Standard)**: ~3.5GB VRAM. Full precision, best quality

### 2. Prompting

- **subject**: Your main idea (e.g., "knight eating pizza"). Can be in Polish if translation is enabled
- **use_translator_PL_EN**: Translates input from Polish to English using offline CPU/GPU model
- **translator_device**: Choose CPU (stable, zero VRAM) or GPU (faster) for translation
- **max_tokens**: Limits prompt length. Lower (60-80) for SD 1.5, higher (100-150) for SDXL/Flux

### 3. Style & Quality

- **style / lighting / quality**: Presets to guide the AI. Set to "Disabled" for full LLM creativity
- Combinations create unique atmospheres (e.g., "Cyberpunk + Neon Lights + 8k Masterpiece")

### 4. Embeddings & Negative

- **emb_positive / emb_negative**: Select embeddings from `ComfyUI/models/embeddings`. Auto-added to prompt
- **add_negative**: Enable to output negative prompt
- **negative_prompt_text**: Edit your negative prompt defaults

### 5. System Settings

**device_mode:**
- **GPU (Fast)**: Uses graphics card. Fast generation (2-5 seconds)
- **CPU (Safe Mode)**: Runs on RAM/CPU. Slower (10-30s), uses **0 VRAM**

**unload_model:** CRITICAL VRAM SETTING
- **True (Save VRAM)**: Loads LLM → Generates → Deletes from VRAM. Essential for low VRAM
- **False (Cache - Fast)**: Keeps LLM in VRAM. **Instant subsequent generations!** (~0.5s)

**seed:** Set to 0 for random, or specific number for reproducible prompts

---

## 🔋 VRAM Optimization Guide

Choose settings based on your GPU memory:

### 🟢 Low VRAM (4GB - 6GB)
**Goal:** Run alongside SD 1.5 without crashing

- **Model:** SmolLM2-1.7B or Qwen-0.5B
- **Precision:** 4-bit (Ultra Light)
- **Unload Model:** True *(Must unload to make room for SD)*
- **Device:** GPU
- **Expected:** 2-4s per prompt, stable workflow

### 🟡 Medium VRAM (8GB - 12GB)
**Goal:** Speed and quality balance

- **Model:** SmolLM2-1.7B or Qwen-1.5B
- **Precision:** 8-bit or 4-bit
- **Unload Model:** False *(Cache for instant prompts!)*
- **Device:** GPU
- **Expected:** First: 3s, Rest: 0.5s per prompt

### 🔴 High VRAM (16GB - 24GB)
**Goal:** Maximum quality

- **Model:** Qwen-1.5B or Phi-3-mini
- **Precision:** fp16 (Standard)
- **Unload Model:** False
- **Device:** GPU
- **Expected:** <1s per prompt, best quality

### 🥔 Integrated Graphics / Very Old GPU
**Goal:** Just make it work

- **Device Mode:** CPU (Safe Mode)
- **Model:** Qwen-0.5B
- **Unload Model:** True
- **Expected:** 15-30s per prompt, but stable

---

## 🎭 Prompt Philosophy

This node generates **conceptual prompts** rather than **literal descriptions**, giving Stable Diffusion creative freedom while maintaining your intended direction.

### Example Generation:

**Input:** `"cyberpunk girl"`  
**Settings:** SmolLM2-1.7B, 8-bit, 80 tokens, Cyberpunk + Dark & Moody

**Generated Output:**
```
cyberpunk girl in high-tech environment with sleek lines, sharp angles, 
digital textures, deep shadows, cinematic lighting effects, ultra-detailed 
facial features, masterful composition, 8k resolution
```

**Tokens Used:** 35/80 ✅

### Why Conceptual Prompts Work Better:

| Traditional (Literal) | Our Approach (Conceptual) |
|----------------------|---------------------------|
| "girl with black leather jacket, purple hair, neon city background, standing pose..." | "cyberpunk girl in high-tech environment with sleek lines, sharp angles, digital textures..." |
| ❌ Too rigid, limits SD creativity | ✅ Focuses on mood and atmosphere |
| ❌ Often 100+ tokens | ✅ Concise 30-50 tokens |
| ❌ Same output every time | ✅ Natural variation between generations |

---

## 🎨 Using Custom Models (v1.1+)

### Three Ways to Use Models:

**1. Preset Models (Default)**
- Select from dropdown of tested models
- See model size and VRAM requirements
- Best for beginners

**2. Custom HuggingFace ID**
- Use ANY instruction-tuned model from HuggingFace
- Examples: 
  - `mistralai/Mistral-7B-Instruct-v0.2`
  - `google/gemma-2b-it`
  - `stabilityai/stablelm-2-1_6b`
- Model downloads automatically on first use

**3. Local Path**
- Use models you've downloaded manually
- Example: `/home/user/models/my-custom-llm`
- Fastest loading (no download)

### How to Use Custom Models:

1. Set **Model Source** to your preferred method
2. If using Custom/Local, fill **Custom Model ID** field
3. Choose **Precision** based on your VRAM
4. Generate!

### Recommended Custom Models:

**Lightweight (6GB VRAM):**
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0` - Ultra fast
- `stabilityai/stablelm-2-1_6b` - Stable, reliable

**Balanced (12GB VRAM):**
- `microsoft/Phi-3-mini-4k-instruct` - Excellent quality
- `google/gemma-2b-it` - Google's model

**High Quality (24GB VRAM):**
- `mistralai/Mistral-7B-Instruct-v0.2` - Industry standard
- `meta-llama/Llama-3.2-3B-Instruct` - Meta's latest

---

## 🛠️ Troubleshooting

### Diagnostic Node Shows Failures

**Run the diagnostic node first!** It will tell you exactly what's wrong:

- **Internet FAILED** → Check your connection or try VPN
- **Permission FAILED** → Run ComfyUI with appropriate permissions
- **Disk space warning** → Free up at least 10GB
- **Download FAILED** → Check error message for specific issue

### Error: `ModuleNotFoundError: No module named 'bitsandbytes'`

Windows users often face this. **Solution:**

1. Go to `ComfyUI_windows_portable` folder
2. Open CMD/Terminal there
3. Run:
   ```cmd
   .\python_embeded\python.exe -m pip install https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.41.1-py3-none-win_amd64.whl
   ```

**Note:** Without bitsandbytes, the node automatically falls back to fp16 precision.

### Error: OOM (Out of Memory)

If you see "CUDA out of memory" or GPU driver crashes:

1. **Set `precision` to 4-bit (Ultra Light)**
2. **Set `unload_model` to True**
3. **Lower `max_tokens` to 60**
4. If still crashing: **Switch to CPU mode**

The node includes intelligent OOM protection with fallback prompts.

### Slow Generation Times

**On GPU:**
- First generation: 2-5s (model loading)
- Subsequent: <1s (if `unload_model` is False)
- Always slow? → Check console, model may be reloading each time

**On CPU:**
- Expected: 10-30s per generation
- This is normal for CPU inference
- Use Qwen-0.5B for faster CPU generation

### Models Don't Download

**Symptoms:** Node hangs, no progress, timeout errors

**Solutions:**
1. **Run Diagnostic Node** - it will test and show exact error
2. **Check internet** - Try opening https://huggingface.co
3. **Check firewall** - Temporarily disable antivirus/firewall
4. **Try VPN** - HuggingFace may be blocked in your region
5. **Manual download:**
   - Visit: `https://huggingface.co/[model-id]/tree/main`
   - Download all files to `ComfyUI/models/LLM/manual-[model-name]/`
   - Use "Local Path" mode in node

### Translation Issues

**Polish text not translating:**
1. Verify `use_translator_PL_EN` is enabled
2. First use downloads translator model (~300MB)
3. Check console for translation errors

**Translation cache:** The node remembers up to 100 translations automatically.

---

## 🧪 Advanced Tips

### Performance Optimization

**Cache Strategy:**
- Set `unload_model = False` for **10x faster** subsequent generations
- Model stays in VRAM between prompts
- Perfect for batch workflows

**VRAM Management:**
- Node clears VRAM only when switching models (not every generation)
- Smart cleanup prevents interference with SD models
- Console shows `⚡ Using cached model` when cache is working

### Token Management

The node intelligently trims long outputs:
- Generates 20% more than requested
- Prioritizes tags containing your subject keywords
- Removes duplicates automatically

**Console example:**
```
✂️ [LLM] Response too long (95 tokens), trimming to 80...
📊 Kept 15/22 tags (78 tokens)
```

### Seed Behavior

Seeds provide *approximate* reproducibility:
- Same seed + same input ≈ similar output
- Temperature (0.8) introduces natural variation
- Useful for iterating on a concept while keeping style

---

## ❓ FAQ

### Q: Do I need to download models manually?
**A:** No! Models download automatically. Run the **Diagnostic Node** first to test your setup.

### Q: Where are models stored?
**A:** In `ComfyUI/models/LLM/`. You can delete them to free space - they'll re-download if needed.

### Q: Can I use this offline?
**A:** Yes! After the first download, everything works offline. No API keys, no internet needed.

### Q: How much disk space do I need?
**A:** ~10GB for all preset models. Each model is 1-3.5GB (Phi-3 is larger at ~7.6GB in fp16).

### Q: Why is my first generation slow?
**A:** Model is loading into VRAM (2-5s). Set `unload_model=False` for instant subsequent generations.

### Q: Can I use models from HuggingFace?
**A:** Yes! Set Model Source to "Custom HuggingFace ID" and enter any instruction-tuned model ID.

### Q: What's the difference between the models?
- **SmolLM2-1.7B**: Best all-around, recommended default
- **Qwen-0.5B**: Fastest, good for low-end hardware
- **Dolphin**: More creative, less restricted outputs
- **Phi-3**: Highest quality, needs more VRAM

---

## 📊 Changelog

### [1.1.0] - 2026-02-23

#### Added
- **Custom Model Support**: Use any HuggingFace model or local models
- **Diagnostic Node**: Test your setup before using main node
- **Model Size Information**: See parameter count and VRAM requirements in dropdown
- **VRAM Estimation**: Console shows estimated VRAM usage after loading
- **Better Error Messages**: Detailed diagnostics with troubleshooting tips
- **Extended Model List**: Added Phi-3, Llama-3.2, TinyLlama presets

#### Fixed
- **CRITICAL**: Fixed VRAM cache not working - 10x faster subsequent generations
- **Performance**: Model no longer reloads unnecessarily when `unload_model=False`
- **Permissions**: Better handling of folder creation and write permissions
- **Downloads**: Improved error messages for failed downloads

#### Improved
- **Console Logs**: Added cache status indicator `⚡ Using cached model`
- **Translator Device Tracking**: Prevents unnecessary model moves between CPU/GPU

### [1.0.0] - 2026-02-16
- Initial release
- Core prompt expansion functionality
- Polish-English translation
- 4-bit/8-bit quantization support
- Smart token management

---

## ❤️ Credits

- **Qwen Models**: [Qwen Team at Alibaba Cloud](https://github.com/QwenLM/Qwen)
- **SmolLM2**: [HuggingFaceTB](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct)
- **Phi-3**: [Microsoft](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
- **Llama**: [Meta AI](https://huggingface.co/meta-llama)
- **MarianMT Translation**: [Helsinki-NLP](https://huggingface.co/Helsinki-NLP)
- **Dolphin Uncensored Models**: [Cognitive Computations](https://huggingface.co/cognitivecomputations)
- **ComfyUI**: [comfyanonymous](https://github.com/comfyanonymous/ComfyUI)
- **Transformers & BitsAndBytes**: [HuggingFace](https://huggingface.co/)

---

## 📄 License

MIT License - Feel free to use and modify!

See [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
git clone https://github.com/AnonBOTpl/ComfyUI-Qwen-Prompt-Expander.git
cd ComfyUI-Qwen-Prompt-Expander
pip install -r requirements.txt
```

### Areas for Contribution
- 🌍 Additional language support (Spanish, German, French, etc.)
- 🎨 New style presets
- 🔧 Performance optimizations
- 📝 Documentation improvements
- 🐛 Bug reports and fixes

---

## 🌟 Star History

If this project helped you, please consider giving it a star! It helps others discover the project.

---

## 💬 Support

- **Issues:** [GitHub Issues](https://github.com/AnonBOTpl/ComfyUI-Qwen-Prompt-Expander/issues)
- **Discussions:** [GitHub Discussions](https://github.com/AnonBOTpl/ComfyUI-Qwen-Prompt-Expander/discussions)

---

**Made with ❤️ for the ComfyUI community**
