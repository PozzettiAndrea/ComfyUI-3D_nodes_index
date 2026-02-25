# NX_Translator

![hero](https://github.com/user-attachments/assets/95bdcfd6-a581-4f41-9652-25db0d3fe1ac)

<img src="https://img.shields.io/badge/Python-3.10-blue" /> <img src="https://img.shields.io/badge/ComfyUI-orange" /> [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

A custom node for translating prompts with Google Translate or DeeplL directly in ComfyUI.

## Installation

If GIT is installed on your system, go to the `custom_nodes` subfolder of your ComfyUI installation, open a terminal and type: 
```:bash
git clone https://github.com/Franck-Demongin/NX_Translator.git
```

If GIT is not installed, retrieve the [ZIP](https://github.com/Franck-Demongin/NX_Translator/archive/refs/heads/main.zip) file, unzip it into the `custom nodes` folder and rename it NX_translator.

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
Restart ComfyUI. ***Translator*** should be available in the ***NX_Nodes*** category.

## Features

![UI](https://github.com/user-attachments/assets/c40d7e22-f94e-428f-8967-1f9069b4a2cc)

- translates from any language into English
- uses Google or DeepL services
- allows you to replace or add one translation to another by choosing the separator
- indicates usage quota for DeepL
- import API key DeepL from node


