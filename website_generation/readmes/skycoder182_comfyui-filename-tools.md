# ComfyUI Filename Tools

## Extract Trim Filename Node

Extract filenames from full paths and optionally trim them using a marker.
Removes file extensions automatically.

Example:
Input: `C:/Images/photo_upscaled_v1.png`, Marker: `_upscaled` → Output: `photo`

## LoadImageWithFilename Node

This node loads an image from the ComfyUI input folder and extracts a cleaned version of the filename.

### Features:
- **Returns the image, image path, and a cleaned filename.**
- Automatically removes a trailing number in parentheses from the filename, e.g., `"ImageName (2)"` → `"ImageName"`.
- Optionally trims the filename at a specified marker string (the trim marker), removing the marker and everything after it.

### Input Parameters

| Parameter    | Type   | Description                                                                |
|--------------|--------|----------------------------------------------------------------------------|
| image        | STRING | Filename as available in the ComfyUI input folder                          |
| trim_marker  | STRING | (Optional) A string marker; if present, the name will be trimmed at marker |

### Examples

| Original Filename          | trim_marker      | Resulting Name   |
|---------------------------|------------------|------------------|
| `photo_upscaled (2).png`  | `_upscaled`      | `photo`          |
| `Vacation23-RAW (1).jpg`  | `-RAW`           | `Vacation23`     |
| `ImageTest (5).png`       | (empty)          | `ImageTest`      |
| `myimage_final.png`       | `_final`         | `myimage`        |

**Note:**  
If the trim marker is not found in the filename, only the optional trailing number in parentheses (if present) will be removed.

---

