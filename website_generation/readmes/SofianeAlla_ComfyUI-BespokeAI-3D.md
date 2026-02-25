<p align="center">
  <img src="assets/banner.png" alt="BespokeAI 3D Generation for ComfyUI" width="100%">
</p>

<h1 align="center">ComfyUI-BespokeAI-3D</h1>

<p align="center">
  <strong>Transform images into 3D models with AI-powered generation</strong>
</p>

<p align="center">
  <a href="https://github.com/SofianeAlla/ComfyUI-BespokeAI-3D/stargazers"><img src="https://img.shields.io/github/stars/SofianeAlla/ComfyUI-BespokeAI-3D?style=flat-square&color=yellow" alt="Stars"></a>
  <a href="https://github.com/SofianeAlla/ComfyUI-BespokeAI-3D/network/members"><img src="https://img.shields.io/github/forks/SofianeAlla/ComfyUI-BespokeAI-3D?style=flat-square" alt="Forks"></a>
  <a href="https://github.com/SofianeAlla/ComfyUI-BespokeAI-3D/issues"><img src="https://img.shields.io/github/issues/SofianeAlla/ComfyUI-BespokeAI-3D?style=flat-square" alt="Issues"></a>
  <a href="https://github.com/SofianeAlla/ComfyUI-BespokeAI-3D/blob/main/LICENSE"><img src="https://img.shields.io/github/license/SofianeAlla/ComfyUI-BespokeAI-3D?style=flat-square" alt="License"></a>
</p>

<p align="center">
  <a href="https://bespokeai.build"><img src="https://img.shields.io/badge/Powered%20by-BespokeAI-blue?style=flat-square" alt="BespokeAI"></a>
  <a href="https://github.com/comfyanonymous/ComfyUI"><img src="https://img.shields.io/badge/ComfyUI-Custom%20Node-green?style=flat-square" alt="ComfyUI"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python">
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-nodes">Nodes</a> •
  <a href="#-examples">Examples</a> •
  <a href="#-pricing">Pricing</a>
</p>

---

## 🎯 Overview

