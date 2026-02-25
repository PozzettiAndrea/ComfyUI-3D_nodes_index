# ComfyUI Prompt Iterator Extension

A powerful custom node extension for ComfyUI that enables automatic iteration through multiple prompts with corresponding filename generation. Perfect for batch processing different variations like character face angles, poses, or any sequential prompt workflow.

**Author:** BiloxiStudios Inc - BizaNator
**Version:** 2.1.0
**License:** MIT

## Features

### 🎯 Core Functionality
- **Sequential Iteration**: Automatically advances through prompts on each queue execution
- **Manual Control**: Jump to specific prompts by index
- **Dynamic Filenames**: Generates matching filenames for SaveImage nodes
- **State Persistence**: Remembers position between queue runs
- **Reset Capability**: Start over from the beginning at any time
- **Dynamic Inputs**: NEW! Support for multiple string inputs (up to 20 prompts)
- **Seed Management**: NEW v2.1! INT seed output for KSampler with intelligent batch control

### 📦 Three Node Types

#### 1. **Prompt Iterator Dynamic** (NEW v2.1!)
Dynamic input system with multiple string connections:
- Connect up to 20 different prompt sources
- Each input can be a text box or string node
- Perfect for modular workflow design
- Auto-detects connected inputs
- Supports all filename modes
- **NEW**: INT seed output for KSampler connection
- **NEW**: Multiple seed modes (fixed, increment_batch, increment_prompt, random)

#### 2. **Prompt Iterator** (Basic)
Simple and straightforward prompt iteration with essential features:
- Multiple prompts input (one per line)
- Sequential, manual, or single modes
- Optional filename list or auto-generation
- Current position tracking

#### 3. **Prompt Iterator Advanced**
Enhanced version with professional features:
- Prepend/append text to prompts
- Multiple filename generation modes
- Suffix lists for organized naming
- Template-based filename generation
- Random order with seed control
- Ping-pong and loop modes
- Debug information output
- **NEW**: INT seed output for KSampler connection
- **NEW**: Multiple seed modes for batch consistency

## Installation

1. Navigate to your ComfyUI custom_nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```
   git clone https://github.com/BiloxiStudios/ComfyUI_PromptIterator.git
   ```

3. Restart ComfyUI

4. The nodes will appear in the "utils/prompt" category

## Usage Examples

### Example 1: Dynamic Inputs (NEW!)

Connect different prompt sources:
- prompt_1 → Text node: "face front view"
- prompt_2 → Another workflow's output
- prompt_3 → Text node: "face left profile"
- prompt_4 → Text node: "face right profile"

The node automatically iterates through all connected inputs.

### Example 2: Character Face Angles

**Prompts Input:**
```
face only headshot, facing camera directly, professional portrait
Left profile View, rotate face 90 degrees left, professional portrait
Right profile View, rotate face 90 degrees right, professional portrait
Back View, direct back of the head, showing hair details
```

**Suffixes Input:**
```
_front
_left
_right
_back
```

**Result:**
- Queue 1: Prompt 1 → "character_front.png"
- Queue 2: Prompt 2 → "character_left.png"
- Queue 3: Prompt 3 → "character_right.png"
- Queue 4: Prompt 4 → "character_back.png"

## Node Parameters

### Prompt Iterator Dynamic (NEW!)

| Parameter | Type | Description |
|-----------|------|-------------|
| prompt_1-20 | STRING | Dynamic string inputs (connect nodes or use text) |
| mode | ENUM | "sequential", "manual", "random", or "single" |
| filename_mode | ENUM | "auto_index", "suffix_list", or "template" |
| base_filename | STRING | Base name for generated files |
| suffixes | STRING | List of suffixes for filename generation |
| manual_index | INT | Index for manual mode |
| reset | BOOLEAN | Reset iterator to beginning |
| generation_seed | INT | Base seed for generation (NEW v2.1) |
| seed_mode | ENUM | "fixed", "increment_batch", "increment_prompt", "random" |

### Prompt Iterator (Basic)

