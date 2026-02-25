<div align="center">

# 🎯 DebugPadawan's ComfyUI Essentials

*Essential custom nodes for ComfyUI workflows*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)](https://github.com/comfyanonymous/ComfyUI)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/DebugPadawan/DebugPadawans-ComfyUI-Essentials.svg)](https://github.com/DebugPadawan/DebugPadawans-ComfyUI-Essentials/stargazers)

</div>

---

## ✨ Features

<table>
<tr>
<td><b>🔤 Text Processing</b></td>
<td>Split, join, and manipulate text strings with precision</td>
</tr>
<tr>
<td><b>📦 Data Conversion</b></td>
<td>Convert between text and JSON formats easily</td>
</tr>
<tr>
<td><b>🐛 Debug Tools</b></td>
<td>Print and inspect values during workflow execution</td>
</tr>
<tr>
<td><b>⏱️ Timing Control</b></td>
<td>Add delays and timing control to your workflows</td>
</tr>
<tr>
<td><b>🔧 Utilities</b></td>
<td>Essential helpers for workflow optimization</td>
</tr>
</table>

---

## 🚀 Installation

```bash
# Navigate to your ComfyUI custom nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/DebugPadawan/DebugPadawans-ComfyUI-Essentials.git

# Restart ComfyUI
```

---

## 📦 Available Nodes

### 🔤 Text Processing

<details>
<summary><b>📝 Text Splitter</b> - Split text strings by delimiter</summary>

**Category:** `DebugPadawan/Text`

Splits a text string at a specified delimiter and returns a list of strings.

**📥 Inputs:**
- `text` *(String)*: The text to split (supports multiline input)
- `delimiter` *(String)*: The character(s) to split by (default: `","`)
- `strip_whitespace` *(Boolean, optional)*: Remove leading/trailing whitespace (default: `True`)
- `remove_empty` *(Boolean, optional)*: Remove empty strings from result (default: `True`)

**📤 Outputs:**
- `text_list` *(List)*: The split list of strings
- `count` *(Integer)*: Number of elements in the list

**💡 Example:**
```
Input: "apple, banana, orange"
Delimiter: ","
Output: ["apple", "banana", "orange"] and 3
```

Process CSV-like data, split tag lists, separate coordinates, create filename lists, parse prompt components.

</details>

<details>
<summary><b>🔗 Text Joiner</b> - Combine strings with custom delimiters</summary>

**Category:** `DebugPadawan/Text`

Combines a list of strings into a single text string with a customizable delimiter.

**📥 Inputs:**
- `text_list` *(List)*: List of strings to join
- `delimiter` *(String)*: Character(s) to join with (default: `", "`)
- `prefix` *(String, optional)*: Text to add at the beginning
- `suffix` *(String, optional)*: Text to add at the end

**📤 Outputs:**
- `joined_text` *(String)*: The combined text string

**💡 Example:**
```
Input: ["red", "green", "blue"]
Delimiter: " | "
Prefix: "Colors: "
Suffix: " - end"
Output: "Colors: red | green | blue - end"
```

Combine prompt parts, convert lists to readable text, create metadata tags, build filenames, format output strings.

</details>

---

### 📦 Data Conversion

<details>
<summary><b>🗃️ TextToJSON</b> - Convert text to JSON</summary>

**Category:** `DebugPadawan/JSON`

Converts a valid JSON string into a JSON object, enabling further data processing or integration with other nodes.

**📥 Inputs:**
- `text` *(String)*: The text to parse as JSON

**📤 Outputs:**
- `json` *(JSON/Object)*: The parsed JSON object

**💡 Example:**
```
Input: '{"name": "Alice", "age": 30}'
Output: { "name": "Alice", "age": 30 }
```

Use this node to quickly transform JSON-formatted text into a usable data structure for your ComfyUI workflows.

</details>

---

### 🐛 Debug Tools

<details>
<summary><b>🖨️ Debug Print</b> - Console output for debugging</summary>

**Category:** `DebugPadawan/Debug`

Prints values to the console without interrupting the workflow. Perfect for debugging and monitoring data values during execution.

**📥 Inputs:**
- `value` *(Any)*: Any value to print to console (supports all data types)
- `label` *(String, optional)*: Label for the debug output (default: `"Debug"`)

**📤 Outputs:**
- `passthrough` *(Any)*: The same value passed through unchanged

**💻 Console Output:**
```
[MyLabel] list: ['Element1', 'Element2', 'Element3']
[Debug] str: Hello World
[Checkpoint] int: 42
[Data Flow] dict: {'key': 'value', 'count': 5}
[Boolean Test] bool: True
[Float Value] float: 3.14159
```

Monitor values during execution, debug complex workflows, verify data types, set checkpoints, troubleshoot unexpected results.

</details>

---

### ⏱️ Timing Control

<details>
<summary><b>⏳ Wait</b> - Add delays to workflow execution</summary>

**Category:** `DebugPadawan/Timing`

Pauses workflow execution for a specified duration. Useful for rate limiting, timing control, or debugging workflow sequences.

**📥 Inputs:**
- `value` *(Any)*: Any value to pass through after the delay
- `delay_seconds` *(Float)*: Duration to wait in seconds (default: `1.0`)
- `label` *(String, optional)*: Label for console output (default: `"Wait"`)

**📤 Outputs:**
- `passthrough` *(Any)*: The same value passed through after delay

**💻 Console Output:**
```
[Wait] Waiting for 2.5 seconds...
[Wait] Wait completed.
[Custom Timer] Waiting for 5.0 seconds...
[Custom Timer] Wait completed.
```

Rate limit API calls, debug timing issues, control workflow execution speed, add pauses between operations, synchronize parallel processes.

**⚠️ Note:** Use with caution in production workflows as it will genuinely pause execution.

</details>

---

### 🔧 Utility Nodes

<details>
<summary><b>📊 List Info</b> - Analyze list properties</summary>

**Category:** `DebugPadawan/Utilities`

Analyzes a list and returns useful information about it.

**📥 Inputs:**
- `input_list` *(List)*: The list to analyze

**📤 Outputs:**
- `count` *(Integer)*: Number of elements
- `first_item` *(String)*: First element (as string)
- `last_item` *(String)*: Last element (as string)

Validate list processing results, get quick statistics, check if lists are empty, extract boundary values.

</details>

<details>
<summary><b>🔀 Conditional String</b> - Boolean-based string selection</summary>

**Category:** `DebugPadawan/Logic`

Returns one of two strings based on a boolean condition.

**📥 Inputs:**
- `condition` *(Boolean)*: The condition to evaluate
- `true_string` *(String)*: String to return if True (default: `"True"`)
- `false_string` *(String)*: String to return if False (default: `"False"`)

**📤 Outputs:**
- `result` *(String)*: The selected string

Conditional prompt modification, dynamic filename generation, workflow branching, status message generation.

</details>

---

## 🎨 Quick Start Examples

### Basic Text Processing
```
"apple,banana,orange" → Text Splitter → ["apple", "banana", "orange"]
                                    ↓
["apple", "banana", "orange"] → Text Joiner → "apple | banana | orange"
```

### Text to JSON Conversion
```
'{"foo": "bar"}' → TextToJSON → { "foo": "bar" }
```

### Debug Workflow
```
Input Data → Debug Print ("Input") → Processing Node → Debug Print ("Output") → Result
```

### Timed Processing
```
Data → Wait (2.0s) → Processing → Wait (1.0s) → Output
```

---

## 📋 Node Categories

| Category | Nodes | Purpose |
|----------|-------|---------|
| **DebugPadawan/Text** | Text Splitter, Text Joiner | Text manipulation and processing |
| **DebugPadawan/JSON** | TextToJSON | Text to JSON conversion |
| **DebugPadawan/Debug** | Debug Print | Debugging and monitoring |
| **DebugPadawan/Timing** | Wait | Timing control and delays |
| **DebugPadawan/Utilities** | List Info | Data analysis helpers |
| **DebugPadawan/Logic** | Conditional String | Conditional operations |

---

## 🤝 Contributing

We welcome contributions! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features  
- 🔧 Submit pull requests
- 📖 Improve documentation

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Made with ❤️ by [DebugPadawan](https://github.com/DebugPadawan)**

</div>