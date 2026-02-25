# ComfyUI-Prediction-Boost
Modify noise prediction to make image brighter on Stable Diffusion.
This is a custom node for ComfyUI.

# Method
We use xₜ⊥Ɛ̃(the vector component of xₜ perpendicular to Ɛ̃) to boost up the image part of xₜ by this:

Ɛ̃ ← Ɛ̃ - boost_scale * (xₜ⊥Ɛ̃)


# Result
- model: Animagine XL V3.1<https://civitai.com/models/260267/animagine-xl-v31>
- seed: 42
- steps: 20
- cfg: 5.0
- sampler: uni_pc
- scheduler: normal
- negative prompt: flat design, early sketch, PTSD, stain, signature

- prompt: original, "the aquarium girl"

prompt: original, "the aquarium girl"
||||||
| --- | --- | --- | --- | --- |
| boost=0.0 | [![original, "the aquarium girl" (0)](samples/thumbnails/ComfyUI_00896_.png)](samples/ComfyUI_00896_.png) | [![original, "the aquarium girl" (1)](samples/thumbnails/ComfyUI_00897_.png)](samples/ComfyUI_00897_.png) | [![original, "the aquarium girl" (2)](samples/thumbnails/ComfyUI_00898_.png)](samples/ComfyUI_00898_.png) | [![original, "the aquarium girl" (3)](samples/thumbnails/ComfyUI_00899_.png)](samples/ComfyUI_00899_.png) |
| boost=0.15 | [![original, "the aquarium girl" (0)](samples/thumbnails/ComfyUI_00920_.png)](samples/ComfyUI_00920_.png) | [![original, "the aquarium girl" (1)](samples/thumbnails/ComfyUI_00921_.png)](samples/ComfyUI_00921_.png) | [![original, "the aquarium girl" (2)](samples/thumbnails/ComfyUI_00922_.png)](samples/ComfyUI_00922_.png) | [![original, "the aquarium girl" (3)](samples/thumbnails/ComfyUI_00923_.png)](samples/ComfyUI_00923_.png) |

prompt: original, "the rainy days"
||||||
| --- | --- | --- | --- | --- |
| boost=0.0 | [![original, "the rainy days" (0)](samples/thumbnails/ComfyUI_00900_.png)](samples/ComfyUI_00900_.png) | [![original, "the rainy days" (1)](samples/thumbnails/ComfyUI_00901_.png)](samples/ComfyUI_00901_.png) | [![original, "the rainy days" (2)](samples/thumbnails/ComfyUI_00902_.png)](samples/ComfyUI_00902_.png) | [![original, "the rainy days" (3)](samples/thumbnails/ComfyUI_00903_.png)](samples/ComfyUI_00903_.png) |
| boost=0.15 | [![original, "the rainy days" (0)](samples/thumbnails/ComfyUI_00924_.png)](samples/ComfyUI_00924_.png) | [![original, "the rainy days" (1)](samples/thumbnails/ComfyUI_00925_.png)](samples/ComfyUI_00925_.png) | [![original, "the rainy days" (2)](samples/thumbnails/ComfyUI_00926_.png)](samples/ComfyUI_00926_.png) | [![original, "the rainy days" (3)](samples/thumbnails/ComfyUI_00927_.png)](samples/ComfyUI_00927_.png) |

prompt: original, "botanical cafe"
||||||
| --- | --- | --- | --- | --- |
| boost=0.0 | [![original, "botanical cafe" (0)](samples/thumbnails/ComfyUI_00904_.png)](samples/ComfyUI_00904_.png) | [![original, "botanical cafe" (1)](samples/thumbnails/ComfyUI_00905_.png)](samples/ComfyUI_00905_.png) | [![original, "botanical cafe" (2)](samples/thumbnails/ComfyUI_00906_.png)](samples/ComfyUI_00906_.png) | [![original, "botanical cafe" (3)](samples/thumbnails/ComfyUI_00907_.png)](samples/ComfyUI_00907_.png) |
| boost=0.15 | [![original, "botanical cafe" (0)](samples/thumbnails/ComfyUI_00928_.png)](samples/ComfyUI_00928_.png) | [![original, "botanical cafe" (1)](samples/thumbnails/ComfyUI_00929_.png)](samples/ComfyUI_00929_.png) | [![original, "botanical cafe" (2)](samples/thumbnails/ComfyUI_00930_.png)](samples/ComfyUI_00930_.png) | [![original, "botanical cafe" (3)](samples/thumbnails/ComfyUI_00931_.png)](samples/ComfyUI_00931_.png) |

prompt: original, "across the shore"
||||||
| --- | --- | --- | --- | --- |
| boost=0.0 | [![original, "across the shore" (0)](samples/thumbnails/ComfyUI_00908_.png)](samples/ComfyUI_00908_.png) | [![original, "across the shore" (1)](samples/thumbnails/ComfyUI_00909_.png)](samples/ComfyUI_00909_.png) | [![original, "across the shore" (2)](samples/thumbnails/ComfyUI_00910_.png)](samples/ComfyUI_00910_.png) | [![original, "across the shore" (3)](samples/thumbnails/ComfyUI_00911_.png)](samples/ComfyUI_00911_.png) |
| boost=0.15 | [![original, "across the shore" (0)](samples/thumbnails/ComfyUI_00932_.png)](samples/ComfyUI_00932_.png) | [![original, "across the shore" (1)](samples/thumbnails/ComfyUI_00933_.png)](samples/ComfyUI_00933_.png) | [![original, "across the shore" (2)](samples/thumbnails/ComfyUI_00934_.png)](samples/ComfyUI_00934_.png) | [![original, "across the shore" (3)](samples/thumbnails/ComfyUI_00935_.png)](samples/ComfyUI_00935_.png) |

prompt: original, "the two of us"
||||||
| --- | --- | --- | --- | --- |
| boost=0.0 | [![original, "the two of us" (0)](samples/thumbnails/ComfyUI_00912_.png)](samples/ComfyUI_00912_.png) | [![original, "the two of us" (1)](samples/thumbnails/ComfyUI_00913_.png)](samples/ComfyUI_00913_.png) | [![original, "the two of us" (2)](samples/thumbnails/ComfyUI_00914_.png)](samples/ComfyUI_00914_.png) | [![original, "the two of us" (3)](samples/thumbnails/ComfyUI_00915_.png)](samples/ComfyUI_00915_.png) |
| boost=0.15 | [![original, "the two of us" (0)](samples/thumbnails/ComfyUI_00936_.png)](samples/ComfyUI_00936_.png) | [![original, "the two of us" (1)](samples/thumbnails/ComfyUI_00937_.png)](samples/ComfyUI_00937_.png) | [![original, "the two of us" (2)](samples/thumbnails/ComfyUI_00938_.png)](samples/ComfyUI_00938_.png) | [![original, "the two of us" (3)](samples/thumbnails/ComfyUI_00939_.png)](samples/ComfyUI_00939_.png) |