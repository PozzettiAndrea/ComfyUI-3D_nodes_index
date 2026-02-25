# Hal.fun Model Downloader for ComfyUI

This addon provides a user interface for managing and downloading models from Hugging Face in ComfyUI.

## Features

- User interface for managing model downloads
- Automatic model download status checking
- Persistent configuration of enabled models
- Asynchronous downloads that don't block the UI
- Support for downloading models from Hugging Face repositories

## Installation

1. Clone this repository into your ComfyUI's `custom_nodes` directory
2. Restart ComfyUI

## Usage

1. Click on the "Model Downloader" tab in the ComfyUI interface
2. Check the boxes next to the models you want to download
3. Click the "Download" button next to each model to start the download
4. The download status will be displayed below the model list

## Configuration

The addon uses two configuration files:

1. `model_config.json`: Contains the list of available models and their download configurations
2. `user/default/hal.fun-downloader/active_config.json`: Stores which models are enabled for download

## Requirements

- ComfyUI
- huggingface_hub Python package

## License

MIT License 