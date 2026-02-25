**README.md**

# ComfyUI-PainterFrameCount

Aligns any input frame number to the nearest 4N+1 format (e.g., 120→121, 122→125), ensuring compatibility with video generation models that require specific frame count constraints.

## Input
- **frame_number** (INT): Input frame count from upstream node (force input)

## Output
- **aligned_frame** (INT): Frame count rounded up to nearest 4N+1 value

## Example
Input: 120 → Output: 121  
Input: 122 → Output: 125  
Input: 124 → Output: 125  
Input: 125 → Output: 125


