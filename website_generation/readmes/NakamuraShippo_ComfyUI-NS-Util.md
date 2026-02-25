# ComfyUI-NS-Util
[日本語README](https://github.com/NakamuraShippo/ComfyUI-NS-Util/blob/main/README_JP.md)

A collection of nodes for ComfyUI.

This consolidates the previously created nodes into one package.

[Please see the wiki for an explanation of each node.](https://github.com/NakamuraShippo/ComfyUI-NS-Util/wiki)

## Node Contents

### Utility
Contains useful nodes.
### Graphics Filter
A filter that applies special effects to images.
### LLM(Implementing the tests now.)
Functions for connecting to and interacting with external LLM services. Local LLM supports Ollama.

## Installation

### If you have [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) installed
1. Click Main Menu -> Manager -> Install via Git URL
2. Paste the URL into the text box that appears at the top of the window and press OK  
    https://github.com/NakamuraShippo/ComfyUI-NS-Util
3. Once installation is complete, restart ComfyUI

### If you don't have [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) installed
1. Navigate to ComfyUI's custom nodes directory (usually ComfyUI/custom_nodes/)
2. Clone this repository:  
`git clone https://github.com/NakamuraShippo/ComfyUI-NS-Util`
3. Restart ComfyUI
4. In ComfyUI\venv\Scripts, Shift+right-click -> Open terminal -> activate
  ```python
pip install pyyaml watchdog
  ```
## Usage
Each node page of the wiki is written in both Japanese and English.

[wiki](https://github.com/NakamuraShippo/ComfyUI-NS-Util/wiki)

## Requirements

- ComfyUI (0.3 or later recommended, other versions not tested)
- Python packages (automatically included with ComfyUI):
  - pyyaml
  - watchdog
  - aiohttp
  - opencv-python

## Roadmap

This is the first node in the NS-Util collection. Future additions planned:
 - [ManySliders](https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders)
   - Will be redesigned to be switchable with presets before addition

## Contributing

Contributions are welcome! Feel free to submit pull requests or create issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter problems or have questions:
- Create an issue on GitHub
- [Nakamura Shippo lit.link](https://lit.link/nakamurashippo)

## Acknowledgments

- Thanks to the ComfyUI team for creating an amazing platform
- Thanks to AI animals for giving me ideas
