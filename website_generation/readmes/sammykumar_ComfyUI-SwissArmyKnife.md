# ComfyUI-SwissArmyKnife

A collection of custom nodes for ComfyUI featuring Gemini AI integration for video and image analysis, with a complete development environment using GPU-accelerated containers.

## Features

- **🤖 Gemini AI Integration**: Video, image, and media analysis using Google's Gemini AI
- **🎨 Super LoRA Loader**: Advanced multi-LoRA management with enhanced UI (forked from nd-super-nodes)
- **🎮 JavaScript Widgets**: Enhanced ComfyUI interfaces with custom video controls
- **🐳 Dev Container Support**: GPU-enabled development environment with mmartial/ComfyUI-Nvidia-Docker
- **🧪 Full Testing Suite**: Python and JavaScript testing with CI/CD integration
- **⚡ Hot Reload Development**: Instant feedback for both backend and frontend changes

## Quick Start with Dev Container (Recommended)

The fastest way to get started is using the provided dev container with GPU support:

### Prerequisites

- Docker with NVIDIA Container Toolkit
- VS Code with Dev Containers extension
- NVIDIA GPU with drivers installed

### Setup

```bash
# Clone the repository
git clone https://github.com/sammykumar/ComfyUI-SwissArmyKnife.git
cd ComfyUI-SwissArmyKnife

# Open in VS Code
code .

# Use "Reopen in Container" from VS Code command palette
# OR run directly with Docker:
docker run --gpus all -v $(pwd):/workspaces/repo -p 8188:8188 \
  mmartial/comfyui-nvidia-docker:ubuntu24_cuda12.8-latest

# Inside the container, start ComfyUI:
./.devcontainer/run-comfy.sh
```

ComfyUI will be available at **http://localhost:8188** with your custom nodes automatically loaded.

## Manual Installation

### For ComfyUI Users

If you want to use the nodes in an existing ComfyUI installation:

```bash
# Go to your ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/sammykumar/ComfyUI-SwissArmyKnife.git

# Install dependencies
cd ComfyUI-SwissArmyKnife
pip install -e .

# Restart ComfyUI
```

### For Development

If you're contributing to the project or want to modify the nodes:

```bash
# Clone the repository
git clone https://github.com/sammykumar/ComfyUI-SwissArmyKnife.git
cd ComfyUI-SwissArmyKnife

# Install Python dependencies
pip install -e .
pip install ruff black mypy pytest opencv-python pillow

# Install JavaScript tooling
cd web
npm install

# Install pre-commit hooks
pre-commit install
```

**System Requirements:**

- Python 3.10+
- Node.js 20+ (for development)
- FFmpeg (for video processing)
- NVIDIA GPU (optional, for accelerated inference)

## Available Nodes

### Backend Nodes (Python)

- **GeminiUtilVideoDescribe**: Analyze videos using Gemini AI
- **GeminiUtilImageDescribe**: Analyze images using Gemini AI
- **GeminiUtilMediaDescribe**: Multi-media analysis functionality
- **Super LoRA Loader 🔪**: Advanced multi-LoRA loading with UI enhancements (from nd-super-nodes)
    - Load multiple LoRAs in a single node
    - Individual enable/disable controls per LoRA
    - Dual strength support (model and CLIP)
    - Automatic trigger word extraction
    - Template save/load system
    - Enhanced file picker with search
    - See [docs/LORA_MANAGER_INTEGRATION.md](docs/LORA_MANAGER_INTEGRATION.md) for details
- **VACE Annotators**: Video preprocessing nodes for VACE-Annotators integration
    - **VACE Annotator - Depth**: Generate depth maps (MiDaS, Depth Anything V2)
    - **VACE Annotator - Flow**: Compute optical flow (RAFT)
    - **VACE Annotator - Scribble**: Extract edge/scribble maps (Anime, General, Sketch)
    - Model caching, batch processing, configurable resolution
    - See [docs/nodes/vace-annotators/README.md](docs/nodes/vace-annotators/README.md) for details

### Web Extension (JavaScript)

- **Video Controls Widget**: Enhanced video timeline controls with trimming
- **Custom Styling**: Themed UI components that integrate with ComfyUI

## 🔐 API Key Configuration

### Required: Google Gemini API Key

