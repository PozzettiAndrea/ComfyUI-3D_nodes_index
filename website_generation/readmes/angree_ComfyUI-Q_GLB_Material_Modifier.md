# ComfyUI-Q_GLB_Material_Modifier

A ComfyUI custom node for enhancing GLB 3D models generated with Hunyuan 3D 2.0. This comprehensive module transforms the default "plastic look" by adding realistic materials, smart emissive elements, and procedural normal maps with advanced batch generation capabilities.

## Features

- **Material Enhancement**: Transforms the default "plastic" appearance of Hunyuan 3D 2.0 models into realistic materials
- **Smart Emissive Detection**: Automatically detects bright areas in textures and converts them to emissive parts
- **Normal Map Generation**: Creates high-quality normal maps from diffuse textures using multiple algorithms and presets
- **Batch Processing**: Generate up to 4 model variants simultaneously with different normal map and emissive combinations
- **Advanced Normal Maps**: Support for both auto-generated and custom normal textures with compression optimization
- **Color Preservation**: Preserves original colors in emissive areas for authentic lighting effects
- **Embedded Textures**: Properly embeds all textures (diffuse, emissive, normal) directly into GLB files
- **Material Presets**: Easy-to-use presets optimized for different material types
- **Flexible Workflows**: Works with any GLB model from Hunyuan 3D 2.0

## Installation

