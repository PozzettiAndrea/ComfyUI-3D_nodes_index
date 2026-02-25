# ComfyUI extension

## Touchpad and trackpad support

Fixes the annoying trackpad zooming in ComfyUI

## Implements

### Touchpad gestures

- Two-finger touchpad swiping to pan in all directions
- Two-finger pinch to zoom in and out

### Optional mouse controls

- Pan up and down by scrolling
- Pan left and right by holding shift while scrolling
- Zoom in and out by holding control while scrolling

### Tested with

#### Browsers

- Chrome (133)
- Firefox (133) (not yet fully tested in combination with mice)

#### Hardware

- Windows laptop touchpad
- MacBook touchpad
- Generic Logitech mouse
- Apple Mighty Mouse
- Apple Magic Mouse

### Should in theory work on

- MacBooks without multitouch gesture support, so older touchpads like on MacBook 4,1 and below
- Touchpads and trackpads without WDF


### Installation

1. Clone this repository into ComfyUI/custom_nodes/
2. Restart ComfyUI
3. Reload the UI
4. Enjoy!

Partially inspired by: https://github.com/subtleGradient/TinkerBot-tech-for-ComfyUI-Touchpad