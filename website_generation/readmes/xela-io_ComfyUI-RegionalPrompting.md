# ComfyUI-RegionalPrompting

Regional Prompting for ComfyUI - assign different prompts to different image areas.

## Features

- Create masks for any image region (rectangular, oval, predefined)
- Assign multiple prompts to different regions
- **Full compatibility** with CharacterBuilder, StyleSelector, SettingSelector, QualityEnhancer
- Predefined layouts (Left/Right, Top/Bottom, 2x2, 1x3, etc.)
- Soft transitions (feathering) between regions
- Strength control per region

## Installation

```bash
# In ComfyUI Docker Container
sudo docker cp ComfyUI-RegionalPrompting comfyui-exp:/opt/ComfyUI/custom_nodes/
sudo docker restart comfyui-exp
```

## Nodes

### 1. SimpleRegionalPrompt (Recommended for Beginners)

The easiest way for 2-region scenes.

**Inputs:**
- `clip`: CLIP Model
- `width/height`: Image size
- `split_mode`: left_right, top_bottom, center_surround
- `split_ratio`: Where the split occurs (0.5 = center)
- `global_prompt`: Applies to entire image
- `region_a_prompt`: Left/Top region (or center)
- `region_b_prompt`: Right/Bottom region (or surround)
- `negative_prompt`: Negative description
- `feather`: Soft edges (0-0.3)

**Outputs:**
- `positive`: Combined conditioning
- `negative`: Negative conditioning
- `mask_a/mask_b`: The created masks (for debugging)

### 2. MaskRegionCreator

Creates a single mask for an image area.

**Inputs:**
- `width/height`: Image size
- `region_type`: rectangle, oval, left_half, right_half, top_half, bottom_half, center, full
- `x_start/y_start/x_end/y_end`: Coordinates (0.0-1.0)
- `feather`: Soft edges
- `invert`: Invert mask

**Outputs:**
- `mask`: The created mask
- `x, y, region_width, region_height`: Pixel coordinates

### 3. MaskFromRegions

Creates up to 4 masks from predefined layouts.

**Layouts:**
- `1x2`: Left | Right
- `2x1`: Top | Bottom
- `1x3`: 3 columns
- `3x1`: 3 rows
- `2x2`: 4 squares
- `1+2`: 1 top, 2 bottom
- `2+1`: 2 top, 1 bottom
- `custom`: Define custom regions

**Custom Format:**
```
x1,y1,x2,y2
0,0,0.5,0.5
0.5,0,1,0.5
0,0.5,1,1
```

### 4. RegionalPromptComposer

Combines multiple prompts with their masks.

**Inputs:**
- `global_prompt`: Base prompt for entire image
- `region1-4_prompt`: STRING input (from CharacterBuilder etc.)
- `region1-4_mask`: MASK input (from MaskRegionCreator etc.)
- `region1-4_strength`: Strength per region (0-2)
- `negative_prompt`: Negative description

**Outputs:**
- `regional_data`: Structured data for Combiner
- `combined_prompt_preview`: Text preview
- `negative_prompt`: Pass-through

### 5. RegionalConditioningCombiner

Converts RegionalPromptComposer output into final conditioning.

**Inputs:**
- `regional_data`: From RegionalPromptComposer
- `clip`: CLIP Model
- `base_conditioning`: Optional, as base
- `blend_mode`: average, add, max

**Outputs:**
- `positive`: Final positive conditioning
- `negative`: Final negative conditioning

---

## Workflow Examples

### Example 1: Two Characters (Left/Right)

```
+-----------------+     +-----------------+
| CharacterBuilder|     | CharacterBuilder|
| (Person 1)      |     | (Person 2)      |
+--------+--------+     +--------+--------+
         |                       |
         |     +-------------+   |
         +---->| SimpleRegional|<-+
               | Prompt       |
               | split: L/R   |
               +------+-------+
                      |
               +------v-------+
               |   KSampler   |
               +--------------+
```

### Example 2: Foreground + Background

```
+-----------------+     +-----------------+
| CharacterBuilder|     | SettingSelector |
| (Person)        |     | (Background)    |
+--------+--------+     +--------+--------+
         |                       |
         |     +-------------+   |
         +---->| SimpleRegional|<-+
               | split: center |
               | _surround     |
               +------+--------+
                      |
               +------v-------+
               |   KSampler   |
               +--------------+
```

### Example 3: Complex 4-Region Layout

