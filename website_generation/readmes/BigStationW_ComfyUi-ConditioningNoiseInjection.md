# ComfyUi-ConditioningNoiseInjection

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that injects controlled noise into conditioning embeddings (like prompts) for a portion of the diffusion process.

## ✨ Use case

- Some models such as **Z-Image Turbo** exhibit low seed variance, meaning they generate very similar images even when the seed changes.

- This node **adds noise directly to the conditioning embeddings at the start of denoising**, then restores the clean conditioning once the specified **threshold** is reached.

- By perturbing the conditioning instead of the latent, you can:
  - Increase compositional diversity  
  - Better preserve prompt adherence

<img src="https://github.com/user-attachments/assets/98baeead-5ca5-4bdb-97bb-dfdbd1174aae" width="700" />

## 📥 Installation

Navigate to the **ComfyUI/custom_nodes** folder, [open cmd](https://www.youtube.com/watch?v=bgSSJQolR0E&t=47s) and run:

```bash
git clone https://github.com/BigStationW/ComfyUi-ConditioningNoiseInjection
```

Restart ComfyUI after installation.

## 🛠️ Usage

<img src="https://github.com/user-attachments/assets/0bd62054-c061-4b87-8bea-bbebafe91bf1" width="700" />

An example workflow (for Z-image turbo) can be found [here](https://github.com/BigStationW/ComfyUi-ConditioningNoiseInjection/blob/main/workflow_Z-image_turbo.json).
