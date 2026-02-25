# ComfyUI Prompt Studio

A rich, feature-packed prompt editor designed for ComfyUI and other AI applications. ComfyUI Prompt Studio provides an intuitive interface for creating, editing, and managing complex prompts with real-time compilation, custom chants, LoRA support, and intelligent autocompletion.

## Features

- **Real-time Compilation**: Prompts are automatically compiled as you type and changes are reflected instantly in the underlying text area
- **Advanced Prompt Editor**: Rich text editing with syntax highlighting and tag recognition
- **Custom Chants System**: Create reusable prompt templates with variables and descriptions
- **LoRA & Embedding Support**: Built-in support for LoRA and embedding tags with proper formatting
- **Intelligent Autocompletion**: Context-aware suggestions based on tag databases and custom definitions
- **Live Preview**: See your compiled prompt output update in real-time as you make changes
- **Flexible Integration**: Works as an overlay on any text area in ComfyUI and other applications

## Installation

### ComfyUI Installation

1. **Download the extension:**
   - Clone or download this repository to your ComfyUI `custom_nodes` directory
   - Path should be: `ComfyUI/custom_nodes/ComfyUI-Prompt-Studio/`
2. **Install dependencies:**

   ```bash
   cd ComfyUI/custom_nodes/ComfyUI-Prompt-Studio
   pip install -r requirements.txt
   ```

3. **Restart ComfyUI:**
   - Restart your ComfyUI instance
   - The extension will automatically load and be available on text input fields

## Quick Start

### Basic Usage

1. **Open the editor:**
   - Click on any text input field in ComfyUI
   - Press <kbd>Ctrl+Space</kbd> to open the ComfyUI Prompt Studio editor

2. **Write your first prompt:**

   ```text
   1girl, beautiful, looking at viewer, smile
   ```

   - Type normally - you'll see syntax highlighting and autocompletion
   - The compiled prompt appears in real-time in the preview panel

3. **Use autocompletion:**
   - Start typing a tag name like "bea..."
   - Press <kbd>Ctrl+Space</kbd> or wait for suggestions to appear
   - Use arrow keys to navigate, <kbd>Tab</kbd> or <kbd>Enter</kbd> to accept

4. **Add weights to tags:**
   - Type `(beautiful:1.2)` for increased emphasis
   - Use `[[beautiful]]` for reduced emphasis
   - Use <kbd>Ctrl+Up</kbd> / <kbd>Ctrl+Down</kbd> arrows to adjust weights quickly

### Working with Custom Chants

Create a chant in the right panel:

```text
@@quality
  /// High quality rendering tags
  masterpiece, best quality, high quality
  ultra-detailed, highly detailed
```

Use the chant in your prompt:

```text
@quality, 1girl, beautiful
```

See real-time expansion:

- The preview panel shows the expanded version
- Your original prompt structure is preserved

Add LoRA models:

```text
<lora:character_model:0.8>
1girl, specific_character_name
```

Use embeddings:

```text
<embedding:negative_embedding:0.9>
bad_quality, blurry
```

Combine everything:

```text
@quality, 1girl, beautiful
<lora:style_model:0.7>
// This is a comment that won't appear in output
smile, looking at viewer
```

### Tips for New Users

- **Start simple:** Begin with basic tags and gradually add complexity
- **Use the preview:** Always check the preview panel to see your compiled output
- **Experiment with weights:** Try different emphasis levels to see what works
- **Save your chants:** Create reusable chants for common tag combinations
- **Check the help panel:** Click the Help button for detailed documentation

## User Interface

### Main Window Layout

The ComfyUI Prompt Studio interface consists of three main panels:

#### Left Panel - Prompt Editor

- **Primary editing area** for writing your prompts
- Supports all tag types: normal tags, custom chants, LoRA, and embeddings
- **Syntax highlighting** with different colors for different tag types
- **Real-time validation** with visual indicators for invalid or unregistered tags
- **Autocompletion** triggered by typing or `Ctrl+Space`

#### Right Panel - Chants Editor

- **Define custom chants** using the `@@name` syntax
- Write **reusable prompt templates** with descriptions
- **Comments support** using `///` for chant descriptions
- **Real-time expansion** of chants in the preview panel as you type

#### Bottom Panel - Preview/Settings/Help

Three mutually exclusive panels that can be toggled:

