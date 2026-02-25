# ComfyUI-LivePortrait_v2



https://github.com/user-attachments/assets/3bc8bb2a-7e2b-4c1f-9f09-55c38a7a86c7


https://github.com/user-attachments/assets/01ba6af3-9080-4af7-8795-11b8561e78f8


## 🔥 Updates
ComfyUI nodes for LivePortrait, We support animal image driven mode and regional control for Comfyui!!!
We have developed animal expression-driven nodes for ComfyUI that have the same effect as the source code.
## Introduction 
This repo, named ComfyUI-LivePortrait_v2, thanks to paper LivePortrait: Efficient Portrait Animation with Stitching and Retargeting Control.
We developed a custom_node for Liveportrait_v2 that enables flexible use on Comfyui to drive animal image-based emoji generation from videos.
## Getting Started
### Clone the code and prepare the environment 
```bash
git clone https://github.com/VangengLab/ComfyUI-LivePortrait_v2.git
cd ComfyUI-LivePortrait_v2
```
In this node, we need dependencies related to XPose. Specifically, it needs to be configured and prepared according to the instructions on https://github.com/KwaiVGI/LivePortrait. The cuda version is preferably 12.1.

or you can refer to my environment on https://github.com/VangengLab/Comfyui_Liveportrait_v3/edit/main/README.md
## Download pretrained weights

refer to https://github.com/VangengLab/Comfyui_Liveportrait_v3/edit/main/README.md
this repo will tell you all details about pretrained weights
## !!!Important reminder
Since the node we developed is relatively simple and we hope that users can get started quickly, we did not open a video upload window. We need to put the expression video (of a person) that needs to be driven into
ComfyUI-LivePortrait_v2/assets/examples/driving 
and enter its name in the node. According to the example in the figure, it can be completed.
![image](https://github.com/user-attachments/assets/0711de7e-2336-4eaf-b8d1-7a66a6fa093b)
