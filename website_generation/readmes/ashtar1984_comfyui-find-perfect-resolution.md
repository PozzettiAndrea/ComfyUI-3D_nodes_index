# comfyui-find-perfect-resolution
This custom ComfyUI node, Find Perfect Resolution, calculates an optimal output resolution for an input image while preserving its aspect ratio and ensuring dimensions are divisible by a specified value. It is designed to work seamlessly in ComfyUI workflows, particularly for resizing images with nodes like "Resize Image v2".

# Features
## Input: 
Accepts an image (from a "Load Image" node) to determine the original dimensions and aspect ratio.
## User Parameters:
- desired_width and desired_height: Target resolution set by the user (default: 512x512, range: 64–4096).
- divisible_by: Ensures output dimensions are divisible by this value (default: 16, range: 1–64).

## Output: 
Returns two integers (width, height) representing the calculated resolution, maintaining the original aspect ratio and adhering to the divisible_by constraint.
## Logic: 
- Computes the target pixel count from the desired width and height.
- Calculates the new height using: round(sqrt((target_pixels * orig_height) / orig_width) / divisible_by) * divisible_by.
- Calculates the new width using: round((orig_width / orig_height) * sqrt((target_pixels * orig_height) / orig_width) / divisible_by) * divisible_by.

## Category: 
Listed under "utils" in ComfyUI's node menu.

# Use Case
Ideal for workflows requiring precise image resizing while maintaining aspect ratio and ensuring dimensions meet specific divisibility requirements (e.g., for compatibility with H.264 encoding or other processing constraints).Installation

- Place the FindPerfectResolution folder in ComfyUI/custom_nodes/.
- Restart ComfyUI to load the node.
- Find the node under the "utils" category and connect it to your workflow.

# Example Workflow
- Connect a "Load Image" node to the image input.
- Set desired_width, desired_height, and divisible_by as needed.
- Use the output width and height in a "Resize Image v2" node for further processing.

# Greetings to #Verole for the logical behind the scene.

