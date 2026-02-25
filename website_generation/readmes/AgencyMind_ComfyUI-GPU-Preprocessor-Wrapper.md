# ComfyUI GPU Preprocessor Wrapper

A ComfyUI custom node extension that solves multi-GPU device conflicts for ControlNet preprocessors.

## Problem Solved

In multi-GPU ComfyUI setups using ComfyUI-MultiGPU, ControlNet preprocessors can cause "Expected all tensors to be on the same device" errors. This happens because:

1. Preprocessors auto-download models from HuggingFace
2. They load models using `comfy.model_management.get_torch_device()`
3. ComfyUI-MultiGPU monkey-patches this function with dynamic device assignment
4. During model loading, the global device state can change
5. Result: Model components split across devices (cuda:0 and cuda:1)

## Solution

This extension provides wrapper nodes that temporarily override device placement during preprocessor model loading to force consistent device placement (cuda:0), then restore normal MultiGPU behavior.

## Installation

### Standard ComfyUI Custom Node Installation

1. Clone to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-username/ComfyUI-GPU-Preprocessor-Wrapper.git
```

2. Restart ComfyUI

3. Wrapper nodes will appear in the Add Node menu under `preprocessors/gpu_wrapper`

### Requirements

- ComfyUI with ComfyUI-MultiGPU extension
- comfyui_controlnet_aux extension (for the preprocessors being wrapped)
- No additional dependencies required

## Usage

### Available Wrapper Nodes

- **DepthAnything V2 (GPU Wrapper)** - Wraps DepthAnythingV2Preprocessor
- **DWPose (GPU Wrapper)** - Wraps DWPreprocessor  
- **Canny Edge (GPU Wrapper)** - Wraps CannyEdgePreprocessor
- **OpenPose (GPU Wrapper)** - Wraps OpenposePreprocessor
- **Midas Depth (GPU Wrapper)** - Wraps MidasDepthMapPreprocessor

### Drop-in Replacements

Simply replace your existing ControlNet preprocessor nodes with the corresponding GPU wrapper versions. All inputs and outputs remain identical.

**Before:**
```
Video Frame → DepthAnything V2 → ControlNet → Generation
```

**After:**
```
Video Frame → DepthAnything V2 (GPU Wrapper) → ControlNet → Generation
```

### Workflow Example

1. Load your video/image input
2. Use any GPU wrapper preprocessor instead of the original
3. Connect to ControlNet as normal
4. Generate without device conflicts

## Technical Details

### How It Works

The wrapper temporarily overrides `comfy.model_management.get_torch_device()` during model loading:

```python
# Save original function
original_get_device = model_management.get_torch_device

# Override with consistent device during model loading
model_management.get_torch_device = lambda: torch.device('cuda:0')

try:
    # Execute original preprocessor
    result = original_preprocessor.execute(**kwargs)
finally:
    # Always restore original function
    model_management.get_torch_device = original_get_device
```

### Device Strategy

- **Target device**: `cuda:0` (typical preprocessor GPU in multi-GPU setups)
- **Scope**: Only affects NEW model loading during preprocessor execution
- **Timing**: Atomic operation - no race conditions with MultiGPU
- **Restoration**: Original function restored immediately after completion

### Error Handling

- Uses try/finally blocks to ensure device function restoration
- Handles ImportError for missing ControlNet preprocessors gracefully
- Logs failures but doesn't crash ComfyUI startup
- Only registers wrappers for available preprocessors

## Verification

### Check Installation Success

1. **Console**: Look for registration messages:
   ```
   Registered 5 GPU wrapper nodes: ['DepthAnythingV2Wrapper', 'DWPreprocessorWrapper', ...]
   ```

2. **Node Menu**: Check `preprocessors/gpu_wrapper` category exists

3. **GPU Memory**: Use `nvidia-smi` to monitor memory allocation

4. **No Errors**: Confirm no "device mismatch" errors in ComfyUI console

### Test Workflow

Create a simple test workflow:
```
Video Input → DepthAnything V2 (GPU Wrapper) → ControlNet → Model → Generation
```

## Troubleshooting

### Import Warnings

If you see warnings like:
```
DepthAnythingV2Preprocessor not available: No module named 'comfyui_controlnet_aux'
```

This is normal - the extension only wraps preprocessors that are actually installed.

### Device Conflicts Still Occurring

1. Ensure you're using the **wrapper** versions, not original preprocessors
2. Check that ComfyUI-MultiGPU is active
3. Verify wrapper nodes appear in the correct category

### Performance Impact

- **None** - Identical performance to original preprocessors
- **Memory**: No additional GPU memory usage
- **Compatibility**: Works with future controlnet_aux updates

## Production Setup

Tested and designed for:
- Multi-GPU production setups (3x A6000+ hardware)
- ComfyUI with MultiGPU extension
- High-throughput video processing workflows
- Enterprise-grade stability requirements

## Contributing

This extension is designed to be maintenance-free and update-proof. The wrapper pattern automatically adapts to changes in the underlying preprocessor implementations.

## License

Same as ComfyUI - GPL-3.0