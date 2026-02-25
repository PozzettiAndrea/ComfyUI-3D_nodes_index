# ComfyUI BishaNodes
**Custom Nodes for ComfyUI to Simplify Multi-Resolution and Prompt Workflows**

## 🌟 **Nodes Overview**

### 1. Simple Size Picker
### 2. Empty Latent Size Picker
### 3. Create Prompts With Text From File
### 4. Wildcard Replace
### 5. Wildcard Replace (with values from File)
### 6. Load Data From Files

---

## 📋 **Features**

### 🖼️ **Resolution Nodes**
#### **Simple Size Picker**
- **30+ Standardized Resolutions** (512px to 8K):
  - ✅ **Square** (1:1) – 512×512 to 2048×2048
  - ✅ **Portrait** (2:3, 9:16) – 512×768 to 1080×1920
  - ✅ **Landscape** (16:9, 3:2) – 768×512 to 3840×2160 (4K)
  - ✅ **Ultra-Wide** (21:9, 32:9) – 2560×1080 to 7680×2160
  - ✅ **Exotic Ratios** (e.g., 9600×1200 at 8:1)
- **User-Friendly**:
  - Categorized dropdown menu with tooltips
  - Zero-configuration workflow integration

#### **Empty Latent Size Picker** (Extended Version)
- All features of Simple Size Picker **PLUS**:
- 🚀 **Auto-Generated Latent Output**:
  - Directly connects to samplers
  - Eliminates manual "Empty Latent Image" nodes
  - Preserves selected dimensions in latent space

### 📝 **Prompt Engineering Nodes**
#### **Create Prompts With Text From File**
- **Batch Prompt Generation**:
  - 🔄 Combine base text with dynamic content from files
  - 🎛️ Control output quantity with `results` parameter
- **File-Based Variability**:
  - Supports .txt files with line-separated entries
  - Random line selection for diverse outputs
- **Use Cases**:
  - Character variations (e.g., "a portrait of [name_from_file]")
  - Style mixing ("in the style of [artist_from_file]")
  - Batch testing different descriptors

#### **Wildcard Replace** and **Wildcard Replace (with values from File)**
- **Enhance Prompt with templates**:
  - 🔄 Combine base text with dynamic content from files
  - 🎛️ Control values quantity with `values_count` parameter
- **Variability of values**:
  - Supports .txt files with line-separated entries _for Wildcard Replace (with values from File)_
  - Supports a list of values as input data
  - Random value selection for diverse outputs
- **Use Cases**:
  - Character variations (e.g., "a portrait of {person} with {object}")
  - Style mixing ("in the style of {artist}")
  > `{person}`, `{object}` and `{artist}` are set in the `wildcard` parameter

#### **Load Data From Files**
- Loading data from multiple files with the ability to disable files

---

### 🛠 **Installation**

#### **Method 1: Manual (Git)**
1. Navigate to your ComfyUI’s `custom_nodes` directory:
```bash
   cd /path/to/ComfyUI/custom_nodes/
```
2. Clone the repository **into this folder**:
```bash
   git clone https://github.com/vladpro3/ComfyUI_BishaNodes.git
```
3. Restart ComfyUI.

#### **Method 2: Custom Nodes Manager**
Alternatively, search for `ComfyUI_BishaNodes` in ComfyUI’s **Custom Nodes Manager** and install with one click.

---

## 🎮 **Usage Examples**

```
TODO
```

---

## 🔧 **Technical Specifications**

```
TODO
```

---

## 📜 **License**
MIT License - Free for commercial and personal use.

---

> **Happy Generating!** 🎨  
> *For real-time updates, star this repo.*
