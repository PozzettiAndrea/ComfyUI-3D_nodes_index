# ComfyUI_SamplingUtils

A collection of utility nodes for ComfyUI providing sampling parameter management, text encoding with system prompts, mask manipulation, image blending, text obfuscation, and more.

## Installation

Place this folder in your `ComfyUI/custom_nodes/` directory.

### Dependencies

- `pilgram` - For image blending modes
- `kornia` - For morphological mask operations
- `scipy` - For mask hole filling

## Nodes

### Sampling & Parameters

#### SamplingParameters
**Category:** `utils`

Centralized sampling parameter management node. Outputs width, height, batch size, upscaled dimensions, steps, CFG scale, seed, and calculated tile dimensions for tiled processing.

- **Inputs:** width, height, batch_size, scale_by, multiple, steps, cfg, seed
- **Outputs:** All input parameters plus computed upscaled_width, upscaled_height, tile_width, tile_height, tile_padding

---

### JSON Utilities

#### GetJsonKeyValue
**Category:** `utils`

Loads values from a JSON key-value file with multiple selection methods. Useful for API key rotation or configuration management.

**Key ID Methods:**
- `custom` - Select a specific key by name
- `random_rotate` - Randomly select from available keys
- `increment_rotate` - Cycle through keys based on rotation interval

---

### Text Encoding (Conditioning)

#### TextEncodeSystemPrompt
**Category:** `advanced/conditioning`

Unified text encoder supporting multiple model template formats. The recommended node for system prompt injection.

| Model Type | Template Format | Use Case |
|------------|-----------------|----------|
| `flux2dev` | `[SYSTEM_PROMPT]...[/SYSTEM_PROMPT][INST]{}[/INST]` | Flux 2 Dev |
| `klein` | `<\|im_start\|>system...` with `<think>` tags | Klein (supports thinking content) |
| `z-image` | `<\|im_start\|>system...` format | Z-Image models |

#### TextEncodeFlux2SystemPrompt
**Category:** `advanced/conditioning`

Dedicated encoder for Flux 2 models with LLAMA-style system prompt injection.

#### TextEncodeKleinSystemPrompt
**Category:** `advanced/conditioning`

Encoder for Klein models with support for custom thinking content injection.

#### TextEncodeZITSystemPrompt
**Category:** `advanced/conditioning`

Encoder for Z-Image models using the `<|im_start|>` template format.

#### SystemMessagePresets
**Category:** `advanced/conditioning`

Provides preset system prompts for Flux 2 models:
- `F2_SYSTEM_MESSAGE` - Standard system message
- `F2_SYSTEM_MESSAGE_UPSAMPLING_I2I` - Image-to-image upsampling prompt
- `F2_SYSTEM_MESSAGE_UPSAMPLING_T2I` - Text-to-image upsampling prompt

---

### Mask Operations

#### ModifyMask
**Category:** `utils/mask`

Advanced mask manipulation with expansion, contraction, blurring, and hole filling.

**Features:**
- Expand/contract masks using morphological operations
- Tapered or square corner modes
- Gaussian blur with original pixel preservation
- Incremental expansion rate for animated masks
- Lerp alpha and decay factor for temporal effects
- Optional hole filling

---

### Image Operations

#### ImageBlendByMask
**Category:** `utils/mask`

Composite images using various Photoshop-style blending modes.

**Supported Modes:**
`add`, `color`, `color_burn`, `color_dodge`, `darken`, `difference`, `exclusion`, `hard_light`, `hue`, `lighten`, `multiply`, `overlay`, `screen`, `soft_light`

#### Image_Color_Noise
**Category:** `utils`

Generate procedural noise images with various frequency characteristics.

**Noise Types:**
- `grey` - Grayscale noise
- `white` - RGB white noise
- `red`, `green`, `blue` - Single channel noise
- `pink` - 1/f noise (natural frequency distribution)
- `mix` - Multi-frequency RGB noise

#### SU_LoadImagePath
**Category:** `image`

Load images from arbitrary file system paths with proper mask handling.

**Features:**
- Loads from absolute file paths (not just ComfyUI input folder)
- Proper alpha channel extraction for RGBA and palette images
- Full-sized zero mask for images without alpha (not 64x64)
- 16-bit image support with correct normalization
- Multi-frame image support (GIFs)
- EXIF orientation handling

---

### Text Obfuscation

#### Frakturpad (Text Obfuscation)
**Category:** `text`

Obfuscates text by converting ASCII letters to Unicode bold fraktur characters (𝕬𝖇𝖈...) and padding with word joiner characters (U+2060). Useful for bypassing text filters while maintaining readability.

#### UnFrakturPad (Text Deobfuscation)
**Category:** `text`

Reverses the frakturpad operation - removes word joiners and converts bold fraktur back to ASCII.

---

## API Version

This extension uses the **ComfyUI V3 API** (`ComfyExtension`, `io.Schema`).

## License

See LICENSE file in the repository root.
