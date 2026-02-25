# MF PipoNodes - ComfyUI Custom Nodes

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-orange.svg)](https://github.com/comfyanonymous/ComfyUI)

**A comprehensive collection of utility and quality-of-life nodes for ComfyUI workflows**

## 📋 Overview

MF PipoNodes provides 10 specialized nodes for ComfyUI covering:

- 🎲 **Randomization** - Dice rolling for seeds and conditional logic
- 📝 **Text Processing** - Line manipulation and extraction
- 📊 **Logging** - File-based logging with timestamps
- 🔢 **Math Operations** - Modulo with cycle tracking
- 🎬 **Sequencing** - Shot helpers and story progression
- 📈 **Visualization** - Interactive graph plotting
- 🌱 **Project Management** - Seed management and step tracking

## 🚀 Quick Start

### Installation via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "MF PipoNodes"
3. Click Install
4. Restart ComfyUI

### Manual Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/pierreb-mf/ComfyUI-MF-PipoNodes.git
cd ComfyUI-MF-PipoNodes
pip install -r requirements.txt
```

*Note that the **MF Graph Plotter** node uses [Chart](https://www.chartjs.org/), loaded at init using a CDN*

## 📦 Available Nodes

### 🎲 Random Category

#### MF Dice Roller

<details>
<summary>
Simulate dice rolls for random number generation.
</summary>

**Inputs:**

- `dice` (ENUM) - D4, D6, D8, D10, D12, D20, D100

**Outputs:**

- `int` (INT) - Roll result as integer
- `string` (STRING) - Roll result as string

**Use Cases:**

- Random seed generation
- Conditional branching
- Prompt variation

**Example:**

```text
MF Dice Roller (D6) → Random value 1-6
↓
Use for seed or Line Select index
```

</details>

---

### 🔧 Utilities Category

#### MF Line Counter

<details>
<summary>
Count the number of lines in multi-line text.
</summary>

**Inputs:**

- `text` (STRING, multiline) - Text to count

**Outputs:**

- `line_count_int` (INT) - Line count as integer
- `line_count_str` (STRING) - Line count as string

**Features:**

- Handles all line break formats (\n, \r\n, \r)
- Counts empty lines
- Returns 0 for empty input

**Use Cases:**

- List validation before processing
- Loop control
- Workflow logic

</details>

#### MF Line Select

<details>
<summary>
Extract a specific line from multi-line text by index (0-based).
</summary>

**Inputs:**

- `text` (STRING, multiline) - Source text
- `line_index` (INT, 0-1000) - Line to extract (0 = first line)

**Outputs:**

- `selected_line` (STRING) - The extracted line

**Features:**

- Zero-based indexing
- Error handling for out-of-range indices
- Preserves empty lines

**Use Cases:**

- Cycling through prompts
- Processing lists sequentially
- Dynamic text selection

**Example:**

```text
Prompts: "forest\nbeach\nmountain\ncity"
Line Index: 2
Output: "mountain"
```

</details>

---

### 📝 Logging Category

#### MF Log File

<details>
<summary>
Write timestamped entries to a log file.
</summary>

**Inputs:**

- `log_entry` (STRING, multiline, required) - Content to log
- `save_log_path` (STRING, optional) - Directory (defaults to output dir)
- `log_file_name` (STRING, optional) - Filename (defaults to "logfile.txt")

**Outputs:**

- `log_content` (STRING) - Full log file contents

**Features:**

- Automatic timestamps
- Creates directories if needed
- Appends to existing logs
- Display widget shows full log

**Format:**

```text
[2025-10-22 14:30:15] Your log entry here
[2025-10-22 14:32:08] Another entry
```

**Use Cases:**

- Generation tracking
- Debugging workflows
- Audit trails
- LLM conversation history

</details>

#### MF Log Reader

<details>
<summary>
Read the contents of a log file.
</summary>

**Inputs:**

- `log_file_path` (STRING, optional) - Directory
- `log_file_name` (STRING, optional) - Filename

**Outputs:**

- `log_content` (STRING) - File contents

**Use Cases:**

- Reading workflow history
- Feeding context to LLMs
- Reviewing generation logs

</details>

---

### 🔢 Math Category

#### MF Modulo

<details>
<summary>
Basic modulo operation with visual feedback.
</summary>

**Inputs:**

- `input_number` (INT) - Number to process
- `modulo_value` (INT, min 1) - Divisor

**Outputs:**

- `result_int` (INT) - Modulo result
- `result_str` (STRING) - Result as string

**Example:**

```text
Input: 7, Modulo: 3 → Output: 1
Input: 9, Modulo: 3 → Output: 0
```

**Use Cases:**

- List cycling
- Pattern generation
- Periodic triggers

</details>

#### MF Modulo Advanced

<details>
<summary>
Enhanced modulo with cycle tracking.
</summary>

**Inputs:**

- `input_number` (INT) - Number to process
- `modulo_value` (INT, min 1) - Divisor
- `reset_cycle` (BOOLEAN) - Reset cycle counter

**Outputs:**

- `result_int` (INT) - Modulo result
- `result_str` (STRING) - Result as string
- `cycle_int` (INT) - Complete cycles
- `cycle_str` (STRING) - Cycles as string

**Example:**

```
Steps 0-4, Mod 5: Cycle 0, Results 0-4
Steps 5-9, Mod 5: Cycle 1, Results 0-4
Steps 10-14, Mod 5: Cycle 2, Results 0-4
```

**Use Cases:**

- Batch rendering with progress tracking
- Multi-pass workflows
- Iteration counting

</details>

---

### 🎬 Sequencing Category

#### MF Shot Helper

<details>
<summary>
Organize frames/steps into sequences and shots based on beat points.
</summary>

**Inputs:**

- `step` (INT, required) - Current frame/step number
- `beats` (STRING, required) - Beat points marking sequence boundaries

**Outputs:**

- `sequence_int` (INT) - Current sequence number
- `sequence_str` (STRING) - Sequence as string
- `shot_int` (INT) - Shot number within sequence
- `shot_str` (STRING) - Shot as string
- `shot_name` (STRING) - Formatted name (e.g., "seq01_shot03")

**Beat Formats Supported:**

```text
Comma-separated: "3,8,15,25"
Newline-separated: "3\n8\n15\n25"
Array format: "[3,8,15,25]"
```

**How It Works:**

- Sequence 1: Steps 0 until first beat
- At each beat: New sequence starts, shot resets to 1
- Perfect for dividing long animations into logical segments

**Example:**

```text
Beats: "120,240,360"

Frames 0-119:   seq01_shot001 through seq01_shot120
Frames 120-239: seq02_shot001 through seq02_shot120
Frames 240-359: seq03_shot001 through seq03_shot120
Frames 360+:    seq04_shot001 through seq04_shot...
```

**Use Cases:**

- Video/animation organization
- Musical synchronization
- Scene-based rendering
- Automatic file naming

</details>

#### MF Story Driver

<details>
<summary>
Project-based step sequencing with persistent seed management.
</summary>

**Inputs:**

- `projectName` (STRING) - Project identifier
- `randomize_seed_on_reset` (BOOLEAN) - Whether to change seed on reset

**Outputs:**

- `step_int` (INT) - Current step number (auto-increments)
- `step_str` (STRING) - Step as string
- `projectName` (STRING) - Sanitized name (spaces → underscores)
- `saveFolder` (STRING) - Formatted folder name (`projectName_seed`)
- `storySeed` (INT) - Project's persistent seed

**Features:**

- ✨ **Persistent State:** State saved per project across sessions
- 🔢 **Auto-Increment:** Steps advance automatically on each execution
- 🌱 **Seed Management:** Consistent seeds per project
- 🔄 **Reset Button:** Reset step counter and optionally randomize seed
- 📁 **Folder Naming:** Generates organized output paths

**UI Elements:**

- Status display: `Step: X | Seed: Y`
- 🔄 Reset Story button

**Example Workflow:**

```text
MF Story Driver (projectName: "MyStory")
├─ Step 0, Seed: 12345678901234567890
├─ Outputs:
│  ├─ step_int: 0
│  ├─ projectName: "MyStory"
│  ├─ saveFolder: "MyStory_12345678901234567890"
│  └─ storySeed: 12345678901234567890
│
Next execution:
├─ Step 1, Same seed
│
After reset (randomize ON):
└─ Step 0, New seed: 98765432109876543210
```

**Use Cases:**

1. **Sequential Image Generation**

   ```text
   Story Driver → storySeed → KSampler
   ↓
   Consistent seed across all story steps
   ```

2. **Batch Rendering with Tracking**

   ```text
   Story Driver → step_int → Filename
   ↓
   Automatic numbering: "MyStory_001.png", "MyStory_002.png"...
   ```

3. **Multi-Shot Story Development**

   ```text
   Story Driver → step_int → Line Select → Different prompts per step
   ↓
   Each story beat uses different prompt
   ```

4. **Organized Output Structure**

   ```text
   Story Driver → saveFolder → Save Image path
   ↓
   All renders go to "MyStory_12345/image_001.png"
   ```

**State Persistence:**

- State saved in `story_driver_state.json` (automatically created)
- Each project tracked independently
- Survives ComfyUI restarts

</details>

---

### 📈 Visualization Category

#### MF Graph Plotter

<details>
<summary>
Interactive X/Y data plotter with Chart.js visualization.
</summary>

**Inputs:**

- `X` (INT) - X coordinate
- `Y` (INT) - Y coordinate

**Outputs:**

- `X` (INT) - Pass-through X value
- `Y` (INT) - Pass-through Y value

**Features:**

- 📊 **Live Visualization:** Real-time Chart.js graph
- 💾 **Save to PNG:** Export graph image
- 🔄 **Reset Per Node:** Clear data for each node independently
- 📈 **Smooth Curves:** Interpolated line rendering
- 🎯 **Interactive Tooltips:** Hover to see exact X/Y values
- 💾 **Persistent State:** Data preserved across sessions

**UI Elements:**

- Interactive canvas (400x300px)
- 🔄 Reset Graph button
- 💾 Save Graph button
- Tooltip on hover showing coordinates

**Graph Styling:**

- Yellow (#FFEC00) line with subtle fill
- Minimal axis labels (Y label only)
- Black axis borders
- Grid lines for reference
- Smooth curve interpolation

**Example Workflow:**

```text
Loop Counter (0-10)
├─ X coordinate
├─ Some Calculation → Y coordinate
└─ MF Graph Plotter → Visual plot
```

**Use Cases:**

1. **Parameter Relationship Visualization**

   ```text
   CFG Scale → X
   Quality Score → Y
   Plot to find optimal CFG value
   ```

2. **Workflow Progression Tracking**

   ```text
   Step Number → X
   Loss Value → Y
   Monitor training progress
   ```

3. **Data Analysis**

   ```text
   Prompt Variation Index → X
   Image Similarity Score → Y
   Visualize prompt effectiveness
   ```

4. **Real-time Monitoring**

   ```text
   Time Step → X
   Memory Usage → Y
   Track resource consumption
   ```

**State Management:**

- Data stored per node ID in `graph_plotter_state.json`
- Each Graph Plotter node maintains independent data
- State survives ComfyUI restarts
- Reset button clears data for that specific node only

**Saving Graphs:**

1. Click 💾 Save Graph button
2. Choose save location via file dialog
3. Graph exported as PNG image

</details>

---

### 💾 Data Category

#### MF Save Data

<details>
<summary>
Save string data to various file formats (JSON, XML, CSV, YAML).
</summary>

**Inputs:**

- `data` (STRING, force input) - Data to save
- `output_path` (STRING) - Directory path (default: "output")
- `filename` (STRING) - Filename without extension (default: "data")
- `format` (ENUM) - File format: json, xml, csv, yaml

**Outputs:**

- `filepath` (STRING) - Path to saved file

**Features:**

- ✨ **Multi-format support:** JSON, XML, CSV, YAML
- 📁 **Auto-directory creation:** Creates output folders if needed
- 🔄 **Smart parsing:** Attempts to parse input as structured data
- 🛡️ **Error handling:** Graceful fallback for invalid formats

**Use Cases:**

1. **Save LLM outputs**

   ```text
   LLM Response → MF Save Data (JSON) → Structured storage
   ```

2. **Export workflow data**

   ```text
   Data Processing → MF Save Data (CSV) → Excel-compatible export
   ```

3. **Configuration files**

   ```text
   Settings → MF Save Data (YAML) → Human-readable config
   ```

4. **API responses**

   ```text
   API Data → MF Save Data (JSON) → Persistent cache
   ```

</details>

#### MF Read Data

<details>
<summary>
Read data from various file formats and output as string.
</summary>

**Inputs:**

- `file_path` (STRING) - Directory path (default: "output")
- `filename` (STRING) - Full filename with extension (default: "data.json")

**Outputs:**

- `data` (STRING) - File contents as formatted string

**Features:**

- ✨ **Auto-format detection:** Based on file extension
- 📖 **Multiple formats:** JSON, XML, CSV, YAML, or plain text
- 🔄 **Formatted output:** Pretty-printed JSON for readability
- 🛡️ **Error handling:** Clear error messages if file not found

**Supported Formats:**

- `.json` - Parsed and formatted JSON
- `.xml` - Formatted XML string
- `.csv` - Converted to JSON array
- `.yaml`, `.yml` - Converted to JSON
- Others - Read as plain text

**Use Cases:**

1. **Load configuration**

   ```text
   MF Read Data (config.yaml) → Parse settings → Workflow
   ```

2. **Resume from checkpoint**

   ```text
   MF Read Data (state.json) → Restore workflow state
   ```

3. **Process saved data**

   ```text
   MF Read Data → Transform → MF Save Data (different format)
   ```

4. **Feed context to LLM**

   ```text
   MF Read Data → Concatenate → LLM Input
   ```

</details>

#### MF Show Data

<details>
<summary>
Display string data in an auto-sizing text widget with console output.
</summary>

**Inputs:**

- `data` (STRING, force input) - Data to display

**Outputs:**

- `data` (STRING) - Pass-through data

**Features:**

- 📺 **Live preview:** Auto-updating text display in node
- 📏 **Auto-resize:** Widget adjusts to content (3-20 lines)
- 🖥️ **Console output:** Also prints to ComfyUI console
- 📝 **Monospace font:** Perfect for code and structured data
- 🔄 **Pass-through:** Data continues to next node

**UI Elements:**

- Read-only text widget
- Auto-sizing (3-20 rows based on content)
- Monospace font for readability
- Console logging with dividers

**Use Cases:**

1. **Debug data flow**

   ```text
   Any Node → MF Show Data → Visual inspection → Next node
   ```

2. **Monitor LLM output**

   ```text
   LLM → MF Show Data → See response → Save/Process
   ```

3. **Validate transformations**

   ```text
   Transform → MF Show Data → Verify → Continue
   ```

4. **Inline documentation**

   ```text
   Config → MF Show Data → Document workflow behavior
   ```

</details>

## 📚 Best Practices

### For Batch Rendering

- Use **Modulo Advanced** + **Line Select** to cycle through prompts
- Enable cycle tracking to know your progress
- Combine with **Log File** to record each generation

### For LLM Workflows

- Store **all** LLM interactions in Log File
- Use **Log Reader** to feed context back
- Timestamp tracking helps debugging

### For List Processing

- Always **count lines** before selecting
- Use modulo to safely cycle through lists
- Handle edge cases with error checking

### For Animation Workflows

- Use **Shot Helper** for frame organization
- Set beats at musically significant points
- Leverage automatic shot naming for rendering

### For Story Generation

- Use **Story Driver** for consistent seeds per project
- Reset between stories, not between steps
- Leverage saveFolder for automatic organization
- Track multiple projects simultaneously

### For Data Analysis

- Use **Graph Plotter** for visual parameter sweeps
- Save graphs before resetting for record-keeping
- Plot relationships between generation parameters

## 🎯 Common Workflow Patterns

### 1. Infinite Prompt Cycling

```text
Counter → MF Modulo Advanced (mod 5) → MF Line Select
               ↓                              ↓
         Tracks cycles              Cycles through 5 prompts
               ↓
         Your prompt list (5 items)
```

Perfect for batch rendering that loops through prompts indefinitely.

### 2. LLM Context Accumulation

```text
LLM Output → MF Log File → Stores conversation history
               ↓
   MF Log Reader → Concatenate with new prompt
               ↓
         LLM Input (with full context)
```

Maintains conversation history across multiple LLM generations.

### 3. Random Selection

```text
MF Dice Roller (D6) → MF Line Select → Picks random line
                              ↓
               Your list of 6 options
```

Each execution randomly selects from your list.

### 4. Progress Tracking with Logging

```text
Counter → MF Modulo Advanced → Position + Cycles
            ↓
   MF Log File → Logs progress with timestamps
```

Track exactly where you are in long batch processes.

### 5. Video Sequence Organization

```text
Frame Counter → MF Shot Helper (beats: "120,240,360")
                     ↓
   Automatic sequence/shot naming:
   - Frames 0-119: seq01_shot001-120
   - Frames 120-239: seq02_shot001-120
   - Frames 240-359: seq03_shot001-120
                     ↓
   Use shot_name in filename → Organized output
```

Perfect for long animations divided into sequences.

### 6. Sequence-Based Prompt Switching

```text
Frame Counter → MF Shot Helper → sequence_int
                     ↓
            MF Line Select (using sequence_int)
                     ↓
         Different prompt for each sequence
```

Automatically switch prompts when crossing sequence boundaries.

### 7. Story-Driven Generation

```text
MF Story Driver (projectName: "MyStory")
├─ step_int → Image naming/numbering
├─ storySeed → KSampler seed (consistent across story)
├─ saveFolder → Output directory organization
└─ projectName → Metadata/tagging
```

Perfect for sequential storytelling with consistent style.

### 8. Parameter Sweep with Visualization

```text
Loop: CFG Scale 1-10
├─ CFG Value → X coordinate
├─ Image Quality Metric → Y coordinate
└─ MF Graph Plotter → Visual results
```

Visualize how parameters affect output quality.

### 9. Multi-Project Workflow

```text
Project Selector → MF Story Driver (projectName input)
                        ↓
         Multiple projects tracked independently
         - "Character_Study": Step 25, Seed: 123...
         - "Environment_Test": Step 10, Seed: 456...
         - "Style_Exploration": Step 5, Seed: 789...
```

Manage multiple concurrent projects with independent progression.

## 🐛 Troubleshooting

### Nodes Not Appearing

1. Check that `ComfyUI/custom_nodes/ComfyUI-MF-PipoNodes/` exists
2. Verify `web/pipoNodes.js` is present
3. Restart ComfyUI completely
4. Check console for errors during startup

### Display Not Updating

1. Queue the workflow to trigger execution
2. Check browser console (F12) for JavaScript errors
3. Verify Chart.js loaded (check console for "📊 Chart.js loaded")

### Log File Not Found

1. Run MF Log File node first to create the file
2. Verify file paths match between writer and reader
3. Check that output directory is writable

### Graph Not Resetting

1. Ensure you clicked the 🔄 Reset Graph button
2. Check browser console for API errors
3. Verify node ID is correctly identified

### Story Not Incrementing

1. Verify projectName is unique per project
2. Check that state file is writable
3. Ensure node is actually executing (not cached)

### Shot Helper Not Incrementing Sequences

1. Verify beat points are in ascending order
2. Check beat string formatting
3. Remember: beats mark the START of each new sequence

## 🤝 Contributing

See [CONTRIBUTING](CONTRIBUTING.md)

## 📜 License

See [LICENSE](LICENSE.md)

## 👤 Author and Contributors

See [AUTHORS](AUTHORS.md)

## 🙏 Acknowledgments

- ComfyUI community for feedback and inspiration
- Chart.js team for the excellent visualization library
- All contributors and users of MF PipoNodes

## 🔗 Links

- **GitHub Repository:** https://github.com/pierreb-mf/ComfyUI-MF-PipoNodes
- **Moment Factory:** https://momentfactory.com

---

**Made with ❤️ for the ComfyUI Community**
