# ComfyUi-DisplayAllSteps

## ✨ Use case

This custom node displays the intermediate images generated at each denoising step during sampling.

https://github.com/user-attachments/assets/91d3882a-7c6e-4ed0-afc1-fcad4ca401a1

## 📥 Installation

Navigate to the **ComfyUI/custom_nodes** folder, [open cmd](https://www.youtube.com/watch?v=bgSSJQolR0E&t=47s) and run:

```bash
git clone https://github.com/BigStationW/ComfyUi-DisplayAllSteps
```

Restart ComfyUI after installation.

## 🛠️ Usage

It uses 2 custom nodes:
- Sampler (Custom Advanced All Steps)
- VAE Decode All Steps

An example workflow (for Z-image turbo) can be found [here](https://github.com/BigStationW/ComfyUi-DisplayAllSteps/blob/main/workflow_Z-image_turbo.json)
