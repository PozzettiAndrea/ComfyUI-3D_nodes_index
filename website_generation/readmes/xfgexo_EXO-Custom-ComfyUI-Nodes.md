# EXO-Custom-ComfyUI-Nodes

This repository contains all the custom nodes I originally made for myself for ComfyUI. However, I have decided to make them available to everyone.

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO Prompt Builder Deluxe Node

Designed for dynamic prompt creation and template management within ComfyUI. This advanced node goes beyond what standard text prompts and styler nodes can do by offering a modular system that allows users to construct complex text prompts. It utilizes over 90 JSON file templates, each containing 50 to 80 entries and each entry having its own unique keywords, which in turn provides a wide selection of options for a truly dynamic and creative process. The node supports both template and manual and combined inputs.

### Features

* Dynamic Prompt Building: Combines prompt templates from multiple categories.
* Extensive Template Library: Utilizes 90 JSON file templates.
* Manual Input Support: Allows for manual input of text prompts.
* Template Management: Utilizes a modular system for managing and organizing prompt templates.
* Configuration File: Easily edit a config file to modify sort order and rename labels and entries.
* Section Toggles: Ability to Enable/Disable category sections.
* Category Selections: Easily selectable drop-down lists of categories.
* Console Logging: Offers an option to log combined prompts to the console.

### Inputs

* Positive_Prompt_Text: Manually entered positive prompt text.
* Negative_Prompt_Text: Manually entered negative prompt text.
* Log_Prompt_to_Console: Input toggle to enable or disable console logging of the combined prompts.
* Section Toggles: Boolean inputs for enabling or disabling specific sections of templates.
* Category Selections: Dropdowns for selecting specific templates from each category.

### Outputs

* Positive_Prompt_Text: The combined positive prompt text.
* Negative_Prompt_Text: The combined negative prompt text.

<div align="center">
<img height="2816" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_pbd_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO Translate Text Node

A powerful node for translating text between multiple languages within ComfyUI workflows.

### Modes

* Ignore: Pass-through functionality without translation.
* Translation: Utilizes MarianMT models from the Helsinki-NLP project for translation.

### Features

* Multilingual Translation from English to Chinese, French, German, Japanese, Spanish.
* Multilingual Translation from Chinese, French, German, Japanese, Spanish to English.
* Model Caching: Auto Downloads and caches models on first use.
* Language Detection: Detects the source language to avoid unnecessary translations.
* UTF-8 Encoding: Ensures proper text encoding, supporting diverse characters and languages.

### Inputs

* Positive_Text: The positive prompt text to be translated.
* Negative_Text: The negative prompt text to be translated.
* Translation_Model: Selects the translation language direction.

### Outputs

* Trans_Positive_Text: The translated positive text.
* Trans_Negative_Text: The translated negative text.

<div align="center">
<img height="210" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_translatetext_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO Clip Text Encode Node

Features:

* Dual Prompt Handling: This node processes both positive and negative text prompts.
* Encoding: Utilizes CLIP models to convert text inputs into conditioning tensors.
* UTF-8 Compatibility: Ensures that text inputs are properly encoded in UTF-8.

### Inputs

* Clip_Input: Connect this to the output of a loaded CLIP model.
* Positive_Text: A multiline string input for positive prompts.
* Negative_Text: A multiline string input for negative prompts.

### Outputs

* Clip_Cond_Positive: The positive conditioning tensor.
* Clip_Cond_Negative: The negative conditioning tensor.
* Positive_Text: The original positive text prompt, available for downstream use.
* Negative_Text: The original negative text prompt, available for downstream use.

<div align="center">
<img height="210" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_textencode_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO Display Text Node

The ComfyUI EXO Display Text node is a custom node designed to display and pass through text content within the ComfyUI nodes UI. It provides a visual representation of both positive and negative prompts while allowing the text to continue through the workflow downstream.

### Features

* Text Display: Displays both positive and negative text prompts in the UI.
* Pass-Through Capability: Maintains the ability to connect to downstream nodes.
* UTF-8 Compatibility: Ensures that text inputs are properly encoded in UTF-8.

### Inputs

* Positive_Text: A multiline string input for positive prompts.
* Negative_Text: A multiline string input for negative prompts.

### Outputs

* Positive_Text: The original positive text prompt, passed through for further processing.
* Negative_Text: The original negative text prompt, passed through for further processing.

<div align="center">
<img height="484" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_displaytext_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO Save Text Node

The ComfyUI EXO Save Text Node is a robust component designed for efficiently saving prompt text to files within ComfyUI workflows. This node supports both positive and negative prompts and offers versatile file operations, including append and overwrite functionalities.

