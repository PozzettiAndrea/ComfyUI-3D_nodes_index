# ComfyUI-FaceCalloutNode

A collection of custom nodes for ComfyUI that provide advanced face callout, annotation, and compositing effects using OpenCV and PIL. These nodes are designed for image processing workflows that require face detection, annotation, and creative compositing.

## Nodes Overview

### 1. FaceCalloutNode
- **Purpose**: Detects a face in an input image and draws an annotated callout (circle) around it, with a customizable Bezier-curved line and arrow connecting the face to the callout.
- **Key Features**:
  - Face detection using OpenCV Haar Cascades.
  - Highly configurable callout position, scale, border, and colors.
  - Customizable Bezier curve for annotation lines with arrowheads.
  - Flexible handling for images with no or multiple faces.
- **Inputs**:
  - Image (torch.Tensor)
  - Face padding, callout scale, position, border thickness/color, line color/thickness, Bezier control factors, arrowhead size, fallback and multiple face behaviors.
- **Output**: Annotated image with callout effect.

### 2. IsolatedFaceCalloutNode
- **Purpose**: Detects and crops a face from an input image, placing it inside a circular callout with optional border, and outputs the result as a transparent PNG (RGBA).
- **Key Features**:
  - Face detection and cropping with padding.
  - Generates a circular callout with optional border color and thickness.
  - Handles images with no faces (blank fallback or error).
  - Supports selection of first or largest face if multiple are detected.
- **Inputs**:
  - Source image (torch.Tensor)
  - Face padding, callout scale, border thickness/color, fallback, and multiple face behavior.
- **Output**: RGBA image with isolated face callout.

### 3. IntegratedFaceCompositeNode
- **Purpose**: Integrates the isolated face callout into a background image, allowing for precise placement, scaling, and compositing.
- **Key Features**:
  - Uses IsolatedFaceCalloutNode logic internally to generate the face callout.
  - Composites the callout onto a background image at a configurable position, scale, and pivot.
  - Handles fallback behaviors if no face is detected.
- **Inputs**:
  - Background image, source image for face (torch.Tensor)
  - Face padding, callout scale, border thickness/color, position, composite scale, pivot, fallback, and multiple face behavior.
- **Output**: Composited image with face callout overlay.

## Common Features
- All nodes use OpenCV's Haar Cascade for robust face detection (`haarcascade_frontalface_default.xml` included).
- Helper functions for tensor ↔ PIL image conversion.
- Designed for easy integration into ComfyUI workflows.

## Installation
1. Place this folder (`ComfyUI-FaceCalloutNode`) in your `ComfyUI/custom_nodes/` directory.
2. Ensure dependencies are installed:
   - `torch`, `numpy`, `Pillow`, `opencv-python`
3. Restart ComfyUI. The nodes will be auto-registered.

## Node Registration
Nodes are registered in `__init__.py` as follows:
- `FaceCalloutEffect`: FaceCalloutNode
- `IsolatedFaceCallout`: IsolatedFaceCalloutNode
- `IntegratedFaceComposite`: IntegratedFaceCompositeNode

## Example Usage
- **FaceCalloutNode**: Annotate faces in images for presentations or documentation.
- **IsolatedFaceCalloutNode**: Create cut-out face callouts for compositing or avatars.
- **IntegratedFaceCompositeNode**: Overlay isolated face callouts onto backgrounds for creative effects or collages.

## Example Workflow

![Example Workflow Preview](example_workflows/example_workflows.png)

## File Structure
- `FaceCalloutNode.py`: Main callout annotation node.
- `IsolatedFaceCalloutNode.py`: Node for extracting and formatting isolated face callouts.
- `IntegratedFaceCompositeNode.py`: Node for compositing face callouts onto backgrounds.
- `haarcascade_frontalface_default.xml`: Haar Cascade model for face detection.
- `__init__.py`: Registers all nodes for ComfyUI.

## Credits
- Built using [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- Face detection via OpenCV Haar Cascades

## License
MIT License (or specify your own)

---
For more details, see the code comments in each file.
