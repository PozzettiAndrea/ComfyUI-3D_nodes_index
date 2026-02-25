# ComfyUI RH QwenImage I2L (Image-to-LoRA)

A ComfyUI custom node that generates an **Image-to-LoRA (I2L)** LoRA from one or more training images using **DiffSynth-Studio Qwen-Image i2L** pipelines.

- **Nodes**
  - `RunningHub_ImageQwenI2L_Loader(Style)`
  - `RunningHub_ImageQwenI2L_Loader(CFB)`
  - `RunningHub_ImageQwenI2L_LoraGenerator` (outputs a `.safetensors` LoRA into `ComfyUI/models/loras/`)

Original model page: [`DiffSynth-Studio/Qwen-Image-i2L` on ModelScope](https://modelscope.cn/models/DiffSynth-Studio/Qwen-Image-i2L/summary)

---

## Installation

### 1) Install this ComfyUI node

Clone into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/HM-RunningHub/ComfyUI_RH_QwenImageI2L.git
```

Install Python dependencies:

```bash
cd ComfyUI/custom_nodes/ComfyUI_RH_QwenImageI2L
pip install -r requirements.txt
```

> Note: `sync.sh` is intentionally ignored and should not be committed.

### 2) Install DiffSynth-Studio (required)

This project uses `diffsynth` from DiffSynth-Studio. Install the latest version:

```bash
git clone https://github.com/modelscope/DiffSynth-Studio.git
cd DiffSynth-Studio
pip install -e .
```

### 3) (Recommended) Install git-lfs

Some model repositories require Git LFS:

```bash
git lfs install
```

### 4) Restart ComfyUI

After installation, restart ComfyUI to load the new nodes.

---

## Models (Required)

This node loads models via `DiffSynth-Studio` model configs. On **first run**, models may be **auto-downloaded** (requires network access to the model host used by DiffSynth/ModelScope/HF).

If you prefer **offline / deterministic setup**, place models under your ComfyUI models directory.

### Recommended offline layout

Put the following under `ComfyUI/models/`:

```
ComfyUI/models/
├─ DiffSynth-Studio/
│  ├─ General-Image-Encoders/
│  │  ├─ SigLIP2-G384/model.safetensors
│  │  └─ DINOv3-7B/model.safetensors
│  └─ Qwen-Image-i2L/
│     ├─ Qwen-Image-i2L-Style.safetensors
│     ├─ Qwen-Image-i2L-Coarse.safetensors
│     ├─ Qwen-Image-i2L-Fine.safetensors
│     └─ Qwen-Image-i2L-Bias.safetensors
└─ Qwen/
   ├─ Qwen-Image/
   │  └─ text_encoder/model*.safetensors
   └─ Qwen-Image-Edit/
      └─ processor/
```

### What each Loader needs

- **`Loader(Style)`** loads:
  - `DiffSynth-Studio/General-Image-Encoders`
    - `SigLIP2-G384/model.safetensors`
    - `DINOv3-7B/model.safetensors`
  - `DiffSynth-Studio/Qwen-Image-i2L`
    - `Qwen-Image-i2L-Style.safetensors`
  - Processor:
    - `Qwen/Qwen-Image-Edit` → `processor/`

- **`Loader(CFB)`** loads:
  - `Qwen/Qwen-Image`
    - `text_encoder/model*.safetensors`
  - `DiffSynth-Studio/General-Image-Encoders`
    - `SigLIP2-G384/model.safetensors`
    - `DINOv3-7B/model.safetensors`
  - `DiffSynth-Studio/Qwen-Image-i2L`
    - `Qwen-Image-i2L-Coarse.safetensors`
    - `Qwen-Image-i2L-Fine.safetensors`
    - (optional at generation time) `Qwen-Image-i2L-Bias.safetensors`
  - Processor:
    - `Qwen/Qwen-Image-Edit` → `processor/`

---

## Usage (ComfyUI)

### Basic workflow (Style)

```
[Load Image(s)] → [RunningHub_ImageQwenI2L_Loader(Style)] → [RunningHub_ImageQwenI2L_LoraGenerator] → (LoRA saved to models/loras)
```

### Output

`RunningHub_ImageQwenI2L_LoraGenerator` writes a LoRA file:

- Path: `ComfyUI/models/loras/i2l_style_lora_<uuid>.safetensors`
- Returns:
  - `lora_name` (for ComfyUI LoRA dropdown)
  - `lora_path` (full path)

---

## Notes

- **GPU**: the pipeline uses `cuda` and `bfloat16`. Make sure your GPU/driver supports BF16.
- **Disk offload**: the loader uses disk offload to reduce VRAM usage; ensure you have enough free disk space.

---

## License

Open-source. If you redistribute, please comply with the licenses of upstream projects and model providers.


