# Steganos Node for ComfyUI

This custom node for ComfyUI allows you to hide a video file within a PNG image using a file concatenation technique. The resulting image can be viewed as a normal picture, but a standard unzip tool can extract the hidden video from it.

## Features

- Encodes an image sequence into an MP4 video.
- Uses a static carrier image (`test.png`) as the "cover".
- Zips the MP4 video and appends it to the carrier image.
- The final output is a valid PNG file that also contains the hidden video.
- No special decoding tools required; any standard unzip utility will work.

## Installation

1.  Navigate to the `ComfyUI/custom_nodes/` directory.
2.  Clone this repository or simply place the `steganos` folder inside `custom_nodes`.
3.  Ensure the `steganos` folder contains:
    - `__init__.py`
    - `nodes.py`
    - `test.png` (You can replace this with your own cover image, but keep the filename the same).
4.  Restart ComfyUI.

## Usage

1.  In the ComfyUI menu, go to `Add Node` -> `Steganos` -> `Steganos Video Encoder`.
2.  Connect an image sequence (e.g., from a VAE Decode or a Load Image sequence) to the `images` input.
3.  Adjust the `fps` (frames per second) for the output video.
4.  Set a `filename_prefix` for the output file.
5.  Queue the prompt. The final PNG file containing the hidden video will be saved in your ComfyUI output directory.
6.  The node will also output the `test.png` carrier image, which you can then connect to other nodes like "Save Image" or "Preview Image".

## How to Extract the Hidden Video

1.  Locate the output PNG file.
2.  Use any standard archive utility (like 7-Zip, WinRAR, or the `unzip` command in Linux/macOS) to open or extract the contents of the PNG file.
3.  The utility will find the appended ZIP archive and extract the `secret.mp4` video file from it.