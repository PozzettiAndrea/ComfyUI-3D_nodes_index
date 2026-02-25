comfyui-orpheus-loader

Custom node for ComfyUI
 to load the Orpheus TTS base model and prepare it for LoRA injection + speech generation.

📦 Installation
Node Manager (Recommended)

Open ComfyUI on your GPU server.

Go to Node Manager → Install from URL.

Paste this repository URL:

https://github.com/<your-username>/comfyui-orpheus-loader.git


Restart ComfyUI.

Search for “Orpheus-TTS Base Loader” in the node list.

📂 Repository Structure
comfyui-orpheus-loader/
 ├─ custom_nodes/
 │   └─ orpheus_loader/
 │       └─ __init__.py   # node implementation
 ├─ requirements.txt      # dependencies
 └─ README.md             # this file

🖥 Usage

Drag the Orpheus-TTS Base Loader node into your workflow.

Set base_model_id (default: unsloth/orpheus-3b-tts)

If testing locally without GPU, set dry_run=True (no heavy model load, just placeholder).

On GPU server, set dry_run=False to load the real model.

This node will output an internal handle (ORPHEUS_MODEL) that can be connected to:

LoRA Applier Node (for injecting LoRA adapters)

TTS Generator Node (for generating WAV audio from text)

⚙️ Requirements

Dependencies are listed in requirements.txt:

torch
transformers
peft
soundfile


Install manually if needed:

pip install -r requirements.txt

📝 Notes

This loader does not perform generation itself, only prepares the base model.

Combine with future nodes (LoRA Applier, TTS Generator) for a complete pipeline.

If GPU memory is limited, prefer float16 or bfloat16 when loading.

If running locally without GPU, always use dry_run=True.
