# Multiple LoRA Loader for ComfyUI

A collection of custom nodes for ComfyUI that allow working with LoRAs and trigger words by index selection.

## Installation

1. Place these files in a folder named `ComfyUI-loras-loader` inside the `custom_nodes` directory of your ComfyUI installation
2. Restart ComfyUI
3. The nodes will appear in the node menu

## Available Nodes

### LoRA Loader (by Index)

Loads a LoRA by its numerical index in your sorted loras folder.

#### Inputs

- **model**: The base model to apply the LoRA to
- **index**: The numerical index of the LoRA in your alphabetically sorted loras folder
- **lora_list**: A dropdown showing all available LoRAs (the selection is visual only, the index determines which one is loaded)
- **strength_model**: The strength to apply to the model part of the LoRA
- **strength_clip**: The strength to apply to the CLIP part of the LoRA
- **clip** (optional): The CLIP model to apply LoRA to (if applicable)

#### Outputs

- **MODEL**: The model with the LoRA applied
- **CLIP**: The modified CLIP model (if provided)

### LoRAname (by Index)

Returns a LoRA filename selected by index from a list of user-defined LoRA names. This can be connected directly to a standard "Load LoRA" node.

#### Inputs

- **index**: The numerical index to select from the LoRA names list
- **LoRAnames**: Multiline text input with one LoRA filename per line

#### Outputs

- **lora_name**: The selected LoRA filename, compatible with the standard "Load LoRA" node

### Trigger Words (by Index)

Returns a text string selected by index from a list of user-defined trigger words or phrases.

#### Inputs

- **index**: The numerical index to select from the trigger words list
- **triggers**: Multiline text input with one trigger word or phrase per line

#### Outputs

- **STRING**: The selected trigger word or phrase

## Example Workflows

### Basic Index Selection

1. Load a base model with a checkpoint loader
2. Connect the model to the "LoRA Loader (by Index)" node
3. Set the index to select a specific LoRA (e.g., 0 for the first LoRA alphabetically)
4. Adjust strength_model and strength_clip as needed
5. Use the output model for your image generation

### Dynamic LoRA Selection

1. Create a "LoRAname (by Index)" node
2. Enter your desired LoRA filenames in the multiline text field
3. Connect its output to a standard "Load LoRA" node's lora_name input
4. Change the index to dynamically select different LoRAs
5. Connect your model and adjust strength as needed

### Using Trigger Words

1. Create a "Trigger Words (by Index)" node
2. Enter your trigger words/phrases in the multiline text field
3. Connect its output to a text input in your workflow
4. Change the index to dynamically select different trigger words
