# ComfyUI Mask to Center Point Nodes

This pack provides two custom nodes for ComfyUI designed to find the center coordinates of masks and segments. They are useful for workflows where you need to precisely identify the location of objects or regions of interest.

## Features

* **Multiple Input Types:** Accepts both standard `MASK` and `SEGS` (from nodes like the Impact Pack) inputs.
* **Two Distinct Nodes:**
    1.  **Mask to Center Point:** For finding the center of whole masks or separating physically disconnected masks.
    2.  **Detect Mask Sub-Masses (WIP):** For advanced analysis of a single, irregular mask to find the centers of its dense areas.
* **Flexible Modes:**
    * `Combined`: Finds the single center of mass for all provided masks/segments.
    * `Separate Regions`: Finds the individual centers of multiple, non-contiguous masks.
* **Noise Filtering:** Includes a `min_area` parameter to ignore small, noisy masks.
* **Detailed Debug Output:** Provides a clear, text-based summary of the operations performed, including areas and coordinates found.
* **Simple Coordinate Outputs:** Provides the final coordinates in multiple formats: a clean JSON string of the coordinate(s) (compatible with SAM2 nodes), and, separately, the first X and Y coordinates as integers (first detected mask only)

## Usage & Behavior

* **Input Priority:** If both `mask` and `segs` inputs are connected, the node will **prioritize and process the `segs` input**, ignoring the `mask`.
* **Mask Batch Handling:** The nodes are fully compatible with mask batches. They will iterate through and process **every mask in the batch** individually.
* **SEGS Handling:** When `segs` are provided, the nodes process each segment from the list.
    * In `Combined` mode, all segment masks are reconstructed onto a single canvas before processing.
    * In `Separate Regions` mode, each segment's mask is analyzed individually within its own cropped region.

## Installation

### 1. Clone the Repository

1.  Open a terminal or command prompt.
2.  Navigate to your ComfyUI `custom_nodes` directory. For example:
    ```bash
    cd C:\Users\YourName\Desktop\ComfyUI_windows_portable\ComfyUI\custom_nodes
    ```
3.  Clone the repository using the following command:
    ```bash
    git clone https://github.com/9nate-drake/ComfyUI-MaskCenter
    ```
    This will create a `ComfyUI-MaskCenter` folder inside `custom_nodes`.

### 2. Install Requirements

If you've got other custom nodes installed, these libraries are probably already installed. Otherwise, follow the instructions for your specific ComfyUI version to install the required Python libraries. 

#### Method A: Standard/Manual Installation

These instructions are for users who installed ComfyUI manually (e.g., via `git clone`).

1.  **Activate your Python virtual environment (venv).** In your terminal, navigate to your main ComfyUI directory and activate your venv:
    ```bash
    # On Windows
    .\venv\Scripts\activate
    
    # On Linux/macOS
    source venv/bin/activate
    ```
2.  **Install the requirements:**
    ```bash
    pip install -r custom_nodes/ComfyUI-MaskCenter/requirements.txt
    ```
3.  Restart ComfyUI.

#### Method B: Portable Installation

These instructions are for users of the standalone portable version of ComfyUI.

1.  **Open a standard command prompt or PowerShell.**
2.  **Navigate to your ComfyUI portable directory's root.** For example:
    ```bash
    cd C:\Users\YourName\Desktop\ComfyUI_windows_portable
    ```
3.  **Run the pip install command using the embedded Python:**
    ```bash
    .\python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-MaskCenter\requirements.txt
    ```
4.  Once it's finished, you can close the command prompt and restart ComfyUI.

## Nodes

### 1. Mask to Center Point

This is the primary node for most use cases. It finds the geometric center of masks.

#### Inputs

* **mode** (`Dropdown`):
    * `Combined`: Treats all input masks/segments as a single entity and calculates one center point for the entire group.
    * `Separate Regions`: Calculates the center point for each physically disconnected mask or segment individually.
* **min_area** (`Int`): The minimum number of pixels a mask must have to be processed. Useful for ignoring small artifacts or noise.
* **mask** (`MASK`, optional): A standard ComfyUI mask tensor. Can be a batch of masks.
* **segs** (`SEGS`, optional): Segment data, compatible with the format from the Impact Pack.

#### Outputs

* **coordinates** (`STRING`): A JSON-formatted string containing a list of all found coordinates. Example: `[{"x": 100, "y": 150}, {"x": 320, "y": 240}]`
* **x** (`INT`): The X-coordinate of the *first* point found.
* **y** (`INT`): The Y-coordinate of the *first* point found.
* **debug** (`STRING`): A detailed log of the process, including the number of masks found, their areas, and whether they were processed or skipped.

### 2. Detect Mask Sub-Masses (WIP)

This is an advanced node for analyzing a single, complex mask that might have several dense areas connected by narrow "bridges". It intelligently severs these narrow connections to find the center of each larger part.

#### Inputs

* **separation_strength** (`Int`): Controls how aggressively the node severs connections. A higher value will break thicker "bridges" between dense areas.
* **mask** (`MASK`, optional): A standard ComfyUI mask tensor. Can be a batch of masks.
* **segs** (`SEGS`, optional): Segment data. Each segment will be analyzed individually for sub-masses.

#### Outputs

* **coordinates** (`STRING`): A JSON-formatted string of the centers of the detected sub-masses.
* **x** (`INT`): The X-coordinate of the *first* sub-mass center found.
* **y** (`INT`): The Y-coordinate of the *first* sub-mass center found.
* **debug** (`STRING`): A detailed log of the detection process.