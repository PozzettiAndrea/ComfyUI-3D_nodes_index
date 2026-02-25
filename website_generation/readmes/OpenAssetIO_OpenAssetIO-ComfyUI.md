# OpenAssetIO-ComfyUI

## What

Custom [ComfyUI](https://comfy.org) nodes for resolving and publishing
assets directly from a workflow via
[OpenAssetIO](https://docs.openassetio.org/OpenAssetIO/).

## Why

This project allows ComfyUI to leverage the abilities of
OpenAssetIO-enabled asset management systems, such as versioning,
dependency tracking, and collaboration.

For example, if the asset manager supports a meta-version of "latest",
then the workflow inputs can be updated without having to edit the
workflow or move files around.

Then, when the workflow completes, the output can be published back to
the asset manager, which typically creates a new version/revision
(rather than overwriting), and makes the output available for review and
for use by downstream tools.

## Features

- _OpenAssetIO Resolve Image_: An alternative to the built-in
  _Load Image_ node that resolves an OpenAssetIO entity reference to an
  image.

- _OpenAssetIO Publish Image_: An alternative to the built-in _Save
  Image_ node that publishes the output of a workflow to an OpenAssetIO
  entity reference.

## Requirements

The plugin is known to work with

- Python 3.11
- [ComfyUI](https://comfy.org) 0.3.57
- [OpenAssetIO](https://github.com/OpenAssetIO/OpenAssetIO) 1.0.0
- [OpenAssetIO-MediaCreation](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation)
  1.0.0-alpha.12

## Installation

Install [ComfyUI](https://docs.comfy.org/get_started).

Clone this repository under `ComfyUI/custom_nodes`.

From the repository root, install dependencies

```
pip install -r requirements.txt
```

Ensure the ComfyUI execution environment is configured correctly for an
OpenAssetIO host application. See the
[OpenAssetIO documentation](https://docs.openassetio.org/OpenAssetIO/runtime_configuration.html)
for general instructions on host application configuration.

In particular, ensure the `OPENASSETIO_DEFAULT_CONFIG` environment
variable contains a path to a valid OpenAssetIO configuration file.

## Development

To install the dev dependencies and pre-commit (will run the
[Ruff](https://docs.astral.sh/ruff/) hook), from the repository root run

```bash
pip install -e .[dev]
pre-commit install
```

> Note that installing this project to the Python environment has no
> effect on ComfyUI, since it loads plugins from the `custom_nodes`
> directory. However, installing the package helps with IDE code
> completion and linting; and of course ensures test/lint dependencies
> are installed.

### Running Tests

This project contains unit tests written in
[pytest](https://docs.pytest.org/en/stable/) in the `tests` directory.
To run the tests, from the repository root run

```bash
pytest tests
```

### Linting

The project makes use of the [Ruff](https://docs.astral.sh/ruff/)
linter, configured through the `pyproject.toml` file. To run Ruff, from
the repository root run

```bash
ruff check .
```

## License

Apache-2.0 - See [LICENSE](./LICENSE) file for details.

## Contributing

Please feel free to contribute pull requests or issues. Note that
contributions will require signing a CLA.

See the OpenAssetIO contribution docs for how to structure
[commit messages](https://github.com/OpenAssetIO/OpenAssetIO/blob/main/doc/contributing/COMMITS.md),
the [pull request process](https://github.com/OpenAssetIO/OpenAssetIO/blob/main/doc/contributing/PULL_REQUESTS.md),
and [coding style guide](https://github.com/OpenAssetIO/OpenAssetIO/blob/main/doc/contributing/CODING_STYLE.md).
