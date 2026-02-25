# Comfyui-ColorMatchNodes
Various ( vibe coded ) Color Match Nodes 

Currently only two ComfyUI custom nodes to color-match a target image (or batch) against two reference images, then blend the two matched results with either a manual or an auto-ramped weight schedule.

✨ What you get

ColorMatch2Refs – match to Ref A and Ref B with a manual weight_a (B gets 1 - weight_a), then optionally pull toward the blended result with strength.

ColorMatchBlendAutoWeights – same idea, but weight_a is automatically ramped across the batch (defaults: first frame toward A, last frame toward B). Supports easing curves and start/end weights.

Examples : 
![Preview](/docs/excolormatch2ref.png)
![Preview](/docs/exblend-1-1.png)

Use Case for ColorMatchBlendAutoWeights : Smooth Color Transition Between Clips ( for example when using Vace to generate clip transition )

Imagine you’re grading a video sequence made of three clips:

[ Clip A ] → [ Clip B ] → [ Clip C ]

You want Clip B (the middle one) to smoothly inherit the color mood from Clip A to Clip C — avoiding a harsh visual jump.

That’s exactly where ColorMatchBlendAutoWeights ( should ) shines:

Use the last frame of Clip A as Reference A

Use the first frame of Clip C as Reference B

Use all frames of Clip B as Targets

The node will then:

Color-match each frame of Clip B to both references (A & B)

Automatically ramp the influence from A → B across the batch
(first frame close to Clip A’s color tone, last frame close to Clip C’s)

Blend them progressively according to the easing curve and strength

This produces a natural, cinematic color transition — perfect for scene bridges, shot stitching, or matching intermediate frames between two graded looks.

Example weight ramp for 10-frame Clip B (default linear mode):
 ```
Frame:     0    1    2    3    4    5    6    7    8    9
weight_a: 1.0  0.9  0.8  0.7  0.6  0.5  0.4  0.3  0.2  0.1 → 0.0
weight_b: 0.0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9 → 1.0
 ```
Result → first frames look closer to Clip A, last frames closer to Clip C, with a smooth transition in between.

You can also use strength_mode : u_shape to make the color-match intensity dip in the center of the target sequence.
For example with the same 10-frame Clip B but wit strength_mode = "u_shape", mid_strength = 0.5, strength_easing = "linear": 
 ```
Frame:     0    1    2    3    4    5    6    7    8    9
weight_a: 1.0  0.9  0.8  0.7  0.6  0.5  0.4  0.3  0.2  0.1 → 0.0
weight_b: 0.0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9 → 1.0
strength: 1.0  0.9  0.8  0.7  0.6  0.5  0.5  0.6  0.7  0.8 → 1.0
 ```
