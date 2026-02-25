# ComfyUI-Otacoo

ComfyUI custom nodes for loading checkpoints and LoRAs with **model image previews** in the selector.

## Nodes

### Checkpoint Loader 🔰

- Loads a checkpoint (MODEL, CLIP, VAE) just like the built-in loader.
- **Optional separate VAE:** Choose “default” to use the checkpoint’s built-in VAE, or pick another VAE from your `models/vae` folder.
- **Preview grid:** Select your model using a grid with preview images.

### LoRA Loader 🔰

- Apply **any amount of LoRAs** in one node, each with its own **model strength** and **toggle**.
- **Preview grid:** Select your model using a grid with preview images.
- **Trigger Words:** Extracts and outputs each LoRAs trigger words by reading **.json** or **.metadata.json** files.

### Global Sampler 🔰

- Globally set the **sampler** and **scheduler** for all nodes in the workflow.

## Preview images

Previews are loaded from **ComfyUI’s model folders** (same folder as the model file). Place an image next to the model with the same base name:

| Model file | Preview file (any of these) |
|------------|----------------------------|
| `example.safetensors` | `example.preview.jpg`, `example.png`, etc. |

**Names checked (first match wins):**  
`<basename>.preview.png`, `.preview.jpg`, `.preview.jpeg`, `.preview.webp`  
`<basename>.png`, `.jpg`, `.jpeg`, `.webp`

## Adding support for Pythongossss' View Info... feature

Go into ComfyUI settings > pysssss > ModelInfo

For Checkpoints add: `OtacooCheckpointLoader.ckpt_name.*`\
For LoRAs add: `OtacooLoraLoader.lora_name.*`

## Installation

Clone or copy into `ComfyUI/custom_nodes/`:

```git clone https://github.com/otacoo/comfyui-otacoo.git```


## Nodes 2.0

Currently previews only work with **LiteGraph.**\
**Nodes 2.0** support will be added once ComfyUI adds support for custom nodes in Vue UI.
