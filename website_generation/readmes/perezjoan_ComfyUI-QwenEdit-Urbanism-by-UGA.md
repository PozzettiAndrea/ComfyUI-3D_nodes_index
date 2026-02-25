# 🏙️ ComfyUI-QwenEdit-Urbanism-by-UGA
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ComfyUI](https://img.shields.io/badge/Compatible%20with-ComfyUI-blue)](https://github.com/comfyanonymous/ComfyUI)
[![Urban Geo Analytics](https://img.shields.io/badge/By-Urban%20Geo%20Analytics-orange)](https://urbangeoanalytics.com)

**Qwen Image Edit for Urbanism** brings localized, text-driven image editing to urban and architectural workflows using the open-source **Qwen-Image-Edit** model in **GGUF format**. All processing runs fully offline — no API, no cloud — making it ideal for architects, planners, and researchers who need privacy, reproducibility, and full visual control.

---

## 🧠 1. Qwen Image Edit for Urbanism : Comfy Pipelines  

| Version | Description | Tutorial |
|----------|--------------|-----------|
| **v1.0** | Basic Qwen Image Edit workflow for single-image editing. Adapts automatically to input ratio and size. | [v1.0 Tutorial →](https://urbangeoanalytics.com/local-ai-image-editing-urbanism-comfyui-qwen-gguf/) |
| **v1.1** | Adds image editing from a reference image and advanced sampling capabilities for complex scenes. | [v1.1 Tutorial →](https://urbangeoanalytics.com/local-ai-image-editing-for-urbanism-v1-1/) |
| **v1.2** | Add sequential & Batch Edits | [v1.2 Tutorial →](https://urbangeoanalytics.com/qwen-image-edit-for-urbanism-v1-2-custom-nodes-sequential-processing/) |
| **v1.3** | Add editing with a Mask and a reference image and/or prompt | [v1.3 Tutorial →](https://urbangeoanalytics.com/qwen-image-edit-for-urbanism-v1-3-editing-with-a-mask) |

### Download the Workflows
Right-click any link above and choose **“Save link as…”** to download the workflow file. Then, open **ComfyUI → File → Load → Workflow**, and select the downloaded `.json` file to load it into your workspace.
| Version | Workflow File |
|---|---|
| v1.0 | [Download Qwen-Edit-UGA-v1.0.json](https://github.com/perezjoan/ComfyUI-QwenEdit-Urbanism-by-UGA/blob/main/Qwen-Edit-UGA-v1.0.json) |
| v1.1 | [Download Gwen-Edit-UGA-v1.1.json](https://github.com/perezjoan/ComfyUI-QwenEdit-Urbanism-by-UGA/blob/main/Qwen-Edit-UGA-v1.1.json) |
| v1.2 | [Download Gwen-Edit-UGA-v1.2.json](https://github.com/perezjoan/ComfyUI-QwenEdit-Urbanism-by-UGA/blob/main/Qwen-Edit-UGA-v1.2.json) |
| v1.3 | [Download Gwen-Edit-UGA-v1.3.json](https://github.com/perezjoan/ComfyUI-QwenEdit-Urbanism-by-UGA/blob/main/Qwen-Edit-UGA-v1.3.json) |

---

## ⚙️ 2. Custom Nodes 

Custom nodes developed for urban image processing and automation within ComfyUI.

| Node Name | Function | Description |
|------------|-----------|--------------|
| 🎲 **Random Image Selector** | Randomly selects one image among several inputs each run. | For stochastic rendering. |
| 🔁 **Sequential Image Loader** | Loads each connected image in order across executions. | For batch processing. |
| 🖼️ **Stateful Image Collector** | Stores and display the processed outputs from each run into six persistent slots. | For preview. |

## 🧩 Installation

1. Download and install ComfyUI
2. Open the desired workflow and install the required models.
  Follow the Qwen-Edit-UGA tutorials to download and place the necessary checkpoints, VAE, CLIP, and other model files inside your ComfyUI/models directory.
3. Add custom nodes (required from v1.2).
   Navigate to your ComfyUI directory:
ComfyUI/custom_nodes/
5. Clone or download our repository and put the QwenUrbanismNodes folder in your custom_nodes directory
https://github.com/perezjoan/ComfyUI-QwenEdit-Urbanism-by-UGA.git
6. Restart **ComfyUI.**

The nodes will appear under **image/sequence** and **image/random** categories.

---

## 🧩 Credits
Developed by **Urban Geo Analytics (UGA)**  
Based on open-source work by **QuantStack**, **ComfyUI**, and **Qwen Image Edit** contributors.

---

## 🪪 License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

