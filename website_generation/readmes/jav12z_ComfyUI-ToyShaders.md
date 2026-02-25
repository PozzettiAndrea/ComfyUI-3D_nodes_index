👾 ComfyUI ToyShaders

ToyShaders is a custom node for ComfyUI that allows you to render GLSL shaders (Shadertoy-style) directly inside your workflows.
It supports internal textures, multipass rendering, presets, animated previews and automatic depth map output.

✨ Features

Shadertoy-style GLSL rendering inside ComfyUI

Multipass support (Buffer A + Main Image)

Built-in procedural textures (noise, clouds, wood, checkerboard, etc.)

Optional external textures via iChannel0–3

Automatic preset discovery from the shaders/ folder

Animated WebP preview output

Automatic depth map generation using a custom variable

Clean separation between rendering backend and UI node



✔ Option 2 — Manual Installation

git Clone this repository into:

ComfyUI/custom_nodes/
Install requeriments.txt 

Then restart ComfyUI.

🗂 Shader Presets

Download new shaders from https://www.shadertoy.com/

You can place .glsl or .txt shader files inside:

ComfyUI-ToyShaders/shaders/


They will automatically appear in the preset selector inside the node.

This allows you to build your own library of shaders or reuse Shadertoy-style code with minimal adjustments.

🧪 Dependencies


🛠 Quick Usage Guide, test the sample workflow

Add the ToyShader Render node in ComfyUI.

Select a preset or paste your own GLSL code.

Optionally add a Buffer A shader for multipass effects.

Tune parameters like:

speed

scale

internal texture selection

depth variable & depth scaling

The node outputs:

RGB animation frames

Depth map (3-channel grayscale) - EXPERIMENTAL



🧑‍💻 Author: jav12z aka striking-Long aka...

 😄
Feel free to contribute, fork or open issues!

❤️ Enjoy

This project brings the expressiveness of Shadertoy into ComfyUI’s node-based workflow.
Have fun creating procedural graphics, loops, VFX and experiments directly inside the AI pipeline!

Disclaimer regarding Shadertoy code:
While this node engine is MIT licensed, the GLSL code snippets you copy from Shadertoy.com are subject to their original authors' licenses (usually CC BY-NC-SA 3.0 unless specified otherwise). Please respect the original artists' rights when using their code for commercial projects.


