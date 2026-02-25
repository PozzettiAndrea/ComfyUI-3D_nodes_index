# ComfyUI-Gemini_Flash_2.0_Exp

## Support My Work
If you find this project helpful, consider buying me a coffee:

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=shmuelronen&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/shmuelronen)

A ComfyUI custom node that integrates Google's Gemini Flash 2.0 Experimental model, enabling multimodal analysis of text, images, video frames, and audio directly within ComfyUI workflows. Now with image generation capabilities!

![image](https://github.com/user-attachments/assets/ad7cdf57-3d42-4d61-bb23-45b1ce228bca)
![image](https://github.com/user-attachments/assets/57db07a4-01b4-4578-ae18-7969ebd8d673)
Audio option
![image](https://github.com/user-attachments/assets/b7db8643-0443-45b9-b79d-c3b8d4e88ce1)

## Features

- Multimodal input support:
  - Text analysis
  - Image analysis
  - Video frame analysis
  - Audio analysis
- **NEW! Image Generation** using gemini-2.0-flash-exp-image-generation model
- Chat mode with conversation history
- Voice chat with smart Audio recorder node
- Structured output option
- Temperature and token limit controls
- Proxy support
- Configurable API settings via config.json

## Installation

Install via ComfyUI manager

or

Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ShmuelRonen/ComfyUI-Gemini_Flash_2.0_Exp.git
```

Install required dependencies:
```bash
# Install BOTH packages (both are required)
pip install google-genai
pip install google-generativeai
# OR
python -m pip install google-genai
python -m pip install google-generativeai

# Other dependencies
pip install pillow
pip install torchaudio
```
### Important:
For Ubuntu/Debian-based systems:
 ```
sudo apt-get install libportaudio2
 ```

1. Get your free API key from Google AI Studio:
   - Visit [Google AI Studio](https://aistudio.google.com/prompts/new_chat)
   - Log in with your Google account
   - Click on "Get API key" or go to settings
   - Create a new API key
   - Copy the API key for use in config.json

2. Set up your API key in the `config.json` file (will be created automatically on first run)

## Configuration

### API Key Setup

Make `config.json` file in the node main folder:
```json
{
    "GEMINI_API_KEY": "your_api_key_here"
}
```

### WSL 2 Ubuntu Users

### Note: always insert the API-KEY into Gemini Flash 2 node.

## Node Inputs

### Required Inputs:
- **prompt**: Main text prompt for analysis or generation
- **input_type**: Select from ["text", "image", "video", "audio"]
- **model_version**: Select model including the new image generation model
- **operation_mode**: Select between "analysis" or "generate_images" mode
- **chat_mode**: Boolean to enable/disable chat functionality
- **clear_history**: Boolean to reset chat history

### Optional Inputs:
- **Additional_Context**: Additional text input for context
- **images**: Multiple image inputs (IMAGE type with list=True)
- **video**: Video frame sequence input (IMAGE type)
- **audio**: Audio input (AUDIO type)
- **api_key**: Directly enter your API key (recommended for WSL/Ubuntu)
- **max_output_tokens**: Set maximum output length (1-8192)
- **temperature**: Control response randomness (0.0-1.0)
- **structured_output**: Enable structured response format
- **max_images**: Maximum number of images to process (1-16)
- **batch_count**: Number of images to generate (for image generation mode)
- **seed**: Random seed for reproducible image generation

## Usage Examples

### Basic Text Analysis:
```
Text Input Node -> Gemini Flash Node [input_type: "text", operation_mode: "analysis"]
```

### Image Analysis:
```
Load Image Node -> Gemini Flash Node [input_type: "image", operation_mode: "analysis"]
```

### Video Analysis:
```
Load Video Node -> Gemini Flash Node [input_type: "video", operation_mode: "analysis"]
```

### Audio Analysis:
```
Load Audio Node -> Gemini Flash Node [input_type: "audio", operation_mode: "analysis"]
```

### Image Generation:
```
Text Input Node -> Gemini Flash Node [model_version: "gemini-2.0-flash-exp-image-generation", operation_mode: "generate_images"]
```

### Image Generation with Reference:
```
Load Image Node -> Gemini Flash Node [model_version: "gemini-2.0-flash-exp-image-generation", operation_mode: "generate_images"]
```

## Chat Mode

Chat mode maintains conversation history and provides a more interactive experience:

1. Enable chat mode by setting `chat_mode: true`
2. Chat history format:
```
=== Chat History ===
USER: your message
ASSISTANT: Gemini's response
=== End History ===
```
3. Use `clear_history: true` to start a new conversation
4. Chat history persists between calls until cleared

### Chat Mode Tips:
- Works with all input types (text, image, video, audio)
- History is displayed in the output
- Maintains context across multiple interactions
- Clear history when switching topics

## Video Frame Handling

When processing videos:
- Automatically samples frames evenly throughout the video
- Resizes frames for efficient processing
- Works with both chat and non-chat modes

## Image Generation

The new image generation capabilities allow you to:
- Generate images from text descriptions
- Generate variations based on reference images
- Control the generation with seed and temperature parameters
- Generate multiple images with batch_count

### Image Generation Tips:
- For best results, use the "gemini-2.0-flash-exp-image-generation" model
- Use "generate_images" operation mode
- Provide clear, detailed prompts for better results
- Connect reference images for style guidance
- Use seed parameter for reproducible results

## Troubleshooting Cross-Platform Issues

### Windows vs. Ubuntu/WSL Differences
- On Windows, both config file and GUI methods work well
- On Ubuntu/WSL, entering the API key directly in the GUI is more reliable
- If using lowercase filenames on Ubuntu (e.g., `gemini_flash_node.py` instead of `Gemini_Flash_Node.py`), the node will still work properly

### Common Issues on Ubuntu/WSL:
- If you get "400 Bad Request" errors, try entering your API key directly in the GUI
- Make sure binary data (images, audio) is properly base64 encoded
- Check network connectivity and proxy settings
- Ensure proper file permissions for config files

## Error Handling

The node provides clear error messages for common issues:
- Invalid API key
- Rate limit exceeded
- Invalid input formats
- Network/proxy issues

## Rate Limits

Default rate limits (from config.json):
- 10 requests per minute (RPM_LIMIT)
- 4 million tokens per minute (TPM_LIMIT)
- 1,500 requests per day (RPD_LIMIT)

### Audio Analysis with Smart Recording:

The package includes two nodes for audio handling:
1. **Audio Recorder Node**: Smart audio recording with silence detection
2. **Gemini Flash Node**: Audio content analysis

#### Audio Recorder Node Features:

- Live microphone recording with automatic silence detection
- Smart recording termination after detecting silence
- Configurable silence threshold and duration
- Compatible with most input devices
- Visual recording status indicator (10-second auto-reset)
- Seamless integration with Gemini Flash analysis

#### Audio Recording Setup:

```
Audio Recorder Node -> Gemini Flash Node [input_type: "audio"]
```

#### Audio Recorder Controls:

- **device**: Select input device (microphone)
- **sample_rate**: Audio quality setting (default: 44100 Hz)
- **silence_threshold**: Sensitivity for silence detection (0.001-0.1)
- **silence_duration**: Required silence duration to stop recording (0.5-5.0 seconds)
- **Record Button**: 
  - Click to start recording
  - Records until silence is detected
  - Button resets after 10 seconds automatically
  - Visual feedback during recording (red indicator)

#### Using Voice Commands/Audio Analysis:

1. Add Audio Recorder node to your workflow
2. Connect it to Gemini Flash node
3. Configure recording settings:
   - Choose input device
   - Adjust silence detection parameters
   - Set sample rate if needed
4. Click "Start Recording" to begin
5. Speak your message
6. Recording automatically stops after detecting silence
7. The recorded audio is processed and sent to Gemini for analysis
8. Recording button resets after 10 seconds, ready for next recording

#### Example Audio Analysis Workflow:

```
Audio Recorder Node [silence_duration: 2.0, silence_threshold: 0.01] -> 
Gemini Flash Node [input_type: "audio", prompt: "Transcribe and analyze this audio"]
```


## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

MIT License

## Acknowledgments

- Google's Gemini API
- ComfyUI Community
- All contributors

---

**Note**: This node is experimental and based on Gemini 2.0 Flash Experimental model. Features and capabilities may change as the model evolves.
