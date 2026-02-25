# MovieLabs ComfyUI Nodes for Publishing Workflow

This project implements two custom nodes for the ComfyUI to enable the publishing of assets to the filesystem and ShotGrid:

1. PublishAsset: This node publishes an asset to the filesystem and ShotGrid.
2. PublishBlender: This node publishes a Blender file to the filesystem.

An extensive set of validation checks, automatic version numbering, automatic directory creation, and naming conventions are implemented to meet the production requirements and to ensure that the file system is kept in sync with ShotGrid.

## Important Notes

The PublishAsset node ensures that the file system is kept in sync with ShotGrid. This means there cannot be "Versions" in ShotGrid that are not present in the file system, and vice versa.

If that happens, the PublishAsset node will fail to publish the asset to ShotGrid, although the asset will be written to the file system.

<b>The file system is considered the source of truth.</b>

## Publish Asset Node

### How to use

The Publish Asset node is designed to be used in the following way:

1. Select the artist login to authenticate with ShotGrid.
2. Select the shot code to publish the asset for.
3. Select the task to publish the asset for.
4. Specify the path of the original file to publish. 
- This is the asset file that is written to the file system (and sometimes to ShotGrid). For example, AI generated images and videos are published to ShotGrid even though they are the original assets. In almost all other cases, only the proxy file is published to ShotGrid and the original file is written to the file system.
- In the case of EXR files, it is sufficient to specify just one EXR file. The node will automatically find all the other EXR files in the same directory and publish them as well.
5. Specify the path of the proxy file to publish. This is the file that is published to ShotGrid usually as explained above. It is optional for some tasks.
6. Specify any notes to add to the version in ShotGrid.
7. Execute (i.e, queue) the prompt. 

The node will publish the asset to ShotGrid and write the original file to the file system, after performing a variety of checks and following the naming conventions.

#### Validation Checks

1. Artist login: By default, a blank artist login is selected. This will make the artist specifically select their login (as opposed to using the default login).
2. Shot code: The shot code list is populated from ShotGrid. So bogus shot codes will not be presented at all.
3. Task: The selected task must exist for the selected shot code. Otherwise, the node will fail.
4. Original file: A variety of checks are performed here.
- The specified file is verified to exist. 
- The file extension must match the expectation for the selected task. For example, a PNG file cannot be specified for Generate Blender Ref task, which expects an EXR file.
- If it is a task that expects EXR files, the node will check if the file is an EXR file. If it is, it will check if the file is part of a sequence of EXR files. If it is, the node will check if the sequence is consecutive. If it is not, the node will fail.
5. Proxy file: For tasks that expect a proxy file, the node will check if the specified file is a valid proxy file (based on the file extension).
6. Version number: The node will automatically determine the next version number for the selected task based on existing versions in the file system.
7. Automatic directory creation: The node will automatically create the necessary directories in the file system based on the selected task and the shot code.

#### Naming Conventions

The naming conventions are defined in the `config.json` file.


## TODO
Lensing task and Upres task are not yet defined by the team. Once they are defined, the implementation of the Publish Asset node will need to be updated.


## Publish Blender Node

### How to use

The Publish Blender node is designed to be used in the following way:

1. Select the shot code to publish the blender file for.
2. Select the blender file to publish.
3. Execute (i.e, queue) the prompt.

The node will publish the blender file to the file system, after performing a variety of checks and following the naming conventions.

#### Validation Checks

1. Shot code: The shot code list is populated from ShotGrid. So bogus shot codes will not be presented at all.
2. Blender file: The specified file is verified to exist.
3. Version number: The node will automatically determine the next version number based on existing versions in the file system.
4. Automatic directory creation: The node will automatically create the necessary directories in the file system based on the selected task and the shot code.

#### Naming Conventions

The naming conventions are defined in the `config.json` file.