To use the Gemini AI features, you'll need a Google Gemini API key:

1. **Get your API key**: Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. **Create API key**: Click "Create API Key" and copy the generated key
3. **Configure securely**:

    ```bash
    # Copy the environment template
    cp .env.example .env

    # Edit .env and add your actual API key
    GEMINI_API_KEY=your_actual_api_key_here
    ```

⚠️ **Security Note**: Never commit your actual API keys to version control. The `.env` file is already included in `.gitignore`.

**Alternative**: You can also enter your API key directly in the ComfyUI node interface, but using environment variables is more secure.

## Development Workflow

### Dev Container (Recommended)

```bash
# Start the development environment
./.devcontainer/run-comfy.sh

# ComfyUI available at http://localhost:8188
# Changes are automatically reloaded
```

### Local Development

```bash
# Python backend development
ruff check .                    # Lint Python code
pytest                         # Run Python tests
python -c "from nodes.nodes import NODE_CLASS_MAPPINGS; print(list(NODE_CLASS_MAPPINGS.keys()))"

# JavaScript web extension development
cd web
npm run lint                   # Lint JavaScript
npm run format                 # Format code
cd tests && npm test           # Run Playwright tests (requires running ComfyUI)
```

**Important Notes:**

- Python changes require ComfyUI server restart
- JavaScript changes require browser cache refresh only
- JavaScript widgets are plain JS files (no build step required)

## Testing

### Automated Testing

The project includes comprehensive CI/CD testing:

- **Python**: Linting (ruff), formatting (black), type checking (mypy), unit tests (pytest)
- **JavaScript**: Linting (eslint), formatting (prettier), integration tests (playwright)
- **Integration**: ComfyUI node loading, FFmpeg availability, system compatibility

### Manual Testing

```bash
# Test Python nodes
python -c "from nodes.nodes import NODE_CLASS_MAPPINGS; print('Nodes:', list(NODE_CLASS_MAPPINGS.keys()))"

# Test JavaScript widgets
# 1. Start ComfyUI with the custom node
# 2. Add a Gemini node to your workflow
# 3. Test video controls and interface elements
```

## Usage

This template includes a simple example extension that displays workflow node statistics. After installation:

1. Look for the "React Example" tab in the ComfyUI sidebar
2. Click to open the example UI

When developing your own extension, you can:

1. Replace the example UI in App.tsx with your own components
2. Update the tab title and icon in main.tsx
3. Customize the extension's appearance and behavior

## Development

### Setup Development Environment

```bash
# Go to the UI directory
cd ui

# Install dependencies
npm install

# Start development mode (watches for changes)
npm run watch
```

### Available ComfyUI Extension APIs

This template provides access to ComfyUI's powerful JavaScript APIs through the official type definitions. You can use these APIs to build rich extensions:

- **Sidebar Tabs**: Create custom sidebar panels like this template demonstrates
- **Bottom Bar Panels**: Add panels to the bottom of the UI
- **Top Menu Items**: Add custom entries to the top menu
- **Context Menus**: Create custom context menus for the graph
- **Settings**: Add settings to the ComfyUI settings panel
- **Toasts**: Display notification messages
- **Commands**: Create and register custom commands
- **Hotkeys/Keybindings**: Register custom keyboard shortcuts
- **About Panel Badges**: Add badges to the about panel
- **App Events**: Listen to and respond to app events
- **Graph Manipulation**: Programmatically manipulate the workflow graph

