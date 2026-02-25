# ComfyUI-Orchestration-Toolkit

A custom node pack for ComfyUI that improves prompt handling and workflow control.

## Included Nodes

###  PromptOrchestrator

A structured prompt management node that allows loading two different text files from separate folders directly into editable fields inside ComfyUI with a single click.  
It automatically loads the most recently added text file from each folder and provides two independent editors with one-click content transfer between them and flexible output switching for efficient prompt handling.

![PromptOrchestrator](assets/PromptOrchestrator.png)

###  Dynamic Node State Controller

A workflow control node that allows you to enter the ID of any node and define what should happen to it when pressing the apply button.  
You can mute, unmute, bypass, or unbypass any number of nodes with a single click — without adding additional connections to the canvas.

![Dynamic Node State Controller](assets/DynamicNodeStateController.png)

## Installation

Install directly via the ComfyUI Manager.

Alternatively, clone the repository into your `ComfyUI/custom_nodes/` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/flows-and-frames/ComfyUI-Orchestration-Toolkit.git
