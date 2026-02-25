# WanVideoLooper Nodes for ComfyUI

This is a set of custom nodes for ComfyUI designed for generating sequential long video clips, handling continuity between segments, and offering advanced control over the sampling process, including per-segment LoRA/model application.

This pack contains **three** nodes:

1.  **`WanVideo Looper`**: The main node that takes base models, a list of prompts, and various settings to generate a sequence of video clips, merging them seamlessly.
2.  **`WanVideo Looper Prompts`**: A new helper node for managing multiline positive prompts, a global negative prompt, prefixes/suffixes, and saving/loading prompt profiles.
3.  **`WanVideo Looper Lora Sequencer`**: A helper node designed to feed pre-patched Model and CLIP objects into the `WanVideo Looper` for specific segments, enabling per-segment LoRA application.

<img width="353" height="347" alt="image" src="https://github.com/user-attachments/assets/69054332-b01e-4c54-a75b-7dc5cd683930" />

---

**Watch the Tutorial Video (Original):**
*(Note: This video may be for an older version but can still be helpful for understanding the core concepts.)*

<a href="https://www.youtube.com/watch?v=jztckgdkCHc">
  <img src="https://img.youtube.com/vi/jztckgdkCHc/maxresdefault.jpg" 
       alt="Watch the tutorial video" 
       width="480" height="270" border="0" />
</a>

---

## How to Install

1.  Navigate to your ComfyUI installation directory.
2.  Go into the `ComfyUI/custom_nodes/` folder.
3.  Create a new folder inside `custom_nodes` named **`WanVideoLooper`**.
4.  Place all the `.py` files inside the new `WanVideoLooper` folder:
    * `__init__.py`
    * `wan_looper_node.py`
    * `wan_lora_sequencer.py`
    * `wan_prompts_node.py`
5.  Create a `js` subfolder inside your new folder: `ComfyUI/custom_nodes/WanVideoLooper/js`.
6.  Place all the `.js` files inside that `js` folder:
    * `wan_lora_sequencer.js`
    * `wan_prompts_node.js`
7.  **(Required for Color Match)** Open a terminal or command prompt, activate your ComfyUI virtual environment (if you use one), and run:
    ```bash
    pip install color-matcher
    ```
8.  **Restart your ComfyUI server.**

The nodes will be available by right-clicking the canvas and selecting **Add Node > WanVideoLooper**.

---

## 1. WanVideo Looper

This is the core node for generating video sequences segment by segment. It intelligently handles continuity and uses an advanced MoE-style sampling approach.

<img width="268" height="608" alt="image" src="https://github.com/user-attachments/assets/0fdb8552-ec6d-4e7c-b0fa-ee2b5a455dc9" />

### Features

* **Prompt List Input:** Takes a `prompt_list` and `negative_prompt` directly from the `WanVideo Looper Prompts` node.
* **Seamless Continuity:** Uses frame merging (`frame_merge`) to ensure smooth transitions between segments.
* **MoE-Style Sampling:** Integrates Mixture of Experts logic with a single `steps` input and automatic calculation of the split point (`model_switch_point`).
* **Internal Color Matching:** Can apply MKL color matching between segments (`color_match`) or match the entire video to the very last frame (`color_match_lastframe`) to fix color drift. Requires `pip install color-matcher`.
* **Per-Segment Models/LoRAs:** Supports an optional input from the `WanVideo Lora Sequencer` to use different, pre-patched models for specific segments.
* **Dry Run Mode:** Includes an `enable_dry_run` toggle to quickly check setup and logs without performing sampling/decoding.

### Inputs & Outputs

