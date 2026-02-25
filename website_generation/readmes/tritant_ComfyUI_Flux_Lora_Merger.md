# Flux LoRA Merger — Custom Node for ComfyUI

A custom ComfyUI node to **merge up to 4 LoRA models into a Flux.1-Dev UNet**

⚠️ If you experience VRAM issues (OOM) when saving, try using the sequential strategy instead of additive or average. It avoids direct weight modifications and makes saving more memory-efficient.

---

## ✨ Features

- ✅ Merge up to **4 LoRA models**
- ✅ Compatible with UNet models in **FP8 / FP16 / FP32**
- ✅ Three fusion strategies:
  - `additive`: weighted sum of LoRA deltas
  - `average`: average of LoRA deltas
  - `sequential`: apply one after another
- ✅ Option to **save the final merged model** in `.safetensors`

---

## 📥 Inputs

| Parameter        | Type     | Description |
|------------------|----------|-------------|
| `unet_model`     | `MODEL`  | The base UNet model to apply LoRAs to |
| `merge_strategy` | `CHOICE` | `"additive"`, `"average"`, or `"sequential"` |
| `enable_loraX`   | `BOOLEAN`| Whether to enable the corresponding LoRA |
| `loraX`          | `STRING` | Filename of the LoRA (from your `loras/` folder) |
| `loraX_weight`   | `FLOAT`  | Weight multiplier for the LoRA |
| `save_model`     | `BOOLEAN`| Save the merged model to `output/` |
| `save_filename`  | `STRING` | Custom name for the saved `.safetensors` file |

---

## 📤 Outputs

| Output           | Type     | Description |
|------------------|----------|-------------|
| `model`          | `MODEL`  | The merged UNet model |

![Capture d'écran 2025-04-15 143351](https://github.com/user-attachments/assets/3aad6d4d-9701-440f-82b4-a33088b4aa5b)
