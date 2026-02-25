# ComfyUI and Claude
A set of custom nodes that are using Anthropic's Claude models for describing images and transforming texts.

## Setup

You can find the node in the ComfyUI package registry via its name "ComfyUI
Claude" and install it from there. Alternatively, clone the repository into your
custom nodes folder and install the requirements:

```bash
git clone https://github.com/tkreuziger/comfyui-claude.git ./ComfyUI/custom_nodes/comfyui-claude
python3 -m pip install -r ./ComfyUI/custom_nodes/comfyui-claude/requirements.txt
```

Then restart ComfyUI.

## Requirements

You need an Anthropic API key that you must fill in the nodes. Learn more about
this [here](https://docs.anthropic.com/en/api/getting-started).

## Included nodes

1. DescribeImage: Takes an image as input and returns a textual description of
   it.
2. CombineTexts: Combine two texts into something new with the help of Claude.
3. TransformText: Transforms an input text into some other text, ideal for
   rephrasing prompts or similar.

