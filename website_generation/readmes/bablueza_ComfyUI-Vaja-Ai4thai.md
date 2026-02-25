# Vaja TextToSpeech Node for ComfyUI

https://github.com/bablueza/ComfyUI-Vaja-Ai4thai

Example Result.

## Installation

1. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/bablueza/ComfyUI-Vaja-Ai4thai
```

## Usage

1. In ComfyUI, locate the "Vaja TextToSpeech" node under the "Ai4Thai" category
2. Connect the node to your workflow
3. Input your text 
4. The node will output an audio waveform that can be used with other audio nodes

### Input Parameters

- `text`: The text you want to convert to speech (supports multiline text)
- `speaker`: The voice to use for speech synthesis (default: Woman)

### Output

- `audio`: Audio data in the format expected by ComfyUI audio nodes

