# ComfyDeploy

<div>
  English / <a href="./README_zh.md">简体中文</a>
</div><br>

ComfyDeploy is a ComfyUI extension that allows you to deploy ComfyUI workflows as API services in conjunction with [comfy-deploy-admin](https://github.com/ihmily/comfy-deploy-admin), making them easily accessible from external applications.

## Features

- Deploy ComfyUI workflows as API endpoints
- Support for callback notifications
- Support for progress tracking

## Version Compatibility

- comfy-deploy v1.0.0: supports only ComfyUI v0.3.48–0.3.66
- comfy-deploy v1.0.1~: supports only ComfyUI v0.3.67 and above

## Installation

### Method 1: Using Git

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/ihmily/comfy-deploy.git
cd comfy-deploy
pip install -r requirements.txt
```

### Method 2: Using ComfyUI-Manager

1. Search for comfy-deploy and select the node by author ihmily
2. Click Install
3. Restart ComfyUI

## Complete System Architecture

The ComfyDeploy project system consists of two components:

1. **comfy-deploy node extension** (this project): Custom nodes installed in ComfyUI for creating deployable workflows.
2. **[comfy-deploy-admin](https://github.com/ihmily/comfy-deploy-admin)**: Management backend system for managing, debugging, and publishing API services.

These components work together to enable workflow creation, deployment, and management:
- The comfy-deploy node extension provides nodes and deployment functionality needed to create deployable workflows, exposing images, text, etc. as external inputs.
- comfy-deploy-admin provides a management interface for managing deployed workflows, debugging API interfaces, monitoring task execution, etc.

## Usage

### 1. Install comfy-deploy-admin

Follow the instructions in the [comfy-deploy-admin project](https://github.com/ihmily/comfy-deploy-admin) to install and configure the management backend:

```bash
git clone https://github.com/ihmily/comfy-deploy-admin.git
cd comfy-deploy-admin
# Follow the instructions in the project README to continue installation
```

### 2. Configure ComfyDeploy Nodes

In the ComfyUI interface, click the "ComfyDeploy" button in the top menu bar or the "Deploy" button in the left sidebar to configure the following settings:
- API Endpoint Address: Enter the service address of comfy-deploy-admin
- API Key: Enter the API key set in comfy-deploy-admin

### 3. Create a Workflow

1. Add ComfyDeploy nodes to your workflow:
   - External Text (ComfyDeploy)
   - External Integer (ComfyDeploy)
   - External Float (ComfyDeploy)
   - External Image (ComfyDeploy)

2. Set a parameter name (param_name) for each node, which will be used as the external API request parameter name.

### 4. Deploy the Workflow

1. Create and test your workflow.
2. Click the "Deploy" button to deploy the workflow as an API.
3. After successful deployment, check the corresponding workflow in the comfy-deploy-admin backend, debug and publish it.

## License

[MIT License](LICENSE)
