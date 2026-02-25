# ComfyUI NormalCrafter

This is a ComfyUI custom node implementation for [NormalCrafter: Learning Temporally Consistent Normals from Video Diffusion Priors](https://github.com/Binyr/NormalCrafter) by Yanrui Bin, Wenbo Hu, Haoyuan Wang, Xinya Chen, and Bing Wang.

It allows you to generate temporally consistent normal map sequences from input video frames.

## Installation

1.  Clone this repository into your `ComfyUI/custom_nodes/` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/AIWarper/ComfyUI-NormalCrafterWrapper.git
    ```
2.  Install the required dependencies. Navigate to the `ComfyUI-NormalCrafter` directory and install using the `requirements.txt`:
    ```bash
    ACTIVATE YOUR VENV FIRST
    ComfyUI-NormalCrafterWrapper
    pip install -r requirements.txt
    ```
    (See the `requirements.txt` for notes on the `diffusers` dependency, which ComfyUI often manages.)
3.  Restart ComfyUI.

## Node: NormalCrafter (Process Video)

This node takes a sequence of images (video frames) and processes them to output a corresponding sequence of normal map images.

### Parameters

*   **`images` (Input Socket)**: The input image sequence (video frames).
*   **`pipe_override` (Input Socket, Optional)**: Allows providing a pre-loaded NormalCrafter pipeline instance. If unconnected, the node loads its own.
*   **`seed`**: (Integer, Default: 42) Controls the randomness for reproducible results.
*   **`control_after_generate`**: (Fixed, Increment, Decrement, Randomize) Standard ComfyUI widget for seed behavior on subsequent runs. Note: The underlying pipeline uses the seed for each full video processing.
*   **`max_res_dimension`**: (Integer, Default: 1024) The maximum dimension (height or width) to which input frames are resized while maintaining aspect ratio.
*   **`window_size`**: (Integer, Default: 14) The number of consecutive frames processed together in a sliding window. Affects temporal consistency.
*   **`time_step_size`**: (Integer, Default: 10) How many frames the sliding window moves forward after processing a chunk. If less than `window_size`, frames will overlap, potentially improving smoothness.
*   **`decode_chunk_size`**: (Integer, Default: 4) Number of latent frames decoded by the VAE at once. Primarily a VRAM management setting.
*   **`fps_for_time_ids`**: (Integer, Default: 7) Conditions the model on an intended Frames Per Second, influencing motion characteristics in the generated normals. *Note: In testing, this parameter showed minimal to no visible effect on the output for this specific model and task. As such I hard coded the value*
*   **`motion_bucket_id`**: (Integer, Default: 127) Conditions the model on an expected amount of motion. *Note: In testing, this parameter showed minimal to no visible effect on the output for this specific model and task. As such I hard coded the value*
*   **`noise_aug_strength`**: (Float, Default: 0.0) Strength of noise augmentation applied to conditioning information. *Note: In testing, this parameter showed minimal to no visible effect on the output for this specific model and task. As such I hard coded the value*

### Troubleshooting Flicker / Improving Temporal Consistency

If you are experiencing flickering or temporal inconsistencies in your output:

*   **Increase `window_size`**: A larger window allows the model to see more temporal context, which can significantly improve consistency between frames.
*   **Adjust `time_step_size`**: Using a `time_step_size` smaller than `window_size` creates an overlap between processed windows. This overlap is merged, which can smooth transitions. For example, if `window_size` is 20, try a `time_step_size` of 10 or 15.

You may be able to increase `window_size` and `time_step_size` substantially (e.g., to their maximum values) without encountering Out Of Memory (OOM) issues, depending on your hardware. Experiment to find the best balance for your needs.

### Dependencies

*   `mediapy`
*   `decord`
*   `diffusers` (and its dependencies like `transformers`, `huggingface_hub`) - ComfyUI usually manages its own `diffusers` version. Install manually if you encounter specific import errors related to it.
*   `torch`, `numpy`, `Pillow` (standard Python ML/Image libraries)

Refer to `requirements.txt` for more details.
