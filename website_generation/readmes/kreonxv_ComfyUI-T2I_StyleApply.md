# ComfyUI T2I Apply Style Node (only SD 1.5)

Simple node for ComfyUI that applies a text-to-image (T2I) style to an image or embedding with support for start/end frame control and a weight parameter.

Features
- Apply a style (image or embedding) to the target image or embedding.
- Start / End support: limit the style application to a frame range (useful for animations or frame sequences).
- Weight: control the strength of the style application (0.0 = no effect, 1.0 = full effect).

Inputs
- `Image/Input` — the image or embedding to be styled.
- `Style` — style source (image or style embedding).
- `Start` — start frame or step (inclusive) where the style begins applying.
- `End` — end frame or step (inclusive) where the style stops applying.
- `Weight` — float (0.0–1.0) controlling style strength.

Outputs
- `Styled` — the resulting image or embedding with the style applied according to the specified range and weight.

Usage
1. Add the node to your ComfyUI flow.
2. Connect the target `Image/Input` and the `Style` source.
3. Set `Start` and `End` to control which frames receive the style (leave blank or set to full range to apply globally).
4. Adjust `Weight` to blend between the original and styled outputs.

Notes
- When using for animations, ensure frame indices match your sequence indexing (0-based vs 1-based depending on your pipeline).
- If `Start` > `End`, the node will skip applying the style.


