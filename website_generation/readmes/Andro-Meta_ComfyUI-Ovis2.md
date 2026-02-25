# ComfyUI-Ovis2

A ComfyUI custom node set for integrating [Ovis2](https://huggingface.co/AIDC-AI/Ovis2-34B), a powerful multimodal large language model designed to analyze images and videos.

## Features

- **Image Captioning**: Generate detailed descriptions of images
- **Multi-Image Analysis**: Compare and analyze up to 4 images simultaneously
- **Video Description**: Process video frames for scene understanding
- **Auto-Download**: Automatically download models from Hugging Face
- **Multiple Models**: Support for all Ovis2 model sizes (1B to 34B parameters)

## Installation

### Option 1: Using ComfyUI Manager (Recommended)

1. Install ComfyUI Manager if you haven't already
2. Open ComfyUI Manager
3. Go to "Install Custom Nodes" tab
4. Click "Install from Git URL"
5. Enter the GitHub repository URL
6. Click Install

### Option 2: Manual Installation

1. Navigate to your ComfyUI installation folder
2. Go to the `custom_nodes` directory (create it if it doesn't exist)
3. Clone this repository:
   ```bash
   git clone https://github.com/Andro-Meta/ComfyUI-Ovis2.git
   ```
4. Install the required dependencies:
   ```bash
   pip install -r custom_nodes/ComfyUI-Ovis2/requirements.txt
   ```
5. Restart ComfyUI

## Dependencies

- transformers>=4.46.2
- huggingface-hub>=0.23.0
- torch>=2.4.0
- pillow>=10.3.0
- flash-attn>=2.7.0
- numpy>=1.25.0

## Usage

After installation, you'll find four new nodes in the "Ovis2" category:

### Load Ovis2 Model

Loads the Ovis2 model with configurable settings:
- `model_name`: Choose which Ovis2 model to load
- `precision`: Set numerical precision
- `max_token_length`: Maximum context length
- `device`: Choose CPU or CUDA for inference
- `auto_download`: Enable or disable automatic model downloading

### Ovis2 Image Caption

Generates detailed descriptions of images:
- `model`: Connect to the Ovis2 model
- `image`: Connect to an image input
- `prompt`: Instructions for the model
- `max_new_tokens`: Maximum length of generated text
- `temperature`: Controls randomness

### Ovis2 Multi-Image Analysis

Analyzes multiple images together:
- Supports up to 4 images simultaneously
- Great for comparison or sequence analysis

### Ovis2 Video Frames Description

Processes video frames:
- Works with ComfyUI's standard video frame output format
- Controls for frame_skip and max_frames to handle longer videos

## Example Workflows

### Basic Image Captioning

1. Add a "Load Image" node and select an image
2. Add a "Load Ovis2 Model" node and choose your preferred model size
3. Add an "Ovis2 Image Caption" node
4. Connect:
   - The image output to the "image" input on the caption node
   - The model output to the "model" input on the caption node
5. Run the workflow to generate a detailed caption

### Multi-Image Comparison

1. Load two or more images using "Load Image" nodes
2. Add a "Load Ovis2 Model" node
3. Add an "Ovis2 Multi-Image Analysis" node
4. Connect:
   - The model output to the "model" input
   - Each image to the corresponding image inputs
   - Set a prompt like "Compare these images and describe their similarities and differences"
5. Run the workflow to get a comparative analysis

## Model Storage

Models are stored in the `models/ovis` directory inside your ComfyUI installation. The nodes will automatically create this directory if it doesn't exist.

## Troubleshooting

### Memory Issues

If you encounter CUDA out of memory errors, try:
- Using a smaller model (Ovis2-1B or Ovis2-2B)
- Reducing the image size before processing
- Switching to "float16" precision
- Reducing max_token_length

### Model Loading Errors

- Check if auto_download is enabled
- Ensure you have a proper internet connection during first run
- Check if the model files are already downloaded to the correct location

### Import Errors

- Verify that all dependencies are correctly installed
- Check the ComfyUI console for specific error messages

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [AIDC-AI](https://huggingface.co/AIDC-AI) for creating the Ovis2 models
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for the amazing stable diffusion interface
