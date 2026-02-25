# Nearest Qwen Resolution

A simple ComfyUI custom node that takes an `IMAGE` input and outputs the width and height (two `INT`s) of the nearest recommended Qwen-Image resolution, matching orientation and minimizing aspect ratio difference. Ties are resolved by smallest size delta to the input image.

- Input: `IMAGE` (tensor shaped `(B,H,W,C)`; first frame used)
- Output: `width (INT)`, `height (INT)`
- Setting: `square_tolerance` (percent; how close to 1:1 counts as square)

## How it decides
1. Determines orientation (Wide / Vertical / Square) from the input size with a configurable tolerance for square.
2. Filters the Qwen presets to that orientation.
3. Chooses the preset with the smallest aspect ratio difference; ties broken by the smallest difference to the input dimensions.

## Presets

These resolutions are the **official recommended sizes** for Qwen-Image models, specifically optimized during the final training phase. They cover common aspect ratios like 9:16 (928x1664), 1:1 (1328x1328), and 16:9 (1664x928), ensuring stable generation quality without artifacts.

**Why these sizes?**
- Based on 32-pixel multiples (~1-2 megapixels), allowing efficient processing by diffusion models
- Other common social media formats (e.g., 1080x1080 or 1080x1350) often produce inferior results, as they aren't aligned with Qwen's training data

**Available presets:**
- Vertical: `928x1664` (9:16), `1056x1584` (2:3), `1140x1472` (3:4)
- Square: `1328x1328` (1:1)
- Wide: `1664x928` (16:9), `1584x1056` (3:2), `1472x1140` (4:3)

## Category
Appears under `image/resolution`.

## Notes
- Qwen-Image does not require 64-multiple rounding, so widths/heights are reported exactly as the preset.
- If the input is very close to square (within `square_tolerance%`), the square preset is preferred.

## License
MIT License - see [LICENSE](LICENSE) for details.
