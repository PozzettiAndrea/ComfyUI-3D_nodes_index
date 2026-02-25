# AAA Metadata System for ComfyUI

![GitHub License](https://img.shields.io/github/license/EricRollei/AAA_Metadata_System)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

Advanced metadata management and multi-format image save/load system for ComfyUI with professional features for Adobe workflows and color management.

## 🎯 Key Highlights

### 🎨 Professional Format Support
- **Adobe Photoshop PSD** - Load and save with full layer preservation, blend modes, and layer groups
- **True Vector SVG** - Native SVG export with embedded metadata and scalability
- **ICC Color Profile Management** - Embed and preserve color profiles (sRGB, Adobe RGB, ProPhoto RGB, etc.)
- **Adobe-Compatible Metadata** - XMP sidecar files formatted for Photoshop, Lightroom, Bridge, and other cataloging software
- **MWG-RS Compliant Regions** - Face/area metadata with coordinates compatible with Adobe's region standard

### 📁 Multi-Format Image Support
- **PNG** - Full metadata embedding with workflow preservation
- **JPEG** - Smart 4-stage fallback for EXIF size limits
- **TIFF** - 16-bit support with layers and metadata
- **WebP** - Modern format with full metadata
- **PSD** - Complete Photoshop file support with layers, blend modes, and groups

### 📋 Comprehensive Metadata Management
- **XMP Sidecar Files** - Industry-standard structured metadata for Adobe applications
- **TXT Summaries** - Human-readable metadata descriptions
- **JSON Export** - Complete metadata for custom workflows
- **Embedded EXIF/XMP** - In-image metadata for portability
- **SQLite Database** - Optional centralized metadata storage

## Overview

This metadata system provides professional-grade image and metadata management for ComfyUI workflows, with deep integration for Adobe software ecosystems and color-managed workflows.

## 🌟 Features

- **Multi-format Support**: Store metadata in multiple locations simultaneously for maximum compatibility with various software and workflows
- **Smart Merging**: Intelligently merge metadata from different sources with conflict resolution and prioritization
- **Extensible Structure**: Well-organized metadata structure with sections for different types of information, easily extended with custom fields
- **ComfyUI Integration**: Seamlessly integrates with ComfyUI nodes for workflow capture and parameter extraction
- **Human-readable Output**: Optional human-readable text format with context-aware descriptions for easy viewing
- **MWG Standard Compliance**: Follows Metadata Working Group standards for compatibility with professional software
- **Workflow Data Preservation**: Captures generation parameters and workflow structure for reproducibility
- **Advanced Querying**: Complex metadata filtering and searching with multiple query methods
- **Error Recovery**: Sophisticated error handling and recovery strategies to prevent data loss
- **Thread Safety**: Lock-based concurrency protection for multi-threaded applications

## Installation

### 📋 Requirements

- Python 3.8+
- ComfyUI
- PyExiv2 (optional, for enhanced embedded metadata support)
- ExifTool (optional, for additional format support)

### 🚀 Install as ComfyUI Custom Node

Option 1: Clone Repository

1. Clone this repository into your ComfyUI custom_nodes directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/EricRollei/AAA_Metadata_System.git
```

2. Install required dependencies:

```bash
cd AAA_Metadata_System
pip install -r requirements.txt
```

3. Restart ComfyUI

For detailed installation instructions, including platform-specific steps for PyExiv2 and ExifTool, see [INSTALLATION.md](INSTALLATION.md).

## Included Nodes

This package includes several ComfyUI nodes that integrate with the metadata system:

### Metadata Save Image Node

![Metadata Save Image Node](docs/images/save_image_node.png)

This node saves images with comprehensive metadata embedding. It extends ComfyUI's standard image saving capabilities with:

- **Multiple Format Support**: Save images in PNG, JPG, WEBP, TIFF, PSD, APNG, and SVG formats with appropriate metadata for each
- **Metadata Embedding**: Embeds comprehensive metadata directly into image files following industry standards
- **Color Profile Support**: Embed ICC color profiles (sRGB, Adobe RGB, ProPhoto) for color accuracy across devices
- **Layer Support**: Handle layers for formats that support them (TIFF, PSD) with custom blending modes
- **16-bit Export**: High-precision 16-bit image export for formats that support it
- **Alpha Channel Handling**: Advanced transparency handling with premultiplied, straight, and matte modes
- **Workflow Embedding**: Save ComfyUI workflow data directly in PNG files for later reloading
- **Animated PNG**: Create APNGs from multiple input images with timing controls
- **Multiple Documentation Formats**: Generate XMP sidecar, JSON workflow, and human-readable text files

The node automatically captures generation parameters from your workflow, including model names, prompts, sampling settings, and other crucial information that helps reproduce your results.

[Detailed documentation](documentation/ReadMe%20Docs/MetadataSaveImage_Node_Documentation.md)

### Metadata Query Node

This specialized node allows for extracting specific information from image metadata using multiple query methods:

- **Multiple Query Methods**:
  - **Simple Dot Notation**: Easy path-based access (e.g., "ai_info.generation.model")
  - **JSONPath Expressions**: Advanced queries with filtering and conditions
  - **Regular Expressions**: Pattern matching across the entire metadata structure
- **Source Flexibility**: Query from embedded metadata, XMP sidecars, text files, or database
- **Source Prioritization**: Configure which source to try first with customizable fallback chain
- **Formatted Output**: Results are properly formatted for human readability
- **Performance Optimization**: Query results are cached for rapid repeated access
- **Default Values**: Specify fallback values when data isn't found
- **Extraction Flexibility**: Return specific values or entire metadata structures

This node is invaluable for creating conditional workflows based on metadata values or for extracting specific information to display or process in other nodes.

[Detailed documentation](documentation/ReadMe%20Docs/MetadataQueryNodeDoc.md)

### Text Overlay Node

The Text Overlay Node allows you to overlay customizable text on images with extensive styling options:

- **Rich Text Styling**:
  - Font selection from system fonts with preview browser
  - Size, color, alignment, and spacing controls
  - Bold and italic formatting
- **Special Effects**:
  - **Gradient Effect**: Smooth color transitions
  - **Metal Effect**: Reflective metallic appearance
  - **Neon Effect**: Bright center with colored glow
  - **Emboss Effect**: 3D raised appearance
- **Layer Blending**: Multiple blend modes (normal, multiply, screen, overlay)
- **Shadow & Outline**: Customizable drop shadows and outlines with color control
- **Dynamic Text Wrapping**: Automatic wrapping based on width or character count
- **External Text Support**: Load content from TXT or Markdown files
- **Transparent Background**: Create text overlays with adjustable opacity
- **Precise Positioning**: Percentage-based offsets for exact placement

Perfect for adding watermarks, captions, titles, or decorative text to your AI-generated images.

[Detailed documentation](docs/TextOverlayNodev04Documentation.md)

### Image Duplicate Finder Node

This advanced node scans folders of images to identify duplicates and similar images using perceptual hashing algorithms:

- **Multiple Hash Algorithm Support**:
  - **pHash (Perceptual Hash)**: Best general-purpose algorithm for visual similarity
  - **dHash (Difference Hash)**: Excellent for detecting structural changes
  - **aHash (Average Hash)**: Fast simple algorithm for quick scanning
  - **wHash (Wavelet Hash)**: Sophisticated analysis using Haar wavelets
- **Multi-level Similarity Detection**:
  - Exact duplicates: Bit-for-bit identical images
  - Similar images: Visually similar but not identical
  - Variants: Related images with more significant differences
- **Advanced Analysis**:
  - Filename pattern analysis for related images
  - Metadata analysis including generation parameters
  - Combined hash and metadata scoring
- **Metadata Integration**:
  - Stores computed hashes for faster future processing
  - Records similarity relationships between images
- **Duplicate Management**:
  - Move or copy duplicates to organized folders
  - Group by similarity level
  - Keep largest/best quality option
- **Comprehensive Reporting**:
  - Detailed JSON reports
  - CSV export for spreadsheet analysis
  - Summary statistics

Invaluable for organizing large image collections, identifying variations from the same generation session, and maintaining a clean image library.

[Detailed documentation](docs/DuplicateImageFinderNodeDoc.md)

### Wan 2.2 Video Generation Nodes

Two specialized nodes for optimizing image dimensions for Hunyuan Video (Wan 2.2) workflows:

- **Wan22 Aspect Ratio Helper** (v2.2): Analyzes input images and generates optimal dimensions for Image-to-Video (I2V) workflows
- **Wan22 Size Preset** (v1.1): Generates optimal dimensions from predefined aspect ratios for Text-to-Video (T2V) workflows

Both nodes provide intelligent dimension calculation that:

- **Follows Wan 2.2 Official Specs**: All dimensions divisible by 8 pixels, aspect ratios from 1:3 to 3:1
- **Smart Hybrid Algorithm**: Checks 28 known Wan 2.2 training sizes first for best results, calculates optimal dimensions if no exact match
- **6 Size Presets**:
  - **Tiny** (~200K pixels): Fast prototyping and quick tests
  - **Small** (~400K pixels): Balanced quality for mobile/social media
  - **Medium** (~650K pixels): Standard professional quality
  - **Large** (~900K pixels): High-quality video production
  - **Extra-Large** (~1.4M pixels): Premium quality for detailed scenes
  - **Gigantic** (~2M pixels): Maximum quality for feature productions
- **15 Predefined Ratios** (Size Preset only): Portrait (6 ratios), Square (1:1), Landscape (8 ratios)
- **Multiple Outputs**: Width, height, and detailed info text showing all size options
- **No Rewiring Needed**: Change size preset from dropdown without reconnecting nodes

Perfect for ensuring your video generation inputs meet Wan 2.2 specifications without manual dimension calculations or trial-and-error testing.

[Detailed documentation](documentation/WAN22_NODES_README.md)

## Using the Metadata System

### 💡 Basic Usage

```python
from Metadata_system import MetadataService

# Initialize the service
service = MetadataService(debug=False, human_readable_text=True)

# Write metadata to all supported formats
metadata = {
    'basic': {
        'title': 'My AI Image',
        'description': 'A beautiful landscape',
        'keywords': ['landscape', 'mountains', 'AI generated'],
        'rating': 4,
        'creator': 'Your Name',
        'rights': 'Copyright © 2025'
    },
    'ai_info': {
        'generation': {
            'model': 'stable-diffusion-v1-5',
            'prompt': 'majestic mountains with snow caps',
            'negative_prompt': 'ugly, blurry',
            'sampler': 'euler_a',
            'steps': 30,
            'cfg_scale': 7.5,
            'seed': 1234567890,
            'width': 512,
            'height': 512
        }
    },
    'analysis': {
        'technical': {
            'blur': {
                'score': 0.92,
                'higher_better': True
            },
            'noise': {
                'score': 0.08,
                'higher_better': False
            }
        },
        'aesthetic': {
            'composition': 7.8,
            'color_harmony': 8.2,
            'overall': 7.9
        }
    }
}

# Write to all supported formats
result = service.write_metadata('path/to/image.png', metadata)

# Read metadata with fallback to other formats if primary fails
stored_metadata = service.read_metadata('path/to/image.png', source='embedded', fallback=True)

# Access specific metadata fields
if 'basic' in stored_metadata:
    print(f"Title: {stored_metadata['basic'].get('title')}")
    
if 'ai_info' in stored_metadata and 'generation' in stored_metadata['ai_info']:
    gen = stored_metadata['ai_info']['generation']
    print(f"Prompt: {gen.get('prompt')}")
    print(f"Seed: {gen.get('seed')}")
```

### Database Querying Example

```python
from Metadata_system.handlers.db import DatabaseHandler

# Initialize database handler
db = DatabaseHandler()

# Perform a complex search
results = db.search_images({
    # Find images with high aesthetic scores
    'scores': [
        ('aesthetic', 'overall', '>', 7.5),
        ('technical', 'blur.score', '>', 0.85)
    ],
    # With specific keywords
    'keywords': ['landscape', 'mountains'],
    # Using a specific model
    'classifications': [('style', 'photorealistic')],
    # In landscape orientation
    'orientation': 'landscape',
    # Order by creation date
    'order_by': 'images.created_date DESC',
    # Limit results
    'limit': 10
})

# Process results
for image in results:
    print(f"Found image: {image['filepath']}")
    print(f"Rating: {image.get('rating', 'N/A')}")
```

For more detailed usage instructions, including advanced features and examples, see [USAGE_GUIDE.md](USAGE_GUIDE.md).

## System Architecture

The metadata system follows a layered architecture:

```
┌────────────────────────────────────────────────────┐
│                   ComfyUI Nodes                    │
│  ┌──────────────┐ ┌───────────┐ ┌───────────────┐  │
│  │Metadata Save │ │Metadata   │ │Duplicate      │  │
│  │Image Node    │ │Query Node │ │Finder Node    │  │
│  └──────┬───────┘ └─────┬─────┘ └───────┬───────┘  │
└─────────┼───────────────┼───────────────┼──────────┘
          │               │               │
          ▼               ▼               ▼
┌─────────────────────────────────────────────────────┐
│              MetadataService (Facade)               │
│  ┌───────────────┐ ┌─────────────┐ ┌────────────┐   │
│  │write_metadata │ │read_metadata│ │merge_metadata   │
│  └───────────────┘ └─────────────┘ └────────────┘   │
└────────────────────────┬────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│                   Handlers Layer                    │
├─────────────┬───────────┬────────────┬─────────────┤
│ Embedded    │ XMP       │ Text File  │ Database    │
│ Handler     │ Handler   │ Handler    │ Handler     │
└─────────────┴───────────┴────────────┴─────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│                  Utility Components                  │
├─────────────┬───────────┬────────────┬─────────────┤
│ Format      │ Namespace │ Error      │ XML         │
│ Detector    │ Manager   │ Recovery   │ Tools       │
└─────────────┴───────────┴────────────┴─────────────┘
```

- **ComfyUI Nodes**: User interface for the metadata system in ComfyUI workflows
- **MetadataService**: Facade pattern service that coordinates between different handlers
- **Handlers**: Specialized components for different metadata formats
  - `EmbeddedMetadataHandler`: For metadata within image files using PyExiv2/ExifTool
  - `XMPSidecarHandler`: For XMP sidecar files following MWG standards
  - `TxtFileHandler`: For text file metadata with human-readable formatting
  - `DatabaseHandler`: For SQLite database storage with advanced querying
- **Utility Components**: Support infrastructure for the system
  - `FormatHandler`: Detects file formats and capabilities
  - `NamespaceManager`: Manages XMP namespaces and registrations
  - `ErrorRecovery`: Implements recovery strategies for errors
  - `XMLTools`: Provides XML processing utilities for XMP

For detailed architecture information, including component interactions and design decisions, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Metadata Structure

The metadata is organized into a hierarchical structure with sections for different types of information:

```
metadata
├── basic
│   ├── title                  # Image title
│   ├── description            # Detailed description
│   ├── keywords               # Tags/keywords as array
│   ├── rating                 # 1-5 star rating
│   ├── creator                # Author/creator name
│   └── rights                 # Copyright information
│
├── analysis
│   ├── technical              # Technical measurements
│   │   ├── blur               # Blur detection results
│   │   │   ├── score          # Blur score (higher = sharper)
│   │   │   └── higher_better  # Whether higher is better
│   │   ├── noise              # Noise detection results
│   │   └── dimensions         # Image dimensions
│   │
│   ├── aesthetic              # Aesthetic analysis 
│   │   ├── composition        # Composition quality score
│   │   ├── color_harmony      # Color harmony score
│   │   └── overall            # Overall aesthetic score
│   │
│   └── pyiqa                  # Image quality assessment models
│       ├── niqe               # No-reference IQA model
│       ├── musiq              # Multi-scale IQA model
│       └── clipiqa            # CLIP-based IQA model
│
├── ai_info
│   ├── generation             # Generation parameters
│   │   ├── model              # Model name/identifier
│   │   ├── prompt             # Positive prompt
│   │   ├── negative_prompt    # Negative prompt
│   │   ├── sampler            # Sampling algorithm
│   │   ├── steps              # Number of sampling steps
│   │   ├── cfg_scale          # Classifier-free guidance scale
│   │   ├── seed               # Random seed value
│   │   ├── width              # Image width
│   │   ├── height             # Image height
│   │   └── loras              # Array of LoRA models used
│   │
│   └── workflow               # Complete workflow structure
│       └── nodes              # Workflow node definitions
│
└── regions                    # Image regions/areas
    ├── faces                  # Detected faces
    │   ├── type               # Region type
    │   ├── name               # Region name/identifier
    │   ├── area               # Coordinates (normalized 0-1)
    │   └── extensions         # Additional analysis data
    │
    └── areas                  # Other detected regions
        ├── type               # Region type
        ├── name               # Region name/identifier
        ├── area               # Coordinates (normalized 0-1)
        └── extensions         # Additional data
```

This structured approach makes it easy to organize, retrieve, and understand the metadata associated with each image.

For a complete reference of the metadata structure, including field descriptions and format-specific details, see [METADATA_STRUCTURE.md](METADATA_STRUCTURE.md).

## Integration

The metadata system can be integrated with other ComfyUI nodes or Python applications:

```python
# Create a metadata-aware ComfyUI node
class MyMetadataAwareNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "metadata": ("METADATA", {"default": None})
            }
        }
    
    RETURN_TYPES = ("IMAGE", "METADATA")
    FUNCTION = "process"
    
    def process(self, images, metadata=None):
        # Initialize metadata if None
        if metadata is None:
            metadata = {}
            
        # Process images...
        
        # Add your own metadata
        if 'analysis' not in metadata:
            metadata['analysis'] = {}
        
        metadata['analysis']['my_analysis'] = {
            'score': 0.85,
            'timestamp': self._get_timestamp()
        }
        
        return (processed_images, metadata)
