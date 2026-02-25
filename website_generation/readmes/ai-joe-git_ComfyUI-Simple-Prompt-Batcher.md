# ComfyUI Simple Prompt Batcher

A simple and efficient ComfyUI custom node that allows you to batch process multiple prompts in a single queue. Perfect for testing variations, exploring different ideas, or running systematic prompt experiments.

## 📋 Features

- ✅ **Simple text input** - One prompt per line, no complex syntax
- ✅ **Automatic batching** - All prompts run in a single queue
- ✅ **Optimized performance** - Models stay loaded between inferences
- ✅ **Unlimited prompts** - Add as many lines as you need
- ✅ **Clean console output** - Shows prompt count and preview
- ✅ **No empty lines** - Automatically filters blank entries

## 🚀 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Simple Prompt Batcher"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/ai-joe-git/ComfyUI-Simple-Prompt-Batcher.git
   ```

3. Restart ComfyUI

4. The node will appear as **"📝 Simple Prompt Batcher"** in the node menu under `utils/text`

## 💡 Usage

### Basic Workflow

1. **Add the node** to your workflow
   - Search for "Simple Prompt Batcher" or "📝 Simple Prompt Batcher"
   - Add it to your canvas

2. **Enter your prompts** in the text area (one per line):
   ```
   a beautiful sunset over mountains
   a cat sleeping on a couch
   a futuristic city at night
   a serene forest landscape
   ```

3. **Connect the output** to CLIPTextEncode (or any text input node)
   ```
   [Simple Prompt Batcher] → [CLIPTextEncode] → [Your Workflow]
   ```

4. **Queue the prompt ONCE** - ComfyUI will automatically run all prompts in sequence

### Example Workflow Structure

```
📝 Simple Prompt Batcher
    ↓ (prompt output)
CLIPTextEncode (Positive)
    ↓
KSampler
    ↓
VAE Decode
    ↓
Save Image
```

## 📊 Performance Benefits

### Without Batching
- Load models (30s) → Generate (25s) → Unload
- **Repeat for each prompt**
- **8 prompts = ~7 minutes 20 seconds**

### With Simple Prompt Batcher
- Load models once (30s) → Generate all 8 (8 × 25s)
- Models stay loaded between generations
- **8 prompts = ~3 minutes 50 seconds**

**Result: ~50% time savings on batch processing!** 🎯

## 🎨 Use Cases

### Camera Angle Testing (Video Generation)
```
Turn the camera to a close-up
Turn the camera to a wide-angle lens
Rotate the camera 45 degrees to the right
Turn the camera to an aerial view
Turn the camera to a low-angle view
```

### Style Variations (Image Generation)
```
a red sports car in photorealistic style
a red sports car in anime style
a red sports car in watercolor painting style
a red sports car in cyberpunk style
```

### Scene Exploration
```
a forest in spring with blooming flowers
a forest in summer with lush green leaves
a forest in autumn with golden foliage
a forest in winter with snow-covered trees
```

### Systematic Testing
```
quality: high, lighting: soft, mood: peaceful
quality: high, lighting: dramatic, mood: intense
quality: high, lighting: natural, mood: casual
quality: high, lighting: studio, mood: professional
```

## 📝 Console Output

When you run the batcher, you'll see helpful output in your console:

```
[Prompt Batcher] 📋 Batching 5 prompts:
[Prompt Batcher]   1. a beautiful sunset over mountains
[Prompt Batcher]   2. a cat sleeping on a couch
[Prompt Batcher]   3. a futuristic city at night
[Prompt Batcher]   4. a cyberpunk street scene
[Prompt Batcher]   5. a serene forest landscape
```

## ⚙️ Technical Details

- **Output Type**: `STRING` (batch list)
- **Category**: `utils/text`
- **Compatibility**: Works with any node that accepts text input
- **Memory**: Efficient - models remain loaded during batch processing
- **Format**: One prompt per line, empty lines automatically filtered

## 🔧 Requirements

- ComfyUI (latest version recommended)
- No additional dependencies required

## 📖 Tips

1. **No empty lines needed** - The node automatically filters them out
2. **Long prompts supported** - No character limit per line
3. **Preview in console** - First 60 characters of each prompt shown
4. **Compatible with all samplers** - Works with any generation workflow
5. **Combine with other nodes** - Use with wildcards, style mixers, etc.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share your use cases

## 📄 License

MIT License - Feel free to use in your projects!

## 🙏 Credits

Created for the ComfyUI community to make batch prompt processing simple and efficient.

## 🔗 Links

- [GitHub Repository](https://github.com/ai-joe-git/ComfyUI-Simple-Prompt-Batcher)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

---

**Made with ❤️ for the ComfyUI community**

*If you find this node useful, please star the repository! ⭐*
