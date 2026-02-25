# LoRA Tag Power Loader for ComfyUI

A powerful ComfyUI custom node that combines text-based LoRA tag detection with advanced dual noise weight support, perfect for WanVideo/Hunyuan Video workflows.

## Features

- **Text-Based LoRA Loading** - Embed LoRA tags directly in your prompts (like A1111/ImpactWildcardEncode)
- **Dual Noise Weighting** - Different LoRA strengths for high noise vs low noise passes (perfect for WanVideo 2.2)
- **Unlimited LoRAs** - Load as many LoRAs as you need from a single text input
- **Optional Inputs** - Model and CLIP are optional (like Power Lora Loader)
- **Standard ComfyUI Weighting** - Uses the same method as Power Lora Loader
- **Video Model Support** - Built-in WanVideo/Hunyuan LoRA key standardization
- **Smart Matching** - Flexible LoRA file name matching
- **Performance** - LoRA caching for faster processing
- **Clean Output** - Returns text with tags removed for use in subsequent nodes
- **Helpful Tooltips** - All parameters have explanatory tooltips

## Installation

1. Clone or download this repository into your `ComfyUI/custom_nodes/` directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/comfyui-Lora-Tag-Power-Loader.git
```

2. Restart ComfyUI

3. The node will appear under `loaders > LoRA Tag Power Loader`

## Tag Format

The node supports a clean, intuitive tag format with progressive complexity:

### Basic Format
```
<lora:name:weight>
```
Single weight applies to model, clip, and both noise levels.

**Example:**
```
<lora:style_lora:0.8>
```

### Dual Noise Format (Primary Use Case)
```
<lora:name:high_noise:low_noise>
```
Different weights for high and low noise passes. Clip strength follows high noise value.

**Examples:**
```
<lora:detail_enhancer:1.2:0.3>    # Strong at high noise, weak at low noise
<lora:style_transfer:0.6:0.9>     # Weak at high noise, strong at low noise
```

### Advanced Format (Clip Override)
```
<lora:name:high_noise:low_noise:clip>
```
Full control over all parameters.

**Example:**
```
<lora:character:1.0:0.8:0.6>      # High=1.0, Low=0.8, Clip=0.6
```

## Node Parameters

### Required Inputs

- **text** - Text containing LoRA tags (multiline supported). Tags will be parsed and removed from output.
- **noise_mode** - Which noise weights to use:
  - `high_noise` - Use high noise weights
  - `low_noise` - Use low noise weights
  - `auto` - Average of high and low weights

### Optional Inputs

- **model** (MODEL, optional) - The model to apply LoRAs to. Can be omitted if you only want to parse tags.
- **clip** (CLIP, optional) - The CLIP model to apply LoRAs to. Can be omitted for model-only LoRA loading.
- **default_weight** (Float, default: 1.0) - Default weight when not specified in tag. Uses standard ComfyUI weighting method (same as Power Lora Loader).
- **weight_multiplier** (Float, default: 1.0) - Global multiplier for ALL LoRA weights. Set to 2.0 to double all weights, 0.5 to halve them. Applied after individual tag weights.
- **video_model_mode** (Boolean, default: False) - Enable WanVideo/Hunyuan key standardization. Turn ON when using video models.
- **auto_trigger** (Boolean, default: False) - When enabled, extracts trigger words from LoRA metadata and inserts them at the position where the LoRA tag was. Prevents LoRA tags from appearing as text artifacts in images.

### Outputs

- **MODEL** - Model with LoRAs applied
- **CLIP** - CLIP with LoRAs applied
- **text** - Input text with LoRA tags removed (or replaced with trigger words if `auto_trigger` is ON)
- **lora_info** - Formatted list of loaded LoRAs with weights and trigger words
- **trigger_words** - Comma-separated list of all extracted trigger words from loaded LoRAs

## Usage Examples

### Example 1: Basic LoRA Loading
```
Input text:
A beautiful portrait <lora:photorealistic:0.8> with detailed lighting

