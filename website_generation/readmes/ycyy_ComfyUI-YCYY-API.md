# ComfyUI-YCYY-API
[**English**](README.md) | [**中文**](README_zh_CN.md)

Freely call APIs in ComfyUI

## Instructions for use
* In ComfyUI, go to your custom_nodes folder, open a terminal and run the following command:
```
git clone https://github.com/ycyy/ComfyUI-YCYY-API.git
```
* Copy the `config.json.example` file and rename it to `config.json`. Then modify the corresponding `base_url` and `api_key`.

* Start `ComfyUI` and find the `YCYY/API` node directory to start your experience.

## Configuration file description

### gemini-image

`base_url` supports both official and third-party compatible interfaces, which can be configured according to actual conditions. The path ends with `v1beta/models`. `models` supports `gemini-2.5-flash-image` and `gemini-3-pro-image-preview` models. If using a third-party interface, modify the model name according to actual conditions.

### ollama-vlm and ollama-llm
`base_url` supports both local and `ollama` cloud service interfaces, which can be configured according to actual conditions. The interface is in `OpenAI` compatible format. The models in the configuration file are those supported by the official cloud service and can be modified as needed. If calling a local interface without configuring `api_key`, this option can be left blank.

### modelscope-image

The ModelScope image generation interface only requires you to fill in the corresponding `api_key`. Other parameters remain unchanged.

## Advanced usage instructions

API nodes support `Config Options` and `Proxy Options`. Both can be used to override configuration file parameters by configuring parameters through the front-end node.
