# ComfyUI-HairDetailer

**Hair detection, masking, and enhancement for ComfyUI**

A comprehensive custom node pack for detecting hair regions, creating precise masks, and enhancing hair details in images. Includes 6 specialized nodes for various hair processing workflows.

---

## Features

- **Multiple Detection Methods**: Color-based, edge-based, texture-based, and combined detection
- **Advanced Masking**: Separate masks for tight regions, expanded boundaries, and flyaways
- **Mask Refinement**: Post-processing tools for cleaning and perfecting masks
- **Hair Enhancement**: Targeted image enhancement for strand definition, shine, texture, and color
- **Color Analysis**: Extract and visualize dominant hair colors with K-means clustering
- **Regional Prompting**: Integrate hair masks with CLIP conditioning for targeted generation

---

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Install via ComfyUI Manager
2. Search for "HairDetailer"
3. Click Install

### Method 2: Manual Installation
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/xela-io/ComfyUI-HairDetailer.git
```

Restart ComfyUI after installation.

---

## Nodes Overview

### 1. Hair Detector
**Basic hair detection with traditional computer vision methods**

**Inputs:**
- `image` (IMAGE): Input image
- `method` (COMBO): Detection method
  - `combined`: Weighted combination of all methods (recommended)
  - `color`: HSV color range detection
  - `edge`: Edge density detection (good for curly hair)
  - `texture`: Gabor filter texture analysis
- `hair_color` (COMBO): Hair color for color-based detection
  - `auto`: Automatic color detection (uses all ranges)
  - `black`, `brown`, `blonde`, `red`, `white`, `gray`: Specific colors
  - `all`: Combine all color ranges
- `sensitivity` (FLOAT): Detection sensitivity (0.5-2.0, default 1.0)
- `blur_radius` (INT): Gaussian blur for mask smoothing (0-21)
- `morph_iterations` (INT): Morphological operations for cleanup (0-10)
- `expand_mask` (INT): Expand (+) or contract (-) mask (-20 to +20 pixels)
- `threshold` (FLOAT): Final threshold for mask binarization (0.0-1.0)

**Outputs:**
- `hair_mask` (MASK): Binary hair detection mask
- `preview` (IMAGE): Visual preview with blue overlay
- `method_info` (STRING): Detection method used and coverage percentage

**Use Cases:**
- Basic hair detection for any hair type
- Quick mask generation for further processing
- Testing different detection methods

---

### 2. Hair Detector (Advanced)
**Advanced detection with multiple mask outputs and filtering options**

**Inputs:**
- `image` (IMAGE): Input image
- `sensitivity` (FLOAT): Detection sensitivity (0.5-2.0)
- `face_mask` (MASK, optional): Exclude face region from detection
- `exclude_dark` (BOOLEAN): Remove very dark regions
- `exclude_bright` (BOOLEAN): Remove highlights/reflections
- `min_area` (INT): Minimum contour area to keep (0-10000 pixels)
- `detect_flyaways` (BOOLEAN): Create separate flyaway mask
- `feather` (INT): Edge blur amount (0-50)

**Outputs:**
- `hair_mask` (MASK): Standard hair mask
- `hair_tight` (MASK): Eroded mask (main hair mass only)
- `hair_expanded` (MASK): Dilated mask (includes flyaways)
- `flyaway_mask` (MASK): Only flyaway/loose strands
- `preview` (IMAGE): Visual preview

**Use Cases:**
- Separate processing for main hair and flyaways
- Exclude face regions when using face detection
- Filter out small noise regions
- Create multiple mask variations in one pass

---

### 3. Hair Mask Refiner
**Post-process hair masks with specialized refinements**

**Inputs:**
- `mask` (MASK): Input mask to refine
- `fill_holes` (BOOLEAN): Fill interior holes in mask
- `remove_small` (INT): Remove regions smaller than N pixels
- `feather` (INT): Edge smoothing radius (0-50)
- `expand` (INT): Expand (+) or contract (-) mask (-50 to +50)
- `connect_nearby` (BOOLEAN): Bridge gaps between nearby regions

**Outputs:**
- `refined_mask` (MASK): Refined mask

**Use Cases:**
- Clean up noisy detection results
- Fill gaps in hair masks
- Smooth harsh edges
- Remove unwanted small regions

---

### 4. Hair Detail Enhancer
**Apply targeted enhancement to hair regions**

**Inputs:**
- `image` (IMAGE): Input image
- `mask` (MASK): Hair region mask
- `strand_definition` (FLOAT): Enhance fine strand visibility (0.0-2.0)
- `shine_enhancement` (FLOAT): Enhance highlights/reflections (0.0-2.0)
- `texture_detail` (FLOAT): Multi-scale sharpening for texture (0.0-2.0)
- `color_vibrancy` (FLOAT): Saturation adjustment (0.0-2.0)
- `depth_enhancement` (FLOAT): Local contrast for 3D appearance (0.0-1.0)
- `blend_mode` (COMBO): Blending mode
  - `normal`: Direct blending
  - `luminosity`: Blend only brightness, preserve color
  - `overlay`: Overlay blend for dramatic effect
- `feather_edges` (INT): Mask edge softness (0-50)

**Outputs:**
- `enhanced_image` (IMAGE): Image with hair enhancement applied

**Enhancement Techniques:**
- **Strand Definition**: Multi-scale unsharp masking for crisp strands
- **Shine Enhancement**: Highlight boosting in LAB color space
- **Texture Detail**: Bilateral filtering with edge-preserving sharpening
- **Color Vibrancy**: HSV saturation adjustment
- **Depth Enhancement**: CLAHE local contrast enhancement

**Use Cases:**
- Enhance hair detail in portraits
- Add shine to dull hair
- Sharpen individual strands
- Increase color saturation in hair regions

---

### 5. Hair Color Analyzer
**Analyze and visualize dominant hair colors**

**Inputs:**
- `image` (IMAGE): Input image
- `mask` (MASK): Hair region mask
- `num_colors` (INT): Number of dominant colors to detect (1-5)
- `exclude_extremes` (BOOLEAN): Ignore very dark/bright pixels

**Outputs:**
- `color_info` (STRING): JSON data with color analysis
- `palette_image` (IMAGE): Visual color palette
- `dominant_color_mask` (MASK): Mask of most dominant color

**Color Info JSON Format:**
```json
{
  "num_colors": 3,
  "colors": [
    {
      "rank": 1,
      "name": "brown",
      "rgb": [120, 85, 60],
      "percentage": 65.5
    },
    {
      "rank": 2,
      "name": "blonde",
      "rgb": [180, 150, 110],
      "percentage": 25.3
    },
    {
      "rank": 3,
      "name": "gray",
      "rgb": [90, 88, 85],
      "percentage": 9.2
    }
  ]
}
```

**Use Cases:**
- Analyze hair color distribution
- Detect highlights and multi-tone hair
- Extract color palettes for reference
- Create masks for specific color regions

**Note:** Requires `scikit-learn` for K-means clustering. Falls back to average color if not available.

---

### 6. Hair Region Prompt
**Integrate hair masks with CLIP conditioning for regional prompting**

**Inputs:**
- `conditioning` (CONDITIONING): Base conditioning from CLIP Text Encode
- `hair_mask` (MASK): Hair region mask
- `hair_prompt` (STRING): Additional prompt for hair region (e.g., "detailed hair, fine strands, natural texture")
- `strength` (FLOAT): Conditioning strength (0.0-2.0)
- `feather` (INT): Mask edge blur (0-50)
- `set_area_to_bounds` (BOOLEAN): Optimize to bounding box area

**Outputs:**
- `conditioning` (CONDITIONING): Modified conditioning with regional prompt

**Use Cases:**
- Apply different prompts to hair vs. rest of image
- Enhance hair generation quality
- Control hair style independently
- Integrate with standard samplers (KSampler, etc.)

**Compatible with:**
- SD 1.5, SDXL, and other Stable Diffusion models
- Standard ComfyUI samplers (KSampler, KSampler Advanced, etc.)
- Other regional prompting workflows

---

## Example Workflows

### Basic Hair Detection and Enhancement

```
[Load Image]
    ↓
