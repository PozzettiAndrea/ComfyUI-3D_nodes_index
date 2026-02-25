# ComfyUI-Cog

- This is a custom node aiming to run CogView4 on diffusers while there is no official implementation on ComfyUI.
- You will need a updated version of diffusers and I don't know if updating it my break other stuff, so I advise you to make in a new instance of ComfyUI
- There is no progress bar preview in this node

## Installation

### Prerequisites

- ComfyUI installed and working
- GPU with at least 8GB VRAM (recommended)

### Installation Steps

1. Clone this repository to your ComfyUI's `custom_nodes` folder:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/your-username/ComfyUI-Cog
   ```

2. Install the required dependencies:
   ```bash
   # For standard ComfyUI installation (non-portable):
   pip install diffusers transformers accelerate
   
   # To install the latest version of diffusers (recommended):
   pip install git+https://github.com/huggingface/diffusers.git
   
   # For ComfyUI Portable:
   .\python_embeded\python.exe -m pip install diffusers transformers accelerate
   # Or for the latest version of diffusers:
   .\python_embeded\python.exe -m pip install git+https://github.com/huggingface/diffusers.git
   ```

3. Restart ComfyUI

## Usage

After installation, you'll have access to a new node:

### CogView4 Generator

This is the main node that generates images using the CogView4 model.

#### Parameters:

- **prompt**: Text description of the image you want to generate
- **width**: Width of the output image (default: 1024)
- **height**: Height of the output image (default: 1024)
- **num_inference_steps**: Number of inference steps (default: 50)
- **guidance_scale**: Model guidance scale (default: 3.5)
- **num_images**: Number of images to generate per execution (default: 1)
- **seed**: (Optional) Seed for reproducible results

#### Note about Progress Bar:

The CogView4 model does not support progress callbacks, so there is no real-time progress bar available during generation. You will see console output when generation starts and finishes, but no step-by-step progress indication.

## Example Workflow

1. Add the **CogView4 Generator** node to your workspace
2. Configure the prompt and other desired parameters
3. Connect the output of the CogView4 Generator to a Preview Image node to view the result
4. Optionally, connect to a Save Image node to save the image to disk

![Example Workflow](workflow_example.png)

## Performance Optimization

- Model CPU offload: loads parts of the model to CPU when not in use
- VAE slicing: processes the image in smaller slices
- VAE tiling: divides the image into blocks for processing


## Troubleshooting

### Import Error

If you encounter import errors like `No module named 'diffusers'`, make sure you have installed all required dependencies.

### CUDA Memory Errors

If you receive errors like `CUDA out of memory`, try:
- Close other applications using the GPU
- Decrease the image size parameters
- Enable the CPU offload function (enabled by default)

### Slow First Run

On the first run, the model will be downloaded from Hugging Face (approximately 12GB). This can take some time depending on your internet connection.
