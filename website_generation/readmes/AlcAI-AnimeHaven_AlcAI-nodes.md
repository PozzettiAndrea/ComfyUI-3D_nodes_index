# AlcAI Nodes for ComfyUI

[![ComfyUI](https://img.shields.io/badge/ComfyUI-EAEAEA?style=for-the-badge&logo=comfyui&logoColor=white)](https://github.com/comfyanonymous/ComfyUI) [![GitHub Repo stars](https://img.shields.io/github/stars/AlcAI-AnimeHaven/AlcAI-nodes?style=social)](https://github.com/AlcAI-AnimeHaven/AlcAI-nodes)

## Overview

AlcAI Nodes is a collection of custom nodes for **ComfyUI**, a modular interface for image generation with Stable Diffusion. This project focuses on tools optimized for creating anime-style images and stylized effects, inspired by the AnimeHaven universe. It aims to simplify workflows for artists and AI creativity enthusiasts.

## Installation

### Prerequisites
- ComfyUI installed and functional.
- Python 3.10+ and pip.
- Git for cloning the repo.

### Manual Installation (Recommended)

1. Navigate to the `custom_nodes` folder in your ComfyUI installation:
   ```
   cd path/to/ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```
   git clone https://github.com/AlcAI-AnimeHaven/AlcAI-nodes.git
   ```

3. Restart ComfyUI. The new nodes should appear in the available nodes list.

## Usage

For advanced examples, import JSON workflow files from the `workflows/` folder and put them in the `user/default/workflows` folder.

## Dependencies

- `torch` and `torchvision` (already included in ComfyUI).

## Contributing

Contributions are welcome! 
- Fork the repo.
- Create a branch for your feature (`git checkout -b feature/new-node`).
- Commit your changes (`git commit -m "Add node X"`).
- Push to the branch (`git push origin feature/new-node`).
- Open a Pull Request.

Ensure you follow ComfyUI's code guidelines (nodes based on `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS` in `__init__.py`).

## License

This project is not licensed

## Support and Contact

- **Author**: AlcAI-AnimeHaven
- **Issues**: Open an issue on GitHub for bugs or suggestions.