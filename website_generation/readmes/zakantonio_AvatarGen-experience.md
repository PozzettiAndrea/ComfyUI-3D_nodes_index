# ✨ Avatar Generation Experience

A custom node for ComfyUI that transforms user photos into stylized character avatars.

## 🔍 Project Overview

Avatar Generation Experience is an interactive application developed as a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI). The project creates an engaging user experience that transforms ordinary photos into stylized avatars across different fictional universes and themes.

## 🚀 Key Features

- **Themed Character Groups**: Includes Marvel, DC, Disney, Pixar, historical figures, and film characters
- **Real-time Photo Processing**: Captures and transforms user photos on the fly
- **Interactive UI**: Intuitive interface for character selection and avatar generation
- **QR Code Scanning**: Scan user QR code to start the experience
- **QR Code Sharing**: Generated avatars can be shared via QR codes
- **Screensaver Gallery**: Displays previously generated avatars when the system is idle
- **Google Drive Integration**: Cloud storage and sharing capabilities
- **Simplified Controls**: The entire experience can be navigated using just a three-button joystick, designed for exhibition on large vertical screens at trade shows and events

## 🛠️ Technical Implementation

- **Custom ComfyUI Node**: Extends ComfyUI's functionality with specialized image processing
- **WebSocket Communication**: Real-time updates during the generation process
- **IndexedDB Storage**: Local caching of generated images
- **REST API Integration**: Communicates with backend services for image processing
- **Responsive Design**: Works across different device sizes

## 📸 Screenshots

| ![Application Interface](web/assets/screen_1.png) | ![Generated Avatar](web/assets/screen_2.png) |
|:---:|:---:|
| *Main interface showing Themed Character Groups selection* | *Example of customization options available for avatar generation* |

## 💻 Technologies Used

- JavaScript
- WebSockets
- IndexedDB
- Google Drive API
- ComfyUI Framework
- Python (for QR code scan)