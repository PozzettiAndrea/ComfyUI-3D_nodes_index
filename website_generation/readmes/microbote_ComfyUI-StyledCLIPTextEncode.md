# StyledCLIPTextEncode, a Style-Decorated Prompt Node for ComfyUI

StyledCLIPTextEncode is a node that enables you to build your prompts(both postive and negative) based on the selected style. 
It provides up-to 77 styles  currently and has been tested  on SDXL and SD1.5 checkpoints. 
It's ported from project [Style Selector for SDXL 1.0](https://github.com/ahgsql/StyleSelectorXL), which is only availabe on WebUI.


### StyledCLIPTextEncode
![StyledCLIPTextEncode Screenshot](examples/style-demo.png)

- the first conditioning output is Positive.
- the second conditioning output is Negative.


### Installation

To install and use the SDXL Prompt Styler nodes, follow these steps:

1. Open a terminal or command line interface.
2. Navigate to the `ComfyUI/custom_nodes/` directory.
3. Run the following command:
```git clone https://github.com/microbote/ComfyUI-StyledCLIPTextEncode.git```
4. Restart ComfyUI.

This command clones the SDXL Prompt Styler repository into your `ComfyUI/custom_nodes/` directory. You should now be able to access and use the nodes from this repository.

### Inputs
                "clip": ("CLIP",),
                "positive_prompt": ("STRING", {"default": "", "multiline": True, "dynamicPrompts": True}),
                "negative_prompt": ("STRING", {"default": "", "multiline": True, "dynamicPrompts": True}),
                "select_style": (cls.getStyleList(),)
* **clip** - CLIP from the model
* **positive_prompt** - text for the positive base prompt
* **negative_prompt** - text for the negative base prompt
* **select_style** - choose the style you want to use

### Outputs

* **CONDITIONING** - the first  conditioning with style for positive prompt
* **CONDITIONING** - the second conditioning with style for negative prompt
