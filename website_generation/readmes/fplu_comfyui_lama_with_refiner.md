# ComfyUI LaMa with Refiner Inpaint Nodes

Large-image inpainting in **ComfyUI** using **LaMa** followed by a refinement stage.

---

## Installation

### 1 / 2 Install the custom node

```bash
cd PATH_TO_COMFYUI/ComfyUI/custom_nodes
git clone https://github.com/fplu/comfyui_lama_with_refiner.git
```

### 2 / 2 Download the LaMa model

Download **`big-lama.pt`** from any of the mirrors below and place it in
`PATH_TO_COMFYUI/ComfyUI/models/inpaint/` (create the `inpaint` folder if it doesn’t already exist).

- [https://huggingface.co/fashn-ai/LaMa/blob/main/big-lama.pt](https://huggingface.co/fashn-ai/LaMa/blob/main/big-lama.pt)
- [https://huggingface.co/aasda111/bigllama/blob/main/big-lama.pt](https://huggingface.co/aasda111/bigllama/blob/main/big-lama.pt)
- [https://huggingface.co/okaris/simple-lama/blob/main/big-lama.pt](https://huggingface.co/okaris/simple-lama/blob/main/big-lama.pt)

---

## How to Use in ComfyUI

1. Add a **Load Inpaint LaMa Model** node and select **`big-lama.pt`**.
2. Add an **Inpaint (LaMa + Refinement)** node and connect:

   - **Model** → output of _Load Inpaint LaMa Model_
   - **Image** → image you want to inpaint
   - **Mask** → corresponding mask of the image

---

## Acknowledgements

- **LaMa + Refiner** [geomagical/lama-with-refiner](https://github.com/geomagical/lama-with-refiner)
- **LaMa** [advimman/lama](https://github.com/advimman/lama)
