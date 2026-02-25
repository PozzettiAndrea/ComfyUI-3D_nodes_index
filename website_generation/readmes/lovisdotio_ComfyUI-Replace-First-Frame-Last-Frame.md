# ComfyUI Replace First & Last Frames

Replace the first and last frames of an image sequence in ComfyUI. Auto-resizes frames to match video dimensions, handles batches, and adjusts parameters if needed.

![Node Preview](node.png)

## Installation

Clone into `ComfyUI/custom_nodes/` and restart ComfyUI. Node appears in `image/animation`.

## Usage

- **image_sequence**: Your image sequence (video)
- **start_frames**: Frame(s) to replace at start (auto-resized to match sequence)
- **last_frames**: Frame(s) to replace at end (auto-resized to match sequence)
- **num_start_frames**: How many frames to replace at start (0-10000)
- **num_last_frames**: How many frames to replace at end (0-10000)

**Auto-resizing**: Start and last frames are automatically resized to match the video dimensions (height, width, channels). No manual resizing needed.

## License

MIT

