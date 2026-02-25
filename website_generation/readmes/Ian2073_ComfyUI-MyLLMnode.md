# ComfyUI-MyLLMNode

Custom ComfyUI node for running LLMs via HuggingFace pipeline. Supports both local paths and HuggingFace model names.

## Installation

Clone this repo into your ComfyUI `custom_nodes/` folder.

## Usage

- Drag "My LLM Node" into your ComfyUI workflow.
- Fill in:
    - Prompt
    - Model path (e.g. mistralai/Mistral-7B-Instruct-v0.3 or ./models/mistral-7b-instruct)
    - Max new tokens
    - Temperature
- Run!

## Example

prompt = "你好！今天過得如何？"
model_path = "./models/mistral-7b-instruct"