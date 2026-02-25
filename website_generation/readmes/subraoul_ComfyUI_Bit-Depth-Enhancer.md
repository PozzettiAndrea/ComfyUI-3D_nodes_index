# ComfyUI Bit Depth Enhancer

Custom nodes for bit-depth enhancement and banding removal in ComfyUI.

## Description

This package provides nodes for enhancing 8-bit images to 16-bit with reduced banding artifacts. Includes both classical image processing methods and deep learning approaches.

**All nodes support batch processing.**

## Nodes

### 1. Bit Depth Enhancement (Classical)
Classical image processing methods for bit-depth enhancement. No ML models required.

**Methods:**
- **Bilateral+Dither** - Edge-aware filtering with Floyd-Steinberg dithering
- **Gradient Domain** - Gradient-space processing for smooth transitions
- **Multi-scale Fusion** - Laplacian pyramid decomposition
- **Fast Edge-Aware** - Guided filter for fast processing

**Parameters:**
| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `image` | IMAGE | - | Input image |
| `method` | STRING | 4 options | Enhancement algorithm |
| `strength` | FLOAT | 0.0-1.0 | Enhancement intensity (default: 0.7) |
| `preserve_edges` | BOOLEAN | - | Maintain edge sharpness (default: True) |

### 2. Save 16-bit TIFF
Export enhanced images as 16-bit TIFF files.

**Parameters:**
| Parameter | Type | Options | Description |
|-----------|------|---------|-------------|
| `images` | IMAGE | - | Input images |
| `filename_prefix` | STRING | - | Output filename prefix |
| `color_profile` | STRING | 4 options | Color space (sRGB, Adobe RGB, ProPhoto RGB, Linear) |

### 3. ABCD Bit-Depth Enhancement (8→16)
Deep learning model for 8-bit to 16-bit enhancement using the ABCD (Arbitrary Bitwise Coefficient for De-quantization) architecture.

