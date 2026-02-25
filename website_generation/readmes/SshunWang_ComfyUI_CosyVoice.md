# ConfyUI for CosyVoice
Support both CosyVoice1.0 and CosyVoice2.0. 

Referenced [CosyVoice-ComfyUI](https://github.com/AIFSH/CosyVoice-ComfyUI), the following modifications have been made:
* Add support for CosyVoice2.0
* Add whether to use stream processing options
* Use speed control by CosyVoice
* Add model path check to avoid duplicate downloads
* Provide two ways of use


## 👉🏻 CosyVoice 👈🏻
**CosyVoice 2.0**: [Demos](https://funaudiollm.github.io/cosyvoice2/); [Paper](https://arxiv.org/abs/2412.10117); [Modelscope](https://www.modelscope.cn/studios/iic/CosyVoice2-0.5B); [HuggingFace](https://huggingface.co/spaces/FunAudioLLM/CosyVoice2-0.5B)

**CosyVoice 1.0**: [Demos](https://fun-audio-llm.github.io); [Paper](https://funaudiollm.github.io/pdf/CosyVoice_v1.pdf); [Modelscope](https://www.modelscope.cn/studios/iic/CosyVoice-300M)

## **How to use**
### Open with ComfyUI-Manager
1. clone the repo
```sh
git clone https://github.com/SshunWang/ComfyUI_CosyVoice.git
cd ComfyUI_CosyVoice
pip install -r requirements.txt
```
2. load the custom node with comfyui-manager, see [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager).

### Auto load by ComfyUI
Copy to "your comfyui path"/custom_nodes or create a solft link to the path of this repo with ln -s command or clone to "your comfyui path"/custom_nodes directly

## Example
![image](https://github.com/user-attachments/assets/87815b95-6870-4abd-a44a-0e333cdb3110)


## Note
The corresponding model will be downloaded during the first use
