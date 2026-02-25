## Comfy MultiGPU Loader
A set of ComfyUI nodes that shard SD/SDXL/Flux-style checkpoints across multiple GPUs using custom forwards.

### Project status
Sunset / “as-is”. No active support or new features. Kept for reference; a future ComfyUI-inspired project will carry new work. Use at your own risk.

### Solidarity
We stand with Ukraine. #standwithukraine.

### Not GGUF/Quantization
This project focuses on sharding native safetensors checkpoints across multiple GPUs. It does not provide GGUF loaders, quantization, or VRAM-reduction tooling like ComfyUI-GGUF. The goal here is to combine multiple GPUs to run large models, not to compress models for single-GPU fits.

### License
Licensed under GPL-3.0 (see LICENSE). Ethical use is encouraged, but GPL terms apply for compatibility with ComfyUI.

### Attribution
Developed by Stefan with assistance from AI tools (Claude by Anthropic, GPT-5 by OpenAI, Gemini by Google).

### Installation
- Drop this repository into `ComfyUI/custom_nodes/Comfy-MultiGPU-Loader` (folder name can vary; ensure it contains this README and `nodes/`).
- Install requirements if needed: `pip install -r requirements.txt` (accelerate/torch are typically already present in ComfyUI environments).
- Restart ComfyUI. Nodes appear under `MultiGPU/Loaders`, `MultiGPU/Sampling`, `MultiGPU/VAE`, `MultiGPU/Diagnostics`, and `MultiGPU/Safety`.
For usage and debugging details, see `USER_GUIDE.md`.

### Safety rail
For heavy checkpoints (e.g., Flux Dev 2 FP32), run the `Hardware Validator (MultiGPU)` node before the loaders and feed its `gpu_ids`/`ok` outputs into the loader inputs. It will block or warn when GPU count/VRAM is below profile requirements.

### Known issues
- Logging/diagnostics can under-report activity on later runs; ongoing investigation.
- Early-stage code — other bugs may exist.

### Verified models
- Flux Dev Full Model fp32 (~22.17 GB) on multi-GPU.

### Needs Verifying models
- Flux Dev 2 (~60 GB) planned for validation when hardware/credits allow. 

### Project goals
- Stable multi-GPU sharding for SD/SDXL/Flux checkpoints.
- Broader node coverage (samplers/VAEs/utility).
- Future: video workflows and additional node support.

### Future updates
Roadmap is frozen while the project is sunset. See `CHANGELOG.md` for the last released updates; future work moves to the next ComfyUI-inspired project.

See `NODES.md` for the current node list.

See `TESTED.md` for hardware details 

### Key contributors
Humans: 
- Stefan (AngelCookies), code/research/testing  

AI: 
- Gemini (license help, research)
- GPT-5 / GPT-5-Codex-Max (license, code)
- Claude (original test nodes, research, fixes)

These are the primary contributors; all contributors (including AI tools and suggestion authors) are listed in `CONTRIBUTORS.md`. This project encourages AI coding tools with human oversight.

### Motivation and Why
High-end GPUs are expensive (e.g., RTX 5090 ~£2,500), and even large cards cap out on sequence length or render duration. Inspired by Ollama’s multi-GPU weight sharding, this project aims to combine multiple affordable GPUs to match or exceed a single large card without sacrificing quality. The first milestone is a stable workflow where all cards participate; next is broader node coverage so the setup is useful for real workloads, not just demos. Example goals: make 4×RTX 5060 8GB approximate a 5090 32GB, or 2×RTX 3090 24GB compete with a 6000 Ada 48GB.

Note on low-VRAM cards: the focus is 8, 12, 24 GB GPUs working together. While some of the techniques might help 4–6 GB cards, supporting very low-VRAM hardware for large models is not a target.

Note on interconnects: NVLink/SLI is not required; sharding runs over standard PCIe (e.g., tested on RTX 3070s without NVLink).
