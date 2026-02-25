# ComfyUI-AmazonBedrock

A ComfyUI custom node package that integrates Amazon Bedrock's AI models for text generation, image generation, and video generation workflows.

## Overview

This extension provides ComfyUI nodes to leverage Amazon Bedrock's powerful AI models including:
- **LLM Models**: Claude (text generation and multimodal)
- **Image Models**: SDXL, Nova Canvas (text-to-image, image variations)
- **Video Models**: Nova Reel (video generation)

## Features

### Text Generation Nodes
- **Bedrock - Claude**: Text generation using Claude models
- **Bedrock - Claude Multimodal**: Multimodal text generation with image input support
- **Bedrock - Nova**: Amazon Nova multimodal text generation

### Image Generation Nodes
- **Bedrock - SDXL**: Stable Diffusion XL image generation
- **Amazon Bedrock - Nova Canvas Generate Image**: Text-to-image generation using Nova Canvas
- **Amazon Bedrock - Nova Canvas Generate Variations**: Generate image variations using Nova Canvas

### Video Generation Nodes
- **Amazon Bedrock - Nova Reel Video**: Video generation using Nova Reel

## Prerequisites

### AWS Setup
1. **AWS Account**: You need an active AWS account with access to Amazon Bedrock
2. **AWS Credentials**: Configure your AWS credentials using one of these methods:
   - AWS CLI: `aws configure`
   - Environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`
   - IAM roles (if running on EC2)

3. **Bedrock Model Access**: Request access to the required models in the Amazon Bedrock console:
   - Claude models (Anthropic)
   - Nova models (Amazon)
   - Stable Diffusion XL (Stability AI)

### Python Dependencies
The following Python packages are required:
```
boto3
requests
retry
PIL (Pillow)
numpy
torch
```

## Installation

1. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-repo/ComfyUI-AmazonBedrock.git
```

2. Install the required dependencies:
```bash
pip install boto3 requests retry pillow numpy torch
```

3. Restart ComfyUI

## Configuration

### AWS Region
Make sure your AWS region supports the Bedrock models you want to use. Popular regions include:
- `us-east-1` (N. Virginia)
- `us-west-2` (Oregon)
- `eu-west-1` (Ireland)

### Model IDs
The nodes support various model IDs including:
- `amazon.nova-pro-v1:0`
- `amazon.nova-lite-v1:0`
- `anthropic.claude-3-sonnet-20240229-v1:0`
- `anthropic.claude-3-haiku-20240307-v1:0`
- `stability.stable-diffusion-xl-v1`

## Usage

### Text Generation
1. Add a "Bedrock - Claude" or "Bedrock - Nova" node to your workflow
2. Configure the model ID, prompt, and generation parameters
3. Connect the output to other nodes as needed

### Image Generation
1. Add a "Amazon Bedrock - Nova Canvas Generate Image" node
2. Provide a text prompt describing the desired image
3. Configure generation parameters (dimensions, quality, etc.)
4. Connect the output image to your workflow

### Video Generation
1. Add a "Amazon Bedrock - Nova Reel Video" node
2. Provide a text prompt or input image
3. Configure video parameters (duration, dimensions)
4. The node will generate and save the video locally

## Node Parameters

### Common Parameters
- **model_id**: The Amazon Bedrock model identifier
- **prompt**: Input text prompt
- **maxTokens**: Maximum number of tokens to generate
- **temperature**: Controls randomness (0.0 = deterministic, 1.0 = very random)
- **topP**: Nucleus sampling parameter

### Image-Specific Parameters
- **width/height**: Output image dimensions
- **cfgScale**: Classifier-free guidance scale
- **seed**: Random seed for reproducible results
- **numberOfImages**: Number of images to generate

### Video-Specific Parameters
- **durationSeconds**: Video duration
- **fps**: Frames per second
- **dimension**: Video resolution

## Troubleshooting

### Common Issues

1. **AWS Credentials Not Found**
   - Ensure AWS credentials are properly configured
   - Check AWS CLI configuration: `aws sts get-caller-identity`

2. **Model Access Denied**
   - Request access to the specific models in the Amazon Bedrock console
   - Wait for approval (can take a few minutes to hours)

3. **Region Not Supported**
   - Check if your AWS region supports the Bedrock models you're trying to use
   - Switch to a supported region if necessary

4. **Import Errors**
   - Ensure all required Python packages are installed
   - Check ComfyUI console for specific error messages

### Error Messages
Check the ComfyUI console for detailed error messages. The nodes include retry logic and comprehensive error handling.

## Cost Considerations

Amazon Bedrock charges based on:
- **Text models**: Per input/output token
- **Image models**: Per generated image
- **Video models**: Per second of generated video

Monitor your usage in the AWS console and set up billing alerts to avoid unexpected charges.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review AWS Bedrock documentation
3. Open an issue on the GitHub repository

## Changelog

### Latest Updates
- Added Nova Reel video generation support
- Enhanced error handling and retry logic
- Improved multimodal capabilities
- Added support for latest Nova models
