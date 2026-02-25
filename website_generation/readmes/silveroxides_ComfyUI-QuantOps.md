# ComfyUI-QuantOps

Extended quantization layouts for ComfyUI, enabling loading and inference with models quantized by [convert_to_quant](https://github.com/silveroxides/convert_to_quant).

## Supported Formats

| Format | Layout | quant_format | Status |
|--------|--------|--------------|--------|
| FP8 (tensor-wise) | `TensorCoreFP8Layout` | `float8_e4m3fn` | Supported (ComfyUI built-in) |
| FP8 (row-wise) | `RowWiseFP8Layout` | `float8_e4m3fn_rowwise` | WIP |
| FP8 (block-wise) | `BlockWiseFP8Layout` | `float8_e4m3fn_blockwise` | WIP |
| INT8 (block-wise) | `BlockWiseINT8Layout` | `int8` | Supported |

## Installation

1. Clone to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/silveroxides/ComfyUI-QuantOps.git
   ```

2. (Optional) Install Triton for GPU-accelerated INT8:
   ```bash
   # Activate your ComfyUI venv first!
   # Linux
   pip install triton
   # Windows
   pip install triton-windows
   ```

## Usage

Use the **QuantizedModelLoader** node to load models created by `convert_to_quant`:

1. Quantize your model with [convert_to_quant](https://github.com/silveroxides/convert_to_quant):
   ```bash
   convert_to_quant -i model.safetensors --int8 --comfy_quant --simple --block_size 128
   ```

2. Place the output in your ComfyUI models/checkpoints folder

### Text Encoder Loading

Use the **Load CLIP (Quantized)** node for INT8-quantized text encoders:

1. Quantize your text encoder (CLIP, T5, etc.):
   ```bash
   convert_to_quant -i t5xxl.safetensors --int8 --comfy_quant --simple --block_size 128
   ```

2. Place the output in `ComfyUI/models/text_encoders/`
3. Select the appropriate type (e.g., `sd3` or `flux` for T5-XXL)


## License

MIT License

## Acknowledgements

- [lyogavin](https://github.com/lyogavin) for [PR #10864](https://github.com/comfyanonymous/ComfyUI/pull/10864) to ComfyUI.
- [Clybius](https://github.com/Clybius) for inspiring me to take on quantization and his [Learned-Rounding](https://github.com/Clybius/Learned-Rounding) repository.
