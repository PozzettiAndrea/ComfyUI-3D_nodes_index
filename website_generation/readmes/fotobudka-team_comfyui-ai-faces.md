# ComfyUI AI Faces - Photo Verification Node

A ComfyUI custom node for automated face verification, designed to check if a person is clearly visible and suitable for passport-style photos. This node performs comprehensive facial analysis to ensure photo quality meets identification document standards.

## Features

This node performs the following verifications:

### 🔍 **Face Detection & Count**
- Detects faces in the image using InsightFace
- Ensures exactly one person is present in the photo
- Rejects photos with no faces or multiple people

### 📏 **Face Size Validation**
- Checks if face occupies appropriate portion of the image
- Face must be between 10% and 70% of the total image area
- Ensures proper distance from camera for ID photo standards

### 🎯 **Head Pose Analysis**
- Validates head orientation using 3D pose estimation
- Checks pitch (up/down tilt) - max 30° deviation
- Checks yaw (left/right turn) - max 30° deviation  
- Checks roll (side tilt) - max 30° deviation
- Ensures face is looking straight at camera

### 🌟 **Image Quality Assessment**
- Analyzes face detection confidence score
- Requires minimum 75% confidence for acceptable quality
- Ensures proper lighting and image sharpness

### 👁️ **Facial Feature Visibility**
- Uses BiSeNet face parsing to segment facial features
- Validates presence and visibility of:
  - Left and right eyebrows (min 0.4% of face area)
  - Left and right eyes (min 0.3% of face area, unless wearing glasses)
  - Nose (min 2.0% of face area)
  - Upper and lower lips (min 0.4% of face area each)

### 🚫 **Occlusion Detection**
- Detects and rejects photos with:
  - Non-transparent sunglasses or dark eyewear
  - Hats, caps, or head coverings
- Allows transparent prescription glasses

### 🔬 **Glasses Transparency Check**
- Analyzes glasses pixel brightness to determine transparency
- Uses 50-pixel brightness threshold to distinguish clear vs. dark glasses
- Automatically adjusts feature visibility requirements for glasses wearers

## Installation

### Method 1: Git Clone (Recommended)

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd /path/to/ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/your-username/comfyui-ai-faces.git
```

3. Install dependencies:
```bash
cd comfyui-ai-faces
pip install -r requirements.txt
```

### Method 2: Manual Installation

1. Download the repository as ZIP and extract to your ComfyUI custom nodes folder
2. Install the required packages:
```bash
pip install opencv-python torch numpy torchvision requests onnxruntime insightface supervision Pillow matplotlib
```

### Method 3: ComfyUI Manager

If you have ComfyUI Manager installed:
1. Open ComfyUI Manager
2. Search for "AI Faces" or "Photo Verification"
3. Click Install

## Usage

1. **Restart ComfyUI** after installation
2. The node will appear in the node menu under `Fotobudka > Photo Verification`
3. Connect an image input to the node
4. The node will:
   - ✅ Pass through the image if verification succeeds
   - ❌ Throw an error with specific feedback if verification fails

### Example Workflow

```
Load Image → Photo Verification → Save Image
```

The node acts as a quality gate - images that pass verification continue through your workflow, while rejected images stop the workflow with descriptive error messages.

## Error Messages

The node provides specific, actionable feedback:

- **Face Detection Issues:**
  - "No face detected. Please ensure your face is clearly visible."
  - "Only one person should be in the photo. Please ensure you are alone in the image."

- **Distance Problems:**
  - "Move closer to the camera so your face occupies more of the image."
  - "Move away from the camera so your face occupies less of the image."

- **Pose Issues:**
  - "Turn your head more towards the camera (too much side rotation)."
  - "Don't tilt your head too much up or down."
  - "Don't tilt your head to the side."
  - "Unable to determine head position."

- **Quality Issues:**
  - "Take a photo with better lighting and ensure image sharpness."

- **Occlusion Problems:**
  - "Please remove your glasses"
  - "Please remove your hat or cap"
  - "Please remove your glasses and hat or cap"

- **Feature Visibility:**
  - "Please show your [specific facial features] more clearly"

## Technical Details

### Models Used
- **InsightFace Buffalo_L**: Face detection and 3D pose estimation
- **BiSeNet**: 19-class face parsing for feature segmentation
- **Execution Providers**: CPU and GPU (CUDA) support

### Face Parsing Classes
The node uses 19 semantic classes for face parsing:
- Background, face skin, eyebrows, eyes, nose, mouth, lips, hair, glasses, hat, etc.

### Requirements
- Python 3.8+
- PyTorch
- OpenCV
- InsightFace
- ONNX Runtime
- Other dependencies in `requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [InsightFace](https://github.com/deepinsight/insightface) for face detection and analysis
- [BiSeNet](https://github.com/zllrunning/face-makeup.PyTorch) for face parsing
- ComfyUI community for the amazing framework

---

For questions, issues, or feature requests, please open an issue on GitHub.
