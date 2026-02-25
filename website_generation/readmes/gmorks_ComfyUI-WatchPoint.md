![Watch Point Banner](media/banner.png)

# 👁️ ComfyUI Watch Point

![node preview](media/preview.png)

**Dual preview system for ComfyUI workflows**

### About This Project
This node was developed by a creator with limited Python experience, using AI tools like Claude, Gemini, and Kimi. While fully functional, it may not strictly adhere to all Python best practices. 

We warmly invite you to fork, improve, and adapt this code—collaboration is what makes open-source thrive!

Watch Point provides two simultaneous preview methods:
- Monitor Preview: External Tkinter window on any monitor
- Floating Preview: ComfyUI's built-in preview system

---

![node preview](example/example_workflow.png)

---

## 🔧 Features

### Monitor Preview (Tkinter)
- Display on any connected monitor
- Zoom/Pan controls with mouse
- Keyboard shortcuts
- Save images directly from preview
- Copy to clipboard
- Customizable settings
- Thread Safety: Windows minimize instead of closing to prevent ComfyUI crashes

### Floating Preview (JavaScript)
- Uses ComfyUI's native preview system
- Works with existing preview extensions
- Auto-updates during workflow execution
- Configurable via browser localStorage (no file editing)
- Customizable keyboard shortcuts
- Snap-to-grid positioning
- Adjustable opacity levels

---

## 🛡️ Thread Safety & Window Protection

WatchPoint includes built-in protection against threading issues that can crash ComfyUI:

### Window Minimization Protection
- **Close Button Behavior**: Clicking the Windows close button minimizes the window instead of closing it
- **Thread Safety**: Prevents `Tcl_AsyncDelete` errors and threading conflicts
- **ComfyUI Stability**: Ensures ComfyUI continues running even if windows are "minimized"
- **Window Recovery**: Minimized windows can be restored from the taskbar

### Technical Details
- Uses thread-safe Tkinter operations
- Implements proper cleanup procedures
- Prevents memory leaks and threading deadlocks
- Global window management for consistent behavior

---

## 📦 Installation

