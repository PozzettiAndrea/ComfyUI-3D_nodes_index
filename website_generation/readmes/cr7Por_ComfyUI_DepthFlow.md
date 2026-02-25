# ComfyUI_DepthFlow
comfyui custom node for depthflow

original depthflow website: https://github.com/BrokenSource/DepthFlow

check this for installation: https://brokensrc.dev/get/

For Ubuntu system, I believe run commands below is enough: 

sudo apt-get update

sudo apt-get install libegl1-mesa libgl1-mesa-glx libgles2-mesa

apt install libasound2-dev

python -m pip install depthflow 

Run the ComfyUI workflow will download depth-anything/Depth-Anything-V2-base-hf from huggingface to your local directory automatically.
you can check it at directory: ~/.cache/huggingface/hub/models--depth-anything--Depth-Anything-V2-base-hf 

if OpenGL can find gpu, you will see log like below, and the code will run quite fast, otherwise it will run really slow.
OpenGL Renderer: NVIDIA GeForce RTX ...

Good Luck, have fun!

