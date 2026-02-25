# Kraken Tools for ComfyUI

A collection of productivity custom nodes for ComfyUI, designed to streamline image generation workflows with smart defaults, advanced features, and quality-of-life improvements.

## Installation

### Via ComfyUI Manager (Recommended)
Search for "Kraken Tools" in ComfyUI Manager and click Install.

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/kraken_tools.git
cd kraken_tools
pip install -r requirements.txt
```

### Requirements
- ComfyUI
- Python 3.10+
- PyTorch 2.0+
- transformers >= 4.45.0 (for Kraken Unbound Prompt)
- Pillow
- requests (for CivitAI trigger word fetching)
- opencv-python (for image processing)
- scipy (for image processing)
- ollama (optional, for Kraken Ollama Prompt Chat)

---

## Nodes Overview (15 Nodes)

### Prompt & Text Nodes

#### 🐙 Kraken Unbound Prompt
Advanced prompt builder with built-in vision model support for image-to-text captioning.

**Features:**
- **Vision Mode**: Use Qwen2-VL-2B-Instruct to generate prompts from images
- **Prompt Enhancement**: Automatically enhance prompts using AI
- **Style Presets**: Choose from photorealistic, cinematic, anime, manga, fantasy, sci-fi, and more
- **Lighting Options**: Soft, dramatic, cinematic, studio, natural, golden hour, neon, rim, backlighting
- **Camera Settings**: Lens type, f-stop, bokeh effect, DSLR style
- **Persistent Prompt**: Add text that always appears (e.g., "blue skies", "brand logo")
- **Negative Prompt**: Separate negative prompt output
- **Position Control**: Prepend or append style settings to your prompt
- **VRAM Management**: Control model loading/unloading with keep_alive_minutes

**Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| prompt | STRING | Your base prompt text |
| use_image_as_source | BOOLEAN | Use vision model to caption an image |
| input_image | IMAGE | Image for vision mode |
| enhance_prompt | BOOLEAN | Use AI to enhance the prompt |
| enhancer_style | DROPDOWN | Modern, Classic Tags, Instructional, or WAN style |
| negative_prompt | STRING | Negative prompt text |
| persistent | STRING | Text always added to the prompt |
| style/lighting/camera_lens/f_stop | DROPDOWNS | Style settings |
| position | DROPDOWN | Prepend or append style settings |
| force_unload | BOOLEAN | Unload model after use to free VRAM |

**Outputs:**
- `positive_prompt` (STRING): The final positive prompt
- `negative_prompt` (STRING): The negative prompt
- `persistent` (STRING): The persistent prompt (passthrough)

---

#### 🐙 Kraken WAN Prompt Splitter
Split and style prompts for WAN video generation with comprehensive cinematic presets.

**Features:**
- **Prompt Splitting**: Split a single prompt into up to 5 segments using delimiters (---, ###, etc.)
- **WAN Packs**: Pre-configured style packs (Cinematic Natural, Moody Neon, Documentary Daylight, Epic Vista, Noir Classic)
- **Shot Type**: extreme close-up, close-up, medium shot, cowboy shot, wide shot, aerial, POV, etc.
- **Lens Selection**: 24mm to 200mm, anamorphic, tilt-shift, fisheye, macro
- **Aperture**: f/1.4 dreamy bokeh to f/16 deep focus
- **Lighting**: natural daylight, golden hour, neon mix, studio 3-point, film noir, candlelight, etc.
- **Film Stocks**: photoreal, portra-like, cinestill-like, black-and-white, vintage chrome, etc.
- **Color Grading**: warm amber teal, cool cyan steel, muted pastels, high contrast, etc.
- **Composition**: rule of thirds, centered symmetry, leading lines, dutch angle, etc.
- **Environment**: clear, fog, rain, snowfall, dust storm, haze
- **Texture**: ultra-detailed, fine film grain, clean minimal, gritty texture

**Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| prompt | STRING | Main prompt (use --- to split) |
| persistent | STRING | Text added to all prompts |
| wan_pack | DROPDOWN | Pre-configured style pack |
| shot_type/lens/aperture/etc. | DROPDOWNS | Individual style controls |
| combine_persistent | BOOLEAN | Add persistent text to prompts |
| combine_style_presets | BOOLEAN | Add style settings to prompts |

**Outputs:**
- `Prompt 1` through `Prompt 5` (STRING): Split and styled prompts

---

#### 🐙 Kraken Ollama Prompt Chat
Connect to a local Ollama LLM instance for interactive prompt enhancement.

**Features:**
- Connect to any Ollama server
- Use any Ollama model (llama3.2, mistral, etc.)
- Interactive chat for refining prompts
- Specialized system prompt for AI art generation

**Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| host | STRING | Ollama server URL (e.g., http://localhost:11434) |
| model | STRING | Model name (e.g., llama3.2) |
| action | DROPDOWN | Connect, Send Message, Clear Chat, Use Last Response |
| user_message | STRING | Your message to the LLM |

**Outputs:**
- `prompt_output` (STRING): The generated prompt
- `ai_response` (STRING): Full AI response
- `conversation_log` (STRING): Chat history

---

### Model Loading Nodes

#### 🐙 Kraken Checkpoint Loader
Enhanced checkpoint loader with model tracking.

**Features:**
- Load checkpoints with optional dtype control (fp16, bf16, fp32)
- Output model name for metadata tracking
- Compute SHA-256 hash (first 10 chars) for version tracking

**Outputs:**
- `MODEL`, `CLIP`, `VAE`: Standard model outputs
- `model_name` (STRING): Filename of loaded checkpoint
- `ckpt_sha10` (STRING): First 10 chars of SHA-256 hash

---

#### 🐙 Kraken Dual CLIP Loader
Full-featured dual text encoder loader for modern models.

**Features:**
- Support for Flux, SDXL, SD3, and Hunyuan models
- Load CLIP-L + T5 text encoders
- Modes: dual, t5-only, clip-only
- Device placement control (auto, cuda, cpu)
- Precision override (fp16, bf16, fp32)
- Optional warmup for faster first inference

**Outputs:**
- `clip` (CLIP): Combined CLIP object
- `diagnostics` (STRING): Loading information

---

#### 🐙 Kraken LoRA Loader (3)
Load up to 3 LoRAs with automatic trigger word fetching.

**Features:**
- Load 3 LoRAs simultaneously with individual enable toggles
- Per-LoRA strength control for both model and CLIP
- Per-LoRA CLIP skip setting
- **CivitAI Integration**: Automatically fetch trigger words from CivitAI
- API key stored securely in `~/Documents/ComfyUI/user/kraken_config.json`
- Trigger word placement: prepend, append, or replace
- Caches trigger words locally for offline use

**Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| model/clip | MODEL/CLIP | Input model and clip |
| lora_X_enabled | BOOLEAN | Enable/disable each LoRA |
| lora_X_file | DROPDOWN | LoRA file selection |
| lora_X_model_strength | FLOAT | Model weight (-2.0 to 2.0) |
| lora_X_clip_strength | FLOAT | CLIP weight (-2.0 to 2.0) |
| lora_X_clip_skip | INT | CLIP skip (0 = off) |
| lora_X_force_fetch | BOOLEAN | Re-fetch trigger words |
| fetch_triggers | BOOLEAN | Enable CivitAI fetching |
| placement | DROPDOWN | prepend, append, or replace |

**Outputs:**
- `model` (MODEL), `clip` (CLIP): Modified model/clip
- `prompt` (STRING): Prompt with trigger words
- `lora_names`, `triggers`, `tags` (STRING_LIST): Metadata

---

### Latent & Resolution Nodes

#### 🐙 Kraken Empty Latent Image
Create empty latent images with preset aspect ratios.

**Features:**
- Megapixel selection: 0.5 to 3.0 MP or Custom
- Preset aspect ratios organized by category:
  - Vertical/Portrait (9:20, 9:16, 2:3, 3:4, 4:5)
  - Square (1:1)
  - Landscape (5:4, 4:3, 3:2, 16:10, 16:9)
  - Cinematic (1.85:1, 2:1, 21:9, 2.39:1)
  - Screen sizes (Android, iPhone, Full HD, 4K)
  - Social media sizes (Instagram, YouTube, Facebook)
- Custom aspect ratio input
- Divisible-by alignment (8, 16, 32, 64)

**Outputs:**
- `latent` (LATENT): Empty latent for generation
- `width_out`, `height_out` (INT): Dimensions
- `resolution` (STRING): "1024 x 1024" format
- `preset_out` (STRING): For connecting to upscale calculator

---

#### 🐙 Kraken Resolution Helper
Ensures final output matches a specific target resolution. Batch-safe for video.

**Features:**
- Multiple modes: fill/crop, pad, keep proportion, stretch
- Interpolation: lanczos, bicubic, bilinear, nearest
- Anchor positioning for crop/pad (left/center/right, top/center/bottom)
- Upscale prevention option
- Works with batched images (video frames)

**Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| image | IMAGE | Input image batch |
| mode | DROPDOWN | Resize mode |
| target_resolution_in | STRING | Target as "WxH" |
| preset_in | STRING | From Kraken Empty Latent |

---

#### 🐙 Kraken Upscale & Tile Calc
Calculate parameters for Ultimate SD Upscale.

**Features:**
- Connects to Kraken Empty Latent Image via resolution_in and preset_in
- Calculates optimal upscale factor to reach target
- Computes tile width/height for USDU
- Handles seam fix parameters
- Minimum upscale policy (auto, off, 1.5x, 2.0x, custom)
- Generates preview showing predicted vs target resolution

**Outputs:**
- `image_out` (IMAGE): Passthrough
- `upscale_by` (FLOAT): Scale factor for USDU
- `tile_width`, `tile_height` (INT): Tile dimensions
- `mask_blur`, `tile_padding` (INT): USDU parameters
- `seam_fix_width`, `seam_fix_mask_blur`, `seam_fix_padding` (INT)
- `predicted_resolution`, `target_resolution`, `target_preset` (STRING)

---

#### 🐙 Kraken Preset From Image
Extract dimensions from an image for upscaling calculations.

**Features:**
- Multiple sizing modes:
  - Factor: Multiply by scale factor (e.g., 2x)
  - Long side: Target longest edge
  - Short side: Target shortest edge
  - Megapixels: Target total megapixels
- Alignment to model-friendly multiples
- Optional max width/height clamping

**Outputs:**
- `preset_out` (STRING): Resolution as "WxH" (e.g., "2048x1536")

---

### Sampling Nodes

#### 🐙 Kraken KSampler
Smart KSampler wrapper with AMP handling for modern models.

**Why this exists:**
WAN/Flow/FP8 models manage their own precision internally. Wrapping them in an additional autocast context causes crashes like "RuntimeError: Unexpected floating ScalarType in at::autocast::prioritize". This node automatically detects such models and disables outer AMP.

**Features:**
- **AMP Mode** (auto/on/off): Auto-detect WAN/Flow/FP8 models
- All standard KSampler controls
- Negative prompt handling (auto/use/ignore)
- Built-in decode option (standard or tiled)
- Compatible with ComfyUI 0.3.x+ and PyTorch 2.x

**Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| model | MODEL | Diffusion model |
| positive/negative | CONDITIONING | Prompts |
| amp_mode | DROPDOWN | auto, on, or off |
| decode_switch | DROPDOWN | on/off for VAE decode |
| tiled_decode | DROPDOWN | on/off for large images |
| tile_size | INT | Tile size for tiled decode |

**Outputs:**
- `LATENT`: Sampled latent
- `IMAGE`: Decoded image (or placeholder if decode off)

---

### Image Processing Nodes

#### 🐙 Kraken Image Resize
Comprehensive image resizing with multiple methods.

**Features:**
- Source: Upload or upstream connection
- Resize modes: longest_side, width, height, fit, fill, stretch
- Interpolation: lanczos, bicubic, bilinear, nearest, area
- Option to prevent upscaling smaller images
- Background color for fill mode

**Outputs:**
- `image` (IMAGE): Resized image
- `width`, `height` (INT): Final dimensions
- `info` (STRING): Processing summary

---

#### 🐙 Kraken Image Processor
Versatile pre/post-processing for upscaling pipelines.

**Features:**
- **Denoising**: Bilateral, Gaussian, median, non-local means, GPU-accelerated Gaussian
- **Contrast Enhancement**: Auto-contrast, manual contrast/brightness
- **Sharpening**: Unsharp mask, edge enhance, custom kernel
- **Color Correction**: Saturation, gamma
- **Film Grain**: Adjustable amount and size (post-processing only)
- Alpha channel preservation
- Quality metrics output
- 16-bit processing precision option

**Modes:**
- `pre_process`: Prepare image for upscaling
- `post_process`: Refine upscaled image (gentler settings auto-applied)

---

### Video / WAN Nodes

#### 🐙 Kraken WAN Helper
Quick parameter selection for WAN video generation.

**Features:**
- Performance tiers: 720p Quality or 480p Speed
- Duration slider: 1-10 seconds
- FPS options: 8, 12, 16, 24, 30
- Automatic aspect ratio detection from first frame
- First/last frame preprocessing
- Bookend frame option for looping

**Outputs:**
- `processed_first_frame`, `processed_last_frame` (IMAGE)
- `width`, `height` (INT)
- `frames(length)` (INT): Total frame count
- `fps` (FLOAT)
- `resolution_text` (STRING)

---

#### 🐙 Kraken Last Frame + Meta
Extract last frame from video for creating extended sequences.

**Use case:** Generate 5-second video clips, then use the last frame of each as the first frame of the next to create seamless longer videos.

**Features:**
- Extracts last frame from image batch
- Forwards all WAN metadata (width, height, frames, fps)
- Optional frame duplication

**Outputs:**
- `last_frame` (IMAGE): The last frame
- `first_frame_out` (IMAGE): Same as last_frame (for chaining)
- `width`, `height`, `frames(length)`, `fps`, `resolution_text`: Metadata passthrough

---

## Typical Workflow Examples

### Basic Image Generation with LoRAs
```
Kraken Checkpoint Loader --> Kraken LoRA Loader (3) --> Kraken KSampler
                                      ^
