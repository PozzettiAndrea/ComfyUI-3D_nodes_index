# VAE Decode Switch for ComfyUI

A simple but powerful utility node for ComfyUI that allows you to switch between the standard `VAE Decode` and the `VAE Decode (Tiled)` nodes without rewiring your workflow.

This node is designed to keep your graphs clean and make A/B testing different decoding methods quick and easy.

![VAE Decode Switch Demo](https://i.imgur.com/jVLfvfl.png)

---

## Features

* **Seamless Switching:** A simple dropdown menu lets you select either the "default" or "tiled" VAE decoder on the fly.
* **Dynamic UI:** The node's interface is dynamic. When "default" is selected, the extra settings for the tiled decoder (like `tile_size`, `overlap`, etc.) are completely hidden, keeping the node compact and clean.
* **Clean Workflows:** Avoid messy rerouting nodes or having to manually disconnect and reconnect pipelines when you want to try a different decoder.
* **Preserves Inputs:** All standard inputs (`samples`, `vae`) are maintained, and the node correctly passes the required parameters to the selected decoder.

---

## Installation

1. Navigate to your ComfyUI installation directory.
2. Go into the `custom_nodes` folder.
3. Download or clone this repository into the `custom_nodes` folder. Ensure the final folder structure looks like this:
   ```
   ComfyUI/
   └── custom_nodes/
       └── VAE-Decode-Switch/
           ├── __init__.py
           ├── vae_decode_switcher.py
           └── js/
               └── vae_decode_switcher.js
   ```
4. Restart ComfyUI completely.

---

## Usage

1. After restarting ComfyUI, you can add the node by:
   * Right-clicking on the graph and selecting `Add Node` -> `Logic/Switchers` -> `VAE Decode Switch`.
   * Double-clicking the graph and searching for "VAE Decode Switch".
2. Connect your `samples` (LATENT) and `vae` (VAE) inputs as you would with a standard decoder.
3. Use the `select_decoder` dropdown to choose your desired method.
   * **default:** Uses the standard `VAEDecode`. The node will shrink to hide the other settings.
   * **tiled:** Uses the `VAEDecodeTiled`. The node will expand to show the tiled-specific settings.
