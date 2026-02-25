# ComfyUI-ZSNodes

Custom nodes for ComfyUI with specialized image processing and saving functionality.

## Features

### 1. Save Image (ZS Custom)
A custom save image node that provides direct control over filenames:
- **Direct Filename Control**: Uses `filename_prefix` directly as the filename without auto-incrementing counters
- **Minimal Batch Numbering**: Only adds numbers (_001, _002, etc.) when saving multiple images
- **Metadata Preservation**: Maintains ComfyUI metadata (prompt, workflow info) in saved images
- **Caption Support**: Can save text captions alongside images
- **Flexible Output Paths**: Supports both relative and absolute output folders

### 2. Bounding Box Crop (ZS)
A powerful text-based object detection and cropping node using GroundingDINO:
- **Text-based Detection**: Detect objects using natural language descriptions
- **Two Output Modes**:
  - **Crop Mode**: Extract detected objects from the image
  - **Paint Mode**: Paint out everything except detected objects
- **Multiple Detection Modes**:
  - **First**: Use first detection
  - **Best**: Use highest confidence detection
  - **All**: Process all detections separately
  - **Merge**: Combine all detections into one
- **Adjustable Padding**: Add padding around detected objects
- **Custom Paint Color**: Choose background color for paint mode
- **Batch Processing**: Process multiple images efficiently
- **Visual Feedback**: Shows bounding boxes on original image
- **Mask Output**: Provides binary masks for detected regions

## Key Differences from Default Save Image

The default ComfyUI Save Image node automatically adds counters and batch numbers to filenames, which can be undesirable when you want predictable, specific filenames. This custom node:

1. Uses your exact `filename_prefix` as the filename (with .png extension)
2. Only adds batch numbers when processing multiple images in a single batch
3. Doesn't maintain a persistent counter across saves

## Installation

### Method 1: ComfyUI Manager (Recommended)
If you have ComfyUI Manager installed, search for "ComfyUI-ZSNodes" and install directly through the manager interface.

### Method 2: Manual Installation

1. Navigate to your ComfyUI custom_nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ComfyUI-ZSNodes
   ```

3. Install dependencies:
   ```bash
   cd ComfyUI-ZSNodes
   pip install -r requirements.txt
   ```
   
   **For Windows Portable ComfyUI**, use the embedded Python:
   ```cmd
   ..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
   ```

4. Restart ComfyUI

**Note**: ComfyUI will often automatically install missing dependencies from requirements.txt when you first load the nodes.

## Usage

### Save Image (ZS Custom)
Appears in the `zsnodes/image` category.

#### Inputs
- **images**: The images to save
- **filename_prefix**: Used directly as the filename (without counter)
- **output_folder**: Folder to save images (relative to ComfyUI output or absolute path)
- **caption** (optional): Text to save as a .txt file alongside the image
- **caption_file_extension** (optional): Extension for caption files (default: .txt)

#### Outputs
- **filename**: The filename of the saved image

#### Example Usage
- Single image with `filename_prefix="my_image"` → saves as `my_image.png`
- Batch of 3 images with `filename_prefix="batch"` → saves as `batch_000.png`, `batch_001.png`, `batch_002.png`

### Bounding Box Crop (ZS)
Appears in the `zsnodes/image` category.

#### Inputs
- **image**: Input image to process
- **prompt**: Text description of object to detect (e.g., "person", "car", "red apple")
- **dino_model**: Choose GroundingDINO model:
  - **GroundingDINO_SwinT_OGC (694MB)**: Faster, smaller model
  - **GroundingDINO_SwinB (938MB)**: Better accuracy
- **output_mode**: "Crop" or "Paint"
- **device**: Auto/CPU/GPU selection
- **threshold**: Detection confidence threshold (0.05-0.95, default: 0.35)
- **crop_mode**: How to handle multiple detections
- **padding**: Pixels to add around bounding box
- **paint_color**: Background color for paint mode (hex format)

#### Outputs
- **OUTPUT_IMAGE**: Cropped regions or painted image
- **ORIGINAL_WITH_BOXES**: Original image with bounding boxes drawn
- **BBOX_INFO**: Text information about detected boxes
- **MASK**: Binary mask of detected regions

#### Example Usage
- Detect and crop "person" from an image
- Paint out background keeping only "cat" visible
- Extract all "car" objects from a street scene

## Extending the Node Pack

To add more custom nodes to this pack:

1. Create a new Python file in the `nodes/` directory
2. Define your node class with ComfyUI's required structure
3. Import and register it in `nodes/__init__.py`:
   ```python
   from .your_new_node import YourNewNode
   
   NODE_CLASS_MAPPINGS = {
       "ZS_SaveImage": CustomSaveImage,
       "ZS_YourNewNode": YourNewNode,
   }
   ```

## Structure

```
ComfyUI-ZSNodes/
├── __init__.py              # Main package initialization
├── nodes/                   # Node implementations
│   ├── __init__.py         # Node registration
│   ├── custom_save_image.py # Custom save image implementation
│   └── bounding_box_crop.py # Text-based object detection and cropping
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Dependencies

- **Basic Requirements**: Pillow, numpy (required for all nodes)
- **For Bounding Box Crop**: PyTorch, torchvision, opencv-python, huggingface-hub, protobuf, GroundingDINO (optional)
  
**Notes:**
- ComfyUI will automatically try to install missing dependencies from `requirements.txt`
- GroundingDINO models (694MB or 938MB) will be automatically downloaded on first use
- If GroundingDINO installation fails, the Save Image node will still work, but Bounding Box Crop will be unavailable

## License

[Your preferred license]

## Contributing

Feel free to submit issues and pull requests.