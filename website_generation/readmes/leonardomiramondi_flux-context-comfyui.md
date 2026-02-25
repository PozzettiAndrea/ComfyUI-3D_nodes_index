# Flux Kontext ComfyUI Node

A ComfyUI custom node for **Flux Kontext** - advanced image editing and transformation using text prompts via the Replicate API.

## What is Flux Kontext?

Flux Kontext is Black Forest Labs' state-of-the-art **image editing** model that allows you to transform existing images using natural language descriptions. Unlike image generation models, Flux Kontext specializes in:

- **Style Transfer**: Convert photos to different art styles (watercolor, oil painting, sketches)
- **Object/Clothing Changes**: Modify hairstyles, add accessories, change colors  
- **Text Editing**: Replace text in signs, posters, and labels
- **Background Swapping**: Change environments while preserving subjects
- **Character Consistency**: Maintain identity across multiple edits

### Manual Installation

1. **Find your ComfyUI installation directory**:
   ```bash
   # Common locations:
   # Windows: C:\ComfyUI\ or C:\Users\[username]\ComfyUI\
   # Mac: /Applications/ComfyUI/ or ~/ComfyUI/
   # Linux: ~/ComfyUI/ or /opt/ComfyUI/
   ```

2. **Navigate to custom nodes directory**:
   ```bash
   cd [your-comfyui-path]/custom_nodes/
   ```

3. **Clone this repository**:
   ```bash
   git clone https://github.com/leonardomiramondi/flux-kontext-comfyui.git
   ```

4. **Install dependencies**:
   ```bash
   cd flux-kontext-comfyui
   pip install -r requirements.txt
   ```

5. **Restart ComfyUI** completely

## Setup

1. **Get a Replicate API token**:
   - Go to [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)
   - Create a new token
   - Copy the token (starts with `r8_`)

2. **Add the node to your workflow**:
   - In ComfyUI, add the **Flux Kontext Node** (found under `image/editing`)
   - Paste your API token in the "api_token" field

## Usage

### Basic Image Editing
1. Connect an image to **"image 1"** (required)
2. Enter your **editing prompt** describing the desired changes
3. Choose your **model** (Pro or Max)
4. Select **output format** (JPG or PNG)
5. Run the workflow

### Reference-Style Editing  
1. Connect your main image to **"image 1"**
2. Connect a reference/style image to **"image 2"** (optional)
3. Describe the transformation in the **editing prompt**
4. The model will use image 2 as a style reference

### Example Prompts

**Style Transfer:**
- "Transform this into a watercolor painting"
- "Make this look like a Renaissance oil painting"
- "Convert to a pencil sketch with detailed shading"

**Object Changes:**
- "Change the red car to a blue motorcycle"
- "Replace the person's outfit with a business suit"
- "Add sunglasses and a hat to the person"

**Background Edits:**
- "Change the background to a beach scene while keeping the person"
- "Replace the indoor setting with a forest"
- "Add falling snow to this winter scene"

**Text Editing:**
- "Change the sign text from 'OPEN' to 'CLOSED'"
- "Replace the billboard text with 'SALE 50% OFF'"

## API Requirements

- **Replicate account** with available credits
- **Valid API token** (get from [replicate.com](https://replicate.com/account/api-tokens))
- **Internet connection** for API calls

## Troubleshooting

### "Invalid API token"
- Verify your token starts with `r8_`
- Check you have credits in your Replicate account
- Ensure the token has proper permissions

### "Image too large" errors
- The node automatically compresses large images
- Try reducing your input image resolution if issues persist
- Maximum recommended size: 2048x2048 pixels

### Node not appearing
- Ensure you've restarted ComfyUI completely after installation
- Check that `requirements.txt` packages installed successfully
- Verify the node files are in the correct custom_nodes directory

### "Model not found" errors
- Only use the supported models (flux-kontext-pro or flux-kontext-max)
- Ensure your Replicate account has access to these models

## Contributing

Feel free to submit issues, feature requests, or pull requests on the [GitHub repository](https://github.com/leonardomiramondi/flux-kontext-comfyui).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- **Black Forest Labs** for the Flux Kontext models
- **Replicate** for API infrastructure  
- **ComfyUI** community for the amazing framework 
