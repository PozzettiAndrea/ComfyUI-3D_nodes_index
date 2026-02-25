# ComfyUI-CatvtonFluxWrapper
ComfyUI wrapper of [catvton-flux](https://github.com/nftblackmagic/catvton-flux)

## workflow usage

The workflows can be found in the `examples` folder.

If you'd like more flexibility like using fp8 flux fill model, use `CatvtonLoRA-SAM2.json` or `CatvtonLoRA-Draw.json`. You can download the LoRA [here](https://huggingface.co/xiaozaa/catvton-flux-lora-alpha).

If you'd like to automatically download all models with diffusers, use `CatvtonFluxWrapper-SAM2.json` or `CatvtonFluxWrapper-draw.json`, but You may have to set up a huggingface token BEFORE you start ComfyUI.
- Go to `https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev`
- Accept FLUX policy
- Get a huggingface token for your account in settings->Access Tokens
- Set environment variable `set HF_TOKEN=PUT-YOUR-TOKEN-HERE` and `set HUGGING_FACE_HUB_TOKEN=PUT-YOUR-TOKEN-HERE`, thanks to [raymondgp](https://github.com/raymondgp).

Then you are safe to start ComfyUI; search `ComfyUI-CatvtonFluxWrapper` in the ComfyUI manager and install it; if you cannot find it, update the ComfyUI-manager node, then search again.

## workflow preview

### SAM2 segment

- CatvtonFluxWrapper-SAM2.json
<img width="960" alt="preview" src="https://github.com/user-attachments/assets/5d3cb124-1988-433e-b2fa-0a6102a7ed89">

- CatvtonLoRA-SAM2.json
<img width="960" alt="preview" src="https://github.com/user-attachments/assets/6b08f124-6b19-41a2-bc5c-fbcf1badcc4c">


### Manually segment

- CatvtonFluxWrapper-draw.json
<img width="960" alt="preview" src="https://github.com/user-attachments/assets/8c334427-81d5-4efe-ba11-2dc477b0fc18">

- CatvtonLoRA-Draw.json
<img width="960" alt="preview" src="https://github.com/user-attachments/assets/9bbfaaa5-fca3-495f-8e36-d29fea3e8314">

