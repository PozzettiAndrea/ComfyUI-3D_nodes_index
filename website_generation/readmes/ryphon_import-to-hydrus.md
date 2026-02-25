# ComfyUI Import to Hydrus

## Overview

This project is a work in progress and should be mostly functional. However, it does not come with any assurances or guarantees.

## Setup

Before you start using Comfy, make sure to set `HYDRUS_KEY` and `HYDRUS_URL` in your environment variables. Alternatively, you can fill in the relevant information for your Hydrus server in the provided file within the project's repository. (`hydrus_api.txt`)

## Usage

Attach all the relevant inputs to get started.

### Workflow Setup

In this repo is a file "minimum.json". It requires WLSH, and RGThree, which are both excellent nodes to use anyway. This doesn't explicitly require them, but it absolutely utilizes the "info" from WLSH, and several pieces of RGthree.

As well, drag this image onto the ComfyUI page to load the workflow, and then you can use the ComfyUI manager to install all missing custom nodes.

![workflow](BasicFlow.png "Basic Workflo")

LORAs as a power loader output is open in a PR [here](https://github.com/rgthree/rgthree-comfy/pull/235).

### Hydrus API and Server

- Ensure your Hydrus API token is set up to import files and add tags as needed.
- Your Hydrus server must be accessible from the system running ComfyUI. Make sure your DNS settings are configured appropriately.

## Tags

The `tags` object accepts a comma-separated list of tags. To include namespaces, simply add them in the format `namespace:tag`.

**Example Tags:**
- `ai, comfyui, hyshare: ai`
- `namespace: tag, namespace2: tag, namespace: tag2`

All inputs except for the image are optional, but without them, the resulting image will have limited metadata.

## Metadata

By default, the node saves a significant amount of metadata to the generated PNG file. I've found it to be more useful than not, but if you don't want it included, don't attach the inputs to the node.

## Node Recommendations

- **[WLSH Nodes](https://github.com/wallish77/wlsh_nodes)**: These nodes export a substantial amount of data that can be useful for injection.
- **[RGThree Nodes](https://github.com/rgthree/rgthree-comfy)**: These nodes are excellent for organizing various elements of your workflow.
- **[CrysTools](https://github.com/crystian/ComfyUI-Crystools)**: These nodes provide effective pipeline tools to ensure data flows smoothly to the end of your workflow.


## Future Updates

If I think of more details or improvements, I will document them and ensure the README is formatted correctly in the coming days.

---

Feel free to contribute or provide feedback to improve this project!
