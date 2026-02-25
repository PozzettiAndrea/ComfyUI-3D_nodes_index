# Niutonian GLM-4.6V ComfyUI Nodes (Transformer Version)

This is the transformer-based implementation of Niutonian GLM-4.6V nodes for ComfyUI with extensive memory optimizations to prevent CUDA out-of-memory errors.

**Version:** v0.1

## Features

- **Memory Optimized**: Multiple strategies to reduce VRAM usage
- **Quantization Support**: 4-bit and 8-bit quantization via bitsandbytes
- **Automatic Memory Management**: CUDA cache clearing and efficient tensor handling
- **Error Recovery**: Graceful handling of OOM errors with helpful messages
- **Niutonian Branding**: Professional custom node package with consistent naming

## Nodes

### 1. Niutonian GLM46VLoader
Loads the GLM-4.6V-Flash model with memory optimizations.

**Inputs:**
- `device`: auto/cuda/cpu (default: auto)
- `torch_dtype`: auto/bfloat16/float16/float32 (default: bfloat16)
- `low_cpu_mem_usage`: Enable low CPU memory usage (default: True)
- `load_in_8bit`: Enable 8-bit quantization (default: False)
- `load_in_4bit`: Enable 4-bit quantization (default: True)

**Outputs:**
- `GLM_MODEL`: Model and processor for other nodes

### 2. Niutonian GLM46VDescriber
Describes images using the GLM-4.6V vision model.

**Inputs:**
- `glm_model`: Model from Niutonian GLM46VLoader
- `image`: Input image tensor
- `user_prompt`: Description prompt (default: "Describe this image in detail.")
- `max_tokens`: Maximum output tokens (default: 1024)
- `temperature`: Sampling temperature (default: 0.7)

**Outputs:**
- `output_text`: Clean description text
- `raw_output`: Raw model output with thinking tags

### 3. Niutonian GLM46VAgenticSampler
Advanced KSampler that uses GLM-4.6V to verify generated images.

**Inputs:**
- Standard KSampler inputs (model, seed, steps, cfg, etc.)
- `glm_model`: GLM model for verification
- `vae`: VAE for decoding latents
- `verification_prompt`: Prompt for image verification
- `max_retries`: Maximum retry attempts (default: 3)

**Outputs:**
- `latent`: Final latent representation
- `verified_image`: Decoded image
- `is_match`: Boolean indicating if image matches prompt
- `summary`: Analysis summary

### 4. Niutonian GLM46VPromptGenerator
Intelligent prompt generator using GLM-4.6V vision model.

**Inputs:**
- `glm_model`: Model from Niutonian GLM46VLoader
- `mode`: Generation mode (create_from_image, refine_prompt, creative_variations, style_transfer)
- `base_prompt`: Base prompt text for refinement modes
- `style`: Target artistic style (photorealistic, artistic, cinematic, anime, etc.)
- `detail_level`: Level of detail (basic, detailed, very_detailed, ultra_detailed)
- `creativity`: Creativity factor (0.0-1.0)
- `max_tokens`: Maximum output tokens
- `reference_image`: Optional reference image
- `negative_elements`: Elements to avoid in prompts

**Outputs:**
- `positive_prompt`: Generated positive prompt
- `negative_prompt`: Generated negative prompt
- `analysis`: Analysis of prompt choices

## Memory Optimization Strategies

### 1. Quantization (Recommended)
Enable 4-bit or 8-bit quantization to significantly reduce VRAM usage:
- **4-bit**: ~75% memory reduction, minimal quality loss
- **8-bit**: ~50% memory reduction, negligible quality loss

### 2. Device Mapping
- Uses `device_map="sequential"` for efficient GPU memory allocation
- Automatically reserves 15% of VRAM for other operations
- Falls back to CPU if GPU memory is insufficient

### 3. Memory Management
- Automatic CUDA cache clearing before/after operations
- Efficient tensor movement and cleanup
- Gradient checkpointing enabled when available

## Installation

1. Clone this repository to your ComfyUI `custom_nodes` directory:
```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/Niutonian/comfyui_Niutonian_GLM_4_6V.git
```

2. Install dependencies:
```bash
cd comfyui_Niutonian_GLM_4_6V
pip install -r requirements.txt
```

3. Restart ComfyUI to load the new nodes

## Usage Tips

### For Low VRAM Systems (8-12GB)
1. Enable 4-bit quantization in Niutonian GLM46VLoader
2. Use `torch_dtype="float16"`
3. Set `low_cpu_mem_usage=True`

### For Medium VRAM Systems (16-24GB)
1. Try 8-bit quantization first
2. Fall back to 4-bit if needed
3. Use `torch_dtype="float16"`

### For Medium VRAM Systems (24-32GB)
1. Try 8-bit quantization first
2. Fall back to 4-bit if needed
3. Use `torch_dtype="bfloat16"`

### For High VRAM Systems (32GB+)
1. Can use without quantization
2. Use `torch_dtype="bfloat16"` for best performance
3. Consider `torch_dtype="float16"` if bfloat16 causes issues

## Troubleshooting

### CUDA Out of Memory
1. Enable 4-bit quantization
2. Reduce `max_tokens` in Niutonian GLM46VDescriber
3. Close other GPU applications
4. Restart ComfyUI to clear memory

### Model Loading Fails
1. Check internet connection (model downloads from HuggingFace)
2. Ensure sufficient disk space (~9GB for model)
3. Try CPU device if GPU fails
4. Check transformers version (>=5.0.0rc0 required)

### Slow Performance
1. Ensure CUDA is available and working
2. Use quantization (4-bit/8-bit) for faster inference
3. Reduce image resolution if possible
4. Check GPU utilization

### Grey or Missing Images
If the image is generated but appears grey or not showing properly:
1. Reduce the image size to 1024x1024 or lower
2. Try again with the smaller resolution
3. This often resolves display issues with large images

## Testing

Run the memory test script to validate your setup:
```bash
python test_memory.py
```

This will test different quantization configurations and report memory usage.

## Requirements

- Python 3.8+
- PyTorch 2.0+
- transformers 5.0.0rc0+
- bitsandbytes 0.41.0+ (for quantization)
- CUDA-capable GPU (recommended)
- 8GB+ VRAM (with quantization) or 24GB+ VRAM (without quantization)

## Model Information

- **Model**: zai-org/GLM-4.6V-Flash
- **Size**: ~9B parameters
- **Context**: 128K tokens
- **Vision**: Supports image + text input
- **License**: Check model repository for licensing terms

## About Niutonian

This package is part of the Niutonian suite of AI tools, providing professional-grade implementations of cutting-edge AI models for creative workflows.

**Version:** v0.1  
**Release Date:** January 5, 2026  
**Repository:** [Niutonian/comfyui_Niutonian_GLM_4_6V](https://github.com/Niutonian/comfyui_Niutonian_GLM_4_6V)

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history and changes.