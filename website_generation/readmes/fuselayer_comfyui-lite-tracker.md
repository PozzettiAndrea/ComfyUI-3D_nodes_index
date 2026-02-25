# ComfyUI LiteTracker

ComfyUI custom nodes for **LiteTracker**, a fast and efficient point tracking model for videos.

This implementation wraps the original [ImFusionGmbH/lite-tracker](https://github.com/ImFusionGmbH/lite-tracker) repository as ComfyUI nodes.

## Features

- **Load Model** node: Download and load LiteTracker weights
- **Track** node: Track points across video frames with online processing
- **Grid Editor** node: Graphical interface to define multiple rotatable tracking regions with custom point density

## Installation

1. Clone this repository into your ComfyUI custom nodes directory:

```
cd ComfyUI/custom_nodes/
git clone https://github.com/fuselayer/comfyui-lite-tracker.git
pip install -r requirements.txt
```
2. Restart ComfyUI


Usage

Drag and drop this image into ComfyUI and move the video and mask files to ComfyUI/input:

![workflow](example_workflows/lite-tracker-workflow.png)




# Acknowledgements

Special thanks to the authors of CoTracker3, MFT, STIR Challenge, and SuPer Framework that made this work possible.

Please cite their work if you use LiteTracker in your research:

```
@inproceedings{karaoglu2025litetracker,
  title={LiteTracker: Leveraging Temporal Causality for Accurate Low-Latency Tissue Tracking},
  author={Karaoglu, Mert Asim and Ji, Wenbo and Abbas, Ahmed and Navab, Nassir and Busam, Benjamin and Ladikos, Alexander},
  booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention},
  pages={308--317},
  year={2025},
  organization={Springer}
}
```

Adapted from:
Original model and research: ImFusionGmbH/lite-tracker



