# ComfyUI_HunyuanFoley

Update: Now work on lowvram, also new workflow
New Workflow: created by **[https://aistudynow.com/hunyuanvideo-foley-comfyui-workflow-turn-quiet-video-into-sound/](https://aistudynow.com/hunyuanvideo-foley-comfyui-workflow-turn-quiet-video-into-sound/)**

ComfyUI wrapper for **Tencent HunyuanVideo-Foley**.  


---

## Models

Get the files from the official release: **[HunyuanVideo-Foley on Hugging Face](https://huggingface.co/tencent/HunyuanVideo-Foley/tree/main)**

Place all HunyuanVideo-Foley weights and `config.yaml` in one folder named `hunyuanfoley`:

```text
ComfyUI/models/hunyuanfoley/
├─ hunyuanvideo_foley.pth
├─ vae_128d_48k.pth
├─ synchformer_state_dict.pth
└─ config.yaml

# ComfyUI_HunyuanFoley


