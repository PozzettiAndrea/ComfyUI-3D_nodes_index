# ComfyUI-ARZUMATA

Random nodes for ComfyUI for various purposes.

## Nodes List

### 🔧 Universal Device Override (New!)

Type-safe node that forces **any model or module** to run on a specified device (`cpu`, `cuda:0`, etc.).

Designed to work seamlessly with:
- `MODEL`, `CLIP`, `VAE`
- `WANVAE`, `CLIP_VISION`
- `CONTROL_NET`, `T2I_ADAPTER`, `IP_ADAPTER`
- And other custom types

---

### Caching CLIP Text Encode for FLUX

A simple performance-optimized FLUX node that stores CLIP to CONDITIONING conversion results in it's cache.
Caching eliminates redundant processing time by reusing previous results, significantly improving workflow efficiency and saving a lot of time.
It only activates when there is a change in one of the text inputs, clip model change or cache expired.

What node caches:
- CLIP model reference in memory (you can switch clip model and try it without losing cache from previous clip model should you decide to switch back) 
- clip_l string
- t5xxx string

> **Guidance value is NOT cached** — can be changed on the fly without invalidating cache

There is also a cache limit option to limit cache size, it will delete the oldest cache when the cache size is exceeded.

### Caching CLIP Text Encode

Same as above, but simplified:
- Single text input
- No guidance value

---

## Installation

Clone this repository to `ComfyUI/custom_nodes` directory.

## Credit

- [discus0434/comfyui-caching-embeddings](https://github.com/discus0434/comfyui-caching-embeddings) — inspiration for caching logic
- City96 [Apache2] [ComfyBootlegOffload](https://gist.github.com/city96/30743dfdfe129b331b5676a79c3a8a39)

**And, to all ComfyUI custom node developers**