Output text:
A beautiful portrait with detailed lighting

LoRA info:
✓ 1. photorealistic [AUTO] M:0.80 C:0.80
```

### Example 2: Dual Noise for Video Generation
```
Input text:
Epic fantasy landscape <lora:cinematic:1.2:0.4> with <lora:detail_plus:0.8:1.0>

Noise mode: high_noise

Output text:
Epic fantasy landscape with

LoRA info:
✓ 1. cinematic [HIGH] M:1.20 C:1.20
✓ 2. detail_plus [HIGH] M:0.80 C:0.80
```

### Example 3: WanVideo 2.2 Workflow

For WanVideo 2.2's dual LoRA loading pattern, you can use two instances of this node:

**High Noise Pass:**
```
Text: Beautiful portrait <lora:style:1.2:0.3> <lora:detail:0.9:0.5>
Noise Mode: high_noise
Video Model Mode: ON
```

**Low Noise Pass:**
```
Text: Beautiful portrait <lora:style:1.2:0.3> <lora:detail:0.9:0.5>
Noise Mode: low_noise
Video Model Mode: ON
```

### Example 4: Global Weight Multiplier
```
Input text:
Fantasy scene <lora:style:0.8> with <lora:lighting:0.6>

Weight Multiplier: 2.0  (doubles all weights)

LoRA info:
✓ 1. style [AUTO] M:1.60 C:1.60  (0.8 × 2.0)
✓ 2. lighting [AUTO] M:1.20 C:1.20  (0.6 × 2.0)
```

**Use cases for weight_multiplier:**
- Quickly test different overall LoRA strengths without editing tags
- Fine-tune all LoRAs together in final iterations
- Create variations with one parameter change
- Batch process with different intensity levels

### Example 5: Multiple LoRAs with Mixed Formats
```
Input text:
A warrior <lora:character_base:0.9> wearing armor <lora:medieval:1.0:0.6:0.7>
in a forest <lora:background:0.8> at sunset <lora:lighting:1.5:0.5>

LoRA info:
✓ 1. character_base [AUTO] M:0.90 C:0.90
✓ 2. medieval [AUTO] M:0.80 C:0.70 (H:1.00 L:0.60)
✓ 3. background [AUTO] M:0.80 C:0.80
✓ 4. lighting [AUTO] M:1.00 C:1.50 (H:1.50 L:0.50)
```

### Example 6: Auto-Trigger Word Extraction
```
Input text:
A portrait <lora:anime_style:0.8> in a garden <lora:watercolor:0.6>

Auto-trigger: ON

Output text (cleaned):
A portrait anime, detailed rendering in a garden soft brushstrokes, pastel

LoRA info:
✓ 1. anime_style [AUTO] M:0.80 C:1.00 | Triggers: "anime, detailed rendering"
✓ 2. watercolor [AUTO] M:0.60 C:1.00 | Triggers: "soft brushstrokes, pastel"