| Parameter | Type | Description |
|-----------|------|-------------|
| prompts | STRING | Multiline text input, one prompt per line |
| mode | ENUM | "sequential", "manual", or "single" |
| base_filename | STRING | Base name for generated files |
| filenames | STRING | Optional list of specific filenames |
| manual_index | INT | Index for manual mode |
| reset | BOOLEAN | Reset iterator to beginning |

### Prompt Iterator Advanced

All basic parameters plus:

| Parameter | Type | Description |
|-----------|------|-------------|
| filename_mode | ENUM | "list", "suffix_list", "template", or "index" |
| suffixes | STRING | List of suffixes for filename generation |
| filename_template | STRING | Template with {base}, {index}, {suffix} |
| prepend_text | STRING | Text to add before each prompt |
| append_text | STRING | Text to add after each prompt |
| loop_mode | ENUM | "once", "loop", or "ping_pong" |
| generation_seed | INT | Base seed for generation (NEW v2.1) |
| seed_mode | ENUM | "fixed", "increment_batch", "increment_prompt", "random" |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| prompt | STRING | Current prompt text (connects to CLIPTextEncode) |
| filename | STRING | Current filename (connects to SaveImage) |
| current_index | INT | Current position in list |
| total_count | INT | Total number of prompts |
| status | STRING | Human-readable status |
| seed | INT | (Dynamic & Advanced) Seed for KSampler (NEW v2.1) |
| debug_info | STRING | (Advanced only) JSON debug data |

## Seed Management (NEW v2.1)

The Dynamic and Advanced nodes now include intelligent seed management for consistent batch generation:

### Seed Modes

1. **Fixed**: Uses the same seed for all prompts
   - Perfect for comparing different prompts with identical generation parameters
   - Example: Testing different face angles with the same seed

2. **Increment Batch**: Increments seed when returning to first prompt
   - Ideal for generating multiple variations of a complete set
   - Example: Generate 3 full sets of character angles with different seeds per set

3. **Increment Prompt**: Increments seed for each new prompt
   - Each prompt gets a unique, sequential seed
   - Example: Ensure each face angle has a slightly different variation

4. **Random**: Generates a random seed for each execution
   - Maximum variation between generations
   - Example: Exploring diverse outputs

### Connecting to KSampler

Simply connect the `seed` INT output to your KSampler's `seed` input:
```
PromptIteratorDynamic.seed → KSampler.seed
```

This ensures consistent seed management across your batch generations.

## Workflow Integration

### Basic Setup
1. Add a Prompt Iterator node to your workflow
2. Enter your prompts or connect string inputs
3. Connect `prompt` output to your text encoding node
4. Connect `filename` output to SaveImage's filename_prefix
5. Connect `seed` output to KSampler's seed input (v2.1)
6. Queue your workflow multiple times

### Dynamic Input Setup (v2.0)
1. Add Prompt Iterator Dynamic node
2. Connect string nodes to prompt_1, prompt_2, etc.
3. Node automatically detects connected inputs
4. Connect seed output to KSampler (v2.1)
5. Queue to iterate through all connected prompts

## Version History

### v2.1.0 (Current)
- Added INT seed output for KSampler connection
- Intelligent seed management with multiple modes:
  - **Fixed**: Same seed for all prompts
  - **Increment Batch**: Increment seed when restarting prompt list
  - **Increment Prompt**: Increment seed on each prompt
  - **Random**: Random seed for each generation
- Seed persistence across workflow executions
- Support for batch-based seed incrementing

### v2.0.0
- Added Prompt Iterator Dynamic with multiple string inputs
- Support for up to 20 dynamic prompt connections
- Updated author: BiloxiStudios Inc - BizaNator
- Enhanced state management

### v1.0.0
- Initial release
- Basic and Advanced iterator nodes
- Multiple filename generation modes
- State persistence
- Reset functionality

## License

MIT License

Copyright (c) 2024 BiloxiStudios Inc - BizaNator

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Support

For issues or feature requests, please contact BiloxiStudios Inc

## Credits

Created by BiloxiStudios Inc - BizaNator for the ComfyUI community