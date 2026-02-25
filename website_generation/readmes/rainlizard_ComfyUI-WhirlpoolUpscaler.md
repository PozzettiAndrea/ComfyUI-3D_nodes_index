# Whirlpool Upscaler

This is a modified implementation of impact-pack's iterative upscaler. It leans in on the idea that giving too much attention to computation at high resolutions isn't a good idea.

## Node settings

- **upscale_by**: Final resolution multiplier (e.g., 2.0 = double width and height)
- **upscale_curve**: Progression curve for all parameters (resolution, CFG, steps, denoise). 1.0 = linear progression, >1.0 = exponential progression
- **iterations**: Number of complete sampling cycles to perform (4 iterations would mean doing four sets of Steps)
- **steps_start**: Number of sampling steps for the first iteration
- **steps_end**: Number of sampling steps for the last iteration
- **cfg_start**: CFG scale for the first iteration
- **cfg_end**: CFG scale for the last iteration
- **denoise_start**: Denoise strength for the first iteration
- **denoise_end**: Denoise strength for the last iteration
- **resize_filter**: Image resizing filter algorithm - "lanczos", "nearest-exact", "bilinear", "area", or "bicubic"
- **tile_size**: Tile size for VAE operations to manage memory usage (if you get lag due to low VRAM then set this lower)

## How It Works

Each iteration upscales the image to a progressively larger resolution. Steps, CFG, and denoise values evolve from start to end values across iterations. The `upscale_curve` determines how linear or non-linear this progression is.

### Upscale Curve Examples (4 iterations)
- **upscale_curve = 1.0**: Linear progression → 1.25x → 1.50x → 1.75x → 2.00x
- **upscale_curve = 2.0**: More exponential → 1.13x → 1.42x → 1.69x → 2.00x

- **Higher `upscale_curve` values:**
   - Faster, spends more time sampling at lower resolutions
   - Smarter, reduces body horror
   - Less detail, resembles base image more
- **Lower `upscale_curve` values:**
   - Slower, spends more time sampling at higher resolutions
   - Dumber, more body horror
   - More detail, different to base image

So try to strike a balance. And if you change `upscale_by` then you'll definitely want to change `upscale_curve` as well.

## Tips

- **Reducing Artifacts**: Either decrease CFG, increase steps, or connect the model input to a Skimmed CFG node.
- **Too Many Fingers/Body Horror**: Either reduce denoise, reduce the base resolution of the image you're feeding the upscaler, or increase the `upscale_curve`.
- **Better Images**: If you connect the model input to a Skimmed CFG node and set `cfg_start` really high, it'll usually result in better images.

## Known Issues

- Cancelling doesn't instantly stop the generation process. You have to wait for the current iteration to finish before the process will terminate. Please share if you have the solution.
