# Eigen AI FLUX API Plugin for ComfyUI

A **ComfyUI plugin** that integrates with the **Eigen AI FLUX API**, providing high-quality image generation with **LoRA** support.

---

## 🚀 Quick Installation

### 1. Install ComfyUI

If you haven’t installed **ComfyUI** yet:

```bash
# Clone ComfyUI
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# Install dependencies
pip install -r requirements.txt

# (Optional) Start ComfyUI
python main.py
```

---

### 2. Install the Plugin

#### Method A: Install via ComfyUI-Manager (Recommended)

1. Install **ComfyUI-Manager** if not already installed:

   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/ltdrdata/ComfyUI-Manager.git
   ```

   > Restart ComfyUI after installation.

2. Install this plugin via Manager:

   1. Start ComfyUI:

      ```bash
      python main.py
      ```
   2. Open **ComfyUI-Manager**
   3. Search for **“Eigen AI FLUX API”** or **“flux api”**
   4. Click **Install** and wait until it finishes
   5. Restart ComfyUI
   6. Verify nodes appear in the left panel by searching **“Eigen AI FLUX API”**

---

#### Method B: Manual Install

If you prefer manual installation:

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/jialuw0830/flux_api_comfyui_plugin.git

# (Optional) Start ComfyUI
cd ComfyUI
python main.py
```

---

### 3. Post-Installation Steps

1. Restart **ComfyUI**
2. Search for **“Eigen AI FLUX API”** in the node browser
3. Generated images will be saved in:

   ```
   ComfyUI/output
   ```

---

## 🎨 Key Features

* **High-Quality Generation** — Uses **FLUX.1-schnell** model
* **Multi-LoRA Support** — Up to **3 LoRAs simultaneously**
* **Upscaling** — Supports **2×** and **4×** upscaling
* **Fast Performance** — Uses **quantized models** for quick generation

---

## 🔧 Node Descriptions


### 1. **Text Node** (`EigenAITextNode`)
**Purpose**: Text prompt processing and formatting
**Input**: Text prompt
**Output**: Processed prompt (PROMPT type)
**Usage**: 
- Add text prompt in the textarea
- Connect output to any generator node
- Supports multiline text up to 2000 characters

### 2. **LoRA Node** (`EigenAILoraNode`)
**Purpose**: LoRA model configuration and management
**Input**: LoRA file paths and weights
**Output**: LoRA configuration (LORA_CONFIG type)
**Usage**:
- Set up to 3 LoRA models simultaneously
- Configure LoRA weights (0.0 to 2.0)
- Connect to generator nodes for LoRA-enhanced generation

### 3. **Qwen Generator** (`EigenAIQwenGeneratorNode`)
**Purpose**: Image generation using Qwen-compatible model
**Input**: Prompt + LoRA config + generation parameters
**Output**: Generated image
**Usage**:
- Connect prompt from Text Node
- Connect LoRA config from LoRA Node
- Adjust width, height, guidance scale, and seed
- Default API: http://74.81.65.108:8010

### 4. **Schnell Generator** (`EigenAISchnellGeneratorNode`)
**Purpose**: Fast image generation using Schnell model
**Input**: Prompt + LoRA config + generation parameters
**Output**: Generated image
**Usage**:
- Similar to Qwen Generator but optimized for speed
- Ideal for batch processing
- Same parameter controls as Qwen Generator

### 5. **Kontext Generator** (`EigenAIKontextGeneratorNode`)
**Purpose**: Image-to-image generation using Kontext model
**Input**: Input image + Prompt + LoRA config + parameters
**Output**: Generated image
**Usage**:
- Upload or connect an input image
- Add text prompt for guidance
- Connect LoRA config for style enhancement
- Adjust generation parameters as needed

### 6. **Upscaler** (`EigenAIUpscalerNode`)
**Purpose**: Image upscaling and enhancement
**Input**: Image + upscaling parameters
**Output**: Upscaled image
**Usage**:
- Connect input image from generator nodes
- Choose upscaling factor (2x or 4x)
- Apply ESRGAN upscaling for better quality

---

## 🔄 Basic Workflows

### Standard Workflow
```
Text Node → LoRA Node → Generator Node → Upscaler → Output
```

### Quick Workflow (Built-in LoRA)
```
Text Node → Generator Node → Output
```

### Image-to-Image Workflow
```
Input Image → Kontext Generator → Upscaler → Output
```

---


---

## 🆘 Troubleshooting

* **Error: "This action is not allowed with this security level configuration."**
  Solution:
  Edit:

  ```
  ComfyUI/user/default/ComfyUI-Manager/config.ini
  ```

  Change:

  ```
  security_level = normal
  ```

  to:

  ```
  security_level = weak
  ```

  Then restart **ComfyUI**.

---

## 📄 License

**MIT License**

---

✨ Enjoy using the **Eigen AI FLUX API Plugin**! 🎨

---

