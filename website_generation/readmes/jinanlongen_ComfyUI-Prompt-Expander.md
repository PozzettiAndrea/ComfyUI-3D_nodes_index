# ComfyUI Prompt Expander Node

A custom node for ComfyUI that expands text prompts using the SuperPrompt-v1 T5 model. This node helps generate more detailed and descriptive prompts from simple input text, which can be particularly useful for image generation workflows.

## Features

- Expands simple prompts into more detailed descriptions
- Configurable generation parameters
- Optional removal of incomplete sentences
- GPU acceleration support (when available)
- Automatic model downloading and caching

<img width="1168" alt="image" src="https://github.com/user-attachments/assets/228237f3-d24b-4aa1-9fd8-1be436d524a5" />

## Requirements

- Python 3.x
- PyTorch
- Transformers
- ComfyUI

## Installation

1. Install ComfyUI if you haven't already
2. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-username/ComfyUI-Prompt-Expander.git
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. After installation, restart ComfyUI
2. In the node menu, find the "Prompt Expander" node under the "text" category
3. Connect the node to your workflow

### Node Parameters

- **prompt** (STRING): The input text you want to expand
- **max_new_tokens** (INT): Maximum number of new tokens to generate (1-2048, default: 512)
- **repetition_penalty** (FLOAT): Penalty for repetition in generated text (0.0-2.0, default: 1.2)
- **remove_incomplete_sentences** (BOOLEAN): Whether to remove incomplete sentences from the output (default: True)

### Example

Input prompt: "a beautiful girl"
Output: [The model will generate a more detailed description of the scene]

## Model Information

This node uses the `roborovski/superprompt-v1` model, which will be automatically downloaded on first use and cached in the user's home directory under `.models/`.

## License

[Your License Here]

## Credits

- Model: roborovski/superprompt-v1
- https://github.com/NeuralSamurAI/Comfyui-Superprompt-Unofficial

 