- **Preview Panel**: Shows the final compiled prompt output in real-time with all chants resolved and comments removed
- **Settings Panel**: Configure editor appearance, compilation options, and data sources
- **Help Panel**: Comprehensive documentation and keyboard shortcuts

## Prompt Syntax

### Tag Types

ComfyUI Prompt Studio supports four main types of tags:

#### Normal Tags

Standard tags that form the core of your prompt.

```text
1girl, looking_at_viewer, smile
((masterpiece)), (best quality:1.2)
[[sky]], (dark:0.8)
```

**Features:**

- Automatic underscore/space conversion based on settings
- Weight syntax using parentheses `(tag:1.2)` or brackets `[[tag]]`
- Comments support using `//` or `/* */` syntax
- **Minus notation**: Use `-tag` or `-<lora:name>` to delete/remove previous tags (interpreted as weight 0.0)

#### Custom Chants

User-defined reusable prompt templates prefixed with `@`.

```text
@quality, @character:girl, @pose:standing
```

**Usage:**

- Reference: `@chant_name` or `@chant_name:weight`
- Chants can include multiple tags and even LoRA/embedding references
- Weights are applied to all tags within the chant

#### Embedding Tags

Tags for textual inversions and embeddings.

```text
<embedding:embedding_name>
<embedding:embedding_name:0.9>
```

#### LoRA Tags

Specialized tags for LoRA (Low-Rank Adaptation) models.

```text
<lora:model_name.safetensors:0.8>
<lora:model_name:0.7:extra_params>
```

### Chants Definition Syntax

Define custom chants in the right panel using this syntax:

```text
@@quality_high
  /// High quality prompts for detailed artwork
  masterpiece, best quality, high quality
  ultra-detailed, highly detailed

@@character_girl
  /// Basic female character setup
  1girl, solo, beautiful detailed face
  looking at viewer

@@style_anime
  /// Anime art style modifiers
  anime, manga style, cell shading
  vibrant colors, sharp lines
```

**Syntax Rules:**

- **Label**: `@@chant_name` starts a new chant definition
- **Description**: Lines starting with `///` are treated as descriptions
- **Content**: All other lines are treated as prompt content
- **Comments**: Use `//` for single-line comments and `/* */` for multi-line comments

### Weight and Modifier Syntax

#### Parentheses Weights

```text
(tag:1.2)        # Increase emphasis
(tag:0.8)        # Decrease emphasis
((tag))          # Double emphasis (equivalent to :1.21)
(((tag)))        # Triple emphasis (equivalent to :1.331)
```

#### Bracket Weights

```text
[[tag]]          # Reduce emphasis (equivalent to :0.826)
[[[tag]]]        # Further reduce emphasis
```

#### Keyboard Shortcuts for Weights

- `Ctrl+Up Arrow`: Increase weight by 0.1
- `Ctrl+Down Arrow`: Decrease weight by 0.1

### Tag Deletion (Minus Notation)

You can delete or remove previously added tags using minus notation:

```text
-1girl, -<lora:example>
```

**How it works:**

- Tags prefixed with `-` are interpreted as having a weight of 0.0
- Tags with zero weight have the special effect of deleting previous occurrences
- Works with all tag types: normal tags, LoRA, embeddings, and chants
- Adding a regular tag afterward will restore the deleted tags

**Examples:**

```text
1girl, beautiful, -1girl, 2girls  # Results in: beautiful, 2girls
<lora:model:0.8>, -<lora:model>, <lora:other:0.5>  # Results in: <lora:other:0.5>
```

## How Prompts Are Processed

As you type, your prompt automatically goes through several processing steps in real-time:

1. **Comment Removal**: All comments (`//` and `/* */`) are stripped from the prompt
2. **Chant Resolution**: Custom chants (e.g., `@quality`) are expanded to their full content
3. **Duplicate Handling**: Duplicate tags are processed according to your settings:
   - **Overwrite**: Later occurrences replace earlier ones
   - **Multiply**: Weights are multiplied together
   - **Add**: Weights are added together
   - **Ignore**: First occurrence is kept, duplicates are ignored
4. **Normalization**: Tags are normalized according to underscore/space settings
5. **Source Embedding**: Original prompt is compressed and embedded as a comment for restoration

### Example Transformation

**Input:**

```text
@quality, 1girl, looking_at_viewer
// This is a comment
<lora:style_model:0.8>
```

**With chant definition:**

