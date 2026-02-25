# Lora Info for ComfyUI

Shows Lora Base Model, Trigger Words and Examples. Pulls data from CivitAI


Special thanks to:

- `badjeff` for doing all the actual hard work (https://github.com/badjeff/comfyui_lora_tag_loader)
- `alessandroperilli` for all the feedback.

![image](preview.png)


## Example Usage

![image](lorainfo_example.gif)

## Youtube Tutorials
- `Joe Conway` (https://www.youtube.com/watch?v=uU4jUV4rm_A)
- `스페이스 플라워` (https://www.youtube.com/watch?v=1XNQQ63MfLs)


## Installation

#### Method 1. 
Open ComfyUI Manager, search for "lorainfo", or "jitcoder", click install

#### Method 2.

Inside ComfyUI/custom-nodes

```sh
git clone https://github.com/jitcoder/lora-info.git
```

#### Method 3.

Download this repo as a zip and extract in the custom-nodes directory.


## FAQ

>Q: How do I connect this node's outputs (trigger_words, example_prompt, lora_name) to other nodes?
>
>A: This node's outputs are of type `STRING`, therefore you can connect this node to ANY node that takes `STRING` or `TEXT` types as input.

>Q: What node did you use in the screenshot?
>
>A: The node in the screenshot is RGThree's display any node. But you can use any node that takes `STRING` or `TEXT` as input.

>Q: I connected my nodes and nothing happens. I see LoRA info updated in the node, but my connected nodes aren't reacting or doing anything or showing anything.
>
>A: Click on "Queue Prompt." In ComfyUI inputs and outputs of nodes are only processed once the user queues a prompt


#
#
#

### Note: Contains two Nodes
Apologies for shoving another node into this repo, I'll eventually create a new repo for the Image From URL 

- Lora Info
- Image From URL

## Image From URL

Loads an image from the URL and makes it available for use in your workflow. This is especially useful if you intend on 
sharing your workflows and want to make it easier for users to use them instead of having to download images separately.

![image](image-from-url.png)