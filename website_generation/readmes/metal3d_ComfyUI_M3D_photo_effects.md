# M3D photo effects for ComfyUI

This repository provides some nodes to make photo effects.

![Effects](images/effects.png)

At this time, we only present the "Bleach Bypass" and "RGB Curve" effects.
But, keep in touch, we will add more effects soon.

## Installation

As I am using Linux, I cannot ensure that it works well on Windows or macOS. But, I think it should work. I strongly
recommend you to use the ComfyUI manager and to install this module searching "M3D" inside.

For the moment, this module has no requirements. ComfyUI already requires the `numpy` and `Pillow` packages. And we only
use these packages.

## The bleach bypass effect

This common effect is used in movies and photos to give a dramatic look. It is commonly used in war movies, but it can
be used in any kind of movie or photo.

![Bleach Bypass](./images/bleach-bypass.png)

- The slope makes contrast more dramatic (keep the value near 4.0)
- the shadows offset should fix brightness (keep the value near 0.5)
- the desaturation will remove colors from the base layer, it will not remove all colors
- the overlay strength will make the effect stronger or weaker, this parameter should stay between 0.8 and 1.0

The displayed curve, below the values, shows the S-curve applied to the base before making the "overlay". It's highly
experimental and the drawing of this curve is not perfect. But it gives an idea of what the effect will look like.

## RGB Curve

The RGB curve is a simple curve that can be used to adjust all the RGB channels at once.
It is a simple curve that can be used to enforce shadows, midtones, and highlights.

![RGB Curve](./images/rgb-curve.png)
