# ComfyUI Roop Custom Nodes

Custom nodes for ComfyUI to enable face swapping using the Roop library.

Features

- Face swap between two images
- Optional face enhancement
- Batch image folder processing
- Face swap for videos
- Webhook sender for images (tensor) or file paths
- Auto-increment filenames to prevent overwriting

## Node Descriptions

RoopFaceSwap
- Basic face swap using source and target image tensors
- Returns a single swapped image tensor

RoopFaceSwapWithEnhancer
- Like RoopFaceSwap but also runs a face enhancer after swapping
- Useful for improving visual quality

RoopBatchFaceSwap
- Takes a source image and a folder of input images
- Applies face swap to each and saves results to an output folder
- Supports enhancement and multi-face mode

RoopFaceSwapVideo
- Swaps a face from an image into a video file
- Keeps original FPS and frames
- Saves a new video file

RoopSendWebhookImage
- Sends an image tensor to a webhook URL
- Accepts optional secret for HMAC verification
- Ideal for live image results

RoopSendWebhookFile
- Sends a file path (e.g. video or saved image) to a webhook
- Supports HMAC-secured sending
- Useful for post-processing delivery

## Requirements

- Python 3.8+
- torch
- torchvision
- Pillow (PIL)
- requests
- roop (clone from GitHub)

## Installation

1. Clone this repo into your ComfyUI custom nodes folder:

   git clone https://github.com/glitchinthemetrix16/ComfyUI-Roop

2. Install required Python packages:

   pip install torch torchvision pillow requests

3. Clone the roop repo for Google Colab Environment:

   git clone https://github.com/FurkanGozukara/roop /content/roop

4. Ensure that run.py exists in /content/roop

## Installation For Google Colab With T4 GPU (Tested and working)

```
%cd /content/

!git clone https://github.com/FurkanGozukara/roop
%cd roop

#Tested and updated 23 August 2023 commit
#!git checkout da1ef285f1d43bd0cc8b9cdb9a0f80f7ae793a97
!pip install onnxruntime-gpu && pip install -r requirements.txt
!pip install onnxruntime-gpu --upgrade
!apt-get update --yes
!apt install nvidia-cuda-toolkit --yes
!pip install opennsfw2 keras --upgrade
!pip install numpy==1.26.4
```

Usage Notes

- All temporary files are saved inside roop_dir/temp_io
- File overwrites are avoided via auto-renaming
- Video swapping works best with shorter clips due to performance
- Webhook nodes allow sending output to remote servers or APIs