1. Clone into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone [https://github.com/gmorks/ComfyUI-WatchPoint.git](https://github.com/gmorks/ComfyUI-WatchPoint.git)

```

2. Install dependencies (if needed):

```bash
pip install pillow screeninfo

```

3. Restart ComfyUI

---

## 👁️ Nodes

### Watch Point

The main preview node.

1. Add **Watch Point** to your workflow.
2. Connect an `IMAGE` input.
3. Enable/disable previews:
* `floating_preview`: Enable ComfyUI's built-in preview.
* `monitor_preview`: Enable or pause the external monitor window (window stays alive, image updates only when True).
4. Configure the target monitor via the **⚙ Settings** dialog or by editing `watchpoint_settings.json` (`monitor_index`).
5. The node acts as a pass-through for the `IMAGE` output.

### Optional string input

1. Connect any `STRING` input.
2. The text will appear in the side panel of the external window.

---

## 🎮 Controls (Monitor Preview)

### Mouse

* **Scroll wheel**: Zoom in/out
* **Left click + drag**: Pan image
* **Right click**: Context menu

### Keyboard

* **R**: Reset zoom and pan
* **T**: Toggle toolbar
* **P**: Toggle Text panel
* **1**: Zoom 1:1 (100% actual size)

### Window Close Behavior

**Important**: The Windows close button (❌) minimizes the window instead of closing it. This prevents threading errors and keeps ComfyUI stable. To "close" the window:

* Click the close button → Window minimizes to taskbar
* Right-click taskbar icon → "Close window" for forced closure

### Toolbar Buttons

* **↻ Reset**: Reset zoom and pan
* **⊕ Zoom In**: Increase zoom level
* **⊖ Zoom Out**: Decrease zoom level
* **1:1 (100%)**: View image at actual size
* **Window Size**: Quick resize presets
* **⛶ Fullscreen**: Toggle fullscreen mode
* **⚙ Settings**: Open settings dialog

---

## ⚙️ Settings

Access settings via the **⚙ Settings** button in the toolbar.

### Save Options

* Default format: PNG or JPEG
* JPEG quality slider (10-100)

### Monitor Options

* Select the target monitor from the **Monitor** dropdown in the Settings dialog.
* Persist the monitor selection globally via `monitor_index` in `watchpoint_settings.json`.

### UI Options

* Show/hide toolbar by default

All settings are saved to `watchpoint_settings.json`.

---

## 🔧 Configuration Files

### Monitor Preview Settings

Edit `watchpoint_settings.json` to customize defaults for the external Tkinter window:

```json
{
  "window_width": 800,
  "window_height": 600,
  "window_x": null,
  "window_y": null,
  "window_size_mode": "fixed",
  "show_toolbar": true,
  "save_format": "png",
  "jpeg_quality": 90,
  "monitor_index": 0
}

```

#### Settings Explained

* `window_x`, `window_y`: Window position (null = auto)
* `window_size_mode`: "fixed", "Half Vertical", "Half Horizontal", or "Quarter"
* `show_toolbar`: Show toolbar on startup
* `save_format`: Default save format ("png" or "jpeg")
* `jpeg_quality`: JPEG compression quality (10-100)
* `monitor_index`: Index of the monitor used for the external preview (0 = first monitor).

### Floating Preview Configuration

The floating preview window is configured via browser localStorage. No file editing required!

#### Quick Start

**View Current Configuration**

Open browser console (F12) and run:

```javascript
WatchPointFloating.getConfig()

```

**Change Configuration**

```javascript
WatchPointFloating.setConfig({
    window: {
        defaultWidth: 500,
        defaultHeight: 500,
        defaultPosition: "top-right",
        defaultOpacity: 80
    },
    shortcuts: {
        toggle: "Ctrl+Alt+KeyP"  // Change toggle shortcut
    }
})

```

**Reset to Defaults**

```javascript
WatchPointFloating.resetConfig()

```

**Show Help**

```javascript
WatchPointFloating.showHelp()

```

**Note**: Reload the page after changing config to apply changes.

#### Available Configuration Options

##### Window Settings

```javascript
{
    window: {
        defaultWidth: 320,           // Width in pixels
        defaultHeight: 320,          // Height in pixels
        defaultPosition: "middle-right", // Initial position
        defaultOpacity: 100          // 0-100 (percentage)
    }
}

```

**Available Positions**:

* `"top-left"`, `"top-center"`, `"top-right"`
* `"middle-left"`, `"middle-center"`, `"middle-right"`
* `"bottom-left"`, `"bottom-center"`, `"bottom-right"`

##### Opacity Settings

```javascript
{
    opacity: {
        levels: [20, 40, 60, 80, 100],  // Available opacity levels (%)
        showIndicator: true,             // Show opacity % when changing
        indicatorDuration: 1000          // How long indicator shows (ms)
    }
}

```

##### UI Settings

```javascript
{
    ui: {
        showHeader: true,          // Show title bar
        showTitle: true,           // Show "👁️ Watch Point" title
        showCloseButton: true,     // Show X button
        dragFromAnywhere: false    // Drag from image area (only if header=false)
    }
}

```

##### Keyboard Shortcuts

```javascript
{
    shortcuts: {
        // Main controls
        toggle: "Ctrl+Alt+KeyW",
        increaseOpacity: "Ctrl+Alt+Equal",    // or Ctrl+Alt++
        decreaseOpacity: "Ctrl+Alt+Minus",    // or Ctrl+Alt+-
        
        // Arrow navigation (relative)
        snapUp: "Ctrl+Alt+ArrowUp",
        snapDown: "Ctrl+Alt+ArrowDown",
        snapLeft: "Ctrl+Alt+ArrowLeft",
        snapRight: "Ctrl+Alt+ArrowRight",
        
        // Numpad navigation (absolute positions)
        snapToPosition7: "Ctrl+Alt+Numpad7",  // Top-left
        snapToPosition8: "Ctrl+Alt+Numpad8",  // Top-center
        snapToPosition9: "Ctrl+Alt+Numpad9",  // Top-right
        snapToPosition4: "Ctrl+Alt+Numpad4",  // Middle-left
        snapToPosition5: "Ctrl+Alt+Numpad5",  // Middle-center
        snapToPosition6: "Ctrl+Alt+Numpad6",  // Middle-right
        snapToPosition1: "Ctrl+Alt+Numpad1",  // Bottom-left
        snapToPosition2: "Ctrl+Alt+Numpad2",  // Bottom-center
        snapToPosition3: "Ctrl+Alt+Numpad3"   // Bottom-right
    }
}

```

#### Default Keyboard Shortcuts

| Action | Shortcut | Description |
| --- | --- | --- |
| **Toggle window** | `Ctrl+Alt+W` | Show/hide floating preview |
| **Increase opacity** | `Ctrl+Alt++` | Make more opaque |
| **Decrease opacity** | `Ctrl+Alt+-` | Make more transparent |
| **Move up** | `Ctrl+Alt+↑` | Snap to position above |
| **Move down** | `Ctrl+Alt+↓` | Snap to position below |
| **Move left** | `Ctrl+Alt+←` | Snap to position left |
| **Move right** | `Ctrl+Alt+→` | Snap to position right |
| **Snap to corner** | `Ctrl+Alt+Numpad[1-9]` | Jump to specific position |

#### Storage Location

Configuration is stored in browser localStorage under the key:

```
watchpoint-floating-config

```

---

## Use Cases

### Dual Monitor Setup

Perfect for users with multiple monitors:

* Work on ComfyUI on main monitor
* View live preview on secondary monitor
* No need to switch windows or tabs

### Quality Control

Use 1:1 zoom to inspect:

* Image quality at pixel level
* Upscaling artifacts
* Detail preservation

### Live Monitoring

Watch your workflow progress in real-time:

* Both previews update simultaneously
* Choose the view that works best for your setup
* Keep an eye on intermediate results

---

## Requirements

* Python 3.7+
* tkinter (usually included with Python)
* PIL/Pillow
* screeninfo (optional, for multi-monitor detection)

---

## Optional Dependencies

For clipboard support (Windows):

```bash
pip install pywin32

```

---

## 🛠️ Troubleshooting

### Window doesn't appear

* Check if `monitor_preview` is enabled (True).
* Open the **⚙ Settings** dialog and verify that a valid monitor is selected.
* Alternatively, check that `monitor_index` in `watchpoint_settings.json` points to an existing monitor.
* Check console for error messages.

### Window appears in wrong location

* Set explicit X, Y coordinates in settings
* Use `window_x: 0, window_y: 0` for top-left

### Image not updating

* Ensure workflow is executing.
* Check that image is connected to Watch Point input.
* Verify that `monitor_preview` is enabled (True); when False, the window stays open but the image will not refresh.
* Try disabling/re-enabling monitor preview.

### Window snapping (Win + Arrows) doesn't work in Fullscreen

*   **Reason**: To guarantee that fullscreen mode activates on the correct monitor (avoiding a Windows bug that forces it to Monitor 0), we use a custom "borderless window" approach.
*   **Solution**: To move the window to another monitor, exit fullscreen (F11 or toolbar button), drag the window to the desired monitor, and re-enable fullscreen. Alternatively, use the Monitor selector in Settings.

### Floating preview not working

* Ensure `floating_preview` is enabled (True)
* Check if other preview extensions are conflicting
* Restart ComfyUI

---

## Credits

Vibe Coded for ComfyUI by gmorks using AI.

---

## License

MIT License - Feel free to use and modify!

---

## 🚧 Development Status

**Note**: This extension is not yet compatible with ComfyUI Nodes 2.0. Support for the new node system is on our to-do list and will be implemented in a future update.

### Known Issues
*   **Fullscreen Mode**: Currently, toggling fullscreen (F11) may default to the primary monitor (Monitor 0) regardless of the window's current position. We are actively working on a fix to ensure fullscreen activates on the correct monitor. [WIP]

---

## Recent Changes

### v2.0.0 - Cleanup & Optimization
* Removed debug nodes and utilities
* Integrated Signal Scout text feature into main node
* Simplified codebase while preserving stability

### v1.0.0 - Initial Release

* Dual preview system (Monitor + Floating)
* Basic window controls and settings
* Multi-monitor support
