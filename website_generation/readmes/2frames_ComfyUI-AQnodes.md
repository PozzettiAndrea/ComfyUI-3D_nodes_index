# ComfyUI-AQnodes

A collection of custom nodes for ComfyUI that enhance your workflow with additional functionality for image processing, AI model integration, and API interactions.

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-AQnodes.git
```

2. Install the required dependencies:
```bash
cd ComfyUI-AQnodes
pip install -r requirements.txt
```

## Available Nodes

### Image Processing Nodes

#### AQ_MasksAndImagesAsList
- **Purpose**: Combines multiple masks and images into a list format for loop processing
- **Use Case**: When you need to process multiple images with masks and send them to AQ_multiface_ApplyPulidFlux node
- **Example**: Combining multiple segmentation masks for batch image processing

#### AQ_multiface_ApplyPulidFlux
- **Purpose**: Applies PULID effects to multiple faces in an image
- **Example**: Feed with multiple images and masks from AQ_MasksAndImagesAsList node

### Transformer Model Nodes

#### AQ_QwenLoader
- **Purpose**: Loads the Qwen transformer model for text (with vision) generation and processing
- **Use Case**: When you need to initialize the Qwen model for text-based operations (extract image feautures and transform them into something new)
- **Example**: Setting up Qwen for text generation or image analysis tasks

#### AQ_Qwen
- **Purpose**: Interfaces with the Qwen transformer model for text generation (with vision) and processing
- **Use Case**: Text generation, completion, or image analysis using the Qwen model
- **Example**: Generating descriptions for images or creating creative text content (extract image feautures and transform them into something new)

### API Integration Nodes

#### AQ_Gemini
- **Purpose**: Integrates with Google's Gemini AI model through its API
- **Use Case**: When you need advanced AI capabilities provided by Gemini
- **Example**: Using Gemini for complex text generation or analysis tasks (extract image feautures and transform them into something new)
- **Note**: Requires API key configuration

#### AQ_SendImageToAPI
- **Purpose**: Sends images to specified API endpoints
- **Use Case**: When you need to integrate with external image processing services or don't want to pool comfy to see if generation is ready (when using api) 
- **Example**: Sending images for analysis, storage, or processing to external services
- **Note**: Requires API endpoint configuration

## Configuration

Some nodes may require additional configuration:

1. For API nodes (AQ_Gemini, AQ_SendImageToAPI):
   - API keys should be stored securely
   - Configure endpoint URLs as needed

2. For transformer nodes (AQ_Qwen):
   - Ensure sufficient system resources
   - Models will be downloaded automatically on first use

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See the [LICENSE](LICENSE) file for details. 