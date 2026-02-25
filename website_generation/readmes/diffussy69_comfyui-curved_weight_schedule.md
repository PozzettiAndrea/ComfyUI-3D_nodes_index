# ComfyUI Curved Weight Schedule

Advanced ControlNet scheduling, temporal masking, regional prompting, and image utilities for ComfyUI. Control your ControlNet strength across time and space with precision and visual feedback, plus powerful masking and regional prompting tools.

## 🌟 Features

### ControlNet Scheduling
- **Curved ControlNet Scheduler**: Schedule ControlNet strength across generation steps with multiple curve types
- **Advanced Curved ControlNet Scheduler**: Feature-rich version with presets, custom formulas, curve blending, and more
- **Multi-ControlNet Curve Coordinator**: 🌟 Coordinate up to 4 ControlNet curves simultaneously with independent timing
- **Curved Blur Batch Preprocessor**: ⭐ Generate batches of progressively blurred images following curves
- **Batch Images to Timestep Keyframes**: ⭐ Map blur batches to ControlNet timestep keyframes
- **Redistribute Keyframe Percents**: 🔄 Redistribute keyframe timing while preserving curves
- **Curve Formula Builder**: Beginner-friendly pattern builder - select shapes and adjust sliders!
- **Visual Curve Designer**: Plot control points with numeric inputs for precise curves
- **Interactive Curve Designer**: 🎨 Draw curves with your mouse on an interactive canvas!
- **Visual Feedback**: Real-time graph preview showing your strength curve

### Temporal Masking (NEW! 🎭)
- **Multi-Mask Combiner (Batch)**: 🌟 Create temporal mask schedules where different masks are active at different generation stages
- **Apply CN Extras Masks**: Apply masks to per-keyframe control images
- **Extract First Keyframe Image**: Helper node for workflow compatibility
- **Complete Temporal Control**: Different masked regions active at 0-30%, 30-60%, 60-100% of generation
- **Smooth Transitions**: Optional fade-in/fade-out between mask regions
- **Visual Schedule**: See exactly which masks are active at each stage

### Regional Prompting & Masking
- **Multi-Layer Mask Editor**: 🎨 Interactive canvas-based mask editor with multiple layers
- **Multi-Mask Strength Combiner**: Apply different ControlNet strengths to different regions of your image
- **Regional Prompting**: Use different text prompts for different masked areas
- **Regional Prompt Interpolation**: Smooth gradient transitions between different prompts
- **Mask Symmetry Tool**: Mirror masks across axes for symmetrical compositions
- **Auto Person Mask**: AI-powered automatic person/foreground detection and masking
- **Auto Background Mask**: Automatic background masking (inverted person mask)

## 🎯 Choose Your Curve Creation Method

Different tools for different skill levels and preferences:

| Method | Best For | Skill Level | Interface |
|--------|----------|-------------|-----------|
| **Presets** | Quick workflows | 🟢 Beginner | Dropdown menu |
| **Curve Formula Builder** | Pattern-based curves | 🟢 Beginner | Sliders + patterns |
| **Visual Curve Designer** | Precise coordinates | 🟡 Intermediate | Number inputs |
| **Interactive Canvas** 🎨 | Drawing curves | 🟢 Beginner | Mouse drawing |
| **Custom Formulas** | Mathematical curves | 🔴 Advanced | Code/math |

**Recommendation:** Start with **Interactive Canvas** or **Presets** for the easiest experience!

## 📦 Installation

### Prerequisites

This package requires a **modified version** of Advanced ControlNet to support per-keyframe images for temporal masking.

