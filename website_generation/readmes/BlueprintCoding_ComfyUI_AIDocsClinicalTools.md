### MOST RECENT UPDATE 7/21/2025
Please note this most recent update may make the multi-text node forget the titles and text values for your nodes. Please make a backup of your node before updating.

# ComfyUI_AIDocsClinicalTools
 The AI Doctors Custom ComfyUI Nodes

This package provides two advanced nodes for use in the Comfy Node system: the MultiInt node and the MultiText node. They are designed to handle setup multiple of ints and text in a single node, respectively, with built‐in features for dynamic configuration, custom labeling, and per–input settings.

---

## Overview

### MultiInt Node
![image](https://github.com/user-attachments/assets/1b6a6b57-1c18-417e-a149-cd156401f246)

The **MultiInt** node allows you to manage multiple integer outputs (up to 20) within a single node. Each integer has its own:
- **Label:** A custom string (e.g., "Frames", "Steps", etc.) that identifies the input.
- **Value:** The current integer value.
- **Step:** A configurable increment/decrement step value. You can adjust the step individually for each integer.
- **Control Buttons:** Plus and minus buttons allow users to increment or decrement the values. In addition, you can adjust values via dragging (by clicking and holding on the int value) or inline editing (by clicking on the pencil).
- **Settings:** Configure default parameters such as the background color, button colors, and step values.

This node is ideal when you need to setup multiple numeric parameters (such as thresholds, counts, or configuration numbers) through a single node saving space.

### Multi Float Node
![image](https://github.com/user-attachments/assets/926d5647-5df6-4962-97a4-ec6f02eff835)


The **Multi Float** node allows you to manage multiple float outputs (up to 20) within a single node. Each integer has its own:
- **Label:** A custom string (e.g., "Frames", "Steps", etc.) that identifies the input.
- **Value:** The current float value.
- **Step:** A configurable increment/decrement step value. You can adjust the step individually for each float.
- **Control Buttons:** Plus and minus buttons allow users to increment or decrement the values. In addition, you can adjust values via dragging (by clicking and holding on the float value) or inline editing (by clicking on the pencil).
- **Settings:** Configure default parameters such as the background color, button colors, and step values.

This node is ideal when you need to setup multiple numeric float parameters (such as thresholds, counts, or configuration numbers) through a single node saving space.

### MultiText Node
![image](https://github.com/user-attachments/assets/cb64eabe-69b1-4c27-aa03-6a88ccc4723d)

The **MultiText** node is similar in concept to the MultiInt node but is designed to manage multiple text inputs (up to 20). Each text field has its own customizable label and multiline support. Forked from "ComfyUI_SKBundle" where I had made a few PRs previously but decieded it was time to split to my own node set. It is particularly useful for:
- Building prompts.
- Handling multiple strings or notes within one node.
- Single output of one input or concatting multiple prompts together with a specified seperator.
- Keeping your node-based UI organized while handling dynamic text data.

### Both nodes support:
- Adding or removing individual inputs via +,- buttons.