trigger_words output:
anime, detailed rendering, soft brushstrokes, pastel
```

**Use cases for auto_trigger:**
- Prevent LoRA tags from appearing as text artifacts in images
- Automatically add proper trigger words without manual lookup
- Works with LoRAs from Civitai, Kohya, AI Toolkit, SimpleTuner, and more

## Use Cases

### Image Generation
- Use single weight format for standard workflows: `<lora:style:0.8>`
- Works exactly like traditional LoRA loaders

### Video Generation (WanVideo/Hunyuan)
- Use dual noise format: `<lora:style:1.2:0.4>`
- Toggle `noise_mode` between high_noise and low_noise passes
- Enable `video_model_mode` for proper key standardization

### Workflow Flexibility
- Embed LoRAs directly in your prompt text
- No need for multiple LoRA loader nodes
- Easy to copy/paste prompts between workflows
- Clean text output for CLIP encoding

## Technical Details

### LoRA File Matching

The node uses flexible name matching:
1. Exact filename match
2. Stem match (filename without extension)
3. Prefix match
4. Case-insensitive match

This means `<lora:my_style>` will find:
- `my_style.safetensors`
- `my_style_v2.safetensors`
- `MY_STYLE.safetensors`

### Caching

LoRA files are cached in memory after first load for better performance when:
- Processing multiple prompts
- Reusing the same workflow
- Batch processing

### Duplicate Tag Handling

If the same LoRA appears multiple times in a prompt, only the **first occurrence** is applied:
- Prevents rendering issues from double-loading the same LoRA
- Case-insensitive matching (`<lora:Style:0.8>` and `<lora:style:0.6>` = same LoRA)
- Duplicates are logged as skipped: `⊘ Skipped duplicate 'name' (already loaded)`
- All tags (including duplicates) are still removed from the cleaned text output

### Video Model Support

When `video_model_mode` is enabled, the node attempts to import WanVideoWrapper's `standardize_lora_key_format` function to handle various LoRA formats:
- AIToolkit/LyCORIS format
- Diffusers format
- Fun LoRA format
- FineTrainer format

If WanVideoWrapper is not installed, it falls back to standard LoRA loading.

## Model Architecture Compatibility

This node is **fully compatible** with all major ComfyUI model architectures:

| Model Type | Compatible | Text Encoder(s) | Notes |
|-----------|-----------|----------------|-------|
| **Flux** (Black Forest Labs) | ✅ YES | CLIP-L + T5-XXL | Full support, standard key mapping |
| **SDXL** (Stable Diffusion XL) | ✅ YES | CLIP-L + CLIP-G | Dual CLIP encoders supported |
| **Wan/WanVideo** (Alibaba) | ✅ YES | UMT5-XXL | Enable `video_model_mode` for best results |
| **Qwen** (Qwen2-VL) | ✅ YES | Qwen25-7B-VLI | Vision-language model support |
| **HunyuanVideo** | ✅ YES | Llama + T5 | Enable `video_model_mode` |
| **Z-Image** | ✅ YES | Qwen 4B (single) | Standard .safetensors format, LoKR not supported |
| **SD 1.5/2.1** | ✅ YES | CLIP-L | Standard support |

**Why it works:** The node uses ComfyUI's universal `load_lora_for_models()` function, which automatically detects model architecture and maps LoRA keys correctly. This is the same method used by Power Lora Loader and all official ComfyUI loaders.

**Supported LoRA Formats:**
- Standard PyTorch state_dict (.safetensors, .pt)
- Diffusers format (transformer.* keys)
- LyCORIS/SimpleTuner format
- OneTrainer format
- AIToolkit format (for video models)
- DoRA (Decomposed LoRA)

## Z-Image Support

The LoRA Tag Power Loader has full compatibility with Z-Image LoRAs trained in standard .safetensors format.

### About Z-Image

Z-Image is Alibaba's 6-billion parameter text-to-image generation model released in November 2025:

- **Architecture**: Single-stream DiT (S3-DiT) - unified processing of text and image tokens
- **Text Encoder**: Qwen 4B (single encoder - simpler than SDXL's dual encoders)
- **VAE**: Flux VAE (same as Flux models)
- **Inference**: 8-step Turbo optimization for lightning-fast generation
- **LoRA Training**: Ostris AI Toolkit with de-distill adapter

### Usage Examples

**Basic Setup:**
```
Prompt: A beautiful portrait <lora:zimage_style:0.8> with dramatic lighting
Noise Mode: auto
Video Model Mode: OFF

Output:
✓ 1. zimage_style [AUTO] M:0.80 C:0.80
Text: "A beautiful portrait with dramatic lighting"
```

**Multiple LoRAs:**
```
Prompt: Epic fantasy landscape <lora:cinematic:0.9> with <lora:detail_enhancer:0.7>

Output:
✓ 1. cinematic [AUTO] M:0.90 C:0.90
✓ 2. detail_enhancer [AUTO] M:0.70 C:0.70
Text: "Epic fantasy landscape with"
```

**Using Dual Noise Format:**
```
Prompt: A warrior <lora:character:1.2:0.5> in medieval armor
Noise Mode: high_noise (for structure pass) or low_noise (for detail pass)

