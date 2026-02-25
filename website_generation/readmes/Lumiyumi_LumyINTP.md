# ComfyUI-LumyINTP

INT+ node for ComfyUI with "control after generate" style functionality.

## Features

- **INTPlus**: Integer primitive with signal-controlled increment/decrement/randomize
  - `fixed` - No change
  - `increment` - Add 1 each execution
  - `decrement` - Subtract 1 each execution  
  - `random_seed` - Generate random seed (1 to max)
  
- **Signal input**: Connect any output to control when the mode applies
  - When signal is `None` or `False`: considered "inactive"
  - When signal has a value: considered "active"
  - Use `invert` toggle to flip this behavior

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Lumiyumi/LumyINTP.git
```

Restart ComfyUI after installation.

## Usage

1. Add the `INTPlus` node from `LumyLogic/Primitive+` category
2. Set your control mode
3. Optionally connect a signal to the `signal` input
4. The value updates based on your mode when the signal condition is met

## Credits

Contains code adapted from MIT-licensed ComfyUI custom node projects.
