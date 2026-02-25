# ComfyUI-Buff-Nodes

Several quality-of-life batch operation and string manipulation nodes.

_WORK IN PROGRESS_

In part written with Claude-3.7-Sonnet in a human in-the-loop development standard.

## File Path Selector Node

The `FilePathSelectorFromDirectory` node is a utility for ComfyUI that helps you select files from a specified directory. 
- **Directory Selection**: Choose any directory on your system to scan for files
- **File Type Filtering**: Specify which file extensions to include (e.g., "mp4,jpg,png")
- **Selection Modes**:
  - **Randomize**: Pick a random file from the directory (can be seeded for reproducibility)
  - **Sequential**: Go through files one by one in alphabetical order, remembering position between runs
- **Subdirectory Support**: Optionally search through subdirectories for matching files
- **Persistent Memory**: Tracks the sequential position between ComfyUI sessions
- **Caching**: Efficient file list caching with configurable duration

## String Processor Node

The `StringProcessor` node allows you to manipulate text strings with various operations:
- **Operations**:
  - **First/Last N Characters**: Extract the first or last specified number of characters
  - **First/Last N Words**: Extract the first or last specified number of words using a custom delimiter
  - **Custom Expression**: Use Python expressions to transform strings with full flexibility
- **Features**:
  - Custom word delimiters
  - Comprehensive tooltips with examples
  - Error handling for custom expressions

## Console Output Node

The `ConsoleOutput` node provides a simple way to display text in the console:
- **Features**:
  - Custom prefix to identify your outputs
  - Optional timestamps
  - Acts as a terminal output node in workflows
  - Useful for debugging or logging information

## Most Recent File Selector Node

The `MostRecentFileSelector` node finds the most recently modified file in a specified directory:
- **Features**:
  - Automatically detects the most recently modified file in a directory
  - Optional file type filtering using comma-separated extensions
  - Can create a black initialization image if no file is found
  - Configurable black image dimensions and format
- **Input Options**:
  - **Directory Path**: Path to search for files (defaults to ComfyUI's input directory)
  - **File Types**: Optional comma-separated list of file extensions to filter by (e.g., "png,jpg")
  - **Create Init Image**: Option to create a black image if no file is found
  - **Init Image Settings**: Configurable width, height, and format (png/jpg) for the black image
- **Output**:
  - Returns the full path to the most recent file
  - Returns an empty string if no file is found and init image creation is disabled
  - Creates and returns path to a black image if no file is found and init image creation is enabled
- **Behavior**:
  - Always re-executes when the workflow is queued
  - Handles missing directories gracefully
  - Provides detailed console logging for debugging

## Two Image Concatenator Node

> Note: The following node is for the use of [TemporalNet2](https://huggingface.co/CiaraRowles/TemporalNet2) in video streaming workflows

The `TwoImageConcatenator` node combines two 3-channel images into a single 6-channel image:
- **Features**:
  - Concatenates two input images along the channel dimension
  - Maintains batch processing capability
  - Useful for temporal models that require both previous and current frames
  - Preserves image dimensions while doubling the channel count
- **Input Requirements**:
  - Both images must have the same batch size, height, and width
  - Both images must be 3-channel images
- **Output**:
  - Single 6-channel image tensor (batch, height, width, 6 channels)

## Frame Rate Modulator Node

The `FrameRateModulator` node allows you to modify the frame rate of image sequences by resampling frames:
- **Features**:
  - **Mode Selection**: Choose between exact frame count or multiplier-based resampling
  - **Frame Count Mode**: Set a specific target number of output frames
  - **Multiplier Mode**: Scale input frame count by a factor (2.0 = slow motion, 0.5 = speed up)
  - **Interpolation Methods**:
    - **Nearest**: Simple frame duplication/skipping (fastest)
    - **Linear**: Smooth blending between adjacent frames
    - **Cubic**: High-quality cubic interpolation for smooth motion
  - **Loop Modes** for handling edge cases:
    - **Clamp**: Use first/last frame for out-of-bounds positions
    - **Repeat**: Loop the sequence seamlessly
    - **Mirror**: Reverse and repeat for ping-pong effect
- **Input Requirements**:
  - Batch of images in ComfyUI format (batch, height, width, channels)
- **Output**:
  - Resampled image sequence with target frame count
  - Frame count as integer for downstream processing
- **Use Cases**:
  - Creating slow motion effects (50 frames → 75 frames)
  - Speeding up sequences (50 frames → 25 frames)
  - Standardizing frame counts across different clips
  - Temporal upsampling with smooth interpolation

## Raft Optical Flow Node

> Note: The following node is for the use of [TemporalNet2](https://huggingface.co/CiaraRowles/TemporalNet2) in video streaming workflows

The `RaftOpticalFlowNode` calculates optical flow between two images using the RAFT (Recurrent All-Pairs Field Transforms) model:
- **Features**:
  - Uses the state-of-the-art RAFT model for optical flow estimation
  - Processes images in batches
  - Automatically handles device placement (CPU/GPU)
  - Produces a visualization of motion between frames
- **Input Requirements**:
  - Two input images (typically previous and current frames)
  - Images should be in ComfyUI's standard format (batch, height, width, channels)
- **Output**:
  - Optical flow visualization as an image
  - Color-coded representation of motion between frames
  - Output is normalized to [0,1] range

## Use Cases

- Randomly selecting input files for processing
- Creating workflows that process batches of files in sequence
- Manipulating text data within workflows (filenames, prompts, metadata)
- Extracting portions of text from larger strings
- Debugging workflows by logging intermediate values to the console
- Formatting and transforming text for use in prompts or file operations
- Processing video frames for motion analysis
- Combining multiple image channels for temporal models
- Visualizing motion between consecutive frames
- Finding the latest output from a previous workflow run
- Creating initialization images for new workflows
- Monitoring directories for new files
- Setting up automated workflows that process the most recent file

## Technical Details

The File Path Selector node saves its sequential position state to a JSON file, allowing it to remember where it left off even if you restart ComfyUI. When using the randomize mode with a seed, you'll get consistent, reproducible selections.

The String Processor supports Python expressions that give you the full power of string manipulation in a controlled environment.

The Raft Optical Flow Node uses the RAFT model from torchvision, which provides high-quality optical flow estimation. The model is automatically downloaded when first used and cached for subsequent runs.