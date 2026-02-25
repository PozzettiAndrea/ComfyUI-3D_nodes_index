# ComfyUI OA 360 Clip

A ComfyUI custom node for extracting perspective views from 360° equirectangular images with an interactive drag-and-drop crop interface.

Why? Because I want to do camera shots from different angles with a consistent background. One way to do that is to generate a 360 image, then take background snips from that image. But you need to undo the curviture introduced by 360 photos, hence this extension.

Why the OA prefix? I go by "Ordinary Alan" (username: xordinary99) on the [ComfyUI Discord server](https://discord.gg/comfyui).

## Features

- **360° Image Support**: Extract perspective views from equirectangular 360° images using gnomonic projection
- **Interactive Crop Zone**: Drag and resize the crop region directly in the node preview using the projected outline
- **Visual Feedback**: See the projection outline on the input image to understand what will be extracted
- **Flexible Output Dimensions**: Set output width and height either via external inputs or through the UI widgets
- **Resizable Node**: The node can be resized to fit your workflow, and the preview scales to fit the available space

## Installation

Place this folder in your `custom_nodes` directory:

```
ComfyUI/custom_nodes/ComfyUI-OA-360-Clip/
```

Restart ComfyUI to load the extension.

## Usage

1. Add the **OA 360 Clip** node to your workflow
2. Connect a 360° equirectangular image to the `image` input
3. Run the workflow once to load the image preview
4. Adjust the crop region by:
   - **Dragging the crop outline**: Click and drag inside the projected outline to move the crop region
   - **Resizing**: Click and drag the corner handles to resize the crop region (maintains output aspect ratio)
   - **Jumping**: Click outside the crop outline to instantly move the crop center to that location
5. Set the output dimensions:
   - Use the `output_width` and `output_height` widgets in the node
   - Or connect external integer inputs to these properties
6. Run the workflow to generate the output image

## Node Properties

### Inputs

- **image**: Input 360° equirectangular image (required)
- **output_width**: Width of output image (optional, default: 1280, range: 1-8192)
- **output_height**: Height of output image (optional, default: 720, range: 1-8192)

### Outputs

- **IMAGE**: The extracted perspective view as a standard ComfyUI image tensor

## Crop Region

The crop region is controlled entirely through the interactive UI:

- **Center-based**: The crop is defined by its center point (`crop_center_x`, `crop_center_y`) and dimensions (`crop_width`, `crop_height`)
- **Maximum width**: The crop width is limited to 25% of the input image width to prevent excessive distortion
- **Wrapping**: The center point can wrap around horizontally (equirectangular images wrap at the edges)
- **Aspect ratio**: When resizing by dragging corners, the crop maintains the aspect ratio of the output dimensions

## Notes

- The crop region defines the area in the equirectangular image to extract
- The output dimensions define the final perspective view size
- The projection uses gnomonic projection, which may have distortion near the poles
- For best results, keep crop regions away from the extreme poles (±90° latitude)
- The node can be resized by dragging the bottom-right corner
- Crop values are automatically saved with the workflow

## Technical Details

- **Projection**: Gnomonic (pinhole) projection for perspective view extraction
- **Coordinate System**: Equirectangular input with spherical coordinate conversion
- **Crop Constraints**: Maximum crop width is 25% of input image width
- **State Management**: Crop values are stored in node properties and synchronized with the backend via API

## Acknowledgements

This project was inspired by the [ComfyUI-Olm-DragCrop](https://github.com/olm-comfyui/ComfyUI-Olm-DragCrop) extension, which provides an excellent interactive crop interface for ComfyUI. However, this is a clean implementation written from scratch, as the original extension's license was not permissive enough for our needs. This project was vibe coded with Cursor AI from scratch (and it took a while even then to get right!)

If you need to clip a rectangular region from a standard (non-360°) image, we recommend using the [ComfyUI-Olm-DragCrop](https://github.com/olm-comfyui/ComfyUI-Olm-DragCrop) extension instead, which is specifically designed for that use case.
