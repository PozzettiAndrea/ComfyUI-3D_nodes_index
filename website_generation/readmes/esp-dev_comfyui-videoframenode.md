# comfyui-videoframenode (ComfyUI)

![VideoFrameNode icon](./icon-256.png)

Custom node for ComfyUI that loads an `.mp4` video and outputs two images:

- first frame
- last frame

## What this node does

- Reads a video file from `ComfyUI/input` (by filename) or from an absolute path.
- Optionally accepts a **wired video input** from another node (`video_in`).
- Outputs two `IMAGE` values: `FIRST_FRAME` and `LAST_FRAME`.
- Supports choosing the video from a **recent files list** or via **file picker upload** (UI feature).
- Supports drag & drop of an `.mp4` directly onto the node (UI feature).

## How to use

1. Add the node **Video: First & Last Frame** to your graph.
2. Provide the input video using one of these methods:
    - Connect `video_in` from another node (if it outputs a path/filename, a dict with a path, or an IMAGE batch of frames).
    - Set `video` to a filename from `ComfyUI/input`.
    - Set `video` to an absolute path to an `.mp4` file.
    - (UI) Use the `recent` dropdown or `Browse…` to pick an `.mp4` from your computer (it uploads into `ComfyUI/input`).
            The `recent` list can include entries like `input/your.mp4` and `output/your.mp4`.
    - (UI) Drag & drop an `.mp4` onto the node. It will upload into `ComfyUI/input` and set `video` automatically.
3. Execute the graph.
4. Use outputs `FIRST_FRAME` and `LAST_FRAME` (both are ComfyUI `IMAGE`).

### Notes (API mode)

- The core node works in API mode, but drag & drop is UI-only (it adds an upload route + frontend JS).

## Install via ComfyUI-Manager (recommended)

1. In the ComfyUI, open **Manager**.
2. Install this node from the list (search by repo name) or paste the repo URL.
3. Restart ComfyUI after installation.

## Manual install (advanced users)

The recommended way to install is via ComfyUI-Manager. Manual install is best treated as a fallback.

1. Copy/clone this repo into `ComfyUI/custom_nodes/`, for example:

    - `ComfyUI/custom_nodes/comfyui-videoframenode` (this repo root is the node folder)

2. Run commands inside the same Python environment that ComfyUI uses (usually ComfyUI's venv):

    Windows (PowerShell):

    - Activate venv (example): `& "D:\\ComfyUI\\.venv\\Scripts\\Activate.ps1"`

        Note: Windows often blocks running `.ps1` scripts by default.

        - Option A (temporary for this shell only): `Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process -Force`
            (This applies only to the current PowerShell process; closing the terminal reverts it.)
        - Option B: use the `.bat` activator instead (works well from CMD): `"D:\\ComfyUI\\.venv\\Scripts\\activate.bat"`

    - Check what's already installed (recommended before installing anything):
        - `python -m pip show opencv-python imageio`
        - `python -c "import cv2, imageio; print('cv2', cv2.__version__, 'imageio', imageio.__version__)"`
        - (optional) `python -m pip list | findstr /i "opencv imageio torch"`

    - Install deps: `pip install -r requirements.txt`

    Note about `torch` / Pylance

    - This node uses `torch` because ComfyUI images are `torch.Tensor`.
    - `torch` is usually already included with ComfyUI, so you typically don't need to install it separately.
    - ComfyUI commonly uses a CUDA-specific build (for example `torch-cu130`). Installing the plain `torch` package via `pip` can override the working CUDA build and break GPU acceleration.
    - For that reason, `torch` is intentionally commented out in `requirements.txt` in this repo.
    - If Pylance shows `Import "torch" could not be resolved`, make sure VS Code is using the same environment (venv) as ComfyUI.

3. Restart ComfyUI.