**ComfyUI-BespokeAI-3D** brings the power of [BespokeAI's](https://bespokeai.build) image-to-3D generation directly into your ComfyUI workflows. Generate high-quality 3D models (GLB/OBJ) from any image with AI enhancement, PBR textures, and automatic part segmentation.

<p align="center">
  <img src="assets/workflow-demo.gif" alt="Workflow Demo" width="80%">
</p>

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🖼️ **Image to 3D** | Convert any image into a detailed 3D model |
| 🎨 **AI Enhancement** | Automatic photorealistic enhancement of input images |
| 🌟 **PBR Textures** | Generate models with physically-based rendering textures |
| 📐 **Multiple Resolutions** | Choose from 500K, 1M, or 1.5M polygons |
| 🔷 **Low Poly Mode** | Create optimized game-ready models |
| 🧩 **Part Segmentation** | Automatic segmentation of 3D model components |
| ⚡ **Async Processing** | Non-blocking generation with progress tracking |

## 📦 Installation

### Prerequisites

1. **Download and install ComfyUI** from [comfy.org/download](https://www.comfy.org/download)
2. Launch ComfyUI at least once to initialize the directory structure

### Method 1: Git Clone

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/SofianeAlla/ComfyUI-BespokeAI-3D.git
cd ComfyUI-BespokeAI-3D
pip install -r requirements.txt
```

### Method 2: Download ZIP

1. Download the [latest release](https://github.com/SofianeAlla/ComfyUI-BespokeAI-3D/releases)
2. Extract to `ComfyUI/custom_nodes/`
3. Install dependencies: `pip install -r requirements.txt`
4. Restart ComfyUI

### Required Companion Nodes

This node works with the following built-in ComfyUI nodes:
- **Load Image** (`Charger Image`) - To provide image input to the 3D generation node
- **3D Preview** (`Aperçu 3D`) - To preview the generated 3D model directly in ComfyUI

## 🔑 Getting Your API Key

1. Visit [bespokeai.build](https://bespokeai.build)
2. Create an account or sign in
3. Navigate to **Settings → API**
4. Generate your API key (starts with `bspk_`)

> 💡 **Tip**: Keep your API key secure and never commit it to version control!

## 🚀 Quick Start

1. Add a **Load Image** node
2. Add **BespokeAI 3D Generation** node (found in `BespokeAI/3D`)
3. Connect the image output to the node
4. Enter your API key
5. Configure options and run!

<p align="center">
  <img src="assets/quickstart-workflow.png" alt="Quick Start Workflow" width="70%">
</p>

## 🧩 Nodes

### BespokeAI 3D Generation

The main node for converting ComfyUI images to 3D models.

<details>
<summary><strong>📥 Inputs</strong></summary>

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `image` | IMAGE | ✅ | ComfyUI image input |
| `api_key` | STRING | ✅ | Your BespokeAI API key |
| `resolution` | ENUM | ✅ | Polygon count: `500k`, `1m`, `1.5m` |
| `with_texture` | BOOLEAN | ✅ | Enable PBR textures |
| `ai_enhancement` | BOOLEAN | ✅ | AI photorealistic enhancement |
| `low_poly` | BOOLEAN | ❌ | Low poly optimization mode |
| `segmentation` | BOOLEAN | ❌ | Part segmentation (500k only) |
| `prompt` | STRING | ❌ | Custom prompt for AI enhancement |
| `poll_interval` | FLOAT | ❌ | Polling interval in seconds |
| `max_poll_attempts` | INT | ❌ | Maximum polling attempts |

</details>

<details>
<summary><strong>📤 Outputs</strong></summary>

| Output | Type | Description |
|--------|------|-------------|
| `glb_path` | STRING | Local path to downloaded GLB file |
| `obj_path` | STRING | Local path to downloaded OBJ file |
| `model_url` | STRING | Direct URL to 3D model |
| `enhanced_image_url` | STRING | URL of AI-enhanced input image |
| `credits_used` | INT | Credits consumed for this generation |

</details>

### BespokeAI 3D Generation (URL)

Alternative node that accepts an image URL directly.

<details>
<summary><strong>📥 Inputs</strong></summary>

Same as above, but replaces `image` with:

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `image_url` | STRING | ✅ | Direct URL to an image |

</details>

## 📸 Examples

### Basic Image to 3D

```
Load Image → BespokeAI 3D Generation → 3D Preview
```

<p align="center">
  <img src="assets/workflow-example.png" alt="Workflow Example" width="100%">
</p>

The screenshot above shows the correct node setup:
1. **Load Image** (Charger Image) - Load your source image
2. **BespokeAI 3D Generation** - Connect the image, enter your API key, and configure options
3. **3D Preview** (Aperçu 3D) - Connect the `mesh_path` output to preview the generated 3D model

<p align="center">
  <img src="assets/example-basic.png" alt="Basic Example" width="80%">
</p>

### With AI Enhancement + Segmentation

```
Load Image → BespokeAI 3D Generation → Save GLB
                    ↓
            Resolution: 500k
            AI Enhancement: ✓
            Segmentation: ✓
```

### Batch Processing Workflow

```
Load Image Batch → Loop → BespokeAI 3D Generation → Collect → Save All
```

## 💰 Pricing

| Feature | Credits |
|---------|:-------:|
| Base 3D Generation | 10 |
| AI Enhancement | +2 |
| Low Poly Mode | +5 |
| Part Segmentation | +6 |

**Total range: 12-23 credits per generation**

> Get credits at [bespokeai.build](https://bespokeai.build)

## 📁 Output Location

Generated 3D models are automatically saved to:

```
ComfyUI/
└── output/
    └── bespokeai_3d/
        ├── model_1699999999.glb
        └── model_1699999999.obj
```

## ⚠️ Troubleshooting

<details>
<summary><strong>❌ "Invalid API key" error</strong></summary>

- Verify your API key starts with `bspk_`
- Check that the key hasn't been revoked
- Ensure no extra spaces in the key field

</details>

<details>
<summary><strong>❌ "Insufficient credits" error</strong></summary>

- Add more credits at [bespokeai.build](https://bespokeai.build)
- Disable optional features to reduce credit usage
- Check your current balance in the dashboard

</details>

<details>
<summary><strong>❌ "Rate limit exceeded" error</strong></summary>

- Wait 1 minute before retrying
- Rate limit: 20 requests per minute
- Consider batching requests with delays

</details>

<details>
<summary><strong>❌ Segmentation not working</strong></summary>

- Segmentation **only works with 500k resolution**
- The node automatically switches to 500k when enabled
- Check console for warnings

</details>

<details>
<summary><strong>❌ Generation timeout</strong></summary>

- Increase `max_poll_attempts` (default: 120)
- Check your internet connection
- Complex images may take longer to process
- Try with a simpler/cleaner input image

</details>

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **BespokeAI Website**: [bespokeai.build](https://bespokeai.build)
- **ComfyUI**: [github.com/comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- **Issues & Support**: [GitHub Issues](https://github.com/SofianeAlla/ComfyUI-BespokeAI-3D/issues)

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/SofianeAlla">Sofiane</a> • <a href="https://bespokeai.build">BespokeAI</a>
</p>
