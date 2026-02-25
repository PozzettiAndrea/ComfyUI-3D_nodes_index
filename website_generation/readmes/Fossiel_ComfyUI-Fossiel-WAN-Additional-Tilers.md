# ComfyUI-Fossiel-WAN-Additional-Tilers

This is a suite of nodes which was inspired by [ComfyUI--WanImageToVideoTiled](https://github.com/stduhpf/ComfyUI--WanImageToVideoTiled) and brings VAE tiling functionality to WAN conditioners not *(yet)* supported by ComfyUI--WanImageToVideoTiled. The nodes function identically to their original counterparts with the exception of VAE tiling. By tiling the conditioners' VAE encoding, additional frames and/or larger frame sizes can be squeezed from your VRAM with zero impact on the quality and only negligable impact on generation time. This is especially useful in low-VRAM setups, where the conditioner can oftentimes be a bottle neck.

---

## Nodes

**Wan22 Animate To Video (Tiled VAE Encode)** - Original source: [ComfyUI native nodes](https://github.com/comfyanonymous/ComfyUI)  

**Wan22 First Middle Last Frame (Tiled VAE Encode)** - Original source: [ComfyUI-Wan22FMLF](https://github.com/wallen0322/ComfyUI-Wan22FMLF)  

**Wan22 Fun Control To Video (Tiled VAE Encode)** - Original source: [ComfyUI native nodes](https://github.com/comfyanonymous/ComfyUI)  

**Wan22 Painter I2V (Tiled VAE Encode)** - Original source: [ComfyUI-PainterI2V](https://github.com/princepainter/ComfyUI-PainterI2V)  

**Wan22 Painter FLF2V (Tiled VAE Encode)** - Original source: [Comfyui-PainterFLF2V](https://github.com/princepainter/Comfyui-PainterFLF2V)  

**Wan22 Painter Long Video (Tiled VAE Encode)** - Original source: [ComfyUI-PainterLongVideo](https://github.com/princepainter/ComfyUI-PainterLongVideo)  

**Wan22 Sound Image To Video (Tiled VAE Encode)** - Original source: [ComfyUI native nodes](https://github.com/comfyanonymous/ComfyUI)  

**Wan22 Sound Image To Video Extend (Tiled VAE Encode)** - Original source: [ComfyUI native nodes](https://github.com/comfyanonymous/ComfyUI)  

---

### Installation Instructions
1. Clone or download this repository to your local machine.
2. Copy the repository folder to your ComfyUI custom nodes directory: `ComfyUI/custom_nodes/`
3. Restart ComfyUI to load the Fossiel-WAN-Additional-Tilers nodes and refresh active session.

---

## History
2025/12/02 – Original commit.  

---

## Credits  
- [comfyanonymous](https://github.com/comfyanonymous), [stduhpf](https://github.com/stduhpf), [wallen0322](https://github.com/wallen0322), [princepainter](https://github.com/princepainter)  
- Model developers for supplying fantastic open source models, free of charge.  
- Developed with help from Grok3  

