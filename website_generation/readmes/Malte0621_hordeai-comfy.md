# HordeAI

AI Horde integration as custom node(s) for ComfyUI

This extension provides ComfyUI nodes for generating images using the [AI Horde](https://aihorde.net/) distributed network of Stable Diffusion models.

## Features

- **AI Horde Image Generate**: Generate images using AI Horde's distributed network
- **AI Horde Model List**: Get list of available models on the network
- Support for multiple models (Deliberate, Anything Diffusion, AlbedoBase XL, etc.)
- Configurable image dimensions, steps, CFG scale, and more
- Anonymous generation or use your own API key
- Image generation with proper ComfyUI integration
- Support for txt2img, img2img, inpainting, outpainting, and remix modes
- Support for LORA and textual inversion models

## Installation

### Option 1: ComfyUI Manager (Recommended)
1. Install [ComfyUI](https://docs.comfy.org/get_started)
2. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
3. Look up "HordeAI" in ComfyUI-Manager and install it
4. Restart ComfyUI

### Option 2: Manual Installation
1. Clone this repository into your `ComfyUI/custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/malte0621/hordeai-comfy.git
   ```
2. Install dependencies:
   ```bash
   cd hordeai-comfy
   pip install -r requirements.txt
   ```
3. Restart ComfyUI

## Usage

### AI Horde Image Generate Node

This node generates images using the AI Horde network:

**Required Inputs:**
- `prompt`: Text description of the image to generate
- `width`: Image width (64-2048, step 64)
- `height`: Image height (64-2048, step 64) 
- `num_images`: Number of images to generate (1-4)
- `model`: AI model to use (Deliberate, Anything Diffusion, etc.)

**Optional Inputs:**
- `negative_prompt`: Text describing what to avoid in the image
- `api_key`: Your AI Horde API key (leave empty for anonymous)
- `steps`: Sampling steps (1-100, default 20)
- `cfg_scale`: Classifier-free guidance scale (1.0-20.0, default 7.5)
- `seed`: Random seed (-1 for random)
- `denoising_strength`: Denoising strength for img2img (0.0-1.0, default 1.0)
- `source_image`: Input image for img2img or inpainting (ComfyUI tensor)
- `source_processing`: "txt2img", "img2img", "inpainting", "outpainting", or "remix" (default "txt2img")
- `sampler_name`: Sampler to use (e.g., "k_lms", "k_euler_a", default "k_lms")
- `karras`: Whether to use Karras noise schedule (default True)
- `loras`: List of LORA model names to apply
- `textual_inversions`: List of textual inversion names to apply

**Output:**
- `images`: Generated images as ComfyUI tensors

### AI Horde Model List Node

This node lists available models on the AI Horde network:

**Optional Inputs:**
- `api_key`: Your AI Horde API key

**Output:**
- `model_list`: String containing available model names

## API Key

While you can use AI Horde anonymously, having an API key provides benefits:
- Higher priority in the generation queue
- Access to more models
- Faster generation times

Get your free API key at [AI Horde](https://aihorde.net/).

## Requirements

- Python 3.10+
- ComfyUI
- horde-sdk>=0.17.1
- aiohttp>=3.9.0
- Pillow>=10.0.0
- numpy>=1.24.0
- torch>=2.0.0
- loguru>=0.7.0

## Develop

To install the dev dependencies and pre-commit (will run the ruff hook), do:

```bash
cd hordeai-comfy
pip install -e .[dev]
pre-commit install
```

The `-e` flag above will result in a "live" install, in the sense that any changes you make to your node extension will automatically be picked up the next time you run ComfyUI.

## Publish to Github

Install Github Desktop or follow these [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for ssh.

1. Create a Github repository that matches the directory name. 
2. Push the files to Git
```
git add .
git commit -m "project scaffolding"
git push
``` 

## Writing custom nodes

An example custom node is located in [node.py](src/hordeai/nodes.py). To learn more, read the [docs](https://docs.comfy.org/essentials/custom_node_overview).


## Tests

This repo contains unit tests written in Pytest in the `tests/` directory. It is recommended to unit test your custom node.

- [build-pipeline.yml](.github/workflows/build-pipeline.yml) will run pytest and linter on any open PRs
- [validate.yml](.github/workflows/validate.yml) will run [node-diff](https://github.com/Comfy-Org/node-diff) to check for breaking changes

## Publishing to Registry

If you wish to share this custom node with others in the community, you can publish it to the registry. We've already auto-populated some fields in `pyproject.toml` under `tool.comfy`, but please double-check that they are correct.

You need to make an account on https://registry.comfy.org and create an API key token.

- [ ] Go to the [registry](https://registry.comfy.org). Login and create a publisher id (everything after the `@` sign on your registry profile). 
- [ ] Add the publisher id into the pyproject.toml file.
- [ ] Create an api key on the Registry for publishing from Github. [Instructions](https://docs.comfy.org/registry/publishing#create-an-api-key-for-publishing).
- [ ] Add it to your Github Repository Secrets as `REGISTRY_ACCESS_TOKEN`.

A Github action will run on every git push. You can also run the Github action manually. Full instructions [here](https://docs.comfy.org/registry/publishing).

