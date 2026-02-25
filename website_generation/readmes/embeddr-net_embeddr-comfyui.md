<div align="center"><a name="readme-top"></a>

<img height="120" src="https://embeddr.net/embeddr_logo_transparent.png">

<h1>Embeddr ComfyUI Extension</h1>
</div>

> [!WARNING]
> Requires [embeddr-cli](https://github.com/embeddr-net/embeddr-cli) to be running.

![Example](.github/assets/example_1.webp)

## Installation

1. Download [latest release](https://github.com/embeddr-net/embeddr-comfyui/releases)
2. Extract into `comfyui/custom_nodes`
3. [Install Embeddr-CLI](https://github.com/embeddr-net/embeddr-cli?tab=readme-ov-file#installation)
4. Run Embeddr-CLI with `embeddr serve`
5. Run ComfyUI


## Usage


### Use New Load & Save Image

![Example IO](.github/assets/io_nodes.png)

![Example](.github/assets/example_2.png)

### Retrieve from your collections

![Example Retrieval](.github/assets/retrieval_nodes.png)


### Access more info on the [WebUI](https://github.com/embeddr-net/embeddr-cli) 

![Example Lineage](.github/assets/lineage_large.png)

## Development

To get a development version working.

```sh
git clone https://github.com/embeddr-net/embeddr-comfyui
cd embeddr-comfyui
pnpm install
pnpm build

# Link into ComfyUI custom_nodes
# Example:
ln -s /home/user/git/embeddr-comfyui \
    /home/user/comfyui-dev/custom_nodes/embeddr-comfyui
```
