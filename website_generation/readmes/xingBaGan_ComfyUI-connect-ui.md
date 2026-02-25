How to use it:

plase use it with the https://github.com/xingBaGan/comfy-workflow-ui

## Installation:

Clone this repo into custom_nodes folder.
Install dependencies: pip install -r requirements.txt or if you use the portable install, run this in ComfyUI_windows_portable -folder:
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-connect-ui\requirements.txt

## WebSocket Image Communication Nodes:
SaveImageByWebsocket: A node that can send processed images through WebSocket connection
reciveImageByWebsocket: A node that can receive images through WebSocket connection

![](https://picgo-1300491698.cos.ap-nanjing.myqcloud.com/20250310211100394.png)

## Key Features:
Real-time image transfer between client and server
Base64 image encoding/decoding support
Supports PNG image format
Includes a floating preview window for received images
Preview window has minimize/maximize functionality

## UI Features:
Floating preview window positioned at bottom-right corner
Toggle button to minimize/maximize the preview
Preview window shows received images at 250px width
Responsive image scaling with aspect ratio preservation

## Technical Implementation:
Uses WebSocket for real-time bidirectional communication
Handles image data in ComfyUI's tensor format




