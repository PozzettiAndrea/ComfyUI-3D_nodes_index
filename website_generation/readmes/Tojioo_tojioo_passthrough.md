# Tojioo Passthrough Nodes for ComfyUI

Typed passthrough nodes to reduce wire clutter in subgraphs. Includes a multi-type dynamic passthrough, and utility nodes for batch switching among other various quality-of-life improvements.

### Nodes

* **Simple Passthroughs**: Image, Mask, Latent, CLIP, Model, VAE, ControlNet, SAM Model, String, Int, Float, Bool. Muted or bypassed predecessor nodes are gracefully handled (treated as `None`).
* **Conditioning Passthrough**: Positive and negative conditioning. Handles missing/muted inputs.
* **Multi-Passthrough Hub**: Optional inputs with typed outputs.
* **Utility Nodes**:
  + Dual CLIP Text Encode: Encodes positive and negative prompts into conditioning using a shared CLIP model.
  + Tiled VAE Settings: Provides tiled VAE encoding/decoding settings as connectable outputs.
* **Dynamic Nodes**:
  + Dynamic Passthrough: Flexible multi-input passthrough with type mirroring
  + Dynamic Any: Single input passthrough with type mirroring
  + Dynamic Bus (Beta): Context/bus for carrying multiple typed values
  + Dynamic Preview (Beta): Tabbed multi-input preview with interactive controls
* **Batch Switch Nodes**: Any Image, Mask, Latent, Conditioning Batch Switch
* **Switch Nodes**: Any Image, Mask, Latent, CLIP, Model, VAE, ControlNet, SAM Model, String, Int, Float, Bool Switch

### Install

#### Manager

Open ComfyUI → Manager → Install Custom Nodes → search "Tojioo Passthrough" → Install → Restart.

#### Git

```
cd ComfyUI/custom_nodes
git clone https://github.com/Tojioo/tojioo_passthrough.git
```

Restart ComfyUI.

### Usage

**Category Structure:**

* `Tojioo Passthrough`: Multi-Passthrough hub
* `Tojioo Passthrough/Simple Passthrough`: All typed passthroughs, Conditioning Passthrough
* `Tojioo Passthrough/Simple Passthrough/Widget Variants`: Widget-based versions of primitive passthroughs
* `Tojioo Passthrough/Dynamic Nodes`: Dynamic Passthrough, Dynamic Bus, Dynamic Any
* `Tojioo Passthrough/Dynamic Nodes/Batch Switch Nodes`: Batch switching nodes
* `Tojioo Passthrough/Dynamic Nodes/Switch Nodes`: First-valid switching nodes

---

#### Dual CLIP Text Encode

* Purpose: Encode a positive and negative text prompt into conditioning using a single shared CLIP model, keeping the two encode nodes consolidated.
* Behaviour:
  + Accepts one CLIP input and two text widgets (positive, negative)
  + Outputs separate `positive` and `negative` CONDITIONING values

#### Tiled VAE Settings

* Purpose: Bundle tiled VAE encoding/decoding parameters into connectable outputs so they can be routed cleanly through subgraphs without wiring individual widgets.
* Behaviour:
  + Exposes `tile_size`, `overlap`, `temporal_size`, and `temporal_overlap` as typed outputs
  + Default values: tile_size 512, overlap 64, temporal_size 64, temporal_overlap 8
  + All values are adjustable via the built-in widget controls

#### Example:

<img alt="v1 7 0_Nodes" src="https://github.com/user-attachments/assets/6c7f84a6-14dd-4578-bb8d-503e928fe6c7" />


---

#### Batch Switch Nodes

* Purpose: Combine multiple compatible inputs into a single batch while keeping wiring tidy.
* Behaviour:
  + Starts with one slot, adds a new slot when the last one gets connected
  + With a single connected input, passes through unchanged
  + With multiple connected inputs, builds a batch when shapes are compatible
  + Muted or bypassed upstream nodes are treated as missing and ignored

#### Example:

<img alt="image" src="https://github.com/user-attachments/assets/97cf66cd-307e-40e6-a8be-9a014b70a3c5" />

---

#### Switch Nodes

* Purpose: Select the first valid connected input, based on slot order.
* Behaviour:
  + Dynamic inputs auto-add slots
  + Returns the first connected input by slot number
  + Muted or bypassed upstream nodes are treated as missing and ignored

#### Example:

<img alt="image" src="https://github.com/user-attachments/assets/4eabfea0-4ec4-4a38-83e8-fb391b60afeb" />

---

#### Dynamic Passthrough

* Purpose: A flexible multi-input passthrough where slot types mirror what you connect.
* Behaviour:
  + Dynamic inputs and outputs, slots grow as you connect
  + Output slot types mirror their corresponding connected input types
  + Updates live as connections change

#### Example:

<img alt="image" src="https://github.com/user-attachments/assets/311f7d35-2895-4527-9113-d8c4eaa3aa96" />

---

#### Dynamic Preview (Beta)

* Purpose: In-graph image viewer for quick A/B checks across multiple IMAGE inputs.
* Behaviour:
  + Accepts multiple IMAGE inputs and shows one at a time
  + Switch between inputs via the built-in tab selector
  + Includes interactive viewer controls
  + No outputs, this node is a pure viewer
  + Marked Beta because UI and behavior may change as the ComfyUI frontend evolves

#### Example (together with Dynamic Bus Node):

<img alt="image" src="https://github.com/user-attachments/assets/14202fa5-741a-417c-908c-2589086b2d4a" />

---

### License

GPL-3.0-only. See [LICENSE](LICENSE).

### Changelog

See [CHANGELOG](CHANGELOG.md).