For comprehensive documentation on all available APIs, see the [ComfyUI JavaScript Developer Documentation](https://docs.comfy.org/custom-nodes/js/javascript_overview).

### File Structure

```
ComfyUI-SwissArmyKnife/
├── .github/                    # GitHub configurations
│   └── workflows/
│       └── react-build.yml     # Automatic build and publishing workflow
├── __init__.py                 # Python entry point for ComfyUI integration
├── pyproject.toml              # Project metadata for ComfyUI Registry
├── dist/                       # Built extension files (generated)
└── ui/                         # React application
    ├── public/
    │   └── locales/            # Internationalization files
    │       ├── en/
    │       │   └── main.json   # English translations
    │       └── zh/
    │           └── main.json   # Chinese translations
    ├── src/
    │   ├── App.tsx             # Main React component with example UI
    │   ├── App.css             # Styles for the example UI
    │   ├── index.css           # Global styles and theme variables
    │   ├── main.tsx            # Entry point for React app
    │   ├── vite-env.d.ts       # Vite environment types
    │   ├── setupTests.ts       # Testing environment setup
    │   ├── __tests__/          # Unit tests for components
    │   │   └── dummy.test.tsx  # Example test
    │   └── nodes/
    │       └── i18n.ts         # Internationalization setup
    ├── eslint.config.js        # ESLint configuration
    ├── jest.config.js          # Jest testing configuration
    ├── jest.setup.js           # Jest setup file
    ├── package.json            # npm dependencies
    ├── tsconfig.json           # TypeScript configuration
    ├── tsconfig.node.json      # TypeScript configuration for Node
    └── vite.config.ts          # Build configuration
```

### TypeScript Support

This extension uses the official `@comfyorg/comfyui-frontend-types` package for type-safe interaction with ComfyUI APIs. To install it:

```bash
cd ui
npm install -D @comfyorg/comfyui-frontend-types
```

## Publishing to ComfyUI Registry

### Prerequisites

1. Set up a [Registry](https://registry.comfy.org) account
2. Create an API key at https://registry.comfy.org/nodes

### Steps to Publish

1. Install the comfy-cli tool:

    ```bash
    pip install comfy-cli
    ```

2. Verify your pyproject.toml has the correct metadata:

    ```toml
    [project]
    name = "your_extension_name"  # Use a unique name for your extension
    description = "Your extension description here."
    version = "0.1.0"  # Increment this with each update

    [tool.comfy]
    PublisherId = "your_publisher_id"  # Your Registry publisher ID
    DisplayName = "Your Extension Display Name"
    includes = ["dist/"]  # Include built React code (normally ignored by .gitignore)
    ```

3. Publish your extension:

    ```bash
    comfy-cli publish
    ```

4. When prompted, enter your API key

### Automatic Publishing with GitHub Actions

This template includes a GitHub Actions workflow that automatically publishes to the ComfyUI Registry whenever you update the version in pyproject.toml:

1. Go to your repository's Settings > Secrets and variables > Actions
2. Create a new repository secret called `REGISTRY_ACCESS_TOKEN` with your API key
3. Commit and push an update to pyproject.toml (e.g., increment the version number)
4. The GitHub Action will automatically run and publish your extension

The workflow configuration is set up in `.github/workflows/react-build.yml` and will trigger when:

- The `pyproject.toml` file is modified and pushed to the `main` branch

The workflow automatically:

1. Sets up Node.js environment
2. Installs dependencies (`npm install`)
3. Builds the React extension (`npm run build`)
4. Publishes the extension to the ComfyUI Registry

## Unit Testing

This template includes a basic setup for unit testing with Jest and React Testing Library:

```bash
# Run tests
npm test

# Run tests in watch mode during development
npm run test:watch
```

Example tests can be found in the `src/__tests__` directory. The setup includes:

- Jest for running tests
- React Testing Library for testing components
- Mock implementation of the ComfyUI window.app object

## Resources

- [ComfyUI JS Extension Documentation](https://docs.comfy.org/custom-nodes/js/javascript_overview) - Official documentation for ComfyUI JavaScript Extensions
- [ComfyUI Registry Documentation](https://docs.comfy.org/registry/publishing) - Learn how to publish your extension
- [ComfyUI Frontend Repository](https://github.com/sammykumar/ComfyUI-Frontend) - The main ComfyUI frontend codebase
- [Official ComfyUI Frontend Types](https://www.npmjs.com/package/@comfyorg/comfyui-frontend-types) - TypeScript definitions for ComfyUI
- [React Extension Guide](REACT_EXTENSION_GUIDE.md) - Detailed guide for creating React extensions
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [React Documentation](https://react.dev/reference/react)
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this template.

## Credits

### Third-Party Integrations

- **LoRA Manager** - Forked from [nd-super-nodes](https://github.com/HenkDz/nd-super-nodes) by HenkDz
    - Super LoRA Loader with multi-LoRA management
    - Enhanced file picker overlay
    - Template management system
    - CivitAI integration for trigger words

## License

GNU General Public License v3
