# unwdef Custom Nodes for ComfyUI

This is a work in progress repo. 

## Randomize LoRAs Node
The Randomize LoRAs node randomly loads LoRAs based on a predefined selection with also randomized weights. This enables users to experiment with different artistic effects on their generated images.

![nodes_lora](https://github.com/unwdef/unwdef-nodes-comfyui/assets/166751903/e3ae5179-06ac-4154-94a9-1fb31a47fe35)
Note: The "Show Text" node is part of [pythongosssss/ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)

There is also a "stack" version for working with other lora nodes with the stacking functionality such as [Efficiency Nodes](https://github.com/jags111/efficiency-nodes-comfyui)

### How It Works
Connect the **model** and **clip** outputs from this node to your KSampler or other processing nodes. The output, **chosen loras**, provides a textual representation detailing which LoRAs and corresponding weights were applied during the generation.

You can also provide the **trigger words** for each lora. They will be outputted as a formatted text separated by commas. Useful for you to concatenate the trigger words into your prompts.

### Configuration Fields
- **seed**: Ensures reproducibility. Maintain the same seed for consistent results across generations. _Note: Keep the same selected loras for this to work._
- **max_random**: Limits the maximum number of LoRAs to apply. Even if you select up to 10, you can choose to apply fewer.
- **lora_x**: Specifies the LoRA file to use.
- **min_str_x** and **max_str_x**: Defines the minimum and maximum strengths for each LoRA, allowing for a range of intensities.
- **trigger_words_x**: The trigger words for the selected lora.

## Random Text from Multiline Node
Will output one (or multiple) lines from a multiline text component.

![node_random_text_from_multiline](https://github.com/unwdef/unwdef-nodes-comfyui/assets/166751903/432196cc-067f-4f84-9ca4-769d3a3c46d7)

## Text Multiline with Variables

Will replace instances of !var_x in your text with the contents of the var_x inputs.

![nodes_text](https://github.com/unwdef/unwdef-nodes-comfyui/assets/166751903/cd9c0724-1dcc-426b-b66e-6e733b3be264)


## Installation
You can use the [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager). Search for "unwdef" or "unwdef-nodes".

Or you can install it manually:

1. Open your terminal and navigate to your `ComfyUI/custom_nodes` directory.
2. Clone the repository using:
   ```
   git clone https://github.com/unwdef/unwdef-nodes-comfyui.git
   ```
3. Restart ComfyUI to apply the changes.  

### Uninstallation
To remove the custom node:
1. Delete the `unwdef-nodes-comfyui` directory from `ComfyUI/custom_nodes`.
2. Restart ComfyUI to apply the changes. 

### Updates
To update the node:

1. Navigate to `ComfyUI/custom_nodes/unwdef-nodes-comfyui` in your terminal.
2. Run the following command: `git pull`
3. Restart ComfyUI to apply the changes. 
