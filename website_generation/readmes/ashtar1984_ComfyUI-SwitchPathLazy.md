# Switch Path (Lazy)

A simple and efficient path switch for ComfyUI using native **lazy evaluation**.

### Features
- Chooses between two paths based on a boolean `state`.
- The **inactive branch is never executed** → perfect for skipping heavy nodes like Ollama Generate, API calls, etc.
- Live display on the node showing current state and active path.
- No external dependencies (works with vanilla ComfyUI).

### Installation
1. Go to your `ComfyUI/custom_nodes/` folder.
2. Clone this repo:
   ```bash
   git clone https://github.com/ashtar1984/ComfyUI-SwitchPathLazy.git
