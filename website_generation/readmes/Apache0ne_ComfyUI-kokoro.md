# ComfyUI-Kokoro TTS

This is the [ComfyUI](https://github.com/comfyanonymous/ComfyUI) custom node wrapper for the [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx)

## Dependencies
'onnxruntime-gpu' py lib\
'kokoro-onnx' py lib
# depen issues 
kokoro-onnx will change your numpy install version 
## Installation
ComfyUI-Manager (rec)\
Can be downloaded from ComfyUI-manager\
IF using Windows Port version\
ComfyUI Folder\
```pip install onnxruntime-gpu kokoro-onnx```\
Inside Custom_nodes Folder\
```git clone https://github.com/Apache0ne/ComfyUI-kokoro.git ```\
IF using Matrix \
Inside venv\Scripts\
```activate```\
```pip install onnxruntime-gpu kokoro-onnx```\
Inside Custom_nodes Folder\
```git clone https://github.com/Apache0ne/ComfyUI-kokoro.git ```
## Models
Models are automatically downloaded to `ComfyUI\models\kokoro-onnx` directory.

Updated to Latest TTS version is v1.0

Right now it uses:
- [kokoro-v1.0.onnx](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx)
- [voices.bin](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin)

Should auto download first run in workflow: IF not\
models on huggingface: [kokoro-models](https://huggingface.co/ApacheOne/kokoro-onnx/tree/main)

##credits
Base node built by:
https://github.com/jhj0517 