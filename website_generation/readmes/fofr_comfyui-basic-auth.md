# ComfyUI Basic Auth

A simple authentication middleware for ComfyUI that adds basic HTTP authentication to protect your ComfyUI instance.

## Features

- Basic HTTP Authentication protection for ComfyUI
- Simple username/password configuration
- Lightweight and easy to set up
- Compatible with all ComfyUI versions

## Installation

1. Navigate to your ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/fofr/comfyui-basic-auth
```

## Configuration

Set environment variables for your username and password:

```bash
export COMFYUI_USERNAME=your_username
export COMFYUI_PASSWORD=your_password
```

Restart ComfyUI for the changes to take effect.

## Usage

The authentication will automatically be active once the node is installed and configured. When accessing ComfyUI, you will be prompted for the username and password you specified in the environment variables.

## Security Note

Basic authentication sends credentials encoded (not encrypted) in the HTTP header. While this provides a basic level of protection, it's recommended to:

- Use strong passwords
- Access ComfyUI through HTTPS if exposed to the internet
- Consider additional security measures for production environments