### Option 1: Use Modified Fork (Recommended)

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/diffussy69/comfyui-curved_weight_schedule.git
```

3. Clone the **modified** Advanced ControlNet fork:
```bash
git clone https://github.com/diffussy69/ComfyUI-Advanced-ControlNet.git
cd ComfyUI-Advanced-ControlNet
git checkout per-keyframe-images
cd ..
```
> ⚠️ **Important:** Use the modified fork, not the original! The fork includes support for per-keyframe images required for temporal masking.

4. Install dependencies (if not already installed):
```bash
pip install matplotlib pillow numpy torch scipy
```

5. Restart ComfyUI


**That's it!** ✨ The JavaScript UI extension(s) are included automatically. Presets will update UI fields instantly with no additional setup required!

### 🎉 What You Get Out of the Box

When you select a preset:
- ✅ **All UI fields update automatically** - No manual adjustments needed
- ✅ **True one-click experience** - Select "Fade Out" and watch it apply instantly
- ✅ **Visual confirmation** - See exactly what values are being used
- ✅ **No confusion** - What you see is what you get!

### Verification

After installing and restarting:
1. Hard refresh browser (Ctrl+Shift+F5 / Cmd+Shift+R)
2. Add the Advanced Curved ControlNet Scheduler node
3. Select any preset (like "Fade Out")
4. Watch the UI fields update automatically! 🎊
5. Optional: Check browser console (F12) for success messages

The nodes will appear in:
- `conditioning/controlnet` → Curved ControlNet Scheduler, Advanced Curved ControlNet Scheduler, Multi-ControlNet Curve Coordinator, Curve Formula Builder, Visual Curve Designer, Interactive Curve Designer 🎨
- `ControlNet Preprocessors/tile` → Curved Blur (Batch) ⭐
- `ControlNet/Keyframing` → Batch Images to Timestep Keyframes, Redistribute Keyframe Percents 🔄, Apply CN Extras Masks, Extract First Keyframe Image
- `mask` → Multi-Layer Mask Editor 🎨, Multi-Mask Combiner (Batch) 🌟 NEW!, Multi-Mask Strength Combiner, Mask Symmetry Tool
- `conditioning` → Regional Prompting, Regional Prompt Interpolation

## 🎭 Temporal Masking Workflow (NEW!)

**Create different ControlNet influences at different stages of generation!**

### The Concept

Traditional masking: Same mask throughout entire generation
**Temporal masking**: Different masks active at different % of generation

### Example Use Cases

1. **Composition Lock → Detail Refinement**
   - 0-30%: Full control image (composition)
   - 30-60%: Face region only (character details)
   - 60-100%: Background region only (environment details)

2. **Sequential Region Focus**
   - 0-25%: Left side of image
   - 25-50%: Middle of image
   - 50-75%: Right side of image
   - 75-100%: Entire image

3. **Dynamic Attention**
   - 0-40%: Foreground subjects
   - 40-80%: Background environment
   - 80-100%: Fine details everywhere

### Basic Workflow

```
1. Multi-Layer Mask Editor
   ├─> Draw your masks (up to 10 layers)
   └─> Set temporal ranges (start_percent, end_percent per layer)
       
2. Multi-Mask Combiner (Batch)
   ├─> Receives masks from editor
   ├─> Generates N keyframes (usually 4)
   └─> Each keyframe = combined mask for that time period
   
3. Curved Blur (Batch) [optional]
   └─> Blur the masks if desired
   
4. Advanced Curved ControlNet Scheduler
   ├─> Creates base keyframes with timing
   └─> Stores masks in cn_extras
   
5. Redistribute Keyframe Percents
   ├─> Evenly spaces keyframes (0%, 25%, 50%, 75%, 100%)
   └─> Preserves curves and masks
   
6. Batch Images to Timestep Keyframes
   ├─> Adds your control images to keyframes
   └─> Preserves existing masks from scheduler
   
7. Apply CN Extras Masks
   ├─> Applies masks to control images
   └─> Creates per-keyframe masked images
   
8. Apply Advanced ControlNet
   └─> Uses different masked images at different times!
```

### Step-by-Step Example

**Goal:** Face controls early generation (0-30%), background controls late (60-100%)

1. **Multi-Layer Mask Editor:**
   - Layer 1: Paint face region
     - `start_percent_1`: 0.0
     - `end_percent_1`: 0.3
     - `strength_1`: 1.0
   - Layer 2: Paint background region
     - `start_percent_2`: 0.6
     - `end_percent_2`: 1.0
     - `strength_2`: 1.0
   - Click "Save Masks"

2. **Multi-Mask Combiner (Batch):**
   - Connect masks from editor
   - `num_keyframes`: 4
   - `combine_method`: "max"
   - Output: 4 masks (one for each time period)

3. **Advanced Curved ControlNet Scheduler:**
   - `num_keyframes`: 4
   - `batch_masks`: Connect from Multi-Mask Combiner
   - Creates keyframes with masks stored

4. **Redistribute Keyframe Percents:**
   - `timestep_keyframes`: From scheduler
   - `start_percent`: 0.0
   - `end_percent`: 1.0
   - `distribution`: "linear"
   - Redistributes to 0%, 33%, 67%, 100%

5. **Batch Images to Timestep Keyframes:**
   - `images`: Your control image(s)
   - `prev_timestep_kf`: From Redistribute node
   - Adds control images to keyframes

6. **Apply CN Extras Masks:**
   - `timestep_keyframes`: From Batch Images node
   - Applies masks to control images
   - Output: Per-keyframe masked images

7. **Apply Advanced ControlNet:**
   - `timestep_kf`: From Apply CN Extras Masks
   - `image`: Any image (placeholder, will use per-keyframe images)
   - During generation:
     - 0-33%: Uses masked face region
     - 33-67%: Transition
     - 67-100%: Uses masked background region

### Advanced Features

**Smooth Transitions:**
```
Layer settings:
- fade_in_percent: 0.05 (5% fade in at start)
- fade_out_percent: 0.05 (5% fade out at end)
```

**Combine Multiple Layers:**
```
- Layer 1: Face (0-30%)
- Layer 2: Hands (20-50%)  ← Overlaps with face
- Layer 3: Background (60-100%)
- combine_method: "max" → Takes strongest mask value
```

**Debug Output:**
```
print_schedule: true
→ Shows which masks are active at each keyframe
→ Helps verify your temporal scheduling
```

## 🎯 Node Overview

### 1. Curved ControlNet Scheduler (Original)

Control ControlNet strength across generation steps using mathematical curves.

**Key Parameters:**
- `num_keyframes`: Number of control points (2-100)
- `start_percent` / `end_percent`: When to start/stop the curve (0.0-1.0)
- `start_strength` / `end_strength`: Strength values at start and end (YOU control the direction)
- `curve_type`: Shape of the strength transition
- `curve_param`: Controls transition speed/steepness (higher = more extreme)
- `invert_curve`: Flip the curve shape

**Available Curve Types:**
- `linear`: Straight line transition
- `ease_in`: Slow start, fast end (accelerating)
- `ease_out`: Fast start, slow end (decelerating)
- `ease_in_out`: Slow start and end, fast middle (smooth S-curve)
- `sine_wave`: Oscillating control (experimental)
- `bell_curve`: Peak in middle, low at edges
- `reverse_bell`: Low in middle, high at edges
- `exponential`: Dramatic exponential curve
- `bounce`: Bouncing effect
- `custom_bezier`: Customizable bezier curve

**Outputs:**
- `TIMESTEP_KF`: Connect to Apply Advanced ControlNet's timestep_kf input
- `curve_graph`: Visual preview (connect to Preview Image)

### 2. Advanced Curved ControlNet Scheduler

Enhanced version with powerful new features for maximum control and flexibility.

**All Original Features Plus:**

#### 🎨 Preset System
- **9 Pre-configured Presets**: Quick one-click setups (with optional JS extension for automatic UI updates!)
  - `Fade Out`: Strong start → weak end (composition lock)
  - `Fade In`: Weak start → strong end (detail refinement)
  - `Peak Control`: Peaks in middle (bell curve strength)
  - `Valley Control`: Strong edges, weak middle
  - `Strong Start+End`: Bookend control
  - `Oscillating`: Wave pattern control
  - `Exponential Decay`: Dramatic fade
  - `Smooth Transition`: Gentle S-curve
  - `Custom`: Manual configuration

> **💡 Pro Tip:** Install the JavaScript extension (see Installation section) to make presets automatically update all UI fields for a truly seamless experience!

#### 🔢 Advanced Easing Functions
- **Professional animation easing curves**:
  - `ease_in/out/in_out_quad` (quadratic)
  - `ease_in/out/in_out_cubic` (cubic)
  - `ease_in/out/in_out_quart` (quartic)
- More precise control over acceleration/deceleration

#### 🧮 Custom Formula Support
- **Mathematical Expression Input**
  - Use custom formulas with variable `t` (0 to 1)
  - Examples: `sin(t*3.14)`, `t**2`, `1-exp(-5*t)`
  - Safe evaluation with whitelisted functions
  - Supports: sin, cos, tan, exp, log, sqrt, abs, pi, e, numpy operations

#### 🎛️ Curve Modulation
- **Mirror Curve**: Create symmetrical curves around midpoint
- **Repeat Curve**: Repeat the pattern 1-10 times for multi-segment control
- **Adaptive Keyframes**: Automatically place more keyframes where curve changes rapidly
- **Curve Blending**: Mix two different curve types
  - Blend between any two curve types
  - Adjustable blend amount (0.0-1.0)

#### 📊 Enhanced Features
- **A/B Comparison**: Show two curves side-by-side for visual comparison
- **CSV Export**: Save curve data for reuse and sharing
- **Curve Statistics Output**: Detailed stats (average, max, min, area under curve, rate of change)
- **Step Mode**: Use absolute steps instead of percentages
- **Comparison Graphs**: Overlay multiple curves for testing
- **Temporal Mask Support** 🌟: Accept batch masks for per-keyframe masking

**New Parameters:**
- `preset`: Quick preset selection
- `mode`: "percent" or "steps"
- `total_steps`: For step mode (1-10000)
- `batch_masks` 🌟: Optional mask batch for temporal masking
- `custom_formula`: Mathematical expression using `t` variable
- `blend_curve_type` & `blend_amount`: For curve blending
- `mirror_curve` & `repeat_curve`: Pattern modulation
- `adaptive_keyframes`: Smart keyframe distribution
- `comparison_curve`: Second curve for A/B testing
- `save_curve` & `curve_filename`: CSV export settings
- And all original parameters!

**Outputs:**
- `TIMESTEP_KF`: Keyframes with optional masks in cn_extras
- `curve_graph`: Visual preview
- `curve_stats`: Statistical information

### 3. Multi-Mask Combiner (Batch) 🌟 NEW!
<img width="1642" height="816" alt="image" src="https://github.com/user-attachments/assets/e289915d-8d9f-4508-bcfa-f58b0e0bbc02" />


Create temporal mask schedules where different regions are active at different generation stages.

**Purpose:** Generate a batch of masks, each representing which regions should be active at that point in generation.

**Key Features:**
- **Up to 10 independent layers** with individual temporal ranges
- **Per-layer timing:** Each layer has start_percent and end_percent
- **Fade transitions:** Optional fade_in and fade_out for smooth blending
- **Visual schedule:** Graph showing when each layer is active
- **Multiple combine methods:** max, add, multiply, screen, overlay
- **Debug output:** Detailed frame-by-frame breakdown

**Parameters:**
- `mask_1` through `mask_10`: Input masks for each layer
- `strength_1` through `strength_10`: Opacity/intensity (0.0-1.0)
- `start_percent_1` through `start_percent_10`: When layer becomes active (0.0-1.0)
- `end_percent_1` through `end_percent_10`: When layer becomes inactive (0.0-1.0)
- `fade_in_percent`: Fade duration at start of active period
- `fade_out_percent`: Fade duration at end of active period
- `num_keyframes`: Number of output masks to generate (2-100)
- `combine_method`: How to blend overlapping layers
  - `max`: Take brightest value (recommended)
  - `add`: Add values (can exceed 1.0)
  - `multiply`: Multiply values
  - `screen`: Screen blend mode
  - `overlay`: Overlay blend mode
- `normalize`: Clamp output values to 0.0-1.0
- `print_schedule`: Show detailed frame breakdown in console

**Outputs:**
- `mask_batch`: Batch of N masks (MASK format)
- `schedule_graph`: Visual timeline showing layer activity
- `schedule_info`: Text description of schedule

**Workflow Position:**
```
Multi-Layer Mask Editor → Multi-Mask Combiner (Batch) → Advanced Curved ControlNet Scheduler
```

### 4. Redistribute Keyframe Percents 🔄 NEW!

Redistribute keyframe start_percent values while preserving all other properties.

**Purpose:** Fix keyframe timing without losing curves, weights, or other data.

**Use Case:** Your scheduler creates keyframes but they all start at 0%. This node spreads them evenly across the timeline (0%, 25%, 50%, 75%, 100%) while keeping everything else intact!

**Key Features:**
- **Preserves everything:** Curves, weights, masks, images, all properties
- **Only changes start_percent:** Redistributes timing across timeline
- **Multiple distributions:** Linear, ease_in, ease_out
- **Range control:** Distribute across any percent range (e.g., 0.2-0.8)

**Parameters:**
- `timestep_keyframes`: Input keyframes to redistribute
- `start_percent`: Start of distribution range (0.0-1.0)
- `end_percent`: End of distribution range (0.0-1.0)
- `distribution`: How to space keyframes
  - `linear`: Evenly spaced (recommended)
  - `ease_in`: More keyframes at start
  - `ease_out`: More keyframes at end
- `print_schedule`: Show before/after timing

**Outputs:**
- `timestep_kf`: Keyframes with redistributed timing
- `info`: Summary of redistribution

**Why You Need This:**
Many schedulers create keyframes with `start_percent=0.0` for all of them, meaning they're all active from the beginning. This node fixes that by spreading them across the timeline so they activate sequentially!

### 5. Batch Images to Timestep Keyframes

Maps a batch of images to timestep keyframes, storing each image in the corresponding keyframe's cn_extras.

**Purpose:** Add per-keyframe images (like blurred control images or masked versions) to your keyframes.

**Key Features:**
- **Automatic format conversion:** Converts images from ComfyUI format (NHWC) to ControlNet format (NCHW)
- **Preserves existing data:** Keeps masks and other cn_extras from previous nodes
- **Smart merging:** Adds images without overwriting existing cn_extras content
- **Compatibility:** Works across different Advanced ControlNet versions

**Parameters:**
- `images`: Batch of images (K images for K keyframes)
- `prev_timestep_kf`: Existing keyframes to add images to
- `print_keyframes`: Show which image maps to which keyframe

**Outputs:**
- `timestep_kf`: Keyframes with images added to cn_extras
- `info`: Mapping summary

**Workflow Position:**
```
Control Images → Batch Images to Timestep Keyframes → Apply CN Extras Masks
```

### 6. Apply CN Extras Masks NEW!

Applies masks to images within keyframe cn_extras, creating per-keyframe masked control images.

**Purpose:** Multiply each keyframe's image by its mask, creating the final masked control images.

**Key Features:**
- **Smart format handling:** Auto-detects and converts between HWC and NCHW formats
- **Dimension verification:** Checks that masks and images match before applying
- **Preserves keyframes:** Clones keyframes to avoid modifying originals
- **Optional inversion:** Can invert masks before applying

**Parameters:**
- `timestep_keyframes`: Keyframes with both masks and images in cn_extras
- `invert_mask`: Invert mask values before applying (black↔white)
- `print_debug`: Show detailed processing information

**Outputs:**
- `timestep_kf`: Keyframes with masked images in cn_extras
- `info`: Processing summary

**How It Works:**
1. For each keyframe with cn_extras containing both 'mask' and 'image'
2. Convert image to HWC format for processing
3. Expand mask to match image channels
4. Multiply: masked_image = image * mask
5. Convert back to NCHW format
6. Store in cn_extras['image']

**Workflow Position:**
```
Batch Images to Timestep Keyframes → Apply CN Extras Masks → Apply Advanced ControlNet
```

### 7. Extract First Keyframe Image

Helper node that extracts the first image from keyframes to use as a placeholder.

**Purpose:** Apply Advanced ControlNet requires an image input, but when using per-keyframe images, that input is just a placeholder. This node extracts the first per-keyframe image for that purpose.

**Parameters:**
- `timestep_keyframes`: Keyframes with images in cn_extras
- `fallback_image`: Optional backup image if no keyframe images found

**Outputs:**
- `image`: First keyframe image (or fallback)
- `info`: Which image was extracted

**Usage:**
```
Apply CN Extras Masks ───┬──→ Apply Advanced ControlNet (timestep_kf)
                         │
                         └──→ Extract First Keyframe Image
                                   ↓
                              Apply Advanced ControlNet (image)
```

### 8. Curved Blur (Batch)

Generate batches of progressively blurred images following a curve.

**Use Cases:**
- Sync blur progression with ControlNet strength curves
- Lock composition early, allow creative freedom late
- Create smooth transitions from sharp to blurred
- Perfect for tile ControlNet workflows

**Parameters:**
- `image`: Source image to blur
- `num_keyframes`: How many blurred versions to generate
- `start_sigma` / `end_sigma`: Blur range (0.0-32.0)
- `curve_type`: Same curves as scheduler
- `curve_param`: Curve steepness control
- `show_graph`: Visualize blur progression

**Outputs:**
- `batch_images`: Batch of blurred images
- `curve_graph`: Visual preview
- `stats`: Blur values used

**Example Workflow:**
```
Image → Curved Blur (Batch) → Batch Images to Timestep Keyframes → Apply Advanced ControlNet
```

### 9. Multi-ControlNet Curve Coordinator

Coordinate multiple ControlNet curves simultaneously with independent timing.

**Key Features:**
- **Up to 4 independent slots** for different ControlNets
- **Per-slot timing:** Each slot has its own start_percent and end_percent
- **All curve types:** Full curve library per slot
- **Visual coordination:** See how curves interact
- **Shaded active windows:** Visual timing indicators

**Use Cases:**
- **Sequential control:** Different CNs at different stages
- **Overlapping transitions:** Smooth handoffs between controls
- **Targeted bursts:** Activate specific CNs only when needed
- **Coordinated effects:** Visualize multiple curve interactions

**Parameters:**
- Slot 1-4 sections with independent:
  - `enable`: Turn slot on/off
  - `start_percent` / `end_percent`: When this CN is active
  - `start_strength` / `end_strength`: Strength values
  - `curve_type` / `curve_param`: Curve shape
- `num_keyframes`: Total keyframes to generate
- `show_graphs`: Visual preview per slot

**Outputs:**
- `TIMESTEP_KF_1` through `TIMESTEP_KF_4`: Individual keyframe streams
- `combined_graph`: All curves on one chart

[Rest of the README continues with sections 10-16 as before, unchanged]

## 🎨 Workflow Examples

### Example 1: Basic Temporal Masking

**Goal:** Face controls early (0-30%), background controls late (60-100%)

```
[Multi-Layer Mask Editor]
├─ Layer 1: Face region (0.0-0.3)
└─ Layer 2: Background region (0.6-1.0)
      ↓
