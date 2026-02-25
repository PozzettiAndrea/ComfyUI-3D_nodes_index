# ComfyUI-Satori

Investigative infrastructure for ComfyUI workflows. Based on the Green Tree Restaurant principle - create conditions for discovery without prescribing what will be discovered.

![satori](https://img.shields.io/badge/why_did_it-break%3F-00ff41)
![philosophy](https://img.shields.io/badge/investigate-don't_prescribe-ffb700)
![aesthetic](https://img.shields.io/badge/retrotech-phosphor_glow-ff00ff)

## Philosophy

Most diagnostic tools assume they know what you're looking for. Satori doesn't.

Instead of prescriptive measurements ("brightness is too high"), Satori provides investigative infrastructure that reveals what's actually happening in your workflows. You decide what matters.

## Features

### 🔍 why did it break?
The core investigative node. Place it anywhere in your workflow to understand:
- **Tensor landscape**: Statistical terrain of your data
- **Temporal changes**: What shifts between frames
- **Pattern detection**: Emergent behaviors in your pipeline
- **Channel dynamics**: How color information flows

All displayed directly on the node with retrotech aesthetics - ASCII histograms, phosphor glow, terminal readouts.

### ⏱️ temporal investigator
Specialized for frame-by-frame analysis. Essential for issues like FOUC where specific frames behave differently.

## Visual Language

Inspired by:
- Terminal phosphor displays
- ANSI art and ASCII visualization  
- Cassette futurism LED readouts
- Y2K/vaporwave aesthetics
- CRT scanlines and glitch patterns

Information density without overwhelm. Beauty through function.

## Installation

1. Clone into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-Satori
```

2. Restart ComfyUI

## Usage

### Investigation, Not Prescription

Place "why did it break?" nodes at points of interest:
- After transformations to see what changed
- Before/after problem areas
- At pipeline stages you don't understand

The node shows you what's there. You discover what matters.

### Example: FOUC Investigation

```
LoadImage → [why did it break?] → ImageBlend → [why did it break?] → VAE Encode
```

Compare the readouts. See the amplification. Understand without assumption.

### Modes

Configure investigation modes in the node:
- `tensor`: Statistical landscape and distribution
- `temporal`: Changes over time
- `patterns`: Emergent behaviors (coming soon)

## For Creative Professionals

Built for people who:
- Debug at 3am because they're engaged
- Need to see what tools actually do
- Question fundamental assumptions
- Integrate technical precision with creative flow

No credential checking. No hand-holding. Just investigation tools that respect your intelligence.

## Technical Details

- **Display method**: Uses addDOMWidget() for on-node visualization
- **Data philosophy**: Show everything, interpret nothing
- **Performance**: Minimal overhead, efficient analysis
- **Extensibility**: Modular investigation system

## The Green Tree Restaurant Principle

Like a restaurant where mathematicians and poets share tables, these tools create conditions for discovery without prescribing what you'll find. Today's brightness investigation might reveal tomorrow's timing issue.

## License

AGPL-3.0 - Keep it open, keep it investigative.

## Credits

Created for creative professionals doing sophisticated technical work. Inspired by those who operate at the intersections where categories break down.

---

*"The best discoveries happen when you create conditions for discovery without prescribing what will be discovered."*