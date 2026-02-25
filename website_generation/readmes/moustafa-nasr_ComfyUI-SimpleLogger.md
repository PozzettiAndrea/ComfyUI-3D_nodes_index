# ComfyUI-SimpleLogger

A simple node to save your history in html file. I saves the WorkFlow with all it's input values so you can duplicate it later.

-----------


## Installation

### Installation[method1] (General installation method)

1. download the ![latest release](https://github.com/moustafa-nasr/ComfyUI-SimpleLogger/releases)
2. extract to `ComfyUI/custom_nodes` folder
3. rename folder to `ComfyUI-SimpleLogger`
4. restart ComfyUI


### Installation[method2] (Using ComfyUI-Manager only)

Using [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) goto "Manager > Custom Node Manager"

![Step 1](misc/ComfyUI-Manager-Step_1.png)

Search for `Logger` and select the one by `moustafa-nasr`

![Step 2](misc/ComfyUI-Manager-Step_2.png)


## Usage Example

Consider the following workflow of vision an image, and perform additional text processing with desired LLM. In the OllamaGenerate node set the prompt as input.

![Step 1](misc/Step_1.png)


Workflow Data will be saved in a HTML format

![Step 2](misc/Step_2.png)


All the logs will be saved by date in folder
> { your_ComfyUI_folder }/Logs

![Step 3](misc/Step_3.png)