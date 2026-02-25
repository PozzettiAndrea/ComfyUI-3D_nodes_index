# 🤖 MechaBaby Workflow Tracer

**English** | [简体中文](./README_ZH.md)

An enhanced extension for ComfyUI that records, visualizes, and extracts the actual execution path of a workflow. It helps you "dehydrate" large, complex workflows to keep only the logic that really ran.

---

## 🌟 Core Features

### 1. Real-time Path Visualization
- **Execution Highlighting**: The currently running node is highlighted in **yellow**. Completed nodes are colored by role (see Node & Link Colors below).
- **Glowing Links**: Links that carried data between executed nodes are highlighted; link color indicates whether the source is a pure parameter source (orange), a parameter node (green), or a normal executed node (white).
- **Modern UI Compatible**: Works with ComfyUI's "Modern Node Design (Vue Nodes)".

### 2. Node & Link Colors
After a run, nodes and links are styled to show data flow:

| Type | Color | Meaning |
|------|--------|--------|
| **Currently running** | Yellow | Node currently executing |
| **Pure parameter source** | Orange | Executed node with **no input** from other executed nodes (e.g. CheckpointLoader, Empty Latent, CLIP Text Encode with only text input). Label: "(纯参数源)" |
| **Parameter node** | Green | Executed node whose **output** is used by at least one other executed node (e.g. model → KSampler, KSampler → VAE Decode). Label: "(参数)" |
| **Normal executed node** | White | Executed node whose output is not used by any other executed node (e.g. Save Image, end of chain). |

Links use the same colors: orange when the link comes from a pure parameter source, green when from a parameter node, white when from a normal executed node.

### 3. Precise Execution Statistics
- **Execution order**: Each node shows its execution sequence number(s).
- **Duration**: Per-node run time in seconds; for looped nodes, hover to see all run numbers and total duration.
- **Loop support**: Nodes that run multiple times show a compact list; hover to expand.

### 4. Jump to Error Node
- **Panel**: "⚠️ Jump to Error Node" focuses the canvas on the last node that caused an error.
- **Right-click**: Same option on the canvas context menu; the menu shows the error node ID when available.
- The error node is recorded automatically on execution failure.

### 5. Workflow Export
Two export modes:
- **🛠️ Pure Path**: Saves only nodes that were executed in the current run. Good for analyzing what actually ran.
- **🔗 Logic Integrity** (recommended): Keeps executed nodes and traces back all required ancestors (model loaders, global parameters, etc.).
  - Supports virtual links (e.g. `easy-use` setNode/getNode, Anywhere nodes).
  - Keeps nodes like `GeneralInput` so the exported JSON can be loaded and run as-is.

---

## 🚀 How to Use

1. **Panel**: Check **ON** to enable tracing; uncheck to stop (no performance impact). The panel is draggable and its position is remembered.
2. **Right-click**: On the canvas background you can toggle the tracer, show/hide the panel, clear records, or jump to the error node.
3. **Loops**: If a node runs multiple times, hover over its label to see the full list of run numbers and total time.

---

## 🛠️ Installation

1. Go to ComfyUI’s custom nodes directory: `ComfyUI/custom_nodes/`
2. Clone this repo:
   ```bash
   git clone https://github.com/MechaBabyAi/ComfyUI-MechaBaby-WorkflowTracer.git
   ```
3. Restart ComfyUI.

---

## ⚖️ Performance

The extension hooks only the LiteGraph rendering layer and runs during render frames. It does not change ComfyUI’s Python execution, so impact on generation speed is negligible.

---

## 📝 Changelog

### v0.3.0 (2025-02-01)
- **Added**: Parameter node tracking — nodes whose output is used by other executed nodes are highlighted in **green** and labeled "(参数)".
- **Added**: Pure parameter source tracking — executed nodes with no input from other executed nodes are highlighted in **orange** and labeled "(纯参数源)".
- **Changed**: Normal executed nodes (end of chain) are now highlighted in **white** for clearer contrast on dark backgrounds.
- **Changed**: Link colors match source type: orange (pure source), green (parameter node), white (normal).

### v0.2.0 (2025-02-01)
- **Added**: Jump to Error Node (panel button and right-click menu, with error node ID).
- **Added**: Auto-recording of the error node on execution failure.

---

## 🤝 Acknowledgments

Thanks to everyone who suggested improvements, especially around large workflows and Logic Integrity export.
