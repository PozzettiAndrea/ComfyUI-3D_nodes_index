# ComfyUI LLM Helper

A collection of helper nodes for working with LLM APIs in ComfyUI, intended to complement other LLM custom nodes.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/bedovyy/ComfyUI-LLM-Helper
cd ComfyUI-LLM-Helper
pip install -r requirements.txt
```

## Usage

### `LLMHelper GET /models`

- Set your LLM server's `base_url` and select API key from environment variables (loaded securely from `ComfyUI/.env`).
- Click **"Update model names"** to query the real /models endpoint and instantly refresh the `model_name` dropdown with available models, then use the outputs downstream.

### `LLMHelper POST /models/unload`

- Sends an unload request to `llama-server` when running in **router mode**, freeing the model from memory.

## Example

<img width="1729" height="1241" alt="image" src="https://github.com/user-attachments/assets/4db57a0d-09fe-40bb-9dbe-c09cc714ce6a" />
