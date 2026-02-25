# Eric UniPic3 Nodes for ComfyUI

**Version 1.0.0** | **Author:** Eric Hiss (GitHub: EricRollei) | **License:** MIT

ComfyUI custom nodes for **Skywork UniPic3** - a state-of-the-art unified multimodal framework for single-image editing and multi-image composition with Human-Object Interaction (HOI) capabilities.

---

## Table of Contents

1. [About UniPic3](#about-unipic3)
2. [What's Novel](#whats-novel)
3. [Prompt Format & Image Referencing](#prompt-format--image-referencing)
4. [Model Variants](#model-variants)
5. [Node Reference](#node-reference)
6. [Usage Examples](#usage-examples)
7. [Design Philosophy](#design-philosophy)
8. [Technical Details](#technical-details)
9. [Future Work](#future-work)
10. [Credits & Acknowledgments](#credits--acknowledgments)
11. [Installation](#installation)

---

## About UniPic3

### Overview

UniPic3 is the third generation of Skywork's UniPic family, released in January 2026. Unlike its predecessors (UniPic1 and UniPic2 which include text-to-image capabilities), **UniPic3 is specifically designed for image editing and multi-image composition tasks**.

The model excels at:

- **Single-image editing**: Modify images based on text instructions while preserving unedited regions
- **Multi-image composition**: Combine 2-6 reference images into a coherent unified scene
- **Human-Object Interaction (HOI)**: Create realistic compositions where people naturally interact with objects (wearing clothes, holding items, using equipment)

### What UniPic3 is NOT

UniPic3 does **not** support pure text-to-image generation. It always requires at least one input image. For T2I capabilities, use UniPic1 or UniPic2.

### Supported Tasks

| Task | Input | Description |
|------|-------|-------------|
| Single Edit | 1 image + prompt | Edit an image with text instructions |
| Edit with Reference | 1 image + refs + prompt | Edit using style/content from references |
| Multi-Image Compose | 2-6 images + prompt | Combine multiple elements into one scene |
| Virtual Try-On | Person + clothing images | Put garments on a person naturally |
| Product Composition | Product + background + props | Create product photography compositions |

---

## What's Novel

UniPic3 introduces several innovations that set it apart from previous image editing models:

### 1. Unified Sequence Modeling

UniPic3 reformulates both single-image editing and multi-image composition as **conditional generation on a unified sequence representation**. This means:

- A single model handles both tasks without mode switching
- Knowledge transfers between editing and composition tasks
- Consistent behavior across different input configurations

### 2. Arbitrary Input Flexibility

Unlike models like Qwen-Image-Edit-2509 which support limited input configurations:

- **1-6 input images** supported in a single forward pass
- **Arbitrary resolutions** within a 1024×1024 pixel budget
- **Arbitrary output resolutions** (not fixed to square outputs)

### 3. HOI-Focused Training

The model was trained with a focus on Human-Object Interaction scenarios:

- **700K high-quality HOI training samples** covering apparel, tools, instruments, furniture, sports equipment
- **Comprehensive data curation pipeline** specifically designed for multi-image composition
- Handles realistic occlusions, lighting, and spatial relationships

### 4. Distillation for Fast Inference

Three model variants provide quality/speed tradeoffs:

- **Teacher**: Full 50-step diffusion for maximum quality
- **DMD**: Distribution Matching Distillation for 8-step inference
- **Consistency**: Trajectory-consistent mapping for geometric alignment

The distilled models achieve **12.5× speedup** while maintaining high quality.

---

## Prompt Format & Image Referencing

### Numbered Image References

**UniPic3 understands numbered image references in prompts.** Since it uses Qwen2.5-VL (a vision-language model) as the text encoder, you can explicitly reference which image should contribute what to the output.

Images are numbered **1-indexed** in the order they're provided:

| Node Input | Image Number in Prompt |
|------------|------------------------|
| `image` (Edit) or `image1` (Compose) | "image 1" |
| `ref_image1` or `image2` | "image 2" |
| `ref_image2` or `image3` | "image 3" |
| `ref_image3` or `image4` | "image 4" |
| `ref_image4` or `image5` | "image 5" |
| `ref_image5` or `image6` | "image 6" |

### Example Prompts with Numbered References

**Virtual try-on (2 images):**
```
"The person from image 1 wearing the jacket from image 2"
"Put the dress from image 2 on the model in image 1"
"Make the woman in image 1 wear the outfit from image 2"
```

**Pose transfer (2 images):**
```
"Make the person in image 1 do the exact same pose as the person in image 2"
"Transfer the pose from image 2 to the subject in image 1"
```

**Multi-item composition (3+ images):**
```
"The person from image 1 wearing the shirt from image 2 and the pants from image 3"
"Place the subject from image 1 in the scene from image 2 holding the object from image 3"
"The girl from image 1 wears the black dress from image 2 and sits in the pose from image 3"
```

**Style transfer:**
```
"Edit image 1 in the artistic style of image 2"
"Apply the color palette from image 2 to image 1"
```

### Prompting Tips

1. **Be explicit about image roles**: Instead of "put the jacket on the person", say "put the jacket from image 2 on the person in image 1"

2. **Name what you want from each image**: "The face from image 1, the clothing from image 2, the background from image 3"

3. **Describe the desired output**: Don't just say what to combine - describe the final result: "Professional fashion photo of the model in image 1 wearing the complete outfit from images 2-4"

4. **Use natural language**: The Qwen2.5-VL encoder understands conversational prompts, not just keywords

5. **Be specific about preservation**: "Keep the face and hair from image 1 exactly, only change the clothing to match image 2"

### Alternative: Content-Based References

You can also reference images by describing their content (the model will infer which image you mean):

```
"The woman wearing the red dress"  (if only one image has a red dress)
"Put the cat on the couch"  (if images clearly contain a cat and a couch)
```

However, **numbered references are more reliable** when images have similar content or when precision matters.

---

## Model Variants

### Teacher Model (`Skywork/Unipic3`)

The full-quality teacher model trained with multi-step diffusion sampling.

| Attribute | Value |
|-----------|-------|
| **Steps** | 50 (recommended) |
| **Quality** | Highest |
| **Speed** | ~30-60 seconds per image |
| **Best For** | Final outputs, complex compositions, maximum fidelity |
| **Transformer Path** | `H:\Testing\Unipic3\transformer` |

### DMD Model (`Skywork/Unipic3-DMD`)

Distribution Matching Distillation model that matches the teacher's output distribution in fewer steps.

| Attribute | Value |
|-----------|-------|
| **Steps** | 8 (recommended) |
| **Quality** | High (close to teacher) |
| **Speed** | ~5-10 seconds per image |
| **Best For** | Rapid iteration, preview generation, production workflows |
| **Transformer Path** | `H:\Testing\Unipic3-DMD\ema_transformer` |

### Consistency Model (`Skywork/Unipic3-Consistency-Model`)

Trajectory-consistent mapping model optimized for geometric alignment.

| Attribute | Value |
|-----------|-------|
| **Steps** | ≤8 |
| **Quality** | Good (geometric focus) |
| **Speed** | ~5-10 seconds per image |
| **Best For** | Tasks requiring structural consistency, geometric alignment |
| **Transformer Path** | `H:\Testing\Unipic3-Consistency-Model\ema_transformer` |
| **Note** | May not perform well on all editing tasks |

---

## Node Reference

### Eric UniPic3 Load Model

Loads the UniPic3 pipeline with your choice of transformer variant.

#### Inputs

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `variant` | enum | `teacher` | Model variant: `teacher`, `dmd`, or `consistency` |
| `base_pipeline_path` | string | `H:\Training\Qwen-Image-Edit-2511` | Path to base pipeline (VAE, text encoder, scheduler) |
| `transformer_path_override` | string | `""` | Optional: Override the default transformer path |
| `precision` | enum | `bf16` | Model precision: `bf16`, `fp16`, or `fp32` |
| `device` | enum | `cuda` | Target device |
| `keep_in_vram` | bool | `True` | Cache pipeline between runs for faster subsequent generations |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `pipeline` | UNIPIC3_PIPELINE | Pipeline object for use with Edit/Compose nodes |

#### Notes

- The pipeline is cached globally - loading the same variant twice reuses the cached pipeline
- Switching variants automatically unloads the previous pipeline
- Set `keep_in_vram=False` to free VRAM after each generation (slower but lower memory)

---

### Eric UniPic3 Image Edit

Edit a single image with optional reference images for style or content transfer.

#### Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `pipeline` | UNIPIC3_PIPELINE | Yes | - | Pipeline from loader |
| `image` | IMAGE | Yes | - | Primary image to edit (= "image 1" in prompt) |
| `prompt` | string | Yes | - | Edit instruction (can reference images by number) |
| `ref_image1` | IMAGE | No | None | Reference image (= "image 2" in prompt) |
| `ref_image2` | IMAGE | No | None | Additional reference (= "image 3" in prompt) |
| `ref_image3` | IMAGE | No | None | Additional reference (= "image 4" in prompt) |
| `ref_image4` | IMAGE | No | None | Additional reference (= "image 5" in prompt) |
| `ref_image5` | IMAGE | No | None | Additional reference (= "image 6" in prompt) |
| `negative_prompt` | string | No | `""` | What to avoid |
| `steps` | int | No | `50` | Inference steps |
| `true_cfg_scale` | float | No | `4.0` | CFG scale (quality control) |
| `seed` | int | No | `0` | Random seed |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `image` | IMAGE | Edited image |

#### Use Cases

**Simple edit (no references):**
```
image: Photo of a person
prompt: "Change the background to a sunset beach"
```

**Style transfer (with numbered reference):**
```
image: Photo to edit
ref_image1: Painting with desired style
prompt: "Edit image 1 in the artistic style of image 2"
```

**Content addition (with numbered reference):**
```
image: Photo of person without hat
ref_image1: Photo of a hat
prompt: "Add the hat from image 2 to the person in image 1"
```

---

### Eric UniPic3 Compose (HOI)

Compose multiple images into a unified scene with natural interactions.

#### Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `pipeline` | UNIPIC3_PIPELINE | Yes | - | Pipeline from loader |
| `prompt` | string | Yes | - | Composition instruction (reference images by number) |
| `image1` | IMAGE | Yes | - | Primary subject (= "image 1" in prompt) |
| `image2` | IMAGE | Yes | - | Item to compose (= "image 2" in prompt) |
| `image3` | IMAGE | No | None | Additional item (= "image 3" in prompt) |
| `image4` | IMAGE | No | None | Additional item (= "image 4" in prompt) |
| `image5` | IMAGE | No | None | Additional item (= "image 5" in prompt) |
| `image6` | IMAGE | No | None | Additional item (= "image 6" in prompt) |
| `negative_prompt` | string | No | `""` | What to avoid |
| `steps` | int | No | `50` | Inference steps |
| `true_cfg_scale` | float | No | `4.0` | CFG scale |
| `seed` | int | No | `0` | Random seed |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `image` | IMAGE | Composed image |

#### Image Order Guidelines

The order of images affects the composition. Recommended order:

1. **image1**: Main subject (person for try-on, primary product)
2. **image2**: Primary item to add (main garment, key object)
3. **image3**: Secondary item (accessory, secondary garment)
4. **image4-6**: Additional elements (props, background elements)

#### Use Cases

**Virtual try-on (with numbered references):**
```
image1: Full-body photo of person
image2: Jacket (on white background)
prompt: "The person from image 1 wearing the jacket from image 2"
```

**Complete outfit (with numbered references):**
```
image1: Person
image2: Dress
image3: Shoes
image4: Handbag
prompt: "Professional photo of the model from image 1 wearing the dress from image 2, shoes from image 3, carrying the bag from image 4"
```

**Product photography (with numbered references):**
```
image1: Product
image2: Background scene
image3: Prop item
prompt: "Place the product from image 1 in the scene from image 2 with the prop from image 3 beside it"
```

---

### Eric UniPic3 Unload Model

Unloads the cached pipeline and frees VRAM.

#### Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `trigger` | any | No | Connect any output to trigger unload after that node |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `status` | string | Unload status message |

#### Notes

- This is an output node - it executes when triggered
- Use when switching to other models or when VRAM is needed
- Not necessary if `keep_in_vram=False` in the loader

---

## Usage Examples

### Basic Edit Workflow

```
[Load Image] ─────────────────────────┐
                                      ▼
[Eric UniPic3 Load Model] ──► [Eric UniPic3 Image Edit] ──► [Preview Image]
    variant: teacher                  prompt: "Add dramatic lighting"
    precision: bf16                   steps: 50
                                      true_cfg_scale: 4.0
```

### Virtual Try-On Workflow

```
[Load Image: Person] ────► image1 ─┐
                                   │
[Load Image: Clothing] ──► image2 ─┼──► [Eric UniPic3 Compose] ──► [Save Image]
                                   │        prompt: "Person from image 1 wearing the jacket from image 2"
[Eric UniPic3 Load Model] ─────────┘        steps: 50
    variant: dmd (for speed)                seed: 12345
```

### Multi-Item Composition

```
[Person Photo] ────────► image1 ─┐
[Dress] ───────────────► image2 ─┤
[Shoes] ───────────────► image3 ─┼──► [Eric UniPic3 Compose]
[Handbag] ─────────────► image4 ─┤        prompt: "Model from image 1 in the dress from image 2, 
[Sunglasses] ──────────► image5 ─┘                 shoes from image 3, bag from image 4, 
                                                   sunglasses from image 5"
                                          steps: 50
```

---

## Design Philosophy

### Why These Nodes?

Our node design follows several key principles:

#### 1. Faithful to Model Capabilities

UniPic3 is an **editing and composition model**, not a text-to-image model. Rather than forcing T2I functionality through workarounds (blank images, noise initialization), we expose only what the model actually does well:

- Edit node for single-image editing
- Compose node for multi-image composition

This prevents user confusion and ensures quality outputs.

#### 2. Flexibility Through Optional Inputs

The Edit node accepts 1-6 images (1 required + 5 optional references), while the Compose node requires 2+ images. This matches how users actually work:

- Sometimes you just want to edit one image
- Sometimes you need reference images for style/content
- Sometimes you're composing multiple elements

Using optional inputs rather than separate nodes for each case keeps the workflow simple.

#### 3. Sensible Defaults

- **steps: 50** - Matches the teacher model's recommended setting
- **true_cfg_scale: 4.0** - Official recommended value from Skywork
- **precision: bf16** - Best quality/speed tradeoff for modern GPUs
- **keep_in_vram: True** - Most users want fast subsequent generations

#### 4. Pipeline Caching

The 58GB+ model takes significant time to load. Our global cache ensures:

- First load: Full load time (~30-60 seconds)
- Subsequent runs: Near-instant (reuses cached pipeline)
- Variant switching: Automatic unload/reload

#### 5. Clean Separation of Concerns

```
Loader Node ──► Pipeline Object ──► Processing Nodes ──► Output
```

The loader handles all the complexity of:
- Finding transformer paths
- Loading VAE, text encoder, scheduler from base pipeline
- Managing precision and device placement
- Caching

Processing nodes (Edit, Compose) just use the pipeline - they don't need to know about loading details.

### Why Not a Single "Universal" Node?

We considered a single node that handles all modes, but rejected it because:

1. **Confusing UI**: Too many conditionally-relevant inputs
2. **Error-prone**: Easy to misconfigure (e.g., T2I mode with no images)
3. **Poor discoverability**: Users wouldn't know what's possible

Two focused nodes (Edit + Compose) with clear purposes are better UX.

### Why Use the Diffusers Pipeline?

We leverage `QwenImageEditPlusPipeline` from diffusers rather than implementing custom inference because:

1. **Tested**: The pipeline is battle-tested by the community
2. **Maintained**: Diffusers team maintains compatibility
3. **Features**: Includes optimizations, progress bars, etc.
4. **Simplicity**: Less code to maintain

We only override what's necessary (transformer loading from local paths).

---

## Technical Details

### Architecture

UniPic3 uses the **QwenImageTransformer2DModel** architecture:

| Parameter | Value |
|-----------|-------|
| Layers | 60 |
| Attention Heads | 24 |
| Joint Attention Dim | 3584 |
| Patch Size | 2 |
| In Channels | 64 |
| Out Channels | 16 |
| Parameters | ~13B |

### Text Encoder: Qwen2.5-VL-7B

The text encoder is **Qwen2.5-VL-7B-Instruct**, a vision-language model that:
- Understands both text and images jointly
- Enables numbered image references in prompts ("image 1", "image 2")
- Processes natural language instructions conversationally
- Links prompt text to specific input images

This is why UniPic3 can understand prompts like "put the jacket from image 2 on the person in image 1" - the VL encoder sees both the text and all input images together.

### Memory Requirements

| Component | Size (bf16) | Location |
|-----------|-------------|----------|
| Transformer | ~41 GB | `H:\Testing\Unipic3*` |
| Text Encoder (Qwen2.5-VL-7B) | ~16.5 GB | `Qwen-Image-Edit-2511\text_encoder` |
| VAE (AutoencoderKLQwenImage) | ~254 MB | `Qwen-Image-Edit-2511\vae` |
| **Total** | **~58 GB** | |

**Recommended GPU**: 64GB+ VRAM (RTX PRO 6000, A100, etc.)

### File Structure

```
Eric_UniPic3/
├── __init__.py              # Node registration
├── README.md                # This documentation
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Package metadata
└── nodes/
    ├── __init__.py
    ├── eric_unipic3_utils.py    # Shared utilities, caching
    ├── eric_unipic3_loader.py   # Model loading node
    ├── eric_unipic3_edit.py     # Edit node
    └── eric_unipic3_compose.py  # Compose node
```

### Default Paths

| Component | Path |
|-----------|------|
| Teacher Transformer | `H:\Testing\Unipic3\transformer` |
| DMD Transformer | `H:\Testing\Unipic3-DMD\ema_transformer` |
| Consistency Transformer | `H:\Testing\Unipic3-Consistency-Model\ema_transformer` |
| Base Pipeline | `H:\Training\Qwen-Image-Edit-2511` |

---

## Future Work

### Planned Improvements

#### 1. Quantization Support

The ~58GB VRAM requirement limits accessibility. Planned quantization options:

- **INT8 quantization**: ~30GB VRAM, minimal quality loss
- **NF4 quantization**: ~15GB VRAM, some quality tradeoff
- **GGUF support**: For broader hardware compatibility

#### 2. Batch Processing

Current implementation processes one composition at a time. Future versions may support:

- Batch image inputs for throughput
- Queue-based processing for large jobs

#### 3. Resolution Control

Add explicit output resolution control:

- Target width/height parameters
- Aspect ratio presets
- Automatic scaling within pixel budget

#### 4. Advanced CFG Options

Expose additional pipeline parameters:

- `guidance_scale` (currently only `true_cfg_scale` exposed)
- CFG rescale options
- Negative prompt embedding strength

#### 5. Image Preprocessing

Optional preprocessing nodes for:

- Background removal for cleaner composition
- Auto-cropping to subject
- Resolution normalization across inputs

#### 6. LoRA Support

If/when LoRA fine-tunes become available for UniPic3:

- LoRA loading in the pipeline loader
- Multiple LoRA blending
- LoRA strength control

### Known Limitations

1. **No T2I**: UniPic3 requires input images - this is by design
2. **Consistency model quality**: May not work well for all editing tasks
3. **VRAM hungry**: 58GB+ makes it inaccessible to consumer GPUs
4. **Single output**: Currently outputs one image per run

---

## Credits & Acknowledgments

### UniPic3 Model

**Skywork UniPic 3.0** is developed by **Skywork AI**.

- **GitHub**: [SkyworkAI/UniPic](https://github.com/SkyworkAI/UniPic)
- **Project Page**: [skywork-unipic-v3.github.io](https://skywork-unipic-v3.github.io)
- **Paper**: [arXiv:2601.15664](https://arxiv.org/abs/2601.15664) - "Skywork UniPic 3.0: Unified Multi-Image Composition via Sequence Modeling"
- **Model Weights**: [Hugging Face Collection](https://huggingface.co/collections/Skywork/skywork-unipic3)

#### Paper Authors

Hongyang Wei, Hongbo Liu, Zidong Wang, Yi Peng, Baixin Xu, Size Wu, Xuying Zhang, Xianglong He, Zexiang Liu, Peiyu Wang, Xuchen Song, Yangguang Li, Yang Liu, Yahui Zhou

#### Citation

```bibtex
@misc{wei2026skyworkunipic30unified,
      title={Skywork UniPic 3.0: Unified Multi-Image Composition via Sequence Modeling}, 
      author={Hongyang Wei and Hongbo Liu and Zidong Wang and Yi Peng and Baixin Xu and Size Wu and Xuying Zhang and Xianglong He and Zexiang Liu and Peiyu Wang and Xuchen Song and Yangguang Li and Yang Liu and Yahui Zhou},
      year={2026},
      eprint={2601.15664},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2601.15664}, 
}
```

### Base Pipeline

**Qwen-Image-Edit-2511** provides the VAE, text encoder, and scheduler:

- **Model**: [Qwen/Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)
- **Pipeline**: `QwenImageEditPlusPipeline` from Hugging Face Diffusers
- **Text Encoder**: Qwen2.5-VL-7B-Instruct (vision-language model enabling numbered image references)

### Diffusers Library

Pipeline implementation leverages [Hugging Face Diffusers](https://github.com/huggingface/diffusers) (≥0.35.0).

### Related UniPic Versions

- **UniPic 1.0**: Unified autoregressive model (1.5B params) - includes T2I ([arXiv:2508.03320](https://arxiv.org/abs/2508.03320))
- **UniPic 2.0**: SD3.5M-Kontext and MetaQuery variants - includes T2I ([arXiv:2509.04548](https://arxiv.org/abs/2509.04548))
- **UniPic 3.0**: Multi-image composition focused (this implementation)

---

## Installation

### Requirements

- ComfyUI (recent version)
- Python 3.10+
- PyTorch 2.0+
- CUDA-capable GPU with 64GB+ VRAM
- ~100GB disk space for models

### Steps

1. **Clone to custom_nodes:**
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/EricRollei/Eric_UniPic3.git
   ```

   Or install via ComfyUI Manager / Registry:
   ```bash
   comfy node install comfyui-eric-unipic3
   ```

2. **Install dependencies:**
   ```bash
   pip install -r Eric_UniPic3/requirements.txt
   ```

3. **Download UniPic3 transformers** (if not already):
   ```bash
   # Teacher model
   huggingface-cli download Skywork/Unipic3 --local-dir H:/Testing/Unipic3
   
   # DMD model (optional, for fast inference)
   huggingface-cli download Skywork/Unipic3-DMD --local-dir H:/Testing/Unipic3-DMD
   
   # Consistency model (optional)
   huggingface-cli download Skywork/Unipic3-Consistency-Model --local-dir H:/Testing/Unipic3-Consistency-Model
   ```

4. **Download base pipeline** (if not already):
   ```bash
   huggingface-cli download Qwen/Qwen-Image-Edit-2511 --local-dir H:/Training/Qwen-Image-Edit-2511
   ```

5. **Restart ComfyUI**

### Verifying Installation

After restart, you should see these nodes in the "Eric UniPic3" category:

- Eric UniPic3 Load Model
- Eric UniPic3 Image Edit
- Eric UniPic3 Compose (HOI)
- Eric UniPic3 Unload Model

---

## Support

For issues, questions, or contributions:

- **GitHub Issues**: [Report bugs or request features]
- **Author Contact**: eric@rollei.us

---

*Last updated: January 2026*
