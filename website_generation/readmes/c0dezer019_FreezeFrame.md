# ⏸️ FreezeFrame (Pausable Sampler)

A custom sampler node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to **Pause** generation mid-cycle and **Resume** it.

Useful for inspecting intermediate steps, managing GPU/CPU heat, or simply halting a long render without losing progress. This is particularly useful if you are on older hardware that causes gens to be longer than a minute.

This is a rebuild of the KSampler and Advanced KSampler and simply inserts a listener, signaler, and a trigger into the loop, effectively creating a "trap." There is a running loop that loops back around after each step is performed. all this does is tell the loop to wait while the state is "paused."

<img width="485" height="515" alt="image" src="https://github.com/user-attachments/assets/e51cfd23-1c37-4132-ac53-88f43d8f9f27" />


---

## ✨ Features

* **🛑 Live Pause/Resume:** Hit "PAUSE" mid-generation to hold the current state. The process stays alive in RAM.

---

## ⚠️ Important Note
**Changes made during a Pause do NOT affect the current run.**
If you pause and change the CFG slider, the current generation will finish using the *original* CFG value. The new settings will only apply to the **next** job you queue.

---

## 📦 Installation

1.  Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone [https://github.com/YourUsername/ComfyUI-Pause.git](https://github.com/YourUsername/ComfyUI-Pause.git)
    ```
3.  **Restart ComfyUI.**

---

## 🛠️ The Nodes

### 1. ⏸️ Pausable Sampler (Standard)
A drop-in replacement for the standard KSampler.
* **How to use:** Connect it exactly like a normal KSampler.
* **Controls:** Adds "PAUSE" and "RESUME" buttons directly on the node.

### 2. ⏸️ Pausable Sampler (Advanced)
A drop-in replacement for KSampler (Advanced).
* **Extra Features:** Exposes `add_noise`, `start_at_step`, `end_at_step`, and `return_with_leftover_noise` for complex workflows.

---

## 📜 License

MIT License.
