# About

[ntfy](https://ntfy.sh/) is a simple HTTP-based pub-sub notification service. This repo adds 2 nodes to make ntfy notifications simple in ComfyUI. Supports sending a simple text based notification, or the generated image as an attachment to a topic.

# Install

## Comfy-CLI

```
comfy node registry-install comfyui-ntfy
```

For more info, see [here](https://docs.comfy.org/comfy-cli/getting-started)

## Manual

cd into custom_nodes directory

```
cd YOUR_PATH/ComfyUI/custom_nodes
```

clone repo with shallow copy

```
git clone --depth 1 -b master https://github.com/boredofnames/ComfyUI-ntfy.git
```

or download ntfy.py and place into custom_nodes directory.

# Update

cd into ComfyUi-ntfy directory

```
cd YOUR_PATH/ComfyUI/custom_nodes/ComfyUI-ntfy
```

pull from repo

```
git pull origin master
```

or download ntfy.py and replace in custom_nodes directory.

# Nodes

See [Wiki](https://github.com/boredofnames/ComfyUI-ntfy/wiki) for node documentation.

# Contributing

Feel free to send in a PR, and it will eventually be seen.
