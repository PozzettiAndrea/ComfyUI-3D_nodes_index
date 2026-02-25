# ComfyUI RTX 4090 Nodes

High-performance optimization nodes specifically tuned for NVIDIA RTX 4090 GPUs.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/joe002/comfyui-rtx4090-nodes.git
```

## 6 Nodes

| Node | Purpose |
|------|---------|
| `BatchImageProcessor` | Process multiple images efficiently |
| `BatchLatentProcessor` | Batch latent space operations |
| `RTX4090Optimizer` | Apply GPU-specific optimizations |
| `MemoryManager` | VRAM management and cleanup |
| `GPUMonitor` | Real-time GPU metrics |
| `TensorRTAutoConverter` | Model conversion for speed |

## RTX 4090 Optimizer

Enables hardware-specific optimizations:

- **TF32**: 2x speedup on matrix operations
- **cuDNN Benchmark**: Auto-selects optimal kernels
- **AMP**: Mixed precision for memory efficiency
- **Thread Tuning**: Optimized for high-core-count CPUs

```
Default settings for RTX 4090 + Threadripper:
├─ TF32: Enabled
├─ cuDNN Benchmark: Enabled
├─ Memory Fraction: 95%
└─ CPU Threads: 48
```

## Memory Manager

Actions:
- `clear_cache`: Standard VRAM cleanup
- `optimize`: Conditional cleanup based on threshold
- `report`: Detailed memory breakdown
- `emergency_clear`: Aggressive cleanup for OOM recovery

## GPU Monitor

Real-time metrics via nvidia-smi:
- GPU Utilization (%)
- VRAM Usage (%)
- Temperature (°C)
- Power Draw (W)

## TensorRT Converter

Convert models for faster inference:
- **fp16**: 40-60% speedup
- **int8**: 60-80% speedup (requires calibration)
- **fp32**: 20-30% speedup

## Requirements

- ComfyUI
- torch >= 2.0.0
- NVIDIA RTX 4090 (or compatible GPU)
- nvidia-smi (for GPUMonitor)

## License

MIT License

## Author

Joseph Ibrahim - VFX Lighting TD
