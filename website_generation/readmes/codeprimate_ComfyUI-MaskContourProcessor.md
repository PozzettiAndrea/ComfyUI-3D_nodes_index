# ComfyUI Mask Contour Processor

_Version 0.1_

A ComfyUI node that improves inpainting results by extending mask boundaries with geometric patterns, helping create smoother transitions and better context for AI-driven image completion.

## Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/codeprimate/ComfyUI-MaskContourProcessor
cd ComfyUI-MaskContourProcessor
pip install -r requirements.txt
```

## Usage

### Parameters

- **Line Length** (0.0 - 3.0): Controls pattern extension distance. Start with 1.0
- **Line Count** (1 - 40): Sets pattern density. Recommended: 20-30
- **Line Width** (0.0 - 0.1): Adjusts pattern thickness. Start with 0.01

### Recommended Settings

**Large Areas:**
- Line Length: 1.5-2.0
- Line Count: 30-40
- Line Width: 0.015-0.02

**Detail Work:**
- Line Length: 0.5-1.0
- Line Count: 25-35
- Line Width: 0.005-0.01

## Tips

- Start with conservative settings
- Adjust Line Length based on image scale
- Use higher Line Count for complex textures
- Maximum recommended image size: 4096x4096

## License

MIT License - see [LICENSE](LICENSE) file.

## Contributing

Contributions welcome. Please open an issue first for major changes.
