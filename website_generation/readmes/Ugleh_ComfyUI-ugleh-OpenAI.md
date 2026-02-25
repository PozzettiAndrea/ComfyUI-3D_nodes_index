# ComfyUI-ugleh-OpenAI

Minimal OpenAI API nodes for ComfyUI.

## Nodes

### Ugleh OpenAI - Responses Text

Calls the OpenAI **Responses API**.

Inputs:
- `model`: choose an OpenAI model (includes GPT‑4o/4.1 and GPT‑5 family)
- `reasoning_effort`: `low` / `medium` / `high`
- `instructions`: multi-line text
- `input`: multi-line text
- `max_output_tokens`

Outputs:
- `text_out`

## Setup

### Using Your API Key

To securely store your OpenAI API key:

1. Create a file named `.env` in the root folder of your ComfyUI installation.
2. Add the following line to the `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
   Replace `your_api_key_here` with your actual OpenAI API key.
3. Save the file.

This method allows you to keep your API key secure and separate from your code.

### Installation and Usage

1. Navigate to ComfyUI/custom_nodes folder in the terminal or command prompt.
2. Clone the repo using the following command:
   `git clone https://github.com/Ugleh/ComfyUI-ugleh-OpenAI`
3. Go to `custom_nodes/ComfyUI-ugleh-OpenAI` and install dependencies by running `pip install -r requirements.txt`
4. Restart ComfyUI

## License

MIT (see LICENSE)
