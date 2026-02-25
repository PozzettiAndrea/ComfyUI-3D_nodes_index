
# ComfyUI_Camera

ComfyUI processes local real-time camera feed and provides real-time preview of the result.

# Introduction

1. Through the **ComfyUI_Camera** plugin, you can read local camera frames at any time within ComfyUI.
2. It allows for efficient previewing of the results processed by ComfyUI, making it easier to handle camera frames in real-time and view the processed results instantly.
3. All of this can be done directly within the ComfyUI interface, enabling you to operate and implement it simultaneously.

# Usage Steps

1. Install the `ComfyUI_Camera` plugin.
2. Restart ComfyUI to refresh the interface.
3. Right-click the menu and select `Start Local Camera`.
![](./res/menu.png)
4. Wait for the camera to start, then select the resolution.
![](./res/select.png)
5. Download and execute the workflow, `./res/real_time_camera_flow.json`.
![](./res/demo.png)
![](./res/demo1.png)

6. If you need real-time processing and live preview of the processed results, follow these settings and execute the **Queue Prompt** to keep it running continuously.
![](./res/auto.png)

7. If you do not have a physical camera, you can use the OBS software to enable a virtual camera for use.

8. Right-click the menu and select `Stop Local Camera` for stop camera.

# Verified
## Platforms
- Windows
- Mac

## Features
- Modify resolution does not require a restart.
- It does not support cloud deployment using a local camera; the camera and ComfyUI must be on the same machine.

