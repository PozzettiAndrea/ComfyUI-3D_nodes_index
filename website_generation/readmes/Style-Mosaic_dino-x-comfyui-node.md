# ComfyUI DINO-X Detector Node

A ComfyUI node that integrates DINO-X API for object detection and segmentation. This node allows you to detect and segment objects in images using text prompts.

## Features

- Text prompt-based object detection
- Bounding box visualization
- Instance segmentation masks
- Configurable detection threshold
- Support for multiple objects per image
- Real-time visualization

## Installation

1. Get your DINO-X API token:
   - Visit [DeepDataSpace](https://cloud.deepdataspace.com/apply-token?from=github)
   - Register and request an API token
   - Save your token for use with the node

2. Install the node in your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui-dinox-detector
cd comfyui-dinox-detector
pip install -e .
```

## Usage

1. In ComfyUI, find the "DINO-X Object Detector" node under the "detection" category

2. Connect your inputs:
   - image: The input image to process
   - text_prompt: Text description of objects to detect (e.g. "wheel . eye . helmet")
   - api_token: Your DINO-X API token
   - bbox_threshold: Detection confidence threshold (0.0-1.0)

3. The node outputs:
   - box_annotated: Image with bounding boxes and labels
   - mask_annotated: Image with instance segmentation masks

## Example Workflow

1. Load Image → DINO-X Object Detector → Preview Image
```json
{
  "3": {
    "class_type": "LoadImage",
    "inputs": {
      "image": "example.jpg"
    }
  },
  "4": {
    "class_type": "DinoxDetector",
    "inputs": {
      "image": ["3", 0],
      "text_prompt": "person . car . dog . cat . bird",
      "api_token": "your-api-token-here",
      "bbox_threshold": 0.25
    }
  },
  "5": {
    "class_type": "PreviewImage",
    "inputs": {
      "images": ["4", 0]
    }
  },
  "6": {
    "class_type": "PreviewImage",
    "inputs": {
      "images": ["4", 1]
    }
  }
}
```

## Development

### Running Tests

1. Install development dependencies:
```bash
pip install -e ".[dev]"
```

2. Run the tests:
```bash
pytest dinox_detector/test_node.py -v
```

The tests cover:
- Input validation
- API interaction (mocked)
- Real-world image testing
- Image processing
- Error handling

### Test Assets

The test suite includes:
- Synthetic test images for basic functionality testing
- Real-world test image (leather jacket) for realistic detection scenarios

Test assets are stored in the `test_assets` directory.

## License

This node is released under the Apache 2.0 license. See LICENSE file for details.
