# ComfyUI Generator Add-on

A Blender add-on that integrates with ComfyUI for AI-powered model generation. Provides workflow management, image input handling, and real-time status tracking for seamless AI art creation within Blender's interface.

## Features

- **ComfyUI Integration**: Connect to ComfyUI servers for AI model generation
- **Workflow Management**: Load and execute ComfyUI workflows with custom inputs
- **Image Handling**: Input image preview and automatic image loading
- **Real-time Status**: Progress tracking and detailed logging
- **Threaded Operations**: Non-blocking generation with background processing
- **User Interface**: Collapsible sections with warning system and log viewer

## Installation

1. Download the add-on file
2. In Blender, go to Edit → Preferences → Add-ons
3. Click "Install" and select the downloaded file
4. Enable the "ComfyUI Generator" add-on
5. Access the tools in the 3D Viewport under the "ComfyUI" tab

## Requirements

- Blender 4.5.0 or higher
- Running ComfyUI server instance
- ComfyUI workflow files

## Usage

Configure your ComfyUI server URL and workflow file path, select an input image, then click "Generate Model" to start the AI generation process. Monitor progress in real-time through the status and log sections.