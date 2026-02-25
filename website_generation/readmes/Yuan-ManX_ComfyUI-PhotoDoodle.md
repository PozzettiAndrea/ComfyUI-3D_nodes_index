# ComfyUI-PhotoDoodle

Make [PhotoDoodle](https://github.com/showlab/PhotoDoodle) avialbe in ComfyUI.

[PhotoDoodle](https://arxiv.org/abs/2502.14397): Learning Artistic Image Editing from Few-Shot Pairwise Data.

## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-PhotoDoodle.git
```

3. Install dependencies:
```
cd ComfyUI-PhotoDoodle
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124
pip install --upgrade -r requirements.txt
```
