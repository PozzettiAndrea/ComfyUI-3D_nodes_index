# ⚡ ComfyUI Connect

Expose your workflows into HTTP endpoints directly from ComfyUI itself.

**Key features :**

- **✨ Plug and play** - Automatically serve your ComfyUI workflows into `/api/connect/workflows/*` endpoints
- **📖 Auto Documentation** - Show all your workflows in OpenAPI format using `/api/connect` internal endpoint
- **🏷️ Easy** - Add tag in you nodes names for referencing inputs `$my-node` and outputs `#my-result`
- **⚡ Fast** - No added overload, powerful node caching.
- **🔀 [Load Balancer](https://github.com/Good-Dream-Studio/comfy-connect-gateway)** - Clusterize and monitor your ComfyUI instances with the Gateway.

## Installation

Install by cloning this project into your `custom_nodes` folder.

```sh
cd custom_nodes
git clone https://github.com/Good-Dream-Studio/ComfyUI-Connect
```

## Quick Start

1. Annotate editable inputs, for example rename the `KSampler` by `KSampler $sampler`

2. Annotate your output, for example `Preview Image` into `Preview Image #output`

3. Click on `Workflow > Save API Endpoint` and type your endpoint name.

4. You can now go to the openapi documentation at http://localhost:8188/api/connect to run your workflow with a json payload like :

    ```json
    {
      "sampler": {
        "seed": 1234
      }
    }
    ```

5. Handle the API response by your client, in our example we have annotated one out `#output` :

    ```json
    {
      "output": "V2VsY29tZSB0byA8Yj5iYXNlNjQuZ3VydTwvYj4h..."
    }
    ```

> Multiple values: If you annotate multiple nodes with the same annotation name (`#output` in our example), the json output will contain an array of values instead of a single value.

## Annotations Documentation

### Input Annotations

Annotate nodes to expose inputs to be updated by a payload when calling the workflow.

- `$foo`: Allow update of all inputs for this node under the "foo" name.
- `$foo(bar1,bar2)`: Same as above, but only with the listed inputs.
- `$foo()`: Deny all input modification, but allow node actions (like bypassing).

### Output Annotations

Annotate nodes to retrieve their result into base64 encoded as array in the response.

- `#foo`: Return the result in base64 array.

### Internal Annotations

- `!bypass`: Bypass this node when running from API (but keep it in ComfyUI).
  - Usefull if you want to remove debug nodes from the workflow when running from API.
- `!cache`: Globally register this node to be included on each API call.
  - It allows you to keep the node in memory, denying ComfyUI to unload it. See **How to cache models**.

## Payload Documentation

Each annotated node exposing inputs can be changed by a payload where `<node-name>.<input-name> = <value>`.

Simple primitive values :

```json
{
  "my-sampler": {
    "seed": 1234,
    "steps": 20,
    "cfg": 7
  },
  "my-positive-prompt": {
    "text": "beautiful scenery nature glass bottle landscape, , purple galaxy bottle,"
  }
}
```

Uploading images (from base64, from url) :

```json
{
  "load-image-node": {
    "image": {
      "type": "file",
      "url": "https://foo.bar/image.png",
      "name": "optional_name.png"
    }
  },
  "load-image-node-2": {
    "image": {
      "type": "file",
      "content": "V2VsY29tZSB0byA8Yj5iYXNlNjQuZ3VydTwvYj4h ...",
      "name": "required_name.jpg",
    }
  }
}
```

> Images will be cached and not downloaded/rewritten if the filename already exists.

You can also bypass node by passing the `false` value instead of an object, it will bypass it like the `!bypass` annotation :

```json
{
  "my-node-to-bypass": false
}
```

## How to cache models

Imagine you have two workflows `a.json` and `b.json`, each loading a different model (two different `Load Checkpoint` nodes loading `dreamshaper.safetensors` and `juggernaut.safetensors`).

Running `a.json` will :

- Load `dreamshaper.safetensors` into VRAM
- Execute the rest ...

Then, running `b.json` will :

- Unload `dreamshaper.safetensors` from VRAM
- Load `juggernaut.safetensors` into VRAM
- Execute the rest ...

Finally, running `a.json` again will :

- Unload `juggernaut.safetensors` from VRAM
- Load `dreamshaper.safetensors` into VRAM
- Execute the rest ...

By putting `!cache` annotation on both `Load Checkpoint` workflows you will instruct ComfyUI to **force them to stay in memory** reducing loading times (but increasing VRAM usage).

Now, running `a.json` will :

- Load `dreamshaper.safetensors` into VRAM
- Load `juggernaut.safetensors` into VRAM
- Execute the rest ...

Then, running `b.json` will :

- Execute the rest ...

Then, running `a.json` will :

- Execute the rest ...

> **Note :** Caching is not limited to `Load Checkpoint`. Each node keeping stuff in memory like models will benefit from caching. For example : `Load ControlNet Model`, `SAM2ModelLoader`, `Load Upscale Model`, etc ...

## TODO

- [] Retrieve all default values from the workflow to fill openapi documentation values
- [] Find a way to hook the save event, for replacing the "Save API Endpoint" step for updating workflows
- [] Editable configuration (from the ComfyUI config interface ?)
- [] Test edge cases like image batches, complex workflows ...
- [] Output as download url instead of base64 option, for bigger files

## Why This ?

ComfyUI ecosystem is actually working to solve the deployment and scalability approach when it comes to run ComfyUI Workflows, but ...

**1. Pusing workflows into clouds** ([ComfyDeploy](https://comfydeploy.com/), [RunComfy](https://www.runcomfy.com/), [Replicate](https://replicate.com/), [RunPod](https://www.runpod.io/) etc ...) **can have insane speed issues, violent pricing, and features limitations**

- Simple workflows of 5s can take 15s, 30s and up to minutes due to cold start and the provider queue system overload.
- In managed cloud it can be faster without cold start, but you are limited to available models, custom nodes, etc ...

**2. In-house JSON workflows management is complicated**

- Painful json file versionning, and it is time consuming to sync each time you do a modification.
- I can be a challenge to edit workflows on the fly by your app (specially for bypassing nodes etc ...)

**So, Here is my solution:**

A [ComfyUI-Connect](https://github.com/Good-Dream-Studio/ComfyUI-Connect) plugin to convert ComfyUI into a REST API, and a separate [NodeJS Gateway](https://github.com/Good-Dream-Studio/gateway-connect) server to handle them in a load balanced cluster.

---

Made with ❤️ by Ifnot.
