# ComfyUI Stegaflow

A ComfyUI custom node pack that embeds workflow data into image pixels using steganography (LSB encoding), allowing workflows to be recovered from images even if PNG metadata is stripped.


## Vibe Coding Disclaimer
This custom node pack was totally vibe coded as a proof-of-concept. I took a glance at the implementation and it's pretty bad (e.g. creating a giant list of all pixels in the image). But it works!

## Features

- **Save Image (Stegaflow)** node - Saves images with workflow data embedded in pixels
- Automatic workflow extraction when loading images with embedded data
- Compatible with existing ComfyUI workflow system
- Optional: Can also save to PNG metadata (standard method) simultaneously

## How It Works

### Encoding (Python)
The node embeds workflow JSON data into the lowest bit (LSB) of each RGB channel in the image pixels. The data is stored in a clockwise spiral pattern starting from the top-left corner:
1. Top row (left to right)
2. Right column (top to bottom)
3. Bottom row (right to left)
4. Left column (bottom to top)
5. Repeat inward for inner rectangles

The data is prefixed with a magic string `"ComfyUI\0"` to identify images containing embedded workflows.

### Decoding (JavaScript)
When an image is loaded in ComfyUI, the extension automatically:
1. Reads pixel data from the image
2. Extracts LSBs in the same clockwise spiral pattern
3. Checks for the magic string
4. If found, decodes the workflow JSON and loads it

## Usage

### Saving Images with Embedded Workflows

1. Add the **Save Image (Stegaflow)** node to your workflow
2. Connect your image output to it
3. Configure options:
   - `filename_prefix`: Output filename prefix
   - `embed_in_pixels`: Enable/disable steganography (default: true)
   - `embed_in_metadata`: Enable/disable PNG metadata (default: true)

### Loading Images with Embedded Workflows

Simply drag and drop a PNG image with embedded workflow data into ComfyUI. The workflow will be automatically extracted and loaded.

## Technical Details

- **Data Capacity**: 3 bits per pixel (1 bit each from R, G, B channels)
- **Magic Header**: "ComfyUI\0" (8 bytes = 64 bits)
- **Encoding Method**: LSB (Least Significant Bit) steganography
- **Pattern**: Clockwise spiral from outer edge to center
- **Compatibility**: V3 ComfyUI node API format

## Notes

- The visual impact on images is minimal (only the LSB is modified)
- Images must be large enough to store the workflow data
- Works with PNG images
- Steganography data survives most image operations but may be lost if images are re-encoded with certain compression methods
