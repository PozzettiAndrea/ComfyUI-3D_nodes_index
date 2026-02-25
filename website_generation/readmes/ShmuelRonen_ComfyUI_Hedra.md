# ComfyUI Hedra Node

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that integrates with [Hedra](https://www.hedra.com)'s Character-3 API to generate talking avatar videos from images and audio.

![image](https://github.com/user-attachments/assets/fcfd5b5a-a910-4859-9e61-8affce0c788f)



https://github.com/user-attachments/assets/13150d25-df1f-4bb6-8f0c-ff5ca599575e






## Features

- Generate talking avatar videos using Hedra's advanced Character-3 technology
- **Intelligent background animation** - background objects move in coordination with the main character
- Support for multiple aspect ratios (16:9, 9:16, 1:1)
- Multiple resolution options (540p, 720p)
- Auto duration or custom duration settings
- Custom emotion and gesture prompts
- Video frame extraction for ComfyUI pipeline integration
- Debug mode for troubleshooting
- API connection testing utilities

## Pricing

**Hedra Character-3 API Pricing:**
- **~3.5 to ~7 credits per second of video**
- Actual credit usage depends on video complexity and resolution
- Example: A 30-second video costs approximately 105-210 credits

## What's New in Character-3

Character-3 introduces several advanced features:
- **An othntic image to video character Animation driven by audio and music**
- **Coordinated Background Animation**: Background elements and objects move naturally in sync with the character's movements
- **Enhanced Spatial Awareness**: The AI understands the 3D space and creates more realistic depth and movement
- **Improved Gesture Recognition**: Better interpretation of prompts for natural hand movements and body language
- **Advanced Emotion Mapping**: More nuanced facial expressions that match the audio's emotional content
- **Scene Coherence**: Maintains consistency between character movements and environmental elements

  ![image](https://github.com/user-attachments/assets/348070b6-81ec-4815-beec-7764a6e82d70)


## Installation

1. Clone this repository into your ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ShmuelRonen/ComfyUI_Hedra.git
```

2. Install the required dependencies:
```bash
cd ComfyUI_Hedra
pip install -r requirements.txt
```

3. Restart ComfyUI

## Getting Started

### 1. Obtain API Key

1. Visit [Hedra API Profile](https://www.hedra.com/api-profile)
2. Sign up or log in to your Hedra account
3. Subscribe to a paid plan (Creator tier or higher required for API access)
4. Navigate to your API profile page
5. Copy your API key (it should start with `sk_h`)

### 2. Configure the Node

1. After installation, a `config.json` file will be created in the node folder
2. Open `config.json` and replace `"your_api_key_here"` with your actual API key:

```json
{
    "api_key": "your_api_key_here"
}
```

## Usage

### Available Nodes

#### 1. Hedra Image to Video
The main node for generating talking avatar videos using Character-3.

**Inputs:**
- `image`: Input portrait image (Start frame) - can include background elements
- `audio`: Audio file for lip-sync (Audio script)
- `prompt` (optional): Text description for emotions, gestures, and scene dynamics
- `aspect_ratio`: Choose from 16:9, 9:16, or 1:1
- `resolution`: 540p or 720p
- `use_test_mode`: Set to true for testing without API calls
- `debug_mode`: Enable detailed logging

**Outputs:**
- `images`: Video frames as a batch
- `audio`: Original audio (pass-through)
- `frame_count`: Number of frames extracted
- `video_url`: URL of the generated video
- `fps`: Frames per second (typically 24)

### Prompt Examples for Better Results

To take advantage of Character-3's advanced capabilities, try these prompt patterns:

**Basic Emotion & Gesture:**
```
"smiling warmly, gesturing with hands while speaking"
```

**With Background Interaction:**
```
"speaking enthusiastically with hands, background gently swaying with movement"
```

**Complex Scene Dynamics:**
```
"passionate speech with emphatic gestures, environment responds to emotional intensity"
```

**Specific Background Elements:**
```
"confident presentation, curtains flutter as character moves, plants sway subtly"
```

## Cost Examples

| Audio Duration | Approximate Credits | Estimated Cost Range |
|----------------|--------------------|--------------------|
| 10 seconds     | 35-70 credits     | ~3.5-7 credits/sec |
| 30 seconds     | 105-210 credits   | ~3.5-7 credits/sec |
| 60 seconds     | 210-420 credits   | ~3.5-7 credits/sec |

*Note: Actual costs may vary based on video complexity and additional features used.*

## Workflow Example

1. Load an image using `Load Image` node (include background elements for best effect)
2. Load audio using an audio loader node
3. Connect both to the `Hedra Image to Video` node
4. Set your desired aspect ratio and resolution
5. Add a detailed prompt describing both character and scene dynamics
6. Connect the output frames to a `Video Combine` node or save them

## Character-3 Advanced Features

The Character-3 model from Hedra offers:
- **Scene Understanding**: AI comprehends the relationship between character and environment
- **Dynamic Backgrounds**: Background elements move naturally with character actions
- **Depth Perception**: Creates realistic 3D movement within 2D images
- **Motion Coherence**: Ensures all elements move in physically plausible ways
- **Adaptive Animation**: Adjusts movement intensity based on audio energy and emotion

## Best Practices for Background Animation

1. **Image Selection**: Choose images with distinct background elements (curtains, plants, furniture)
2. **Prompt Clarity**: Describe how you want the background to react to the character
3. **Audio Matching**: Background movement intensity matches audio energy levels
4. **Scene Composition**: Leave space around the character for natural movement

## Important Notes

- **API Credits**: Each video generation consumes credits from your Hedra account
- **Processing Time**: Video generation typically takes 2-5 minutes
- **Audio Length**: Longer audio files will consume more credits (3.5-7 credits per second)
- **Image Requirements**: Best results with clear face portraits and visible background elements
- **Output Format**: Videos are generated at 24 FPS

## Troubleshooting

1. **Background Not Animating**:
   - Ensure your prompt mentions background movement
   - Use images with distinct background elements
   - Try more specific scene descriptions

2. **API Key Issues**:
   - Ensure your API key is correctly set in `config.json`
   - Verify you have an active paid subscription
   - Check that your API key starts with `sk_h`

3. **Generation Failures**:
   - Enable `debug_mode` for detailed error messages
   - Verify your audio format is supported (WAV recommended)
   - Ensure your image contains a clear face

## API Endpoints

The node uses the following Hedra API endpoints:
- Base URL: `https://api.hedra.com/web-app/public`
- `/models` - Get available AI models
- `/assets` - Create and upload assets
- `/generations` - Create and monitor video generations

## Credits

This node was developed to integrate Hedra's powerful Character-3 technology with ComfyUI, enabling seamless talking avatar generation with advanced background animation in visual workflows.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial integration and is not affiliated with or endorsed by Hedra. Use of the Hedra API is subject to their terms of service and pricing. API costs are charged by Hedra and not by this node's developer.
