# Kumiho ComfyUI Custom Nodes 🦊

> **The Revolution Begins** - Connect your ComfyUI workflows with Kumiho Cloud asset management system.

[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Nodes-blue)](https://github.com/comfyanonymous/ComfyUI)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Kumiho](https://img.shields.io/badge/Kumiho-Cloud-orange)](https://kumiho.io)
[![Python SDK](https://img.shields.io/badge/SDK-v0.7.0%2B-brightgreen)](https://pypi.org/project/kumiho/)

## Overview

Kumiho ComfyUI Nodes seamlessly integrate ComfyUI with the Kumiho Cloud asset management platform. This enables:

- **Asset Versioning**: Automatically version your generated images, videos, and workflows
- **Dependency Tracking**: Track lineage and relationships between assets
- **Team Collaboration**: Share assets across your team with proper version control
- **Impact Analysis**: Understand downstream dependencies before making changes
- **BYO Storage**: Your files stay on your storage - only references are tracked

## Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI
2. Go to Manager > Install Custom Nodes
3. Search for "Kumiho"
4. Click Install

### Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/kumihoclouds/kumiho-comfyui.git
pip install -r kumiho-comfyui/requirements.txt
```

### Via pip

```bash
pip install kumiho-comfyui
```

## Authentication Setup (Required)

Before using Kumiho nodes, you must authenticate with Kumiho Cloud:

```bash
# Install the Kumiho CLI
pip install kumiho-cli

# Login to Kumiho Cloud (opens browser for OAuth)
kumiho-cli login

# Verify authentication is working
kumiho-cli whoami
```

This creates a `kumiho_authentication.json` file in your home directory (`~/.kumiho/`) that the SDK uses automatically.

> **Note**: You can also refresh your token anytime with `kumiho-cli refresh`

## Available Nodes

### Input/Output Nodes (`Kumiho/IO`)

#### 🔹 Kumiho Load Asset
Load assets from Kumiho Cloud using kref:// URIs or dropdown browsing.

**Inputs:**
- `project`: Project to load from (leave as auto to use the configured project)
- `space`: Space path (e.g., "checkpoint/flux")
- `item_name`: Item to load
- `item_kind`: Item kind (image, video, checkpoint, etc.)
- `kref_uri`: Direct kref:// URI (overrides the fields above)
- `tag / revision`: Revision tag or number (blank = latest)
- `artifact_name`: Artifact name (e.g., "preview")
- `fallback_file_path`: Local file path if kref resolution fails

**Outputs:**
- `file_path`: Resolved local file path
- `kref`: The kref URI of the loaded asset
- `metadata`: Metadata JSON for the resolved asset

#### 🔹 Kumiho Save Image
Save generated images to Kumiho Cloud as new revisions with automatic lineage tracking.

**Inputs:**
- `images`: Image tensor to save
- `space`: Target space path (e.g., "outputs/portraits")
- `item_name`: Name for the item
- `description`: Description for the revision
- `file_path`: (Optional) Custom save location - if provided, saves to this path instead of default
- `source_krefs`: (Optional) Source asset krefs for lineage tracking

**Outputs:**
- `kref`: The kref:// URI of the created revision

#### 🔹 Kumiho Save Video
Save generated videos to Kumiho Cloud with inline preview support.

**Inputs:**
- `images`: Image tensor (video frames) to save
- `space`: Target space path
- `item_name`: Name for the video item
- `description`: Description for the revision
- `file_path`: (Optional) Custom save location
- `frame_rate`: Video frame rate (default: 8)
- `format`: Video format (mp4, webm, gif)
- `source_krefs`: (Optional) Source asset krefs for lineage tracking

**Outputs:**
- `kref`: The kref:// URI of the created revision
- `video_preview`: Inline video preview for ComfyUI output panel

### Search Nodes (`Kumiho/Search`)

#### 🔹 Kumiho Search Items
Search for items across Kumiho projects and spaces using the SDK's `item_search()` function.

**Inputs:**
- `project`: Project to search within (leave as auto to use the configured project)
- `name_filter`: Filter by item name (supports wildcards like "hero*")
- `kind_filter`: Filter by item kind (model, texture, workflow, etc.)
- `context_filter`: Filter by project/space path (e.g., "project/*" or "*/characters/*")
- `limit`: Maximum number of results to return

**Outputs:**
- `krefs`: List of matching item kref URIs (iterative)
- `file_paths`: List of resolved file paths (iterative)

> **Note**: Items without valid artifacts are automatically skipped to prevent empty values downstream.

### Graph Nodes (`Kumiho/Graph`)

#### 🔹 Kumiho Create Edge
Create dependency relationships between revisions.

**Inputs:**
- `source_kref`: Source revision kref
- `target_kref`: Target revision kref
- `edge_type`: Relationship type (DEPENDS_ON, DERIVED_FROM, REFERENCED, CONTAINS, CREATED_FROM)

**Outputs:**
- `edge_id`: The created edge identifier

#### 🔹 Kumiho Tag Revision
Apply tags to revisions for easy retrieval.

**Inputs:**
- `revision_kref`: The revision to tag
- `tag`: Tag name (e.g., "approved", "published", "wip")

**Outputs:**
- `success`: Boolean indicating success

#### 🔹 Kumiho Get Dependencies
Get all dependencies of a revision.

**Inputs:**
- `revision_kref`: The revision to query
- `max_depth`: Maximum traversal depth (1-20)
- `edge_types`: Comma-separated edge types to filter

**Outputs:**
- `dependencies_json`: JSON with dependency information

## Configuration

### Authentication (Recommended)

The recommended way to authenticate is via the Kumiho CLI:

```bash
# Login (opens browser for OAuth)
kumiho-cli login

# Check authentication status
kumiho-cli whoami

# Refresh token if expired
kumiho-cli refresh
```

This creates `~/.kumiho/kumiho_authentication.json` which the SDK discovers automatically.

## Usage Examples

### Basic Workflow: Load, Process, Save

```
[Kumiho Load Asset] → [Your Processing Nodes] → [Kumiho Save Image]
         |                                               |
         ↓                                               ↓
    kref://project/textures/input.texture      kref://project/outputs/result.image
```

### Search and Process Multiple Assets

```
[Kumiho Search Items] → [Kumiho Load Asset] → [Processing] → [Kumiho Save Image]
    kind_filter: texture          ↑                                    |
    context_filter: */characters/*  |                                    |
                                    └────── iterative connection ────────┘
```

### Lineage Tracking Workflow

```
[Kumiho Load Asset] → [Processing] → [Kumiho Save Image]
         |                                    |
         ↓                                    ↓
    source_kref ─────────────────→ Creates DERIVED_FROM edge
```

### Video Generation with Preview

```
[AnimateDiff Nodes] → [Kumiho Save Video]
                              |
                              ↓
                      Inline video preview in output panel
                      + registered to Kumiho Cloud
```

## kref:// URI Format

Kumiho uses kref:// URIs to identify assets:

```
kref://project/space/item.kind?r=revision&a=artifact

Examples:
- kref://myproject/characters/hero.model
- kref://myproject/textures/skin.texture?r=latest
- kref://myproject/renders/final.image?r=5
- kref://myproject/workflows/processing.workflow?r=published
- kref://comfyui-project/outputs/video.video?r=1
```

## Python SDK Integration

The Kumiho ComfyUI nodes use the [kumiho-python SDK](https://pypi.org/project/kumiho/) (v0.7.0+).

```python
import kumiho

# Search for items
items = kumiho.item_search(
    name_filter="hero*",
    kind_filter="texture",
    context_filter="*/characters/*"
)

# Access item properties
for item in items:
    print(f"Project: {item.project}")
    print(f"Space: {item.space}")
    print(f"Kref: {item.kref}")
```

## API Documentation

For full API documentation, visit [docs.kumiho.io](https://docs.kumiho.io).

## Changelog

### Current
- **KumihoLoadAsset**: Added project dropdown, space text input, and `tag / revision` handling with revision/artifact kref output
- **KumihoSearchItems**: Added project selection to scope searches
- **Docs**: Updated inputs, outputs, and SDK usage examples to match v0.7.0+

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## Support

- 📚 [Documentation](https://docs.kumiho.io)
- 💬 [Discord Community](https://discord.gg/Utp2P8G69P)
- 🐛 [Issue Tracker](https://github.com/kumihoclouds/kumiho-comfyui/issues)
- 📧 [Email Support](mailto:support@kumiho.io)

## License

MIT License - see [LICENSE](LICENSE) for details.

---

Made with 🦊 by [Kumiho](https://kumiho.io)
