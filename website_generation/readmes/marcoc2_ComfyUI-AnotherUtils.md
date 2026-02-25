# ComfyUI AnotherUtils - Complete Node Collection

A comprehensive collection of custom nodes for ComfyUI, featuring image processing, animation tools, character generation, and advanced filters inspired by GIMP/GEGL.

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory
2. Clone this repository:
```bash
git clone https://github.com/yourusername/ComfyUI-AnotherUtils.git
```
3. Restart ComfyUI

## Node Categories

### 🖼️ Image Processing & Loaders

#### Load Images (Original Size)
Loads all images from a directory while preserving their original dimensions.
- **Input:** Directory path
- **Output:** Images in original sizes
- **Features:** Compatible with RebatchImages, supports common formats

#### Load Image (Remove Alpha)
Loads an image from file path and removes alpha channel, compositing over white background.
- **Input:** Image file path
- **Output:** RGB image without transparency

#### Remove Alpha Channel
Removes alpha channel from already loaded images, compositing over white background.
- **Input:** RGBA image
- **Output:** RGB image without transparency

#### Custom Crop
Crops images with specific positioning options.
- **Inputs:** Image, crop dimensions, position mode
- **Modes:** center, left, right, top, bottom

#### Smart Resize with Border Fill
Intelligently resizes images while filling missing areas with border colors.
- **Inputs:** Image, target size, sampling method
- **Color Methods:** mean or mode for border detection

#### Nearest Neighbor Upscale
Perfect upscaling for pixel art without interpolation artifacts.
- **Input:** Image, scale factor (1-8)
- **Output:** Crisp upscaled image

#### Get Last Image
Utility node that returns the last image from a batch.
- **Input:** Image batch
- **Output:** Single image (last in sequence)

### 🎨 Pixel Art Tools

#### Pixel Art Normalizer
Normalizes images into consistent pixel art style with grid detection.
- **Inputs:** Image, block size (auto-detect if 0), color count
- **Outputs:** Normalized image, detected block size, true 1:1 pixel art
- **Features:** Automatic grid detection, color quantization

#### Pixel Art Converter
Advanced pixel art conversion with customizable settings.
- **Inputs:** Image, target resolution, color palette options
- **Output:** Converted pixel art image

#### Pixel Art Converter (Parallel)
Multi-threaded version of the pixel art converter for batch processing.
- **Input:** Image batch
- **Output:** Batch of converted pixel art images

### 🎮 Character Generation

#### Character Randomizer
Generates random character attributes for fighting game characters.
- **Input:** Random seed
- **Outputs:** 10 character attributes (gender, fighting style, nationality, etc.)
- **Features:** Deterministic randomization, extensive attribute lists

#### Character Constructor
Constructs detailed character prompts from selected attributes.
- **Inputs:** All character attributes (gender, style, nationality, etc.)
- **Outputs:** Complete character prompt, formatted attribute summary
- **Use Case:** Perfect for AI character generation workflows

### 🏃‍♂️ Animation Tools

#### Fighting Game Character Generator
Creates character sprites and animations for fighting games.
- **Inputs:** Character parameters, pose settings
- **Output:** Character sprite sheets

#### Walking Pose Generator
Generates walking animation frames with customizable parameters.
- **Inputs:** Base character, walk cycle settings
- **Output:** Animation frame sequence

### 🎨 GIMP-Style Filters

#### Adaptive Noise Filter
Applies frequency-aware noise that adapts to image content.
- **Inputs:** Image, noise strength, adaptation strength, edge threshold
- **Features:** More noise on edges, less on flat areas
- **Types:** Gaussian or Uniform noise

#### RGB Noise (GEGL-like)
RGB channel noise filter matching GIMP's GEGL implementation.
- **Inputs:** Image, noise amount per channel, correlation settings
- **Output:** Image with channel-specific noise

#### CIE LCH Noise (GEGL-like)
Perceptually uniform noise in CIE LCH color space.
- **Inputs:** Image, lightness/chroma/hue noise amounts
- **Features:** Perceptually natural noise distribution

#### Mean Curvature Blur (GEGL-like)
Edge-preserving blur based on surface curvature analysis.
- **Inputs:** Image, blur radius, iterations
- **Features:** Preserves edges while smoothing flat areas

#### Image Type Detector
Detects if input is single image or batch and provides appropriate outputs.
- **Input:** Image/batch
- **Outputs:** Single image, batch images, count, type flag
- **Use Case:** Workflow routing and debugging

## Usage Examples

### Character Generation Workflow
```
CharacterRandomizer -> CharacterConstructor -> [AI Image Generation]
```

### Pixel Art Pipeline
```
LoadImagesOriginal -> PixelArtNormalizer -> NearestUpscale -> [Output]
```

### Advanced Image Processing
```
LoadImages -> AdaptiveNoise -> MeanCurvatureBlur -> [Final Processing]
```

### Animation Creation
```
CharacterGenerator -> WalkingPoseGenerator -> [Animation Export]
```

### Dataset Preparation
```
LoadImagesOriginal -> CustomCrop -> SmartResize -> RemoveAlpha -> [Training]
```

## Node Count
**Total: 19 Nodes**
- 8 Image Processing & Loaders
- 3 Pixel Art Tools  
- 2 Character Generation
- 2 Animation Tools
- 5 GIMP-Style Filters

## Dependencies
- NumPy
- OpenCV (cv2)
- scikit-learn
- PIL/Pillow
- PyTorch (provided by ComfyUI)

## Features
- **Batch Processing:** Most nodes support batch operations
- **Memory Efficient:** Optimized for large image sets
- **ComfyUI Native:** Full compatibility with ComfyUI ecosystem
- **Deterministic:** Seed-based operations for reproducible results
- **Professional Grade:** GIMP/GEGL equivalent filters

## Contributing
Issues and pull requests welcome! Please follow the existing code style and include tests for new features.

## License
MIT License - See LICENSE file for details

---
*Created by marcoags - Version 1.0.0*