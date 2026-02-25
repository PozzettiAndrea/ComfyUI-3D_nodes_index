# Emu3.5 ComfyUI Nodes

**ComfyUI integration for BAAI's Emu3.5 multimodal models**

✅ **STATUS: ALL NODES FULLY WORKING** - Verified December 19, 2025

![Complete Workflow](assets/Emu35_complete_workflow.png)

## Overview

This repository provides ComfyUI custom nodes for running BAAI's Emu3.5 models for:
- **Text-to-Image (T2I)** - Generate images from text descriptions ✅
- **Image Editing (X2I)** - Transform/edit existing images ✅ 
- **Interleaved Generation (Story Mode)** - Create illustrated stories with text and images ✅
- **Visual Q&A** - Answer questions about images, OCR, image comparison ✅

### Workflow Screenshots

| T2I / Basic Workflow | X2I (Image Edit) | Story Mode |
|:---:|:---:|:---:|
| ![T2I](assets/Basic_workflow_screenshot.png) | ![X2I](assets/Emu35-X2I-workflow-screenshot.png) | ![Story](assets/Emu35_base_story_screenshot.png) |

**Models Supported:**
- Emu3.5-Image (34B params - T2I/X2I) - ✅ Working
- Emu3.5-Base (65B params - Story/Interleaved/VQA) - ✅ Working
- Vision Tokenizer (VQ-VAE for image encoding/decoding) - ✅ Working

## What's New (December 2025)

### V2 Nodes Released! 🎉
- **Emu 3.5 Loader V2** - Improved model loading with memory management
- **Emu 3.5 T2I Sampler V2** - Text-to-image with tiled decoding for large images
- **Emu 3.5 X2I (Image Edit)** - Transform/edit images with text prompts
- **Emu 3.5 Interleaved** - Generate stories/tutorials with multiple images
- **Emu 3.5 VQA** - Visual question answering
- **Emu 3.5 Memory Manager** - VRAM management utilities

## Credits & Attribution

This project is built upon:

