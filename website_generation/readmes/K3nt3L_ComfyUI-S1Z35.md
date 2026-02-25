# ComfyUI-S1Z35
Basic nodes for image ratios and size presets (all models)

Presets for :
- SDXL,
- Flux 1,
- Flux 2,
- Z Image turbo,
- Qwen Image,
- Hunyuan Image,
- Custom node 01,
- Custom node 02.

## What ?

The purpose of this node is to allow you to use your preferred image sizes. You can redefine each of the CSV files as needed.

Additionally, it offers the option to switch from landscape mode (default) to portrait mode.

## How ?

You can change the resolutions and aspect ratios of each node by modifying the CSV files located in the **"preset"** directory:

`\custom_nodes\ComfyUI-S1Z35\presets`

---

Example (content of **zit.csv**):

```
1024, 1024, Square (1:1)
1152, 896, Landscape (4:3)
896, 1152, Portrait (3:4)
1216, 832, Landscape (3:2)
832, 1216, Portrait (2:3)
1344, 768, Cinematic (16:9)
768, 1344, Vertical (9:16)
1536, 640, Ultra Wide (21:9)
1280, 1280, Square HD
1472, 1104, 4:3 HD
1536, 1024, 3:2 HD
1600, 896, 16:9 HD
```


---

The **custom1.csv** and **custom2.csv** files allow you to create your own presets.
