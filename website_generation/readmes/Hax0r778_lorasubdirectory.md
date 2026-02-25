# lorasubdirectory

Only show dropdown of loras in a a specified subdirectory

> [!NOTE]
> This projected was created with a [cookiecutter](https://github.com/Comfy-Org/cookiecutter-comfy-extension) template. It helps you start writing custom nodes without worrying about the Python setup.

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
1. Look up this extension in ComfyUI-Manager. If you are installing manually, clone this repository under `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

# Features

- Allows the Lora subdirectory to be specified in a separate dropdown from the Lora itself making it easier and faster to find the Lora you are looking for without needing to scroll through a long list or search.  

The tool appears like the standard Lora Loader but with an extra field
![node screenshot](https://github.com/Hax0r778/lorasubdirectory/blob/main/screenshot_1.png?raw=true)

The first dropdown will contain a sorted list of all Lora subdirectories within your main Lora directory which have at least one lora file in them.
![subdirectory dropdown screenshot](https://github.com/Hax0r778/lorasubdirectory/blob/main/screenshot_2.png?raw=true)

Once the first dropdown is specified, the second dropdown will then show only the Loras from that specific subdirectory making them easier to find. 
![lora dropdown screenshot](https://github.com/Hax0r778/lorasubdirectory/blob/main/screenshot_3.png?raw=true)

In theory this same technique could apply at multiple levels to allow further filtering of the subdirectories themselves, but that would require a separate node type altogether so I'm not prioritizing it. 

One remaining downside is that the subdirectory can not be specified as a string as that is not compatible with the ComfyUI array type needed to populate the dropdown list. 

## Develop

To install the dev dependencies and pre-commit (will run the ruff hook), do:

```bash
cd lorasubdirectory
pip install -e .[dev]
pre-commit install
```

The `-e` flag above will result in a "live" install, in the sense that any changes you make to your node extension will automatically be picked up the next time you run ComfyUI.

## Writing custom nodes

An example custom node is located in [node.py](src/lorasubdirectory/nodes.py). To learn more, read the [docs](https://docs.comfy.org/essentials/custom_node_overview).


## Tests

This repo contains unit tests written in Pytest in the `tests/` directory. It is recommended to unit test your custom node.

- [build-pipeline.yml](.github/workflows/build-pipeline.yml) will run pytest and linter on any open PRs
- [validate.yml](.github/workflows/validate.yml) will run [node-diff](https://github.com/Comfy-Org/node-diff) to check for breaking changes

## Publishing to Registry

If you wish to share this custom node with others in the community, you can publish it to the registry. We've already auto-populated some fields in `pyproject.toml` under `tool.comfy`, but please double-check that they are correct.

You need to make an account on https://registry.comfy.org and create an API key token.

- [ ] Go to the [registry](https://registry.comfy.org). Login and create a publisher id (everything after the `@` sign on your registry profile). 
- [ ] Add the publisher id into the pyproject.toml file.
- [ ] Create an api key on the Registry for publishing from Github. [Instructions](https://docs.comfy.org/registry/publishing#create-an-api-key-for-publishing).
- [ ] Add it to your Github Repository Secrets as `REGISTRY_ACCESS_TOKEN`.

A Github action will run on every git push. You can also run the Github action manually. Full instructions [here](https://docs.comfy.org/registry/publishing). Join our [discord](https://discord.com/invite/comfyorg) if you have any questions!

