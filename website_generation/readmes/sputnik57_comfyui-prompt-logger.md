# comfyui-prompt-logger
This custom node saves metadata when I explore images. It creates a sidecare json file beside the image file.
🧠 A modular ComfyUI node for logging prompt metadata, sampler settings, and image outputs into a unified `.json` sidecar file. Built for reproducibility, brand integrity, and traceable creative workflows.

---

## 🔧 Features

- Logs prompt text, model name, sampler, seed, and other metadata
- Outputs a `.json` file alongside each generated image
- Designed for clean integration with `KSampler` and custom workflows
- Timestamped entries for easy sorting and versioning
- Compatible with ComfyUI Manager structure

---

## 📦 Installation

Clone or symlink into your ComfyUI `custom_nodes/` directory:

```bash
git clone https://github.com/sputnik57/comfyui-prompt-logger.git