[Hair Detector]
    method: combined
    hair_color: auto
    sensitivity: 1.0
    ↓
[Hair Mask Refiner]
    fill_holes: true
    remove_small: 500
    feather: 10
    ↓
[Hair Detail Enhancer]
    strand_definition: 0.7
    shine_enhancement: 0.5
    texture_detail: 0.6
    ↓
[Save Image]
```

### Advanced Multi-Mask Processing

```
[Load Image]
    ↓
[Hair Detector (Advanced)]
    sensitivity: 1.2
    detect_flyaways: true
    ↓ (4 mask outputs)

[hair_mask] → [Hair Detail Enhancer] (main enhancement)
[hair_tight] → [High-intensity enhancement]
[hair_expanded] → [Light enhancement for edges]
[flyaway_mask] → [Separate flyaway processing]
```

### Hair Color Analysis

```
[Load Image]
    ↓
[Hair Detector]
    ↓
[Hair Color Analyzer]
    num_colors: 3
    exclude_extremes: true
    ↓
[color_info] → [Display String]
[palette_image] → [Save Image]
[dominant_color_mask] → [Further processing]
```

### Regional Prompting for Generation

```
[CLIP Text Encode]
    text: "portrait of a person"
    ↓
[Hair Region Prompt]
    hair_prompt: "flowing blonde hair, detailed strands, natural highlights"
    strength: 1.2
    ↓
