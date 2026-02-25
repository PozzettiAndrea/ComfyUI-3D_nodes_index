===============================================================================
                          EARTHBOUND ULTIMATE (MASTER)
===============================================================================

Earthbound Ultimate is a comprehensive "Power Node" for ComfyUI that integrates 
the entire image generation and editing pipeline into a single interface. 
This node manages model merging, LoRA application, latent manipulation, 
and professional-grade post-processing.

MAKE SURE THAT THE NODE IS PUT UNDER CUSTOM_NODES IN A FOLDER NAMED "ultimate node"

-------------------------------------------------------------------------------
1. CORE ARCHITECTURE & FEATURES
-------------------------------------------------------------------------------

* Normalized Model Merger: Blend up to 5 Checkpoints with internal normalization.
* Integrated LoRA Stack: Apply up to 3 LoRAs directly to the merged model.
* Expanded Input Suite: Support for ControlNet, Masking, and Latent Upscaling.
* Optimized GPU Post-Processing: High-performance effect chain with blur caching.
* Auto-Precision System: Optional FP16 toggle to reduce VRAM usage.
* Recipe Persistence: 100-slot save/load system for configurations.

-------------------------------------------------------------------------------
2. TECHNICAL DETAILS: HOW IT WORKS
-------------------------------------------------------------------------------

--- MODEL MERGING LOGIC ---
The node uses a "Normalized Blending" algorithm. Unlike standard mergers that 
can "blow out" weights when summing multiple models, Earthbound Ultimate 
calculates the total sum of all active checkpoint strengths and calculates a 
proportional ratio for each. This ensures the UNet remains stable regardless 
of how many models are stacked. LoRAs are applied immediately after this 
merger to the final patched model and CLIP.

--- THE EXECUTION PIPELINE ---
1. Initialization: Load or Merge Checkpoints -> Apply LoRA Stack.
2. Conditioning: Encode Positive/Negative prompts -> Apply ControlNet (optional).
3. Latent Phase: Create Latent -> Apply Mask (optional) -> KSampler Generation.
4. Latent Scaling: Apply Latent Upscale (Hi-Res Fix logic) if factor > 1.0.
5. Pixel Conversion: VAE Decode -> Pixel Upscale.
6. Effect Chain: Precision Conversion -> Effect Stack -> Color Grading -> Grain.

--- POST-PROCESSING MATHEMATICS ---
* Style Morph: Uses a Dual-Gaussian Blur technique. Negative values lerp 
  the image toward a 5x5 blur while adding edge-detected sharpening to 
  maintain "painterly" structure. Positive values amplify high-frequency 
  deviations from a 5x5 blurred base.
* Texture Pop & Clarity: Uses High-Pass filtering and Mid-tone contrast 
  stretching to accentuate surface micro-details without crushing blacks.
* Chromatic Aberration: Performs a pixel-shift roll on the Red and Blue 
  channels independently in the tensor space before recombining.
* Color Grading: Operates in a linear power space to ensure adjustments 
  do not cause digital clipping or "flat" colors.

-------------------------------------------------------------------------------
3. WORKFLOW INTEGRATION (HOW TO USE)
-------------------------------------------------------------------------------

To add Earthbound Ultimate to your workflow, right-click the workspace and 
navigate to: Earthbound -> Earthbound Ultimate.

--- INPUT DIRECTIONS ---
1. (Standard) Select your primary checkpoint in the 'ckpt 1' dropdown.
2. (Advanced) If you have models already loaded via other nodes, connect them 
   to the 'model in', 'clip in', and 'vae in' optional inputs.
3. (ControlNet) Connect a 'CONTROL_NET' and 'IMAGE' to the optional inputs to 
   enable guided generation.

--- OUTPUT DIRECTIONS ---
1. IMAGE: Connect this to a 'Save Image' or 'Preview Image' node.
2. MODEL / CLIP / VAE: These outputs provide the fully merged/patched versions.

-------------------------------------------------------------------------------
4. TROUBLESHOOTING
-------------------------------------------------------------------------------

* "ModuleNotFoundError: No module named 'comfy_extras'": 
  Ensure you are using a standard ComfyUI installation for upscaling support.
  
* Node appears red: 
  Update your Python environment (torch/torchvision) via requirements.txt.
  
* Recipe not saving: 
  Ensure the 'ComfyUI/input/' folder is writable.

-------------------------------------------------------------------------------
5. RECIPE SYSTEM
-------------------------------------------------------------------------------
- To Save: Select "Save current as Slot", choose Slot (1-100), and Queue Prompt.
- To Load: Select "Apply", choose the target Slot, and Queue Prompt.

-------------------------------------------------------------------------------
6. LICENSE
-------------------------------------------------------------------------------
Copyright (c) 2024 EarthboundAI aka J.Ramsey.

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
===============================================================================