1. Clone this repository into your ComfyUI's `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/ComfyUI-Q_GLB_Material_Modifier.git
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```
or install manually:
```bash
pip install pygltflib>=1.16.1 opencv-python>=4.8.0 pillow>=10.0.0 numpy>=1.24.0
```

**Note**: This node requires PyTorch, but since Hunyuan 3D 2.0 workflows require CUDA-enabled PyTorch, you should install PyTorch with CUDA support separately according to your system's CUDA version. Visit [PyTorch's official installation guide](https://pytorch.org/get-started/locally/) for CUDA-specific installation instructions.

3. Restart ComfyUI

## Dependencies

This module requires the following Python libraries:
- **pygltflib**: For GLB/GLTF file manipulation (>=1.16.1)
- **opencv-python**: For image processing and normal map generation (>=4.8.0)
- **pillow**: For image loading and conversion (>=10.0.0)
- **numpy**: For array operations (>=1.24.0)
- **torch**: For tensor operations and ComfyUI compatibility (install CUDA version separately)

A `requirements.txt` file is included for easy installation of dependencies (except PyTorch).

## Usage with Hunyuan 3D 2.0

The extension provides two powerful nodes specifically designed for enhancing Hunyuan 3D 2.0 outputs:

### Q Manual GLB Material Modifier

This node provides complete control over all material parameters and can generate multiple variants:

**Basic Parameters:**
- **glb_path**: Path to your Hunyuan 3D 2.0 GLB file
- **texture_image**: Input texture from Hunyuan 3D 2.0
- **output_suffix**: Suffix to add to the output filename (default: "_modified")
- **render**: Enable/disable processing (when disabled, skips GLB generation)

**Material Properties:**
- **metallic_factor**: How metallic the surface should be (0-1)
- **smoothness**: How smooth the surface should be (0-1, converted to glTF roughness)
- **base_color_r/g/b**: Base color tint for the material

**Emissive Controls:**
- **emissive_mode**: Choose from "No Emissive", "With Emissive", or "Both Versions"
- **emissive_brightness_threshold**: Threshold for detecting bright areas (0.05-0.5)
- **emissive_percentage**: Percentage of brightest pixels to make emissive (0.01-0.15)
- **absolute_min_brightness**: Minimum brightness to consider emissive (50-200)
- **emissive_strength**: Brightness multiplier for emissive areas (0-2.0)

**Normal Map Generation:**
- **normal_mode_1**: Primary normal map mode with options:
  - No Normal Map
  - Use Input Texture (requires normal_texture input)
  - AutoGen Subtle, Normal, Enhanced, Dramatic, Smooth
- **normal_mode_2**: Secondary normal map mode (same options plus "Disable")
- **normal_algorithm**: "Sobel Filter" or "Simple Gradient" for auto-generation
- **normal_scale**: Texture scaling - "1x (Original)", "2x (Half Size)", "4x (Quarter Size)"
- **normal_compression**: Enable RG compression optimization for normal maps
- **normal_noise**: Add procedural surface detail noise (0-0.5)

**Optional Input:**
- **normal_texture**: Custom normal map texture (when using "Use Input Texture" mode)

**Returns:** Modified GLB path, emissive mask preview, normal map preview

### Q Preset GLB Material Modifier

This node provides convenient presets with the same advanced features:

**Presets Available:**
- **Spaceship Metal**: Balanced metallic with subtle emissive details
- **Brushed Steel**: Industrial look with surface texture noise
- **Chrome Hull**: High-reflectivity mirror finish
- **Chrome Hull Lite**: Softer chrome with more surface detail
- **Titanium**: Aerospace-grade metal appearance
- **Combat Metal**: Rough, battle-worn metallic surface
- **Alien Tech**: Sci-fi material with enhanced emissive effects

**Parameters:**
- All basic parameters from Manual modifier
- **preset**: Choose material preset instead of manual values
- **emissive_mode**: Control emissive generation behavior
- **normal_mode_1/2**: Same normal map options as Manual modifier
- **normal_algorithm, normal_scale, normal_compression**: Same normal controls

## Advanced Features

### Batch Generation Capabilities

Each node can generate up to **4 model variants** in a single run:

1. **Emissive Variants**: When "Both Versions" is selected:
   - Models with emissive effects (_EM suffix)
   - Models without emissive effects (_noEM suffix)

2. **Normal Map Variants**: When both normal_mode_1 and normal_mode_2 are enabled:
   - Each emissive variant gets both normal map versions
   - Automatic suffix generation (e.g., _normalautogen_enh_EM)

3. **Filename Convention**:
   - `{original_name}{output_suffix}{normal_suffix}{emissive_suffix}.glb`
   - Example: `model_modified_normalautogen_enh_EM.glb`

### Normal Map Generation

**Auto-Generation Presets:**
- **Subtle**: Light surface detail (strength: 0.7, blur: 1.0)
- **Normal**: Standard detail level (strength: 1.0, blur: 0.5)
- **Enhanced**: Increased detail (strength: 1.3, contrast: 1.2)
- **Dramatic**: Maximum detail (strength: 1.8, contrast: 1.5)
- **Smooth**: Soft surface details (strength: 1.0, blur: 2.0)

**Algorithms:**
- **Sobel Filter**: High-quality edge detection for detailed normal maps
- **Simple Gradient**: Faster generation with good results

**Advanced Processing:**
- Multi-octave procedural noise for surface roughness
- RG compression optimization for smaller file sizes
- Texture scaling for performance optimization
- Luminance-based heightmap conversion

## Hunyuan 3D 2.0 Workflows

### Complete Material Enhancement Pipeline

1. **Input**: Hunyuan 3D 2.0 GLB file + texture
2. **Processing**: Apply material preset or manual settings
3. **Normal Generation**: Auto-generate or use custom normal maps
4. **Emissive Detection**: Automatically find bright areas for glowing effects
5. **Batch Output**: Generate multiple variants with different combinations
6. **Result**: Up to 4 enhanced GLB files with embedded textures

### Fixing the "Plastic Look" Problem

Hunyuan 3D 2.0 models typically have a default "plastic" appearance. This tool addresses it by:

- **Material Properties**: Proper metallic/roughness values for realistic surfaces
- **Surface Detail**: Generated normal maps add micro-surface variations
- **Lighting Response**: Emissive areas create authentic light emission
- **Texture Integration**: All textures properly embedded and referenced

**Recommended Presets by Model Type:**
- **Mechanical/Sci-Fi**: Chrome Hull or Spaceship Metal
- **Industrial Equipment**: Brushed Steel or Combat Metal
- **High-Tech Devices**: Titanium or Chrome Hull Lite
- **Fantasy/Alien Objects**: Alien Tech with enhanced emissive

### Batch Production Workflow

Efficient workflow for generating multiple material variants:

1. Set **emissive_mode** to "Both Versions"
2. Configure **normal_mode_1** and **normal_mode_2** with different presets
3. Use descriptive **output_suffix** for organization
4. Enable **render** only for final generation
5. Result: 4 variants covering all combinations

### Performance Optimization

- **Normal Scaling**: Use "2x" or "4x" for large textures to reduce file size
- **Render Toggle**: Disable rendering during parameter testing
- **Compression**: Enable normal_compression for smaller file sizes
- **Batch Processing**: Generate multiple variants efficiently in single run

## Technical Implementation

### Emissive Detection Algorithm

1. **Brightness Analysis**: Convert texture to grayscale for luminance calculation
2. **Percentile Threshold**: Find brightest X% of pixels based on user settings
3. **Contrast Validation**: Ensure sufficient contrast between bright and average areas
4. **Mask Generation**: Create smooth transition masks using Gaussian blur
5. **Color Preservation**: Maintain original colors in emissive areas

### Normal Map Generation Pipeline

1. **Heightmap Conversion**: Convert diffuse texture to grayscale heightmap using luminance
2. **Gradient Calculation**: Apply Sobel filters or simple gradients for surface derivatives
3. **Vector Normalization**: Convert gradients to normalized surface normal vectors
4. **Range Conversion**: Transform from [-1,1] to [0,1] for texture storage
5. **Quality Enhancement**: Apply noise, compression, and scaling optimizations

### GLB Integration

- **Texture Embedding**: Convert images to base64 data URIs for direct embedding
- **Material Updates**: Modify glTF material properties for PBR rendering
- **Sampler Configuration**: Set up proper texture sampling parameters
- **Format Optimization**: Use PNG with optimal compression settings

## Example Use Cases

### Spacecraft Model Enhancement
```
Input: Basic Hunyuan 3D spacecraft GLB
Preset: "Spaceship Metal"
Normal: "AutoGen Enhanced" 
Emissive: "With Emissive"
Result: Realistic metal hull with glowing engine parts and surface detail
```

### Industrial Equipment Texturing
```
Input: Machinery GLB from Hunyuan 3D
Preset: "Brushed Steel"  
Normal: "AutoGen Dramatic" + "AutoGen Smooth"
Emissive: "Both Versions"
Result: 4 variants with different surface finishes and lighting combinations
```

### Character Armor Materials
```
Input: Character armor GLB
Manual Settings: High metallic, medium smoothness
Normal: Custom normal texture + "AutoGen Subtle"
Emissive: Force off for realistic armor
Result: Multiple armor variants with custom and generated normal details
```

## License

[MIT License](LICENSE)
