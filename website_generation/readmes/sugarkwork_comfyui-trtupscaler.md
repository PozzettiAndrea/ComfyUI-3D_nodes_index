# ComfyUI TensorRT Upscaler

A high-performance image upscaling node for ComfyUI using TensorRT acceleration.

![image](https://github.com/user-attachments/assets/cf74b89a-bffe-4f65-a6a6-2195c33248f0)


## Features

- TensorRT-accelerated inference for fast upscaling
- Batch processing support
- Tile-based processing for large images
- Support for both FP16 and FP32 precision
- Automatic model detection from file names
- Feathered tile blending to reduce seams

## Requirements

### System Requirements
- NVIDIA GPU with Compute Capability 6.0+ (Pascal architecture or newer)
- CUDA 11.8 or newer
- Windows 10/11 or Linux

### Software Dependencies
- TensorRT 8.6.0 or newer
- Python 3.8+
- PyTorch 2.0+
- CUDA-compatible GPU drivers

## Installation

### 1. Install TensorRT
Download and install TensorRT from NVIDIA Developer:
https://developer.nvidia.com/tensorrt

Follow NVIDIA's installation guide for your platform.

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up Models
Run the setup script to download and convert models:

**Windows:**
```cmd
setup_models.bat
```

**Linux/Manual:**
```bash
python convert_model.py <model_name> --models-dir ../../models/upscale_models
```

## Supported Models

The node automatically detects upscaling models in the `models/upscale_models` directory. Currently supported:
- 4x_foolhardy_Remacri
- 4x-UltraSharp
- Any compatible .pth model (requires conversion)

## Usage

1. Add the "TRT Upscaler" node to your ComfyUI workflow
2. Connect an image input
3. Select your model from the dropdown
4. Adjust tile size and overlap as needed
5. Choose precision (FP16 recommended for speed)

### Parameters

- **image**: Input image tensor
- **model_name**: TensorRT model to use for upscaling
- **tile_size**: Size of processing tiles (64-2048, default: 512)
- **tile_overlap**: Overlap between tiles (0-256, default: 32)
- **use_fp16**: Use FP16 precision (faster, slightly lower quality)

### Tile Settings Guidelines

- **Small GPU memory**: Use smaller tile sizes (256-512)
- **Large GPU memory**: Use larger tile sizes (1024-2048)
- **High overlap**: Better blending but slower processing
- **Low overlap**: Faster but may show tile seams

## Model Conversion

To convert your own .pth models:

1. Place the .pth file in `models/upscale_models/`
2. Run: `python convert_model.py <model_name>`
3. The script will create both FP16 and FP32 TensorRT engines

## Performance Tips

1. **Use FP16**: ~2x faster with minimal quality loss
2. **Optimize tile size**: Balance between speed and memory usage
3. **Batch processing**: Process multiple images together when possible
4. **GPU memory**: Monitor VRAM usage and adjust tile size accordingly

## Troubleshooting

### "TensorRT not available"
- Ensure TensorRT is properly installed
- Check that CUDA is available: `nvidia-smi`
- Verify Python can import tensorrt: `python -c "import tensorrt"`

### "No TRT models found"
- Run `setup_models.bat` to download and convert models
- Check that .trt files exist in `models/upscale_models/`
- Ensure model names include scale factor (e.g., "4x", "2x")

### Out of memory errors
- Reduce tile size
- Use FP16 precision
- Close other GPU-intensive applications
- Consider upgrading GPU memory

### Poor upscaling quality
- Try FP32 precision
- Increase tile overlap
- Use a different model
- Check input image quality

## Development

### Running Tests
```bash
python -m pytest test_trt_upscaler.py -v
```

### Adding New Models
1. Add model URL to `setup_models.bat`
2. Ensure model follows naming convention (include scale factor)
3. Test conversion with `convert_model.py`

## File Structure

```
comfyui-trtupscaler/
├── __init__.py              # Node registration
├── nodes.py                 # Main TRTUpscaler node
├── convert_model.py         # Model conversion utilities
├── setup_models.bat         # Windows setup script
├── requirements.txt         # Python dependencies
├── test_trt_upscaler.py     # Unit tests
└── README.md               # This file
```

## License

This project follows the same license as ComfyUI.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review ComfyUI logs for detailed error messages
3. Open an issue with system info and error details
