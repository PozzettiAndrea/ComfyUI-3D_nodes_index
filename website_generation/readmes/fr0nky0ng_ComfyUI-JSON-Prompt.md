# ComfyUI JSON PROMPT

[中文版 ](READMECN.md)



## Overview

This is a custom node for ComfyUI that generates JSON PROMPTs. Simply input a simple natural language description to produce prompts in JSON format, which helps improve the quality of text-to-image generation.

## Features

- **Simple Input**: Generate complex JSON PROMPTs using natural language descriptions.
- **JSON Output**: Directly outputs parseable JSON format for easy processing by subsequent nodes.
- **Enhanced Generation Quality**: Optimize outputs from Stable Diffusion or other text-to-image models through JSON PROMPTs.

## Supported LLM Integrations

Users can run locally deployed LLMs with the Ollama node or request the Google Gemini model via API using the Gemini Prompt Node.

### Ollama Integration
- Suitable for locally deployed open-source LLM models (e.g., Llama series).
- Ensure the Ollama node is installed and properly configured in ComfyUI.

### Gemini Integration
- Generates prompts by calling the Google Gemini model via API.
- Requires a Gemini API key, which must be set in the Gemini Prompt Node.

## Installation

1. Clone or download the node files to ComfyUI's `custom_nodes` directory.
2. Restart ComfyUI.
3. Search for "JSON PROMPT" in the node menu to find this node.



## Dependencies

- ComfyUI (latest version)
- Ollama node (optional, for local LLM)
- Gemini Prompt Node (optional, for Google Gemini API)

## Contributing and Issue Reporting

Contributions via Issues or Pull Requests are welcome. If you encounter issues, please provide detailed error logs and workflow screenshots.

## License

MIT License - Free to use and modify.