- **[BAAI Emu3.5](https://github.com/baaivision/Emu3.5)** - Original model and codebase
  - Paper: [Emu3.5: Native Multimodal Models are World Learners](https://arxiv.org/pdf/2510.26583)
  - Authors: Emu3.5 Team, Beijing Academy of Artificial Intelligence
  - License: Apache 2.0

**Development Contributors:**
- **Eric Rollei** - ComfyUI node development and integration
- **Claude Opus 4.5 (Anthropic)** - AI pair programming assistant for debugging, compatibility fixes, and feature implementation

**Technical Contributions:**
- Transformers 4.57+ compatibility patches (DynamicCache API changes)
- Blackwell GPU (sm_120) eager attention workaround
- VQA task presets and multi-image comparison support
- Memory management and VRAM optimization

All model weights and architecture remain property of BAAI under Apache 2.0 license.

## Installation

### Prerequisites
- ComfyUI installed
- Python 3.10+
- CUDA-capable GPU:
  - **Full BF16**: 48GB+ VRAM (RTX A6000, RTX 6000 Ada/Blackwell)
  - **NF4 Quantized**: 24GB+ VRAM (RTX 4090, RTX A5000)
- 100GB+ disk space for model weights

### Method 1: Git Clone (Recommended)

```bash
cd ComfyUI/custom_nodes
git clone --recursive https://github.com/EricRollei/Emu35-Comfyui-Nodes.git emu35
cd emu35

# Install dependencies
pip install -r requirements.txt
```

> **Note:** The `--recursive` flag automatically clones the patched Emu3.5 submodule with transformers 4.57+ compatibility fixes.

### Method 2: Manual Download

1. Download this repository
2. Extract to `ComfyUI/custom_nodes/emu35/`
3. Download [Emu3.5 repo](https://github.com/baaivision/Emu3.5) and place in `emu35/Emu3_5_repo/`
4. Install requirements: `pip install -r requirements.txt`

### Download Model Weights

Place models in `ComfyUI/models/emu35/`:

**Option A: Full BF16 (48GB+ VRAM - Best Quality)**
```bash
huggingface-cli download BAAI/Emu3.5-Image --local-dir models/emu35/Emu3.5-Image
huggingface-cli download BAAI/Emu3.5-VisionTokenizer --local-dir models/emu35/vision_tokenizer
```

**Option B: NF4 Quantized (24GB+ VRAM)**
```bash
huggingface-cli download wikeeyang/Emu35-Image-NF4 --local-dir models/emu35/Emu3.5-Image-NF4
huggingface-cli download BAAI/Emu3.5-VisionTokenizer --local-dir models/emu35/vision_tokenizer
```

**Directory structure:**
```
ComfyUI/
├── custom_nodes/
│   └── emu35/
│       ├── nodes.py
│       ├── nodes_v2.py        # New V2 nodes
│       ├── __init__.py
│       ├── patched_tokenization_emu3.py
│       └── Emu3_5_repo/       # Official repo
└── models/
    └── emu35/
        ├── Emu3.5-Image/      # (or Emu3.5-Image-NF4/)
        └── vision_tokenizer/
```

## Nodes Reference

### V2 Nodes (Recommended)

#### 1. Emu 3.5 Loader V2
Loads the Emu3.5 model with improved memory management.

| Input | Type | Description |
|-------|------|-------------|
| `model_name` | dropdown | Model folder (e.g., "Emu3.5-Image") |
| `vq_model_name` | dropdown | Vision tokenizer folder |
| `precision` | dropdown | bf16, fp16, fp32, or nf4 |
| `device` | dropdown | cuda:0, cuda:1, cpu |
| `vq_device` | dropdown | Device for VQ model |
| `attention_implementation` | dropdown | eager (recommended), sdpa |

| Output | Type | Description |
|--------|------|-------------|
| `EMU35_MODEL` | model | Loaded language model |
| `EMU35_TOKENIZER` | tokenizer | Text tokenizer |
| `EMU35_VQ` | model | Vision tokenizer |

---

#### 2. Emu 3.5 T2I Sampler V2
Text-to-image generation with improved quality and tiled decoding.

| Input | Type | Description |
|-------|------|-------------|
| `model/tokenizer/vq_model` | - | From loader |
| `prompt` | string | Text description |
| `aspect_ratio` | dropdown | 1:1, 4:3, 3:4, 16:9, 9:16, etc. |
| `cfg_scale` | float | Guidance scale (default: 5.0) |
| `seed` | int | Random seed |
| `image_top_k` | int | Sampling top-k (default: 5120) |
| `image_temperature` | float | Sampling temperature (default: 1.0) |
| `tiled_decode` | bool | Use tiled VQ decoding (faster for large images) |
| `tile_size` | int | Tile size for decoding (default: 32) |

| Output | Type | Description |
|--------|------|-------------|
| `IMAGE` | image | Generated image |
| `TEXT_RESPONSE` | string | Any text response |
| `REASONING` | string | Chain-of-thought reasoning (if any) |

---

#### 3. Emu 3.5 X2I (Image Edit) ⭐ NEW
Transform or edit existing images based on text instructions.

| Input | Type | Description |
|-------|------|-------------|
| `model/tokenizer/vq_model` | - | From loader |
| `prompt` | string | Edit instruction (e.g., "Make the background a sunset") |
| `reference_image_1` | image | Primary reference image |
| `image_area` | dropdown | Token resolution: 256x256 to 1024x1024 |
| `cfg_scale` | float | Guidance (default: 2.0 for X2I) |
| `seed` | int | Random seed |
| `reference_image_2` | image | Optional second reference |
| `reference_image_3` | image | Optional third reference |
| `tiled_decode` | bool | Use tiled VQ decoding |

**Example Prompts for X2I:**
- "Transform this image into a realistic photo"
- "Change the background to a beach sunset"
- "Add sunglasses to the person"
- "Replace the dog with a cat"
- With 2+ images: "Replace the [object] in first image with [object] from second image"

| Output | Type | Description |
|--------|------|-------------|
| `IMAGE` | image | Edited image |
| `TEXT_RESPONSE` | string | Any text response |
| `REASONING` | string | Chain-of-thought reasoning |

---

#### 4. Emu 3.5 Interleaved (Story/HowTo)
Generate text with multiple embedded images (stories, tutorials).

| Input | Type | Description |
|-------|------|-------------|
| `model/tokenizer/vq_model` | - | From loader |
| `prompt` | string | Topic/story to generate |
| `task_type` | dropdown | story, howto, explore |
| `max_images` | int | Number of images to generate (1-10) |
| `cfg_scale` | float | Guidance scale |
| `seed` | int | Random seed |
| `reference_image` | image | Optional reference for context |

| Output | Type | Description |
|--------|------|-------------|
| `IMAGES` | image batch | Generated images |
| `TEXT_RESPONSE` | string | Full text with [IMAGE_N] markers |
| `REASONING` | string | Reasoning if present |

---

#### 5. Emu 3.5 VQA (Visual Question Answering)
Analyze images, answer questions, describe content, and read text (OCR).

**⚠️ Important:** Use the **emu35-base** model for VQA tasks, not emu35-image!

| Input | Type | Description |
|-------|------|-------------|
| `model/tokenizer/vq_model` | - | From loader (use emu35-base) |
| `image` | image | Image to analyze |
| `question` | string | Question about the image |
| `max_tokens` | int | Max response length (default: 512) |
| `task_type` | dropdown | Preset task types (see below) |
| `temperature` | float | Response creativity (0.1-0.3 for accuracy, 0.5-0.7 for creativity) |
| `image2` | image | Optional second image for comparison tasks |

| Output | Type | Description |
|--------|------|-------------|
| `response` | string | Model's answer |

**Task Types:**

| Task Type | Description | Best For |
|-----------|-------------|----------|
| `caption` | One-sentence summary | Quick descriptions |
| `describe` | Detailed description of subjects, background, colors, composition | Comprehensive analysis |
| `analyze` | Context, mood, artistic style analysis | Art/photo critique |
| `ocr` | Read and transcribe text from images | Screenshots, signs, documents |
| `question` | Free-form Q&A | Specific questions |
| `custom` | Use your own question directly | Any task |

**Example Questions for VQA:**

*Basic Understanding:*
- "Describe this image in detail."
- "What is the main subject of this image?"
- "What colors are dominant in this image?"

*Object Identification:*
- "What objects are visible in this image?"
- "Is there a person in this image? What are they doing?"
- "What type of animal is in the photo?"

*Counting & Spatial:*
- "How many people are in this image?"
- "What is to the left of the car?"
- "Where is the sun in this scene?"

*OCR (Text Reading):*
- "What text appears in this image?"
- "Read the sign in the background."
- "What does the label say?"

*Analysis & Style:*
- "What artistic style is this image?"
- "What time of day is shown?"
- "What emotion does this scene convey?"
- "Is this image indoor or outdoor?"

*Comparison (with 2 images):*
- "What's different between these two images?"
- "Which image shows more people?"
- "Compare the lighting in both photos."

**Tips for Best Results:**

1. **Use emu35-base model** - The Image model is optimized for generation, not understanding
2. **Lower temperature (0.1-0.3)** for factual answers like counting, OCR, or identification
3. **Higher temperature (0.5-0.7)** for creative descriptions or artistic analysis
4. **Be specific** - "What brand is the laptop?" works better than "What's in the image?"
5. **For OCR**, use task_type="ocr" which has an optimized prompt
6. **For comparisons**, connect both images (image + image2)

---

#### 6. Emu 3.5 Memory Manager
Utilities for VRAM management.

| Input | Type | Description |
|-------|------|-------------|
| `action` | dropdown | clear_cache, report_memory, gc_collect |
| `any_input` | any | Pass-through connection |

| Output | Type | Description |
|--------|------|-------------|
| `any_output` | any | Pass-through |
| `memory_info` | string | Memory status report |

---

### Legacy Nodes (V1)

The original nodes are still available for compatibility:
- `Emu35Loader` - Original loader
- `Emu35Sampler` - Original T2I sampler
- `Emu35VQA` - Original VQA node
- `Emu35ClearCache` - Cache clearing

## Performance

### Tested Configurations

| Configuration | GPU | VRAM Used | Speed |
|---------------|-----|-----------|-------|
| Full BF16 + T2I | RTX 6000 Blackwell 96GB | ~65GB | ~5-6 tok/s |
| Full BF16 + X2I (1 image) | RTX 6000 Blackwell 96GB | ~82GB | ~5.4 tok/s |
| NF4 + X2I (2 images @ 1024) | RTX 6000 Blackwell 96GB | ~50GB | ~4-5 tok/s |
| NF4 + T2I | RTX 4090 24GB | ~22GB | ~3-4 tok/s |

### Generation Times

| Task | Resolution | Tokens | Time |
|------|------------|--------|------|
| T2I 1:1 | 1024x1024 | ~4096 | ~12 min |
| T2I 4:3 | 1168x880 | ~4000 | ~11 min |
| X2I | Same as input | ~4000 | ~13 min |

## Technical Details

### Architecture
- **Model Size**: 34B parameters
- **Training**: 10T+ multimodal tokens
- **Image Tokenization**: VQ-VAE (IBQ) with 262,144 codebook
- **Visual Tokens**: Token IDs 151855-413998
- **Max Resolution**: 2048x2048 (128x128 latents)

### Special Token IDs
```python
BOS = 151849  # <|extra_203|> Begin generation
EOS = 151850  # <|extra_204|> End generation  
IMG = 151851  # <|image token|>
BOI = 151852  # <|image start|>
EOI = 151853  # <|image end|>
EOL = 151846  # <|extra_200|> End of line
VISUAL_START = 151854  # First visual token
```

### Task Templates

**T2I (Text-to-Image):**
```
<|extra_203|>You are a helpful assistant for t2i task. USER: {prompt} ASSISTANT: <|extra_100|>
```

**X2I (Image Edit):**
```
<|extra_203|>You are a helpful assistant for x2i task. USER: <|IMAGE|>{prompt} ASSISTANT: <|extra_100|>
```

## Known Issues & Solutions

### 1. SDPA Attention on Blackwell GPUs
**Issue**: SDPA attention produces noise/garbage on Blackwell (sm_120) with CUDA 12.8.
**Solution**: Use `attention_implementation="eager"` (default in V2 loader).

### 2. Tokenizer Crashes
**Issue**: Missing visual tokens in tokenizer.
**Solution**: Patched tokenizer auto-synthesizes missing tokens.

### 3. Out of Memory
**Solutions**:
- Use NF4 quantization (24GB VRAM)
- Reduce `image_area` in X2I node
- Use smaller aspect ratios
- Enable tiled decoding

### 4. X2I Generates Only 1 Token
**Issue**: Stopping criteria triggered by reference image tokens.
**Solution**: Fixed in V2 - stopping criteria now ignores input tokens.

### GPU Compatibility

| GPU Architecture | SDPA | Eager | Recommended |
|-----------------|------|-------|-------------|
| Ampere (sm_80) | ✅ | ✅ | SDPA |
| Ada Lovelace (sm_89) | ✅ | ✅ | SDPA |
| Blackwell (sm_120) | ❌ | ✅ | **Eager** |

## Example Workflows

### Basic T2I
```
[Emu 3.5 Loader V2] → [Emu 3.5 T2I Sampler V2] → [Preview Image]
                              ↑
                    prompt: "a red apple on a wooden table, 
                             studio lighting, photorealistic"
```

### Image Editing (X2I)
```
[Load Image] → [Emu 3.5 X2I] → [Preview Image]
                    ↑
[Emu 3.5 Loader V2] 
                    ↑
          prompt: "Transform into an oil painting"
```

### Multi-Image Edit
```
[Load Image 1] → 
                  [Emu 3.5 X2I] → [Preview Image]
[Load Image 2] →        ↑
                        prompt: "Replace the background 
                                 from image 1 with the 
                                 scene from image 2"
```

## Development

### File Structure
```
emu35/
├── nodes.py           # V1 nodes (legacy)
├── nodes_v2.py        # V2 nodes (recommended)
├── __init__.py        # ComfyUI registration
├── patched_tokenization_emu3.py  # Fixed tokenizer
├── download_nf4.py    # NF4 download helper
├── Emu3_5_repo/       # Official Emu3.5 code
└── dev/               # Development/test scripts
```

### Testing
```bash
cd ComfyUI/custom_nodes/emu35/dev

# Test tokenizer
python test_tokenizer.py

# Test minimal generation
python test_minimal.py
```

## Contributing

Contributions welcome! Priority areas:
- vLLM integration for faster generation
- Additional sampling strategies
- Workflow examples
- Documentation improvements

## License

- **This integration code**: MIT License
- **Emu3.5 models and code**: Apache 2.0 (BAAI)

## Citation

```bibtex
@article{emu3.5,
  title={Emu3.5: Native Multimodal Models are World Learners},
  author={Emu3.5 Team},
  journal={arXiv preprint arXiv:2510.26583},
  year={2024}
}
```

## Links

- **Emu3.5 Project**: https://emu.world/
- **Paper**: https://arxiv.org/pdf/2510.26583
- **Official Code**: https://github.com/baaivision/Emu3.5
- **Model Weights**: https://huggingface.co/BAAI/Emu3.5-Image
- **NF4 Quantized**: https://huggingface.co/wikeeyang/Emu35-Image-NF4
- **ComfyUI**: https://github.com/comfyanonymous/ComfyUI
