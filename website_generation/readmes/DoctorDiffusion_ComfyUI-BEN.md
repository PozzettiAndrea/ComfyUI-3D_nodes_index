# ComfyUI BEN - Background Erase Network

****


Remove backgrounds from images with [BEN](https://huggingface.co/PramaLLC/BEN) in [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## Installation

```
git clone https://github.com/DoctorDiffusion/ComfyUI-BEN.git
```
```
cd ComfyUI-BEN
```
```
pip install -r requirements.txt
```
Go to the [BEN huggingface page](https://huggingface.co/PramaLLC/BEN/tree/main) and download `BEN_Base.pth`, and `model.py` and place them inside:
```
...ComfyUI/custom-nodes/ComfyUI-BEN/
```
The folder should look like this:
```
└── ComfyUI/custom-nodes/ComfyUI-BEN/
    ├── __init__.py
    ├── background_erase_network.py
    ├── ben.png
    ├── BEN_Base.pth
    ├── model.py
    ├── README.md
    └── requirements.txt
```
## Nodes

### Background Erase Network

Outputs image of subject with alpha layer, combine with Image to Mask Node to get alpha mask as well.

![ben](https://github.com/user-attachments/assets/54497cc7-e1c2-4955-8735-06da93dad969)

## Credits

- [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)

- [PramaLLC/BEN](https://huggingface.co/PramaLLC/BEN)

⭐ If you like the project, please give it a star! ⭐

## License
Apache 2.0 License

### OUTPUTS CLEAR FOR COMMERCIAL USE
[PramaLLC](https://www.reddit.com/r/comfyui/comments/1gq8nx0/comment/m2733hy/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) - "You can use our BEN model commercially without any problem. Its under the Apache 2.0 license. The only commercial piece is the BEN+Refiner but the BEN_BASE is perfectly fine for commercial use. :)"
