# ComfyUI-LTXVideoLoRA
A set of custom nodes enabling LoRA support for LTX Video in ComfyUI.

### 25.02.2025 ⭐ NEW ⭐

- Update the **LTXV LoRA Loader** node for the **GGUF** support as a generic way
- Remove useless **LTXV Checkpoint Loader with LoRA** node

Please refer to the quantized versions of :
- **calcuis** - GGUF quantized and fp8 scaled versions of LTX-Video ([here](https://huggingface.co/calcuis/ltxv-gguf))
- **city96** - direct GGUF conversion of Lightricks/LTX-Video ([here](https://huggingface.co/city96/LTX-Video-gguf))

### 08.02.2025 - First release

- ~~Add LoRA support as a individual  **LTXV LoRA Loader** node > for Lightricks **ComfyUI-LTXVideo**~~
- ~~Add LoRA support inside a **LTXV Checkpoint Loader with LoRA** node > for log(td) **ComfyUI-LTXTricks**~~
- Add LoRA selector node that can be chained using multiple **LTXV LoRA Selector**

## Installation

#### Installation via ComfyUI-Manager

Installation via [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) is preferred. Simply search for `ComfyUI-LTXVideoLoRA` in the list of nodes.

#### Manual installation

Simply clone this repository to `custom-nodes` folder in your ComfyUI installation directory.

## Usage

### LTXV LoRA with the ComfyUI-LTXVideo nodes

![workflow](assets/LTXV-LoRA-Usage-1.png)
> [!CAUTION]
> Because the **LTXV Loader** official node use a specific model structure, you need to put the *ltxv_loader_as_input* option as **true**.

### LTXV LoRA with the ComfyUI-LTXTricks nodes

![workflow](assets/LTXV-LoRA-Usage-2.png)
> [!NOTE]
> Here the input node can be  the **'Load Diffusion Model'** node or the **'Load Checkpoint'** node  as well.

### LTXV LoRA with the GGUF Loader nodes

![workflow](assets/LTXV-LoRA-Usage-3.png)
> [!TIP]
> As you can see, you can use the GGUF with the LoRA loader followed by the modified LTX model by log(td)'s LTXTricks nodes.

## LoRA Training

For a **blazing fast training** of your LTXV LoRA you can use:
- **a-r-r-o-w's finetrainers** ([here](https://github.com/a-r-r-o-w/finetrainers))

## Credit and greetings

The main code is inspired by:
- comfyanonymous **ComfyUI** ([here](https://github.com/comfyanonymous/ComfyUI))
- Lightricks **ComfyUI-LTXVideo** ([here](https://github.com/Lightricks/ComfyUI-LTXVideo)) 
- log(td) **ComfyUI-LTXTricks** ([here](https://github.com/logtd/ComfyUI-LTXTricks))
- kijai **ComfyUI-HunyuanVideoWrapper** ([here](https://github.com/kijai/ComfyUI-HunyuanVideoWrapper)) for the LoRA Selector / Block Edit nodes.
