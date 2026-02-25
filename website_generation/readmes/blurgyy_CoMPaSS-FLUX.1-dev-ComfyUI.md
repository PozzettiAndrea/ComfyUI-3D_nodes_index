# CoMPaSS-ComfyUI

A ComfyUI custom node that implements **CoMPaSS** for FLUX.1-dev models. CoMPaSS
enhances the spatial understanding capabilities of text-to-image diffusion models.

> **Paper:** [CoMPaSS: Enhancing Spatial Understanding in Text-to-Image Diffusion Models](https://arxiv.org/abs/2412.13195) (ICCV 2025)  
> **Official Repository:** [https://github.com/blurgyy/CoMPaSS](https://github.com/blurgyy/CoMPaSS)

## What is CoMPaSS?

CoMPaSS improves how diffusion models understand spatial relationships in text prompts
by adding positional encoding to the text attention mechanism. This results in better
adherence to spatial descriptions like "above", "below", "left of", "right of", etc.

## Installation

1. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/blurgyy/CoMPaSS-FLUX.1-dev-ComfyUI.git
```

2. Download the CoMPaSS weights for FLUX.1-dev from Hugging Face:
   - **FLUX.1-dev weights:** [https://huggingface.co/blurgy/CoMPaSS-FLUX.1](https://huggingface.co/blurgy/CoMPaSS-FLUX.1)
   - Place the downloaded LoRA weights (`CoMPaSS-FLUX.1-comfyui.safetensors`) in your
     ComfyUI `models/loras/` directory

3. Restart ComfyUI or refresh your browser if ComfyUI is already running.

## Usage

1. Load a FLUX.1-dev model in your workflow
2. **IMPORTANT**: Add the "CoMPaSS for FLUX.1-dev" node between your model loader and sampler
3. **IMPORTANT:** Load the CoMPaSS LoRA weights
4. Connect the model output through the CoMPaSS node
5. Use the patched model for generation

The node will automatically patch the FLUX.1-dev model's attention mechanism to include
CoMPaSS's spatial understanding improvements. For best results, use the official CoMPaSS
LoRA weights alongside this node.

## Example Workflow

An example ComfyUI workflow is provided in `example-comfyui-workflow.json`. Load this
workflow to see CoMPaSS in action with a complete setup.

## Results Comparison

The following comparison demonstrates CoMPaSS's improved spatial understanding using the
prompt: **"A photo of a sheep below a sink"**

### Without CoMPaSS
| Image 1 | Image 2 |
|---------|---------|
| ![Without CoMPaSS - Image 1](assets/without_compass/0.avif) | ![Without CoMPaSS - Image 2](assets/without_compass/1.avif) |

### With CoMPaSS
| Image 1 | Image 2 |
|---------|---------|
| ![With CoMPaSS - Image 1](assets/with_compass/0.avif) | ![With CoMPaSS - Image 2](assets/with_compass/1.avif) |

As seen above, CoMPaSS significantly improves the model's ability to correctly position
the sheep **below** the sink, demonstrating better spatial understanding of the text
prompt.

## Requirements

- ComfyUI
- FLUX.1-dev model
- PyTorch

## Node Details

**Input:**
- `model`: A FLUX.1-dev model (MODEL type)

**Output:**
- `model`: The same model with CoMPaSS spatial attention patching applied (MODEL type)

**Category:** Conditioning

## Technical Implementation

This implementation patches the `DoubleStreamBlock` forward method in FLUX.1-dev models
to include positional encoding in the text attention mechanism. The key modification
adds learned positional embeddings to text queries and keys while preserving the
original values, enabling better spatial relationship understanding.

## Citation

If you use CoMPaSS in your research, please cite the original paper:

```bibtex
@inproceedings{zhang2025compass,
  title={CoMPaSS: Enhancing Spatial Understanding in Text-to-Image Diffusion Models},
  author={Zhang, Gaoyang and Fu, Bingtao and Fan, Qingnan and Zhang, Qi and Liu, Runxing and Gu, Hong and Zhang, Huaqi and Liu, Xinguo},
  booktitle={ICCV},
  year={2025}
}
```

## Links

- **Official Repository:** [https://github.com/blurgyy/CoMPaSS](https://github.com/blurgyy/CoMPaSS)
- **Project Page:** [https://compass.blurgy.xyz](https://compass.blurgy.xyz)
- **arXiv:** [https://arxiv.org/abs/2412.13195](https://arxiv.org/abs/2412.13195)
- **FLUX.1-dev Weights:** [https://huggingface.co/blurgy/CoMPaSS-FLUX.1](https://huggingface.co/blurgy/CoMPaSS-FLUX.1)
