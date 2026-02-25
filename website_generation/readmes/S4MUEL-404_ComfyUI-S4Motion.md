# ComfyUI-S4Motion

**Version: 1.5.0**

A comprehensive motion animation toolkit for ComfyUI, providing 14 professional-grade motion control nodes for creating dynamic animations with production-ready quality and reliability.

## 🚀 Features

### Core Motion Controls
- **💀Motion Config** - Central configuration hub for motion animations
- **💀Motion Position** - Precise position animation with smooth curves
- **💀Motion Position On Path** - Path-based motion control for complex trajectories
- **💀Motion Rotation** - Smooth rotation animations with customizable pivot points
- **💀Motion Scale** - Dynamic scaling effects with proportional controls
- **💀Motion Opacity** - Alpha channel animation for fade effects

### Advanced Effects
- **💀Motion Distortion** - Professional distortion effects (Wave, Vortex, Radial)
- **💀Motion Shake** - Realistic shake and vibration effects
- **💀Motion Mask** - Animated mask controls for selective effects

### Video Processing
- **💀Video Crop** - Precise video cropping with animation support
- **💀Video Frames** - Advanced frame extraction and processing
- **💀Video Combine** - Concatenate two videos or image sequences in time sequence
- **💀Video Info** - Analyze video or image sequence properties (dimensions, frame count, duration, FPS)
- **💀Video Resize** - Professional video and image sequence resizing with multiple scaling options

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "S4Motion" 
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom_nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```
   git clone https://github.com/S4MUEL-404/ComfyUI-S4Motion.git
   ```
3. Install dependencies:
   ```
   pip install -r ComfyUI-S4Motion/requirements.txt
   ```
4. Restart ComfyUI

## 🔧 Dependencies

The plugin features intelligent dependency management with graceful fallbacks:

### Core Dependencies (Required)
- **PyTorch** - Core tensor operations and ComfyUI compatibility
- **Pillow** - Professional image processing and animation frames
- **NumPy** - High-performance numerical computing for motion curves

### Optional Dependencies (Enhanced Features)
- **OpenCV** - Video processing and advanced distortion effects
- **Scikit-image** - High-quality image transformations
- **SciPy** - Scientific computing for advanced motion curves
- **Bezier** - Professional motion curve calculations

All dependencies are automatically validated at startup with production-quality logging and fallback mechanisms.

## 📖 Usage

1. **Find Nodes**: All S4Motion nodes are prefixed with 💀 in the ComfyUI node browser
2. **Categories**: Look under "💀S4Motion" category
3. **Production Ready**: All nodes include comprehensive error handling and logging
4. **Examples**: Check the `examples/` folder for workflow documentation

### Quick Start Example
1. Add Motion Config node to establish animation timeline
2. Connect motion effector nodes (Position, Rotation, Scale, etc.)
3. Configure motion parameters and curves
4. Connect to your image/video processing workflow
5. Execute animation

## 🎯 Key Features

- ✅ **Production Quality** - Enterprise-grade error handling and validation
- ✅ **Smart Dependencies** - Automatic dependency management with fallbacks
- ✅ **Motion Curves** - Professional easing with Bezier curve support
- ✅ **Timeline Control** - Precise timing with delay, duration, and loop options
- ✅ **Advanced Effects** - Wave, vortex, and radial distortion capabilities
- ✅ **Video Support** - Comprehensive video processing and frame control
- ✅ **Path Animation** - Complex trajectory support for sophisticated motion

## 🎨 Motion Curves

S4Motion supports professional easing functions:
- **Linear** - Constant speed motion
- **Ease In** - Gradual acceleration
- **Ease Out** - Gradual deceleration  
- **Ease In Out** - Smooth acceleration and deceleration

With optional Bezier curve support for ultra-smooth professional animations.

## 🔄 Animation Controls

Each motion node supports:
- **Duration** - Animation length in seconds
- **Delay** - Start delay for sequenced animations
- **Inverse** - Reverse motion for return-to-origin effects
- **Loop** - Continuous repetition for endless animations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or report issues.

## 📜 License

This project is open source. Please respect the licensing terms.

---

**Author:** S4MUEL  
**Website:** [s4muel.com](https://s4muel.com)  
**Version:** 1.5.0
