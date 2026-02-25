### ComfyUI_NativeBlockSwap

Native block swap node for ComfyUI WAN models, reducing VRAM usage by swapping transformer blocks to CPU.

**✨ Features:**
- Compatible with WAN 2.1 and WAN 2.2 models (including all variants: VACE, Camera, HuMo, Animate, S2V)
- Swap up to 40 transformer blocks to CPU (14B model has 40 blocks, 1.3B model has 30 blocks)
- Optional embedding offloading (text and image embeddings)
- Non-blocking memory transfer option for faster performance

**📦 Installation:**
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/lum3on/ComfyUI_NativeBlockSwap.git
```

**🎯 Usage:**

![image](./samples/comfy_usage.png)

**⚙️ Parameters:**
- `blocks_to_swap`: Number of transformer blocks to offload to CPU (0-40)
- `offload_img_emb`: Offload image embeddings to CPU
- `offload_txt_emb`: Offload text embeddings to CPU
- `use_non_blocking`: Use non-blocking memory transfer (faster but uses more RAM)