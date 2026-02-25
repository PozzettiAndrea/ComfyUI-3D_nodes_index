## ComfyUI Workflow Graphics

<img width="1397" height="919" alt="image" src="https://github.com/user-attachments/assets/f117d0a6-833b-4a3a-8d20-fa6ae1d760ea" />


Embed images directly in your workflow JSONs, useful for workflow branding, visual guides and much more!

### Install
- Clone this repo inside your custom_nodes folder `git clone https://github.com/pixelworldai/ComfyUI-WorkflowGraphics.git`
- Restart ComfyUI.

### Usage
1. Add the node by searching for `Workflow Graphics`.
2. Open the node’s panel (double‑click the node or use the right‑side properties).
3. Paste an image base64:
   - Example: `data:image/png;base64,...`

A great place to convert your PNGs to Base64: https://www.base64-image.de/ - Once converted click "copy image"
<img width="1535" height="842" alt="image" src="https://github.com/user-attachments/assets/f313786a-a1a6-4a68-8fda-d5d07a01d053" />

4. Adjust:
   - `Scale (%)`: 0–100 of the image’s natural size
   - `Opacity`: 0..1
   - `Background Color`: any CSS color or `transparent` - Great for adding background colors to transparent PNGs
   - `Border Radius`: radius in pixels - Add rounded edges to image
5. Pin the node (ComfyUI pin) to allow click‑through over the canvas while keeping it visible.
6. Use the context menu item `Reload Workflow Graphics` to reload node once you paste the base64 string, as it does not appear automatically after pasting, alternatively you can refresh the page.

   <img width="423" height="255" alt="image" src="https://github.com/user-attachments/assets/27b146f3-fb78-4b59-84da-a13c06ae8e6d" />


Notes:
- This is a frontend‑only node; it does not participate in execution.
- The node size auto‑matches the displayed image dimensions.

### Support
If you like this node, please support development of this and future projects here: https://ko-fi.com/pixelworldai <3


