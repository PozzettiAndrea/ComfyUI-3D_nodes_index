# ATI_AudioReactive
ComfyUI Node, Mixing RyanOnTheInside’s reactive nodes with Fillip’s Path Animation

# _RyanOnTheInside:_ 

https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside

# _fillip lividtm:_

https://huggingface.co/lividtm/Wan_ATI/tree/main


Little experiment of mixing RyanOnTheInside's Audio reactive nodes with Fillip's ATI Path Animation. using Google antigravity. I'm not a programmer, I'm posting it for anyone who wants to play for a while, it needs to be adjusted and I'm sure it has bugs

<p align="center">
  <img src="./assets/gif.gif" alt="gif" width="70%">
</p>



## Here is the complete list of parameters for the Audio Reactive Path Animator node and how they work:

## Main Controls
movement_mode: Defines how the dot moves.

amplitude: The dot's position is locked to the volume. Silence = Start of path, Loud = End of path.

accumulate: The dot travels along the path like a car. Sound makes it move forward; silence makes it stop. It bounces when it hits the ends.

## Sensitivity:
In Amplitude mode: Controls Range (how far down the path the dot goes).
In Accumulate mode: Controls Speed (how fast the dot travels).
smoothing: Smooths out jittery volume changes.
0.0: Raw, instant reaction (can be jittery).
1.0: No movement (completely flat).
Tip: Use ~0.3 - 0.5 for natural movement.

## Amplitude Mode Specifics (When movement_mode is amplitude)
release: Controls how fast the dot returns to the start after a beat.
Low (0.2): Snappy, returns instantly.
High (0.8): Slow, smooth return. Great for "one jump per rhythm".

## Amplitude_curve: Acts as a Noise Gate / Expander.
1.0: Linear (standard).
> 1.0 (e.g., 3.0): Suppresses low-volume noise ("meaningless jumps") and accentuates loud beats. Use this to clean up the motion.

## Accumulate Mode Specifics (When movement_mode is accumulate)
flip_on_beat: If enabled, the dot will reverse direction whenever it detects a beat, making it "dance" back and forth.
beat_threshold: Sensitivity for the flip_on_beat detection.
Low (0.02): Flips on everything (hi-hats, snares).
High (0.1): Flips only on big kicks.

## Visuals
motion_blur: Draws a streak connecting the previous frame to the current frame.
Enable this to fix the "double point" or stroboscopic effect when the dot moves fast.
blur_radius: Adds a static Gaussian blur (fuzziness) to the dot (like an out-of-focus camera).
trail_length: Leaves a fading trail behind the dot.

shape
, shape_size, shape_color, bg_color: Standard appearance controls.
System
duration_frames: Forces the animation to be a specific number of frames.
0: Matches the audio length exactly.
> 0: Stretches/squashes the audio to fit this exact frame count (useful for syncing with video models like Wan/Kling).
frame_rate: The FPS of the output animation.
fft_size, min_frequency, max_frequency: Advanced audio analysis settings to isolate specific frequency ranges (e.g., set min/max to 20-150Hz to only react to bass).
>
>
<p align="center">
  <img src="./assets/Nodes.png" alt="node" width="70%">
</p>