* **Required Inputs**
    * `model_high`: The BASE high-noise model.
    * `model_low`: The BASE low-noise model.
    * `clip`: The BASE CLIP model.
    * `vae`: The VAE model used for decoding.
    * `start_image`: The seed image for the first loop.
    * `positive_prompts`: Connect the `prompt_list` output from the `WanVideo Looper Prompts` node.
    * `negative_prompt`: Connect the `negative_prompt` output from the `WanVideo Looper Prompts` node.
    * `seed`: The random seed.
    * `steps`: The total number of sampling steps for each loop.
    * `enable_motion_cfg`: Enable a separate CFG for the very first step.
    * `cfg_motion_step`: CFG for the first step ONLY.
    * `cfg_high_noise`: CFG for the high-noise model (structure/motion).
    * `cfg_low_noise`: CFG for the low-noise model (details).
    * `sampler_name`: The sampling algorithm.
    * `scheduler`: The noise scheduler.
    * `model_switch_point`: Timestep to switch from high-noise to low-noise model (e.g., 0.9).
    * `sigma_shift`: Applies sigma shift to both models (e.g., 8.0).
    * `denoise`: Denoise amount (1.0 = full new image).
    * `width`/`height`: The output video dimensions.
    * `frame_merge`: Number of frames to overlap/merge between loops.
    * `duration_sec`: Duration of *each* segment in seconds (5s recommended).
    * `color_match`: (New!) Enable segment-to-segment MKL color matching.
    * `color_match_lastframe`: (New!) Override `color_match` and instead match all frames to the *very last* frame of the sequence.
    * `color_match_strength`: (New!) Strength of the color match (0.0 to 1.0).
    * `enable_dry_run`: Skips sampling and decoding to quickly check setup.
* **Optional Inputs**
    * `clip_vision`: (Optional) A CLIP Vision model for guiding the start image.
    * `model_clip_sequence`: (Optional) Connect the `WanVideo Lora Sequencer` output here.
    * `color_match_ref`: (New!) (Optional) A static reference image for color matching. If omitted, uses the last frame of the previous segment.
* **Outputs**
    * `images`: The final, concatenated batch of all generated video frames.
    * `last_frame`: The single, very last frame of the entire sequence.

---

## 2. WanVideo Looper Prompts

A helper node to manage all your prompts, prefixes, and profiles in one place.

<img width="471" height="621" alt="image" src="https://github.com/user-attachments/assets/60b79704-47d7-4aea-8ed8-cb442d5167e1" />

### Features

* **Multiline Prompts:** Enter one positive prompt per line. Each line becomes a new video segment. Empty lines are ignored.
* **Global Negative Prompt:** A single multiline text box for your negative prompt.
* **Prefix/Suffix:** Automatically add text (like `masterpiece,`) *before* and *after* every single prompt (positive and negative) with a toggle to enable or disable.
* **Profile Management:** Save your complex prompt setups (positive, negative, prefix, suffix) to named profiles in your browser's `localStorage`.
* **Save/Load/Delete:** Easily save new profiles, load existing ones from a dropdown, and delete old profiles.

### Inputs & Outputs

* **Inputs (Widgets)**
    * `prompts`: Multiline text for positive prompts (one per line).
    * `negative_prompt`: Multiline text for the global negative prompt.
    * `enable_prefix_suffix`: A "true"/"false" toggle.
    * `prefix`: Text to add before each prompt.
    * `suffix`: Text to add after each prompt.
    * *(Profile controls for saving/loading)*
* **Outputs**
    * `prompt_list`: A list of processed positive prompts, ready for the main looper node.
    * `negative_prompt`: The single, processed negative prompt string.

---

## 3. WanVideo Looper Lora Sequencer

This helper node allows you to specify different, pre-patched Model and CLIP objects for each segment of your video sequence. It's the key to applying different LoRAs to different parts of your video.

<img width="225" height="112" alt="image" src="https://github.com/user-attachments/assets/f50eaaf3-3282-4d95-ac54-ba3c034d53d7" />

### Features

* **Segment Inputs:** Provides **10** sets of optional inputs (`model_high_X`, `model_low_X`, `clip_X`) corresponding to the first 10 prompt segments.
* **Dynamic Inputs:** The node's UI is dynamic. It only shows inputs for segments that are connected. Connect segment 1 to see segment 2, and so on.
* **Clean Workflow:** You patch your models using standard ComfyUI nodes (`Load LoRA`, etc.) *outside* the sequencer. Connect the final patched MODEL and CLIP into the corresponding inputs on this node.
* **Bundles Inputs:** The sequencer bundles these connected models/clips into a list for the main looper.
* **Fallback:** If you leave the inputs for a specific segment unconnected, the `WanVideo Looper` will automatically fall back to using the clean base models for that segment.

### Inputs & Outputs

* **Optional Inputs (30 total)**
    * `model_high_1` to `model_high_10`: The pre-patched HIGH model for each segment.
    * `model_low_1` to `model_low_10`: The pre-patched LOW model for each segment.
    * `clip_1` to `clip_10`: The pre-patched CLIP