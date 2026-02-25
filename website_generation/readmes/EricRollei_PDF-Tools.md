# PDF Tools - ComfyUI Custom Node Package

Advanced PDF processing, OCR, and AI vision analysis nodes for ComfyUI.

## 📢 Important Notice: Package Split

The **download functionality has moved** to a separate package:

- **PDF Tools** (this package): PDF extraction, OCR, AI vision processing
- **[Download Tools](../download-tools/)** (new package): gallery-dl and yt-dlp downloaders

If you need media download nodes, install the **download-tools** package separately:

```powershell
cd ComfyUI/custom_nodes/download-tools
.\install.ps1
```

---

## 🎉 Quick Start

### Installation

```powershell
cd ComfyUI/custom_nodes/PDF_tools
.\install.ps1
```

### Verify Installation

```powershell
.\check_install.ps1
```

### Start Using

1. Restart ComfyUI
2. Look for nodes under categories: **PDF**, **OCR**, **Vision**, **Layout**
3. Start processing documents!

## 📦 Available Nodes

### PDF Extraction
- **PDF Extractor v08/v09** - Advanced image extraction with quality assessment
  - Automatic spread detection for scanned books
  - Image quality scoring (sharpness, contrast, brightness)
  - Duplicate detection
  - Organize output by quality
  - JSON metadata export
  
- **Simple PDF Extractor** - Basic extraction without advanced features

### OCR (Optical Character Recognition)
- **Surya OCR Layout Node** - State-of-the-art multilingual OCR
  - 90+ languages supported
  - Layout-aware text extraction
  - High accuracy on complex documents
  - GPU-accelerated inference
  
- **Surya Layout OCR Hybrid** - Combined layout analysis + OCR
  - Single-step document processing
  - Preserves reading order
  - Handles multi-column layouts
  
- **PaddleOCR VL Remote** - Specialized for Chinese/CJK documents
  - Excellent for Asian language texts
  - Remote processing capabilities
  - **Requires separate virtual environment** (see [PaddleOCR_VL_SETUP.md](Docs/PaddleOCR_VL_SETUP.md))
  - Runs as standalone service due to CUDA version conflicts

### Layout Analysis
- **Enhanced Layout Parser v06** - Advanced document understanding
  - Detects titles, paragraphs, tables, figures, lists
  - Hierarchical structure extraction
  - Reading order detection
  - Bounding box coordinates
  
- **LayoutLMv3 Node** - Microsoft's document AI model
  - Multi-modal document understanding
  - Form and receipt processing
  - Table structure recognition

### AI Vision & Object Detection
- **Florence2 Rectangle Detector** - Microsoft Florence-2 vision model
  - Object detection with bounding boxes
  - Image captioning (simple & detailed)
  - Visual question answering
  - OCR and text detection
  - Region-specific descriptions
  
- **Florence2 Cropper Node** - Crop based on detections
  - Automatic image region extraction
  - Batch processing of detected objects

## 🚀 Key Features

✅ **Smart PDF Extraction** - Quality scoring, spread detection, duplicate removal  
✅ **Multilingual OCR** - 90+ languages with Surya, Chinese/Japanese with PaddleOCR  
✅ **Layout Understanding** - Detect document structure (titles, paragraphs, tables)  
✅ **AI Vision Models** - Florence-2 for object detection and image analysis  
✅ **Batch Processing** - Process multiple documents efficiently  
✅ **GPU Acceleration** - Fast inference with CUDA support  
✅ **Quality Assessment** - Automatic image quality evaluation  
✅ **JSON Export** - Structured metadata for all extractions

## 💡 Usage Examples

### Extract High-Quality Images from PDF

```
Node: PDF Extractor v08
├── Input PDF: "mybook.pdf"
├── Output Folder: "./extracted_images"
├── Options:
│   ├── ✓ quality_assessment (score each image)
│   ├── ✓ spread_detection (detect 2-page spreads)
│   ├── ✓ organize_by_quality (high/medium/low folders)
│   └── ✓ save_json_output (metadata file)
└── Result: Images sorted by quality with detailed metrics
```

### OCR a Scanned Document

```
Node: Surya OCR Layout Node
├── Input: "scanned_page.png"
├── Languages: ["en"] or ["en", "es", "fr"]
├── Output:
│   ├── Extracted text with 95%+ accuracy
│   ├── Bounding boxes for each word/line
│   └── Layout information (columns, paragraphs)
```

### Detect Objects in Images

```
Node: Florence2 Rectangle Detector
├── Input Image: "photo.jpg"
├── Task: <OD> (Object Detection)
├── Output:
│   ├── Bounding boxes for detected objects
│   ├── Labels (e.g., "person", "car", "dog")
│   └── Confidence scores
```

### Analyze Document Layout

```
Node: Enhanced Layout Parser v06
├── Input: PDF page or image
├── Output:
│   ├── Regions: title, text, table, figure, list
│   ├── Bounding box coordinates
│   ├── Hierarchical structure
│   └── Reading order
```

## 🔧 System Requirements

