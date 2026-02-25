# ComfyUI-BS_Kokoro-onnx

A ComfyUI wrapper for [Kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx)

## Based on
- [onnx-community/Kokoro-82M-ONNX](https://huggingface.co/onnx-community/Kokoro-82M-ONNX)
- [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)

## Installation

Until the repository is registered on ComfyUI-Manager, please install manually using the following steps:

```bash
cd custom_nodes
git clone https://github.com/Burgstall-labs/ComfyUI-BS_Kokoro-onnx
cd ComfyUI-BS_Kokoro-onnx
pip install -r requirements.txt
```

### Required Model Files

Download the following files:
- [kokoro-v0_19.onnx](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx)
- [voices.json](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json)

Place both files in the `/custom_nodes/ComfyUI-BS-Kokoro-onnx/` folder.

## Usage

Example workflows are available in the `Example` folder.

## License

This project inherits licenses from its dependencies:
- kokoro-onnx: MIT
- kokoro model: Apache 2.0

---
*Note: This is my first repository. Feedback and contributions are welcome!*
