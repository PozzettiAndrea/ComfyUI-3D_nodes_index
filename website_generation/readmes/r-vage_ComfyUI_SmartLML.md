# ComfyUI_SmartLML

Smart Language Model Loader for ComfyUI — unified vision-language AI with QwenVL, Mistral, Florence-2 via Transformers, Docker (vLLM/SGLang/Ollama/llama.cpp), and GGUF backends.

## Features

- **Multi-backend support:** Transformers, vLLM (Docker & Native), SGLang, Ollama, llama.cpp, GGUF, WD14 Tagger
- **Vision-language models:** QwenVL (Qwen2.5-VL, Qwen3-VL), Mistral, Florence-2
- **WD14 Tagger:** ONNX-based image tagging with booru-style tag output (SmilingWolf models)
- **Template system:** Save, load, and delete model configurations — full user control over template lifecycle
- **Docker integration:** Automatic container lifecycle management with cross-platform Docker auto-start (Windows, Linux, macOS) and AMD/ROCm GPU auto-detection
- **Advanced options:** Quantization (4-bit, 8-bit), context size, sampling parameters
- **Config protection:** User settings preserved across updates via `.example` pattern

## Documentation

- **[Smart Language Model Loader Guide](Readme/Smart_Language_Model_Loader_Guide.md)** - Complete guide for the unified vision-language and LLM loader
- **[Docker Installation Guide (Windows/WSL2)](Readme/Docker_Installation_Guide.md)** - WSL2 and Docker setup for Windows, including NVIDIA GPU configuration
- **[Docker Installation Guide (Linux)](Readme/Docker_Installation_Guide_Linux.md)** - Docker Engine + NVIDIA Container Toolkit setup for Linux
- **[Model Repository Reference](Readme/Model_Repos_Reference.md)** - HuggingFace repository URLs for all supported models

### Helper Scripts (Linux)

Located in `scripts/` — interactive shell scripts for Docker setup and management:

| Script | Description |
|--------|-------------|
| **[install-docker-engine.sh](scripts/install-docker-engine.sh)** | Install Docker Engine + NVIDIA Container Toolkit + pass (multi-distro) |
| **[remove-docker-nvidia.sh](scripts/remove-docker-nvidia.sh)** | Safely remove Docker and NVIDIA toolkit, with optional data purge |
| **[manage-docker-images.sh](scripts/manage-docker-images.sh)** | Pull, update, list, inspect, and clean SmartLML backend images (auto-detects NVIDIA/AMD GPU) |

All scripts support `--dry-run`, `--yes` (non-interactive), and an interactive menu.

## Nodes

| Node | Description |
|------|-------------|
| **Smart Language Model Loader** | Main node for loading and running vision-language and LLM models |
| **Pipe Out LM Advanced Options** | Configure advanced parameters (temperature, top_p, sampling) |

## Backends

| Backend | Type | Best For |
|---------|------|----------|
| **Transformers** | Local | No Docker needed, moderate performance |
| **Ollama (Docker)** | Docker | **Recommended** — fast, easy setup, auto-pulls models (NVIDIA + AMD/ROCm) |
| **vLLM (Docker)** | Docker | Multi-GPU / advanced inference (NVIDIA + AMD/ROCm) |
| **SGLang (Docker)** | Docker | Multi-GPU / RadixAttention (NVIDIA + AMD/ROCm) |
| **llama.cpp (Docker)** | Docker | Lightweight GGUF inference |
| **GGUF** | Local | Quantized models via llama-cpp-python |
| **WD14 Tagger** | Local | ONNX-based image tagging (booru tags) |

## Installation

Install via ComfyUI Manager or clone directly:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/r-vage/ComfyUI_SmartLML.git
cd ComfyUI_SmartLML
pip install -r requirements.txt
```

## Backward Compatibility

This project was split from ComfyUI_Eclipse. Workflows using `[Eclipse]` node names will continue to work — both `[SmartLML]` and `[Eclipse]` suffixes are registered.

## License

Apache License 2.0 — see [LICENSE](LICENSE) for details.
