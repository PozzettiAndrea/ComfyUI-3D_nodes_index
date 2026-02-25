# CONDUIT - ComfyUI Inference Optimizer

**"Optimize the flow of your inference"**

A production-ready optimization system for ComfyUI that implements non-linear, non-binary optimization strategies for faster generation with lower VRAM usage.

## Nodes

| Node | Purpose | Key Feature |
|------|---------|-------------|
| **ConduitCore** | Workflow Optimizer | DAG analysis, async scheduling |
| **ConduitPool** | VRAM Manager | 4-tier memory temperature gradient |
| **ConduitGate** | Precision Router | Dynamic FP32/FP16/FP8 routing |
| **ConduitPath** | Speculative Generator | Multi-branch generation with pruning |
| **ConduitSeal** | Deterministic Cache | Checksum-verified result caching |
| **ConduitSense** | Type Detector | Auto-detect workflow type |
| **ConduitApply** | Apply Optimizations | Combine configs and execute |

## Quick Start

1. Add **ConduitCore** to set optimization mode (balanced/speed/quality/memory)
2. Add **ConduitGate** to configure precision routing
3. Connect to **ConduitApply** before your model
4. Run workflow

## Optimization Modes

### Speed Mode
- Aggressive FP8 precision on RTX 40 series
- Async model preloading
- Estimated 2-3x speedup

### Quality Mode
- Full FP32 precision for attention
- No early exit from sampling
- Best visual quality

### Memory Mode
- Aggressive VRAM offloading
- Streaming decode
- Tile processing for large images

### Balanced Mode (Default)
- Adaptive precision based on operation type
- Smart preloading without VRAM pressure
- Good balance of speed and quality

## VRAM Temperature System (ConduitPool)

```
HOT  (GPU VRAM)  - Active inference
WARM (Pinned)   - Next 2-3 models, instant transfer
COLD (RAM)      - Recently used, ~500ms load
ARCHIVE (Disk)  - Rarely used, predictive prefetch
```

## Speculative Generation (ConduitPath)

Generate N branches, score at checkpoints, prune losers:

```
4 branches @ 25% → Score → Keep 2
2 branches @ 50% → Score → Keep 1
1 branch   @ 100% → Output

Result: High-quality output at ~50% compute cost
```

## Requirements

- ComfyUI (latest)
- PyTorch 2.0+
- CUDA 11.8+ (for FP8 on RTX 40 series)

## Hardware Optimization

Automatically detects and uses:
- RTX 40 series FP8 TensorCores (1320 TFLOPS)
- BF16 on Ampere+ GPUs
- Mixed precision for optimal performance

## License

Apache 2.0 - See LICENSE file

---

*Built with advanced optimization research*
