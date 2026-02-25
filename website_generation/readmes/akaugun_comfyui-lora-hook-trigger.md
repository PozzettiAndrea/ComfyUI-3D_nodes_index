# ComfyUI LoRA Hook + Trigger Text Node

A clean and minimal **ComfyUI custom node** that automatically links **LoRA hooks** with **LoRA-specific trigger text files**.

This node removes the need to manually manage trigger prompts for each LoRA by detecting and loading `.txt` files placed next to the LoRA model.

---

## ✨ Features

- Creates a **LoRA Hook Group** using `comfy_extras.nodes_hooks.CreateHookLora`
- Automatically detects trigger `.txt` files for each LoRA
- Provides a **dropdown selector (UI-only)** for trigger selection
- Outputs both the **LoRA hook group** and the **selected trigger text**
- Safe text loading with encoding fallback:
  - UTF-8
  - UTF-8-SIG
  - CP949
- No external dependencies
- Minimal, stable, and workflow-safe design

---

## 📁 Folder Structure

### Example (generic, not user data)

```text
models/
└── loras/
    ├── my_lora.safetensors
    └── my_lora/
        ├── trigger1.txt
        ├── style.txt
        └── preset_prompt.txt
```

### Rules

- The folder name **must match the LoRA filename without extension**
- Every `.txt` file inside that folder appears in the trigger selector
- If no `.txt` files are found, the trigger list defaults to `NONE`

---

## 📥 Installation

### 1) Install via ComfyUI Manager (Recommended)

1. Open **ComfyUI Manager**
2. Go to **Custom Nodes → Install via URL**
3. Paste:

```text
https://github.com/akaugun/comfyui-lora-hook-trigger
```

4. Click **Install**
5. Restart ComfyUI

Hard refresh if UI does not update:

- Windows / Linux: `Ctrl + F5`
- macOS: `Cmd + Shift + R`

---

### 2) Manual Installation

```text
ComfyUI/custom_nodes/comfyui-lora-hook-trigger
```

```text
comfyui-lora-hook-trigger/
├── __init__.py
└── js/
    └── lora_trigger_ui.js
```

Restart ComfyUI.

---

## 🧩 Node Overview

### Inputs

| Name | Type | Description |
|-----|-----|------------|
| lora_name | Combo | Select LoRA |
| trigger | String | Selected TXT name or `NONE` |
| strength_model | Float | LoRA model strength |
| strength_clip | Float | LoRA CLIP strength |
| prev_hooks | HOOKS (optional) | Previous hook group to append |

### Outputs

| Name | Type | Description |
|-----|-----|------------|
| hook | HOOKS | LoRA hook group |
| trigger_text | String | Contents of selected TXT |

---

## 🛠 How It Works

### Python (`__init__.py`)
- Defines the custom node
- Exposes `/lora_trigger_list` API
- Scans trigger TXT files next to LoRA models
- Builds and combines LoRA hooks safely

### JavaScript (`js/lora_trigger_ui.js`)
- Injects a UI-only trigger dropdown
- Keeps workflow serialization stable
- Syncs selected trigger with hidden value widget

---

## ⚙ Requirements

- ComfyUI (latest recommended)
- No external dependencies

---

## 📄 License

See `LICENSE`.
