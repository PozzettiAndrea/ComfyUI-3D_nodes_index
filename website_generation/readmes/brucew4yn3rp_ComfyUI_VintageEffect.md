## ComfyUI node that applies vintage/retro effects through JPG compression, color grading, film grain, and vignette to emulate realistic photo aesthetics.

<img width="1684" height="780" alt="workflow" src="https://github.com/user-attachments/assets/83f5b134-5b3d-48b8-a81a-a964d14e374c" />

Args:
- images: Tensor of images in ComfyUI format [B, H, W, C]
- quality: JPG compression quality (0-100)
- passes: Number of compression passes
- grain_strength: Strength of grain effect (0-100, 0 = disabled)
- vignette_strength: Strength of vignette effect (0-100, 0 = disabled)
- color_grade: Color grading preset
- saturation: Color saturation (0-200, 100 = original)
