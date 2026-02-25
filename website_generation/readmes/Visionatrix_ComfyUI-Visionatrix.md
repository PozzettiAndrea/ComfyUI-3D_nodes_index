# ComfyUI-Visionatrix

The ComfyUI-Visionatrix nodes are designed for convenient ComfyUI to [Visionatrix](https://github.com/Visionatrix/Visionatrix) workflow support migration, in particular to extract prompt input params (input, textarea, checkbox, select, range, file) to be used in simplified Visionatrix UI.

Short migration steps guide in [Visionatrix docs](https://visionatrix.github.io/VixFlowsDocs/).

## Nodes list

Current `Visionatrix/UI` nodes list:

- **VixUI-Checkbox** - simple checkbox boolean input field;
- **VixUi-RangeFloat** - range float number input, e.g. for prompt strength selection;
- **VixUi-RangeScaleFloat** - special range float number input, to define the scale factor of the input image (e.g. for upscale)
- **VixUi-RangeInt** - range int number input, e.g. for number of steps selection;
- **VixUi-List** - define list of options to be displayed in Visionatrix UI;
- **VixUI-Prompt** - to define a textarea input in Visionatrix UI and pass it to your CLIPTextEncode node with prompt;
- **VixUi-CheckboxLogic** - to define the boolean logical switch (checkbox), e.g. two modes and paths of workflow execution;
- **VixUi-ListLogic** - to define the list of available mode options similar to `VixUi-CheckboxLogic` (up to 6 input options);
- **VixUi-WorkflowMetadata** - mandatory node to fill the workflow metadata required for each Visionatrix flow for displaying in the UI list of workflows;
- **VixUiAspectRatioSelector** - use it to display the desired image aspect ratio for your Flow.

Current `Visionatrix/Text` nodes list:

- **VixDictionaryNew** - create a dictionary with up to 9 keys.
- **VixDictionaryConvert** - node to create dictionary from text.
- **VixDictionaryGet** - node to get value by key from dictionary.
- **VixDictionaryUpdate** - update one dictionary with values from another dictionary.

Current `Visionatrix/Image` nodes list:

- **VixImageFilters** - applies brightness, saturation, sharpness and other simple Pillow filters to an image.

### Incorporated nodes

- **StyleAlignedBatchAlign** - from the `style_aligned_comfy` repository