Kraken Unbound Prompt --> CLIP Text Encode --+
```

### Upscaling with Ultimate SD Upscale
```
Kraken Empty Latent Image
      |
      +--> resolution_out --> Kraken Upscale & Tile Calc --> Ultimate SD Upscale
      |                              |
      +--> preset_out ---------------+

After USDU:
Ultimate SD Upscale --> Kraken Resolution Helper --> Kraken Image Processor --> Save Image
```

### WAN Video Generation
```
Kraken WAN Prompt Splitter --> WAN Text Encode
                                     |
Kraken WAN Helper -----------------> WAN Generation --> Kraken Last Frame + Meta
                                                              |
                                          (Loop back to WAN Generation as first_frame)
```

---

## Configuration

### CivitAI API Key (for LoRA trigger words)
Create or edit `~/Documents/ComfyUI/user/kraken_config.json`:
```json
{
    "civitai_api_key": "your_api_key_here"
}
```
The key is optional - public model data can be fetched without it.

### Ollama Setup (for Prompt Chat)
1. Install Ollama: https://ollama.ai
2. Pull a model: `ollama pull llama3.2`
3. Configure host in the node (default: `http://localhost:11434`)

---

## Node List Summary

| Node | Category | Description |
|------|----------|-------------|
| 🐙 Kraken Unbound Prompt | Prompt | Vision-enabled prompt builder with styles |
| 🐙 Kraken WAN Prompt Splitter | Prompt | Split & style prompts for WAN video |
| 🐙 Kraken Ollama Prompt Chat | Prompt | LLM-powered prompt enhancement |
| 🐙 Kraken Checkpoint Loader | Loaders | Checkpoint loader with SHA tracking |
| 🐙 Kraken Dual CLIP Loader | Loaders | Dual text encoder for Flux/SD3 |
| 🐙 Kraken LoRA Loader (3) | Loaders | 3-slot LoRA with CivitAI integration |
| 🐙 Kraken Empty Latent Image | Latent | Latent with aspect ratio presets |
| 🐙 Kraken Resolution Helper | Resolution | Enforce target resolution |
| 🐙 Kraken Upscale & Tile Calc | Resolution | Calculate USDU parameters |
| 🐙 Kraken Preset From Image | Resolution | Extract dimensions from image |
| 🐙 Kraken KSampler | Sampling | Smart sampler with AMP handling |
| 🐙 Kraken Image Resize | Image | Comprehensive image resizing |
| 🐙 Kraken Image Processor | Image | Pre/post-processing pipeline |
| 🐙 Kraken WAN Helper | Video | WAN video parameter helper |
| 🐙 Kraken Last Frame + Meta | Video | Extract last frame for looping |

---

## License

MIT License - See individual file headers for details.

---

## Credits

Created by The Kraken (@KrakenUnbound)

Built for the ComfyUI community.
