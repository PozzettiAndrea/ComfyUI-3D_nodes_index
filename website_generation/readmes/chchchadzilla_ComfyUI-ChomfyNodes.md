# ComfyUI-ChomfyNodes

A professional suite of utility nodes for ComfyUI, featuring forensic logging, massive wildcard control, universal noise injection, and persistent counters.

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   `cd ComfyUI/custom_nodes/`
2. Clone this repository:
   `git clone https://github.com/chchchadzilla/ComfyUI-ChomfyNodes.git`
3. Restart ComfyUI.

---

## The Nodes

### 1. Chomfy Mega Wildcard Builder
A massive 24-slot prompt builder designed for complex, randomized prompt engineering.

*   **Setup:** You must place your `.txt` or `.csv` files inside the folder:  
    `ComfyUI-ChomfyNodes/wildcards/`
*   **Features:**
    *   **24 Independent Slots:** Each with its own ON/OFF toggle.
    *   **Modes:**
        *   `Random`: Picks a random line (seed varied).
        *   `Fixed`: Picks a specific line index.
        *   `Sequential Forward`: Walks through the file (Index 0, 1, 2...) as the image seed increments.
        *   `Sequential Reverse`: Walks backward through the file.
    *   **Joiner:** Custom delimiter text inserted between logic (e.g., `, ` or ` AND `).

### 2. Chomfy Forensic Saver
A robust image saver that logs *exactly* how the image was made for debugging and archival.

*   **Output Location:** Automatically saves to:  
    `ComfyUI-ChomfyNodes/outputs/`
*   **Drag & Drop:** Generates standard PNGs that restore the full node graph when dropped into ComfyUI.
*   **Sidecar JSON:** For every image, a `.json` file is generated containing:
    *   System Hardware (GPU model, VRAM, RAM, OS).
    *   Exact Model, LORA, and VAE filenames detected in the workflow.
    *   Latent Dimensions and Python/Torch versions.
    *   Full prompt API data.

### 3. Chomfy Universal Regional Noise
Injects controlled noise into specific regions of a latent image. Known to work with **Flux (16ch), SDXL (4ch), Wan 2.1 Video (5D), and GGUF/FP8** quantizations.

*   **No Empty Latent Needed:** Generates its own noise internally using the source image's data type.
*   **Usage:**
    1.  Define `X, Y, Width, Height` to create a box region.
    2.  Set `Strength` (e.g., 0.3 = 30% Noise / 70% Original).
    3.  Plug into a KSampler with low denoise to "hallucinate" new details inside that region.
*   **Mask Override:** Primarily a Box tool, but you can optionally plug a `MASK` into the override input to noise arbitrary shapes (circles, silhouettes, etc).

### 4. Chomfy Universal Counter
A persistent counter for time-lapses, iterating filenames, or logic gates.

*   **Modes:** Increment, Decrement, Random Step.
*   **Zero Padding:** Format your output automatically (e.g., `0001`, `0002`) for file sorting.
*   **Reset Toggle:** Flip the `reset` switch to force the counter back to start, then flip it off to resume counting.
*   **Counter ID:** Allows you to have multiple independent counters in one workflow, or keep your count memory safe even if you change step sizes.

---

## License

MIT License.

Copyright (c) 2025 Chad Keith

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.