### Features

* File Operations: Choose from Append, Overwrite, Ignore, or Erase.
* Timestamped Entries: Automatically includes the current date and time with each saved entry.
* UTF-8 Encoding: Guarantees proper text encoding, supporting diverse characters and languages.

### Inputs

* Positive_Text: The positive prompt text to be saved.
* Negative_Text: The negative prompt text to be saved.
* File_Action: The file operation to perform (Append, Overwrite, Ignore, Erase).
* File_Name: The name of the file to save the prompts in, including the .txt extension.
* Output_Folder: The folder where the prompt file will be saved.

### Outputs

* This node is an output node, performing file write and save operations.

<div align="center">
<img height="243" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_savetext_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO Numeric Value Node

The ComfyUI EXO Numeric Value node is a simple yet essential node for numeric entry within the ComfyUI workflow. It allows users to input a numeric value, outputting it as a float for use in subsequent nodes.

### Features

* Numeric Input: Provides a straightforward interface for entering numeric values, supporting float precision.
* Seamless Integration: Designed to connect easily with nodes that require numeric inputs.

### Inputs

* Numeric_Value: A float input field for entering the desired numeric value.

### Outputs

* Numeric_Value: The entered numeric value, output as a float for use in other nodes.

<div align="center">
<img height="135" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_numeric_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO Latent Image Size Node

The ComfyUI EXO Latent Image Size node is a customizable node within ComfyUI. Designed to generate latent images based on user-selected dimensions. It facilitates the creation of latent image noise for further processing in workflows.

### Features

* Dimension Selection: Select from predefined dimensions.
* Batch Processing: Supports generating multiple images in a single batch.
* Configurable Defaults: Easily edit an external JSON configuration file, allowing for easy customization.
* Format: The format is "width x height (aspect ratio).

### Inputs

* Dimensions: A dropdown selection for choosing the desired dimensions of the latent image.
* Batch_Size: An integer input specifying the number of images to generate in a single batch.

### Outputs

* Latent: The generated latent image noise at the specified dimensions.

## ComfyUI EXO Latent Image Size X Node

The ComfyUI EXO Latent Image Size X node is an enhanced version of the latent image size node within the ComfyUI framework. It allows for the generation of latent images with additional outputs for width and height, providing greater flexibility in workflow integration.

### Features

* Dimension Selection: Select from predefined dimensions.
* Batch Processing: Supports generating multiple images in a single batch.
* Configurable Defaults: Easily edit an external JSON configuration file, allowing for easy customization.
* Format: The format is "width x height (aspect ratio).
* Additional Outputs: Provides separate outputs for the width and height of the selected dimensions.

### Inputs

* Dimensions: A dropdown selection for choosing the desired dimensions of the latent image.
* Batch_Size: An integer input specifying the number of images to generate in a single batch.

### Outputs

* Latent: The generated latent image noise at the specified dimensions.
* Width: The width of the selected dimensions in pixels.
* Height: The height of the selected dimensions in pixels.

<div align="center">
<img height="759" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_latent_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO Image Rescale Node

A versatile image rescaling node for ComfyUI that provides multiple scaling modes:

### Modes

* Ignore: Passes the image through without any modifications
* Resize: Resizes the image to specific width and height dimensions
* Upscale: Enlarges the image by a specified scale factor
* Downscale: Reduces the image by a specified scale factor

### Features

* Multiple resampling methods (lanczos, nearest, bilinear, bicubic)
* Supersampling anti-aliasing option for higher quality results
* Maintains proper tensor format for ComfyUI compatibility
* Configurable scale factors via external JSON configuration

### Input Parameters

* Image: Input image tensor
* Mode: Scaling mode selection
* Scale_Factor: Multiplier for upscale/downscale operations
* Resize_Width: Target width for resize mode
* Resize_Height: Target height for resize mode
* Resampling: Algorithm used for resizing
* Supersample: Anti-aliasing method selection
* Force_Resize: Option to force exact dimensions

### Output

* Processed image tensor in the correct format for ComfyUI (B,C,H,W)

<div align="center">
<img height="307" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_rescale_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO FluxSampler Node

The ComfyUI EXO FluxSampler node is an advanced sampling node designed for ComfyUI. It provides flexible and customizable sampling capabilities, allowing for precise control over model sampling.

### Features

* Customizable Sampling: Including noise seed, increment value, sampler name, scheduler, and more.
* Model Sampling: Utilizes a custom ModelSamplingFlux logic.
* Noise Generation: Includes a built-in noise generator.
* Guidance Integration: Supports conditioning guidance.

