# ComfyUI Smart Helper Nodes

A collection of helper nodes for ComfyUI with smart functionality.

## Nodes

### Smart Prompt
A node that provides syntax highlighting for prompts, with support for comments (//), punctuation and float (weight) values.
The node also removes all comments from the output string.

![SmartPrompt](img/SmartPrompt.png)

### Smart Remove Comments

A simple node that removes // comments from the string.

![SmartRemoveComments](img/SmartRemoveComments.png)

### Smart Format String, Smart Format String (10 params)
A node that formats a string with placeholders for input parameters and date/time.

![SmartFormatString](img/SmartFormatString.png)

### Smart HV LoRA Select, Smart HV LoRA Stack
Nodes for selecting and stacking HunyuanVideo LoRA files.
Also outputs a human-readable string of the LoRA file name and parameters (for example to save to a file).

![SmartHVLoraSelect](img/SmartHVLora.png)

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes` directory: 