```

For detailed integration instructions, including custom handler implementation and extension points, see [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md).

## API Reference

The metadata system provides a comprehensive API:

```python
# MetadataService API
service = MetadataService(debug=False, human_readable_text=True)
service.write_metadata(filepath, metadata, targets=None)
service.read_metadata(filepath, source='embedded', fallback=True)
service.merge_metadata(filepath, metadata, targets=None)
service.set_resource_identifier(resource_uri)
service.set_text_format(human_readable=True)

# Handler APIs
from Metadata_system.handlers.embedded import EmbeddedMetadataHandler
from Metadata_system.handlers.xmp import XMPSidecarHandler
from Metadata_system.handlers.txt import TxtFileHandler
from Metadata_system.handlers.db import DatabaseHandler

# DatabaseHandler query API
db = DatabaseHandler()
results = db.search_images({...})
batch_results = db.batch_operation('read', filepaths)
```

For a comprehensive API reference, including all methods, parameters, and return values, see [API_REFERENCE.md](API_REFERENCE.md).

## 👏 Acknowledgements

- Thanks to the ComfyUI team for creating an amazing platform
- PyExiv2 for comprehensive EXIF/XMP metadata support
- The Metadata Working Group (MWG) for establishing metadata standards


## Contributing

Contributions are welcome! The codebase follows PEP 8 style guidelines and uses comprehensive docstrings for all classes and methods. See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:

- Code of conduct
- Development setup
- Pull request process
- Coding standards
- Documentation requirements
- Testing approach

## License

Dual License:

1. Non-Commercial Use: This software is licensed under the terms of the Creative Commons Attribution-NonCommercial 4.0 International License.
   
2. Commercial Use: For commercial use, a separate license is required. Please contact Eric Hiss at eric@historic.camera or eric@rollei.us for licensing options.

## 📞 Contact

- GitHub: [EricRollei](https://github.com/EricRollei)
- Email: eric@historic.camera or eric@rollei.us