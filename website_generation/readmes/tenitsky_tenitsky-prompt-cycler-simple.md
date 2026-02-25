# ComfyUI Prompt Cycler Node

A custom ComfyUI node that cycles through an infinite number of prompts, perfect for batch generation with varied content. Supports both built-in example prompts and custom user-defined prompts.

🎥 **Tutorial Video:** [Watch on YouTube](https://youtu.be/FILrz0DDqYU)

## Features

- **Infinite Prompt Support**: Cycle through any number of custom prompts
- **10 Example Prompts**: Pre-configured with diverse, high-quality prompts covering various themes
- **Sequential Cycling**: Automatically cycles through prompts in order
- **Random Mode**: Randomly selects prompts for more variety
- **Custom Prompts**: Option to provide your own prompts (unlimited number)
- **Reset Functionality**: Ability to reset the cycle counter
- **Seed Control**: Reproducible results with seed input

## Installation

### Method 1: Git Clone (Recommended)
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/tenitsky/tenitsky-prompt-cycler-simple.git
cd tenitsky-prompt-cycler-simple
pip install -r requirements.txt
```

### Method 2: Manual Installation
1. Download this repository as a ZIP file
2. Extract it to your ComfyUI `custom_nodes` directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Restart ComfyUI

## Usage

### Basic Usage
1. Add the "Prompt Cycler" node to your workflow
2. Connect the `prompt` output to your text input node
3. Each time you queue the workflow, it will use the next prompt in sequence

### Parameters

- **Seed**: Random seed for reproducible results (0 = no seed)
- **Cycle Mode**: 
  - `sequential`: Cycles through prompts in order
  - `random`: Randomly selects prompts
- **Reset Cycle**: Checkbox to reset the cycle counter to 0
- **Custom Prompts** (optional): Provide your own prompts, one per line. Supports unlimited number of prompts.

### Example Prompts

The node comes with 10 pre-configured example prompts to get you started:

1. "A majestic mountain landscape at sunset with golden light"
2. "A futuristic city with flying cars and neon lights"
3. "A peaceful forest with sunlight filtering through trees"
4. "An underwater scene with colorful coral reefs and fish"
5. "A cozy cabin in the woods during winter snowfall"
6. "A space station orbiting a distant planet"
7. "A bustling marketplace in an ancient city"
8. "A serene lake with mountains reflected in the water"
9. "A steampunk laboratory with brass gears and steam"
10. "A magical garden with glowing flowers and butterflies"

### Custom Prompts

To use your own prompts (supports unlimited number):
1. Enable the `custom_prompts` input
2. Enter your prompts, one per line
3. The node will cycle through your custom prompts instead of the example ones
4. You can have as many prompts as you want - the node will cycle through them infinitely

## Example Workflow

```
Prompt Cycler → Text Input → CLIP Text Encode → KSampler → VAE Decode → Save Image
```

## Outputs

- **prompt**: The current prompt string
- **cycle_index**: The index of the current prompt (0-based, cycles through all available prompts)

## Tips

- Use sequential mode for consistent batch generation
- Use random mode for more variety in your outputs
- Combine with batch processing nodes for efficient multi-prompt generation
- Use the reset cycle option when you want to start over from the first prompt

## Troubleshooting

- Make sure PyTorch is installed correctly
- Check that the node appears in the "text/prompt" category
- If prompts aren't cycling, try using the reset cycle option
- For custom prompts, ensure each prompt is on a separate line
- You can use any number of prompts - the node will cycle through them infinitely

## Author

Created by **Anton Tenitsky** in 2025.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v1.0.0
- Initial release
- Support for infinite number of custom prompts
- 10 built-in example prompts
- Sequential and random cycling modes
- Reset functionality

- Seed control for reproducible results
