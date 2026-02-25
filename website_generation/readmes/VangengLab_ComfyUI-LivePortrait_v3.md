# ComfyUI-LivePortrait_v3
![image](https://github.com/user-attachments/assets/5a7f07e8-c856-4a6e-ad81-82ebe1d5934d)

## 🔥 Updates
ComfyUI nodes for LivePortrait,We support image driven mode and regional control for Comfyui!!!
Using a simple way to use an image as a driving signal to drive the source image or video!
## Introduction 
This repo, named Comfyui_Liveportrait_v3, thanks to paper LivePortrait: Efficient Portrait Animation with Stitching and Retargeting Control.
We developed a custom_node for Liveportrait_v3 that enables flexible use on Comfyui to drive image-based emoji generation from photos.
## Getting Started
### 1. Clone the code and prepare the environment 
```bash
git clone https://github.com/VangengLab/ComfyUI-LivePortrait_v3.git
cd ComfyUI-LivePortrait_v3
```
For the environment, it can be configured according to Comfyui_liveportrait_v1 and liveportrait. For details, you can refer to https://github.com/KwaiVGI/LivePortrait and https://github.com/kijai/ComfyUI-LivePortraitKJ:https://github.com/KwaiVGI/LivePortrait.
or refer to my environment and execute the instruction.
```bash
pip install -r requirements.txt
```
## Download pretrained weights
The easiest way to download the pretrained weights is from HuggingFace:
```bash
cd models/
huggingface-cli download KwaiVGI/LivePortrait --local-dir Liveportrait_v3 --exclude "*.git*" "README.md" "docs"
```
If you cannot access to Huggingface, you can use hf-mirror to download:
```bash
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download KwaiVGI/LivePortrait --local-dir pretrained_weights --exclude "*.git*" "README.md" "docs"
```
You can also manually download the model to the folder from the URL: https://huggingface.co/KwaiVGI/LivePortrait/tree/main, and remember put them to models/Liveportrait_v3

​​![cbedb95a-7d1a-4686-8d26-4b72d9f75552](https://github.com/user-attachments/assets/ef1d9943-5a47-4191-a683-3804439c6197)


###maybe there will be some problem about locating models,please use the abusolte address,or tell me I will offer you help.my cuda is 12.1 which has less problem.


