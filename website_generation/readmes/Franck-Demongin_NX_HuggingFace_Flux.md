# NX_HuggingFace_Flux

![UI](https://github.com/user-attachments/assets/bfb84f1b-7aa4-4c04-92cd-8abfe1f1725a)

<img src="https://img.shields.io/badge/Python-3.10-blue" /> <img src="https://img.shields.io/badge/ComfyUI-orange" /> [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

A ComfyUI's custom node for generating images with the Flux-Dev or Flux-Schnell models directly on Hugging Face 

> [!IMPORTANT]
> Node tested only on Linux. It should work without any problems on Windows and Mac but has not been tested on these OS.

## Installation

If GIT is installed on your system, go to the `custom_nodes` subfolder of your ComfyUI installation, open a terminal and type: 
```:bash
git clone https://github.com/Franck-Demongin/NX_HuggingFace_Flux.git
```

If GIT is not installed, retrieve the [ZIP](https://github.com/Franck-Demongin/NX_HuggingFace_Flux/archive/refs/heads/main.zip) file, unzip it into the `custom nodes` folder and rename it NX_HuggingFace_Flux.

> **IMPORTANT** 
> Activate the Python virtual environment used by ComfyUI
from the ComfyUI installation directory:
> ```bash
> # Linux, Mac
> source venv/bin/activate
>```
>```bash
> # Windows
> venv\Scripts\activate
>```
>The command line must be preceded by *(venv)*, indicating that the virtual environment is active.

Install the dependencies used by the node:
```bash
pip install -r requirements.txt
```

Copy the *.env.example* file and rename it *.env*  

Open it and enter your Hugging Face Access Token (you can create it in your Hugging Face space after creating an account).

Restart ComfyUI. ***Hugging Face Flux*** should be available in the ***NX_Nodes*** category.

## Features

- choice of template: Flux-Dev or Flux-Schnell
- settings for seed, image size, CFG and number of steps


Note that 
- the CFG is only used by the Flu-Dev model and seems to be ignored by the Schnell model
- for Dev, use a high number of steps (25 to 50) and a CFG between 2.5 and 8
- for Schnell, the number of steps can be set to 4

Limitations

- availability of a GPU on Hugging Face to render the image
-GPU time quota allocated to each user

Due to these limitations, an error often occurs, stopping rendering.



