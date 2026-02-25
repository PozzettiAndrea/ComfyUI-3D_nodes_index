# comfyui-RandomPromptsZveroboy

Custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI)  that fixes an existing node [comfyui-dynamicprompts](https://github.com/adieyal/comfyui-dynamicprompts).

![comfy-random](https://github.com/thezveroboy/comfyui-RandomPromptsZveroboy/blob/main/image.jpg)

## Features
- This node finally fixes some annoying issues related to incorrect generation of random values on the original node, which made generations monotonous and multiple choices related.
- The new node does everything the old one did, but:
   - The choices are truly random
   - There are no weird connections between different choice blocks

## Requirements
- Installed ComfyUI.
- Don't forget to put your wildcards in the folder /ComfyUI/custom_nodes/comfyui-RandomPromptsZveroboy/wildcards/

## Installation

1. Clone this repo into custom_nodes folder
   ```bash
   git clone https://github.com/thezveroboy/comfyui-RandomPromptsZveroboy.git
      ```
2. Run ComfyUI

