# ComfyUI_SD3_Flowedit
ComfyUI nodes that support SD3/SD3.5 in FlowEdit
# Start
This is an implementation of image editing using [Flowedit](https://github.com/fallenshock/FlowEdit).

It constructs an ODE (Ordinary Differential Equation) that directly maps between the source and target distributions.

You can use the official pre-trained SD3/SD3.5 models for image mapping. Additionally, you can fine-tune the SD3/SD3.5 models based on your specific needs to learn new distributions for image mapping.

Follow this [workflow](example_workflows/example_SD3_SD3.5_Flowedit.json) to get started.

To use ComfyUI nodes that support Flux in FlowEdit, refer to [ComfyUI-Fluxtapoz](https://github.com/logtd/ComfyUI-Fluxtapoz). This project's code is based on modifications of ComfyUI-Fluxtapoz.

![lighthouse](https://github.com/user-attachments/assets/711c3477-150b-44d8-9644-f68c1616af2c)

# Acknowledgements

```
@article{kulikov2024flowedit,
    title = {FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models},
    author = {Kulikov, Vladimir and Kleiner, Matan and Huberman-Spiegelglas, Inbar and Michaeli, Tomer},
    journal = {arXiv preprint arXiv:2412.08629},
    year = {2024}
}
```  


