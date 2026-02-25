# ComfyUI Together.ai FLUX API Node

A custom node implementation for ComfyUI that integrates with Together.ai's FLUX image generation models. This project is inspired by and adapted from [ComfyUI-FLUX-BFL-API](https://github.com/gelasdev/ComfyUI-FLUX-BFL-API) to work with the Together.ai API.

## Features

- Direct integration with Together.ai's FLUX models
- Support for FLUX.1-schnell-Free model
- Configurable parameters including steps, guidance scale, and dimensions
- Negative prompt support
- Error handling and retry mechanisms



## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/BZcreativ/ComfyUI-FLUX-TOGETHER-API.git
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

OR From the Comfyui Folder
```bash
 ./python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-FLUX-TOGETHER-API\requirements.txt
```

3. Create a `config.ini` file in the root directory with your Together.ai API key:
```ini
[API]
together_api_key = your_api_key_here
```

## Configuration

1. Get your API key from [Together.ai](https://together.ai)
2. Copy the `config.ini.example` to `config.ini`
3. Add your API key to the configuration file

## Usage

1. Start ComfyUI
2. Find the "Together API Node" in the node browser
3. Configure the parameters:
   - Prompt: Your image generation prompt
   - Negative Prompt: Elements to avoid in the generation
   - Steps: Generation steps (1-100)
   - Width: Image width (512-2048)
   - Height: Image height (512-2048)
   - Seed: Generation seed
   - CFG: Guidance scale (0.0-20.0)

For detailed usage instructions, see [USAGE.md](USAGE.md)

## Parameters

| Parameter | Type | Range | Default | Description |
|-----------|------|--------|---------|-------------|
| prompt | string | - | "" | Main generation prompt |
| negative_prompt | string | - | "" | Elements to avoid |
| steps | integer | 1-100 | 20 | Number of generation steps |
| width | integer | 512-2048 | 1024 | Image width |
| height | integer | 512-2048 | 1024 | Image height |
| seed | integer | 0-MAX_INT | 0 | Generation seed |
| cfg | float | 0.0-20.0 | 7.0 | Guidance scale |

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Credits

- This project is inspired by and adapted from [ComfyUI-FLUX-BFL-API](https://github.com/gelasdev/ComfyUI-FLUX-BFL-API)
- Together.ai for providing the FLUX API
- ComfyUI team for the amazing framework

## Author

Created by [BZcreativ](https://github.com/BZcreativ)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Example
![image](https://github.com/BZcreativ/ComfyUI-FLUX-TOGETHER-API/blob/master/nodes.png)