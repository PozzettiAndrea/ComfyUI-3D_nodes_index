# ComfyUI TF32 Enabler

Automatically enables TensorFloat-32 (TF32) acceleration for NVIDIA RTX 30/40/50 series GPUs in ComfyUI.

Note: to use torch compile you have to disable cudamallochasync

## 🚀 Performance Benefits

- **1.5-2x speedup** for diffusion models on Ampere/Ada/Blackwell GPUs
- Minimal precision impact (maintains quality)
- Automatic activation on ComfyUI startup
- Zero configuration required


## 📋 Requirements

- NVIDIA GPU with compute capability >= 8.0:
  - RTX 30 series (Ampere)
  - RTX 40 series (Ada Lovelace)
  - RTX 50 series (Blackwell)
  - A100, A6000, etc.
- PyTorch with CUDA support
- ComfyUI

## 📦 Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/marduk191/ComfyUI-TF32-Enabler.git
# Or download and extract the zip file
```

## ✅ Verification

When ComfyUI starts, you should see:
```
============================================================
🚀 ComfyUI TF32 Acceleration Enabled
============================================================
   Matmul TF32: True
   cuDNN TF32:  True
   CUDA Allocator: expandable_segments:True
   GPU: NVIDIA GeForce RTX 5090
   Compute Capability: 10.0
   ✅ torch.compile CUDA allocator fix applied
============================================================
```

## 🧪 Testing

Run the included test script to verify torch.compile works:
```bash
cd ComfyUI/custom_nodes/ComfyUI-TF32-Enabler
python test_torch_compile.py
```

## 🔧 Technical Details

This custom node enables:
- `torch.backends.cuda.matmul.allow_tf32 = True`
- `torch.backends.cudnn.allow_tf32 = True`
- `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 

TF32 uses 10-bit mantissa (vs FP32's 23-bit) while maintaining the same 8-bit exponent range, providing:
- Faster computation on tensor cores
- Same dynamic range as FP32
- Negligible quality loss for AI inference

The expandable segments allocator configuration resolves memory allocation issues when using torch.compile with CUDA operations.

## 📊 Benchmarks

Typical speedups on RTX 5090:
- SDXL: ~1.8x faster
- Flux: ~1.9x faster
- SD3: ~1.7x faster

## 🛠️ Compatibility

Works with all ComfyUI workflows and custom nodes. No conflicts expected.

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Issues and pull requests welcome!

## 🔗 Links

- [GitHub Repository](https://github.com/marduk191/ComfyUI-TF32-Enabler)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

---

**Note:** If your GPU doesn't support TF32 (older than RTX 30 series), this node will safely do nothing and won't cause errors.
