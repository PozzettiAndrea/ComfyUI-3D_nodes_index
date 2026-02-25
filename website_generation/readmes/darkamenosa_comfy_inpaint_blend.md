# comfy_inpaint_blend

Advanced blending algorithms for seamless inpainting in ComfyUI. Specifically designed for image-space inpainting models like **Google Nano Banana** and **ByteDance Seedream 4** that work directly on images rather than latent space.

## The Problem

When using image-space inpainting models (not latent-space KSampler workflows), the typical workflow is:
1. **Crop** the masked area to a small image
2. **Generate** new content with models like Nano Banana or Seedream 4
3. **Merge** the generated image back into the original

The standard `ImageCompositeMasked` node works well with Google Nano Banana but fails with ByteDance Seedream 4, which tends to generate brighter colors that don't blend naturally.

## Why Poisson Blending?

**Poisson blending** solves the color mismatch problem by:
- **Preserving textures and details** from the generated content
- **Automatically matching colors** to match the original image
- **Creating seamless transitions** without visible seams
- **Especially effective for Seedream 4's** tendency to brighten colors

## Features

- **Default Mode**: Traditional alpha/mask compositing
- **Poisson Mode**: Advanced gradient-domain blending
  - Preserves source gradients (textures, edges, details)
  - Adjusts colors to match destination seamlessly
  - Eliminates visible seams at mask boundaries
  - Perfect for fixing color mismatches in inpainting results

## Installation

1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/darkamenosa/comfy_inpaint_blend.git
   ```

3. Install dependencies:
   ```bash
   pip install -r comfy_inpaint_blend/requirements.txt
   ```

4. Restart ComfyUI

## Usage

The node appears as **"Enhanced Image Composite Masked"** in the image/inpainting category.

### Typical Image-Space Inpainting Workflow

1. **Crop** the masked region from your original image
2. **Generate** new content using Nano Banana or Seedream 4
3. **Use this node** to merge the generated content back
4. **For Nano Banana**: `"default"` mode usually works well
5. **For Seedream 4**: Use `"poisson"` mode to fix color brightness issues

### Inputs

- **destination**: The original/background image
- **source**: The inpainted/generated image to composite
- **x**: X position for placement (0 to MAX_RESOLUTION)
- **y**: Y position for placement (0 to MAX_RESOLUTION)
- **resize_source**: Whether to resize source to fit destination
- **blend_mode**:
  - `"default"`: Standard alpha compositing (may show seams)
  - `"poisson"`: Gradient-domain blending (seamless, color-matched)
- **mask** (optional): Inpainting mask defining the blend region

### Output

- **IMAGE**: The seamlessly composited result

## Poisson Blending Algorithm

The Poisson mode implements the algorithm from "Poisson Image Editing" (Pérez et al., 2003). This technique is particularly effective for inpainting workflows where the AI generates good textures but incorrect colors.

### How It Works

The algorithm solves the Poisson equation **∇²f = ∇²g** where:
- **f**: The final blended image we're solving for
- **g**: The source image (inpainted content) whose gradients we preserve
- **Boundary conditions**: Colors from the destination image at mask edges

### Implementation Details

Currently using a **pure PyTorch Jacobi iterative solver**:
- Preserves source image gradients (textures, edges, patterns)
- Enforces destination colors at boundaries
- Iteratively propagates color corrections inward
- Converges to a seamless blend that matches surrounding colors

### Why This Solves Inpainting Color Mismatch

1. **Gradient Preservation**: Keeps all the texture details from the AI-generated content
2. **Color Harmonization**: Automatically adjusts the overall color/lighting to match surroundings
3. **Seamless Boundaries**: No visible seams or color jumps at mask edges
4. **Structure Retention**: Maintains the structural integrity of the inpainted content

## Technical Details

### Performance Considerations

- **Iterative Solver**: Uses up to 400 iterations with convergence tolerance of 1e-4
- **GPU Acceleration**: Fully leverages PyTorch CUDA for fast computation
- **Memory Efficient**: Operates directly on image tensors without sparse matrices
- **Batch Processing**: Supports batched operations for video/animation workflows

### Algorithm Parameters

The Poisson solver uses:
- **Jacobi iterations**: Stable convergence for the discrete Poisson equation
- **4-neighbor Laplacian**: Standard discrete approximation of gradient operator
- **Replicate padding**: Handles image boundaries naturally
- **Early stopping**: Exits when convergence tolerance is reached

## Model Characteristics

### Google Nano Banana
**Strengths:**
- Accurate color editing
- Works well with default blending mode
- Good for targeted inpainting

**Limitations:**
- Best within 1024x1024 resolution
- May lose skin texture details
- Can alter faces, especially with multiple people

**Recommended for:** Precise inpainting tasks

### ByteDance Seedream 4
**Strengths:**
- Supports 4K resolution
- Excellent face preservation
- Superior skin texture quality

**Limitations:**
- Requires upscaling input to 1024px minimum
- Generates brighter colors (requires Poisson blending)
- Not ideal for direct inpainting without color correction

**Recommended for:** Full image generation, requires Poisson mode for inpainting

## Use Cases

### Perfect for:
- **Image-space inpainting**: Models that work directly on images (not latent space)
- **Color mismatch correction**: Especially Seedream 4's brightness issues
- **Face/skin editing**: Preserving texture while fixing colors
- **High-resolution workflows**: 4K support with proper blending
- **Multi-person scenes**: Maintaining consistent lighting across edits

## Requirements

- Python >= 3.8
- PyTorch >= 1.9.0 (with CUDA support recommended)
- NumPy >= 1.19.0
- OpenCV >= 4.5.0 (optional, for future optimizations)
- ComfyUI (latest version)

## License

MIT