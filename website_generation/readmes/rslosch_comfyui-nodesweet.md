# ComfyUI Batch BBox Detector

Process batches of images (e.g., video frames) with ultralytics bbox detection in ComfyUI. This custom node package extends the standard `BboxDetectorCombined` to handle batches efficiently, making it ideal for processing 300+ video frames.

## Features

- **Batch Processing**: Handle multiple images in a single operation
- **Memory Efficient**: Chunked processing prevents out-of-memory errors on large batches
- **Three Implementations**: Choose the best approach for your workflow
- **Error Handling**: Robust processing that doesn't crash on individual frame failures
- **ComfyUI Integration**: Seamless integration with existing ImpactPack nodes

## Installation

### Method 1: ComfyUI Manager (Recommended when available)

1. Open ComfyUI Manager
2. Search for "Batch BBox Detector"
3. Click Install

### Method 2: Manual Installation

1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone or copy this repository:
   ```bash
   git clone https://github.com/yourusername/comfyui_bbox_batch.git
   ```
   
   Or manually create the directory structure:
   ```bash
   mkdir comfyui_bbox_batch
   cd comfyui_bbox_batch
   ```

3. Copy the following files:
   - `__init__.py`
   - `nodes/` directory (with all its files)
   - `README.md`

4. Restart ComfyUI

## Node Types

### 1. BBox Detector (Batch)

**Best for**: Small to medium batches (< 100 frames)

Standard batch processor that processes each frame sequentially and returns stacked results.

**Inputs:**
- `bbox_detector` (BBOX_DETECTOR): The detector model
- `images` (IMAGE): Batch of images `[B, H, W, C]`
- `threshold` (FLOAT): Detection confidence threshold (0.0-1.0, default: 0.5)
- `dilation` (INT): Mask expansion amount (-512 to 512, default: 4)
- `return_type` (OPTIONAL): "mask_only" or "image_with_boxes"

**Outputs:**
- `images` (IMAGE): Processed images `[B, H, W, C]`
- `masks` (MASK): Detection masks `[B, H, W]`

### 2. BBox Detector (Batch ForEach)

**Best for**: List-based workflows, when memory efficiency is critical

Uses ComfyUI's INPUT_IS_LIST pattern for more memory-efficient processing in certain workflows.

**Inputs:** Same as standard batch processor

**Outputs:** Lists of images and masks

### 3. BBox Detector (Batch Chunked) ⭐ RECOMMENDED

**Best for**: Large batches (300+ frames), video processing

Processes batches in chunks with memory management between chunks. This is the **recommended node for video frame processing**.

**Inputs:**
- Same as standard batch processor, plus:
- `chunk_size` (INT): Number of frames per chunk (1-128, default: 32)

**Outputs:** Same as standard batch processor

**Memory Management:**
- Automatically clears CUDA cache between chunks
- Progress tracking for large batches
- Prevents OOM errors on long videos

## Usage Examples

### Basic Video Frame Processing

```
Workflow:
Video Loader → Video to Image Batch → BBox Detector (Batch Chunked) → Output
```

**Recommended Settings for 300+ frames:**
- `threshold`: 0.5 (adjust based on detection quality needs)
- `dilation`: 4 (increase for larger mask coverage)
- `chunk_size`: 16-32 (lower for less VRAM, higher for faster processing)

### Workflow with Mask Processing

```
Workflow:
Video Loader → Video to Image Batch → BBox Detector (Batch Chunked) → MaskToImage → Save Image
                                    ↓
                                  Save Mask
```

### Integration with ImpactPack

```
Workflow:
Load Checkpoint → UltralyticsDetectorProvider → BBox Detector (Batch Chunked)
                                              ↓
Image Batch ──────────────────────────────────┘
```

## Performance Tips

### Memory Optimization

1. **Adjust Chunk Size**: 
   - 8GB VRAM: chunk_size = 8-16
   - 12GB VRAM: chunk_size = 16-32
   - 24GB+ VRAM: chunk_size = 32-64

2. **Image Resolution**:
   - Lower resolution reduces memory usage
   - Consider downscaling before detection if appropriate

3. **Enable Mixed Precision**:
   - If your detector supports it, enable FP16/mixed precision

### Speed Optimization

