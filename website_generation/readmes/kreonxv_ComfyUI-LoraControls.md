# ComfyUI-LoraControls

A set of ComfyUI custom nodes to control LoRA (Low-Rank Adaptation) strength programmatically during the sampling process. This allows for dynamic and fine-grained control over how a LoRA's influence is applied over time, from simple fades to complex, multi-peaked schedules.

## Nodes

This package includes two main nodes:

1.  **`LoraKeyframes`**: Offers powerful, granular control over LoRA strength using a flexible keyframe and interpolation system.
2.  **`LoRAStepRange`**: Provides a simplified, high-level interface for applying a LoRA only during a specific percentage range of the sampling steps.

---

## 1. LoraKeyframes Node

The `LoraKeyframes` node allows you to define a curve for LoRA strength that evolves over the course of the sampling process. You can make a LoRA fade in, fade out, pulse, or follow any custom schedule you design.


### Intention

The primary goal of this node is to move beyond static LoRA strength. By scheduling the strength, you can:
- **Subtly introduce concepts**: Start a LoRA's effect at zero and fade it in to gently blend its features.
- **Reduce over-baking**: Apply a strong LoRA early in the process and then fade it out to prevent its style from dominating the final image.
- **Target specific styles**: Activate a LoRA only during the middle steps to influence composition without affecting initial noise or final details.
- **Create complex effects**: Use multiple peaks to have a LoRA influence the image at different stages of generation.

### Usage and Inputs

#### Keyframe String
The core of the node is the `keyframes` string, which follows a `strength@percent` format.

-   `strength`: The LoRA strength multiplier at that point (e.g., `0.0` is off, `1.0` is full strength, `0.5` is half).
-   `percent`: The point in the sampling process to apply this strength (`0.0` is the beginning, `0.5` is the midpoint, `1.0` is the end).

**Examples:**
-   `"0@0.0, 1@0.5, 0@1.0"`: A bell curve. The LoRA fades in until the halfway point and then fades out.
-   `"1@0.0, 0@0.7"`: Starts at full strength and fades out by the 70% mark.
-   `"0@0.2, 1@0.5, 0@0.8"`: Activates only in the middle of the sampling process.

#### Presets
For convenience, several common patterns are available in the `preset` dropdown, such as `fade_in`, `fade_out`, `two_peaks`, etc. Selecting a preset will override the `keyframes` string.

#### Interpolation
This setting controls how the strength transitions *between* your defined keyframes.
-   `step`: Jumps directly from one strength to the next (the default behavior in many systems).
-   `linear`: Creates a straight line transition.
-   `smoothstep`, `ease_in`, `ease_out`: Provides various smooth, curved transitions for more organic changes.

#### Other Inputs
-   `strength_multiplier`: A global multiplier applied to all strength values in your schedule.
-   `resolution`: Controls the granularity of the schedule. A higher value creates a smoother, more detailed curve by generating more intermediate steps.

### Outputs
-   `CLIP`: The modified CLIP object with the LoRA schedule applied, ready to be passed to a sampler.
-   `schedule_graph`: A text-based graph printed to the console, visualizing the LoRA strength schedule you have created. This is extremely useful for debugging and confirming your curve looks as expected.

---

## 2. LoRAStepRange Node

This is a simplified version of the keyframing concept, designed for the common use case of applying a LoRA for only a portion of the sampling process.


### Intention

This node is for when you want to quickly "gate" a LoRA. For example, you might want a character LoRA to apply only from 20% to 80% of the steps to establish the character without letting it interfere with the initial layout or final texturing. It's a "set it and forget it" tool for basic LoRA timing.

### Usage and Inputs

-   `lora_name`: The LoRA to apply.
-   `strength_clip`: The strength of the LoRA when it is active.
-   `start_percent`: The percentage of steps at which the LoRA should turn **on**.
-   `end_percent`: The percentage of steps at which the LoRA should turn **off**.

The node works by creating a simple keyframe schedule behind the scenes: `0@0, 1@start_percent, 1@end_percent, 0@end_percent`. The LoRA is off, turns on at the start, stays on, and turns off at the end.

### Outputs
-   `CLIP`: The modified CLIP object with the scheduled LoRA, ready for the sampler.

## Installation

1.  Navigate to your `ComfyUI/custom_nodes/` directory.
2.  Clone this repository: `git clone https://github.com/kreonxv/ComfyUI-LoraControls.git`
3.  Restart ComfyUI.
4.  The "Lora Keyframes" and "LoRA Step Range" nodes will be available under the "loaders" category when you right-click the canvas.
