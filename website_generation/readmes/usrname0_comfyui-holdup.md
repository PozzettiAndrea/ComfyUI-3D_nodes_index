## HoldUp
A ComfyUI node that waits for a GPU temp and/or a number of seconds.

Completely redone but based off of gpucooldown: https://github.com/wmsouza/comfyui-gpucooldown

## Usage
A universal passthrough node that accepts any input type. Insert it anywhere in your workflow where you want to pause execution - between latents, images, models, conditioning, or any other data type. The node monitors GPU temperature and/or waits for a specified time before allowing the workflow to continue.

## Pics
Example SDXL workflow (drag image into ComfyUI):
![ComfyUI Workflow](./example_workflows/ComfyUI-SDXL-HoldUp-Workflow.png)

What this looks like in the terminal:
![ComfyUI Workflow](./example_workflows/HoldUp-Terminal.png)

Project inspired by my deep and abiding mistrust of the 12VHPWR connector.
![ComfyUI Workflow](./example_workflows/temps.jpg)

## Installation

### Via ComfyUI Manager (Recommended)
Search for "HoldUp" in ComfyUI Manager and install. Dependencies will be installed automatically.

### Via Comfy Registry
```
comfy node install holdup
```

### Manual Installation
Clone to "custom_nodes" and install dependencies:

**Windows (Portable Version):**
```bash
cd ComfyUI_windows_portable\ComfyUI\custom_nodes
git clone https://github.com/usrname0/ComfyUI-HoldUp.git
cd ComfyUI-HoldUp
..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
```

**Linux/Mac or Standard Python Installation:**
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/usrname0/ComfyUI-HoldUp.git
cd ComfyUI-HoldUp
pip install -r requirements.txt
```
