# ComfyUI FlipFlop Group Positioner

A ComfyUI custom node that allows you to quickly position node groups at your mouse cursor location using keyboard shortcuts.

## 🎯 Project Status

**✅ WORKING VERSION RESTORED** - The extension is now functional with proper coordinate conversion.

### What Was Fixed

The core issue was **coordinate conversion**. After extensive debugging and research of Crystools' LiteGraph typings, we discovered the proper ComfyUI coordinate conversion methods:

1. **`canvas.convertEventToCanvasOffset()`** - The official ComfyUI method (PRIMARY)
2. **`canvas.ds.convertOffsetToCanvas()`** - The DragAndScale method (SECONDARY)
3. **Manual conversion fallback** - For compatibility (FALLBACK)

### Key Technical Breakthrough

The working solution uses the **exact same methods** that Crystools and other ComfyUI extensions use:

```javascript
// Method 1: Use ComfyUI's convertEventToCanvasOffset method (PROPER WAY)
if (canvas.convertEventToCanvasOffset && typeof canvas.convertEventToCanvasOffset === 'function') {
    const mockEvent = {
        clientX: mousePos[0],
        clientY: mousePos[1]
    };
    graphPos = canvas.convertEventToCanvasOffset(mockEvent);
}
```

This ensures compatibility with ComfyUI's coordinate system and proper positioning accuracy.

## 🚀 Features

- **Keyboard Shortcuts**: Press a key to instantly move a group and its contents to your mouse position
- **Smart Node Detection**: Automatically finds and moves all nodes within a group using multiple detection methods
- **Real-time Configuration**: Change settings directly in the node widgets - no file editing required
- **Proper Coordinate System**: Uses ComfyUI's built-in coordinate conversion for accurate positioning
- **Multiple Detection Methods**: Finds nodes using group_id, group property, bounds overlap, and fallback methods

## 📦 Installation

1. **Clone or download** this repository to your ComfyUI `custom_nodes` folder:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/fredhopp/comfyui-flipflopnodes.git
   ```

2. **Restart ComfyUI** to load the new custom node

3. **Add the node** to your workflow:
   - Search for "Group Positioner" in the node menu
   - Add it to your graph

## 📖 Usage

### Basic Setup

1. **Create a group** in your ComfyUI workflow
2. **Add nodes** to the group
3. **Add the Group Positioner node** to your workflow
4. **Configure the settings**:
   - **Group Name**: The name of your group (case-sensitive)
   - **Shortcut Key**: The key to press for positioning (e.g., "5", "F8", "Ctrl+Shift+G")
   - **Enabled**: Toggle the shortcut on/off
   - **Debug Mode**: Enable detailed logging

### Using the Shortcut

1. **Position your mouse** where you want the group to appear
2. **Press the configured shortcut key**
3. **The group and all its nodes** will instantly move to that position

## 🔧 Configuration

### Node Widgets

The Group Positioner node provides these configuration options:

- **Group Name** (string): Name of the group to position
- **Shortcut Key** (string): Keyboard shortcut to trigger positioning
- **Enabled** (boolean): Enable/disable the shortcut
- **Debug Mode** (boolean): Enable detailed logging

### Supported Shortcut Formats

- **Single keys**: `5`, `a`, `F8`, `Enter`
- **Modifier combinations**: `Ctrl+Shift+G`, `Alt+F1`, `Ctrl+Alt+Delete`
- **Function keys**: `F1` through `F12`

## 🏗️ Architecture

### Module Structure

```
web/js/
├── group_positioner.js      # Main extension entry point
└── modules/
    ├── app.js              # ComfyUI app integration and graph monitoring
    ├── config.js           # Configuration management with real-time updates
    ├── keyboard.js         # Keyboard event handling and shortcut detection
    ├── logging.js          # Logging system
    └── positioning.js      # Group positioning logic and coordinate conversion
```

### Key Components

- **Coordinate Conversion**: Uses ComfyUI's `convertEventToCanvasOffset()` for accurate positioning
- **Node Detection**: Multiple methods to find nodes within groups
- **Real-time Configuration**: Settings update immediately via node widgets
- **Global Mouse Tracking**: Tracks mouse position across the entire document

## 🔍 Troubleshooting

### Common Issues

**Group not found:**
- Check the group name spelling (case-sensitive)
- Ensure the group exists in your workflow
- Try reloading the configuration

**Nodes not moving:**
- Verify nodes are actually within the group bounds
- Check if the group has the correct name
- Enable debug mode for detailed logging

**Shortcut not working:**
- Ensure the shortcut key is correctly configured
- Check if the extension is enabled
- Try a different shortcut key

### Debug Mode

Enable debug mode to see detailed information:

1. Set **Debug Mode** to `true` in the node
2. Open browser console (F12)
3. Look for `[FF Group Positioner]` messages
4. Check coordinate conversion logs

## 📋 TODO List

### High Priority
- [ ] **Add comprehensive error handling** for edge cases
- [ ] **Implement proper logging system** with configurable levels
- [ ] **Add visual feedback** when positioning groups
- [ ] **Create unit tests** for coordinate conversion methods
- [ ] **Add support for multiple groups** in a single workflow

### Medium Priority
- [ ] **Implement smooth animations** for group movement
- [ ] **Add position presets** for common layouts
- [ ] **Create configuration import/export** functionality
- [ ] **Add keyboard shortcut conflicts detection**
- [ ] **Implement undo/redo functionality**

### Low Priority
- [ ] **Add group rotation support**
- [ ] **Create visual group editor**
- [ ] **Add support for nested groups**
- [ ] **Implement group templates**
- [ ] **Add performance optimizations** for large workflows

### Known Issues to Fix
- [ ] **Circular JSON errors** in debug logging
- [ ] **Import/export issues** with ES6 modules
- [ ] **Canvas property access** edge cases
- [ ] **Mouse position tracking** improvements
- [ ] **Group detection reliability** enhancements

## 🔧 Development

### Building

This extension uses ES6 modules and doesn't require a build step. Simply edit the JavaScript files and reload ComfyUI.

### Adding Features

1. **New modules**: Add to `web/js/modules/`
2. **Configuration**: Update `config.js` and node widgets
3. **Testing**: Use the manual test functions
4. **Documentation**: Update this README

### Coordinate System

The extension uses ComfyUI's coordinate system:

- **Screen coordinates**: Mouse position in pixels
- **Canvas coordinates**: Transformed coordinates for positioning
- **Conversion**: Uses `canvas.convertEventToCanvasOffset()` for accuracy

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🙏 Acknowledgments

- **ComfyUI**: The amazing workflow system this extends
- **Crystools**: Reference for LiteGraph coordinate handling and proper API usage
- **rgthree-comfy**: Inspiration for the module architecture

## 📞 Support

- **Issues**: Report bugs on GitHub
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Check this README for usage details

---

**Happy positioning! 🎯**

*Last updated: December 2024 - Working version with proper coordinate conversion restored*
