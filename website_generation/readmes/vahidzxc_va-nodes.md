# VA Nodes for ComfyUI

A collection of custom nodes for ComfyUI, focusing on improving workflow efficiency and adding new functionality.(work in progress!!!)

## Features

### VA Seed Node
- Smart seed management with random generation
- Previous seed tracking
- Automatic workflow re-execution control
- Maximum seed value: 2^40 (1,099,511,627,776)

## Installation

1. Navigate to your ComfyUI custom nodes folder:
```bash
cd custom_nodes
```

2. Clone this repository:
```bash
git clone https://github.com/vahidzxc/va_nodes.git
```


3. Restart ComfyUI

## Requirements

- ComfyUI
- Python 3.10+

## Usage

### VA Seed Node

1. Add the VA Seed node to your workflow
2. Features:
   - Use the 🎲 button to generate random seeds
   - Previous seed value is tracked automatically
   - Smart re-execution control prevents unnecessary workflow runs
   - Supports seed values up to 2^40