[Multi-Mask Combiner (Batch)]
num_keyframes: 4
      ↓
[Advanced Curved ControlNet Scheduler]
batch_masks: connected
      ↓
[Redistribute Keyframe Percents]
Spreads to 0%, 33%, 67%, 100%
      ↓
[Your Control Image]
      ↓
[Batch Images to Timestep Keyframes]
      ↓
[Apply CN Extras Masks]
      ↓
[Apply Advanced ControlNet]
```

Result:
- 0-33%: Face region controls generation
- 33-67%: Transition period
- 67-100%: Background region controls generation

### Example 2: Sequential Regional Focus

**Goal:** Left→Middle→Right progression

```
[Multi-Layer Mask Editor]
├─ Layer 1: Left region (0.0-0.33)
├─ Layer 2: Middle region (0.33-0.66)
└─ Layer 3: Right region (0.66-1.0)
      ↓
[Multi-Mask Combiner (Batch)]
num_keyframes: 6
combine_method: max
      ↓
[Rest of workflow as above]
```

### Example 3: Blurred + Temporal Masking

**Goal:** Blurred background early, sharp face details late

```
[Your Control Image]
      ↓
[Curved Blur (Batch)]
start_sigma: 0.0
end_sigma: 10.0
curve_type: linear
      ↓
