# ComfyUI-DeepseekOCR

[English](README.md) | [中文](README_CN.md)

A custom node that wraps **DeepSeek-OCR** as a ComfyUI plugin, providing powerful OCR recognition and document parsing capabilities.


**Install Dependencies**

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/Geo1230/ComfyUI-DeepseekOCR.git
```

Portable/venv:
Run
```bash
path/to/ComfUI/python_embeded/python.exe -s -m pip install -r requirements.txt
```
With system python
Run
```bash
pip install -r requirements.txt
```
Start ComfyUI

Recommended transformers 4.46.3
If you encounter compatibility issues with transformers 4.55+, downgrade:
```bash
pip install transformers==4.46.3 tokenizers==0.20.3
```

**Download Model**

Create directories and navigate:
```bash
# 1. Navigate to ComfyUI's models directory
cd ComfyUI\models

# 2. Create deepseek-ocr directory (if it doesn't exist)
mkdir deepseek-ocr
cd deepseek-ocr

# 3. Create model directory
mkdir deepseek-ai_DeepSeek-OCR
cd deepseek-ai_DeepSeek-OCR
```

Download model to current directory:
```bash
huggingface-cli download deepseek-ai/DeepSeek-OCR --local-dir . --repo-type model
```

**Note**: Model will be downloaded to `ComfyUI\models\deepseek-ocr\deepseek-ai_DeepSeek-OCR\` directory

**Or Use Automatic Download** (Not recommended, less stable):

Model will automatically download on first run of the Load node. Download progress is shown in the console.

To **disable** automatic download, set environment variable:
```bash
# Windows PowerShell
$env:DPSK_AUTODOWNLOAD = "0"
```


## Usage

### Node 1: DeepSeek OCR: Load Model

Loads and caches the model, outputs a model handle for use by the Run node.

**Parameters:**
- `dtype`: Data precision
  - `bf16` (Recommended, default) - Balance of precision and performance
  - `fp16` - Use when VRAM is insufficient
  - `fp32` - Best compatibility but high VRAM usage
- `device`: Runtime device (default: `cuda`)


### Node 2: DeepSeek OCR: Run

Performs OCR inference and outputs recognized text.

**Parameters:**
- `model`: Model handle (from Load node)
- `image`: Input image (ComfyUI IMAGE type)
- `task`: Task mode
  - `Free OCR`: General OCR recognition
  - `Convert to Markdown`: Document to Markdown conversion
  - `Parse Figure`: Parse charts and figures
  - `Locate by Reference`: Locate specified objects (requires `reference_text`)
- `resolution`: Resolution preset
  - `Gundam` (Recommended for long documents): 1024/640/crop/compress
  - `Tiny`: 512x512
  - `Small`: 640x640
  - `Base`: 1024x1024
  - `Large`: 1280x1280
- `output_type`: **Output type** (determines what is returned)
  - `all` (default): Output both text and visualization image
  - `text`: Text only, image output is original image
  - `image`: Visualization image only (suitable for Locate task)
- `reference_text`: (Optional) **Only when** task=`Locate by Reference`, description of object to locate
- `box_color`: (Optional) Detection box color, default `red`
  - Preset colors: `red`, `green`, `blue`, `yellow`, `cyan`, `magenta`, `white`, `black`
  - Custom RGB: e.g., `"255,0,0"` (red), `"0,255,0"` (green)
- `box_width`: (Optional) Detection box width, default `2` px, range 1-10

**Outputs:**
- `text`: Recognized text content (STRING)
  - Contains original markers (e.g., `<|ref|>...<|/ref|><|det|>[[coordinates]]<|/det|>`)
- `visualization`: Visualization image (IMAGE)
  - **Locate by Reference** task: Image with custom-styled bounding boxes
  - Other tasks: Returns original input image

## Screenshots


## Usage Guide

### 💡 Output Type Selection

- `all` (default): Output both text and visualization image
- `text`: Text only (OCR/Markdown conversion)
- `image`: Visualization image only (Locate task)

### 🎯 Locate by Reference Task

**Parameter Configuration:**
- `task`: Select `Locate by Reference`
- `reference_text`: Enter the object to locate
  - Chinese examples: `"价格"`, `"标题"`, `"二维码"`
  - English examples: `"the teacher"`, `"price"`, `"table"`, `"logo"`

### 🎨 Custom Bounding Box Style

**Supported Preset Colors (16 types):**

| Color Name | RGB | Preview | Color Name | RGB | Preview |
|------------|-----|---------|------------|-----|---------|
| `red` | 255,0,0 | 🔴 Red (default) | `orange` | 255,165,0 | 🟠 Orange |
| `green` | 0,255,0 | 🟢 Green | `purple` | 128,0,128 | 🟣 Purple |
| `blue` | 0,0,255 | 🔵 Blue | `pink` | 255,192,203 | 🩷 Pink |
| `yellow` | 255,255,0 | 🟡 Yellow | `lime` | 0,255,0 | 🟢 Lime |
| `cyan` | 0,255,255 | 🔵 Cyan | `navy` | 0,0,128 | 🔵 Navy |
| `magenta` | 255,0,255 | 🟣 Magenta | `teal` | 0,128,128 | 🔵 Teal |
| `white` | 255,255,255 | ⚪ White | `gold` | 255,215,0 | 🟡 Gold |
| `black` | 0,0,0 | ⚫ Black | `silver` | 192,192,192 | ⚪ Silver |

**Custom RGB Format:**
- Input format: `"R,G,B"` (e.g., `"255,128,0"` for dark orange)
- Range: 0-255

**Box Width:**
- `box_width`: 1-10 pixels (default 2px)

**Example Configuration:**
```
box_color = "red"          → Red 2px border (default)
box_color = "orange"       → Orange border
box_color = "255,105,180"  → Hot pink border
box_width = 5              → 5px thick border
```

### 📌 Basic Workflow

```
LoadImage
   ↓
