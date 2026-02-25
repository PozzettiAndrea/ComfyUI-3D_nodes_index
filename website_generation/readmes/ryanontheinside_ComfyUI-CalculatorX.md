 # ComfyUI CalculatorX

A fully interactive calculator node for ComfyUI. You can use it standalone for quick calculations without connecting it to anything, or optionally wire it into your workflow—build expressions visually, connect inputs as variables, and output the result when the workflow runs.

![Calculator standalone](assets/image.png)

## Features

- **Basic & Scientific modes** — toggle between standard arithmetic and trig/log/power functions
- **Variable inputs (A, B, C)** — optional float inputs (scalar or list) you can wire from other nodes and reference in expressions; lists enable sine waves and temporal scheduling
- **Three outputs** — `result_float`, `result_int`, `result_string`
- **Live preview** — expressions without variables evaluate instantly on `=`; expressions with variables evaluate server-side when queued

![Calculator in a workflow](assets/image_wf.png)

## Installation

Clone into your ComfyUI `custom_nodes` directory and restart:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ryanontheinside/ComfyUI-CalculatorX.git
```

No additional dependencies required.

## Other ComfyUI Projects

- [ComfyUI_RyanOnTheInside](https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside) — Main node pack
- [ComfyUI_ProfilerX](https://github.com/ryanontheinside/ComfyUI_ProfilerX) — Performance profiling
- [ComfyUI_ControlFreak](https://github.com/ryanontheinside/ComfyUI_ControlFreak) — Universal MIDI & gamepad mapping
