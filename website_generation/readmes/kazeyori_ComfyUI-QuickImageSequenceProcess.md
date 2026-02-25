# Quick Image Sequence Process (QuickSeq)

A ComfyUI plugin for efficient image sequence processing. Features frame insertion, duplication, and removal with intuitive controls.

## Recent Updates

- **New Fill Mode Options**: Added ability to fill new frames with either copied frames (original behavior), pure white frames, or pure black frames
- **Enhanced Frame Processing**: Fill mode applies to both between-frame insertion and first/last frame operations
- **Improved Flexibility**: More options for creative sequence manipulation and special effects

## Features

1. **Frame Insertion Between Frames**:
   - Set the number of frames to insert between existing frames
   - Choose whether to copy from the previous or next frame
   - Select fill mode: copy existing frames or use solid white/black frames
   - Example: With frames_between=2, sequence [A,B] becomes [A,A,A,B] or [A,B,B,B]

2. **Quick Process First Frames**:
   - Add or remove frames at the beginning of the sequence
   - Positive values: Add duplicates of the first frame or solid color frames
   - Negative values: Remove frames from the beginning
   - Example: With quick_process_first_frames=2, [A,B,C] becomes [A,A,A,B,C]
   - Example: With quick_process_first_frames=-1, [A,B,C] becomes [B,C]

3. **Quick Process Last Frames**:
   - Add or remove frames at the end of the sequence
   - Positive values: Add duplicates of the last frame or solid color frames
   - Negative values: Remove frames from the end
   - Example: With quick_process_last_frames=2, [A,B,C] becomes [A,B,C,C,C]
   - Example: With quick_process_last_frames=-1, [A,B,C] becomes [A,B]

4. **Fill Mode Options**:
   - `copy_frame`: Use copies of existing frames (original behavior)
   - `white`: Insert pure white frames
   - `black`: Insert pure black frames
   - Applies to both between-frame insertion and first/last frame processing

5. **Processing Order Control**:
   - Choose whether to process first/last frames before or after the between-frame operations
   - Affects the final result when combining multiple operations
   - "Yes": Process first/last frames first
   - "No": Process between-frames first

6. **Real-time Frame Count Display**:
   - Shows the total number of frames after processing
   - Helps track sequence length changes

## Installation

1. Clone this repository into your ComfyUI's `custom_nodes` directory:
   ```bash
   cd custom_nodes
   git clone https://github.com/yourusername/ComfyUI-QuickImageSequenceProcess.git
   ```
2. Restart ComfyUI
3. Find "Quick Image Sequence Process" in the node menu

## Usage Example

1. Load an image sequence into ComfyUI
2. Add the "Quick Image Sequence Process" node
3. Configure parameters:
   - `frames_between`: Number of frames to insert between existing frames
   - `copy_frame`: Choose "previous" or "next" for inserted frames
   - `fill_mode`: Choose between copying frames or using solid white/black frames
   - `quick_process_first_frames`: Add/remove frames at start (negative to remove)
   - `quick_process_last_frames`: Add/remove frames at end (negative to remove)
   - `process_F_L_frames_first`: Choose processing order priority

## Output

The node outputs:
- `image`: The processed image sequence
- `width`: Frame width
- `height`: Frame height
- `count`: Total number of frames in the sequence

## License

Copyright 2024 kazeyori

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.