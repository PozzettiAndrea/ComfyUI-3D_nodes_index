# ComfyUI-AnyLLM

A ComfyUI custom node pack for calling LLM providers.

This pack currently includes **Google Gemini** nodes powered by the official **`google-genai`** Python SDK.

## Install

### Install via ComfyUI Manager

1. Open **ComfyUI Manager**
2. Install this repository as a custom node

If the repository is not listed yet, you can still install it by URL using Manager's "Install via Git URL" feature.

### Manual install (git)

Clone into your ComfyUI `custom_nodes` folder:

```bash
git clone <YOUR_GIT_URL> ComfyUI/custom_nodes/ComfyUI-AnyLLM
```

Then install Python dependencies in the same Python environment ComfyUI uses:

```bash
pip install -r ComfyUI/custom_nodes/ComfyUI-AnyLLM/requirements.txt
```

Restart ComfyUI.

## Nodes

### Get Environment Variable (AnyLLM)

Category:
- `AnyLLM/Utils`

Inputs:
- `name` (STRING) - environment variable name, e.g. `GOOGLE_API_KEY`

Outputs:
- `value` (STRING)

Notes:
- Raises an error if the variable is missing or empty.

### Google Gemini (AnyLLM)

Category:
- `AnyLLM/Google`

Inputs:
- `model` (dropdown)
- `api_key` (STRING) - connect from **Get Environment Variable (AnyLLM)**
- `prompt` (STRING)
- `images` (IMAGE, optional) - image batch input
- `response_images` (BOOLEAN) - request image outputs when supported by the model

Outputs:
- `text` (STRING)
- `images` (IMAGE)

Notes:
- If the model returns images, they are output as `images`.
- If the model does not return images, the node passes through the input `images` (or returns a small blank image if none was provided).

## Notes

- Provider/model capabilities differ; not every model supports images.
- API keys are passed only at runtime (not stored).

## Errors

This pack **raises Python exceptions** on failures (missing keys, missing deps, API errors) so the error shows up directly on the node in ComfyUI.

## ComfyUI Manager listing

To be discoverable in the default ComfyUI Manager registry, submit a PR to the registry list (ComfyUI-Manager maintains a public JSON list of repositories).
