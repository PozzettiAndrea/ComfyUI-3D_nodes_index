# ComfyUI Face Detection Node

A ComfyUI custom node for face detection and cropping using OpenCV Haar cascades, with full ComfyUI v3 schema support and backward compatibility.

![Face Detection Output Example](images/combined_strip.jpg)
![Face Detection Output Example](images/comfyui_face_detection_node.png)

## Features

- **Face Detection**: Uses OpenCV Haar cascade classifiers for robust face detection
- **Flexible Cropping**: Crop largest face or all detected faces
- **Adjustable Parameters**: Configurable detection threshold, minimum face size, and padding
- **Multiple Classifiers**: Choose between default and alternative Haar cascades
- **ComfyUI v3 Ready**: Full schema support with backward compatibility for v1/v2
- **Async Execution**: Stateless execution pattern for better performance

## Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Face Detection Node"
3. Click Install

### Manual Installation
1. Navigate to your ComfyUI custom nodes directory
2. Clone this repository:
   ```bash
   git clone https://github.com/Limbicnation/ComfyUI_FaceDetectionNode.git
   cd ComfyUI_FaceDetectionNode
   pip install -r requirements.txt
   ```

## Usage

1. Add the "Face Detection and Crop" node to your workflow
2. Connect an image input
3. Adjust parameters:
   - **Detection Threshold**: Confidence threshold (0.1-1.0)
   - **Min Face Size**: Minimum face size in pixels (32-512)
   - **Padding**: Padding around detected faces (0-256)
   - **Output Mode**: "largest_face" or "all_faces"
   - **Face Output Format**: "strip" (horizontal layout) or "individual" (separate batch items)
   - **Classifier Type**: "default" or "alternative"

## Parameters

| Parameter | Type | Range | Default | Description |
|-----------|------|-------|---------|-------------|
| detection_threshold | Float | 0.1-1.0 | 0.8 | Face detection confidence threshold |
| min_face_size | Int | 32-512 | 64 | Minimum size for detected faces |
| padding | Int | 0-256 | 32 | Padding around detected faces |
| output_mode | Combo | - | largest_face | Output mode for detected faces |
| face_output_format | Combo | - | strip | Format for multiple faces (strip/individual) |
| classifier_type | Combo | - | default | Haar cascade classifier type |

## Compatibility

- **ComfyUI v3**: Full schema support with async execution
- **ComfyUI v1/v2**: Backward compatibility via wrapper class
- **Auto-detection**: Automatically selects appropriate implementation

## Requirements

- Python ≥ 3.8
- OpenCV ≥ 4.5.0
- PyTorch ≥ 1.9.0
- NumPy ≥ 1.21.0
- Pillow ≥ 8.0.0

## License

Apache License Version 2.0, January 2004 - see LICENSE file for details.
