# ComfyUI Anime Segmentation Nodes v1.1.0

This is a set of custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that provide anime-style image segmentation using efficient pre-trained models. It includes:

- ✅ `SimpleAnimeSeg` — fast ONNX-based segmentation using SkyTNT's model.
- ✅ `AdvancedAnimeSeg` — instance-based character segmentation with converted versions of the CartoonSegmentation models provided by dreMaz.

As of now, this entire node pack is CPU-oriented. GPU support may be added in later versions.

> ⚠️ These nodes are not perfect. Anime character segmentation is still a tricky problem. While decent, results may vary depending on character appearance and background complexity.

---

## Features

### ✅ SimpleAnimeSeg

This provides quick segmentation and is often sufficient when there's a clear difference between the character and background. However, it can struggle when the character's clothes or skin match background elements closely. In such cases, using the advanced node is recommended.

The node is based on the gist [SimpleAnimeSeg.py](https://gist.github.com/city96/103c394ef9cf9300aca67d1c2a2d28b5) by GitHub user [**city96**](https://github.com/city96), and the ONNX model from the [anime-segmentation](https://github.com/SkyTNT/anime-segmentation) project by **SkyTNT**.

- Fast CPU-friendly segmentation
- Uses ONNX model `isnetis.onnx`
- Lightweight and easy to integrate

![Simple segmentation example](images/Simple%20segmentation%20example.png)
![Simple segmentation problems](images/Simple%20Segmentation%20problems.png)

---

### ✅ AdvancedAnimeSeg

A more robust segmentation node based on the [CartoonSegmentation](https://github.com/CartoonSegmentation/CartoonSegmentation) project. This version provides options such as threshold adjustment to refine results.

It uses the original model weights from [dreMaz/AnimeInstanceSegmentation](https://huggingface.co/dreMaz/AnimeInstanceSegmentation), but relies on ONNX-converted versions found [here](https://huggingface.co/Faor-Mati/anime-character-segmentation/tree/main).

> While more customizable, this node can still fail in specific edge cases where the simpler model performs better. It's called "advanced" due to its flexibility and multi-stage approach — not guaranteed accuracy.

- Combines RTMDet-based detection with ISNet-based mask refinement
- Pure PyTorch (no mmcv/mmdet dependencies)
- Cleaner masks, great for downstream editing (e.g., outfits)
- Threshold option for finer control

![Advanced segmentation example](images/advanced%20segmentation.png)

---

## Installation

1. Clone or download this repository.
2. Move the folder `comfyui_animeseg` into your ComfyUI `custom_nodes` directory.
3. Download the model files:

   - [`isnetis.onnx`](https://huggingface.co/skytnt/anime-seg/resolve/main/isnetis.onnx) — used by SimpleAnimeSeg
   - [`ranime_segmentor_rtmdet_e60_simplified.onnx`](https://huggingface.co/Faor-Mati/anime-character-segmentation/resolve/main/anime_segmentor_rtmdet_e60_simplified.onnx) — advanced node detector
   - [`mask_refiner_isnetdis_refine_last_simplified.onnx`](https://huggingface.co/Faor-Mati/anime-character-segmentation/resolve/main/mask_refiner_isnetdis_refine_last_simplified.onnx) — advanced node refiner

4. Place all model files in `comfyui_animeseg/models` (create the folder if it doesn't exist).
5. In your ComfyUI environment, install the requirements:

```bash
pip install torch torchvision onnxruntime pillow numpy
```

Or use the provided `requirements.txt`.

---

## Requirements

```txt
torch
torchvision
onnxruntime
pillow
numpy
```

---

## Future Plans

- 🚧 Merge both nodes to generate higher quality composite masks
- 🧠 Train a part-based segmenter for individual character parts (legs, arms, hair, clothing, etc)
- ♻️ Refactor node structure for more flexibility (may break backward compatibility)

These plans are exploratory. No timeline is guaranteed.

---

## Credits

- [SkyTNT](https://github.com/SkyTNT) — ONNX segmentation model
- [city96](https://github.com/city96) — original segmentation node gist
- [dreMaz](https://github.com/dmMaze) and [ljsabc](https://github.com/ljsabc) — advanced node model providers
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) — node framework

---

Happy generations! 🎨✨
