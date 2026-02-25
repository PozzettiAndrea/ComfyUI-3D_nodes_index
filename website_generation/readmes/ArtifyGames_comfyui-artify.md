# ComfyUI Artify

ComfyUI Artify is a lightweight custom node pack focused on image utilities.

## Included nodes

- `Image Resize (Artify)`
  - Node id: `ArtifyImageResize`
  - Category: `Artify/Image`
- `Inpaint Crop (Artify)`
  - Node id: `ArtifyInpaintCrop`
  - Category: `Artify/Inpaint`
- `Inpaint Stitch (Artify)`
  - Node id: `ArtifyInpaintStitch`
  - Category: `Artify/Inpaint`

## Why this node exists

This resize node is designed to avoid the common `scale_by` pitfall where scale
is effectively applied twice. Here, `scale_by` is applied exactly once.

## Resize behavior

Target dimension priority:

1. `megapixels` (if `> 0`)
2. `resize_value` + `resize_mode` (`longest_side` or `shortest_side`)
3. `custom_width` / `custom_height`
4. original image size

Then:

- `scale_by` is applied once (skipped when `megapixels > 0`)
- `divisible_by` snaps final dimensions using `divisible_mode`:
  - `floor`
  - `ceil`
  - `nearest`

Output modes:

- `stretch`
- `crop`
- `pad`
- `pad_edge`
- `pad_edge_pixel`
- `pillarbox_blur`

Outputs:

- `IMAGE`
- `MASK` (if no input mask is provided, a zero mask is returned)
- `WIDTH`
- `HEIGHT`

## Inpaint Crop/Stitch behavior

`Inpaint Crop (Artify)` and `Inpaint Stitch (Artify)` are based on the same
crop-and-stitch concept, with a simplified crop pipeline:

- no pre-resize stage
- no outpainting/extend stage in the crop node
- no forced output target resize controls
- minimum context area control:
  - `min_context_megapixels`

The crop node computes context from mask/context-mask and then enforces this
minimum context area while preserving the input image aspect ratio and staying
inside image bounds. If the image is too small to reach the target megapixels,
it uses the largest possible context that fits.

To reduce stitch drift with diffusion/latent pipelines, crop dimensions are
internally aligned to a model-friendly grid.

## Install

### Method 1: ComfyUI custom_nodes folder

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ArtifyGames/comfyui-artify.git
```

If you add optional dependencies later:

```bash
python -m pip install -r requirements.txt
```

Restart ComfyUI and refresh the browser page.

## Quick test

1. Add `Image Resize (Artify)` to a workflow.
2. Feed a `1328x1328` image.
3. Set:
   - `custom_width=0`
   - `custom_height=0`
   - `megapixels=0`
   - `resize_value=0`
   - `scale_by=1.25`
   - `divisible_by=1`
4. Expected output: `1660x1660`.

## License

See `LICENSE`.
