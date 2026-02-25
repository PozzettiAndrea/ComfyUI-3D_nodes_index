# Alloy ⚡️
> [!IMPORTANT]
> **🚧 Work in Progress 🚧**
> This project is currently under active development. APIs and CLI commands are subject to change. Use with caution.

A unified toolchain for converting open-source diffusion models (Stable Diffusion, Wan 2.1/2.2) into Apple's **Core ML** format for hardware-accelerated inference on macOS.

## Features

-   **Core ML Conversion**: Optimize models for Apple Silicon (Neural Engine/GPU).
-   **Wan 2.x Support**:
    -   Supports **Wan 2.1** and **Wan 2.2** (Text-to-Video).
    -   Supports **Image-to-Video / Edit** models (automatic 36-channel input detection).
    -   Implements **Int4 Quantization** to run 14B models on consumer Macs (64GB RAM recommended).
-   **Hunyuan Video Support**:
    -   Supports **HunyuanVideo** (Transformer conversion).
    -   Hybrid Runner: PyTorch Text Encoder + Core ML Transformer + PyTorch VAE.
-   **LTX-Video Support**:
    -   Supports **Lightricks/LTX-Video**.
    -   Efficient Core ML implementation for video generation.
-   **Flux ControlNet Support**:
    -   Full support for Flux ControlNet residuals (Base Model + ControlNet Model).
    -   **ComfyUI Nodes**: Dedicated nodes for loading and applying Core ML ControlNets.
-   **Stable Diffusion Support**: Wraps Apple's `python_coreml_stable_diffusion` for SDXL and SD3. (Requires optional `[sd]` extra)
-   **Lumina-Image 2.0 Support**: Implements Next-Gen DiT conversion using Gemma 2B text encoder.
-   **Full Pipeline**: Automates Download -> Convert -> Upload to Hugging Face.
-   **Progress Tracking**: Real-time conversion progress with phases, steps, elapsed time, and ETA estimation.
-   **Memory Monitoring**: Pre-flight memory checks warn if system resources are low before starting conversion.
-   **Dependency Management**: Uses `uv` to resolve complex conflicts between legacy Core ML scripts and modern Hugging Face libraries.

## Installation

1.  **Install uv**:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Install the Tool**:
    ```bash
    uv sync
    # Or install globally:
    # uv tool install .
    ```

3.  **Hugging Face Login** (Required for Uploads/Gated Models):
    ```bash
    uv run huggingface-cli login
    ```
    Or configure it via `.env` (recommended).

4.  **Configuration**:
    Copy the example environment file:
    ```bash
    cp .env.example .env
    ```
    Edit `.env` to set your `HF_TOKEN` and `OUTPUT_DIR`.

## Usage

You can run the tool using `uv run alloy`.

### Convert Stable Diffusion (SDXL/SD3)
> **Note:** SD support requires Apple's `python-coreml-stable-diffusion` package (not on PyPI).
> Install manually: `pip install git+https://github.com/apple/ml-stable-diffusion.git`

```bash
uv run alloy convert stabilityai/stable-diffusion-xl-base-1.0 \
  --type sd \
  --output-dir converted_models/sdxl \
  --quantization float16
```

### Convert Lumina-Image 2.0
```bash
uv run alloy convert Alpha-VLLM/Lumina-Image-2.0 \
  --type lumina \
  --quantization int4
```

### Convert Flux ControlNet (New!)
Support for converting **Flux ControlNet** models (X-Labs, InstantX, etc.) and preparing Base Flux models to accept them.

**1. Convert Base Model (ControlNet Ready)**
You must re-convert your base model with `--controlnet` to inject the residual inputs.
```bash
uv run alloy convert black-forest-labs/FLUX.1-schnell \
  --output-dir converted_models/flux_controlnet \
  --quantization int4 \
  --controlnet
```

**2. Convert ControlNet Model**
```bash
uv run alloy convert x-labs/flux-controlnet-canny \
  --type flux-controlnet \
  --output-dir converted_models/flux_canny \
  --quantization int4
```

### Convert Wan 2.1 / 2.2
Supports both T2V (Text-to-Video) and I2V (Image-to-Video). The converter automatically detects the input channels from the model config.

```bash
# Text-to-Video
uv run alloy convert Wan-AI/Wan2.1-T2V-14B-720P-Diffusers \
  --type wan \
  --output-dir converted_models/wan_t2v \
  --quantization int4

# Image-to-Video (36 channels)
uv run alloy convert Wan-AI/Wan2.1-I2V-14B-720P-Diffusers \
  --type wan \
  --output-dir converted_models/wan_i2v \
  --quantization int4
```

