# Remote Upscale for ComfyUI

Offload image upscaling to a remote server with a dedicated GPU. Useful when your main ComfyUI machine has limited VRAM or when you want to use a different GPU for upscaling tasks.

## Features

- Remote upscaling via HTTP API
- Real-time progress bar in ComfyUI
- Support for `.pth`, `.pt`, and `.safetensors` upscale models
- Configurable tile size for memory management
- Model caching on server for faster subsequent runs

## Installation

### ComfyUI Node (Client)

1. Copy the `remote_upscale` folder to your ComfyUI `custom_nodes` directory
2. Restart ComfyUI
3. The "Remote Upscale" node will appear in the "image/upscaling" category

### Upscale Server

1. Copy the `server` folder to your remote machine
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install PyTorch with CUDA/ROCm support appropriate for your GPU
4. Set the models path and run:
   ```bash
   export UPSCALE_MODELS_PATH="/path/to/your/upscale_models"
   python server.py
   ```

The server will start on port 8189 by default.

## Usage

1. Start the upscale server on your remote machine
2. In ComfyUI, add the "Remote Upscale" node
3. Set the `server_url` to your server address (e.g., `http://192.168.1.100:8189`)
4. Select a model from the dropdown
5. Connect an image input and run the workflow

### Node Parameters

- **server_url**: URL of the remote upscale server
- **model_name**: Upscale model to use (fetched from server)
- **tile_size**: Tile size for processing large images (default: 512)
- **show_progress**: Enable progress bar during upscaling

### Refresh Models

Use the "Refresh Remote Models" node to update the model list from the server.

## Server API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/models` | GET | List available models |
| `/upscale` | POST | Upscale image (no progress) |
| `/upscale_stream` | POST | Upscale with SSE progress |
| `/result/{id}` | GET | Fetch result after streaming |
| `/health` | GET | Server health check |

## Requirements

### Client (ComfyUI)
- requests

### Server
- fastapi
- uvicorn
- python-multipart
- torch (with CUDA or ROCm)
- torchvision
- spandrel
- pillow
- numpy

## License

MIT
