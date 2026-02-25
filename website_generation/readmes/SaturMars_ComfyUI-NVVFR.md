# ComfyUI-NVVFR

ComfyUI node for video super-resolution and frame interpolation using NVEncC.

[中文版本](README_ZH.md) | English Version

## Features

- Video encoding and prsuper-resolution and frame interpolation using NVEncC
- Support for H.264/H.265 encoding
- Super-resolution processing support
- Frame rate conversion support (double frame rate)
- Support for 8bit/10bit color depth

## Installation

1. Download the NVIDIA Video Effects SDK for your graphics card:
   - Go to https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/
   - Download the Video Effects SDK corresponding to your graphics card
   - Supports NVIDIA 20 series graphics cards and above
2. Copy this folder to the `custom_nodes` directory of ComfyUI or use git clone command.
3. Download the NVEnc binary dependencies:
   - Go to the [NVEnc Releases page](https://github.com/rigaya/NVEnc/releases)
   - Download the x64 version
   - Extract the contents to the `nvenc` folder in this node directory
   - Like this `ComfyUI\custom_nodes\ComfyUI-NVVFR\nvenc`
4. Restart ComfyUI
5. Find the "NVVFR Video Processor" node in the node list

## Usage

1. Add the "NVVFR Video Processor" node to your workflow
2. Set the input video path
3. Configure output parameters:
   - Output prefix: Output file name prefix
   - Encoder: H.264 or H.265
   - Quality: High, Medium, Low
   - Super-resolution: Enable/Disable, adjustable intensity
   - Double frame rate: Enable/Disable frame rate conversion
   - Output resolution: Set width and height
   - Color depth: 8bit or 10bit
4. Run the node, wait until finish.

## Parameter Description

### Input Parameters

- **video_path**: Input video file path
- **output_prefix**: Output file name prefix
- **codec**: Video encoder (H.264/H.265)
- **quality**: Encoding quality (high/medium/low)
- **enable_superres**: Whether to enable super-resolution
- **superres_strength**: Super-resolution strength (0.0-1.0)
- **enable_double_frame**: Whether to enable double frame interpolation
- **width**: Output video width
- **height**: Output video height
- **depth**: Color depth (8bit/10bit)

### Output Parameters

- **video_path**: Output video file path

## Notes

1. Ensure NVEncC is installed on the system and included in the nvenc folder
2. H.264 encoder does not support 10bit color depth, will automatically downgrade to 8bit
3. Output files are saved in the ComfyUI output directory

## Troubleshooting

### Encoding failed

1. Confirm that NVEncC64.exe file exists in the nvenc folder
2. Check if the input video file exists and is readable
3. View error information in the console output
4. GPU MUST ABOVE NVIDIA RTX 20 Series

## Changelog

### v1.0.0
- Initial version release
- Basic video processing functionality
- Support for super-resolution and double frame interpolation

## Acknowledgments

This project is based on the [NVEnc](https://github.com/rigaya/NVEnc) project, thanks to rigaya for providing the powerful video encoding and processing tools.

## License

This project follows the MIT license.