Output (high_noise mode):
✓ 1. character [HIGH] M:1.20 C:1.20

Output (low_noise mode):
✓ 1. character [LOW] M:0.50 C:1.20
```

### Important Notes

**LoRA Format Requirements:**
- ✅ **Standard .safetensors format**: Fully supported (trained with Ostris AI Toolkit)
- ❌ **LoKR format**: NOT supported (ComfyUI Issue #10973)
- Use standard LoRA training, not LoKR/Kronecker product variants

**Text Encoder:**
- Z-Image uses a single Qwen 4B encoder (simpler than SDXL's dual CLIP-L + CLIP-G)
- CLIP weight applies to this single encoder
- No special configuration needed

**Key Mapping:**
- No special configuration needed - ComfyUI automatically detects Z-Image architecture
- LoRA keys mapped correctly without intervention
- Use `video_model_mode: OFF` for standard image generation (only enable for WanVideo/Hunyuan)

### Recommended Tag Formats

**For Standard Z-Image Images:**
```
<lora:style_name:0.8>                    # Simple single weight
<lora:style_name:0.8:0.8:0.8>            # Full control (all same = simple)
```

**For 8-Step Workflow Experimentation:**
```
<lora:structure:1.2:0.4>                 # Strong early, weak late
<lora:details:0.3:1.1>                   # Weak early, strong late
```

**Multiple Stacked LoRAs:**
```
<lora:style:0.9> <lora:detail:0.7> <lora:lighting:0.6>
```

### Troubleshooting Z-Image LoRAs

**LoRA loads but has no visible effect:**
- Check if LoRA is LoKR format (not compatible) - retrain as standard LoRA
- Verify LoRA was trained for Z-Image model specifically
- Try increasing weight (start with 0.8-1.0)

**LoRA file not found:**
- Place LoRA in `ComfyUI/models/loras/` directory
- Use filename without extension in tag (e.g., `<lora:my_style:0.8>` finds `my_style.safetensors`)
- Check console for detailed error message

**For more detailed testing and troubleshooting**, see `TESTING_Z_IMAGE.md` in the repository.

## Troubleshooting

### LoRA Not Found
- Check that the LoRA file exists in your `ComfyUI/models/loras/` folder
- Try using the exact filename (without extension)
- Check the console for detailed error messages

### Video Model LoRAs Not Working
- Ensure `video_model_mode` is enabled
- Install ComfyUI-WanVideoWrapper if working with WanVideo/Hunyuan models
- Check console for key standardization messages

### Weights Not Applied Correctly
- Verify tag format: `<lora:name:weight>` or `<lora:name:high:low>`
- Check that weights are valid numbers
- Look at `lora_info` output to see actual applied weights

## Comparison with Other Nodes

| Feature | This Node | Power Lora Loader | ImpactWildcardEncode | Standard LoRA Loader |
|---------|-----------|-------------------|----------------------|---------------------|
| Text-based tags | ✅ | ❌ | ✅ | ❌ |
| Unlimited LoRAs | ✅ | ✅ | ✅ | ❌ |
| Dual noise weights | ✅ | ❌ | ❌ | ❌ |
| Video model support | ✅ | ❌ | ❌ | ❌ |
| Clean text output | ✅ | ❌ | ✅ | ❌ |
| Visual UI | ❌ | ✅ | ❌ | ❌ |

## Credits

Inspired by:
- **rgthree-comfy** - Power Lora Loader concept
- **ComfyUI-Impact-Pack** - ImpactWildcardEncode tag parsing
- **ComfyUI-WanVideoWrapper** - Video model LoRA support

## License

MIT License - Feel free to use and modify!

## Support

If you encounter issues or have suggestions:
1. Check the console for detailed error messages
2. Verify your tag format matches the examples
3. Make sure LoRA files are in the correct directory
4. Open an issue on GitHub with your workflow and error details
