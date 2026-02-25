# ComfyUI-SimpleTunerFlux2

ComfyUI nodes for using **SimpleTuner-trained Flux 2 LoRA models**.

SimpleTuner's Flux 2 architecture uses fused `to_qkv_mlp_proj` layers, making its LoRAs incompatible with standard ComfyUI Flux nodes. This package wraps SimpleTuner's pipeline directly.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone --recursive https://github.com/flowers6421/ComfyUI-SimpleTunerFlux2.git
cd ComfyUI-SimpleTunerFlux2
./install.sh  # Linux/macOS
# or
python install.py  # Windows
```

## Nodes

| Node | Description |
|------|-------------|
| **Load Flux 2 Pipeline** | Load base Flux 2 model |
| **Load LoRA** | Load SimpleTuner-trained LoRA |
| **Sample** | Generate images |
| **Unload LoRA** | Remove LoRA from pipeline |
| **Select LoRA** | Browse available LoRAs |

## Basic Workflow

```
[Load Flux 2 Pipeline] → [Load LoRA] → [Sample] → [Preview Image]
```

## LoRA Paths

Place your trained LoRAs in:
- `SimpleTuner/output/<project>/checkpoint-<step>/pytorch_lora_weights.safetensors`
- `ComfyUI/models/loras/`
- Or use absolute path in the loader node

## Requirements

- Python 3.10+
- PyTorch with CUDA
- ~24GB VRAM for Flux 2

## License

MIT

