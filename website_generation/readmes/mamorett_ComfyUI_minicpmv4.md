# MiniCPM‑V‑4 (GGUF) for ComfyUI

Modular ComfyUI nodes to run the vision-language model MiniCPM‑V‑4 in GGUF format, powered by llama‑cpp‑python.

- Loader: choose a quant, auto-download from Hugging Face, and load with GPU acceleration.
- Prompt Builder: compose prompts with optional chat tags and automatic `<image>` token.
- Vision Inference: send one or more images + prompt, with streaming token output.

Repo of models:
- https://huggingface.co/openbmb/MiniCPM-V-4-gguf

## Features

- Dropdown of official GGUF quantizations
- Auto-download (with resume) to `ComfyUI/models/llama`
- Optional checksum verification (fill in KNOWN_SHA256)
- Multi-image input (image batch) — passed as `images=[PIL...]`
- Token streaming to the ComfyUI console
- Configurable context length, GPU layers, threads, sampler params, stop sequences

## Installation

1) Place this folder in: ComfyUI/custom_nodes/minicpmv4_llamacpp/

Files:
- `loader.py`
- `prompt_utils.py`
- `vision_infer.py`
- `__init__.py`
- `README.md`

2) Install llama‑cpp‑python (0.2.90+ recommended):
- CPU only:
  ```
  pip install "llama-cpp-python>=0.2.90"
  ```
- NVIDIA CUDA (Windows/Linux):
  ```
  pip install --upgrade --force-reinstall --no-binary :all: llama-cpp-python
  ```
  Make sure CUDA toolchain is available for wheel build, or use prebuilt CUDA wheels if available for your platform.
- macOS (Apple Silicon): Metal is used automatically by default wheels.

3) Restart ComfyUI.

## Usage

- Add nodes to your workflow:

1. MiniCPM‑V‑4 (GGUF) Loader
  - Pick a quant (e.g., “Q4_K_M (2.19 GB) [balanced]”).
  - On first run, the file is downloaded to `ComfyUI/models/llama`.
  - Adjust:
    - `n_ctx` (context length), `n_gpu_layers` (0 = CPU), `threads`, `seed`.
  - Outputs:
    - LLAMA handle, a boolean suggesting `<image>` prepend default, and the model path string.

2. Vision Prompt Builder (optional)
  - Compose your prompt (system/user).
  - Enable “prepend_image_token” if image is ignored.
  - “chat_style” wraps prompts with `<|im_start|>` tags (add stop at `"<|im_end|>"` in Infer if you want).

3. MiniCPM‑V‑4 (GGUF) Vision Infer
  - Connect the LLAMA handle, the image (or image batch), and the built prompt.
  - Options:
    - `max_tokens`, `temperature`, `top_p`, `top_k`, `repeat_penalty`
    - `stop_1`, `stop_2`
    - `force_prepend_image_token` (safety net)
    - `stream_tokens` (prints tokens as they arrive)

- Multi-image:
- Provide an IMAGE batch (B x H x W x C). All images in the batch are passed in order.
- Reference them in the prompt if needed (e.g., “Consider all images; describe differences.”).

## Tips

- If the image seems to have no effect:
- Ensure `<image>` appears before the prompt (use Prompt Builder or force toggle in Infer).
- Update llama‑cpp‑python to the latest version.
- Some models expect chat formatting plus the image token.

- Performance
- `n_gpu_layers`: more layers on GPU = higher speed, requires VRAM.
 - 8–12 GB VRAM: try 35–60 for MiniCPM‑V‑4 class.
- Quant:
 - Q4_K_M is a great speed/quality balance.
 - Q5_K_M for better quality if VRAM allows.
- `n_ctx`: 4096 is safe for single-turn; increase for longer interactions (more RAM/VRAM).

- CPU tuning
- Set `threads` > 0 to control llama.cpp threading on CPU.

## Checksums and Integrity

- The loader supports optional SHA‑256 verification. Fill `KNOWN_SHA256` in `loader.py` with the hash for the file(s) you want to enforce.
- Even without hashes, downloads use Hugging Face resumable transfers.

## Troubleshooting

- “Invalid model handle”:
- Ensure you connected the Loader to Infer.
- CUDA not used / slow:
- Your wheel may be CPU-only. Reinstall with CUDA (see install section).
- Reduce `n_gpu_layers` or quant level if you OOM.
- API mismatch errors:
- We support both `llama(prompt=...)` and `llama.create_completion(...)` signatures.
- For streaming, we use `create_completion(..., stream=True)` which is broadly compatible.

## Roadmap

- Optional remote inference node (HTTP) for people who can’t modify the ComfyUI env.
- Add more stop sequences and presets for popular chat formats.
- Progress callback during HF download (when huggingface_hub exposes hooks).

## Credits

- Model: openbmb/MiniCPM‑V‑4‑gguf
- Runtime: llama.cpp (via llama‑cpp‑python)
- ComfyUI community for modular node patterns

Enjoy! PRs/ideas welcome.

