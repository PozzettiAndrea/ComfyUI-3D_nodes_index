# ComfyUI WAN2.1 VACE Video Helper Nodes

WORKFLOW URL:
[wan2_1VaceInfinite.json](https://gist.github.com/heheok/396b0fa639f74ef331081343129c2588)


This collection of custom nodes for ComfyUI is specifically designed to automate and streamline the process of creating infinite videos with WAN2.1 VACE.

## Installation

### Method 1: Using Git (Recommended)

1.  Open a terminal or command prompt.
2.  Navigate to the `custom_nodes` directory inside your ComfyUI installation.
    ```bash
    cd path/to/ComfyUI/custom_nodes
    ```
3.  Clone the repository:
    ```bash
    git clone https://github.com/heheok/comfyui_wan2.1_vace_infinite_helpers.git custom_scripts
    ```
4.  Restart ComfyUI.

---

## Nodes

### CyclicCharacterAndBackgroundPrompt

This node automates the generation of prompts by cycling through predefined lists, allowing for dynamic and varied video creation without manual intervention.

**Inputs:**

- `char_prompts_json`: A JSON array of strings for character prompts.
- `bg_prompts_json`: A JSON array of strings for background prompts.
- `cam_prompts_json`: A JSON array of strings for camera movement or additional prompts.

**Functionality:**

The node combines one prompt from each category to generate a final prompt. If the lists have different lengths, the shorter lists will loop. For example, if you have 2 character prompts and 1 background prompt, the background prompt will be repeated for each character prompt.

**IMPORTANT NOTE:**

This node creates and manages a state file named `cyclic_prompt_indices.json` in the root ComfyUI folder. This file tracks the current index for each prompt list. To reset the cycle and start from the beginning of your prompt lists, you can either:

- Delete the `cyclic_prompt_indices.json` file.
- Manually edit the file to reset the indices: `{"char_idx": 0, "bg_idx": 0, "add_idx": 0}`

### LatestVideoFromFolder

This node automatically finds and loads the most recently created video file from a specified directory. This is essential for creating a continuous video loop, as it feeds the last generated video into the next generation cycle.

**Inputs:**

- `folder_path`: The absolute path to the directory containing your generated videos. For example: `C:\ComfyUI\output\padded`

**Outputs:**

- `video`: The loaded video file.

### PrepareControlVideo

This node prepares the video input for the ControlNet, which is crucial for maintaining consistency between video segments.

**Inputs:**

- `video_frames`: The video to be prepared, typically from the `VAE DECODE` node.
- `tail_count`: The number of frames to take from the _end_ of the input video.
- `pad_count`: The number of gray frames to add to the END of the generated padded video segment.

**Functionality:**

The node takes the last `tail_count` frames of the input video, puts them in the front and appends `pad_count` gray frames. This padded video is then used as the control video for the next segment's generation, ensuring a smooth transition.

---

## Workflow & Important Considerations

### Full Video vs. Padded Video

For a seamless workflow, it is recommended to save your generated videos into two separate locations:

- **Full Video Path:** This folder will contain the final, un-padded video segments that you will later merge together manually to create your final long-form video.
- **Padded Video Path:** This folder is used by the `LatestVideoFromFolder` node. It should contain the padded videos that are used as control inputs for subsequent generations.

### Initial Generation - VERY IMPORTANT!

For the very **first** video generation in your sequence, you **MUST DISABLE** the group of nodes responsible for handling the "Previous Video to Control Video" (which includes `LatestVideoFromFolder`). This is because there is no preceding video to use as a control input.

After the first video has been generated, you must **ENABLE** this group for all subsequent generations so that the system can create a continuous, looping video.
