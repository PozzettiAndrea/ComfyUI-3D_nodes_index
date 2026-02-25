# ComfyUI jhj Kokoro Onnx
This is the [ComfyUI](https://github.com/comfyanonymous/ComfyUI) custom node wrapper for the [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx)

https://github.com/user-attachments/assets/f227159b-86c6-49a7-adba-3823d41974eb


## Installation

Search "ComfyUI jhj Kokoro Onnx" in the Manager.

Or if you want to install manually, follow the steps below:
1. git clone repository into `ComfyUI\custom_nodes\`
```
git clone https://github.com/jhj0517/ComfyUI-jhj-Kokoro-Onnx.git
```

2. Go to `ComfyUI\custom_nodes\ComfyUI-Your-CustomNode-Name` and run
```
pip install -r requirements.txt
```

If you are using the portable version of ComfyUI, do this:
```
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-jhj-Kokoro-Onnx\requirements.txt
```

## Models
Models are automatically downloaded to `ComfyUI\models\kokoro-onnx` directory.

Latest version is v0.19, but look forward to v0.23 from here: https://huggingface.co/spaces/hexgrad/Kokoro-TTS

Right now it uses:
- [kokoro-v0_19.onnx](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx)
- [voices.bin](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.bin)

## Workflows

TTS workflow is in [examples/](https://github.com/jhj0517/ComfyUI-jhj-Kokoro-Onnx/tree/master/examples).
