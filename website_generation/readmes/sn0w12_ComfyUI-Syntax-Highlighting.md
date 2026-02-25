<h1 align="center">
    ComfyUI Syntax Highlighting
</h1>

Syntax highlighting and other quality of life improvements for ComfyUI.

## Features

-   Multiline textbox syntax highlighting.
    -   Weight highlighting.
    -   Lora highlighting.
        -   Incorrect lora highlighting.
    -   Embedding Highlighting.
        -   Incorrect embedding highlighting.
    -   Duplicate tag highlighting.
    -   Unclosed span highlighting.
-   Favorite combo values.
-   Preview images for combo values.

## Configuration

To get preview images, you have to put them in `../ComfyUI/custom_nodes/ComfyUI-Syntax-Highlighting/web/images`. The name of the image must match the name of the combo value exactly (except the file extension).

You can also use the `Save Preview Image` node to save a generated image to the correct location. 

To favorite the currently selected combo value, right click the node and click `favorite [name]`, if there are several combo inputs, it will be a submenu with all favorite options inside it.

## Settings

### Textbox

| Setting Name           | Type                     | Description                                                                                    |
| ---------------------- | ------------------------ | ---------------------------------------------------------------------------------------------- |
| Textbox Colors         | Multiline text           | A list of either rgb or hex colors, one color per line.                                        |
| Textbox Highlight Type | Combo (Strength/Nesting) | If strength, only the first and last colors will be used. If nesting, all colors will be used. |
| Tag Tooltips           | Boolean                  | When hovering over a tag in a textbox, show the tag's tooltip.                                 |

### Combo

| Setting Name          | Type         | Description                              |
| --------------------- | ------------ | ---------------------------------------- |
| Favorite On Top       | Boolean      | Put favorite items over all other items. |
| Combo Highlight Color | Color picker |                                          |

### Preview Image

| Setting Name              | Type               | Description                          |
| ------------------------- | ------------------ | ------------------------------------ |
| Preview Image Hover Delay | Slider (0-1000)    |                                      |
| Preview Image Padding     | Slider (0-100)     |                                      |
| Preview Image Side        | Combo (Left/Right) |                                      |
| Preview Image Size        | Slider (100-1000)  |                                      |
| Index Images              | Button             | Update images available for preview. |

## Examples

### Textbox Highlighting

![Textbox](https://i.imgur.com/UzYnqew.png)

### Favorite Combo Value

![Combo](https://i.imgur.com/nohMc2U.png)

### Preview Image

![Preview](https://i.imgur.com/DCrpAT8.png)
