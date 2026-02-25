# ComfyUI-Automation

A collection of custom nodes for ComfyUI designed to facilitate complex looping and iteration workflows, specialized in media batch processing (Image + Audio + Video).

## Overview

The core feature of this suite is the **Stateful Iterator System**, which allows you to iterate through a list of items across multiple generations without causing circular dependency errors in ComfyUI.

## Nodes

### 1. Iterator Item
The basic building block. It gathers media components into a single bundled object.
- **Inputs**:
    - `image`: The source image for this item.
    - `audio_text`: Multiline string for audio generation (e.g., TTS).
    - `video_prompt`: Multiline string for CLIP text encoding or video generation.
- **Outputs**:
    - `IMAGE`, `AUDIO_TEXT`, `VIDEO_PROMPT`: Individual passthrough components.
    - `ITERATOR_ITEM`: The bundled object used by the Iterator List.

### 2. Iterator List
The controller that manages which item is currently active.
- **Inputs**:
    - `iterator_id`: A unique string identifier to sync state with the `Iterator Signal`.
    - `reset`: When enabled, forces the index back to 0 (the first item).
    - `item1` to `item6`: Slots for your `ITERATOR_ITEM` bundles.
    - `trigger`: **(Optional)** A dummy input (accepts any type) used to force this node to execute *after* some other node in ComfyUI (useful for manual execution ordering).
- **Outputs**:
    - `IMAGE`, `AUDIO_TEXT`, `VIDEO_PROMPT`: Standard types from the *currently active* item.
    - `IS_FINISHED`: Boolean that turns True when the last item in the list is reached.

### 3. Iterator Signal
The "trigger" that tells the system to advance.
- **Inputs**:
    - `image`: The final output image of your processing chain.
    - `iterator_id`: **Important**: Must match the `iterator_id` in the corresponding `Iterator List`.
    - `active`: Toggle to enable/disable the advancement logic.
- **Outputs**:
    - `SIGNAL`: Boolean trigger status.
    - `IMAGE`: The input image (passthrough). This allows you to chain a Save Image or Preview node *after* the signal to ensure the loop captures the result.
- **Logic**: When this node receives a valid image, it increments the index for the specified `iterator_id`. If `IS_FINISHED` is False, it automatically queues the next iteration.

### 4. Iterator Counter
A simple numeric counter that increments with each iteration step.
- **Inputs**:
    - `iterator_id`: A unique string identifier to sync state with the `Iterator Signal`.
    - `start`: The starting integer value.
    - `max_iterations`: The total number of iterations to run.
    - `step`: The amount to increment by each step.
    - `reset`: When enabled, forces the counter back to the start value.
- **Outputs**:
    - `current_count`: The current integer value (start + index * step).
    - `is_finished`: Boolean that turns True when the max iterations are reached.

### 5. Video Concatenation
A specialized node that joins multiple video files into a single sequence, with optional transitions.
- **Inputs**:
    - `transition_type`: The type of transition to use between clips (e.g., `fade`, `slideleft`). Default is `none`.
    - `transition_time`: Duration of the transition in seconds.
    - `output_format`: The format of the concatenated video (e.g., `mp4`, `mkv`, `gif`).
    - `video1` to `video5`: Input video objects (supports paths, lists, or ComfyUI video objects).
- **Logic**:
    - Concatenates videos sequentially.
    - Applies FFmpeg `xfade` transitions if selected.
    - Saves the result to the ComfyUI temp directory.
- **Outputs**:
    - `video`: The concatenated video object (compatible with ComfyUI video nodes).

## How to setup a Video Batch Loop

1. Create several **Iterator Item** nodes with your source images and prompts.
2. Connect them into **Iterator List**. Give it a `iterator_id` like `my_sequence`.
3. Build your workflow (e.g., Upscale -> KSampler -> Video Combine).
4. At the very end, connect your generated image to a **Iterator Signal**. Give it the same `iterator_id` (`my_sequence`).
5. Use **Auto Queue** in ComfyUI.
6. Each time a generation is completed, the system advances to the next item.
7. Once your batch is done, connect the output paths of your generated videos to the **Video Concatenation** node to create the final unified video.

## Examples

I have included example workflows in the [examples/](file:///c:/Users/fjtor/Development/ComfyUI/custom_nodes/ComfyUI-Automation/examples) directory:

- [basic_image_loop.json](file:///c:/Users/fjtor/Development/ComfyUI/custom_nodes/ComfyUI-Automation/examples/basic_image_loop.json): A simple demonstration of iterating through two images.
- [video_batch_loop.json](file:///c:/Users/fjtor/Development/ComfyUI/custom_nodes/ComfyUI-Automation/examples/video_batch_loop.json): A more advanced workflow showing video generation and automatic merging.

## Installation

1. Navigate to `ComfyUI/custom_nodes`.
2. Clone this repository:

   ```bash
   git clone https://github.com/your-repo/ComfyUI-Automation.git
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Restart ComfyUI.
