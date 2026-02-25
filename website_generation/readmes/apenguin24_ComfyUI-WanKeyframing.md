# ComfyUI-WanKeyframing

A powerful ComfyUI custom node collection for keyframe-based video generation and batch image processing. This extension provides advanced tools for creating smooth video sequences from keyframes with intelligent conditioning and latent space interpolation.

## Features

- **Batch Image Loading**: Load and process multiple images from directories with smart resizing and sorting
- **Keyframe Video Generation**: Create video sequences from keyframes with smooth transitions
- **Multiple Resize Modes**: Flexible image resizing with stretch, fit, and crop options
- **Advanced Sorting**: Sort images by name, date, size, or keep original order
- **Multi-Latent Encoding**: Generate video-ready latent representations with conditioning
- **Prompt Keyframing**: Use indexed prompts for different video segments

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Search for "WanKeyframing" in the manager
3. Click Install

### Method 2: Git Clone
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/apenguin24/ComfyUI-WanKeyframing.git
```

### Method 3: Manual Download
1. Download the repository as a ZIP file
2. Extract to `ComfyUI/custom_nodes/comfyui-wankeyframing/`
3. Restart ComfyUI

## Nodes Overview

### Load Images From Directory

Efficiently loads and processes multiple images from a directory with advanced options.

**Features:**
- **Smart Resizing**: Automatically resize images to consistent dimensions
- **Multiple Sort Options**: Sort by name, date, size, or preserve order
- **Reload Control**: Force reload images when needed
- **Format Support**: PNG, JPG, JPEG, BMP, WEBP, TIF, TIFF

**Parameters:**
- `directory`: Input directory path (relative to ComfyUI input folder)
- `reload_on_execute`: Force reload on each execution
- `target_width/height`: Target dimensions for all images (8-8192px)
- `resize_mode`: How to handle different sized images
  - **Stretch**: Stretch to exact dimensions (may distort)
  - **Fit**: Fit inside dimensions, pad with black
  - **Crop**: Crop to fill dimensions, maintain aspect ratio
- `sort_mode`: Image loading order
  - **name_asc/desc**: Sort alphabetically by filename
  - **date_asc/desc**: Sort by file modification date
  - **size_asc/desc**: Sort by file size
  - **none**: System order (no sorting)

### Wan Keyframe To Video

Advanced keyframe-to-video encoder that creates smooth video sequences with intelligent conditioning.

**Features:**
- **Multi-Segment Processing**: Process multiple keyframe pairs simultaneously
- **Indexed Prompts**: Use different prompts for different video segments
- **CLIP Vision Support**: Enhanced conditioning with vision embeddings
- **Flexible Video Length**: Control FPS and duration
- **Latent Space Interpolation**: Smooth transitions between keyframes

**Parameters:**
- `clip`: CLIP model for text encoding
- `positive_prompt`: Multi-line prompts with keyframe indexing (e.g., `[0] prompt1`)
- `negative_prompt`: Negative conditioning text
- `vae`: VAE model for latent encoding
- `width/height`: Video dimensions (16-8192px, step 16)
- `fps`: Frames per second (1-120)
- `seconds`: Video duration (1-60 seconds)
- `keyframes`: Input keyframe images (optional)
- `clip_vision_outputs`: CLIP vision embeddings (optional)

## 🔧 Usage Examples

### Basic Keyframe Video Workflow

1. **Load Keyframes**: Use "Load Images From Directory" to load your keyframe sequence
   - Set appropriate target dimensions
   - Use "name_asc" sorting for numbered sequences
   
2. **Generate Video**: Connect to "Wan Keyframe To Video"
   - Set desired video parameters (FPS, duration, dimensions)
   - Use indexed prompts for segment-specific conditioning:
     ```
     [0] A serene mountain landscape at dawn
     [1] The same landscape in golden hour
     [2] A starlit night scene
     ```

3. **Process**: The node will create smooth transitions between keyframes

### Advanced Prompt Keyframing

Use indexed prompts to control different segments of your video:

```
[0] A peaceful garden in spring, soft lighting
[1] The garden in summer, vibrant colors, bright sun
[2] Autumn garden with falling leaves, warm tones
[3] Winter garden covered in snow, cold blue lighting
```

Each `[N]` corresponds to the keyframe at index N, creating segment-specific conditioning.

## Technical Details

### Resize Modes Explained

- **Stretch**: Direct resize to target dimensions. Fast but may distort aspect ratio.
- **Fit**: Maintains aspect ratio, adds padding. Good for preserving image content.
- **Crop**: Maintains aspect ratio, crops excess. Good for filling frame completely.

### Video Generation Process

1. **Keyframe Processing**: Each consecutive pair of keyframes creates a video segment
2. **Prompt Mapping**: Indexed prompts are matched to keyframe segments
3. **Latent Encoding**: Images are encoded to latent space with VAE
4. **Conditioning**: CLIP embeddings are generated for each segment
5. **Stacking**: All segments are combined into a single batch for processing

### Performance Tips

- Use consistent image sizes when possible to reduce processing overhead
- Moderate video lengths (1-5 seconds) work best for memory efficiency
- Consider using lower resolution for testing, then upscale final results

## Troubleshooting

**Images won't load:**
- Check that the directory path is relative to ComfyUI's input folder
- Ensure images are in supported formats
- Verify file permissions

**Memory errors:**
- Reduce video length or resolution
- Use fewer keyframes
- Close other applications to free RAM

**Inconsistent results:**
- Enable "reload_on_execute" if images change frequently
- Check that keyframe count matches your prompt indexing
- Ensure all keyframes have similar content/style

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