### Inputs

* Model: The model to be used for sampling.
* Conditioning: The conditioning tensor for guiding the sampling process.
* Width and Height: Dimensions for the output image.
* Noise_Seed: Seed for noise generation, ensuring reproducibility.
* Increment_Value: Increment value for sampling adjustments.
* Sampler_Name: Chooses the sampler algorithm.
* Scheduler: Selects the scheduling method for sigma generation.
* Steps: Number of steps for the sampling process.
* Denoise: Denoising factor for adjusting the sampling intensity.
* Max_Shift and Base_Shift: Parameters for controlling the sampling shift.
* Guidance: Guidance factor for conditioning adjustments.
* Negative_Conditioning (optional): Additional conditioning for negative guidance.

### Outputs

* Model_Out: The processed model with applied sampling.
* Noise: The generated noise object.
* Sampler: The sampler object used for processing.
* Sigmas: The computed sigmas for the sampling process.
* Seed: The seed dictionary for noise generation.
* Latent: The generated latent image tensor.
* Guider: The guidance object for conditioning.
* Conditioning_Out: The adjusted conditioning tensor with applied guidance.

## ComfyUI EXO FluxSampler Mini Node

The ComfyUI EXO FluxSampler Mini node is an sampling node designed for ComfyUI. It provides flexible sampling capabilities, allowing for control over model sampling.

### Features

* Model Sampling: Utilizes a custom ModelSamplingFlux logic.

### Inputs

* Model: The model to be used for sampling.
* Width and Height: Dimensions for the output image.
* Max_Shift: Parameters for controlling the sampling shift.
* Base_Shift: Parameters for controlling the sampling shift.

### Outputs

* Model_Out: The processed model with applied sampling.

<div align="center">
<img height="848" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_flux_samp_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

## ComfyUI EXO Notes Node

A simple text entry node that allows adding multiline notes directly within the nodes UI.

### Features

* Multiline Support: Provides a multiline text area for detailed note-taking.

### Input Parameters

* A multiline text input for entering notes, with a default message "Enter your notes here..."

### Output

* Displays the entered notes within the workflow for easy reference.

<div align="center">
<img height="848" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_notes_ss.png" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

### Example Workflows

I have included three workflow examples with my node package. The workflows support SDXL and FLUX.

The workflows:
You will find the workflows in the "workflows" folder of this package.
1. [EXO Text - Image SDXL Workflow.json](https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/workflows/EXO%20Text%20-%20Image%20SDXL%20Workflow.json)
2. [EXO Image - Image SDXL Workflow.json](https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/workflows/EXO%20Image%20-%20Image%20SDXL%20Workflow.json)
3. [EXO Text - Image FLUX Workflow.json](https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/workflows/EXO%20Text%20-%20Image%20FLUX%20Workflow.json)

Note: The workflows use nodes from the following node developers:
- ComfyUI core nodes
- EXO-Custom-ComfyUI-Nodes
- ComfyUI-Detail-Daemon: [GitHub Repository](https://github.com/Jonseed/ComfyUI-Detail-Daemon)
- ComfyUI-Impact-Pack: [GitHub Repository](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- rgthree-comfy: [GitHub Repository](https://github.com/rgthree/rgthree-comfy)

<div align="center">
<img height="780" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_tti_wf.jpg" />
</div>

<div align="center">
<img height="40" src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png" />
</div>

### Installation

To use the ComfyUI EXO custom nodes in your workflow, you now have two options:

#### A. ComfyUI Manager
You can now easily install the nodes directly from the ComfyUI Manager. Simply search for EXO Nodes in the search bar and then click Install.

#### B. Manual Installation
Follow these steps to manually install the EXO Node pack:

1. Navigate to the `custom_node` directory of your ComfyUI installation using Windows Explorer.
2. Then "Shift + Right click" inside the folder and choose either `open in terminal`, `open in PowerShell`, or `get bash here`.
3. Then type in the following command to clone the repository:

```bash
git clone https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes.git
```

### Contributions

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to [open an issue](https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/issues).

### License

This custom ComfyUi node pack is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License v3.0 as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

The GPL license ensures that any derivative work based on GPL-licensed code
must also be distributed under the same GPL license terms. This means that if
you modify GPL-licensed software and distribute your modified version, you must
also provide the source code and allow others to modify and distribute it under
the same GPL license.

A copy of the GNU General Public License is included within these project files.

---

**Date**: Dec.17.2024  
**Author**: Joe Porter / AKA: xfgexo  
**Repository**: [EXO-Custom-ComfyUI-Nodes](https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes)
