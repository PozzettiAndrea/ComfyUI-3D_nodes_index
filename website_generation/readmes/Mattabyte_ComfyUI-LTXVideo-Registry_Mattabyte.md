# ComfyUI-LTXVideo

ComfyUI-LTXVideo is a collection of custom nodes for ComfyUI, designed to provide useful tools for working with the LTXV model.
The model itself is supported in the core ComfyUI [code](https://github.com/comfyanonymous/ComfyUI/tree/master/comfy/ldm/lightricks).
The main LTXVideo repository can be found [here](https://github.com/Lightricks/LTX-Video).

# 5.03.2025 :star: LTXVideo 0.9.5 Release :star:

### LTXVideo 0.9.5 introduces:

1. Improved quality with reduced artifacts.
2. Support for higher resolution and longer sequences.
3. Frame and sequence conditioning (beyond the first frame).
4. Enhanced prompt understanding.
5. Commercial license availability.

### Technical Updates

Since LTXVideo is now fully supported in the ComfyUI core, we have removed the custom model implementation. Instead, we provide updated workflows to showcase the new features:

1. **Frame Conditioning** – Enables interpolation between given frames.
2. **Sequence Conditioning** – Allows motion interpolation from a given frame sequence, enabling video extension from the beginning, end, or middle of the original video.
3. **Prompt Enhancer** – A new node that helps generate prompts optimized for the best model performance.
   See the [Example Workflows](#example-workflows) section for more details.

### LTXTricks Update

The LTXTricks code has been integrated into this repository (in the `/tricks` folder) and will be maintained here. The original [repo](https://github.com/logtd/ComfyUI-LTXTricks) is no longer maintained, but all existing workflows should continue to function as expected.

## 22.12.2024

Fixed a bug which caused the model to produce artifacts on short negative prompts when using a native CLIP Loader node.

## 19.12.2024 ⭐ Update ⭐

1. Improved model - removes "strobing texture" artifacts and generates better motion. Download from [here](https://huggingface.co/Lightricks/LTX-Video/resolve/main/ltx-video-2b-v0.9.1.safetensors).
2. STG support
3. Integrated image degradation system for improved motion generation.
4. Additional initial latent optional input to chain latents for high res generation.
5. Image captioning in image to video [flow](assets/ltxvideo-i2v.json).

## Installation

Installation via [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) is preferred. Simply search for `ComfyUI-LTXVideo` in the list of nodes and follow installation instructions.

### Manual installation

1. Install ComfyUI
2. Clone this repository to `custom-nodes` folder in your ComfyUI installation directory.
3. Install the required packages:

```bash
cd custom_nodes/ComfyUI-LTXVideo && pip install -r requirements.txt
```

For portable ComfyUI installations, run

```
.\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-LTXVideo\requirements.txt
```

### Models

1. Download [ltx-video-2b-v0.9.1.safetensors](https://huggingface.co/Lightricks/LTX-Video/blob/main/ltx-video-2b-v0.9.1.safetensors) from Hugging Face and place it under `models/checkpoints`.
2. Install one of the t5 text encoders, for example [google_t5-v1_1-xxl_encoderonly](https://huggingface.co/mcmonkey/google_t5-v1_1-xxl_encoderonly/tree/main). You can install it using ComfyUI Model Manager.

## Example workflows

Note that to run the example workflows, you need to have some additional custom nodes, like [ComfyUI-VideoHelperSuite](https://github.com/kosinkadink/ComfyUI-VideoHelperSuite) and others, installed. You can do it by pressing "Install Missing Custom Nodes" button in ComfyUI Manager.

### Image-to-video

[Download workflow](assets/ltxvideo-i2v.json)
![workflow](assets/ltxvideo-i2v.png)

### Text-to-video

[Download workflow](assets/ltxvideo-t2v.json)
![workflow](assets/ltxvideo-t2v.png)

### Frame Interpolation

[Download workflow](assets/ltxvideo-frame-interpolation.json)
![workflow](assets/ltxvideo-frame-interpolation.png)

### First Sequence Conditioning

[Download workflow](assets/ltxvideo-first-sequence-conditioning.json)
![workflow](assets/ltxvideo-first-sequence-conditioning.png)

### Last Sequence Conditioning

[Download workflow](assets/ltxvideo-last-sequence-conditioning.json)
![workflow](assets/ltxvideo-last-sequence-conditioning.png)

### Flow Edit

[Download workflow](tricks/assets/ltxvideo-flow-edit.json)
![workflow](tricks/assets/ltxvideo-flow-edit.png)

### RF Edit

[Download workflow](tricks/assets/ltxvideo-rf-edit.json)
![workflow](tricks/assets/ltxvideo-rf-edit.png)