[Multi-Mask Combiner (Batch)]
├─ Layer 1: Full image (0.0-0.5)
└─ Layer 2: Face only (0.5-1.0)
      ↓
[Advanced Curved ControlNet Scheduler]
batch_masks: connected
      ↓
[Redistribute Keyframe Percents]
      ↓
[Batch Images to Timestep Keyframes]
images: from Curved Blur
      ↓
[Apply CN Extras Masks]
      ↓
[Apply Advanced ControlNet]
```

Result:
- 0-50%: Entire control image, progressively less blurred
- 50-100%: Sharp face details only

## 🔧 Troubleshooting

**Issue: Temporal masks not working/all look the same**
- Solution:
  - Verify you're using the **modified** Advanced ControlNet fork
  - Check that masks have different start_percent and end_percent values
  - Ensure Redistribute Keyframe Percents is spreading timing correctly
  - Look for `[DEBUG] Keyframe changed` messages in console
  - Verify Apply CN Extras Masks shows "Processed N keyframes"

**Issue: "Could not import TimestepKeyframe" error**
- Solution:
  - Make sure Advanced ControlNet is installed (either fork or original)
  - If using original, make sure you applied the manual patches
  - Restart ComfyUI after installation

**Issue: Workflow won't execute - needs image input**
- Solution:
  - Use Extract First Keyframe Image node to get a placeholder image
  - OR just connect any image to the required input - per-keyframe images will override it

**Issue: Images all black/white after applying masks**
- Solution:
  - Check your mask values (white=keep, black=remove)
  - Try `invert_mask=true` in Apply CN Extras Masks
  - Verify masks match image dimensions

**Issue: Keyframes not switching during generation**
- Solution:
  - Make sure you used Redistribute Keyframe Percents
  - Check console for `[DEBUG prepare_current_keyframe]` messages
  - Verify keyframes have different start_percent values

**Issue: Same image used throughout generation**
- Solution:
  - This was the original bug! Make sure you're using control.py with cache invalidation
  - Look for `[DEBUG] Keyframe changed from X to Y - invalidating cond_hint cache`
  - If not seeing those messages, you need the updated control.py

**Issue: Custom formula not working**
- Solution:
  - Check syntax - must use `t` as variable (not `x` or other)
  - Ensure parentheses are balanced
  - Avoid forbidden operations (import, exec, eval)
  - Test with simple formulas first: `t**2`, `sin(t*3.14)`

**Issue: Preset UI fields not updating**
- Solution: Make sure you restarted ComfyUI after installation
  - Hard refresh browser (Ctrl+Shift+F5 / Cmd+Shift+R)  
  - Check browser console (F12) - you should see `✅ Node patched successfully!`
  - If you don't see that message, the extension may not have loaded
  - Verify `/web/advanced_curved_scheduler.js` exists in your node folder
- Alternative: Presets still work without UI updates - values are applied internally

**Issue: Masks not affecting output**
- Solution:
  - Check that masks are actually painted (not empty)
  - Verify mask is connected to correct input
  - Try increasing strength values
  - Verify Advanced ControlNet base strength is 1.0

**Issue: Effect too weak everywhere**
- Solution:
  - Check Advanced ControlNet `strength` setting (should be 1.0)
  - Increase `start_strength` and `end_strength` values in scheduler
  - Increase individual mask strengths in Multi-Mask Combiner
  - For blur workflows: decrease sigma values (more sharp = more control)

**Issue: Effect too strong everywhere**
- Solution:
  - Decrease `start_strength` and `end_strength` values
  - Decrease individual mask strengths in Multi-Mask Combiner
  - Check that Advanced ControlNet strength isn't multiplying your values
  - For blur workflows: increase sigma values (more blur = less control)

## 📋 Requirements

- ComfyUI
- **ComfyUI-Advanced-ControlNet** (modified fork with per-keyframe image support - required for temporal masking)
  - Original Advanced ControlNet works for non-temporal features
  - Modified fork required only for temporal masking features
- Python packages: matplotlib, pillow, numpy, torch, scipy

## 🆕 What's New

### Version 4.0 - Temporal Masking System 🎭

- **🌟 MAJOR: Temporal Mask Scheduling** - Different masks at different generation stages!
  - Control which regions are active at 0-30%, 30-60%, 60-100% of generation
  - Smooth transitions between temporal regions
  - Per-layer fade-in and fade-out support
  - Visual timeline showing mask activity
  
- **🎭 Multi-Mask Combiner (Batch)** - Create temporal mask schedules
  - Up to 10 independent layers with individual timing
  - Per-layer start_percent and end_percent
  - Multiple combine methods (max, add, multiply, screen, overlay)
  - Detailed debug output and visual schedule graph
  
- **🔄 Redistribute Keyframe Percents** - Fix keyframe timing
  - Redistributes start_percent values while preserving everything else
  - Keeps curves, weights, masks, images intact
  - Multiple distribution modes (linear, ease_in, ease_out)
  - Essential for making temporal masks work correctly
  
- **🖼️ Apply CN Extras Masks** - Apply masks to per-keyframe images
  - Smart format handling (HWC ↔ NCHW)
  - Dimension verification
  - Optional mask inversion
  - Creates final masked control images
  
- **📤 Extract First Keyframe Image** - Helper for workflow compatibility
  - Extracts first per-keyframe image as placeholder
  - Solves required image input issue
  - Clean workflow integration
  
- **⚙️ Modified Advanced ControlNet Integration**
  - Fork includes per-keyframe image support
  - Automatic cache invalidation when keyframes switch
  - Backward compatible with existing workflows
  - See MODIFICATIONS.md for technical details

- **🎯 Complete Workflow Integration**
  - Seamless integration with existing schedulers
  - Works with all curve types and presets
  - Compatible with blur batch workflows
  - Enhanced debug output for troubleshooting

- **📚 Comprehensive Documentation**
  - Detailed temporal masking guide
  - Step-by-step workflow examples
  - Troubleshooting section
  - Technical explanation of system architecture

### Version 3.3 - Multi-ControlNet Coordination 🎯
- **🌟 MAJOR: Multi-ControlNet Curve Coordinator** - Coordinate multiple ControlNets simultaneously!
  - Manage up to 4 independent ControlNet curves in one node
  - **Per-slot timing**: Each slot has its own start_percent and end_percent
  - Visual dividers for clean organization
  - Combined graph with shaded active windows
  - All curve types and presets available per slot
  - Perfect for complex multi-ControlNet workflows
- **✨ Use Cases**:
  - Sequential control: Different CNs at different stages
  - Overlapping transitions: Smooth handoffs between controls
  - Targeted bursts: Activate specific CNs only when needed
  - Coordinated effects: Visualize how multiple curves interact
- **🐛 Bug Fixes**:
  - Fixed bell_curve and oscillating presets (were showing flat lines)
  - Updated all curve presets to use proper start/end strength values

### Version 3.2 - Dynamic Blur Workflow 🌊
- **🌊 MAJOR: Curved Blur Batch Preprocessor** - Sync blur with ControlNet scheduling!
  - Generate batches of progressively blurred images following curves
  - Gaussian blur with proper 3-sigma kernels and reflect padding
  - Full curve type support matching the scheduler
  - Visual graph preview of blur progression
  - Sigma range from 0.0 (sharp) to 32.0+ (extreme blur)
  - Perfect for tile ControlNet workflows
- **🔗 Batch Images to Timestep Keyframes** - The missing link!
  - Maps blur batches directly to ControlNet keyframes
  - Automatic API compatibility across different Advanced ControlNet versions
  - Smart warnings for mismatched keyframe counts
  - Seamless integration with existing workflow
- **🎯 Complete Workflow Integration**:
  - Synchronize blur progression with strength curves
  - Lock composition early, creative freedom late
  - Or reverse: rough start, detailed refinement
  - Mix and match curve types for blur vs strength
- **⚡ Technical Improvements**:
  - Robust fallback handling for TimestepKeyframe imports
  - Better error messages and user warnings
  - Improved graph generation with graceful failure handling
  - Zero blur (sigma=0) optimization

### Version 3.0 - Interactive Curve Designer 🎨
- **🎨 MAJOR: Interactive Curve Designer** - Draw curves with your mouse!
  - Click and drag interface on an interactive canvas
  - Real-time curve preview as you draw
  - Visual control points with coordinate labels
  - Quick actions: Symmetry, Invert, Clear, Reset
  - Multiple interpolation methods
  - Auto-generates formulas from your drawings
  - **The most intuitive way to create curves!**
- **📊 Visual Curve Designer** - Point-based curve creation
  - Define up to 10 control points with numeric inputs
  - Three interpolation methods (linear, spline, cubic)
  - Precise coordinate control
  - Perfect for mathematical precision
- **🐛 Bug Fixes**:
  - Fixed bell curve and sine wave presets (were showing flat lines)
  - Improved preset handling for pattern-based curves
  - Better normalization for oscillating curves

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new curve types, presets, or features
- Request improvements
- Submit pull requests
- Share your custom formulas and workflows
- Help improve temporal masking features

## 📄 License

MIT License - feel free to use and modify!

## 🙏 Credits

Created with assistance from Claude (Anthropic). Special thanks to the ComfyUI and Advanced ControlNet communities.

Special thanks to Kosinkadink for the amazing Advanced ControlNet extension that made temporal masking possible!

---

**Enjoy creating with precise control over every aspect of your generation!** 🎨✨

If you find this useful, consider starring the repo and sharing your creations!

### 🔗 Links
- [Advanced ControlNet (Modified Fork)](https://github.com/diffussy69/ComfyUI-Advanced-ControlNet.git) - Required for temporal masking
- [Advanced ControlNet (Original)](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet) - Original dependency
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - The amazing UI this runs on

---

**Version:** 4.0 (Temporal Masking System! 🎭)
