# ComfyUI-Lumina-DiMOO

A set of **ComfyUI custom nodes** that wrap the official **[Alpha-VLLM/Lumina-DiMOO](https://github.com/Alpha-VLLM/Lumina-DiMOO)** project into an easy-to-use, node-based workflow.

## Installation

### A) Install via ComfyUI-Manager

1. Open ComfyUI → **Manager**.
2. In **Custom Nodes Manager**, search for **ComfyUI-Lumina-DiMOO**.
3. Click **Install**, then **Restart** ComfyUI.

### B) Manual install

```bash
# Replace /path/to/ComfyUI with your real path
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/L-Hugh/ComfyUI-Lumina-DiMOO.git
cd ComfyUI-Lumina-DiMOO

# Install Python deps (install the right PyTorch first!)
pip install -r requirements.txt
```

> After installation, **restart ComfyUI**.


## Download model weights (Hugging Face Hub CLI — `hf`)

Download the full Lumina-DiMOO snapshot (including the `vqvae/` subfolder) to your **ComfyUI/models** directory:

```bash
# Replace /path/to/ComfyUI with your real path
hf download Alpha-VLLM/Lumina-DiMOO --local-dir "/path/to/ComfyUI/models/lumina_dimoo"
```


## Example workflows

This repo ships example workflows under:

```
custom_nodes/ComfyUI-Lumina-DiMOO/example_workflows/
```

Open ComfyUI → Templates. In the left sidebar, under EXTENSIONS, select ComfyUI-Lumina-DiMOO to view the templates (restart ComfyUI after installing).
