# ComfyUI Preview Image with Pause

A simple custom node that:
- Previews the generated image directly on the node
- Pauses the workflow until you click **✔️ Continue** or **⛔ Cancel**
- Passes the IMAGE forward if you continue (perfect before Save Image, Upscale, etc.)

## Features
- Shows preview **before** pausing (no more delayed/missing previews)
- Buttons right on the node
- Cancel interrupts the current prompt run
- Works with batches (though best with batch_size=1 for review)

## Installation
**ComfyUI Manager**
- Search for `ComfyUI-ImagePreviewPause` and press install

**In ComfyUI Manager (Legacy) → Install via Git URL:**
- Paste: `https://github.com/Cordux/ComfyUI-PreviewPause.git`  
- Restart ComfyUI

**Manual installation:**
- open command prompt in your `ComfyUI/custom_nodes/` folder
- `git clone https://github.com/Cordux/ComfyUI-PreviewPause.git`
- into your `ComfyUI/custom_nodes/` folder

## Usage
- Connect: VAE Decode → Preview Image with Pause → Save Image (or whatever next step)
- Queue prompt → image appears on node → decide → click Continue to save, or Cancel to stop

## Screenshot
<img width="286" height="701" alt="image" src="https://github.com/user-attachments/assets/cbda858e-8b2d-4547-a3db-6ff926b8ed20" />


## Notes
- Uses temp folder for previews (auto-cleaned by ComfyUI)
- Small delay (0.3s) to ensure preview renders — can be adjusted in code
- Best with batch_size = 1 (multiple images show, but you can only approve/cancel the whole batch)
- Requires ComfyUI restart after install

## Issues & Contributing
Found a bug? Want a feature like "Regenerate" button or adjustable delay?  
Feel free to open an issue or PR on GitHub!

[MIT License](LICENSE)


