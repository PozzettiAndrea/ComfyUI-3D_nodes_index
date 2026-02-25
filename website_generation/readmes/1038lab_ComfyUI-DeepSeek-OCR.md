# ComfyUI-DeepSeek-OCR

A powerful OCR node for ComfyUI that integrates the DeepSeek-OCR model from Hugging Face.

## Current Status

> [!NOTE]  
> ComfyUI-DeepSeek-OCR is currently in V0.0.1 beta status. Please stay tuned for future releases as we continue to refine and expand the functionality of this node.

## Features

- ✅ Models stored directly in `ComfyUI/models/LLM/DeepSeek-OCR/` (no nested folders)
- ✅ Uses `hf_hub_download` for clean, direct file downloads
- ✅ Compatible with transformers 4.46+ (with optional patching for 4.50+)
- ✅ Multiple OCR task types (Free OCR, Markdown, Figure parsing)
- ✅ Multiple resolution presets for speed/quality tradeoff
- ✅ Optional detection box visualization

## Installation

### 1. Clone into ComfyUI custom_nodes folder

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/1038lab/ComfyUI-DeepSeek-OCR.git
cd deepseek_ocr
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install flash-attn (Optional but Recommended)

```bash
pip install flash-attn --no-build-isolation
```

If flash-attn fails, the node will work with eager attention (slower but functional).

### 4. Fix compatibility (for transformers 4.50+)

If you have transformers 4.50 or newer (like 4.57):

```bash
python patch_model_code.py
```

This patches the model's Python code to work with newer transformers versions.

### 5. Restart ComfyUI

## Model Download

On first use, the node will automatically download model files (~6.6GB) to:

```
ComfyUI/models/LLM/DeepSeek-OCR/
├── config.json
├── tokenizer.json
├── model-00001-of-00012.safetensors
... (12 safetensors files total)
```

**No nested folders!** All files go directly into `DeepSeek-OCR/`.

## Usage

### Inputs

- **image** (IMAGE): Input image for OCR
- **task_type** (COMBO): OCR task to perform
  - **Free OCR** - Simple text extraction (default)
  - **Convert to Markdown** - Convert document to markdown format
  - **Parse Figure** - Extract text from charts/figures
- **resolution_preset** (COMBO): Quality/speed tradeoff
  - Tiny (512x512) - Fastest
  - Small (640x640) - Fast
  - Base (1024x1024) - Balanced (default)
  - Large (1280x1280) - High quality
  - Gundam (1024x640) - Optimized for documents
- **draw_boxes** (COMBO): Visualization
  - disable - No boxes (default)
  - enable - Draw detection boxes
- **eval_mode** (COMBO): Performance mode
  - disable - Full output (default)
  - enable - Faster, text-only

### Outputs

- **text** (STRING): Recognized text or markdown
- **image_output** (IMAGE): Original or annotated image

## Task Types Explained

### Free OCR
Basic text extraction. Best for:
- Simple documents
- Receipts
- Forms
- Signs

### Convert to Markdown
Converts structured documents to markdown. Preserves:
- Headings
- Tables  
- Lists
- Text formatting

Best for: academic papers, reports, structured documents.

### Parse Figure
Specialized for extracting text from:
- Charts and graphs
- Diagrams
- Scientific figures
- Data visualizations

## Resolution Presets Guide

| Preset | Size | Speed | Accuracy | Best For |
|--------|------|-------|----------|----------|
| Tiny | 512 | ⚡⚡⚡ | ⭐⭐ | Quick tests |
| Small | 640 | ⚡⚡ | ⭐⭐⭐ | Simple docs |
| Base | 1024 | ⚡ | ⭐⭐⭐⭐ | Most cases |
| Large | 1280 | 🐢 | ⭐⭐⭐⭐⭐ | Complex docs |
| Gundam | 1024+crop | ⚡⚡ | ⭐⭐⭐⭐ | Documents |

## Troubleshooting

### ImportError: cannot import name 'LlamaFlashAttention2'

This happens with transformers 4.50+.

**Solution:**
```bash
cd ComfyUI/custom_nodes/deepseek_ocr
python patch_model_code.py
# Restart ComfyUI
```

The patch makes the model code compatible with any transformers version.

### "No model code found" when running patch

1. Try to use the node in ComfyUI once (it will fail but download the code)
2. Run `python patch_model_code.py` again
3. Restart ComfyUI

### Model files location

All model files are stored directly in:
```
ComfyUI/models/LLM/DeepSeek-OCR/
```

No nested `snapshots/` or `models--deepseek-ai--DeepSeek-OCR/` folders!

The node uses `hf_hub_download` with `local_dir` and `local_dir_use_symlinks=False` for clean, direct downloads.

### Download failed or incomplete

If download is interrupted:
1. Delete the `ComfyUI/models/LLM/DeepSeek-OCR/` folder
2. Restart ComfyUI
3. The node will re-download all files

### CUDA out of memory

Use smaller presets: Tiny or Small.

### Slow performance

- Enable eval_mode for faster processing
- Use GPU if available
- Use smaller resolution presets
- Install flash-attn

### No boxes drawn

Detection boxes only appear when:
- Model generates `<|det|>` tags in output
- Task supports grounding (Markdown conversion)

## Why This Approach?

This node follows the same download pattern as ComfyUI-RMBG:
- Uses `hf_hub_download` for individual file downloads
- Stores files directly in model folder (no nested structure)
- Uses `local_dir` parameter for clean organization
- Uses `local_files_only=True` after download

This makes the model folder clean and easy to manage.

## Requirements

- Python 3.10+
- CUDA 11.8+ (for GPU)
- torch >= 2.0.0
- transformers >= 4.46.0
- huggingface_hub
- flash-attn (optional, for speed)

## Links

- Model: https://huggingface.co/deepseek-ai/DeepSeek-OCR
- GitHub: https://github.com/deepseek-ai/DeepSeek-OCR
- This Node: https://github.com/1038lab/ComfyUI-DeepSeek-OCR

## License


MIT License - follows DeepSeek-OCR model license.