DeepSeek OCR: Load Model  
   ↓
DeepSeek OCR: Run
   ├─→ text → Display Text / Save Text
   └─→ visualization → Preview Image / Save Image
```

### 📚 Typical Use Cases

**1. Document to Markdown**
```
task = "Convert to Markdown"
resolution = "Gundam"
→ Output formatted Markdown text
```

**2. Figure Parsing**
```
task = "Parse Figure"
resolution = "Base"
→ Extract structured data from tables and charts
```

**3. Object Localization**
```
task = "Locate by Reference"
reference_text = "哆啦A梦"
box_color = "red"
box_width = 2
→ Text contains coordinates, image shows red box annotations
```


```
ComfyUI/
├─ models/
│  └─ deepseek-ocr/                    # ← Fixed weights directory
│     ├─ deepseek-ai_DeepSeek-OCR/     # Model weights
│     └─ hf_cache/                     # HuggingFace cache
├─ output/
│  └─ DeepseekOCR/                     # Output directory (visualization results)
│     └─ 2025-11-05_20-31-00/          # Timestamp directory
├─ log/
│  └─ deepseek_ocr.log                 # Plugin logs
└─ custom_nodes/
   └─ ComfyUI-DeepseekOCR/
      ├─ __init__.py
      ├─ config.py
      ├─ model_manager.py
      ├─ nodes.py
      ├─ resolver.py
      ├─ io_utils.py
      ├─ tool/
      │  └─ download_weights.py
      ├─ requirements.txt
      └─ README.md
```

## Logging

Plugin logs are located at: `ComfyUI/log/deepseek_ocr.log`

Key log contents:
- Model weight download progress
- Model loading status (device/dtype/attn_impl)
- Cache hit information
- Fallback strategy trigger records
- Error details and suggestions


This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgments

- [DeepSeek AI](https://www.deepseek.com/) - For providing the powerful DeepSeek-OCR model
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Excellent node-based UI framework
- All contributors and users