1. **Use Appropriate Node**:
   - Small batches (< 50): Use standard `BboxDetectorBatch`
   - Large batches (> 100): Use `BboxDetectorBatchChunked`

2. **Batch Processing**:
   - Larger chunk sizes = faster processing (if memory allows)
   - Balance between speed and stability

3. **GPU Utilization**:
   - Ensure CUDA is available and properly configured
   - Monitor GPU usage with `nvidia-smi`

## Parameters Explained

### threshold (Float, 0.0-1.0)

Controls detection confidence. Higher values = more confident detections but may miss objects.

- **0.3-0.4**: Detect more objects, more false positives
- **0.5** (default): Balanced detection
- **0.6-0.8**: Fewer detections, higher confidence

### dilation (Int, -512 to 512)

Expands or contracts the detection mask.

- **Negative values**: Contract mask (useful for precise boundaries)
- **0**: No change
- **Positive values**: Expand mask (useful for including surrounding context)
- **4** (default): Slight expansion for better coverage

### chunk_size (Int, 1-128)

Number of frames to process before clearing memory cache.

- **Lower (8-16)**: Better memory efficiency, slower processing
- **Higher (32-64)**: Faster processing, more memory usage
- **32** (default): Good balance for most systems

## Troubleshooting

### Out of Memory Errors

**Problem**: `RuntimeError: CUDA out of memory`

**Solutions:**
1. Reduce `chunk_size` to 8 or 16
2. Lower input image resolution
3. Close other GPU-intensive applications
4. Use `BboxDetectorBatchChunked` instead of standard batch

### Empty Masks

**Problem**: All masks are black/empty

**Solutions:**
1. Lower `threshold` (try 0.3-0.4)
2. Verify detector model is loaded correctly
3. Check if objects are present in images
4. Ensure image format is correct (RGB, proper range)

### Slow Processing

**Problem**: Processing takes too long

**Solutions:**
1. Increase `chunk_size` (if memory allows)
2. Use `BboxDetectorBatch` for small batches
3. Reduce image resolution
4. Verify GPU is being utilized (check with `nvidia-smi`)

### Detection Quality Issues

**Problem**: Poor detection results

**Solutions:**
1. Adjust `threshold` value
2. Try different bbox detector models
3. Ensure images are properly preprocessed
4. Check image quality and resolution

## Technical Details

### Tensor Formats

- **IMAGE tensors**: `[B, H, W, C]` - Batch, Height, Width, Channels
- **MASK tensors**: `[B, H, W]` - Batch, Height, Width
- All tensors use the same device as input images

### Error Handling

- Individual frame failures are caught and logged
- Failed frames return empty masks and original images
- Processing continues even if some frames fail
- Error messages indicate which frame failed and why

### Memory Management

- CUDA cache is cleared between chunks (chunked processor)
- Tensors are kept on the same device throughout processing
- Intermediate results are properly cleaned up

## Compatibility

- **ComfyUI**: Latest version
- **Dependencies**: 
  - PyTorch
  - NumPy
  - Ultralytics (for bbox detection models)
  - ImpactPack (for BBOX_DETECTOR type)

## Development

### Project Structure

```
comfyui_bbox_batch/
├── __init__.py                            # Package initialization with node mappings
├── nodes/
│   ├── __init__.py                        # Nodes package initialization
│   ├── bbox_batch_detector.py             # Standard batch processor
│   ├── bbox_batch_detector_foreach.py     # ForEach list-based processor
│   └── bbox_batch_detector_chunked.py     # Chunked processor for large batches
└── README.md                              # This file
```

### Node Architecture

Each node class follows ComfyUI's node pattern:
- `INPUT_TYPES`: Defines input parameters
- `RETURN_TYPES`: Defines output types
- `FUNCTION`: Name of the processing method
- `CATEGORY`: Node category in UI

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **ComfyUI Discord**: Get help in the custom nodes channel

## Changelog

### Version 1.0.0 (Current)

- Initial release
- Three node implementations (Standard, ForEach, Chunked)
- Support for batches of 300+ frames
- Memory-efficient chunked processing
- Comprehensive error handling

## Credits

- Inspired by `BboxDetectorCombined` from ImpactPack
- Built for the ComfyUI community
- Ultralytics for bbox detection capabilities

## Acknowledgments

Thanks to the ComfyUI and ImpactPack communities for their excellent work and support.


