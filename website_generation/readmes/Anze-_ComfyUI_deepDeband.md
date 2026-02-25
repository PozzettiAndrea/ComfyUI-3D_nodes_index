# ComfyUI_deepDeband

ComyUI wrapper for RaymondLZhou/deepDeband image and video debanding

![image](https://github.com/user-attachments/assets/61f17843-85f8-44d8-af16-ae3748eeb40c)


<hr>

**WARNING**  : this is an experimental development repo, you have to expect bugs, not recommended for a production environment.

<hr>

## Install
Please run `pip install -r requirements.txt` in the environment where ComfyUI will be running, at the moment some depencies are not automatically installed.

Currently the deepDeband repository is over its data quota. Account responsible for LFS bandwidth should purchase more data packs to restore access but we cannot do anything about it. You can check the current status with `git lfs pull`.  We recommend to **manually download** the model checkpoints manually as stated in the original [README](https://github.com/RaymondLZhou/deepDeband/blob/master/README.md#model) from this file archive [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7523437.svg)](https://doi.org/10.5281/zenodo.7523437)

After downloading and extracting the zip file, place the checkpoint found in ` deepDeband-f ` into 

```
ComfyUI/custom_nodes/ComfyUP_deepDeband/deepDeband/pytorch-CycleGAN-and-pix2pix/checkpoints/deepDeband-f 
```




## Notes
* ~~When the repo is downloaded the model are automatically downloaded via GIT LFS~~: see 'install' above

* The whole node with model weights should require ~ 300 MB of storage.

* The official implementation of deepDeband uses the function ` .deepDeband.deband.deband_images(...) ` which pipes all images through disk read/write and inferences images one by one in a python for loop. These inefficiencies sum up to a slow video/batch processing, therefore the new script deepDeband_batch.py (which calls deepDeband_full_batch.py) was implemented to run the CycleGAN inference sequentially. The script still allows for more straightforward efficiency improvements not currently implemented (torchvision padding, dataloader, avoid read/write).

* the model was trained to perform light debanding tasks where the source of banding isn't too aggressive, it works best on video encodings and the performance for .gif debanding isn't outstanding, but currently this is the best known option for ComfyUI.

* other more classical debanding techniques could be implemented for ComfyUI, one by wrapping [neo_f3kdb](https://silentaperture.gitlab.io/mdbook-guide/filtering/debanding.html#neo_f3kdb), [[...]](https://github.com/vapoursynth/vapoursynth)

# Acknowledgements

All credits for the ComfyUI platform, model development, model framework, go to:
- [deepDeband](https://github.com/RaymondLZhou/deepDeband)
- [CylceGan and Pix2Pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
- [ComfyUI](https://github.com/comfyui)
- [pytorch](https://github.com/pytorch/pytorch)

all respective licence terms are located in the relative subfolders.
