# ComfyUI Virtual Webcam

A Virtual Camera Output For ComfyUI.

On Windows, it will use the OBS Virtual Camera driver. So make sure you have OBS installed.

Then in your other webcam capable applications, such as Google Meet, Teams, Zoom and even OBS itself, you can connect to the `OBS Virtual Camera` option and see what you are outputting from ComfyUI.

## Video Tutorial

[https://youtu.be/zg-UNTQ4rMw](https://youtu.be/zg-UNTQ4rMw)

[![ComfyUI Virtual Webcam](https://img.youtube.com/vi/zg-UNTQ4rMw/0.jpg)](https://youtu.be/zg-UNTQ4rMw)

## Install ComfyUI Virtual Webcam

Install the custom node **ComfyUI Virtual Webcam** using the manager,

![](./img/manager-virtual-webcam.jpg)

Or you can use your command/terminal prompt.

1. Navigate to your `ComfyUI/custom_nodes` folder.
2. Run,

```bash
git clone https://github.com/Sean-Bradley/ComfyUI-Virtual-Webcam.git
```

3. Restart ComfyUI

You will find the new Virtual Camera node in the Nodes menu item under SBCODE.

Or you can double click the workspace and search for `virtual`

## How to Use

1. Copy Paste the [basic workflow](#basic-workflow) below into ComfyUI.

2. Select the input webcam. Do not select "OBS Virtual Camera". This will be used as the output later.

![./img/select-input.jpg](./img/select-input.jpg)

3. Select `Run (Instant)` from the drop down.

![./img/run-instant.jpg](./img/run-instant.jpg)

4. To start, press the `(Run Instant)` button.

![./img/run-instant.jpg](./img/tap-again.jpg)

5. In your broadcasting or collaboration software, select `OBS Virtual Camera` as your webcam input.

![./img/select-obs.jpg](./img/select-obs.jpg)

6. To Stop, press the red square.

![./img/red-square.jpg](./img/red-square.jpg)

## Basic Workflow

```json
{
  "id": "00000000-0000-0000-0000-000000000000",
  "revision": 0,
  "last_node_id": 31,
  "last_link_id": 28,
  "nodes": [
    {
      "id": 8,
      "type": "VAEDecode",
      "pos": [1710, 130],
      "size": [140, 46],
      "flags": {},
      "order": 7,
      "mode": 0,
      "inputs": [
        {
          "name": "samples",
          "type": "LATENT",
          "link": 15
        },
        {
          "name": "vae",
          "type": "VAE",
          "link": 16
        }
      ],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [18]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.59",
        "Node name for S&R": "VAEDecode"
      }
    },
    {
      "id": 10,
      "type": "WebcamCapture",
      "pos": [100, 130],
      "size": [270, 184],
      "flags": {},
      "order": 0,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [21]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.59",
        "Node name for S&R": "WebcamCapture"
      },
      "widgets_values": ["", 480, 360, true, "capture"]
    },
    {
      "id": 13,
      "type": "PreviewImage",
      "pos": [2320, 130],
      "size": [140, 246],
      "flags": {},
      "order": 9,
      "mode": 0,
      "inputs": [
        {
          "name": "images",
          "type": "IMAGE",
          "link": 17
        }
      ],
      "outputs": [],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.59",
        "Node name for S&R": "PreviewImage"
      },
      "widgets_values": []
    },
    {
      "id": 18,
      "type": "VirtualCamNode",
      "pos": [1950, 130],
      "size": [270, 106],
      "flags": {},
      "order": 8,
      "mode": 0,
      "inputs": [
        {
          "name": "image",
          "type": "IMAGE",
          "link": 18
        }
      ],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [17]
        }
      ],
      "properties": {
        "aux_id": "Sean-Bradley/ComfyUI-Virtual-Webcam",
        "ver": "c7d05a91b8bc7695de2c0780066dd014cda5291d",
        "Node name for S&R": "VirtualCamNode"
      },
      "widgets_values": [30, true, false]
    },
    {
      "id": 25,
      "type": "CheckpointLoaderSimple",
      "pos": [100, 444],
      "size": [270, 98],
      "flags": {},
      "order": 1,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "MODEL",
          "type": "MODEL",
          "links": [19]
        },
        {
          "name": "CLIP",
          "type": "CLIP",
          "links": [20]
        },
        {
          "name": "VAE",
          "type": "VAE",
          "links": [16, 22]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.59",
        "Node name for S&R": "CheckpointLoaderSimple"
      },
      "widgets_values": ["v1-5-pruned-emaonly-fp16.safetensors"]
    },
    {
      "id": 26,
      "type": "LoraLoader",
      "pos": [470, 130],
      "size": [270, 126],
      "flags": {},
      "order": 2,
      "mode": 0,
      "inputs": [
        {
          "name": "model",
          "type": "MODEL",
          "link": 19
        },
        {
          "name": "clip",
          "type": "CLIP",
          "link": 20
        }
      ],
      "outputs": [
        {
          "name": "MODEL",
          "type": "MODEL",
          "links": [25]
        },
        {
          "name": "CLIP",
          "type": "CLIP",
          "links": [23, 24]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.59",
        "Node name for S&R": "LoraLoader"
      },
      "widgets_values": ["LCM_LoRA_SD15.safetensors", 1, 1]
    },
    {
      "id": 27,
      "type": "VAEEncode",
      "pos": [470, 386],
      "size": [140, 46],
      "flags": {},
      "order": 3,
      "mode": 0,
      "inputs": [
        {
          "name": "pixels",
          "type": "IMAGE",
          "link": 21
        },
        {
          "name": "vae",
          "type": "VAE",
          "link": 22
        }
      ],
      "outputs": [
        {
          "name": "LATENT",
          "type": "LATENT",
          "links": [28]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.59",
        "Node name for S&R": "VAEEncode"
      }
    },
    {
      "id": 29,
      "type": "CLIPTextEncode",
      "pos": [840, 130],
      "size": [400, 200],
      "flags": {},
      "order": 4,
      "mode": 0,
      "inputs": [
        {
          "name": "clip",
          "type": "CLIP",
          "link": 23
        }
      ],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [26]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.59",
        "Node name for S&R": "CLIPTextEncode"
      },
      "widgets_values": ["alien"]
    },
    {
      "id": 30,
      "type": "CLIPTextEncode",
      "pos": [840, 460],
      "size": [400, 200],
      "flags": {},
      "order": 5,
      "mode": 0,
      "inputs": [
        {
          "name": "clip",
          "type": "CLIP",
          "link": 24
        }
      ],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [27]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.59",
        "Node name for S&R": "CLIPTextEncode"
      },
      "widgets_values": ["text, watermark"]
    },
    {
      "id": 31,
      "type": "KSampler",
      "pos": [1340, 130],
      "size": [270, 474],
      "flags": {},
      "order": 6,
      "mode": 0,
      "inputs": [
        {
          "name": "model",
          "type": "MODEL",
          "link": 25
        },
        {
          "name": "positive",
          "type": "CONDITIONING",
          "link": 26
        },
        {
          "name": "negative",
          "type": "CONDITIONING",
          "link": 27
        },
        {
          "name": "latent_image",
          "type": "LATENT",
          "link": 28
        }
      ],
      "outputs": [
        {
          "name": "LATENT",
          "type": "LATENT",
          "links": [15]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.59",
        "Node name for S&R": "KSampler"
      },
      "widgets_values": [0, "randomize", 1, 1, "lcm", "sgm_uniform", 0.5]
    }
  ],
  "links": [
    [15, 31, 0, 8, 0, "LATENT"],
    [16, 25, 2, 8, 1, "VAE"],
    [17, 18, 0, 13, 0, "IMAGE"],
    [18, 8, 0, 18, 0, "IMAGE"],
    [19, 25, 0, 26, 0, "MODEL"],
    [20, 25, 1, 26, 1, "CLIP"],
    [21, 10, 0, 27, 0, "IMAGE"],
    [22, 25, 2, 27, 1, "VAE"],
    [23, 26, 1, 29, 0, "CLIP"],
    [24, 26, 1, 30, 0, "CLIP"],
    [25, 26, 0, 31, 0, "MODEL"],
    [26, 29, 0, 31, 1, "CONDITIONING"],
    [27, 30, 0, 31, 2, "CONDITIONING"],
    [28, 27, 0, 31, 3, "LATENT"]
  ],
  "groups": [],
  "config": {},
  "extra": {
    "ds": {
      "scale": 0.6670694864048369,
      "offset": [-6.43634656338393, -26.22164671866484]
    },
    "frontendVersion": "1.25.11",
    "VHS_latentpreview": false,
    "VHS_latentpreviewrate": 0,
    "VHS_MetadataImage": true,
    "VHS_KeepIntermediate": true
  },
  "version": 0.4
}
```