- **OS:** Windows 10/11 (primary), Linux compatible
- **Python:** 3.10+ (included with ComfyUI)
- **GPU:** NVIDIA with CUDA recommended (CPU works but slower)
- **RAM:** 8GB minimum, 16GB+ recommended for AI models
- **Storage:** 5-10GB for packages + models

## 📚 Documentation

### Main Guides
- **[INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)** - Detailed setup instructions
- **[CODE_OVERVIEW.md](CODE_OVERVIEW.md)** - Understand the codebase structure
- **[LICENSE.md](LICENSE.md)** - Licensing terms and conditions
- **[CREDITS.md](CREDITS.md)** - Third-party libraries and acknowledgments

### Additional Docs
- **[SURYA_OCR_NODE_GUIDE.md](SURYA_OCR_NODE_GUIDE.md)** - Surya OCR detailed guide
- **[PaddleOCR_VL_SETUP.md](Docs/PaddleOCR_VL_SETUP.md)** - PaddleOCR separate environment setup
- **[PDF_LAYER_DETECTION_GUIDE.md](Docs/PDF_LAYER_DETECTION_GUIDE.md)** - PDF layer analysis
- **[BATCH_PROCESSING_GUIDE.md](Docs/BATCH_PROCESSING_GUIDE.md)** - Batch workflow tips

## 🔧 Core Dependencies

Auto-installed with `install.ps1`:

- **PyMuPDF (fitz)** - PDF processing and rendering
- **Pillow** - Image processing and manipulation
- **numpy** - Array operations and numerical computing
- **opencv-python** - Computer vision operations
- **transformers** - Hugging Face AI models
- **torch** - PyTorch for deep learning
- **surya-ocr** - Advanced OCR engine
- **paddleocr** - Chinese/multilingual OCR (basic version)
- **layoutparser** - Document layout analysis

**Note:** PaddleOCR VL requires a **separate virtual environment** due to CUDA version conflicts. See [PaddleOCR_VL_SETUP.md](Docs/PaddleOCR_VL_SETUP.md) for setup instructions.

See [requirements.txt](requirements.txt) for complete list.

## 📁 Project Structure

```
PDF_tools/
├── nodes/              # ComfyUI node implementations
│   ├── pdf_extractor_v08.py      # Advanced PDF extraction
│   ├── surya_ocr_layout_node.py  # Surya OCR
│   ├── eric-florence2-cropper-node.py  # Florence-2 vision
│   └── enhanced_layout_parser_v06.py   # Layout analysis
├── florence2_scripts/  # Florence-2 AI vision models
├── sam2_scripts/       # SAM2 segmentation models
├── tools/              # Utility scripts
├── Docs/               # Comprehensive documentation
└── __init__.py         # Node registration
```

## 🐛 Troubleshooting

### "Module not found" errors
Run the check script: `.\check_install.ps1`

### "CUDA out of memory" 
- Close other GPU applications
- Process fewer pages at once
- Use CPU mode (slower but works)

### OCR accuracy issues
- Ensure image is high resolution (300+ DPI)
- Check language settings match document
- Try different OCR nodes for comparison

### PDF extraction produces no images
- Verify PDF contains raster images (not just text)
- Check PDF isn't encrypted or password-protected
- Try Simple PDF Extractor for troubleshooting

See [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for more troubleshooting.

## 🎯 Best Practices

1. **High-Quality Inputs** - Use 300+ DPI scans for best OCR results
2. **Enable Quality Assessment** - Let the tool filter low-quality extractions
3. **Batch Process** - Process multiple documents in one workflow
4. **Export Metadata** - Save JSON outputs for downstream processing
5. **GPU Acceleration** - Use CUDA for 10x faster inference with AI models

## 📝 Version Info

Current versions:
- **PyMuPDF:** 1.26.4+
- **Transformers:** 4.55.0+
- **Torch:** 2.7.1+cu128
- **Surya-OCR:** Latest from GitHub
- **Florence-2:** Microsoft Research

## 📄 License

Copyright (c) 2025 Eric Hiss. All rights reserved.

Dual-licensed:
- **Non-Commercial Use:** [Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)](http://creativecommons.org/licenses/by-nc/4.0/)
- **Commercial Use:** Requires separate license - contact eric@rollei.us

**Important:** This project uses third-party libraries with various licenses (GPL, AGPL, MIT, Apache). See [CREDITS.md](CREDITS.md) for complete dependency licensing.

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code style guidelines
- Testing requirements  
- Pull request process
- Development setup

## 👥 Contact & Support

- **Author:** Eric Hiss
- **GitHub:** [EricRollei](https://github.com/EricRollei)
- **Email:** eric@historic.camera, eric@rollei.us
- **Issues:** Open an issue on GitHub for bugs or feature requests

## 🙏 Acknowledgments

Special thanks to:
- **ComfyUI** community for the amazing extensible platform
- **Microsoft Research** for Florence-2 vision models
- **Vikp** for Surya OCR
- **Meta AI** for SAM2 segmentation models
- **Hugging Face** for model hosting and transformers library
- All open-source developers whose work makes this possible

See [CREDITS.md](CREDITS.md) for detailed acknowledgments.

---

**Ready to process documents!** Install dependencies, restart ComfyUI, and start extracting.
