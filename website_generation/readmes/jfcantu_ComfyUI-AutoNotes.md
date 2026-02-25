# ComfyUI-AutoNotes

An intelligent note-taking extension for ComfyUI that automatically displays relevant notes based on your workflow context.

## 🤔 Why use this?

From time to time, I've found myself wanting to take notes on my experimentation, but usually in a specific context - what sampler settings work well with a particular checkpoint, what prompts work well and don't well, what a particular checkpoint is good/bad at, and so on.

The problem is keeping those notes organized, and readily available while using ComfyUI. So I made this extension [by telliing Claude Code what to do], with the following goals:

- **Easy to access**: Notes should be readily available and easy to edit.
  - Notes appear in the sidebar, and can be edited with a single click.
  - Notes can be pinned to the sidebar, so that they always appear regardless of context.
- **Context-specific**: I don't want to have to scroll through a giant text blob, or search through multiple text blobs to find what I need.
  - Notes can be configured to automatically appear only when wanted, using a variety of triggers:
    - When at least one of a list of nodes is present in a workspace.
    - When at least one of a list of nodes is selected.
    - When a specific node is present/selected, AND a specific attribute on the node matches a condition.
- **Easy to organize**: I want to be able to find/filter notes easily.
  - Notes can be organized into folders, and assigned tags which can be used for searching/filtering.

## 😃 Neat! How do I get it?

### Quick Install (Recommended)

Use [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager):

1. Open ComfyUI Manager
2. Search for "AutoNotes"
3. Click Install
4. Restart ComfyUI

### Manual Install

1. Navigate to your ComfyUI custom nodes directory:

   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:

   ```bash
   git clone https://github.com/jfcantu/ComfyUI-AutoNotes.git
   ```

3. Restart ComfyUI

The AutoNotes sidebar will appear on the right side of your interface.

## 😨 Okay, now how do I use it?

### Creating Your First Note

#### Option 1: Quick Add

1. Click the **Add** button in the sidebar.
2. Give your note a name, and select a folder for it to go in.
3. Start typing!

#### Option 2: Smart Add from Selected Node

1. Two options:
   1. Right-click any node in your workflow and select **"Create AutoNote for this node"**.
   2. Click any node in your workflow, and click "Add From Current Node" on the sidebar.
2. A dialog will appear for configuring your new note. It will be pre-configured with trigger conditions for that node type and its current settings.

### Display Modes

Switch between two display modes using the dropdown:

- **All**: Shows all notes.
- **Automatic**: Shows only relevant notes based on trigger conditions.

### Setting Up Triggers

Triggers control when notes automatically appear. Edit a note to configure its triggers:

#### "Node Selected" Trigger

Shows the note when you select specific node types.

**Example**: Create a note with tips about LoRA usage.

- Trigger Type: `Node Selected`
- Node Types: `LoraLoader`

This note will automatically appear whenever you select a LoRA loader node, and disappear when you deselect it.

#### "Node Selected + Attribute" Trigger

Shows the note when you select a specific node type, and that node has certain attribute values.

**Example**: Document settings for your favorite checkpoint

- Trigger Type: `Node Attribute`
- Node Type: `CheckpointLoaderSimple`
- Attribute Name: `ckpt_name`
- Attribute Values: `myFavoriteModel.safetensors`

This note will only appear when you select a CheckpointLoaderSimple node, AND the `ckpt_name` is set to `myFavoriteModel.safetensors`

#### "Node In Workflow" and "Node In Workflow + Attribute" Trigger

These are mostly identical to the previous two triggers. The only difference is that they will appear if the node or node+attribute combination is anywhere in the workflow, regardless of whether it's selected or not.

#### 📝 Workflow Name Trigger

Shows the note when the workflow filename contains specific text.

**Example**: Workflow-specific reminders

- Trigger Type: `Workflow Name`
- Workflow Names: `portrait`, `character`

This note will appear if "portrait" or "character" appear in the workflow name.

## 💡 Example Use Cases

### Model Documentation

Create notes for each checkpoint or LoRA with optimal settings, trigger words, and usage tips. They'll appear automatically when you select that model.

### Node Usage Guides

Document complex nodes with usage instructions that appear when you select them. Great for nodes you don't use every day.

### Workflow Templates

Pin step-by-step checklists for common workflows (portraits, landscapes, upscaling, etc.).

### Troubleshooting Tips

Create notes triggered by problematic node combinations to remind yourself of known issues and solutions.

### Quick Reference

Pin keyboard shortcuts, color management notes, or other frequently-needed information.

## 🛠️ Technical Details

### Data Storage

Notes are stored per-user in your ComfyUI user directory:

```text
ComfyUI/user/<username>/autonotes/
├── notes.json    # All note content and metadata
└── folders.json  # Folder organization
```

### API Endpoints

The extension provides REST API endpoints:

- `GET /autonotes/notes` - Retrieve filtered notes
- `POST /autonotes/notes` - Create note
- `PUT /autonotes/notes/{uuid}` - Update note
- `DELETE /autonotes/notes/{uuid}` - Delete note
- `GET /autonotes/folders` - Retrieve folders
- `POST /autonotes/folders` - Create folder
- `PUT /autonotes/folders/{uuid}` - Update folder
- `DELETE /autonotes/folders/{uuid}` - Delete folder

### Project Structure

```text
ComfyUI-AutoNotes/
├── __init__.py              # Extension entry point
├── autonotes.py             # Python backend (data management, API)
├── web/
│   └── autonotes.js         # JavaScript frontend (UI, interactions)
├── pyproject.toml           # Project metadata
└── README.md                # This file
```

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make changes with proper documentation.
4. Add tests for new functionality.
5. Submit a pull request.
