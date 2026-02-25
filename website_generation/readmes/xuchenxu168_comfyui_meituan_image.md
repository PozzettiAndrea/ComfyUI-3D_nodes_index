<div align="center">

# 🐱 ComfyUI Meituan Image (LongCat)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Node-green.svg)](https://github.com/comfyanonymous/ComfyUI)
[![LongCat-Image](https://img.shields.io/badge/LongCat--Image-v1.0-orange.svg)](https://github.com/meituan-longcat/LongCat-Image)

**ComfyUI integration for Meituan's LongCat-Image model - High-quality bilingual text-to-image generation and image editing**

[English](#english) | [中文](#中文)

</div>

---

## English

### 📖 Overview

This ComfyUI custom node package provides seamless integration with [Meituan's LongCat-Image](https://github.com/meituan-longcat/LongCat-Image), a state-of-the-art open-source bilingual (Chinese-English) foundation model for image generation and editing.

### ✨ Features

| Feature | Description |
|---------|-------------|
| 🎨 **Text-to-Image** | Generate high-quality images from text prompts with excellent Chinese text rendering |
| ✏️ **Image Edit** | Edit images using natural language instructions |
| ⚡ **Performance Options** | CPU offload support and optional SageAttention acceleration |
| 🔧 **Auto Model Detection** | Automatically detects LongCat models in your models directory |
| 📥 **Auto Model Download** | Automatically downloads models from HuggingFace if not found locally |
| 🔄 **Auto Dependency Install** | Automatically installs longcat-image package if not present |

### 📦 Nodes Included

1. **LongCat Model Loader** - Load LongCat-Image, LongCat-Image-Dev, or LongCat-Image-Edit models
2. **LongCat Text to Image** - Generate images from text prompts
3. **LongCat Image Edit** - Single image editing with natural language

### 🚀 Installation

#### Prerequisites

- ComfyUI installed and working
- Python 3.10+
- CUDA-capable GPU with at least 17GB VRAM (with CPU offload) or 24GB+ (without)

#### Step 1: Clone the Repository

`bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-username/comfyui_meituan_image.git
`

#### Step 2: Install Dependencies

`bash
cd comfyui_meituan_image
pip install -r requirements.txt
`

Or install LongCat-Image directly:

`bash
pip install git+https://github.com/meituan-longcat/LongCat-Image.git@main
`

#### Step 3: Download Models (Optional - Auto Download Available)

> **💡 Note:** Starting from v1.1, models are **automatically downloaded** when you first use a node. You can skip this step if you prefer auto-download.

**Model Storage Location:**
```
ComfyUI/
└── models/
    └── diffusion_models/
        ├── LongCat-Image/          # Text-to-Image model
        ├── LongCat-Image-Dev/      # Dev model (faster)
        └── LongCat-Image-Edit/     # Image Editing model
```

**Available Models:**

| Model | HuggingFace Repo | Description |
|-------|------------------|-------------|
| LongCat-Image | [meituan/LongCat-Image](https://huggingface.co/meituan/LongCat-Image) | Full text-to-image model (50 steps) |
| LongCat-Image-Dev | [meituan/LongCat-Image-Dev](https://huggingface.co/meituan/LongCat-Image-Dev) | Faster model (28 steps) |
| LongCat-Image-Edit | [meituan/LongCat-Image-Edit](https://huggingface.co/meituan/LongCat-Image-Edit) | Image editing model |

**Manual Download (if needed):**

```bash
pip install "huggingface_hub[cli]"

# Text-to-Image model
huggingface-cli download meituan/LongCat-Image --local-dir ComfyUI/models/diffusion_models/LongCat-Image

# Dev model (faster, 28 steps)
huggingface-cli download meituan/LongCat-Image-Dev --local-dir ComfyUI/models/diffusion_models/LongCat-Image-Dev

# Image Editing model
huggingface-cli download meituan/LongCat-Image-Edit --local-dir ComfyUI/models/diffusion_models/LongCat-Image-Edit
```

### 📝 Usage

#### Text-to-Image Generation

1. Add **LongCat Model Loader** node and select `LongCat-Image` or `LongCat-Image-Dev`
2. Connect to **LongCat Text to Image** node
3. Enter your prompt (supports both Chinese and English)
4. For text rendering, enclose text in quotes: `"你好世界"`

#### Image Editing

1. Add **LongCat Model Loader** and select `LongCat-Image-Edit`
2. Connect to **LongCat Image Edit** node
3. Load your source image and enter editing instructions

### ⚙️ Node Parameters

#### LongCat Model Loader

| Parameter | Description | Default |
|-----------|-------------|---------|
| model_name | Select from detected models | Auto |
| custom_model_path | Manual path override | - |
| dtype | Precision: bfloat16/float16/float32 | bfloat16 |
| enable_cpu_offload | Enable to save VRAM (~17GB needed) | true |
| attention_backend | default or sage (requires sageattention) | default |

#### LongCat Text to Image

| Parameter | Description | Default |
|-----------|-------------|---------|
| prompt | Image description (Chinese/English) | - |
| negative_prompt | What to avoid | - |
| width/height | Output dimensions | 1344x768 |
| steps | Inference steps | 50 |
| guidance_scale | CFG scale | 4.5 |
| seed | Random seed | 43 |
| batch_size | Number of images | 1 |

#### LongCat Image Edit

| Parameter | Description | Default |
|-----------|-------------|---------|
| image | Source image | Required |
| prompt | Edit instructions | - |
| steps | Inference steps | 50 |
| guidance_scale | CFG scale | 4.5 |

### 📂 Example Workflows

Example workflows are available in the `example/` folder:

- `example_workflow_t2i.json` - Text-to-Image
- `example_workflow_edit.json` - Image Edit

### 🔗 Related Links

- [LongCat-Image GitHub](https://github.com/meituan-longcat/LongCat-Image)
- [LongCat-Image on Hugging Face](https://huggingface.co/meituan-longcat)
- [LongCat Official App](https://longcat.ai)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

---

## 中文

### 📖 概述

这是美团 [LongCat-Image 长猫图像模型](https://github.com/meituan-longcat/LongCat-Image) 的 ComfyUI 自定义节点包。LongCat-Image 是一个开源双语（中英文）图像生成与编辑基础模型。

### ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🎨 **文生图** | 从文本生成高质量图像，出色的中文渲染能力 |
| ✏️ **图像编辑** | 使用自然语言编辑图像 |
| ⚡ **性能优化** | 支持 CPU 卸载和 SageAttention 加速 |
| 🔧 **自动识别** | 自动检测模型目录中的 LongCat 模型 |
| 📥 **自动下载模型** | 如果本地没有模型，自动从 HuggingFace 下载 |
| 🔄 **自动安装依赖** | 如果没有安装 longcat-image 包，自动安装 |

### 📦 包含节点

1. **LongCat Model Loader** - 加载 LongCat 模型
2. **LongCat Text to Image** - 文生图节点
3. **LongCat Image Edit** - 图像编辑节点

### 🚀 安装方法

#### 环境要求

- 已安装 ComfyUI
- Python 3.10+
- CUDA 显卡，至少 17GB 显存（开启 CPU 卸载）或 24GB+（不卸载）

#### 第一步：克隆仓库

`bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-username/comfyui_meituan_image.git
`

#### 第二步：安装依赖

`bash
cd comfyui_meituan_image
pip install -r requirements.txt
`

#### 第三步：下载模型（可选 - 支持自动下载）

> **💡 提示：** 从 v1.1 版本开始，模型会在首次使用时**自动下载**。如果你希望自动下载，可以跳过这一步。

**模型存放位置：**
```
ComfyUI/
└── models/
    └── diffusion_models/
        ├── LongCat-Image/          # 文生图模型
        ├── LongCat-Image-Dev/      # 开发版模型（更快）
        └── LongCat-Image-Edit/     # 图像编辑模型
```

**可用模型：**

| 模型 | HuggingFace 仓库 | 说明 |
|------|------------------|------|
| LongCat-Image | [meituan/LongCat-Image](https://huggingface.co/meituan/LongCat-Image) | 完整文生图模型（50步） |
| LongCat-Image-Dev | [meituan/LongCat-Image-Dev](https://huggingface.co/meituan/LongCat-Image-Dev) | 快速版模型（28步） |
| LongCat-Image-Edit | [meituan/LongCat-Image-Edit](https://huggingface.co/meituan/LongCat-Image-Edit) | 图像编辑模型 |

**手动下载（可选）：**

```bash
pip install "huggingface_hub[cli]"

# 文生图模型
huggingface-cli download meituan/LongCat-Image --local-dir ComfyUI/models/diffusion_models/LongCat-Image

# 开发版模型（更快，28步）
huggingface-cli download meituan/LongCat-Image-Dev --local-dir ComfyUI/models/diffusion_models/LongCat-Image-Dev

# 图像编辑模型
huggingface-cli download meituan/LongCat-Image-Edit --local-dir ComfyUI/models/diffusion_models/LongCat-Image-Edit
```

#### 第四步：重启 ComfyUI

### 📝 使用方法

#### 文生图

1. 添加 **LongCat Model Loader** 节点，选择 `LongCat-Image`
2. 连接到 **LongCat Text to Image** 节点
3. 输入提示词（支持中英文）
4. 渲染文字时用引号包裹：`"你好世界"`

#### 图像编辑

1. 添加 **LongCat Model Loader**，选择 `LongCat-Image-Edit`
2. 连接到 **LongCat Image Edit** 节点
3. 加载源图像并输入编辑指令

### 📄 许可证

本项目基于 [Apache 2.0 许可证](LICENSE) 开源。

### 🙏 致谢

- [美团长猫团队](https://github.com/meituan-longcat) - LongCat-Image 模型
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 强大的图像生成工作流平台
