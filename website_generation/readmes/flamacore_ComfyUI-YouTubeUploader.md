[![Buy me a Coffee](https://buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://buymeacoffee.com/chao.k)


Disclaimer: AI models have been utilized in creation of this repo and this repo is under HEAVY development. It works fine, pretty basic but still use with care please.

# 🎬 YouTube Uploader Nodes for ComfyUI

Upload videos directly to YouTube from your ComfyUI workflows! Perfect for AI-generated content creators.

<img width="1062" alt="ComfyUI_ow3dB7audK" src="https://github.com/user-attachments/assets/5e90807a-b777-420d-9fdc-d5fbc552ef94" />


## ✨ Features

- **Direct Upload**: Upload generated videos straight to YouTube
- **Custom Thumbnails**: Set custom thumbnails for your videos  
- **Audio Support**: Include audio in your uploads
- **Safety Features**: Upload protection to prevent accidents
- **Shorts Optimized**: Perfect for vertical video workflows
- **ComfyUI-Manager Compatible**: Easy installation and updates

## 📦 Installation

## If ComfyUI Manager finds this repo, then the best way to install is from there. 

Otherwise;

### Method 1: Clone from GitHub (Recommended)

```bash
# Navigate to your ComfyUI custom_nodes directory
cd /path/to/ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/flamacore/ComfyUI-YouTubeUploader.git
```

**Windows (Command Prompt):**
```cmd
# Navigate to your ComfyUI custom_nodes directory
cd C:\path\to\ComfyUI\custom_nodes

# Clone the repository
git clone https://github.com/flamacore/ComfyUI-YouTubeUploader.git
```

### Method 2: Download and Extract

1. Download the repository as a ZIP file
2. Extract to your ComfyUI `custom_nodes` directory
3. Rename the folder to `ComfyUI-YouTubeUploader` if needed

### Method 3: Manual Copy (Windows)

```cmd
# Copy the entire directory to your ComfyUI custom_nodes directory
xcopy /E /I "C:\path\to\ComfyUI-YouTubeUploader" "C:\path\to\ComfyUI\custom_nodes\ComfyUI-YouTubeUploader"
```

### Install Dependencies

**Windows (Command Prompt):**
```cmd
# Navigate to the node directory
cd custom_nodes\ComfyUI-YouTubeUploader

# Install Google API dependencies
pip install -r requirements.txt

# Install ComfyUI-specific dependencies
pip install -r requirements_comfyui.txt
```

**Linux/macOS (Terminal):**
```bash
# Navigate to the node directory
cd custom_nodes/ComfyUI-YouTubeUploader

# Install Google API dependencies
pip install -r requirements.txt

# Install ComfyUI-specific dependencies
pip install -r requirements_comfyui.txt
```

## 🔧 Setup

### 1. YouTube API Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create project and enable YouTube Data API v3
3. Create OAuth 2.0 credentials (Desktop application)
4. Note your Client ID and Client Secret

### 2. Node Configuration

#### YouTube Auth Node
- **Input**: Client ID, Client Secret, Authenticate Now
- **Output**: Authentication status and channel info
- **Usage**: Set up once per session

#### YouTube Uploader Node
- **Video Input**: Connect from any video generation node
- **Text Inputs**: Title, description, tags
- **Settings**: Privacy level, FPS, upload enabled
- **Optional**: Audio track, custom thumbnail

## ⚠️ Safety Features

- **Upload Protection**: Must explicitly enable uploads
- **Testing Mode**: Test workflows without uploading
- **Error Handling**: Graceful failure with detailed messages
- **Dependency Checks**: Works even if dependencies missing

## 🎵 Supported Formats

- **Video**: Any format ComfyUI can generate
- **Audio**: WAV, MP3, FLAC (auto-converted to AAC)
- **Thumbnails**: Any image format (auto-resized)

## 🔍 Troubleshooting

### Common Issues

**"Dependencies not available"**
```bash
cd ComfyUI/custom_nodes/comfyui-youtube-uploader
pip install -r requirements.txt
```

**Authentication Failed**
- Check Client ID/Secret are correct
- Ensure YouTube Data API v3 is enabled
- Verify OAuth consent screen is configured

#### Video Upload Failed
- Check file size (YouTube has upload limits based on account verification status)
- Verify video format compatibility
- Ensure stable internet connection

#### Node Not Appearing
- Restart ComfyUI after installation
- Check console for error messages
- Verify all dependencies are installed

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Test with ComfyUI-Manager
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

- GitHub Issues: Bug reports and features
- ComfyUI Discord: Community support

---

**⚠️ Important**: Always test uploads with private videos first. Respect YouTube's Terms of Service and community guidelines.

**💡 Tip**: Use with AI video generation nodes for automated content creation workflows!
