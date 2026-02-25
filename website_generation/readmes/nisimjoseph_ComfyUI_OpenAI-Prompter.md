# ComfyUI OpenAI Prompter

A custom node for ComfyUI that generates creative and detailed prompts using OpenAI's GPT models.

## Features

- Generate AI image prompts using OpenAI's GPT models
- Supports both latest and older versions of the OpenAI API
- Adjustable parameters (temperature, max tokens, seed)
- Detailed logging of responses
- Easy integration with other ComfyUI nodes

## Installation

1. Make sure you have ComfyUI installed and working properly.

2. Navigate to your ComfyUI's custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
```

3. Clone this repository:
```bash
git clone https://github.com/nisimjoseph/ComfyUI_OpenAI-Prompter
```

4. Install the required dependencies:
```bash
pip install openai
```

5. Set up your OpenAI API key:
   - Get your API key from [OpenAI's platform](https://platform.openai.com/api-keys)
   - Set it as an environment variable:
     ```bash
     # On Windows (Command Prompt)
     set OPENAI_API_KEY=your-api-key-here

     # On Windows (PowerShell)
     $env:OPENAI_API_KEY="your-api-key-here"

     # On Linux/MacOS
     export OPENAI_API_KEY="your-api-key-here"
     ```
   - Alternatively, you can add it to your ComfyUI's environment configuration

6. Restart ComfyUI

## Usage

1. In the ComfyUI interface, find the "OpenAI Prompt Generator" node under the "prompt" category

2. Configure the node parameters:
   - `model`: Select from available GPT models
   - `prompt_context`: Enter your prompt context/instructions
   - `max_tokens`: Adjust the maximum length of the generated prompt (256-4096)
   - `temperature`: Control creativity (0.0-2.0)
   - `seed`: Set for reproducible results

3. Connect the node's output to other ComfyUI nodes that accept text prompts

## Example Workflow

1. Add the "OpenAI Prompt Generator" node
2. Configure your desired parameters
3. Connect its output to a text prompt input of an image generation node
4. Run the workflow to generate creative prompts for your images

## Troubleshooting

- If you see "Error: OpenAI API key not found or invalid":
  - Check that your API key is correctly set
  - Verify your API key has available credits
  - Ensure your OpenAI account is in good standing

- If the node isn't appearing:
  - Verify the installation directory is correct
  - Check ComfyUI's console for any error messages
  - Try restarting ComfyUI

- If prompts aren't being generated:
  - Check your internet connection
  - Verify your API key has sufficient quota
  - Look for error messages in the console output

## Support

If you encounter any issues or have questions:
- Check the console output for detailed error messages
- Verify your OpenAI API key and quota
- Ensure you're using a compatible version of the OpenAI package

## License

[MIT License](LICENSE) 