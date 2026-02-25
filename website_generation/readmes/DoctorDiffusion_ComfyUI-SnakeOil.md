# 🐍🛢️ComfyUI-SnakeOil
Use [Doctor Diffusion's snake oil nLoRAs](https://civitai.com/models/987843) as well as [other negative LoRAs](https://civitai.com/models/186617/doctor-diffusions-negative-xl-lora) easily within ComfyUI.

### Installation
Use the world famous [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) or manually install:

Navagate to your custom node folder `...ComfyUI/custom_nodes`
```
git clone https://github.com/DoctorDiffusion/ComfyUI-SnakeOil.git
```
As long as you have torch you are set.
### Get models
Navagate to your models folder `...ComfyUI/models` and create a new folder called `nloras`
Download the nLoRA for SDXL, SD3.5M, or SD3.5L and save to the `nloras` folder

### Snake Oil Node
Loads negative LoRAs or nLoras into image diffusion models with a simple slider interface that removes the confusion of how to use negative LoRAs.

![Screenshot 2024-11-27 192805](https://github.com/user-attachments/assets/8ca2309e-0b2f-4bce-925f-d7b80c5b986a)

A little snake oil can go a long way.

![snakeoil_00005](https://github.com/user-attachments/assets/3f0ab186-4477-4589-8cf1-8c86b8af29d0)

⭐ If you like the project, please give it a star! ⭐

## License
CC0-1.0 license
