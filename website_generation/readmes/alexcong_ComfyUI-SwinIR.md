# ComfyUI-SwinIR

A ComfyUI custom node for SwinIR (Swin Transformer for Image Restoration) supporting image super-resolution and denoising.

## Features

- **Multiple Model Types**: Support for classical SR, lightweight SR, real-world SR, and denoising
- **Flexible Configuration**: Customizable model parameters (window size, embed dim, depths, etc.)
- **Memory Efficient**: Tiled processing for large images
- **Batch Processing**: Process multiple images at once

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/alexcong/ComfyUI-SwinIR.git
```

2. Install dependencies:
```bash
cd ComfyUI-SwinIR
pip install -r requirements.txt
```

3. Download SwinIR models from the [official repository](https://github.com/JingyunLiang/SwinIR/releases) and place them in `ComfyUI/models/upscale_models/`

## Usage

### Nodes

#### SwinIR Model Loader
Loads a SwinIR model with specified configuration.

**Parameters:**
- `model_name`: Select from available models in `upscale_models` folder
- `model_type`: Choose model type (classicalSR, lightweightSR, realSR, denoising)
- `upscale`: Upscale factor (1-8)
- `window_size`: Window size for attention (default: 8)
- `embed_dim`: Embedding dimension (default: 180)
- `depths`: Comma-separated depths for each layer (e.g., "6, 6, 6, 6, 6, 6")
- `num_heads`: Comma-separated number of attention heads (e.g., "6, 6, 6, 6, 6, 6")
- `mlp_ratio`: MLP ratio (default: 2.0)
- `img_size`: Training image size (default: 128) - **must match model's training size**

#### SwinIR Upscale/Denoise
Processes images using the loaded SwinIR model.

**Parameters:**
- `swinir_model`: Model from SwinIR Model Loader
- `images`: Input images
- `tile_size`: Tile size for processing (default: 512)
- `overlap`: Overlap between tiles (default: 32)

### Example Workflow

1. Add **SwinIR Model Loader** node
2. Configure model parameters to match your downloaded model
3. Add **SwinIR Upscale/Denoise** node
4. Connect model output to the upscale node
5. Connect your image input
6. Run!

### Common Model Configurations

#### Classical SR (x2)
- Model: `001_classicalSR_DF2K_s64w8_SwinIR-M_x2.pth`
- Type: classicalSR
- Upscale: 2
- Window Size: 8
- Embed Dim: 180
- Depths: "6, 6, 6, 6, 6, 6"
- Num Heads: "6, 6, 6, 6, 6, 6"
- MLP Ratio: 2.0
- **Img Size: 64** (from `s64` in filename)

#### Lightweight SR (x2)
- Model: `002_lightweightSR_DIV2K_s64w8_SwinIR-S_x2.pth`
- Type: lightweightSR
- Upscale: 2
- Window Size: 8
- Embed Dim: 60
- Depths: "6, 6, 6, 6"
- Num Heads: "6, 6, 6, 6"
- MLP Ratio: 2.0
- **Img Size: 64**

#### Real-World SR (x4)
- Model: `003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth`
- Type: realSR
- Upscale: 4
- Window Size: 8
- Embed Dim: 180
- Depths: "6, 6, 6, 6, 6, 6"
- Num Heads: "6, 6, 6, 6, 6, 6"
- MLP Ratio: 2.0
- **Img Size: 64**

#### Color Denoising (Noise 25)
- Model: `005_colorDN_DFWB_s128w8_SwinIR-M_noise25.pth`
- Type: denoising
- Upscale: 1
- Window Size: 8
- Embed Dim: 180
- Depths: "6, 6, 6, 6, 6, 6"
- Num Heads: "6, 6, 6, 6, 6, 6"
- MLP Ratio: 2.0
- **Img Size: 128** (from `s128` in filename)

## Testing

Run the test suite:
```bash
python test_nodes.py
```

### Model Requirements for Testing

The test suite includes a **real model loading test** that requires downloading a pre-trained model:

1. Download `005_colorDN_DFWB_s128w8_SwinIR-M_noise25.pth` from:
   - [SwinIR GitHub Releases](https://github.com/JingyunLiang/SwinIR/releases/tag/v0.0)

2. Place the model in the same directory as `test_nodes.py`

Without the model, the real model test will be skipped. Other tests run using synthetic models and don't require downloads.

### Test Coverage
- Model loading test
- Basic upscaling test
- Tiled processing test
- Batch processing test
- **Real model loading test** (validates the attention mask fix)

## Credits

- SwinIR: [JingyunLiang/SwinIR](https://github.com/JingyunLiang/SwinIR)
- Paper: [SwinIR: Image Restoration Using Swin Transformer](https://arxiv.org/abs/2108.10257)

## License

This project follows the same license as the original SwinIR repository.
