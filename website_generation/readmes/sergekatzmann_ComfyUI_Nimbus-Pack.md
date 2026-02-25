# ComfyUI Nimbus Pack

A collection of custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), focusing on image manipulation, resolution utilities, and video comparisons.

## Installation

1.  Navigate to your ComfyUI `custom_nodes` directory.
2.  Clone this repository:
    ```bash
    git clone https://github.com/sergekatzmann/ComfyUI_Nimbus-Pack.git
    ```
3.  Install dependencies (primarily for the video node):
    ```bash
    pip install -r requirements.txt
    ```

## Nodes Overview

### 🖼️ Image Manipulation

*   **Image Square Adapter Node**
    *   Fits an image into a target square size.
    *   **Features:** Customizable fill color, resizing filters (lanczos, nearest, etc.), supersampling, and fitting modes (center, top, bottom).
    
*   **Image Resize And Crop Node**
    *   Resizes and crops an image to exact target dimensions.
    *   **Features:** Alignment control (center, left-top, right-bottom, etc.) to choose which part of the image to keep.

*   **Auto Levels (Image)**
    *   Automatically adjusts contrast by stretching the histogram values.
    *   **Features:** Configurable black/white points (percentiles) and channel-independent mode (for color correction) vs global mode (for contrast only).

*   **Image Extract Rect**
    *   Extracts a specific rectangular region from an image based on a corner selection.
    *   **Use Case:** Useful for processing specific parts of an image (e.g., watermarks) separately.

*   **Image Combine Rect**
    *   Pastes a source image (patch) into a destination image at a specific corner.
    *   **Use Case:** Re-combining patches processed by *Image Extract Rect*.

*   **Load Images From Folder**
    *   Loads all images (.png, .jpg, .jpeg) from a specified local folder path as a batch tensor.

### 📐 Resolution & Aspect Ratios

*   **Aspect Ratio (Mobile Devices)**
    *   Provides standard resolutions for popular mobile devices (iPhone, iPad, Samsung Galaxy, etc.).
    *   **Features:** Options to swap dimensions (portrait/landscape), prescale, and upscale factors.

*   **Aspect Ratio (Popular)**
    *   Provides standard screen resolutions (Full HD, 4K, 8K, etc.).
    *   **Features:** Similar scaling and orientation options.

*   **Resolution for 2-Stage Upscale**
    *   Helper node to calculate dimensions for upscaling workflows.
    *   **Features:** aligned rounding (e.g. multiples of 8 or 16) and compression factor calculation.

### 🎥 Video

*   **Slider Comparison (Video)**
    *   Generates a video file comparing two images ("Before" and "After") with a moving slider divider.
    *   **Features:** Customizable duration, frame rate, slider color, thickness, and output height. Uses `moviepy`.

### 🧮 Math & Utilities

*   **Math Operation (Min/Max)**
    *   Performs basic integer arithmetic: `min`, `max`, `add`, `subtract`, `multiply`, `divide`.
    
*   **Number Range**
    *   Generates a list of numbers (integers and floats) given a start, end, and step.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.