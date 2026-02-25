# ComfyUI YOLOv8 Object Detection Node

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)](https://github.com/comfyanonymous/ComfyUI)

A powerful ComfyUI custom node that performs object detection using YOLOv8 and outputs individual images for each detected object. Perfect for automatic mask generation, object isolation, and batch processing workflows.

## ✨ Features

- **Object Detection**: Uses YOLOv8 models for accurate object detection
- **Multiple Outputs**: Generates separate images for each detected object
- **Batch Processing**: Outputs a batch of images containing all detected objects
- **Customizable Parameters**: Adjustable confidence threshold, IoU threshold, and padding
- **Model Selection**: Choose from different YOLOv8 model sizes (nano to extra-large)
- **Custom Models**: Support for custom trained YOLOv8 models

## 🚀 Quick Start

### Automatic Installation

1. **Clone the repository** into your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/mangobyed/ComfyUI_Detection_List.git
   cd ComfyUI_Detection_List
   ```

2. **Run the installation script**:
   
   **Linux/Mac:**
   ```bash
   chmod +x install.sh
   ./install.sh
   ```
   
   **Windows:**
   ```cmd
   install.bat
   ```

3. **Restart ComfyUI** to load the new node.

### Manual Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Copy Files**: Place this folder in your ComfyUI `custom_nodes` directory:
   ```
   ComfyUI/custom_nodes/ComfyUI_Detection_List/
   ```

3. **Restart ComfyUI**: Restart ComfyUI to load the new node.

## Usage

### Node Inputs

- **image**: Input image for object detection
- **model_name**: YOLOv8 model to use (yolov8n.pt, yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt)
- **confidence_threshold**: Minimum confidence score for detections (0.0 - 1.0)
- **iou_threshold**: IoU threshold for non-maximum suppression (0.0 - 1.0)
- **padding**: Pixels to add around detected objects when cropping (0 - 100)
- **custom_model_path** (optional): Path to custom YOLOv8 model file

### Node Outputs

- **detected_objects**: Batch of images containing cropped detected objects
- **object_count**: Number of objects detected
- **class_names**: Comma-separated list of detected object classes
- **detection_info**: Detailed information about each detection

### Example Workflow

1. Load an image using an image loader node
2. Connect the image to the YOLOv8 Object Detection node
3. Adjust detection parameters as needed
4. Connect the outputs to:
   - Image preview nodes to see detected objects
   - Save image nodes to export results
   - Other processing nodes for further manipulation

## Model Information

### Default Models
- **yolov8n.pt**: Nano - Fastest, smallest, lowest accuracy
- **yolov8s.pt**: Small - Good balance of speed and accuracy
- **yolov8m.pt**: Medium - Better accuracy, moderate speed
- **yolov8l.pt**: Large - High accuracy, slower
- **yolov8x.pt**: Extra Large - Highest accuracy, slowest

### Custom Models
You can use custom trained YOLOv8 models by providing the path in the `custom_model_path` input.

## Parameters Guide

- **Confidence Threshold**: Lower values detect more objects but may include false positives
- **IoU Threshold**: Controls overlap tolerance for duplicate detections
- **Padding**: Adds context around detected objects in cropped images

## Troubleshooting

1. **Model Loading Issues**: Ensure ultralytics is properly installed
2. **GPU Memory**: Use smaller models (nano/small) for limited GPU memory
3. **No Detections**: Try lowering the confidence threshold
4. **Too Many False Positives**: Increase the confidence threshold

## Requirements

- ComfyUI
- PyTorch
- ultralytics
- OpenCV
- Pillow
- NumPy

See `requirements.txt` for specific version requirements.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/ComfyUI_Detection_List.git`
3. Create a feature branch: `git checkout -b feature/amazing-feature`
4. Make your changes and test them
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📝 Changelog

### v1.0.0
- Initial release
- YOLOv8 object detection support
- Batch image output functionality
- Configurable detection parameters
- Support for custom models

## 🐛 Known Issues

- Model loading may take some time on first use
- GPU memory usage depends on model size and image resolution
- Some custom models may require additional dependencies

## 💬 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/mangobyed/ComfyUI_Detection_List/issues) page
2. Create a new issue with detailed information about your problem
3. Include your ComfyUI version, Python version, and error logs

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for the YOLOv8 implementation
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for the amazing framework
- The open-source community for continuous support and contributions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note**: YOLOv8 models are subject to their respective licenses from Ultralytics.