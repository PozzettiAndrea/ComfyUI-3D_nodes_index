# Kytra's MatAnyone implementation for ComfyUI

This is a ComfyUI node for [MatAnyone](https://github.com/pq-yang/MatAnyone), a state-of-the-art video matting model that can remove backgrounds from videos using just a single mask for the first frame for enhanced/guided video matting. 

## How To Use:

MatAnyone only requires that you provide the first single frame alpha mask (solid white for the subject against a solid black background for the stuff you don't want in the final output).
My example workflow uses the Rembg+ Session nodes from Comfy Essentials to automatically create the first frame alpha mask for you. The dance video example and the anime example videos below both used that method. Alternatively, you can provide the first frame alpha mask yourself and bypass those nodes. It's really that simple. Check the workflow directory in this repo for the example workflow.

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/KytraScript/ComfyUI_MatAnyone_Kytra.git
```

2. Install pip requirements
```bash
cd ComfyUI/custom_nodes/ComfyUI_MatAnyone_Kytra
pip install -r requirements.txt
```


3. The model weights are automatically downloaded during your first run from:
https://huggingface.co/Mothersuperior/ComfyUI_MatAnyone_Kytra and they will 
be placed in the ComfyUI_MatAnyone_Kytra/model folder

Outdoor Lighting dance example:

https://github.com/user-attachments/assets/bb6daad3-dccc-4201-8334-ccb2e520eb2e

Realism with low light:

https://github.com/user-attachments/assets/2ca7dcb9-d1be-4c15-82ca-d337d719f479

Anime using an AI created animation:

https://github.com/user-attachments/assets/dddde8ec-4312-43a8-9b0f-77ef00c16100

Blue car against a blue sky:

https://github.com/user-attachments/assets/8ac00e53-8ff2-496c-8119-4d10f51292aa


### Parameters

- **video_frames**: Video image batch (example workflow uses VHS Video Loader)
- **mask**: First frame mask (subject rgb(255,255,255))
- **warmup_frames**: Number of warmup iterations (default: 10)
- **erode_kernel**: Erosion kernel size (default: 10)
- **dilate_kernel**: Dilation kernel size (default: 10)
- **bg_red** & **bg_green** & **bg_blue**: Set values for background color for composite video output

## Example Workflow

- Provided in the repository 'workflow' directory

## Credits

- Original MatAnyone implementation: [https://github.com/pq-yang/MatAnyone](https://github.com/pq-yang/MatAnyone)
- Paper: [MatAnyone: Prompting Any Object for Open-world Matting](https://arxiv.org/abs/2401.05228)

## License

This project is licensed under the same license as the original MatAnyone project. 
