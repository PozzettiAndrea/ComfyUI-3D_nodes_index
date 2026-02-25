# ComfyUI Nakagawa - Video Websocket Nodes

A collection of custom nodes for ComfyUI that send video data through websockets instead of saving to disk.

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes` directory
2. Restart ComfyUI
3. The nodes will appear in the `api/video` category

## Nodes

### Save Video Websocket

Sends video data through websocket instead of saving to disk. Compatible with ComfyUI's native `SaveVideo` node.

**Inputs:**
- `video` (VIDEO) - The video to send through websocket
- `format` (COMBO) - Output video format (auto, mp4, webm, avi, mov, etc.)
- `codec` (COMBO) - Video codec to use (auto, libx264, libx265, libvpx-vp9, etc.)

**Features:**
- Uses ComfyUI's native video handling system
- Supports all formats and codecs available in your ComfyUI installation
- Streams video data through websocket with proper headers
- Progress tracking during processing

### Save WEBM Websocket

Converts image sequences to WEBM format and sends through websocket. Compatible with ComfyUI's native `SaveWEBM` node.

**Inputs:**
- `images` (IMAGE) - Sequence of images to convert to WEBM
- `codec` (COMBO) - WEBM codec (vp9, av1)
- `fps` (FLOAT) - Frames per second (0.01-1000.0, default: 24.0)
- `crf` (FLOAT) - Quality setting (0-63, default: 32.0, lower = better quality)

**Features:**
- Specialized WEBM encoding with VP9 and AV1 support
- Optimized for web streaming
- Real-time progress updates
- AV1 preset optimization for faster encoding

## Usage

These nodes work exactly like their native ComfyUI counterparts (`SaveVideo` and `SaveWEBM`) but instead of saving files to disk, they send the video data through ComfyUI's websocket connection. This is useful for:

- Real-time video streaming applications
- Web-based ComfyUI integrations
- Custom clients that need direct video data access
- Reducing disk I/O in automated workflows

## Technical Details

### Video Transmission Protocol

Videos are sent as **binary data** through a custom WebSocket event (type 100) for maximum efficiency:

#### Binary Message Structure

**Note:** ComfyUI's WebSocket protocol adds a 4-byte message length header before the actual data.

```
[Message Length (4)] [Magic Bytes (4)] [Format Length (4)] [Format String (N)] [Video Data]
```

- **Message Length**: 32-bit big-endian integer - Total message size (added by ComfyUI)
- **Magic Bytes**: `VIDF` (0x56494446) - Identifies video data format
- **Format Length**: 32-bit little-endian integer - Length of format string
- **Format String**: UTF-8 encoded format (e.g., "mp4", "webm")
- **Video Data**: Raw video binary data

#### Client Implementation

To receive video data on the client side:

```javascript
// Listen for video data (event type 100)
ws.onmessage = (e) => {
  if (e.data instanceof ArrayBuffer) {
    const view = new DataView(e.data);
    
    // Skip ComfyUI's 4-byte message length header and check for "VIDF" magic bytes
    if (view.getUint32(4) === 0x46444956) {
      const fmtLen = view.getUint32(8, true);
      const format = new TextDecoder().decode(new Uint8Array(e.data, 12, fmtLen));
      const video = e.data.slice(12 + fmtLen);
      
      // Create video URL
      const url = URL.createObjectURL(new Blob([video], {type: `video/${format}`}));
      document.querySelector('video').src = url;
    }
  }
};
```