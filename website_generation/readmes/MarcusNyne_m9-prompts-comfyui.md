# ComfyUI: m9 Prompts

Custom nodes for [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI).

Two custom nodes are included for modifying a prompt to create prompt variations.
   * ScramblePrompts [m9]: Reorder prompts, remove prompts, modify weights
   * TweakWeights [m9]: Modify the weights of prompts matching keywords

## Overview

You may use these nodes as your positive/negative prompt, or combine them with other prompt nodes.

### Common Connectors

   * **clip**: Input. Standard clip connector
   * **conditioning_optional**: Input (optional). If you have another prompt node, you may combine the output of both nodes by connecting the CONDITIONING output of the other node into this input.
   * **CONDITIONING**: Output. Standard output. Connect this to your KSampler input.
   * **seed_optional**: Input (optional).  Recommended to convert this to an input when you want the variation to be deterministic based on the seed.  Otherwise, the same seed could produce different variants.

### Common Fields

   * **prompt**: This is the text prompt that will be modified to create a variation. The extent to which the text prompt is modified depends on node settings.
   * **print_output**: When enabled, output will be sent to the command window describing the new prompt.

## ScramblePrompts [m9] 

Modifications to the prompt may include:
   * Changing the order of prompts
   * Removing prompts
   * Changing the weight of prompts

A 'prompt' is a phrase between commas, but not inside of parenthesis.  If you have parenthesis between commas, it is considered a single prompt.  For example:
- prompt one, prompt two
- prompt (one), prompt two
- (prompt, one), prompt two

### Prompt Order

  * **order_prompts_percent**: The percent of prompts to reorder.

### Prompt Reduction

   * **remove_prompts_percent**: The number of prompts to remove.
     * prompts are removed entirely
     * Does not include Loras
   * **keep_prompts**: A list of keywords for prompts to keep.
     * As long as a prompt includes the specified keyword, it will not be removed
     * Comma delimited

### Prompt Weight

   * **modify_weights_percent**: The percent of prompts that will have the weight changed.
   * **weight_range**: The maximum amount to modify the weight in either direction.
     * If a change would take the weight below zero, the weight will be left as is
   * **max_weight**: Maximum final weight.
     * When a change will take the weight over the max, the change is not made
     * For example, if the weight is 1, the max is 1.2, and the change is +0.3, the weight will be left at 1

## Example Workflows

Example workflows can be found in the two included example images, that use the **ScramblePrompts [m9]** node.

## ScramblePromptsExample-1.png

In this example workflow, the positive "CLIP Text Encode (prompt)" is replaced with a **ScramblePrompts [m9]** node.  ComfyUI will cache the results of nodes to make generation more efficient.  If you use this node without an input into **seed_optional**, the prompts will only be randomized the first time, with the results cached and reused.

By adding a seed primitive, and connecting it to **seed_optional**, the node will be reevaluated for each run, resulting in a different result for each image.

**print_output** is enabled, allowing you to see the results of prompt scrambling in the console window.

## ScramblePromptsExample-2.png

In this example, the **ScramblePrompts [m9]** node is used in conjunction with the existing positive "CLIP Text Encode (prompt)".  The prompts within the text encoder and left as is, and the scrambled prompts are added to them in the final prompt sent to the sampler.

## Help and Feedback

   * **Discord Server**
     * https://discord.gg/trMfHcTcsG

## m9 Prompts Catalog

   * **Scramble Prompts for Stable Diffusion**
     * Works with Automatic1111
     * Reorder, remove, modify weights of prompts
     * https://github.com/MarcusNyne/sd-scramble-prompts-m9

   * **Tweak Weights for Stable Diffusion**
     * Works with Automatic1111
     * Modify prompt weights using keywords
     * https://github.com/MarcusNyne/sd-tweak-weights-m9

   * **m9 Prompts for ComfyUI**
     * Works with ComfyUI
     * Includes nodes for Scramble Prompts and Tweak Weights
     * https://github.com/MarcusNyne/m9-prompts-comfyui
