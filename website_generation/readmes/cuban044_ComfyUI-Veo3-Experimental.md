# ComfyUI-Veo3-Experimental

A custom node extension for ComfyUI that integrates Google's Veo 3 text-to-video generation capabilities.

![image](https://github.com/user-attachments/assets/977fff8f-5418-4904-a44b-f27435a41d55)


## Overview of Veo 3

Veo 3 is Google's latest text-to-video generation model, designed to create high-quality videos from text prompts. It offers improved quality, better motion understanding, and enhanced visual fidelity compared to previous versions.

> ⚠️ **Important:** <span style="color:red">This feature may not yet be available in your country. You may also be charged by Google for additional usage 0.35$ per sec.</span>

### Key Features of Veo 3

* **Text-to-Video Generation**: Create videos from descriptive text prompts
* **Resolution**: Outputs videos in 720p resolution at 24 frames per second
* **Aspect Ratios**: Supports standard formats like 16:9 and 9:16
* **Maximum Video Length**: Up to 8 seconds per video
* **Watermarking**: Videos are watermarked with SynthID for ethical AI use
* **Enhanced Quality**: Improved visual fidelity and motion understanding

## Features

- Generate videos from text prompts using Google's Veo 3 model
- Configure video aspects like duration, aspect ratio, and person generation
- Save generated videos to your output directory
- Convert Veo 3 videos to VHS-compatible image format for further processing

## Requirements

- ComfyUI (latest version recommended)
- Google Cloud API Key with access to Veo 3
- Python 3.8+
- Google Generative AI Python SDK: `pip install google-genai>=0.3.0`

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
   ```
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/ShmuelRonen/ComfyUI-Veo3-Experimental
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Get your free API key from Google AI Studio:
   - Visit [Google AI Studio](https://aistudio.google.com/prompts/new_chat)
   - Log in with your Google account
   - Click on "Get API key" or go to settings
   - Create a new API key
   - Copy the API key for use in .env file

4. Create a `.env` file in the extension directory with your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. Restart ComfyUI

## Usage

### Veo 3 Text to Video

1. Add the "Veo 3 Text to Video" node to your workflow
2. Enter your prompt describing the video you want to generate
3. Configure:
   - Aspect ratio (16:9 or 9:16)
   - Person generation setting (don't allow or allow adult)
   - Duration (5-8 seconds)
4. Connect to "Veo 3 Video Saver" to view and save results

### Veo 3 Video Saver

1. Connect video output from a Veo 3 generation node
2. Configure:
   - Save to output (true/false)
   - Filename prefix
3. Execute to save videos to your ComfyUI output directory

### Veo 3 to VHS

Converts Veo 3 videos to a format compatible with other ComfyUI video processing nodes.

## Notes

- Video generation may take several minutes
- The extension implements rate limiting to avoid quota errors
- Image-to-video generation is currently not supported by Google's API
- Maximum video duration is 8 seconds
- Veo 3 offers improved quality and motion understanding over previous versions

## Troubleshooting

If you encounter "Google API key is required" errors:
- Check that your `.env` file is in the correct location
- Verify your API key is valid and has access to Veo 3
- Restart ComfyUI

If you encounter import errors:
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check that you're using Python 3.8 or higher

## License

[Your License Here]
