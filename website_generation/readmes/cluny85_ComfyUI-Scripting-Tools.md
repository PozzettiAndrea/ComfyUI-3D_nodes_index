# ComfyUI-Scripting-Tools

## Description

A set of utility nodes for ComfyUI focused on scripting. Includes an enhanced UUID generator node.

### Node: Generate UUID (Enhanced)

This node allows you to generate UUIDs of type v1, v3, v4, and v5. You can specify:
- The UUID version (v1, v3, v4, v5)
- Namespace type (DNS, URL, OID, X500, or a custom UUID for v3/v5)
- Name string for v3/v5 UUIDs
- Optional prefix and suffix for the output string
- A trigger input to force regeneration

This is useful for generating unique identifiers in workflows, scripting, or for any automation that requires UUIDs with custom formatting.

### Node: Generate UUID String

This node generates a random UUID (version 4) and returns it as a string. You can optionally add a prefix and/or suffix to the generated UUID. The 'trigger' input can be used to force the node to re-execute and generate a new UUID.

**Inputs:**
- `trigger` (optional): Integer value to force regeneration (changing this value will re-run the node)
- `prefix` (optional): String to prepend to the UUID
- `suffix` (optional): String to append to the UUID

**Output:**
- `uuid_string`: The generated UUID string, with optional prefix and suffix

This node is useful for generating unique identifiers in your ComfyUI workflows, especially when you need a simple, random UUID.

### Installation

1. Clone this repository into the `custom_nodes` folder of your ComfyUI installation.
2. Restart ComfyUI.

### Usage

- The node "Generate UUID (Enhanced)" lets you generate UUIDs with advanced options for scripting and automation.

### License

MIT