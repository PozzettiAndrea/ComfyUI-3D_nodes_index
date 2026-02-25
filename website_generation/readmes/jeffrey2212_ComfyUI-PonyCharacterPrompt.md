# Pony Character Prompt Picker for ComfyUI

This custom node for ComfyUI allows users to randomly select character prompts from an Excel file, specifically designed for pony character generation.

## Node Description

The Pony Character Prompt Picker node reads an Excel file specified by the user, allows manual selection of a tab, and randomly picks a cell value from a specified column, starting from row 3 to the end. The selected value is output as a string to the next node in the ComfyUI workflow.

## Features

- Read Excel files (.xlsx)
- Manually specify the sheet name
- Choose a specific column to pick values from
- Randomly select a value from the specified column, starting from row 3
- Output the selected value as a string

## Installation

1. Ensure you have ComfyUI installed and set up.
2. Clone this repository or download the files into your ComfyUI's `custom_nodes` directory:
