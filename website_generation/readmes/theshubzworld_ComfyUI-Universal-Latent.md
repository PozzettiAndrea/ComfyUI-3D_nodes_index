# 🌌 Universal Latent Node for ComfyUI

An enhanced empty latent node for ComfyUI with extended aspect ratio support and optimized performance. Compatible with various models including SD3.5 and SDXL.

## ✨ Features

- **Wide Range of Aspect Ratios** - Supports square, portrait, landscape, and custom aspect ratios
- **High Resolution Support** - Up to 1536x1536 resolution
- **Aspect Ratio Lock** - Lock width or height while adjusting the other dimension
- **Flexible Downsampling** - Auto or manual selection of downsampling factor
- **Batch Processing** - Generate multiple latent tensors at once
- **Optimized Performance** - Efficient tensor operations for faster processing

## 🚀 Installation

1. Clone this repository into your ComfyUI `custom_nodes` directory:
   ```
   cd ComfyUI/custom_nodes
   git clone https://github.com/theshubzworld/ComfyUI-Universal-Latent.git
   ```

2. Restart ComfyUI

## 🎨 Usage

1. Find the node in the node browser as "🌌✨ Universal Latent (Enhanced) 🎨⚡"
2. Select your desired resolution from the dropdown
3. Adjust batch size and other parameters as needed
4. Connect the output to your model's latent input

## ⚙️ Parameters

- **Resolution**: Predefined resolutions with common aspect ratios
- **Batch Size**: Number of latent tensors to generate
- **Width/Height Override**: Manually set dimensions
- **Aspect Ratio Lock**: Lock width or height while adjusting the other dimension
- **Latent Channels**: Number of channels in latent space (4 for SD, 16 for Flux)
- **Downsample Factor**: Auto (8) or manual selection (4 or 8)
- **Invert Ratios**: Swap width and height dimensions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
