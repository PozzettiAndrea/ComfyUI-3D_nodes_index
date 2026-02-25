# ComfyUI-Latent-Reverb

Creates spatial "echo" and ambient effects by applying reverb-like processing directly in latent space

> [!NOTE]
> This project was created with a [cookiecutter](https://github.com/Comfy-Org/cookiecutter-comfy-extension) template. It helps you start writing custom nodes without worrying about the Python setup.

## Overview

ComfyUI-Latent-Reverb is a custom node that applies neural reverb processing directly to latent representations of images. Instead of processing audio signals, it creates spatial "echo" and reflection effects on encoded image features using convolutional neural networks and attention mechanisms.

## How It Works

The implementation uses a `LatentReverb` neural network that operates in the latent space of diffusion models:

### Core Architecture

- **Reflection System**: Creates multiple delayed reflections using learnable parameters for weights, delays, and diffusion
- **Spatial Processing**: Uses 2D convolutions to process spatial features and maintain image coherence
- **Attention Mechanism**: Applies multi-head attention for spatial coherence across the image
- **Feedback Network**: Implements a feedback loop that creates increasingly complex reflection patterns
- **Dampening Network**: Frequency-dependent decay using learned convolutional layers

### Key Components

1. **Delay Line**: Creates spatially shifted versions of the input using `torch.roll` with fade masks
2. **Reflection Processing**: Each reflection is processed through convolutional layers and scaled by decay rates
3. **Spatial Attention**: Multi-head attention ensures spatial coherence across the image
4. **Adaptive Scaling**: Automatically adjusts effect strength based on the number of reflections

### Technical Implementation

The system operates on 4D tensors `[Batch, Channels, Height, Width]` and:
- Scales delays by room size and reflection count for consistent visual impact
- Applies exponential decay to each reflection layer
- Uses learnable parameters for reflection weights, delays, and diffusion
- Implements cross-channel feedback for complex interaction patterns
- Applies post-processing effects like blur, edge enhancement, and contrast adjustment

## Features

- **Neural Reverb Processing**: AI-powered reverb effects in latent space
- **Spatial Echo Effects**: Creates realistic spatial reflections and echoes
- **Learnable Parameters**: Automatically optimizes reflection patterns
- **Adaptive Scaling**: Maintains consistent visual impact across different settings
- **Real-time Processing**: Efficient GPU-accelerated computation
- **ComfyUI Integration**: Seamless workflow integration with parameter controls

## Node Parameters

The `LatentReverb` node provides intuitive controls:

- **`wet_mix`** (0.0-1.0): Balance between original and processed image
- **`feedback`** (0.0-1.5): Controls reflection complexity and layering
- **`room_size`** (0.05-4.0): Spatial scale of reflections and effects
- **`num_reflections`** (2-32): Number of reflection layers for complexity
- **`decay_rate`** (0.5-0.95): How quickly reflections fade over time

## Usage Examples

### Subtle Ambient Enhancement
```
wet_mix: 0.2
feedback: 0.3
room_size: 0.3
num_reflections: 8
decay_rate: 0.85
```

### Dramatic Echo Effects
```
wet_mix: 0.6
feedback: 0.8
room_size: 2.0
num_reflections: 24
decay_rate: 0.7
```

### Natural Room Reverb
```
wet_mix: 0.4
feedback: 0.5
room_size: 1.0
num_reflections: 16
decay_rate: 0.8
```

## Installation

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
1. Look up this extension in ComfyUI-Manager. If you are installing manually, clone this repository under `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

## Develop

To install the dev dependencies and pre-commit (will run the ruff hook), do:

```bash
cd latent_reverb
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

The main implementation is located in [nodes.py](src/latent_reverb/nodes.py). The `LatentReverb` class implements the neural network architecture, while `LatentReverbNode` provides the ComfyUI interface. To learn more about custom nodes, read the [docs](https://docs.comfy.org/essentials/custom_node_overview).

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

A Github action will run on every git push. You can also run the Github action manually. Full instructions [here](https://docs.comfy.org/registry/publishing). Join our [discord](https://discord.com/invite/comfyorg) if you have any questions!

