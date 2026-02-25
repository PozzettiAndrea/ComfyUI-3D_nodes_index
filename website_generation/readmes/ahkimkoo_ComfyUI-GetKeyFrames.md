# MakeFrame

## GetKeyFrames:
This node intelligently extracts keyframes from a sequence of images by first detecting scene changes and then selecting representative frames from within each scene.

**Workflow:**
1.  **Scene Detection**: The node calculates the difference between consecutive frames. Any difference exceeding the `threshold` marks a potential scene cut.
2.  **Priority Filtering**: If the number of detected scenes is greater than `num_keyframes`, the node automatically prioritizes and selects only the scenes separated by the most significant changes. This ensures that the final output is focused on the most important moments, even with a low threshold.
3.  **Dynamic Allocation**: The total `num_keyframes` are intelligently distributed among these top-priority scenes.
4.  **Frame Extraction**: Within each scene, the allocated number of keyframes are sampled uniformly to represent the entire scene segment.

**Parameters:**
- **`scene_cut_method`**: The algorithm for comparing frames to detect scene cuts.
  - **MSE**: Fast, good for sharp cuts.
  - **SSIM**: Slower, but closer to human perception.
  - **pHash**: Robust against minor edits.
- **`scene_select_method`**: The algorithm for selecting keyframes *within* each detected scene. All non-uniform methods use a peak-finding algorithm to ensure the selected frames are distributed and represent distinct moments of change.
  - **Uniform**: Default. Selects frames evenly distributed throughout the scene.
  - **Peak_Difference**: Selects frames that are most different from the start of the scene, capturing the climax of the action.
  - **Edge_Change_Rate**: A sophisticated method that focuses on the central area of the frame, detecting the rate of change in structural edges to find moments of highest action.
  - **Highest_Contrast**: Selects frames with the highest visual contrast, often corresponding to the most visually striking moments.
- **`num_keyframes`**: The total number of keyframes you want to extract across all scenes.
- **`threshold`**: The core parameter for scene detection, **acting on a normalized 0.0-1.0 scale for all methods**. It defines the minimum relative change required to be considered a scene cut. A value of `0.1` means only changes in the top 90% of intensity are considered. A good starting point for all methods is `0.1` to `0.2`.
- **`central_focus_ratio`**: **(Only used when `scene_select_method` is `Edge_Change_Rate`)**. Defines the size of the central area to analyze (e.g., 0.3 means the central 30% of the image).

![image](https://github.com/LonicaMewinsky/ComfyUI-MakeFrame/assets/93007558/ce9de415-d9c4-43ac-94ba-7b8af52e5927)

## MakeGrid:
Plots given images on a grid. Calculates number of rows and columns for most even aspect ratio.
* For concurrent frame generation. Creates potentially massive image.
* Images are resized to be evenly-divisible by rows, columns, and 8 (to prevent "resize wobble").
* Empty cells are padded with repeats of last image. Black space frustrates generation.

![image](https://github.com/LonicaMewinsky/ComfyUI-MakeFrame/assets/93007558/ac61e777-b5d9-48d5-b20f-57ff1c320d7c)

## BreakGrid:
Breaks given image grid(s) back into individual images. Good practice to use rows/columns output from MakeGrid.

![image](https://github.com/LonicaMewinsky/ComfyUI-MakeFrame/assets/93007558/6a9a5743-4a43-470b-8e10-2f96a2836c8d)

---

## Acknowledgement
This project is a modified version based on the original work by LonicaMewinsky. The original repository can be found at [https://github.com/LonicaMewinsky/ComfyUI-MakeFrame](https://github.com/LonicaMewinsky/ComfyUI-MakeFrame).
