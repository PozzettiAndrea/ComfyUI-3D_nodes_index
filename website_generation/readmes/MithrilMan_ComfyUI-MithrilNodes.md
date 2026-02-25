# ComfyUI Named Configs

These custom nodes for ComfyUI allow you to create "variables" or "named configurations" within your workflow. You can save the output of any node (a model, a camera configuration, a latent, etc.) with a name, and then retrieve it at any other point in the workflow using a convenient dropdown menu.

This is extremely useful for organizing complex workflows and for easily controlling them via API.

## Nodes

* `Set Named Config`: Takes an input and assigns it a name.
* `Get Named Config`: Provides a dropdown menu with all saved configurations and returns the selected one.

## Installation

1. Open the **ComfyUI Manager**.
2. Click on **Install Custom Nodes**.
3. Search for `Named Configs` and click **Install**.
4. Restart ComfyUI.

## Example Usage

(Here you can insert a screenshot of your workflow, like the one you showed me!)

![Example workflow](URL_OF_THE_SCREENSHOT_YOU_WILL_UPLOAD_ON_GITHUB)