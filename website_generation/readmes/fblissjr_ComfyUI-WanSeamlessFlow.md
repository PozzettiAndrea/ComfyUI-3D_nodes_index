# wanvideo - seamless flow

```
ComfyUI-WanSeamlessFlow/
├── __init__.py          # Registry and imports
├── blending.py          # Core embedding interpolation functions
├── nodes.py             # ComfyUI node definitions 
├── visualization.py     # Diagnostic visualization utilities
├── README.md            # Documentation and examples
└── utils/               # Support utilities
    └── optimization.py  # Embedding optimization algorithms
```

## key notes - needs modifications, for now, to Kijai's wanvideo wrapper

- see `./reference/nodes.py` for current patches made:

## architecture / data flow map

```
[Architecture Map]
┌─────────────────────┐      ┌───────────────────────┐      ┌─────────────────────┐
│  WanSeamlessFlow    │ ──→  │ Context Window Engine │ ──→  │ Rendering Pipeline  │
│  • Embedding Order  │      │ • Window Transition   │      │ • Composite Output  │
│  • Blend Parameters │      │ • Interpolation       │      │ • Visual Smoothing  │
└─────────────────────┘      └───────────────────────┘      └─────────────────────┘
```

## integration with [Kijai's ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ LoadWanVideo     │    │ WanVideoText     │    │ WanSmartBlend    │    │ WanVideoSampler  │
│ T5TextEncoder    │───▶│ Encode           │───▶│                  │───▶│                  │
└──────────────────┘    └──────────────────┘    └──────────────────┘    └──────────────────┘
                                                        │
                                                        ▼
                                              ┌──────────────────┐
                                              │ WanBlendVisualize│
                                              │ (Optional)       │
                                              └──────────────────┘
```

### usage

**Multi-Prompt Usage**:
For optimal results with prompt transitions:

Modify your WanVideoTextEncode to use multiple prompts separated by | characters:

`high quality nature video featuring a red panda balancing on a bamboo stem | high quality nature video focusing on the bird perched on the panda's head | high quality nature video showcasing the waterfall in the background`

- Adjust the blend_width parameter based on your number of frames:
- With 257 frames and 3 prompts → 85.6 frames per prompt
- Recommended blend_width: 8-16 frames
- Higher values create wider transition zones

**Compatibility Notes**:
This setup is fully compatible with your existing components:

- TeaCache: Works alongside WanSmartBlend, both optimizing different parts
- Context Windowing: Seamless transitions work at context window boundaries
- Torch Compilation: No interference, remains performance-enhancing

**Parameter Recommendations**:

- for your particular setup with 257 frames:
- blend_width: 8        # Start conservative, increase for smoother transitions
- blend_method: "smooth" # Provides natural transitions without obvious linear interpolation
- optimize_order: true   # Automatically orders prompts for minimal semantic distance
- verbosity: 1           # Basic logging without overwhelming console output

**Extended Analysis**:
This integration creates a multi-dimensional benefits matrix:

```
⎡  TeaCache Compatibility ⎤   ⎡ High | Compatible with caching mechanisms ⎤
⎢ Context Window Flow   ⎥ = ⎢ High | Works with all scheduler types      ⎥
⎢ Smooth Transitions    ⎥   ⎢ High | Creates gradual prompt blending     ⎥
⎢ Performance Impact    ⎥   ⎢ Low  | Minimal computational overhead      ⎥
⎣ Implementation Effort ⎦   ⎣ Low  | Non-invasive integration            ⎦
```

## logical flow

**Integration point: context window embedding selection logic**

```
WindowProcessingPipeline {
  window_context → embedding_selection → model_forward → window_composition
  ↑                    ↑                                      ↑
  | (context info)     | (embedding selection)               | (output compositing)
  ↓                    ↓                                      ↓
  context_scheduler    [INTERVENTION POINT]                  window_blending
}
```
