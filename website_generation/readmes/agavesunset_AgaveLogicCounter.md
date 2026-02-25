# AgaveLogicCounter
Solves the complex "For-Loop" logic in ComfyUI. Perfect for controlling multi-subject vs. multi-scene batch workflows.
# AgaveLogicCounter for ComfyUI

A sophisticated logic controller node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), designed to handle complex batch processing, nested loops (Cartesian products), and stateful integer cycling.

> **Status:** Active & Tested
> **Category:** Logic / Control Flow

## 🎯 The Problem it Solves
In standard ComfyUI workflows, creating a "Nested Loop" (e.g., iterating through 20 subjects against 6 backgrounds) is difficult. Standard primitives or random nodes cannot easily synchronize two different timelines (Inner Loop vs Outer Loop).

**AgaveLogicController** acts as a unified engine that outputs two synchronized signals:
1.  **Value**: The fast-moving index (e.g., 0, 1, 2, 3, 4, 5, 0...) -> *Controls the Inner Loop*
2.  **Cycle**: The slow-moving counter (e.g., 0, 0, 0, 0, 0, 0, 1...) -> *Controls the Outer Loop*
* **group_key**: *(Optional)* Advanced Synchronization.
    * By default, each node maintains its own independent counter.
    * If you enter the same string (e.g., `"sync_A"`) into multiple nodes, they will **share the same internal state**.
    * **Use Case**: Perfect for synchronizing a "Load Image" node at the start of your workflow with a "Save Image" node at the end, without dragging long wires across the canvas.
## ✨ Features

* **Dual Output System**: Simultaneously outputs the current step value and the completed cycle count.
* **State Persistence**: Uses `IS_CHANGED` logic to strictly maintain count state across queue batches.
* **Flexible Modes**:
    * `increment`: Standard linear counting (0 -> End).
    * `decrement`: Reverse counting.
    * `fixed`: Static output.
    * `randomize`: Random integer within range.
* **Grouping**: Supports `group_key` to synchronize or isolate counters across different parts of the workflow.
* **Smart Reset**: Separate controls for full reset vs. cycle-only reset.

## 🛠 Installation

1.  Clone this repository into your ComfyUI custom nodes directory:
    ```bash
    cd ComfyUI/custom_nodes
    git clone [https://github.com/agavesunset/AgaveLogicCounter.git](https://github.com/agavesunset/AgaveLogicCounter.git)
    ```
2.  Restart ComfyUI.
3.  Find the node under `Agave/Logic` -> `Cyclic Int Controller`.

## ⚙️ Usage Guide

### Parameters
* **mode**: Set to `increment` for standard looping.
* **start / end**: Defines the range (Inclusive).
    * *Example:* For 6 images, set `start=0`, `end=5`.
* **step**: The increment value per execution (usually 1).
* **group_key**: (Optional) Use the same string to share the counter between multiple nodes.
* **reset**: Force resets the counter to 0.

### Example: The "Subject x Scene" Workflow
**Goal:** You have **20 Subjects** (Image B) and **6 Scenes** (Image A). You want to generate every subject in every scene (120 total generations).

**Configuration:**
* **Node**: Agave Cyclic Int Controller
* `start`: 0
* `end`: 5  (This creates a modulo-6 loop)
* `step`: 1

**Wiring:**
* **Output `value`** (0-5) ---> Connect to **Scene Loader** (Image A) `index` input.
* **Output `cycle`** (0,1,2...) ---> Connect to **Subject Loader** (Image B) `index` input.

## 📝 License
[MIT License](LICENSE)