```
+---------------+
| MaskFromRegions|
| layout: 2x2   |
+---+---+---+---+
    |   |   |   | (4 masks)
    v   v   v   v
+-------------------------------------------+
|           RegionalPromptComposer          |
|  +----------++----------++----------++----------+
|  |Character ||Character ||Setting   ||Style     |
|  |Builder 1 ||Builder 2 ||Selector  ||Selector  |
|  +----------++----------++----------++----------+
+-----------------------+-------------------+
                        |
                        v
              +---------------------+
              |RegionalConditioning |
              |     Combiner        |
              +----------+----------+
                         |
                  +------v-------+
                  |   KSampler   |
                  +--------------+
```

---

## Tips

### Feathering

- `0.0`: Hard edges (can lead to visible transitions)
- `0.02-0.05`: Light blurring (recommended)
- `0.1+`: Very soft transitions (for natural blends)

### Strength

- `1.0`: Normal
- `<1.0`: Weaker, more of the global prompt visible
- `>1.0`: Stronger, but can lead to artifacts

### Best Practices

1. Use **Global Prompt** for style/quality (e.g., StyleSelector output)
2. Use **Region Prompts** for specific content (CharacterBuilder, SettingSelector)
3. Use **Feathering** for natural transitions
4. Use **QualityEnhancer** at the end of the prompt chain for final improvements

---

## Compatibility

Fully compatible with:
- ComfyUI-CharacterBuilder
- ComfyUI-StyleSelector
- ComfyUI-SettingSelector
- ComfyUI-QualityEnhancer
- ComfyUI-LMStudio-PromptRewriter
- Standard ComfyUI CLIP/VAE/KSampler

## Dependencies

- NumPy (standard in ComfyUI)
- SciPy (for feathering - usually already installed)
- PyTorch (standard in ComfyUI)

If SciPy is missing:
```bash
pip install scipy
```

## Example Workflows

In the `workflows/` folder you'll find ready-made JSON workflows:

- **two_characters_example.json** - Two characters Left/Right with SimpleRegionalPrompt
- **four_regions_advanced.json** - 4-region layout (2x2) with CharacterBuilder + SettingSelector

Import: ComfyUI -> Load -> Select workflow JSON

## Technical Details

### CLIP Encoding

The node uses a robust CLIP API with fallback for different ComfyUI versions:

```python
def encode_text(clip, text):
    tokens = clip.tokenize(text)
    try:
        # Modern ComfyUI API
        output = clip.encode_from_tokens(tokens, return_pooled=True, return_dict=True)
        cond = output.pop("cond")
        return [[cond, output]]
    except (TypeError, KeyError):
        # Fallback for older API
        result = clip.encode_from_tokens(tokens, return_pooled=True)
        if isinstance(result, tuple) and len(result) == 2:
            cond, pooled = result
            return [[cond, {"pooled_output": pooled}]]
        else:
            return [[result, {"pooled_output": None}]]
```

**Note about pooled_output:**
- **SD1.5 models**: `pooled_output: None` is normal behavior
- **SDXL models**: `pooled_output` contains a tensor

### Mask Format

Masks are returned as PyTorch tensor in format `[1, H, W]`:
- Values: 0.0 (outside) to 1.0 (inside the region)
- Feathering creates intermediate values for soft transitions

### Conditioning Structure

Regional conditionings are combined as a list:
```python
[
    [cond_tensor, {"pooled_output": pooled}],           # Global
    [cond_tensor, {"pooled_output": pooled, "mask": mask_a, ...}],  # Region A
    [cond_tensor, {"pooled_output": pooled, "mask": mask_b, ...}],  # Region B
]
```

## Changelog

### 1.0.2 (current)
- **Improvement**: More robust CLIP API with fallback for different ComfyUI versions
- **Compatibility**: Now works reliably with SD1.5 and SDXL
- SD1.5: `pooled_output: None` is normal behavior
- SDXL: `pooled_output` contains correct tensor

### 1.0.1
- **Bugfix**: CLIP encoding for SDXL corrected (`return_dict=True`)
- **Bugfix**: `pooled_output` is now set correctly
- More robust error handling for missing SciPy

### 1.0.0
- Initial release
- 5 Nodes: SimpleRegionalPrompt, MaskRegionCreator, MaskFromRegions, RegionalPromptComposer, RegionalConditioningCombiner
- Predefined layouts and custom regions
- Feathering support
