# Mureka API

A custom node for ComfyUI that provides access to the Mureka API for AI-powered music generation.  This project is not affiliated with Mureka in any way and any issues with their API should be [directed to their support channels](https://platform.mureka.ai/docs/en/faq.html).

&nbsp;
## Please Note

These custom nodes require a Mureka API key and will consume credits from your account when generating samples

### Getting Started
To use these custom nodes you must have an active Mureka API key, which you can get by signing up to the [Mureka API Platform](https://platform.mureka.ai/). Once you have [created an API key](https://platform.mureka.ai/apiKeys), you can use it to generate tracks directly in ComfyUI.

### Cost Disclaimer
- Each generation consumes credits from your Mureka account
- Generation costs vary by model
- Monitor your usage using the Mureka Billing node or your account dashboard
- Understand the cost overhead by reviewing the [Mureka API pricing documentation](https://platform.mureka.ai/pricing)
- No contributors to this project can be held responsible for any charges incurred through your API usage or the use of these nodes

### Security Notice
- Keep your API key private and never commit it to source control
- Don't share your API key with third parties
- Your API key is only used to call the Mureka API within this workflow
- No data is stored and your key is not saved or transmitted anywhere

### Cost Management Tips
- Use Mock Generation: Test your workflow with the Mock Generation node while building complex graphs
- Monitor usage: Check your account balance regularly with the Mureka Billing node or your account dashboard
- Check pricing: Review current pricing at [Mureka API pricing documentation](https://platform.mureka.ai/pricing) before generating

&nbsp;
## Installation

There are two ways to install this custom node:

### ComfyUI Manager (Recommended)

1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) if you don't have it yet.
2. Go to `Manager` > `Install Custom Nodes`.
3. Search for `Mureka API` and click `Install`.
4. Restart ComfyUI.

### Manual

1. Navigate to your `ComfyUI/custom_nodes/` directory.
2. Clone the repository: `git clone https://github.com/leewinder/comfyui-mureka-api.git`.
3. Restart ComfyUI.

&nbsp;
## Usage

The Mureka API custom nodes enables you to generate high-quality music using the Mureka API directly within your ComfyUI workflow. Simply provide a text prompt describing the music you want to create along with your API key, and the workflow will generate the audio tracks for you.

### Available Nodes

- **Mureka Instrumental**: Generate instrumental music from text prompts
- **Mureka Song**: Generate music and lyrics from text prompts
- **Mureka Text Prompt**: Create the music and lyric prompts
- **Mureka API Key**: Manage your Mureka API credentials
- **Mureka Billing**: Provide information about your account usage and available credit
- **Mureka Save**: Saves all generated audio files and the generation metadata to the ComfyUI Output folder
- **Mureka Decode Audio**: Process and decode generated audio files allowing them to be consumed by other AUDIO aware nodes
- **Mureka Mock Generation**: Test workflows using a previously generated sample set 

### Standard Workflow
The repo contains a couple of workflow files which shows how all the nodes work together
- [Generation Workflow](workflows/Mureka-Generation-Workflow.json) - linking up the Song and Instrumental generation nodes, saving content and checking your billing details
<img width="2383" height="971" alt="Screenshot 2025-10-24 at 07 34 39" src="https://github.com/user-attachments/assets/a29a7660-db50-4fcf-8759-9e48389e530f" />

&nbsp;
- [Mock Workflow](workflows/Mureka-Mock-Workflow.json) - using the Mock Generation node to emulate generation steps to build more complex workflows post generation
<img width="2383" height="971" alt="Screenshot 2025-10-24 at 07 35 05" src="https://github.com/user-attachments/assets/3a3fe614-d5f8-4575-958f-84a08a35966a" />

&nbsp;
&nbsp;

Alongside those workflows there are a few things worth noting
- **Mureka Instrumental** & **Mureka Song** do show progression, but it's simply an indicator that something is happening so it doesn't look like the graph has frozen as the API does not provide progression values during generation
- **Mureka Save** will save the audio files and the metadata properties attached to that generation.  This metadata JSON file is your link back to the generation run that created these audio samples, so it's highly recommend you save this metadata file alongside any samples you use publicly as a record that you created them
- **Mureka Decode Audio** is an additional step should you want to use future nodes that need an AUDIO object.  It's still recommend to use **Mureka Save** even if you need to modify the track and save it using a built in _Save Audio_ node, that way you still have access to the metadata file mentioned above
- **Mureka Mock Generation** needs a valid generation response to work correctly.  You can get one by running the **Mureka Instrumental** or **Mureka Song** result into a built-in _Preview Any_ node or copying the content of the generated metadata file from **Mureka Save** node
- **Mureka Billing** has a _*_ input simply allows you to link this node at any point in your graph, useful if you want one before and after the generation step.


&nbsp;
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or if you have any ideas or bugs, please [raise an issue](https://github.com/leewinder/comfyui-mureka-api/issues).  Theres still large parts of the Mureka API that are not supprted yet, so there's always additional features needed.

### Contribution Workflow
1. Fork this repository
2. Make your changes
3. Test your changes
4. Run quality checks
5. Create a Pull Request

### Development Setup

#### Prerequisites

- python 3.11+
- pytest 8.0+
- pylint 3.0+

#### Setting Up Your Development Environment

1. Install pyenv:
```bash
# macOS
brew install pyenv

# Or follow the official installation guide:
# https://github.com/pyenv/pyenv#installation
```

2. Clone the repository:
```bash
git clone git@github.com:leewinder/comfyui-mureka-api.git
cd comfyui-mureka-api
```

3. Set up Python environment:
```bash
# Create the virtual environment
bash scripts/install.sh
source venv/bin/activate
```

4. Create authentication.json in the root:
```json
{
    "mureka": "<your Mureka API key>"
}
```

#### Running Tests
```bash
# Run all tests
pytest test/ -v
```

#### Code Quality
```bash
# Run pylint for code quality checks
pylint src/ test/ --fail-under=8.0
```

&nbsp;
## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International](LICENSE) license.

&nbsp;
## Contributors

- [@leewinder](https://github.com/leewinder)
