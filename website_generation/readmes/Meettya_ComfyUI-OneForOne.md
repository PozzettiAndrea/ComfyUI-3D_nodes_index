# ComfyUi OneForOne

## Image Fit Calculator

<img src="https://github.com/Meettya/ComfyUI-OneForOne-Demo/blob/b1f3ffa041d9b1f615553bb29ea2f74ded8b3b8b/examples/fit_calculator_node.jpg?raw=true" alt="Image Fit Calculator node" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

<br/>

The ComfyUI custom node **Image Fit Calculator** is designed to automatically calculate new image parameters based on a given latent and original image. Specifically, this node can perform calculations for resizing an image and provide data for paddings to control its placement within the latent space. Additionally, it includes settings that allow users to specify horizontal or vertical offsets as well as reduce the size of the image. This node performs only computational tasks, while actual operations on the image may be carried out by external nodes if they have the capability to use input data to manipulate the result.

<img src="https://github.com/Meettya/ComfyUI-OneForOne-Demo/blob/b1f3ffa041d9b1f615553bb29ea2f74ded8b3b8b/examples/fit_calculator.jpg?raw=true" alt="Image Fit Calculator example" style="display: block; margin-left: auto; margin-right: auto;">

In the provided workflow example, one can see how the ComfyUI node integrates with other components to streamline the process of image manipulation. This modular approach ensures flexibility and extensibility, enabling developers to easily incorporate new functionalities or optimize existing ones.

![Demo Animation](https://github.com/Meettya/ComfyUI-OneForOne-Demo/blob/0316b0b971aec47c097bf4389b16c213e6591038/examples/Fitcalcutator.gif?raw=true)

If you encounter any bugs or have ideas for improving the ComfyUI node, feel free to create an issue or submit a pull request. Your contributions are highly appreciated and will help enhance this powerful tool for image processing automation.

