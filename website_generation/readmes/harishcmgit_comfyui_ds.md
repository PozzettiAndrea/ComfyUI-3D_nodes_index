# ComfyUI Document Scanner

A custom ComfyUI node that implements advanced document scanning with automatic perspective correction and multiple enhancement options.

## Features

- **Automatic Document Detection**: Uses contour detection to identify document boundaries
- **Perspective Correction**: Corrects skewed documents to flat, rectangular format
- **Multiple Enhancement Methods**: 6 different enhancement algorithms for optimal results
- **Batch Processing**: Handles multiple images at once
- **Debug Visualization**: Optional edge detection visualization
- **Fallback Safety**: Graceful handling of edge cases and errors

## Nodes

### Document Scanner
Full-featured node with all configuration options:

**Inputs:**
- `image`: Input document image(s)
- `enhancement_method`: Choose from 6 enhancement methods
  - `sharpening`: General purpose sharpening with HSV adjustments
  - `cartooning`: Cartoon-like effect with edge detection
  - `clahe`: Contrast Limited Adaptive Histogram Equalization
  - `threshold`: Binary thresholding with Otsu's method
  - `adaptive_threshold`: Local adaptive thresholding
  - `flat_field`: Flat field correction for uneven lighting
- `edge_threshold_low/high`: Canny edge detection thresholds (20, 70 default)
- `blur_kernel_size`: Bilateral filter kernel size (5 default)
- `skip_preprocessing`: Skip GrabCut text removal step
- `return_debug_edges`: Output edge detection visualization

**Outputs:**
- `scanned_image`: Final processed document
- `debug_edges`: Edge detection visualization (if enabled)

### Simple Document Scanner
Simplified interface with preset configurations:

**Inputs:**
- `image`: Input document image(s)  
- `enhancement`: Choose enhancement preset
  - `auto`: General purpose (sharpening)
  - `text`: Optimized for text documents (adaptive threshold)
  - `photo`: Optimized for photo documents (CLAHE)

**Outputs:**
- `scanned_image`: Final processed document

## Algorithm Overview

1. **Preprocessing**: Optional GrabCut segmentation to remove text
2. **Grayscale Conversion**: Convert to single channel for processing
3. **Blur**: Bilateral filtering for edge-preserving noise reduction
4. **Edge Detection**: Canny edge detection to find document boundaries
5. **Contour Detection**: Find largest quadrilateral contour
6. **Perspective Correction**: Warp document to rectangular format
7. **Enhancement**: Apply selected enhancement method

## Installation

1. Copy the `comfyui_document_scanner` folder to your ComfyUI `custom_nodes` directory
2. Install dependencies: `pip install -r requirements.txt`
3. Restart ComfyUI
4. The nodes will appear under `image/processing` category

## Requirements

- opencv-python >= 4.5.0
- numpy >= 1.20.0  
- torch >= 1.9.0 (provided by ComfyUI)

## Error Handling

The node includes robust error handling:
- If document detection fails, returns original image
- If perspective correction fails, skips correction step
- Graceful fallbacks for all processing steps
- Error messages logged to console

## Tips for Best Results

- Use well-lit images with clear document boundaries
- Ensure document occupies significant portion of image
- For text documents, try `adaptive_threshold` enhancement
- For photos/mixed content, try `clahe` or `sharpening`
- Adjust edge detection thresholds if having detection issues
- Use debug edges output to troubleshoot detection problems