**Based on:** [ABCD - Learning to Restore Compressed Images with Arbitrary Bit-depth](https://github.com/WooKyoungHan/ABCD)
**Paper:** CVPR 2023

ABCD uses coordinate-based implicit neural representation to reconstruct quantized images across arbitrary bit-depths. Three model architectures available:

- **SwinIR-ABCD** (Recommended) - Swin Transformer-based, highest quality (130h training, 4 GPUs)
- **RDN-ABCD** - Residual Dense Network, balanced performance (82h training, 2 GPUs)
- **EDSR-ABCD** - Enhanced Deep Residual, fastest processing (65h training, 1 GPU)

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `image` | IMAGE | Input 8-bit image |
| `model` | STRING | Model architecture (SwinIR-ABCD, RDN-ABCD, EDSR-ABCD) |

### 4. deepDeband (Banding Removal)
Deep learning model specifically trained for banding artifact removal using gradient-domain processing.

**Based on:** [deepDeband - Deep Gradient-Domain Image Debanding](https://github.com/RaymondLZhou/deepDeband)
**Paper:** ICIP 2022

Trained on 51,490 pairs of pristine and banded image patches (256×256). Two model variants:

- **deepDeband-w** (Recommended) - Uses weighted bilateral patch fusion for smoother results
- **deepDeband-f** - Direct patch processing, faster but may show seams

**Important:** These models were trained on real images and video frames. They may produce banding artifacts on synthetic images (3D renders, gradients, vector graphics).

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `image` | IMAGE | Input image with banding |
| `model` | STRING | Model variant (deepDeband-w, deepDeband-f) |
| `strength` | FLOAT | Debanding intensity (0.0-1.0, default: 1.0) |
| `tile_size` | INT | Tile size for processing (default: 256) |
| `tile_overlap` | INT | Overlap between tiles (default: 128) |

## Installation

1. Navigate to ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/subraoul/ComfyUI_Bit-Depth-Enhancer.git
   cd ComfyUI_Bit-Depth-Enhancer
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Restart ComfyUI

**Note:** This package is published to the ComfyUI Registry! You can also install manually following the instructions below.

### Dependencies
- Python 3.9+
- PyTorch 2.0+
- OpenCV 4.8+
- NumPy 1.24+
- scipy 1.11+
- tifffile 2023.0+

## Model Setup

Deep learning nodes require model checkpoints. Models should be placed in the ComfyUI models directory:

```
ComfyUI/models/bit_depth_enhancement/
├── abcd/
│   ├── edsr_abcd.pth
│   ├── rdn_abcd.pth
│   └── swinir_abcd.pth
└── deepdeband/
    ├── deepDeband_w.pth
    └── deepDeband_f.pth
```

### ABCD Models

Download from Google Drive (original ABCD repository):

- **EDSR-ABCD**: [Download](https://drive.google.com/file/d/1LAe1KUPe8MuOP_NRwBMfQ5W32o37Ln6W/view?usp=sharing)
- **RDN-ABCD**: [Download](https://drive.google.com/file/d/1tj7HiSpDxuHdEFQYG_EwWncDisfT_k88/view?usp=sharing)
- **SwinIR-ABCD**: [Download](https://drive.google.com/file/d/1zBGLttDMET7CQcj729sZyPKOVWpMyyMZ/view?usp=sharing)

Rename downloaded files to match the expected names and place in `ComfyUI/models/bit_depth_enhancement/abcd/`

### deepDeband Models

Download from GitHub (original deepDeband repository):

1. Navigate to [deepDeband checkpoints](https://github.com/RaymondLZhou/deepDeband/tree/master/pytorch-CycleGAN-and-pix2pix/checkpoints)

2. Download from subdirectories:
   - `deepDeband-w/latest_net_G.pth` → rename to `deepDeband_w.pth`
   - `deepDeband-f/latest_net_G.pth` → rename to `deepDeband_f.pth`

3. Place in `ComfyUI/models/bit_depth_enhancement/deepdeband/`

**Note:** You only need the generator weights (`latest_net_G.pth`), not the discriminator (`latest_net_D.pth`).

## Basic Usage

### Classical Enhancement Workflow
```
Load Image → Bit Depth Enhancement (Classical) → Save 16-bit TIFF
```

**Recommended Settings:**
- Method: Bilateral+Dither (general use) or Multi-scale Fusion (best quality)
- Strength: 0.7
- Preserve Edges: True
- Color Profile: sRGB (web) or Adobe RGB (print)

### ABCD Deep Learning Workflow
```
Load Image → ABCD Bit-Depth Enhancement → Save Image
```

**Recommended:** Use SwinIR-ABCD for best quality results.

### deepDeband Workflow
```
Load Image → deepDeband → Save Image
```

**Recommended:** Use deepDeband-w with default settings. Lower strength (0.5-0.7) for subtle enhancement.

**Warning:** Avoid using deepDeband on synthetic/rendered images as it may introduce artifacts.

## Known Limitations

- Classical methods cannot recover dynamic range not present in source
- Processing time scales with image resolution
- Deep learning models require GPU for reasonable performance
- Source image quality matters - heavily compressed JPEGs benefit less
- deepDeband may produce artifacts on synthetic/3D rendered images

## Output Format

- **Classical + Save 16-bit TIFF**: True 16-bit TIFF files (65,535 levels per channel)
- **Deep learning nodes**: Standard ComfyUI IMAGE output (can be saved with any ComfyUI save node)

## References

This implementation is based on the following research:

### ABCD
- **Paper:** "Arbitrary Bit-Depth Quantization for Image Restoration"
- **Repository:** https://github.com/WooKyoungHan/ABCD
- **Conference:** CVPR 2023
- **Authors:** WooKyoung Han et al.

### deepDeband
- **Paper:** "Deep Gradient-Domain Image Debanding"
- **Repository:** https://github.com/RaymondLZhou/deepDeband
- **Conference:** ICIP 2022
- **Authors:** Raymond L. Zhou, Shahrukh Athar, Zhongling Wang, Zhou Wang

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Credits

**Author:** raoul-ubuntu

**Built with:**
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [PyTorch](https://pytorch.org/)
- [OpenCV](https://opencv.org/)

## Support

Report issues or request features at: [GitHub Issues](https://github.com/subraoul/ComfyUI_Bit-Depth-Enhancer/issues)
