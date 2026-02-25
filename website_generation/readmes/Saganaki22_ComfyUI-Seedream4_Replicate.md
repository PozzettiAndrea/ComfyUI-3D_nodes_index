# ComfyUI Seedream 4 Replicate

[![Replicate](https://img.shields.io/badge/Replicate-API-blue?logo=replicate)](https://replicate.com/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Node-orange)](https://github.com/comfyanonymous/ComfyUI)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green?logo=python)](https://www.python.org/)

A ComfyUI custom node for ByteDance's Seedream 4 image generation model via the Replicate API. Generate high-quality images with advanced control over aspect ratios, multi-image generation, and seed management.

## Gallery

| | | |
|:---:|:---:|:---:|
| <img width="309" height="335" alt="Einstein Portrait" src="https://github.com/user-attachments/assets/731a09f6-b156-4905-84d8-efd94daec566" /> |<img width="309" height="335" alt="Node Interface" src="https://github.com/user-attachments/assets/ca695ba4-2555-47bf-86c9-366b297a8e1f" /> | <img width="231" height="308" alt="Portrait Example" src="https://github.com/user-attachments/assets/0f764a9d-6716-4228-b41f-7119f22e6ddc" /> |

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
git clone https://github.com/Saganaki22/ComfyUI-Seedream4_Replicate.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Get your Replicate API token from [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)

4. Restart ComfyUI

## Node Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| **API Key** | String | Your Replicate API token (starts with r8_) |
| **Prompt** | String | Text description of what you want to generate |
| **Size Preset** | Dropdown | Common aspect ratios (1:1, 4:3, 16:9, etc.) or Custom |
| **Width** | Integer | Custom width in pixels (1024-4096, used with Custom preset) |
| **Height** | Integer | Custom height in pixels (1024-4096, used with Custom preset) |
| **Max Images** | Integer | Maximum images to generate (1-15, only with Sequential mode) |
| **Sequential Generation** | Dropdown | `disabled` (single image) or `auto` (let AI decide multiple) |
| **Seed** | Integer | Random seed for reproducible results (-1 for random) |
| **Control After Generate** | Dropdown | Seed behavior after generation (fixed/increment/decrement/randomize) |
| **Image Input** | Image | Optional reference image for image-to-image generation |

## Features

- **Multiple aspect ratios** with preset sizes
- **Sequential image generation** for related image sets
- **Image-to-image support** with reference images
- **Seed control** for reproducible results
- **Real-time progress tracking** with 4-stage progress updates
- **Automatic cancellation** support with ComfyUI's cancel button
- **Error handling** with content policy detection

## Usage Tips

- Use **Sequential mode** with prompts like "story sequence" or "character variations" for multiple related images
- **Custom dimensions** work best for specific use cases outside standard ratios
- **Seed control** lets you iterate on prompts while maintaining composition
- Large input images may exceed data URL limits (shows warning)

## License

MIT License - see LICENSE file for details

---

<p align="center">
<a href="https://replicate.com/" target="_blank">
<img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/ef0e9c4c-5174-41f4-a956-0d2460a34820" />
</a>
</p>
