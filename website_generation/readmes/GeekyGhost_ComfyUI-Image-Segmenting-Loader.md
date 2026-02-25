\# Geeky Qwen Edit - ComfyUI Segmentation \& Effects Suite



Interactive image segmentation, advanced effects processing, and composition nodes optimized for workflow efficiency and transparency handling.



\## Nodes Included



\### 🎯 Qwen Segment Loader

Interactive image segmentation with real-time coordinate preview.



\*\*Features:\*\*

\- Visual coordinate grid with customizable spacing

\- Auto-updating preview when parameters change

\- Selection rectangle with corner markers

\- Info panel showing selection details

\- Outputs clean cropped segments (no padding)



\*\*How to Use:\*\*

1\. Upload your image

2\. Connect `coordinate\_preview` output to a Preview Image node

3\. Adjust coordinates (X, Y, width, height) and grid spacing

4\. Run workflow to see updated grid preview

5\. Fine-tune coordinates based on visual feedback

6\. Process the segment with your editing nodes



\*\*Outputs:\*\*

\- `original\_image`: Full original image

\- `segment\_image`: Cropped segment (exact size, no padding)

\- `segment\_metadata`: JSON data for compositor

\- `coordinate\_preview`: Visual grid preview



\### ✨ Qwen Effects

Advanced effects processor optimized for images with alpha channels/transparent backgrounds.



\*\*Effects Available:\*\*



\*\*Drop Shadow:\*\*

\- Customizable offset, blur, opacity, and color

\- Works perfectly with transparent images



\*\*Outer Glow:\*\*

\- Adjustable radius, intensity, and color

\- Creates beautiful glow effects around transparent objects



\*\*Stroke/Outline:\*\*

\- Variable width and color options

\- Clean outlines that follow alpha channel



\*\*Color Adjustments:\*\*

\- Brightness, contrast, saturation controls

\- Hue shifting (-180° to +180°)



\*\*Blur \& Sharpen:\*\*

\- Gaussian blur with alpha preservation

\- Customizable sharpening strength



\*\*Artistic Effects:\*\*

\- Emboss with strength control

\- Edge enhancement

\- Posterize with level control

\- Noise addition



\*\*Advanced Effects:\*\*

\- Color overlay with blend modes (normal, multiply, screen, overlay, soft light, hard light)

\- Vignette with customizable strength and radius

\- All effects preserve transparency



\*\*Perfect For:\*\*

\- Post-processing background-removed images

\- Enhancing segments from Geeky RemBG nodes

\- Adding professional effects to transparent objects

\- Creating composite-ready elements



\### 🔧 Qwen Compositor

Smart compositor that handles alpha channels and properly positions edited segments.



\*\*Features:\*\*

\- \*\*Full Alpha Channel Support\*\*: Properly handles RGBA images from effects processing

\- Automatic scaling and positioning from metadata

\- Multiple blend modes (normal, multiply, screen, overlay, soft light)

\- Opacity control and edge feathering

\- \*\*Transparency-Aware\*\*: Works seamlessly with background-removed images



\*\*Blend Modes:\*\*

\- Normal: Standard compositing

\- Multiply: Darkening blend

\- Screen: Lightening blend  

\- Overlay: Contrast enhancement

\- Soft Light: Subtle lighting effects



\## Typical Workflows



\### Basic Segmentation Workflow:

```

Image Input → Qwen Segment Loader → \[Your Editing Nodes] → Qwen Compositor → Final Output

```



\### With Background Removal \& Effects:

```

Image Input → Qwen Segment Loader → RemBG Node → Qwen Effects → Qwen Compositor → Final Output

```



\### Professional Effects Chain:

```

Segment → RemBG → Effects (Drop Shadow + Glow + Color Adjust) → Compositor

```



\## Alpha Channel Handling



This suite is specifically designed to work with transparent images:



\- \*\*Segment Loader\*\*: Outputs clean segments ready for alpha processing

\- \*\*Effects Node\*\*: All effects preserve and enhance alpha channels

\- \*\*Compositor\*\*: Intelligent alpha compositing with proper blending



\## Grid Preview Features



The coordinate preview shows:

\- White grid lines with customizable spacing (25-200px)

\- Gold coordinate numbers on all edges

\- Bright pink selection rectangle with corner markers

\- Info panel showing selection details and grid spacing

\- Auto-update status indicator



\## Tips for Best Results



1\. \*\*Use the coordinate preview\*\* to precisely select your areas of interest

2\. \*\*Enable auto-preview\*\* for real-time feedback while adjusting coordinates

3\. \*\*Chain effects\*\* in the Effects node for complex processing

4\. \*\*Experiment with blend modes\*\* in the compositor for creative results

5\. \*\*Use alpha-aware workflows\*\* for professional transparency handling



\## Compatibility



\- Works with all standard ComfyUI image formats

\- Optimized for transparency and alpha channels

\- Compatible with background removal nodes

\- No conflicts with existing ComfyUI nodes



\## Requirements



See `requirements.txt` for dependencies:

\- Pillow>=9.0.0

\- torch>=1.13.0 

\- numpy>=1.20.0

