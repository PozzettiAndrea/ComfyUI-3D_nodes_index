# ComfyUI Seed API Integration

This ComfyUI custom node provides comprehensive integration with Seed AI APIs, including both video generation (Seedance), image generation (Seedream/SeedEdit), and chat models (Seed 1.6).

## Features

### Video Generation (Seedance)
- **Text-to-Video Generation**: Create videos from text descriptions
- **Image-to-Video Generation**: Generate videos using input images as first frames
- **First+Last Frame Generation**: Create videos between two specific frames
- **Reference Images Generation**: Generate videos based on multiple reference images
- **High-Quality Pro Models**: Access to premium Seedance Pro model

### Image Generation
- **Seedream 4 Unified Generation**: Advanced image generation with dynamic multi-image inputs, batch generation, and sequential image support
- **Text-to-Image Generation**: Create high-quality images from text prompts using Seedream 3.0
- **Image-to-Image Editing**: Edit and transform existing images with text descriptions using SeedEdit 3.0
- **Frame Extraction**: Convert video URLs to individual frames for further processing

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/FloyoAI/ComfyUI-Seed-API.git
```

2. Install requirements:
```bash
cd ComfyUI-Seed-API
pip install -r requirements.txt
```

3. Configure your BytePlus API key:
   - Get your API key from: https://www.byteplus.com/
   - Edit `config.ini` and replace `<your_byteplus_api_key_here>` with your actual API key
   - Or set the environment variable: `export BYTEPLUS_API_KEY="your_key_here"`

4. Restart ComfyUI

## Available Nodes

### Video Generation Nodes (Seed/VideoGeneration)

- **Seedance Lite Text-to-Video**: Generate videos from text prompts only
  - Input: Text prompt, resolution, ratio, duration, FPS, seed, camera settings
  - Output: Video URL (STRING)
  - Use case: Create videos from scratch using descriptive text

- **Seedance Lite Image-to-Video**: Generate videos from a starting image
  - Input: Text prompt, input image, resolution, ratio, duration, FPS, seed, camera settings
  - Output: Video URL (STRING)
  - Use case: Animate static images or create videos with specific starting frames

- **Seedance Lite First+Last Frame**: Generate videos between two keyframes
  - Input: Text prompt, first frame image, last frame image, resolution, ratio, duration
  - Output: Video URL (STRING)
  - Use case: Create smooth transitions between two specific images

- **Seedance Lite Reference Images**: Generate videos using multiple reference images
  - Input: Text prompt, 2-4 reference images, resolution, ratio, duration
  - Output: Video URL (STRING)
  - Use case: Generate videos that maintain style/appearance consistency with reference materials

- **Seedance Pro Text/Image-to-Video**: High-quality video generation with end frame support
  - Input: Model selection (regular/fast), text prompt, mode selection, optional input image, optional end frame, resolution, ratio, duration
  - Output: Video URL (STRING)
  - Models: seedance-1-0-pro-250528 (supports end frame), seedance-1-0-pro-fast-251015 (faster, no end frame support)
  - Features: Automatic first+last frame detection when end frame is provided in image-to-video mode
  - Use case: Premium quality video generation for professional use

### Image Generation Nodes (Seed/ImageGeneration)

- **Seedream 4**: Unified advanced image generation node
  - Input: Text prompt, width, height, batch mode (single/parallel/sequential), batch size, up to 10 optional images, optional seed
  - Output: Generated image(s) (IMAGE)
  - Features:
    - **Dynamic image inputs**: Automatically adds/removes image inputs as you connect them (up to 10)
    - **Text-to-Image**: Generate from text when no images are connected
    - **Image-to-Image**: Single image editing mode
    - **Multi-Image Blending**: Blend 2-10 reference images together
    - **Batch Generation Modes**:
      - Single: Generate one image
      - Parallel: Generate multiple independent variations with concurrent API calls (each with random seed)
      - Sequential: Generate thematically related images in one request
  - Use case: All-in-one solution for advanced image generation workflows

- **Seedream Text-to-Image**: Generate images from text descriptions (Seedream 3.0)
  - Input: Text prompt, size selection, optional seed
  - Output: Generated image (IMAGE)
  - Use case: Create high-quality images from detailed text descriptions

- **SeedEdit Image-to-Image**: Edit and transform existing images (SeedEdit 3.0)
  - Input: Text prompt, input image, size selection, guidance scale, optional seed
  - Output: Edited image (IMAGE)
  - Use case: Modify existing images based on text instructions (change colors, add/remove objects, style transfer)

### Chat & Vision Nodes (Seed/Chat)

- **Seed 1.6 Chat**: Unified chat node with vision support and session memory
  - Input: Model selection, user message, session ID, optional system message, up to 4 images
  - Output: Response text, full conversation, session status
  - Models: seed-1-6-250615, seed-1-6-flash-250715
  - Features: Session-based conversation memory, multimodal support, external history import
  - Use case: All chat scenarios - text generation, image analysis, complex conversations

### Utility Nodes (Seed/Video)

- **Video URL to Frames**: Extract all frames from a video URL
  - Input: Video URL (STRING)
  - Output: Frame batch (IMAGE), frame count (INT), FPS (FLOAT)
  - Use case: Convert generated videos into individual frames for further image processing

## Usage Guide

### Video Generation Workflow
1. **Choose the appropriate video node** based on your input type:
   - Text only → Seedance Lite Text-to-Video or Seedance Pro (text-to-video mode)
   - Single image → Seedance Lite Image-to-Video or Seedance Pro (image-to-video mode)
   - Two images → Seedance Lite First+Last Frame or Seedance Pro (image-to-video mode with end frame)
   - Multiple references → Seedance Lite Reference Images
   - High quality → Seedance Pro (supports all modes with automatic detection)

2. **Configure parameters**:
   - **Prompt**: Describe what you want in the video
   - **Resolution**: 480p, 720p, or 1080p
   - **Ratio**: Aspect ratio (16:9, 1:1, 9:16, etc.)
   - **Duration**: 3-12 seconds

3. **Connect the output** to other nodes:
   - Use output URL directly with video preview nodes
   - Connect to "Video URL to Frames" to extract individual frames
   - Save video using external video saving nodes

### Image Generation Workflow

#### Seedream 4 (Advanced/Unified Node)
1. **Dynamic Image Inputs**:
   - Start with just one image input slot
   - Connect images and new slots automatically appear (up to 10)
   - Disconnect images and unused slots disappear
   - No images connected = Text-to-Image mode
   - 1 image = Image-to-Image mode
   - 2-10 images = Multi-Image Blending mode

2. **Batch Generation Modes**:
   - **Single**: Generate one image with specified seed (or random if -1)
   - **Parallel**: Generate multiple independent variations
     - Makes concurrent API calls for faster generation
     - Each request uses a random seed for maximum variety
     - Great for exploring different variations of the same prompt
   - **Sequential**: Generate thematically related images
     - Single API call that produces multiple related images
     - Images share a narrative or visual theme
     - Limited to 15 total images (input + output combined)

3. **Tips for Seedream 4**:
   - Use parallel mode for quick variations and comparisons
   - Use sequential mode for creating image sequences or stories
   - Specify seed for reproducibility (except in parallel mode which always uses random seeds)
   - Combine multiple reference images for complex style blending

#### Seedream 3.0 / SeedEdit 3.0
1. **For new images**: Use Seedream Text-to-Image
   - Write detailed prompts for best results
   - Experiment with different sizes for various use cases
   - Use seed values for reproducible results

2. **For image editing**: Use SeedEdit Image-to-Image
   - Load your source image
   - Describe the changes you want in the prompt
   - Adjust guidance scale (higher = more prompt adherence)
   - Size can be "adaptive" to maintain original dimensions

3. **Process results**:
   - Images output as standard ComfyUI IMAGE tensors
   - Compatible with all ComfyUI image processing nodes
   - Can be saved, edited, or used as input for video generation

### Chat & Vision Workflow
1. **Session management**:
   - **Session ID**: Use unique identifiers for different conversations (e.g., "project1", "analysis2")
   - **Session Memory**: Toggle on/off to maintain conversation context across multiple runs
   - **Clear Session**: Reset conversation memory when starting new topics

2. **Model selection**:
   - **seed-1-6-250615**: Balanced performance and quality
   - **seed-1-6-flash-250715**: Faster responses, optimized for speed

3. **Configure thinking and reasoning**:
   - **Thinking mode**: Enable for deeper reasoning (default: enabled)
   - **Reasoning effort**: Adjust computational intensity (low/medium/high)

4. **Use multimodal features**:
   - Attach up to 4 images simultaneously
   - Set image detail level (auto/high/low) based on your needs
   - High detail for analysis, low detail for simple recognition

5. **Conversation continuity**:
   - **Built-in memory**: Automatically remembers previous messages in the session
   - **External history**: Import conversations from other sources
   - **Full conversation output**: Get formatted conversation history for export/review

## Requirements

- ComfyUI
- Python 3.8+
- BytePlus API key
- Required packages (see requirements.txt)

## Key Features

- **No External Dependencies**: Base64 image conversion means no external hosting required
- **Automatic Task Polling**: Video generation waits until completion automatically
- **Comprehensive Error Handling**: Graceful degradation with detailed error messages
- **ComfyUI Integration**: 
  - Video outputs as URL strings compatible with video preview nodes
  - Image outputs as standard IMAGE tensors compatible with all image nodes
- **Flexible Sizing**: Support for various aspect ratios and resolutions
- **Seed Control**: Reproducible results with optional seed parameters

## Tips for Best Results

### Video Generation
- **Be specific in prompts**: Include details about movement, camera angles, and style
- **Use appropriate ratios**: Match your intended use case (16:9 for landscape, 9:16 for mobile, etc.)
- **Leverage reference images**: For consistent character/style appearance across videos
- **Seedance Pro model selection**: Use fast model for quicker generation, regular model when you need end frame support
- **Seedance Pro end frame support**: In image-to-video mode with regular model, connect an optional end frame to automatically enable first+last frame generation for smoother transitions

### Image Generation
- **Seedream 4 batch modes**: Use parallel for variations, sequential for thematic series
- **Dynamic inputs**: Simply connect images - slots auto-add up to 10 for multi-image blending
- **Detailed prompts work better**: Include style, lighting, composition details
- **Use SeedEdit for modifications**: Better than text-to-image for specific edits
- **Guidance scale tuning**: Start with default 5.5, increase for more prompt adherence
- **Size selection**: Use "adaptive" for SeedEdit to maintain original proportions

### Chat & Vision
- **Session management**: Use descriptive session IDs and enable memory for ongoing conversations
- **Model choice**: Use seed-1-6-flash-250715 for speed, seed-1-6-250615 for quality
- **Image detail settings**: High detail for analysis tasks, low for simple recognition
- **Thinking mode**: Keep enabled for complex reasoning, disable for simple responses
- **System prompts**: Use for role-playing, context setting, and output formatting
- **Memory limits**: Sessions automatically trim to last 20 messages to prevent memory bloat

## Troubleshooting

- **API Key Issues**: Ensure your BytePlus API key is correctly set in config.ini or environment variables
- **Empty Results**: Check ComfyUI console for detailed error messages
- **Image Quality**: Try different prompts, seeds, or guidance scale values for better results