```text
@@quality
  /// High quality tags
  masterpiece, best quality
```

**Output:**

```text
masterpiece, best quality, 1girl, looking_at_viewer, <lora:style_model:0.8>

/*# PROMPT_STUDIO_SRC: <compressed_original_data> */
```

## Data Sources

### Dictionary Sources

ComfyUI Prompt Studio uses various data sources for autocompletion and tag validation:

#### Built-in Sources

- **Tags**: Comprehensive database of tags with categories and aliases
- **E621 Tags**: Furry artwork tags from e621.net
- **Artist Database**: Artist names and associated URLs
- **Quality Tags**: Common quality and style modifiers

#### Custom Sources

You can configure data sources in the settings panel:

```text
# Dictionary Sources Configuration
https://example.com/tags.csv  # Remote dataset
./local/tags.csv  # Local file
# Lines starting with # are comments
```

**CSV Format** (headerless, UTF-8 encoded):

```csv
1girl,1,50000,"girl,female,woman"
looking_at_viewer,2,25000,eye_contact
masterpiece,5,40000,"best_quality,high_quality"
```

#### Source Configuration

- **Remote URLs**: Fetch data from web sources (e.g., `https://example.com/tags.csv`)
- **Local Files**: Load CSV files from your local system (e.g., `./local/tags.csv`)
- **Multiple Sources**: Combine multiple data sources for comprehensive coverage
- **CSV Format**: Headerless CSV files encoded in UTF-8 with columns: Tag, Category, Usage count, Comma-separated aliases

## Settings and Configuration

### Editor Settings

- **Font Family**: Choose your preferred coding font
- **Font Size**: Adjust text size for better readability
- **Line Height**: Control vertical spacing
- **Theme**: Light or dark mode support

### Compilation Settings

- **Normalization**: Convert between underscores and spaces
- **Escape Characters**: Handle special characters in prompts
- **Duplicate Handling**: Configure how duplicate tags are processed

### Data Settings

- **Dictionary Sources**: Add or remove tag databases
- **Auto-loading**: Configure automatic data loading on startup
- **Cache Settings**: Control how data is cached and updated

## Integration

### ComfyUI Integration

ComfyUI Prompt Studio integrates seamlessly with ComfyUI:

- **Overlay Mode**: Appears as an overlay on any text input field
- **Automatic Detection**: Detects ComfyUI text areas and provides enhanced editing
- **Workflow Integration**: Works with ComfyUI's workflow system and node-based interface

### Other Applications

The extension is designed to work with other applications:

- **Universal Text Areas**: Can be called from any text input field
- **Customizable Integration**: Settings can be adjusted per application
- **Extensible Architecture**: Easy to add support for new applications

## Keyboard Shortcuts

### General

- `Ctrl+Enter` or `OK` button: Close the editor
- `Ctrl+Space`: Trigger autocompletion

### Editing

- `Tab`: Accept current autocompletion suggestion
- `Ctrl+Up/Down`: Increase/decrease tag weight

### Navigation

- `Ctrl+Z`: Undo
- `Ctrl+Y`: Redo

## Advanced Features

### Restoration System

Original prompts are preserved even after compilation:

- Compressed using Brotli compression
- Embedded as comments in the output
- Allows full restoration of original prompt structure

### WASM Performance

- High-performance dictionary engine written in Rust
- Compiled to WebAssembly for fast search and filtering
- Handles large datasets efficiently

### Internationalization

- Multi-language support with i18n system
- Currently supports English and Japanese
- Easy to add new translations

## Development

### Requirements

- Node.js and npm/pnpm
- Rust toolchain for WASM compilation
- Modern browser with WebAssembly support

### Building

```bash
# Install dependencies
pnpm install

# Build WASM module
pnpm run build-wasm

# Start development server
pnpm run dev

# Build ComfyUI extension
pnpm run build-extensions-comfyui

# Run tests
pnpm run test
```

### Architecture

- **Svelte**: Frontend framework with custom element support
- **Web Components**: Custom elements for reusable UI components with encapsulation
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Rust/WASM**: High-performance dictionary engine
- **Jotai**: Robust state management with isolation and reactivity
- **daisyUI**: Pre-built components for rapid UI development
- **CodeMirror**: Advanced text editing capabilities
- **Paraglide**: Localization and internationalization support

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure code quality
5. Submit a pull request

## License

This project is open source. Please check the license file for specific terms and conditions.
