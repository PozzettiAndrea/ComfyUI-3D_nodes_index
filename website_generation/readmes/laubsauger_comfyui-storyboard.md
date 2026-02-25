# ComfyUI Storyboard

This custom node for ComfyUI provides a markdown renderer to display formatted text and notes within your workflow.

![Node Inspector](https://raw.githubusercontent.com/laubsauger/comfyui-storyboard/refs/heads/main/docs/inspector_full.png)

## Features

### 📝 Markdown Renderer Node

- **Universal input acceptance** - Handles strings, lists, dictionaries, and complex objects
- **Intelligent formatting** - Auto-detects content type and applies appropriate rendering
- **Code syntax highlighting** - Built-in highlighting with automatic language detection
- **Smart code block detection** - No triple backticks required for standalone code
- **Pretty-print formatting** - Enhanced dictionary and object visualization
- **Deduplication logic** - Automatically removes duplicate content from list inputs

### 🔍 Node Inspector Node

- **Real-time inspection** - Live monitoring of connected node states and values
- **Multi-level tracking** - Traces values through complex upstream connection chains
- **Interactive UI** - Hover effects, scrollable interface, and clickable navigation
- **Connection inheritance** - Visual indicators showing which widgets inherit from inputs
- **Smart navigation** - Click-to-navigate to parent nodes with smooth viewport animation
- **Dual output modes** - Provides both structured data (lists/dicts) and passthrough outputs
- **Type visualization** - Color-coded socket types and connection state indicators
- **Segmented display** - Separate informational and selectable sections for optimal UX

### 🤖 OpenAI Chat GPT Node

- **Smart caching system** - Automatically caches identical requests to avoid redundant API calls
- **Visual cache status** - Real-time indicator showing "New", "Cached", or "Error" states  
- **Multi-model support** - Full GPT-4, GPT-3.5 model family with temperature controls
- **Advanced configuration** - JSON response formatting, seeded generation, custom parameters
- **Integrated API key management** - Secure configuration file handling
- **Error resilience** - Graceful error handling with informative status messages

### 🚀 Workflow Benefits

- **Debug-friendly** - Comprehensive inspection and visualization capabilities
- **Performance optimized** - Smart caching reduces API costs and latency
- **Developer-focused** - Enhanced debugging and development workflow tools
- **Production-ready** - Robust error handling and state management

---

## TypeScript Development Guide

This project now uses TypeScript for frontend development, following the same build mechanism as rgthree-comfy.

## Setup

1. Install dependencies:

   ```bash
   npm install
   ```

2. Build the project:

   ```bash
   python __build__.py
   ```

## Project Structure

- `src_web/` - TypeScript source files
  - `nodes/` - Node-specific frontend code
  - `common/` - Shared utilities
  - `typings/` - TypeScript type definitions
  - `scripts_comfy/` - Dummy files for ComfyUI imports
- `web/` - Compiled JavaScript output (auto-generated)

## Development Workflow

1. Make changes to TypeScript files in `src_web/`
2. Run `python __build__.py` to compile
3. The build script will:
   - Copy non-TS files from `src_web/` to `web/`
   - Compile TypeScript files to JavaScript
   - Fix import paths for ComfyUI compatibility
   - Process any SCSS files (if present)

## TypeScript Configuration

The project uses:

- ES2019 target for compatibility
- ESNext modules
- Strict type checking (with `noImplicitAny` disabled for easier migration)
- Path mappings for ComfyUI types

## Adding New Files

1. Create new `.ts` files in `src_web/`
2. Import ComfyUI modules using:

   ```typescript
   import { app } from "scripts/app.js";
   import { ComfyWidgets } from "scripts/widgets.js";
   ```

3. Use the build script to compile

## Tips

- The build script supports `--fix` flag to automatically add `.js` extensions to imports
- Type definitions for ComfyUI are provided by `@comfyorg/litegraph` and `@comfyorg/comfyui-frontend-types`
- Custom type definitions can be added to `src_web/typings/index.d.ts`