[KSampler]
```

---

## Detection Methods Explained

### Color-Based Detection
Uses HSV color ranges to detect hair based on color. Works well for:
- Uniform hair color
- High contrast with background
- Black, brown, blonde, red, white, gray hair

**Limitations:**
- Struggles with very dark hair on dark backgrounds
- May miss highlights/multi-tone hair

### Edge-Based Detection
Detects high edge density areas (hair has many fine strands). Works well for:
- Curly/textured hair
- Flyaways and loose strands
- Complex hair patterns

**Limitations:**
- Can pick up other detailed textures
- Sensitive to noise

### Texture-Based Detection
Uses Gabor filters to detect directional patterns. Works well for:
- Straight/wavy hair with clear direction
- Smooth hair with consistent texture
- Low-contrast scenarios

**Limitations:**
- Slower than other methods
- May miss very fine strands

### Combined Method (Recommended)
Weighted combination of all three methods:
- 50% color-based
- 30% edge-based
- 20% texture-based

Provides the most robust detection across different hair types and scenarios.

---

## Hair Types and Recommended Settings

### Straight/Wavy Hair
- **Method**: `combined` or `color`
- **Sensitivity**: 1.0
- **Morph iterations**: 2-3
- **Enhancement**: Moderate strand definition (0.5), high shine (0.6)

### Curly/Textured Hair
- **Method**: `combined` or `edge`
- **Sensitivity**: 1.2-1.5
- **Morph iterations**: 3-5 (more connection needed)
- **Enhancement**: High texture detail (0.7), moderate strand definition (0.4)

### Dark Hair on Dark Background
- **Method**: `edge` or `texture`
- **Sensitivity**: 1.5-2.0
- **Exclude dark**: false
- **Enhancement**: High strand definition (0.8), moderate depth (0.5)

### Blonde Hair
- **Method**: `combined` with `hair_color: blonde`
- **Sensitivity**: 1.0-1.2
- **Exclude bright**: false
- **Enhancement**: Moderate shine (0.5), high color vibrancy (0.6)

### Gray/White Hair
- **Method**: `combined` with `hair_color: gray` or `white`
- **Sensitivity**: 1.0
- **Exclude bright**: true (to avoid background)
- **Enhancement**: Moderate strand definition (0.5), low color vibrancy (0.0)

---

## Technical Details

### Tensor Formats
- **Input Images**: PyTorch tensor (B, H, W, C) float [0, 1]
- **Masks**: PyTorch tensor (1, H, W) or (B, H, W) float [0, 1]
- **Processing**: NumPy arrays (H, W, C) uint8 [0, 255] for OpenCV operations
- **Conditioning**: Standard ComfyUI CONDITIONING format

### Morphological Operations
- Uses elliptical kernels for natural shapes
- CLOSE operation fills interior holes
- OPEN operation removes small noise
- Configurable iterations for intensity control

### Color Spaces
- **RGB**: Input/output images
- **HSV**: Color-based detection, saturation adjustment
- **LAB**: Shine enhancement, depth enhancement
- **Grayscale**: Edge detection, texture analysis

### Performance Considerations
- Detection methods vary in speed:
  - **Fastest**: Color-based
  - **Fast**: Edge-based
  - **Slower**: Texture-based (Gabor filters), Combined
- Image size affects processing time significantly
- Consider downscaling large images before detection

---

## Dependencies

### Required (Already in ComfyUI)
- `torch`: PyTorch tensors
- `numpy`: Array operations
- `cv2` (OpenCV): Image processing

### Optional
- `scikit-learn`: K-means clustering for HairColorAnalyzer (falls back to mean color if unavailable)

---

## Troubleshooting

### Detection Issues

**Problem**: No hair detected / empty mask
- **Solution**: Increase `sensitivity`, try different `method`, check `hair_color` setting

**Problem**: Too much false detection (background included)
- **Solution**: Decrease `sensitivity`, use `exclude_dark`/`exclude_bright` in Advanced node, increase `min_area`

**Problem**: Holes in hair mask
- **Solution**: Increase `morph_iterations`, use HairMaskRefiner with `fill_holes: true`

**Problem**: Flyaways not detected
- **Solution**: Use HairDetectorAdvanced with `detect_flyaways: true`, increase `sensitivity`

### Enhancement Issues

**Problem**: Enhancement looks unnatural
- **Solution**: Reduce enhancement strength values, use `luminosity` blend mode, increase `feather_edges`

**Problem**: Harsh edges around enhanced region
- **Solution**: Increase `feather_edges` in HairDetailEnhancer, increase `feather` in HairMaskRefiner

**Problem**: Hair looks over-sharpened
- **Solution**: Reduce `strand_definition` and `texture_detail` values

### Regional Prompting Issues

**Problem**: Hair prompt not affecting generation
- **Solution**: Increase `strength`, check mask coverage, ensure mask is properly feathered

**Problem**: Hard edges in generated hair region
- **Solution**: Increase `feather` value, ensure mask has smooth transitions

---

## Future Enhancements

Planned features for future releases:
- ML-based detection using segmentation models (SAM, BiRefNet)
- Hair style classification (straight, wavy, curly, coily)
- Automatic hair color correction
- Hair loss/density analysis
- Integration with ControlNet for hair guidance

---

## License

MIT License - See LICENSE file for details

---

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with clear description

---

## Support

- **Issues**: https://github.com/xela-io/ComfyUI-HairDetailer/issues
- **Discussions**: https://github.com/xela-io/ComfyUI-HairDetailer/discussions

---

## Credits

Developed by **xela-io**

Part of the ComfyUI custom node ecosystem for advanced image processing workflows.

---

## Version History

### v1.0.0 (2026-01-19)
- Initial release
- 6 core nodes: HairDetector, HairDetectorAdvanced, HairMaskRefiner, HairDetailEnhancer, HairColorAnalyzer, HairRegionPrompt
- Multiple detection methods: color, edge, texture, combined
- Advanced mask refinement and enhancement
- Regional prompting integration
