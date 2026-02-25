# BoxBox - Enhanced Version

ComfyUI custom node for interactive box/region selection with advanced features.

## 🎉 What's New in This Enhanced Version

This is an improved fork of the original [BoxBox](https://github.com/mercu-lore/BoxBox) with several bug fixes and new features:

### ✅ Bug Fixes

1. **Fixed Image Loading After ComfyUI Update**
   - Updated image URL construction to use ComfyUI's API helper
   - Added proper filename encoding for special characters
   - Improved error handling with fallback mechanisms

2. **Fixed Backend Issues**
   - Corrected temp directory usage to use ComfyUI's proper temp folder
   - Fixed HTTP response format (now returns proper `web.json_response`)
   - Sanitized filenames to prevent path separator issues

3. **Fixed Coordinate Scaling**
   - Removed duplicate coordinate division (was happening in both frontend and backend)
   - Coordinates now correctly convert from display space to original image space

4. **Fixed Intermediate Node Support**
   - Added recursive node chain traversal to find source images
   - Now works with processing nodes (Brightness, Blur, etc.) between LoadImage and BoxSelector
   - Searches up to 20 levels deep in the node graph

5. **NumPy 2.0 Compatibility**
   - Updated backend logic with explicit casting (`np.uint8`, `np.float32`)
   - Fixed binary incompatibility issues in coordinate processing

6. **ComfyUI v0.12.2+ (Modern API) Support**
   - Re-engineered frontend to use the modern `window.comfyAPI` system
   - Eliminated "Legacy API" deprecation warnings
   - Improved dialog instantiation with robust fallback mechanisms

7. **Adaptive Window Scaling**
   - Fixed coordinate misalignment when the browser window is resized
   - System now dynamically calculates total scale (Server Scale * Browser CSS Scale)

### 🆕 New Features

1. **Aspect Ratio Memory**
   - Remembers your last selected aspect ratio using localStorage
   - Persists across browser sessions and system restarts
   - Keeps aspect ratio locked when drawing new selections

2. **Selection Restoration**
   - Automatically restores your previous selection when reopening the selector
   - Shows the blue selection box from your last session
   - Allows you to adjust or modify existing selections

3. **Improved User Experience**
   - Removed annoying popup alerts for small images
   - Better console logging for debugging
   - Image error handler with helpful messages

---

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "BoxBox Enhanced"
3. Click Install

### Method 2: Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Latentnaut/BoxBox.git
```

Then restart ComfyUI.

---

## 🎯 Usage

1. Add a **LoadImage** node to your workflow
2. Add a **BoxSelector** node
3. Connect the image output to BoxSelector
4. Click **📦 Select Box** button
5. Draw a rectangular selection on your image
6. Choose an aspect ratio (optional)
7. Click **✅ Confirm**
8. Use **BoxCrop** to crop the selected region
9. Use **BoxResize** to resize the cropped image

### Supported Workflows

✅ **Direct**: LoadImage → BoxSelector → BoxCrop  
✅ **With Processing**: LoadImage → Brightness → BoxSelector → BoxCrop  
✅ **Complex Chains**: LoadImage → Node1 → Node2 → ... → BoxSelector

---

## 🔧 Nodes Included

- **📦 BoxSelector**: Interactive region selection with aspect ratio locking
- **✂️ BoxCrop**: Crops image based on selected coordinates
- **📐 BoxResize**: Resizes images with aspect ratio preservation

---

## 🐛 Known Issues

- Preview shows original image (not processed) when using intermediate nodes
  - This is intentional for performance reasons
  - Coordinates are still applied correctly to the processed image

---

## 🙏 Credits

- **Original Author**: [mercu-lore](https://github.com/mercu-lore)
- **Enhanced Version**: Latentnaut
- **Improvements**: AI-assisted development with Claude

---

## 📄 License

Same license as the original BoxBox project.

---

## 🤝 Contributing

Issues and pull requests are welcome! If you find bugs or have feature requests, please open an issue on GitHub.
