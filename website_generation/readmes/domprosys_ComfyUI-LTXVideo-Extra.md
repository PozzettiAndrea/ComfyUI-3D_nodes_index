# ComfyUI-LTXVideo-Extra

Extra nodes for LTX-2 video generation in ComfyUI.

## Nodes

### LTXV Img To Video Inplace At Index

Enhanced version of the built-in `LTXVImgToVideoInplace` that supports:

- **Arbitrary frame placement** — place an image at any frame, not just frame 0. Use `frame_idx=-1` for the last frame.
- **Chainable noise masks** — chain multiple instances to condition multiple frames (e.g., first + last frame) without masks overwriting each other.
- **Preprocessing** — CRF compression, Gaussian blur, interpolation method, and crop mode (matching `LTXVAddGuideAdvanced`).

#### Example: First + Last Frame Conditioning with IC-LoRA

```
EmptyLTXVLatentVideo (97 frames)
  → LTXV Img To Video Inplace At Index (frame_idx=0, first frame)
  → LTXV Img To Video Inplace At Index (frame_idx=-1, last frame)
  → Add Video IC-LoRA Guide (driving video)
  → LTXVCropGuides
  → CFGGuider + SamplerCustomAdvanced
```

## Install

```bash
cd /path/to/ComfyUI/custom_nodes/
git clone https://github.com/domprosys/ComfyUI-LTXVideo-Extra.git
```

Then restart ComfyUI. No additional dependencies required.

## Update

```bash
cd /path/to/ComfyUI/custom_nodes/ComfyUI-LTXVideo-Extra/
git pull
```
