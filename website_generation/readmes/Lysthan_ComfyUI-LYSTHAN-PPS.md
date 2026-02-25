# Privacy-Protected Saver Node - Installation Guide

# This node protects the privacy of the output, do not use for illegal purposes
# Usage: Search for the PPS node in ComfyUI and connect the batch of images to this node

## 📦 Dependencies

LYSTHAN_PPS node requires the following dependencies:

- **pyzipper** 
- **imageio[ffmpeg]** 
- **cryptography** 

---

## 🚀 Dependencies Installation

### Method 1: Automatic Installation (Recommended)

#### Windows Users:
Double-click to run `install_dependencies.bat`

#### macOS/Linux Users:
```bash
python install_dependencies.py
```

---

### Method 2: Using requirements.txt

```bash
pip install -r requirements.txt
```

---

### Method 3: Manual Installation

```bash
pip install pyzipper
pip install imageio[ffmpeg]
pip install cryptography
```

---

---

## 📝 Node Usage

### Input Parameters

- **images** (required) - Batch of images to pack
- **fps** (optional) - Video frame rate, default 16
- **password** (optional) - ZIP encryption password, leave empty for no encryption
- **mode** (optional) - Mode:
  - `both` - Video and images (default)
  - `images only` - Images only
  - `video only` - Video only

### Output

- Auto-saved to ComfyUI output directory
- Filename format: `YYYYMMDD_HHMMSS.jpg`

### Console Output Example

```
==================================================
LYSTHAN_PPS - Start
==================================================

==================================================
LYSTHAN_PPS - Complete
Docu Size: 15.67 MB
Frame Count: 10
Content: both
Temp folder cleaned
Time consumed: 3.45 s
==================================================
```

---

## ⚠️ FAQ

### Q: What if installation fails?

A: Try upgrading pip and reinstall:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Q: imageio still reports missing ffmpeg after installation?

A: Try manually installing ffmpeg:
```bash
pip install imageio-ffmpeg
```

### Q: Encoding error when running batch file on Windows?

A: Right-click `install_dependencies.bat` and select "Run as administrator"

---

## 📧 Support

For issues, visit: https://github.com/Lysthan

---

## 📄 License

This node employs RSA-2048 and AES-256-GCM for encryption
For privacy protection only, do not use for illegal purposes
