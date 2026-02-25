# ComfyUI ElevenLabs TTS Node

A custom node for ComfyUI that integrates ElevenLabs' text-to-speech API, enabling high-quality voice synthesis within your ComfyUI workflows.

## Features

- Access to all ElevenLabs voices including premium and cloned voices
- Support for multiple models (Multilingual v2, English v2, Turbo v2)
- Advanced voice settings control (stability, similarity boost, style)
- Text input flexibility - connect from other nodes or use built-in text box
- Real-time voice list fetching with caching
- Audio output compatible with ComfyUI's audio system

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-11labs
```

2. Install the required dependencies:
```bash
pip install requests torch torchaudio
```

3. Restart ComfyUI

## Setup

You'll need an ElevenLabs API key to use this node:

1. Sign up at [ElevenLabs](https://elevenlabs.io)
2. Go to your profile settings
3. Generate an API key
4. Enter the API key in the node's `api_key` field

## Usage

### Basic Text-to-Speech

1. Add the "ElevenLabs TTS Node" to your workflow
2. Enter your API key
3. Type or connect text to synthesize
4. Select a voice from the dropdown
5. Choose a model (multilingual_v2 recommended)
6. Adjust voice settings as needed
7. Connect the audio output to audio preview or save nodes

### Input Options

- **api_key**: Your ElevenLabs API key (required)
- **text**: Text to synthesize (can use the text box or connect from another node)
- **voice**: Select from available voices including celebrity impressions
- **model**: Choose between multilingual_v2, english_sts_v2, or turbo_v2
- **stability**: Controls voice consistency (0.0-1.0)
- **similarity_boost**: How closely to match the original voice (0.0-1.0)
- **style**: Style exaggeration (0.0-1.0)
- **use_speaker_boost**: Enhance speaker similarity (True/False)

### Output

- **AUDIO**: Audio tensor compatible with ComfyUI audio nodes

## Voice Settings Guide

- **Stability**: Lower values (0.3) create more expressive speech, higher values (0.7+) are more consistent
- **Similarity Boost**: Higher values make the voice more similar to the original
- **Style**: Controls the expressiveness and emotion in the voice
- **Speaker Boost**: Enable for better voice cloning accuracy

## Available Voices

The node automatically fetches all available voices from your ElevenLabs account, including:
- Default ElevenLabs voices
- Any custom cloned voices you've created
- Premium voices available with your subscription tier

## Troubleshooting

- **No voices loading**: Check your internet connection and API key
- **Audio generation fails**: Verify your API key has sufficient credits
- **Voice not available**: Some voices may require specific subscription tiers

## Requirements

- ComfyUI
- Python packages: requests, torch, torchaudio
- ElevenLabs API key
- Internet connection for API calls

## License

MIT License

Copyright (c) 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.