# ComfyUI Street View Loader Node

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Version: v1.0.4](https://img.shields.io/badge/Version-v1.0.4-green.svg)](https://github.com/ru4ls/ComfyUI_StreetView-Loader)

A custom node for ComfyUI that allows you to load images directly from Google Street View to use as backgrounds, textures, or inputs in your workflows. Version 1.01 adds animation capabilities, v1.0.2 adds cubemap generation, v1.0.3 adds historical date support, and v1.0.4 adds equirectangular panorama generation!

Instead of manually taking screenshots, this node programmatically fetches a clean, high-resolution image from any location on Earth with Street View coverage, giving you precise control over the camera angle, direction, and field of view.

![Street View Loader Node](https://github.com/ru4ls/ru4ls-public-media/blob/main/comfyui-streetview-loader/images/preview.png)

---

## Why Use This Node? The Power of "Ground Truth"

While standard text-to-image models are incredible at *imagining* locations ("a charming street in Paris"), they struggle to recreate the **exact appearance and layout** of a specific, real-world place. Their output is an approximation, an artistic blend of countless images.

This node solves that problem by providing **photographic ground truth**. It pulls the real, pixel-for-pixel view of a location, ensuring your generations are anchored in reality.

This gives you the best of both worlds: the authenticity of a real photograph combined with the creative power of AI.

### Key Advantages & Use Cases

*   **Guaranteed Location Accuracy:** When you need the background to be recognizably *your* street, a specific landmark, or a favorite travel spot, this node is the only way to guarantee a 100% accurate representation.
*   **The Ultimate Base for ControlNet:** Feed the real Street View image into your workflow as a base for stylization (anime, oil painting), re-imagining (futuristic, historical), or precise inpainting.
*   **Virtual Location Scouting:** Instantly scout real-world locations from your desktop and experiment with different styles and moods for your project.
*   **Personalized & Sentimental Art:** Create unique art based on a place with personal meaning—a childhood home, a proposal spot, or a favorite vacation view.
*   **Consistent Backgrounds for Testing:** Use a consistent, real-world background to reliably test LoRAs, IPAdapters, or character models.
*   **Animation Capabilities:** Create smooth camera movements and parameter transitions with the new Street View Animator node (v1.0.1).

*example using nano-banana to re-context the output image

![Street View Loader Node combine with NanoBanana in ComfyUI](https://github.com/ru4ls/ru4ls-public-media/blob/main/comfyui-streetview-loader/images/preview_2.png)

*example using the output as a set of input for first and last frame video diffusion workflow to create a walk-through video

https://github.com/user-attachments/assets/63f26d92-4ef3-4403-b5cf-82189c61ffec

## Features
- **Direct API Integration:** Pulls images directly from the Google Street View Static API.
- **Easy Workflow with URL Parser:** Just find a spot on Google Maps and paste the URL.
- **Secure API Key Storage:** Uses a `.env` file to keep your API key safe and out of your workflow files.
-   **Simple Aspect Ratio Presets:** Choose from common ratios like 16:9 or 1:1 without manual calculations.
- **Clean Output:** No UI overlays, just the pure image.
- **Panorama Mode:** Stitch multiple images together to create ultra-wide cinematic landscapes.
- **(New in v1.0.1) Animation Mode:** Animate camera parameters over time to create smooth transitions and camera movements.
- **(New in v1.0.2) Cubemap Mode:** Generate 3D environment maps with six images representing all directions (front, back, left, right, up, down) for use in 3D applications and game engines.
- **(New in v1.0.3) Historical Date Support:** Load images from specific historical dates using panorama IDs. All loader nodes now support historical image retrieval by providing a historical date ID.
- **(New in v1.0.4) Equirectangular Mode:** Generate 360°x180° panoramic images from six cube faces for VR applications, environment mapping, and immersive experiences with optional upscaling for enhanced quality.

---

## 1. Installation

1.  Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```

2.  Clone this repository:
    ```bash
    git clone https://github.com/ru4ls/ComfyUI_StreetView-Loader.git
    ```

3.  Install the required Python dependencies. Open a terminal, navigate to the new `ComfyUI_StreetView-Loader` folder, and run:
    ```bash
    pip install -r requirements.txt
    ```
    *(This will install the `requests` and `python-dotenv` libraries required for the node to function.)*

4.  **Restart ComfyUI.**

---

## 2. Setup: Getting Your Google API Key (Crucial Step)

This node requires a Google Cloud API key to function. Google provides a generous **$200/month free credit**, which is more than enough for extensive personal use without any charge.

### Step-by-Step Guide

1.  **Create Project & Enable API**: Go to the [Google Cloud Console](https://console.cloud.google.com).
2.  Create a **New Project**. Give it a name like `ComfyUI-API`.
3.  In the new project, search for "API Library".
4.  In the library, search for and **Enable** the **"Street View Static API"**.

5.  **Set Up Billing**: You will be prompted to link a billing account. This is required, but you will **not be charged** unless you exceed the $200 free monthly credit.

6.  **Create and Secure Your API Key**: In the Cloud Console search bar, navigate to **"Credentials"**.
7.  Click **"+ Create Credentials"** and select **"API key"**.
8.  **Copy this key immediately.**
9.  **(IMPORTANT!)** Click **"Edit API key"**. Under "API restrictions," select **"Restrict key"** and add **"Street View Static API"** to the list. This protects your account. Click **"Save"**.

10. **Configure the Node**: In your `ComfyUI/custom_nodes/ComfyUI_StreetView-Loader/` folder, create a new file named `.env` (or rename the existing `.env.example` file).
11. Open this `.env` file and add your copied API key in the following format:
    ```
    GOOGLE_STREET_VIEW_API_KEY="your_actual_api_key_goes_here"
    ```
12. Save the file. Your setup is now complete!

---

## 3. How to Use & Workflow

The recommended workflow is to use the **URL Parser** node to feed information into the other nodes.

1.  **Find your view** in [Google Maps](https://maps.google.com) and enter Street View.
2.  Frame the perfect shot, then **copy the entire URL** from your browser's address bar.
3.  In ComfyUI, add the **`Street View URL Parser`** node and paste the URL into it.
4.  Add one of the loader nodes.
5.  Connect the outputs of the Parser to the inputs of the loader (`location` to `location`, etc.).

---

### Node Descriptions

## Street View URL Parser

This node takes a full Google Maps URL as input and outputs the camera parameters (`location`, `heading`, `pitch`, `fov`, `historical_date_id`).

The `historical_date_id` parameter represents the panorama ID that can be used to access historical Street View imagery from specific dates in the past.

## Street View Loader
This is the main node that fetches the image.
-   **`aspect_ratio`**: Choose your desired output aspect ratio from the dropdown. This replaces manual width/height inputs.
-   **API Limit & Upscaling:** The Google Street View API has a maximum output size of **640x640 pixels**. For high-resolution images (like 1080p or 4K), you **must** use an upscaling workflow.
-   **Recommended HD Workflow:**
    1.  Select `"16:9 Widescreen (640x360)"` in the `Street View Loader`.
    2.  Connect its `IMAGE` output to an **`Upscale Image (using model)`** node.
    3.  Use a `Load Upscale Model` node (e.g., `4x-UltraSharp`) to get a final, high-quality **2560x1440** image.
-   **Historical Date Support (v1.0.3):** Provides an optional `historical_date_id` input parameter. When provided, this parameter overrides the location and fetches a historical image from the specified date, allowing you to access Street View imagery from previous years. To obtain a historical date ID, use the Street View URL Parser (see below) or extract it from a Google Maps URL.

## Street View Pano Loader

For users who need to create wide, cinematic landscapes, the project includes the **Street View Pano Loader** node.

This node overcomes the API's FOV limitations by using a sophisticated stitching algorithm. It fetches multiple overlapping image "tiles" and then uses the OpenCV library to analyze, warp, and seamlessly blend them into a single, perspective-corrected panoramic image.

![Street View Pano Loader Node in ComfyUI](https://github.com/ru4ls/ru4ls-public-media/blob/main/comfyui-streetview-loader/images/preview_3-new.png)

![Street View Pano Loader Node result](https://github.com/ru4ls/ru4ls-public-media/blob/main/comfyui-streetview-loader/images/StreetView_Pano_00010_.png)

### How to Use & Parameter Suggestions

1.  Add the **"Street View Pano Loader"** node to your canvas.
2.  Provide a `location` and `center_heading` (the direction you want the middle of your panorama to face).
3.  Fine-tune the parameters for a successful stitch:
    -   **`overlap_percentage`**: This is the most critical setting. For OpenCV to work, it needs to see the same features in adjacent images. An overlap of **30-50%** is a great starting point. **If a stitch fails, increase this value first.**
    -   **`fov_per_image`**: A narrower Field of View (like 70-80) can reduce distortion at the edges of each tile, making it easier for the algorithm to find matching points. However, you may need to increase the `num_images` to capture the same total width.
    -   **`num_images`**: Controls the final width of your panorama. Start with 3 and increase if needed.

### Understanding the Output: Warping & Black Borders

A successful, high-quality stitch will **not** be a perfect rectangle. To correctly align the perspectives, the stitcher "warps" the flat photos onto a virtual cylinder.

**The curved edges and black borders are not an error; they are proof that the perspective correction worked!** This warped image is now a seamless, geometrically correct panorama, ready for refinement.

### Refining Your Panorama: Optional Next Steps

Once you have your stitched result, you have two great options to create a final, rectangular image:

**1. Cropping (The Simple Method)**
-   **Goal:** To get a clean, cinematic widescreen image.
-   **How:** Connect the `IMAGE` output from the Pano Loader to a `Crop` node in ComfyUI. Adjust the crop box to frame the best part of the scene and remove the black areas.

**2. AI Outpainting (The Advanced Method)**
-   **Goal:** To use AI to intelligently fill in the missing areas, creating a larger, natural-looking scene.
-   **How:** Feed the panoramic image into your main workflow (`VAE Encode`, `KSampler`, etc.) with a descriptive prompt of the scene and a **low denoise** (e.g., 0.3-0.5). The AI will use the existing pixels as a guide to generate new details in the black corners.

## Street View Animator (v1.0.1)

Version 1.0.1 introduces the **Street View Animator** node, which allows you to create animated sequences by smoothly transitioning camera parameters over time.

This node enables you to create dynamic camera movements like slow rotations, pitch changes, or field-of-view adjustments that can be used as input for video generation workflows or simply to create smooth transitions between different viewpoints of the same location.

![Street View Animator Node in ComfyUI](https://github.com/ru4ls/ru4ls-public-media/blob/main/comfyui-streetview-loader/images/StreetView_Animate.png)


https://github.com/user-attachments/assets/7edbbdf8-2dcd-4e0c-aae0-ccc5ad1be679


### How to Use & Parameter Suggestions

1.  Add the **"Street View Animator"** node to your canvas.
2.  Provide a `location` (same as other nodes).
3.  Set your animation parameters:
    -   **Start/End Values:** Define the beginning and ending values for `heading`, `pitch`, and `fov` parameters.
    -   **Duration & FPS:** Control the total animation length and frame rate (frames per second).
    -   **Interpolation:** Choose from different transition types (linear, ease-in, ease-out, ease-in-out) for smooth camera movements.
    -   **aspect_ratio:** Select your desired output aspect ratio.

4.  The node will generate a sequence of images as a stacked tensor output, which can be used for:
    -   Video generation workflows
    -   Frame-by-frame processing
    -   Creating dynamic backgrounds for animations

### Key Animation Parameters

-   **Start/End Heading:** Control camera rotation from start to end values (0-360 degrees)
-   **Start/End Pitch:** Adjust camera tilt from start to end values (-90 to 90 degrees) 
-   **Start/End FOV:** Change field of view from start to end values (10-120 degrees)
-   **Duration:** Total animation time in seconds
-   **FPS:** Frames per second - determines smoothness and total frame count
-   **Interpolation:** Defines how values transition between start and end points

### Animation Tips

-   **Smooth Rotations:** For a full 360° rotation, set start_heading=0 and end_heading=360
-   **Camera Dolly:** Keep heading constant but change fov for zoom effects
-   **Tilt Effects:** Combine pitch changes with heading changes for dynamic camera movements
-   **Frame Count:** Total frames = duration × fps (higher values = smoother but may increase API usage costs)

## Street View Cubemap Loader (v1.0.2)

Version 1.02 introduces the **Street View Cubemap Loader** node, which enables the generation of 3D environment maps from Street View locations. This node fetches six images at specific orientations to create a complete cubemap suitable for 3D applications and environment mapping in game engines or rendering software.

![Street View Cubemap Loader Node in ComfyUI](https://github.com/ru4ls/ru4ls-public-media/blob/main/comfyui-streetview-loader/images/Streetview_cubemap_cross.png)

![Street View Cubemap Merged Hstrip Loader Node in ComfyUI](https://github.com/ru4ls/ru4ls-public-media/blob/main/comfyui-streetview-loader/images/Streetview_cubemap_hstrip.png)

![Street View Cubemap Merged Hstrip Loader Node in ComfyUI](https://github.com/ru4ls/ru4ls-public-media/blob/main/comfyui-streetview-loader/images/Streetview_cubemap_vstrip.png)

https://github.com/user-attachments/assets/8f9b3771-ee5d-449a-97fe-b884d33b950b


### How to Use & Parameter Suggestions

1.  Add the **"Street View Cubemap Loader"** node to your canvas.
2.  Provide a `location` (same as other nodes) for the center point of your environment map.
3.  Adjust the parameters as needed:
    -   **`face_resolution`**: Select the resolution for each of the 6 cubemap faces. Options include 256x256, 512x512, 640x640, and 1024x1024. Higher resolutions provide better quality but require more API requests and resources.
    -   **`output_mode`**: Choose how to output the cubemap faces:
        - **individual_faces**: Outputs six separate image tensors (front, back, left, right, up, down)
        - **merged_cross**: Combines all faces into a single cross-shaped layout texture
        - **merged_hstrip**: Combines all faces into a horizontal strip layout
        - **merged_vstrip**: Combines all faces into a vertical strip layout


4.  The node will generate outputs based on the selected output mode:
    -   **Individual faces** (when selected): Six separate image outputs representing the six faces of the cube map:
        -   **Front**: The view facing forward from the location (0° heading, 0° pitch)
        -   **Back**: The view facing backward from the location (180° heading, 0° pitch)
        -   **Left**: The view facing left from the location (270° heading, 0° pitch)
        -   **Right**: The view facing right from the location (90° heading, 0° pitch)
        -   **Up**: The view looking upward from the location (0° heading, 85° pitch) - note slightly less than 90° to work with API limitations
        -   **Down**: The view looking downward from the location (0° heading, -85° pitch) - note slightly less than -90° to work with API limitations
    -   **Merged texture** (when selected): A single image tensor containing all six faces arranged according to the selected layout

### Use Cases for Cubemap Output

- **3D Environment Mapping**: Use the cubemap output as an environment map for 3D scenes in Blender, Unity, or Unreal Engine
- **Background Texturing**: Create realistic backgrounds for 3D scenes with accurate real-world lighting information
- **VR Applications**: Generate real-world environments for virtual reality experiences
- **Reflection Probes**: Use in rendering pipelines for accurate reflections and lighting calculations
- **Easy 3D Integration**: The merged output modes make it simple to use cubemaps directly in 3D engines without manual texture assembly

### Important Notes

- **API Usage**: This node makes six API calls (one for each face of the cube). Each cubemap generation will count as **6 requests** against your free monthly Google Cloud credit.
- **API Limitations**: The Street View API might not return valid images for extreme pitch angles. The node uses 85° and -85° for the up and down faces to avoid common API limitations at exactly 90° vertical pitch.
- **Resolution Constraints**: Each face will be limited by the Street View API's maximum output size of 640x640 pixels. For higher resolutions, you'll need to upscale the results using ComfyUI's upscaling nodes after generation.
- **Memory Considerations**: The merged output modes will create larger textures (e.g., cross layout is 4x width by 3x height of individual faces) so consider your system's memory limitations when choosing high resolutions.

## Street View Equirectangular Loader (v1.0.4)

Version 1.0.4 introduces the **Street View Equirectangular Loader** node, which creates full 360°x180° panoramic images by combining six individual Street View captures (front, back, left, right, top, bottom) into a single equirectangular projection. This format is ideal for VR applications, environment mapping, and immersive experiences.

<img width="1803" height="532" alt="Screenshot 2026-01-11 153535" src="https://github.com/user-attachments/assets/56cd8242-55cf-4be6-a5ad-c5b34eff832d" />

### How to Use & Parameter Suggestions

1.  Add the **"Street View Equirectangular Loader"** node to your canvas.
2.  Provide a `location` (same as other nodes) for the center point of your panoramic capture.
3.  Adjust the parameters as needed:
    -   **`face_resolution`**: Select the resolution for each of the 6 source cubemap faces. Options include 256x256, 512x512, and 640x640. Higher resolutions provide better quality but require more API requests and resources.
    -   **`upscale_factor`**: Choose a factor (1-4) to upscale the source images before equirectangular conversion. This significantly improves output quality by working with higher-resolution source material. Factor 2x will double the resolution of each face (e.g., from 640x640 to 1280x1280).
    -   **`upscale_method`**: Select the resampling algorithm for upscaling. Options are "LANCZOS" (highest quality, slower), "BICUBIC" (good quality, medium speed), "BILINEAR" (medium quality, faster), or "NEAREST" (lower quality, fastest). LANCZOS is recommended for best results.
    -   **`interpolation_mode`**: Select the interpolation method for pixel sampling during the equirectangular conversion. Options are "BILINEAR" (smoother) or "NEAREST" (sharper but potentially more aliased).

4.  The node will generate multiple outputs:
    -   **`equirectangular_image`**: The main output - a single 360°x180° panoramic image in equirectangular projection
    -   **`front`, `back`, `left`, `right`, `top`, `bottom`**: Individual cube face images after any necessary transformations and upscaling
    -   **`metadata`**: Information about the generation process, including successful fetches and API usage

### Use Cases for Equirectangular Output

- **VR Applications:** Create immersive virtual reality environments from real-world locations
- **360° Panoramic Views:** Generate full spherical panoramas for virtual tours or real estate
- **Environment Mapping:** Use as environment maps for 3D rendering and lighting calculations
- **Immersive Experiences:** Integrate into VR/AR applications or 360° video projects
- **Architectural Visualization:** Capture and present real-world spaces in spherical format
- **Game Development:** Create authentic environment maps for game engines

### Technical Details

- **Conversion Process:** The node fetches six individual Street View images at specific orientations (every 90°) and mathematically converts them to equirectangular projection
- **Face Orientations:**
  - Front: 0° heading, 0° pitch
  - Back: 180° heading, 0° pitch
  - Left: 270° heading, 0° pitch
  - Right: 90° heading, 0° pitch
  - Top: 0° heading, 90° pitch
  - Bottom: 0° heading, -90° pitch
- **Quality Enhancement:** The upscale factor allows working with higher-resolution source images to minimize quality loss during the geometric transformation
- **Optimized Conversion:** Uses vectorized numpy operations for efficient equirectangular projection conversion

### Important Notes

- **API Usage:** This node makes six API calls (one for each face of the cube). Each equirectangular generation will count as **6 requests** against your free monthly Google Cloud credit.
- **Processing Time:** The equirectangular conversion involves complex mathematical transformations and may take longer than other nodes, especially with higher resolution and upscale factors.
- **Memory Considerations:** Higher resolution faces and upscale factors will require more memory during processing.
- **Historical Support:** Like other nodes, this supports the optional `historical_date_id` parameter to generate equirectangular panoramas from historical Street View captures.

### Important Notes for All Nodes

-   **API Usage:** All nodes make API requests against your Google Cloud monthly credit.
-   **API Limitations:** The Street View API may not have coverage for all locations or may return black images for extreme angles or unavailable locations.
-   **Resolution Constraints:** The maximum resolution from the API is 640x640 pixels per image. For higher-resolution results, use ComfyUI's upscaling nodes.

## New Feature: Historical Date Support (v1.0.3)

Version 1.0.3 introduces the ability to load historical Street View images by using panorama IDs (historical date IDs). This feature allows you to access Street View imagery from specific dates in the past, enabling comparison of locations over time or creating content based on historical views.

<img width="1919" height="1032" alt="Screenshot 2025-12-19 122335" src="https://github.com/user-attachments/assets/84f822e7-face-4392-8413-5c9555da5f52" />

Current date 2025
<img width="640" height="640" alt="StreetView_2025_00001_" src="https://github.com/user-attachments/assets/89d50b59-318d-46f9-9239-161b61bcf77e" />

Previous date 2021
<img width="640" height="640" alt="StreetView_2021_00001_" src="https://github.com/user-attachments/assets/d4bf82e5-c361-4a2e-91d3-aac034362f4a" />

### How to Obtain Historical Date IDs

1.  **Find Your Location in Google Maps:** Navigate to the location you want to view historically.
2.  **Enter Street View Mode:** Click on the Street View icon (orange person) and drag it to the location.
3.  **Navigate to Historical Imagery:** Click on the clock icon in the top left of the Street View panel to see available historical dates.
4.  **Select a Date:** Choose a specific date from the timeline to view the historical imagery.
5.  **Extract the URL:** Copy the complete URL from your browser's address bar after selecting the historical date.
6.  **Use the URL Parser:** Pass this URL to the **Street View URL Parser** node, which will extract the historical date ID along with the other parameters.

### Using Historical Date IDs in Nodes

All loader nodes (Street View Loader, Street View Animator, Street View Pano Loader, Street View Cubemap Loader) now include an optional `historical_date_id` parameter. When this parameter is provided:

- **Location Override:** The historical date ID takes precedence over the location parameter, ensuring you get imagery from that specific historical capture
- **Full Parameter Control:** You can still adjust heading, pitch, fov, and other parameters to control the view of the historical scene
- **Historical Animation:** The Street View Animator node allows you to create smooth camera movements on historical scenes
- **Historical Panoramas:** The Street View Pano Loader creates historical panoramic views
- **Historical Cubemaps:** The Street View Cubemap Loader creates 3D historical environment maps

### Use Cases for Historical Imagery

- **Before and After Comparisons:** Compare how locations have changed over time
- **Historical Context:** Create content showing specific events or changes at locations
- **Time Travel Effects:** Blend historical imagery with AI generated content
- **Research and Documentation:** Access historical views for architectural or geographical studies
- **Creative Projects:** Generate artistic content based on historical locations

### Important Notes about Historical Imagery

- **API Behavior:** When a historical date ID is provided, the API returns the view from that specific capture, regardless of the current date imagery
- **Available Dates:** Historical coverage varies by location - not all locations have historical imagery available
- **Image Quality:** Historical images may have different resolution or quality depending on when they were captured
- **API Usage:** Historical requests count the same as current date requests against your Google Cloud monthly credit

## 7. Troubleshooting

-   **`ValueError: API key not found`:** Your `.env` file is missing, in the wrong location, or the variable name is not `GOOGLE_STREET_VIEW_API_KEY`.
-   **Black Image Output:** This usually means Google has no Street View imagery for that coordinate, or your API key is invalid/restricted. Check your key's restrictions on the Google Cloud Console.
-   **Node not appearing in ComfyUI:** Ensure you have fully restarted the ComfyUI server after installation.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
