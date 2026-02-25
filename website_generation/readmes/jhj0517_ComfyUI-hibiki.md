# ComfyUI hibiki

This is the [ComfyUI](https://github.com/comfyanonymous/ComfyUI) custom node for [hibiki](https://github.com/kyutai-labs/hibiki).
<br>hibiki is an end-to-end speech-to-speech ( `FR -> EN` ) translation model. 



## Installation

Search "ComfyUI hibiki" in the Manager.

Or if you want to install manually, follow the steps below:
1. git clone repository into `ComfyUI\custom_nodes\`
```
git clone https://github.com/jhj0517/ComfyUI-hibiki.git
```

2. Go to `ComfyUI\custom_nodes\ComfyUI-hibiki` and run
```
pip install -r requirements.txt
```

If you are using the portable version of ComfyUI, do this:
```
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-hibiki\requirements.txt
```

## Models

Models will be automatically downloaded to your huggingface hub cache directory.

Setting it to ComfyUI's model directory path is WIP : https://github.com/jhj0517/ComfyUI-hibiki/issues/4

## Workflows

Example workflow is in [workflows/](https://github.com/jhj0517/ComfyUI-hibiki/tree/master/workflows).