### Convert Flux
```bash
# Basic Conversion
uv run alloy convert black-forest-labs/FLUX.1-schnell \
  --output-dir converted_models/flux \
  --quantization int4

# With LoRA Baking
uv run alloy convert black-forest-labs/FLUX.1-schnell \
  --output-dir converted_models/flux_style \
  --quantization int4 \
  --lora "path/to/style.safetensors:0.8:1.0" \
  --lora "path/to/fix.safetensors:1.0"
```

### Civitai / Single-File Models
Support for directly loading `.safetensors` files (e.g., from Civitai) for **Flux** and **LTX-Video**. 

**Auto-Detection**: The CLI automatically detects the model architecture (Flux vs LTX) from the file header, so you can often skip the `--type` argument.

```bash
# Convert a single file checkpoint (Type auto-detected!)
uv run alloy convert /path/to/flux_schnell.safetensors \
  --output-dir converted_models/flux_civiai \
  --quantization int4
```

### Full Pipeline
Downloads a model, converts it, and uploads the Core ML package to your Hugging Face account.

### Run Locally
Verify your converted models by generating an image directly.

```bash
uv run alloy run converted_models/wan2.2  \
  --prompt "A astronaut riding a horse on mars, photorealistic, 4k" \
  --type wan \
  --output result.png
```

### Benchmark Performance
Measure real performance on your hardware:

```bash
uv run alloy run converted_models/flux \
  --prompt "test image" \
  --benchmark \
  --benchmark-runs 5 \
  --benchmark-output benchmarks.json
```

This will run 5 iterations and report:
- **Mean/median generation time**
- **Memory usage**
- **Per-step timing** breakdown
- **Statistical variance**

Results are saved to JSON for further analysis.

## ComfyUI Integration

Alloy includes **custom nodes** for seamless ComfyUI integration with Core ML acceleration!

### Installation

```bash
# 1. Install silicon-alloy
pip install -e .

# 2. Link to ComfyUI
ln -s /path/to/alloy/comfyui_custom_nodes /path/to/ComfyUI/custom_nodes/alloy

# 3. Restart ComfyUI
```

### Quick Start (ComfyUI)

1. **Install Alloy** via ComfyUI Manager
2. **Convert Model** using the `CoreMLQuickConverter` node
   - Select preset (e.g., "Flux Schnell")
   - Run once to convert (caches automatically)
3. **Load Model** using `CoreMLFluxWithCLIP`
4. **Generate!**

### Example Workflows

Check out `comfyui_custom_nodes/example_workflows/` for ready-to-use examples:
- **flux_txt2img.json**: Basic Flux text-to-image workflow
- **flux_img2img.json**: Flux image-to-image transformation
- **flux_allinone.json**: Simplified workflow with integrated CLIP/T5/VAE
- **convert_quick.json**: One-click model conversion in ComfyUI
- **convert_lora.json**: Bake multiple LoRAs into one model

See the [ComfyUI Node Reference](comfyui_custom_nodes/NODE_REFERENCE.md) for full documentation of all 13 nodes.

## Utility Commands

### Validate Models
```bash
alloy validate converted_models/flux/Flux_Transformer.mlpackage
```

### Show Model Info
```bash
alloy info converted_models/flux/Flux_Transformer.mlpackage
```

### List All Converted Models
```bash
alloy list-models
# or specify directory
alloy list-models --dir /path/to/models
```


## Architecture

-   **`src/alloy/cli.py`**: CLI entry point.
-   **`src/alloy/converters/`**: Model conversion logic (Flux, Wan, LTX, Hunyuan, Lumina, Stable Diffusion).
    -   All converters use **2-phase subprocess isolation** to prevent OOM during large model conversion.
    -   Intermediate files enable **resume capability** for interrupted conversions.
    -   Worker modules (`*_workers.py`) handle subprocess conversion logic.
-   **`src/alloy/runners/`**: Inference runners (PyTorch/Core ML hybrids).
-   **`src/alloy/utils/`**: Utilities for file handling, Hugging Face auth, and benchmarking.
-   **`pyproject.toml`**: Dependency overrides to force compatibility between `coremltools` and `diffusers`.

## Requirements
-   macOS 14+ (Sonoma) or newer.
-   Python 3.11+.
-   Apple Silicon (M1/M2/M3/M4).
