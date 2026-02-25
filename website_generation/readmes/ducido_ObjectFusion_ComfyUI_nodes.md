# 🎨 Object Fusion Pipeline

## 🌟 Motivation
Have you ever fantasized about crafting a single masterpiece from elements of different photos? 😲 What if I told you that manually prompting each object's shape, color, and features for diffusion could be a thing of the past? And let’s be real, using GPT to describe each object step by step can feel like chasing an AI in slow motion. 🐢💤

Here, I introduce a complete pipeline that takes two images as input, allowing you to choose which objects from the images you want to fuse seamlessly.

## 🚀 Features
- Combine objects from two different images into a single scene.
- Easy selection and customization of objects to be fused.
- Optimized integration with ComfyUI.
  
## 🖼️ Some Examples

![Example 2](https://github.com/user-attachments/assets/73877129-01b4-4197-a62c-d891ad02b760)

<details>
  <summary>Click to expand/collapse</summary>
  
![Example 1](https://github.com/user-attachments/assets/68d2c121-45a4-4c47-a02e-17d2e96ec84c)
![Example 3](https://github.com/user-attachments/assets/285f74ae-0320-4a8b-831d-1ef8d4d201fb)
![Example 4](https://github.com/user-attachments/assets/ad6d4e41-343d-4b4b-bb15-175bf71e9c13)

</details>

## 🛠️ Installation

1. Clone this repo into the `custom_nodes` directory in [ComfyUI](https://github.com/comfyanonymous/ComfyUI):
    ```bash
    git clone https://github.com/ducido/ObjectFusion_ComfyUI_nodes
    ```
    
3. Clone these amazing repositories and follow their instructions:
    - [ComfyUI-SD3-nodes](https://github.com/liusida/ComfyUI-SD3-nodes)  
      _Note: Place the 3 clips model into `models/clip`._
    - [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
    - [img2txt-comfyui-nodes](https://github.com/christian-byrne/img2txt-comfyui-nodes)
      
4. Install the required packages:
    ```bash
    conda create -n objectfusion python=3.10 -y
    conda activate objectfusion
    pip install -r custom_nodes/ObjectFusion_ComfyUI_nodes/requirements.txt
    wget https://huggingface.co/camenduru/YoloWorld-EfficientSAM/resolve/main/efficient_sam_s_gpu.jit -P custom_nodes/ObjectFusion_ComfyUI_nodes/Custom_ComfyUI_YoloWorld_EfficientSAM
    ```
5. Or you can install with [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) which is much easier and faster.

## 📌 Note
_All the folders, except `CROP_OBJECT`, are from other repositories. Thank you for your amazing works, I appreciate that. Besides, I have made some minor modifications to fit this project. Here are the details:_

- **[Custom_ComfyUI-YoloWorld-EfficientSAM](https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM)**
  - Added 2 output fields: `BBOX`, `categories`.
  - Displayed ID also in the IMAGE output (e.g., `{ID} - {class} - {confidence}`).

- **[comfyui-llm-assistant](https://github.com/longgui0318/comfyui-llm-assistant)**
  - Removed input field: `prompt`.
  - Added 4 input fields: `object1`, `desc_obj1`, `object2`, `desc_obj2`.
  - Change all `default` value to `""` because the newest frontend of ComfyUI consider `None` value as a bug
  

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## 📄 License
This project is licensed under the MIT License.
