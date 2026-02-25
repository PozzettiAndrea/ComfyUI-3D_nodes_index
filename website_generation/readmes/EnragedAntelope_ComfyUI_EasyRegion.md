# ComfyUI EasyRegion

Control different parts of your image with separate prompts using visual box drawing.

## Quick Start

1. **Install**: Clone to `ComfyUI/custom_nodes/` or use ComfyUI Manager
2. **Add Node**: Search for "EasyRegion"
3. **Connect**: CLIP → EasyRegion → Sampler
4. **Draw**: Use canvas to position regions, type prompts
5. **Generate**: Connect to your sampler and run

## Nodes

### EasyRegion (Mask-Based)
**For:** Models using mask-based conditioning (Flux, Chroma, SD3, SD3.5, Qwen-Image)

**Inputs:**
- `clip`: CLIP from checkpoint
- `width`/`height`: Must match your latent dimensions
- `soften_masks`: Feathering at edges (recommended ON)
- `background_prompt`: Scene description
- `background_strength`: Background conditioning strength (0.5 default)
- `region1-4_prompt`: Region-specific prompts
- `region1-4_strength`: Per-region strength (start with 2-4, adjust as needed)

**General Tips:**
- **Include spatial location in prompts** - Try adding location hints like "on left side", "right third of image", "top right corner" to your region prompts. This may help guide placement, though results vary by model.
- Start with strength values 2.5-4.5, adjust if regions don't show or become too soft
- Lower background_strength (0.3-0.5) makes regions more prominent
- See "Model-Specific Tips" below for per-model guidance

### EasyRegion (Area-Based)
**For:** SD1.5, SD2.x, SDXL

Same interface, uses area-based conditioning instead of masks.

## Canvas Controls

- **region**: Select which region to edit (1-4)
- **box_x, box_y**: Region top-left position (pixels)
- **box_w, box_h**: Region dimensions (pixels)

## Example Workflow

```
Checkpoint Loader
├→ CLIP → EasyRegion (Mask-Based)
│           ├ width: 1024
│           ├ height: 1024
│           ├ soften_masks: true
│           ├ background_prompt: "empty city street at night"
│           ├ background_strength: 0.5
│           ├ region1_prompt: "red sports car on left side (left third)"
│           ├ region1_strength: 2.5
│           ├ region2_prompt: "giraffe on right side (right third)"
│           └ region2_strength: 3.5
├→ MODEL → KSampler ← conditioning
└→ VAE → VAE Decode
```

## Troubleshooting

**Regions not showing:**
- **Increase region strength** (try 3.0-5.0)
- Lower background_strength (try 0.3-0.5)
- Check width/height match your latent exactly
- Verify boxes aren't outside image bounds
- Try including spatial location in prompts ("left side", "right third")

**Soft/blurry regions:**
- **Lower region strength** (too high = loss of detail)
- Sweet spot is usually 2.5-4.5 with bg_strength=0.5

**Validation errors:**
- Ensure width/height are multiples of 64
- Check no regions overlap fullscreen

## Model-Specific Tips

### Flux (Flux.1-Dev, Flux.1-Schnell)
- **CFG**: Use CFG 1.0 with Flux Base (NO negative prompt)
  - Higher CFG = blur and artifacts
- **Strength range**: 2.5-4.5 works well with bg_strength=0.5
- **Region count**: Keep to 3-4 regions max for best results
- **Positioning**: Works best with regions positioned far apart (e.g., left/right thirds)

### SD3 / SD3.5
- Similar to Flux - mask-based conditioning
- Start with strength 2.5-4.5

### Chroma
- Mask-based conditioning like Flux
- Keep to 3-4 regions max

### SDXL / SD1.5
- Use EasyRegion (Area-Based) node instead
- Area-based conditioning doesn't use masks

## Credits

Based on visual area conditioning by [Davemane42](https://github.com/Davemane42).

Maintained by EnragedAntelope - [github.com/EnragedAntelope/ComfyUI_RegionalConditioning](https://github.com/EnragedAntelope/ComfyUI_RegionalConditioning)

## License

MIT License - use freely in personal and commercial projects.
