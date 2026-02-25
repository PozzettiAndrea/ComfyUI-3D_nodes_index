# comfyui-sg-openai-client

Custom nodes for ComfyUI to integrate with OpenAI API (local supported), providing chat completion capabilities with support for images.

![Screenshot](assets/node_preview.png)

## Features

- **OpenAI Client Node**: Authenticate with OpenAI API using API key and optional custom base URL
- **OpenAI Chat Completion Node**: Generate text completions with system/user prompts, optional image inputs, and configurable parameters (temperature, top_p, max_tokens, etc.)
- **Model Fetching API**: Endpoint to retrieve available models from OpenAI

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` directory:
   ```
   git clone https://github.com/yourusername/comfyui-sg-openai-client.git
   cd ComfyUI/custom_nodes/comfyui-sg-openai-client
   pip install -r requirements.txt
   ```

2. Restart ComfyUI to load the custom nodes.

## Usage

### OpenAI Client Node
- **Inputs**:
  - `api_key` (required): Your OpenAI API key
  - `base_url` (optional): Custom API base URL (defaults to OpenAI's)
- **Output**: OpenAI client object for use in other nodes

### OpenAI Chat Completion Node
- **Required Inputs**:
  - `client`: Connected from OpenAI Client Node
  - `system_prompt`: System message for the conversation
  - `user_prompt`: User message
  - `model`: Model selection (choices populated via API)
- **Optional Inputs**:
  - `image`: Image tensor for vision-enabled models
  - `temperature`: Sampling temperature (0.0-2.0, default 1.0)
  - `top_p`: Nucleus sampling parameter (0.0-1.0, default 1.0)
  - `max_tokens`: Maximum tokens to generate (1-4096, default 1000)
  - `frequency_penalty`: Frequency penalty (-2.0-2.0, default 0.0)
  - `presence_penalty`: Presence penalty (-2.0-2.0, default 0.0)
- **Output**: Generated completion text

### API Endpoint
The package adds a POST endpoint `/sg_openai_models` to ComfyUI's server for fetching available models. It requires `api_key` and optional `base_url` in the request body.

## Requirements
- ComfyUI
- OpenAI Python client (included in requirements.txt)

## License
See LICENSE file.
