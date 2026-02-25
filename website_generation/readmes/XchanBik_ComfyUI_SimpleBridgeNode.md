# Custom ComfyUI Node: SimpleBridgeNode

## Overview

This repository provides a **custom node** for ComfyUI designed to facilitate the storage and retrieval of data with dynamic typing. The `BridgeStoreNode` allows users to store arbitrary data with a unique ID, and the `BridgeLoadNode` allows the data to be retrieved later using that ID. The data is stored along with its type, and the UI provides a dropdown to select the key for retrieval.

### Key Features:
- **Store arbitrary data** with a unique ID.
- **Retrieve data** dynamically using a stored ID from a dropdown.
- **Automatic type handling** ensures proper output wiring in the UI.
- **Customizable node pack** can be reused in different workflows.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/enhanced-bridge-node.git
