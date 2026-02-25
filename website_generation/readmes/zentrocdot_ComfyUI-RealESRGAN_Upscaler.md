# ComfyUI-RealESRGAN_Upscaler [![ComfyUI - Homepage](https://img.shields.io/badge/ComfyUI-Homepage-aa00ee)](https://github.com/comfyanonymous/ComfyUI) [![ComfyUI - Manager](https://img.shields.io/badge/ComfyUI-Manager-2aeeef)](https://github.com/ltdrdata/ComfyUI-Manager)

> [!IMPORTANT]  
> <p align="justify">🚧 This documentation is still under 
> construction. The development of the upscaler is a ongoing 
> activity. There might be small differenes in comparison of 
> node and documentation.</p>

> [!CAUTION]
> <p align="justify">Please note, that the node will run, only
> if an error in one Python package file is fixed. See the 
> related section for informations on this topic.</p> 

## Preface

<p align="justify">This node uses the RealESRGAN model from
xinntao [1]. This is my personal favourite upscaling model and 
upscaling approach.</p>

## Prerequisites

<p align="justify">What I am writing is valid for a computer on
which as the operating system Linux is installed.</p>

<p align="justify">To run the upscaler one needs a NVIDIA graphic
card.</p>

## Whats New

<p align="justify">Yesterday I added a bunch of things to the node.
Now the node is a little bit more complicated than before. On the 
other hand side the node considers now everything which is possible
to do with the node.</p>

## Models

<p align="justify">One needs a model for the upscaling. While installing 
the nodes some models from xinntao are downloaded and placed in the 
directory models so that one can start working with the upscaling.</p>

Following models are compatible with the node [2]:

* RealESRGAN_x4plus.pth
* RealESRNet_x4plus.pth
* RealESRGAN_x2plus.pth
* ESRGAN_SRx4_DF2KOST_official-ff704c30.pth

## Netscale

<p align="justify">One important setting depends on the model like the ones in the last
section. The x2 and the x4 denotes the scale factor. This scale factor 
must fit the value of netscale. Otherwise one will get an error message.</p> 

## Upscaling

<p align="justify">One can set the scaling factor in steps of 0.1
in the node. For the moment there is no known limit for the scaling
factor. I used for example an unrealistic scaling factor of 30.0 
for upscaling of a test image. The limiting factor is in this case 
the size of the image file.</p>

## Node Preview

<p align="justify">Figure 1 shows the node preview. Input is an image. 
Main output is the upscaled image. In addition to this one can output
the local installation with respect to the GPUs. In case of an error
the error can be printed too.</p>

<img src="./images/node_preview.png" alt="node preview" width="512">
<p><i>Figure 1: Main node preview</i></p>

## Node Parameter
The node has following parameter

+ scale_factor (FLOAT)
+ tile_number (INT)
+ tile_pad (INT)
+ pre_pad (INT)
+ fp_format (STRING)
+ denoise (FLOAT)
+ netscale (INT)
+ gpu_id (LIST)
+ model (LIST)

<p align="justify">For an upscaling one needs in a first shot the scale 
factor and a model. The other parameter can be as they are. For a 
resolution of the image of 512 x 512 pixel this is in general valid.</p> 

Over the gpu_id the user can decide, which GPU should be used for the upscaling.

Depending on the hardware one needs the tiling. In my case I needs tiling 
for a resolution of 1024 upwards.

## Model Selection

<img src="./images/model_selection.png" alt="model selection" width="512">
<p><i>Figure 2: Model selection</i></p>

## What the Node Does

The node can upscale images which have following formats

- JPG/JPEG
- PNG
- WEBP

## Workflow Preview

Figure 3 shows the example workflow preview.

<img src="./images/workflow_preview.png" alt="node preview" width="1024">
<p><i>Figure 3: Workflow preview</i></p>

Figure 4 shows the example workflow preview.

<img src="./images/workflow_error_preview.png" alt="node preview" width="1024">
<p><i>Figure 4: Workflow preview</i></p>

## Tiling

If the tiling is not set (for larger images), one will get following error:

![Bildschirmfoto vom 2025-02-09 19-26-10](https://github.com/user-attachments/assets/bebd9bc8-39a9-4a90-b2c8-6dd055a1f1e5)


<p><i>Figure 4a: Tiling problem preview</i></p>

If the tiling is wrong set, one will get following error:

![Bildschirmfoto vom 2025-02-09 19-19-43](https://github.com/user-attachments/assets/b2684003-d7ad-490b-8367-9bf433c22ce5)

<p><i>Figure 4b: Tiling problem preview</i></p>

## Installation

<p align="justify">Use the ComfyUI Manager for the installation.
Use my nick 'zentrocdot' or for 'ComfyUI_realESRGAN_Upscaler'</p>

## Known Problems

While first run I got an error message that the installation
of the node failed. After first investigation I found the 
problem. Fix for the moment is as follows. Go into directory
ComfyUI. Then search for a file.

<code>find -name "degradations.py"</code>

This looks like.

<code>./venv/lib/python3.10/site-packages/basicsr/data/degradations.py</code>

Open the file e.g.

<code>nano ./venv/lib/python3.10/site-packages/basicsr/data/degradations.py</code>

and change

<code>from torchvision.transforms.functional_tensor import rgb_to_grayscale</code>

to

<code>from torchvision.transforms.functional import rgb_to_grayscale</code>

After that, the node will work.

## Bug Fixing

In the directory scripts there is a file called <code>fix.bash</code>. This can 
be used to fix the bug in the Python package. The only one prerequiste for this
script is that ComfyUI is installed in a Python virtual envirnoment.

## Error Screen

While working on the node I have also provoked errors for testing purposes. 
When the number of netscale is not matching the value of the model's
netscale one got an error. 

![Bildschirmfoto vom 2025-02-09 08-57-01](https://github.com/user-attachments/assets/03771469-3a59-4115-baba-a362b60d20fb)

<p><i>Figure 5: Error message preview</i></p>

<p align="justify">The error led to unexpected behaviour of the node.
This was the reason to rethink the programming. Now I catch the error
Over the output ERROR one can make such an error visible. To prevent 
misleading results the output is an empty image with text.</p> 

## Limitations

Limitation at the moment not known.

## To-Do

<p align="justify">There are a plenty of things to to</p>

## Example Using Converted Models

<p align="justify">Figure 6 and Figure 7 show two examples where
I used two converted models for the upscaling. it depends on your
personal taste which upscaler you like.</p> 

![ultrasharp](https://github.com/user-attachments/assets/60d7e2ff-53d4-48b8-96a8-5f42fcf01868)

<p><i>Figure 6: Upscaling using 4x-UltraSharp.pth</i></p>

![nomos](https://github.com/user-attachments/assets/1d0305f3-d8e9-4e75-98f0-3fbe593d18b6)

<p><i>Figure 7: Upscaling using 4xNomos8kSC.pth</i></p>

## Credits

<p align="justify">Special credits goes to xinntao (Xintao Wang) for his excellent 
work on ESRGAN and RealESRGAN models The results achieved are quite impressive.</p> 

## Final Words

Have fun. Be inspired!

# Reference

[1] https://github.com/xinntao/Real-ESRGAN

[2] https://github.com/xinntao/Real-ESRGAN/blob/master/docs/model_zoo.md

[3] https://arxiv.org/abs/2107.10833

[4] https://github.com/zentrocdot/ESRGAN_RRBD_CONVERTER

[5] https://github.com/ltdrdata/ComfyUI-Manager

[6] https://openmodeldb.info/
