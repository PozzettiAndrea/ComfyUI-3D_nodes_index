# ComfyUI Substance Designer Integration Plugin

A comprehensive ComfyUI plugin that enables seamless integration with Substance 3D Designer workflows through command line automation. This plugin provides custom nodes for cooking .sbs files, rendering .sbsar archives, controlling material parameters, and batch processing Substance materials within ComfyUI workflows.

## Features

### Core Functionality
- **Substance Cooker Node**: Convert .sbs files to .sbsar archives with configurable optimization levels
- **Substance Renderer Node**: Render .sbsar files to texture maps with full parameter control
- **Parameter Controller Node**: Dynamically manipulate material parameters and generate variations
- **Batch Processor Node**: Process multiple files or generate multiple variations efficiently
- **Info Extractor Node**: Extract metadata and parameter information from .sbsar files

### Advanced Capabilities
- **Parallel Processing**: Multi-threaded batch operations for improved performance
- **Parameter Randomization**: Generate material variations with controlled randomization
- **Intelligent Caching**: Avoid redundant operations with smart caching system
- **Comprehensive Error Handling**: Robust error management with detailed logging
- **Flexible Configuration**: Customizable settings for tools, performance, and behavior

## Prerequisites

### Required Software
1. **ComfyUI**: Latest version with custom node support
2. **Substance 3D Automation Toolkit**: Required for command line tools
   - Download from [Adobe Substance 3D](https://www.adobe.com/products/substance3d-automation-toolkit.html)
   - Ensure `sbscooker` and `sbsrender` are accessible in your system PATH

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **Memory**: 8GB RAM minimum, 16GB recommended for batch processing
- **Storage**: 2GB free space for plugin and cache
- **CPU**: Multi-core processor recommended for parallel processing

## Installation

### Method 1: Direct Installation
1. Clone or download this repository to your ComfyUI custom nodes directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   git clone https://github.com/jasonjgardner/comfyui-substance-designer-integration.git
   ```

2. Install Python dependencies:
   ```bash
   cd comfyui-substance-designer-integration
   pip install -r requirements.txt
   ```

3. Restart ComfyUI to load the new nodes

### Method 2: ComfyUI Manager (if available)
1. Open ComfyUI Manager
2. Search for "Substance Designer Integration"
3. Click Install and restart ComfyUI

### Verification
After installation, you should see the following nodes in the "substance" category:
- Substance Cooker
- Substance Renderer
- Substance Parameter Controller
- Substance Batch Processor
- Substance Info Extractor

## Configuration

### Automatic Tool Detection
The plugin automatically detects Substance 3D Automation Toolkit installations in common locations:
- Windows: `C:\\Program Files\\Adobe\\Adobe Substance 3D Automation Toolkit\\bin`
- macOS: `/Applications/Adobe Substance 3D Automation Toolkit/bin`
- Linux: `/opt/Adobe/Adobe_Substance_3D_Automation_Toolkit/bin`

### Manual Configuration
If automatic detection fails, you can manually configure tool paths by creating a configuration file:

```json
{
  "tool_paths": {
    "sbscooker": "/path/to/sbscooker",
    "sbsrender": "/path/to/sbsrender"
  },
  "defaults": {
    "cooking": {
      "optimization_level": 1,
      "timeout": 300
    },
    "rendering": {
      "output_format": "png",
      "bit_depth": "8",
      "memory_budget": 2000
    }
  }
}
```

Save this as `config.json` in your ComfyUI configuration directory under `substance_designer/config.json`.

## Quick Start Guide

### Basic Workflow: Cook and Render
1. **Add Substance Cooker Node**
   - Set `sbs_file_path` to your .sbs file
   - Set `output_directory` for .sbsar output
   - Configure optimization level (0-3)

2. **Connect to Substance Renderer Node**
   - Connect the `sbsar_file_path` output from cooker
   - Set texture output directory
   - Choose output format (PNG, TIFF, EXR, etc.)

3. **Execute Workflow**
   - The cooker will convert .sbs to .sbsar
   - The renderer will generate texture maps
   - Images are automatically loaded as ComfyUI tensors

### Parameter Variation Workflow
1. **Add Parameter Controller Node**
   - Connect to your .sbsar file
   - Enable randomization or set specific parameters
   - Use JSON format for parameter overrides

2. **Connect to Renderer**
   - Use the parameter output to control rendering
   - Generate multiple variations with different seeds

### Batch Processing Workflow
1. **Add Batch Processor Node**
   - Set input directory containing .sbs files
   - Configure operation mode (cook, render, or both)
   - Set parameter variations for multiple outputs

2. **Monitor Progress**
   - Check batch summary for processing status
   - Review error log for any failed operations

## Node Reference

### Substance Cooker
Converts Substance Designer .sbs files to .sbsar archives.

**Inputs:**
- `sbs_file_path` (STRING): Path to input .sbs file
- `output_directory` (STRING): Directory for output .sbsar file
- `output_name` (STRING, optional): Custom output filename
- `optimization_level` (INT): Cooking optimization (0-3)
- `enable_icons` (BOOLEAN): Include graph icons
- `merge_graphs` (BOOLEAN): Merge all graphs into one file
- `verbose` (BOOLEAN): Enable detailed logging

**Outputs:**
- `sbsar_file_path` (STRING): Path to generated .sbsar file
- `cooking_log` (STRING): Command output and logs
- `output_directory` (STRING): Actual output directory used

### Substance Renderer
Renders .sbsar files to texture maps with full control over output settings and support for dynamic image inputs.

**Inputs:**
- `sbsar_file_path` (STRING): Path to input .sbsar file
- `output_directory` (STRING): Directory for texture outputs
- `output_format` (COMBO): Image format (PNG, TIFF, EXR, JPG, TGA, HDR)
- `bit_depth` (COMBO): Bit depth (8, 16, 16f, 32f)
- `output_name` (STRING, optional): Custom output name pattern
- `graph_selection` (STRING, optional): Specific graph to render
- `output_selection` (STRING, optional): Specific outputs to render
- `parameters` (STRING): JSON parameter overrides
- `preset_name` (STRING, optional): Preset to apply
- `cpu_count` (INT): Maximum CPU cores (0 = auto)
- `memory_budget` (INT): Memory limit in MB
- `resolution` (INT): Output texture resolution (256-4096, default: 1024)
- `return_images` (BOOLEAN): Load images as ComfyUI tensors
- `verbose` (BOOLEAN): Enable detailed logging
- `input_image_1` (IMAGE, optional): First input image for material parameters
- `input_image_1_param` (STRING): Parameter name for input_image_1
- `input_image_2` (IMAGE, optional): Second input image for material parameters
- `input_image_2_param` (STRING): Parameter name for input_image_2
- `input_image_3` (IMAGE, optional): Third input image for material parameters
- `input_image_3_param` (STRING): Parameter name for input_image_3
- `input_image_4` (IMAGE, optional): Fourth input image for material parameters
- `input_image_4_param` (STRING): Parameter name for input_image_4

**Outputs:**
- `texture_paths` (STRING): JSON list of generated texture paths
- `texture_images` (IMAGE): ComfyUI image tensors
- `organized_outputs` (STRING): JSON organized by texture type
- `render_log` (STRING): Command output and logs
- `output_directory` (STRING): Actual output directory used

**Image Input Feature:**
The Substance Renderer now supports dynamic image inputs from ComfyUI workflows. You can connect generated images, processed textures, or any ComfyUI IMAGE output to the input_image slots and specify the corresponding Substance parameter names. This enables dynamic material creation where AI-generated content can be used as input textures for procedural materials.

### Substance Parameter Controller
Controls and manipulates Substance material parameters for variation generation.

**Inputs:**
- `sbsar_file_path` (STRING): Path to input .sbsar file
- `parameter_overrides` (STRING): JSON parameter name-value pairs
- `preset_name` (STRING, optional): Preset name to apply
- `random_seed` (INT): Seed for randomization (-1 for random)
- `randomize_parameters` (BOOLEAN): Enable parameter randomization
- `randomization_strength` (FLOAT): Randomization intensity (0.0-1.0)
- `extract_info` (BOOLEAN): Extract material information

**Outputs:**
- `parameter_json` (STRING): Final parameter values as JSON
- `applied_parameters` (STRING): Complete parameter application info
- `material_info` (STRING): Extracted material metadata
- `preset_info` (STRING): Applied preset information

### Substance Batch Processor
Processes multiple Substance files or generates multiple variations efficiently.

**Inputs:**
- `input_directory` (STRING): Directory containing input files
- `output_base_directory` (STRING): Base output directory
- `operation_mode` (COMBO): Processing mode (cook_only, render_only, cook_and_render)
- `file_pattern` (STRING): File filtering pattern (default: "*.sbs")
- `batch_parameters` (STRING): JSON array of parameter sets
- `output_format` (COMBO): Output image format
- `bit_depth` (COMBO): Output bit depth
- `optimization_level` (INT): Cooking optimization level
- `max_workers` (INT): Maximum parallel workers
- `organize_by_material` (BOOLEAN): Organize outputs by material name
- `verbose` (BOOLEAN): Enable detailed logging

**Outputs:**
- `processed_files` (STRING): JSON list of processing results
- `batch_summary` (STRING): Processing statistics and summary
- `error_log` (STRING): JSON list of any errors encountered
- `output_structure` (STRING): JSON organization of output files

### Substance Info Extractor
Extracts comprehensive metadata and parameter information from .sbsar files.

**Inputs:**
- `sbsar_file_path` (STRING): Path to input .sbsar file
- `extract_parameters` (BOOLEAN): Extract parameter information
- `extract_outputs` (BOOLEAN): Extract output information
- `extract_graphs` (BOOLEAN): Extract graph information
- `format_output` (BOOLEAN): Format JSON for readability
- `verbose` (BOOLEAN): Enable detailed logging

**Outputs:**
- `file_info` (STRING): Basic file information as JSON
- `graph_info` (STRING): Graph metadata as JSON
- `parameter_info` (STRING): Parameter definitions as JSON
- `output_info` (STRING): Output channel information as JSON
- `formatted_summary` (STRING): Human-readable summary

## Advanced Usage

### Parameter Control
Parameters can be controlled using JSON format in the Parameter Controller or Renderer nodes:

```json
{
  "basecolor_r": 0.8,
  "basecolor_g": 0.6,
  "basecolor_b": 0.4,
  "roughness": 0.7,
  "metallic": 0.0,
  "tiling": 2.0,
  "random_seed": 42
}
```

### Batch Parameter Variations
For batch processing with multiple parameter sets:

```json
[
  {
    "roughness": 0.2,
    "metallic": 0.9,
    "random_seed": 1
  },
  {
    "roughness": 0.8,
    "metallic": 0.1,
    "random_seed": 2
  },
  {
    "roughness": 0.5,
    "metallic": 0.5,
    "random_seed": 3
  }
]
```

### Output Organization
The renderer automatically organizes outputs by texture type:
- **diffuse**: Albedo/base color maps
- **normal**: Normal maps
- **roughness**: Roughness maps
- **metallic**: Metallic maps
- **height**: Height/displacement maps
- **ambient_occlusion**: AO maps
- **emission**: Emissive maps
- **opacity**: Alpha/transparency maps

## Performance Optimization

### Memory Management
- Set appropriate `memory_budget` values based on your system
- Use lower bit depths (8-bit) for faster processing when high precision isn't needed
- Enable caching to avoid reprocessing unchanged files

### Parallel Processing
- Adjust `max_workers` in batch processing based on your CPU cores
- Consider I/O limitations when setting high worker counts
- Monitor system resources during large batch operations

### Optimization Levels
- **Level 0**: Fastest cooking, larger file sizes
- **Level 1**: Balanced performance and size (recommended)
- **Level 2**: Better compression, slower cooking
- **Level 3**: Maximum compression, slowest cooking

## Troubleshooting

### Common Issues

**"Tool not found" errors:**
- Verify Substance 3D Automation Toolkit is installed
- Check that tools are in your system PATH
- Manually configure tool paths in config.json

**Memory errors during rendering:**
- Reduce `memory_budget` setting
- Lower output resolution or bit depth
- Process files individually instead of batch

**Slow performance:**
- Reduce `max_workers` for batch processing
- Enable caching in configuration
- Use appropriate optimization levels

**Parameter errors:**
- Verify JSON syntax in parameter inputs
- Check parameter names match those in the .sbsar file
- Use Info Extractor to discover available parameters

### Logging and Debugging
Enable verbose logging in any node to get detailed information about the processing steps. Logs include:
- Command line arguments used
- Processing times
- File paths and sizes
- Error details and stack traces

### Getting Help
1. Check the error logs for specific error messages
2. Verify your Substance files work with the command line tools directly
3. Test with simple workflows before complex batch operations
4. Review the configuration settings for any conflicts

## Examples and Workflows

See the `examples/` directory for complete workflow examples:
- `basic_cooking.json`: Simple .sbs to .sbsar conversion
- `material_rendering.json`: Complete material rendering workflow
- `parameter_variations.json`: Generating material variations
- `batch_processing.json`: Processing multiple materials
- `advanced_pipeline.json`: Complex multi-step workflow

## Contributing

Contributions are welcome! Please see the development documentation for:
- Code style guidelines
- Testing procedures
- Submission process

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Acknowledgments

- Adobe for the Substance 3D Automation Toolkit
- ComfyUI community for the excellent framework
- Contributors and testers who helped improve this plugin

## Version History

### v1.0.0 (Current)
- Initial release with core functionality
- Support for cooking, rendering, and parameter control
- Batch processing capabilities
- Comprehensive error handling and logging

