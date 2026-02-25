

https://github.com/user-attachments/assets/083e1c06-8dad-4f6e-823f-22330355a6ff



https://github.com/user-attachments/assets/012d1f26-b2ea-481e-9b9a-8b65504409a6



https://github.com/user-attachments/assets/a5f4c5e7-eb4b-47db-b791-daf6755518b0


# 🧑‍指揮 Orchestrator Node (Multi-Group & Auto-Discovery) for ComfyUI

An advanced, "zero-configuration" custom node for ComfyUI, designed to manage complex and modular workflows.

This node scans your graph for specific tags in the `[[GROUP:TAG]]` format and dynamically builds a control interface. It allows for the use of **multiple independent Orchestrator nodes** within the same workflow, each managing its own group of nodes, making it ideal for complex setups.

-----

## \#\# ✨ Features

  * **Multi-Group Management:** Use multiple Orchestrator nodes, each controlling a subset of your workflow via a unique `Group ID`.
  * **Automatic Discovery:** Automatically detects tags belonging to its group without any manual configuration.
  * **Dynamic Interface:** Creates toggle switches on the fly for each tag detected within its group.
  * **Exclusive Control:** Only one toggle can be active at a time within a single group.
  * **Common Nodes Ignored:** Untagged nodes always remain active.

-----

## \#\# 🚀 Usage

Operation is based entirely on how you name your nodes.

### Step 1: Add an Orchestrator Node and Set Its Group

  * Add the `Logic > Orchestrator (Auto-Discovery)` node to your graph.
  * In the node's `group_id` field, enter a unique name for the group you want to control. For example: `MODELS`.

### Step 2: Tag Your Target Nodes

Use a double-bracket syntax `[[GROUP_ID:TAG_NAME]]` in the titles of the nodes you want to control.

  * **Example for the `MODELS` group:**
      * Rename a KSampler to `[[MODELS:SDXL]] KSampler`.
      * Rename another KSampler to `[[MODELS:PONY]] KSampler`.

### Step 3: The Node Updates

After tagging your nodes, the Orchestrator node with the ID `MODELS` will scan the graph, find the `SDXL` and `PONY` tags belonging to its group, and create the corresponding toggle switches.

### Multi-Group Usage

You can repeat the process to manage other parts of your workflow independently.

1.  Add a **second Orchestrator node**.
2.  Give it a different `group_id`, for example, `STYLES`.
3.  Tag other nodes accordingly: `[[STYLES:Cinematic]]`, `[[STYLES:Anime]]`.

The second node will create the `Cinematic` and `Anime` toggles and will only control those nodes, never interfering with the `MODELS` group.

-----

## \#\# How It Works

On load, each Orchestrator node reads its own `Group ID`. It then iterates through all other nodes in the graph, looking for tags in the `[[GROUP:TAG]]` format. If a tag's `GROUP` matches the node's `Group ID`, it adds the `TAG` to its list of options and builds its UI accordingly. This ensures that each Orchestrator only manages the nodes explicitly assigned to it.
