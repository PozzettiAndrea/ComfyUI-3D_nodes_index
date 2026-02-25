# ComfyUI-ZImageDit


<img width="559"  alt="ComfyUI-zimage-diffusers-wrapper_00002_" src="https://github.com/user-attachments/assets/eac45a4d-ad75-4a0f-9de7-b6bcf51f2292" />
<img width="559"  alt="image" src="https://github.com/user-attachments/assets/bac94951-c82c-46f4-ab14-089875693072" />


## What is this ?
- an Alpha repo: unofficial **diffusers** integration of the official **SDNQ pipeline** to run in ComfyUI
- ...because I wanted to compare quality and be even more vram savy via SDNQ which is not officially supported and experiments with parameters

## What can I do with this ?

Check these example LLM "Clones" , credits to the original authors (Civitai) for variety of generes, styles, media.

<img width="559" height="558" alt="image" src="https://github.com/user-attachments/assets/a523c061-0dab-4cf5-85a4-a527e30fe1e7" />
<img width="562" height="558" alt="image" src="https://github.com/user-attachments/assets/b79131d2-7794-40d1-b7b4-2f59293fb21f" />


## Notes:
- **installation**
    you might have to install some pip packages manually, nothing too difficult
    you need: accelerate, the latest diffusers from source to support z-image pipeline
 
- **install_sdnq.bat** might help on windows because it looks like their toml file has an issue with double licensing (open inside the bat and change paths)
- ** diffusers** to install the latest diffusers manually via git to support the pipeline **(from the embedded python folder if using portable comfyui)**:
  `python.exe -m pip install git+https://github.com/huggingface/diffusers.git`
- for **flash attention (optional) ** find a .whl, if you need you can try these places:
  - seems to be **the best place to find them**:
  -   https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/tag/v0.5.4
  - other places
    - prebuilt wheels https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/tag/v0.4.10 (i ended up using one package from here, it gives a nice speed boost, sage attention makes it slower, not sure why)
    - prebuilt wheels  https://huggingface.co/Kijai/PrecompiledWheels/tree/main
    - prebuilt wheels https://huggingface.co/lldacing/flash-attention-windows-wheel/tree/main
- about **compile**: does not work, for me. 

- **if startup fails** check requirements for what is needed (quanto is not needed for these nodes, but for the other broken ones)
- **weights** are downloaded by diffusers on first run for sdnq nodes, in you huggingface default cache folder unless you change it
- **some option dont work** or I did not finish porting, test.
- there are **other** files in the other folders but they are experimental, ignore them (you might need quanto even or other installs)
- internally sampling happens with flowmatching euler
- only tested on windows (but linux should be even easier)
  - Platform: Windows
  - Python version: 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]
  - pytorch version: 2.8.0+cu128
  - xformers version: 0.0.32.post2
  - Set vram state to: NORMAL_VRAM
  - Device: cuda:0 NVIDIA GeForce RTX 3080 : cudaMallocAsync
  - ComfyUI version: 0.3.75
  - ComfyUI frontend version: 1.33.8
  - Total VRAM 10240 MB, total RAM 32560 MB


- if you are on linux... you are smart enought to know what to do

**Enjoy!**
Enrico aka ErosDiffusion

ps.: you might have issues installing, but I have no time to support :D

**additional notes**:
- this does not use ComfyUI memory management, so use carefully.
- I have added an option to unload but did not test it not sure it works.
- the memory footprint is around 7gb vram more or less, you can safely run up to 2048x2048 i can run lmstudio with qwen4 3b in parallel and between ram and vram and this, and never get oom.
  

´´
