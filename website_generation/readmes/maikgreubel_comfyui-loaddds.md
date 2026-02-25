# Load DDS File Node

A simple node for loading DDS (DirectDraw Surface) texture files into a PyTorch tensor.  
The node is designed to be used in visual programming frameworks that support custom nodes (e.g., ComfyUI, AUTOMATIC1111).

## Features

- **Secure file loading** – prevents directory traversal by validating the absolute path against the input folder.
- **DDS format validation** – ensures the file is a DDS texture before processing.
- **Alpha handling** – automatically strips the alpha channel if it is fully opaque or fully transparent.
- **Normalization** – pixel values are converted to `[0, 1]` range and returned as a `torch.Tensor`.
- **Supports multiple DDS formats** (compressed/uncompressed) via Wand.

## Installation

Clone the repository into the custom_nodes directory of your ComfyUI installation.

```bash
cd comfyui/custom_nodes
git clone https://github.com/maikgreubel/comfyui-loaddds.git
```

Restart your ComfyUI instance to enable the node.

## Usage

Add the node **Load DDS File** to your workflow.  
Select an image from the dropdown; the node will output a tensor of shape `[1, H, W, C]`.  
The tensor can be fed into downstream PyTorch models or converted back to an image.

Now you are able to embed the loading for DDS textures into workflows.

Use https://comfy.icu/node/DDSSaveImage for doing the opposite and save the DDS file.

## License

See LICENSE file.

## Contributing

Feel free to open issues or pull requests.  
Make sure tests pass and documentation stays up‑to‑date.
