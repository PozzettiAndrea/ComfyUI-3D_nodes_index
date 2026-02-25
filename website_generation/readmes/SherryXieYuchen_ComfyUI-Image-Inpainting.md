1. cd custom_nodes/  
   git clone https://github.com/ltdrdata/ComfyUI-Impact-Pack.git  
   git clone https://github.com/SherryXieYuchen/comfyui_controlnet_aux.git  

3. download sd inpainting model "sd-v1-5-inpainting.ckpt" and put it in models/checkpoints/stable-diffusion-inpainting/  
   download vae "vae-ft-mse-840000-ema-pruned.safetensors" and put it in models/vae/  
   download controlnet depth model "control_v11f1p_sd15_depth.pth" and put it in models/controlnet/  
   download lama inpainting model "big-lama.pt" and put it in models/inpaint/  
   download upscale model "RealESRGAN_x2plus.pth" and put it in models/upscale_models/  
   download depth model "ZoeD_M12_N.pt" and put it in custom_nodes/comfyui_controlnet_aux/ckpts/lllyasviel/Annotators/  
   download lcm lora model "pytorch_lora_weights.safetensors" and put it in models/loras/  
