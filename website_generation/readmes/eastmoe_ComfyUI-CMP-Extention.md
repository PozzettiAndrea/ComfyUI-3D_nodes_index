
# ComfyUI-CMP-Extention

![./static/2026-02-08-123234.png](https://github.com/eastmoe/ComfyUI-CMP-Extention/blob/main/static/2026-02-08-123234.png?raw=true)

[中文](./README_zh.md)

## Introduction
ComfyUI-CMP-Extention is a ComfyUI acceleration extension designed specifically for the **170HX GPU**. Based on research findings from **["Instruction-Level Performance Analysis and Optimization Strategies for Constrained AI Accelerators A Case Study of CMP 170HX"](https://github.com/eastmoe/cmp_ext/blob/main/paper/paper_20260208.pdf).**, it enhances inference performance by optimizing specific operators. This extension requires the use of the [cmp_ext](https://github.com/eastmoe/cmp_ext) library.

## Installation

1. Ensure that [cmp_ext](https://github.com/eastmoe/cmp_ext) is installed and configured.
2. Navigate to the `custom_nodes` directory of your ComfyUI installation.
3. Run the following command to clone this extension:

```bash
git clone https://github.com/eastmoe/ComfyUI-CMP-Extention
```

4. Restart ComfyUI.

## Usage

1. In ComfyUI, locate the **CmpExt3ControlPanelNode** within the **CmpExt3** category in the node menu.
2. Insert this node **after the model loader** and **before the sampler**.
3. Check or uncheck the operator types you wish to optimize as needed.
4. Connect the nodes:
   - Connect the output of the model loader node to the `model` input (optional)
   - Connect the output of the CLIP loader node to the `clip` input (optional)
   - Connect the output of the VAE loader node to the `vae` input (optional)

## Node Parameters Description

### Core Operators
- **Ops: Linear**: Linear layer optimization (Enabled by default)
- **Ops: Conv2d**: Convolutional layer optimization (Enabled by default)
- **Ops: ConvTranspose2d (VAE Upscale)**: Transposed convolution optimization, used for VAE upscaling (Enabled by default)
- **Ops: BMM (Attention)**: Batch matrix multiplication optimization in attention mechanisms (Enabled by default)

### Normalization Layers
- **Norm: GroupNorm (VAE)**: Group normalization optimization, primarily used for VAE (Enabled by default)
- **Norm: LayerNorm (CLIP/Transformer)**: Layer normalization optimization, used for CLIP/Transformer (Enabled by default)

### Activation Functions
- **Act: SiLU / Swish (VAE Main Suspect!)**: SiLU/Swish activation function optimization, the primary optimization target in VAE (Enabled by default)
- **Act: GELU (CLIP/UNet)**: GELU activation function optimization, used for CLIP/UNet (Enabled by default)
- **Act: Softmax (Attention)**: Softmax activation function optimization, used in attention mechanisms (Enabled by default)
- **Act: Mish**: Mish activation function optimization (Disabled by default)
- **Act: Softplus**: Softplus activation function optimization (Disabled by default)
- **Act: Softsign**: Softsign activation function optimization (Disabled by default)

## Notes

1. This extension is specifically optimized for the **170HX GPU**. Other graphics card models may not achieve the same results or may encounter compatibility issues.
2. If you experience performance degradation or instability, try disabling some of the operator optimizations.


## Node Definition Reference

```python
class CmpExt3ControlPanelNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # --- Core ---
                "enable_linear": ("BOOLEAN", {"default": True, "label": "Ops: Linear"}),
                "enable_conv2d": ("BOOLEAN", {"default": True, "label": "Ops: Conv2d"}),
                "enable_conv_transpose": ("BOOLEAN", {"default": True, "label": "Ops: ConvTranspose2d (VAE Upscale)"}),
                "enable_bmm": ("BOOLEAN", {"default": True, "label": "Ops: BMM (Attention)"}),
              
                # --- Norms ---
                "enable_group_norm": ("BOOLEAN", {"default": True, "label": "Norm: GroupNorm (VAE)"}),
                "enable_layer_norm": ("BOOLEAN", {"default": True, "label": "Norm: LayerNorm (CLIP/Transformer)"}),
              
                # --- Activations (Suspects) ---
                "enable_silu": ("BOOLEAN", {"default": True, "label": "Act: SiLU / Swish (VAE Main Suspect!)"}),
                "enable_gelu": ("BOOLEAN", {"default": True, "label": "Act: GELU (CLIP/UNet)"}),
                "enable_softmax": ("BOOLEAN", {"default": True, "label": "Act: Softmax (Attention)"}),
                "enable_mish": ("BOOLEAN", {"default": False, "label": "Act: Mish"}),
                "enable_softplus": ("BOOLEAN", {"default": False, "label": "Act: Softplus"}),
                "enable_softsign": ("BOOLEAN", {"default": False, "label": "Act: Softsign"}),
            },
            "optional": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "vae": ("VAE",),
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    RETURN_NAMES = ("model", "clip", "vae")
    FUNCTION = "execute_patch"
    CATEGORY = "CmpExt3"
```

## License

MIT License

---

**Disclaimer**: This extension is implemented based on academic research and has limited engineering stability. The author is not responsible for any issues caused by the use of this extension. Please test thoroughly and understand the associated risks before use.
