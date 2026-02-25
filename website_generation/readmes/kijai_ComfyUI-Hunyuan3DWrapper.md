
# ComfyUI wrapper for [Hunyuan3D-2](https://github.com/Tencent/Hunyuan3D-2)
---

![image](https://github.com/user-attachments/assets/a5fcd4e1-f9d1-4c21-b299-c9af85dee163)

## Models
Main model, original: https://huggingface.co/tencent/Hunyuan3D-2/blob/main/hunyuan3d-dit-v2-0/model.ckpt

Converted to .safetensors: https://huggingface.co/Kijai/Hunyuan3D-2_safetensors

to `ComfyUI/models/diffusion_models/`

Rest of the models are diffusers models, so they are wrapped and autodownloaded for now. Very new version of ComyUI is also required for the Preview3D -node.

---

# Installation
Dependencies, in your python env:

`pip install -r requirements.txt`

or with portable:

`python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-Hunyuan3DWrapper\requirements.txt`


For the texturegen part compilation is needed, I have included my compilations as a wheel for the rasterizer, and compiled .pyd for the mesh_processor (already in place), these are compiled for:

**Windows 11 python 3.12 cu126 (works with torch build on 124)**

You would do `pip install wheels\custom_rasterizer-0.1-cp312-cp312-win_amd64.whl`

or with portable (in `ComfyUI_windows_portable` -folder):
`python_embeded\python.exe -m pip install ComfyUI\custom_nodes\ComfyUI-Hunyuan3DWrapper\wheels\custom_rasterizer-0.1-cp312-cp312-win_amd64.whl`

**Windows 11 python 3.12 torch 2.6.0 + cu126**
Current latest portable was updated to use pytorch 2.6.0, for this you should use new wheel:
`python_embeded\python.exe -m pip install ComfyUI\custom_nodes\ComfyUI-Hunyuan3DWrapper\wheels\custom_rasterizer-0.1.0+torch260.cuda126-cp312-cp312-win_amd64.whl`

This was tested to work on latest ComfyUI portable install

---

## If this doesn't work or there isn't a suitable wheel available for your system. you need to compile yourself:

Rasterizer, to build and install:

```
cd hy3dgen/texgen/custom_rasterizer
python setup.py install
```

**If you are using the portable ComfyUI installation:**
For example (check the paths on your system):
```
cd C:\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-Hunyuan3DWrapper\hy3dgen\texgen\custom_rasterizer
C:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install .
```

If you get an error about Python.h missing, refer to the instructions here as it's the same compilation issue (you don't need Triton itself):

https://github.com/woct0rdho/triton-windows?tab=readme-ov-file#8-special-notes-for-comfyui-with-embeded-python


Or build with `python setup.py bdist_wheel` which creates the .whl file to the dist -subfolder, which you then would pip install to your python environment. 
End result needs to be `custom_rasterizer_kernel*.pyd` file and `custom_rasterizer` folder in your python environments `site-packages` folder.

---

For the mesh_processor extension the build command would be this:
```
cd hy3dgen/texgen/differentiable_renderer
python_embeded\python.exe setup.py build_ext --inplace
```
This file is supposed to be in that very folder. It is only used for the vertex inpainting, if this file doesn't exist the fallback is run on cpu and is much slower. The vertex inpainting is on it's own node and in the worst case can just be bypassed, downside would be worse filling of the textures.

Again, with portable you should use the embedded python to run the commands.

---

# Update:

## Added [BPT](https://github.com/whaohan/bpt)

**This has some hefty requirements, fully optional, install at your own discretion**
```
cd ComfyUI-Hunyuan3DWrapper\hy3dgen\shapegen\bpt
pip install -r requirements.txt
```

## Installation with portable ComfyUI:
from the portable's root directory:
`python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-Hunyuan3DWrapper\hy3dgen\shapegen\bpt\requirements.txt`

Download weights <https://huggingface.co/whaohan/bpt/blob/refs%2Fpr%2F1/bpt-8-16-500m.pt>

Copy `bpt-8-16-500m.pt` to `ComfyUI-Hunyuan3DWrapper-main\hy3dgen\shapegen\bpt`

# Xatlas upgrade procedure to fix UV wrapping high poly meshes

`python_embeded\python.exe -m pip uninstall xatlas`

in the portable root folder (`ComfyUI_windows_portable`):

`git clone --recursive https://github.com/mworchel/xatlas-python.git`

`cd .\xatlas-python\extern`

delete `xatlas` folder 

`git clone --recursive https://github.com/jpcy/xatlas`

in `xatlas-python\extern\xatlas\source\xatlas` modify `xatlas.cpp`

change line 6774: `#if 0` to `//#if 0`

change line 6778: `#endif` to `//#endif`

Finally go back to portable root (`ComfyUI_windows_portable`) folder:

`.\python_embeded\python.exe -m pip install .\xatlas-python\`

---
