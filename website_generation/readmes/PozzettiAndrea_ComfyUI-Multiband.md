# ComfyUI-Multiband

Multi-channel image handling for ComfyUI. Work with images that have arbitrary number of channels (segmentation masks, feature maps, spectral bands, etc.).

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-username/ComfyUI-Multiband.git
pip install -r ComfyUI-Multiband/requirements.txt
```

## Data Type

`MULTIBAND_IMAGE` - A tensor with shape `(B, C, H, W)` where:
- B = batch size
- C = number of channels (arbitrary)
- H, W = spatial dimensions

Includes optional channel names and metadata.

## Nodes

### I/O

| Node | Description |
|------|-------------|
| **Load Multiband Image** | Load from .npy, .npz, .tiff, .exr |
| **Save Multiband Image** | Save to .npy, .npz, .tiff, .exr |
| **Preview Multiband Image** | Visualize as RGB, single channel, or grid |

### Conversion

| Node | Description |
|------|-------------|
| **Image to Multiband** | Convert IMAGE (B,H,W,3) to MULTIBAND |
| **Multiband to Image** | Extract 3 channels as IMAGE |
| **Mask to Multiband** | Convert MASK to single-channel MULTIBAND |
| **Multiband to Mask** | Extract one channel as MASK |

### Compose/Decompose

| Node | Description |
|------|-------------|
| **Compose Multiband** | Stack multiple inputs into one MULTIBAND |
| **Decompose Multiband** | Split into individual MASK channels |

### Operations

| Node | Description |
|------|-------------|
| **Select Multiband Channels** | Select channels by index or name |
| **Concat Multiband** | Concatenate two MULTIBANDs |
| **Rename Multiband Channels** | Rename channel names |

## File Formats

| Format | Extension | Features |
|--------|-----------|----------|
| NumPy | .npy | Simple, fast, no metadata |
| NumPy Compressed | .npz | Channel names + metadata |
| TIFF | .tiff, .tif | Multi-page, metadata in description |
| OpenEXR | .exr | Named channels, HDR (optional) |

## Example Usage

### Stack segmentation masks
```
[SAM Mask 1] ──┐
[SAM Mask 2] ──┼── [Compose Multiband] ── [Save Multiband]
[SAM Mask 3] ──┘
```

### Preview channels
```
[Load Multiband] ── [Preview Multiband (mode=channel_grid)]
```

### Extract specific channels
```
[Load Multiband] ── [Select Channels "0,2,5"] ── [Multiband to Image]
```

## License

MIT
