# Pixel Constrained Scaler (ComfyUI Node)

This node helps manage image sizes in a predictable way when working with ComfyUI.  
It keeps aspect ratio intact, respects a hard megapixel limit, applies an optional scaling factor, and makes sure dimensions land on clean multiples like 8 or 64.

The main goal is to avoid out-of-memory issues on GPUs while still giving you control over image scaling.

---

## What this node does

The scaler looks at your input image and runs through a simple logic:

1. If the input image is larger than the megapixel cap and you did not ask to scale down, it automatically shrinks the image to the pixel limit.  
2. If the input image is within the megapixel limit, it tries to apply the scaling factor you set.  
3. If the scaled image would exceed the limit, it pulls the size back down to fit.  
4. All dimensions are clamped within your min/max resolution settings.  
5. Final dimensions are rounded to the nearest multiple you specify (like 8, 16, 64).  
6. Aspect ratio is always preserved within a small tolerance.

This means:
- Large images automatically shrink unless you ask for explicit downscaling.  
- Smaller images upscale when allowed.  
- You always stay under the GPU’s safe resolution range.

---

## Why this exists

ComfyUI workflows often need a reliable way to prevent OOM errors, especially on lower-VRAM GPUs.  
At the same time, people want predictable scaling behavior that respects their inputs.  
This node sits in the middle and solves both problems without surprises.

---

## Inputs

**image**  
The image you want to process. Accepts single images or batches.

**min_res**  
Minimum width or height allowed. Prevents tiny outputs.

**max_res**  
Maximum width or height allowed. Prevents accidental huge outputs.

**max_megapixels**  
Hard pixel limit. Anything above this gets scaled down.

**scaling_factor**  
How much to scale the image.  
1.0 keeps the same size, 2.0 doubles it, 0.5 halves it.  
The megapixel cap still applies.

**multiple_of**  
Rounds the final width and height to this value.  
Useful for models that expect multiples of 8 or 64.

---

## Outputs

**image_passthrough**  
Your original image, unchanged.  
The scaler only calculates numbers; it doesn't modify the image.

**constrained_width / constrained_height**  
The final recommended resolution.

**constrained_aspect_ratio**  
Final aspect ratio after constraints.

**original_aspect_ratio**  
The aspect ratio from your input.

---

## Behavior examples

### Input smaller than limit
Input: 1366x768  
Scaling factor: 1.5  
Max MP: 2.6  
Result stays around 2048x1152 (rounded to nearest multiple).

### Input larger than limit
Input: 4096x4096  
Scaling factor: 1.0  
Max MP: 2.36  
Result becomes 1536x1536 (fits under pixel cap).

### Explicit downscale
Input: 4096x4096  
Scaling factor: 0.25  
Max MP: 2.36  
Result goes to 1024x1024 because the user explicitly asked for it.

---

## Installation

1. Create a `custom_nodes` folder in your ComfyUI directory if it doesn't exist
2. Clone this repository into the `custom_nodes` folder:
   ```bash
   git clone https://github.com/neonr-0/ComfyUI-PixelConstrainedScaler.git
   ```
---

## Notes

- The node does not change or resize your image. It only calculates what size it should be.  
- To actually resize, plug the width and height outputs into your preferred image resize node.  
- No external dependencies are required.

---

## License

This project is released under the MIT license. See the [LICENSE](LICENSE) file for details.