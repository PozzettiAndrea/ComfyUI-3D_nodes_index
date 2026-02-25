# This custom node allows you to generate images directly from text prompts using Hugging Face's text-to-image models within ComfyUI. It provides a simple interface to leverage powerful AI models like FLUX.1-dev without leaving your ComfyUI workflow.



Features

Generate images from text prompts using Hugging Face models

Configurable model selection (default: black-forest-labs/FLUX.1-dev)

Seamless integration with ComfyUI workflows

Outputs standard ComfyUI image format



Installation

Method 1: Manual Installation

Download this repository as a ZIP file

Extract the contents to your ComfyUI/custom_nodes directory

Install the required dependencies:

pip install -r requirements.txt

Restart ComfyUI



Method 2: Using Git

Navigate to your ComfyUI custom nodes directory:

cd path/to/ComfyUI/custom_nodes
Clone this repository:

git clone [repository-url]
Install the required dependencies:

cd [repository-name]
pip install -r requirements.txt

Restart ComfyUI



Requirements

This node requires the following Python packages:

requests
numpy
torch
Pillow


Usage

Add the "Hugging Face Text to Image" node to your workflow

Enter your text prompt in the "prompt" field

Provide your Hugging Face API key in the "api_key" field

Optionally, change the model ID (default is "black-forest-labs/FLUX.1-dev")

Connect the output to other nodes in your workflow



Getting a Hugging Face API Key

Create a Hugging Face account at huggingface.co

Navigate to your profile settings

Go to the "Access Tokens" section

Create a new token with appropriate permissions

Copy the token and paste it into the "api_key" field in the node



Troubleshooting

If you encounter errors, ensure your API key is valid

Check that all dependencies are properly installed

Verify your internet connection as this node requires online access to Hugging Face's API