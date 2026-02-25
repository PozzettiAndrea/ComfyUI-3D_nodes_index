# ComfyUI-Liebs-Toast

A node to display a toast notification. Use it to send a toast when your prompt is complete. Also pairs well with [ComfyUI-Liebs-Picker](https://github.com/marklieberman/ComfyUI-Liebs-Picker) and [cg-image-filter](https://github.com/chrisgoringe/cg-image-filter) to be notified when the picker is waiting.

## Features

* Display a toast notification.
* Customize the toast message, duration, and/or silence the notification audio.
* Setting to skip the toast if the browser tab is already visible.

> [!IMPORTANT]
> The companion browser add-on is required to support the following functionality:

* **View Workflow** button in the toast will bring focus to the browser tab that sent the toast.
* Center the view on self or another node when the **View Workflow** button is clicked.

### Screenshots

| Screenshot | Description |
| :---- | :---- |
| <img src="./docs/images/workflow.png" width="500"/> | An example workflow with two toasts. The first toast is triggered when the image batch from the VAE Decode is available. It is used to get your attention for the image picker node. The second toast is triggered after the SD Ultimate Upscae is complete, and announces that the prompt is finished. |
| <img src="./docs/images/toast.png" width="500"/> | A toast on Windows. The **View Workflow** button is displayed when the companion browser add-on is installed. |

### Center On Node
`center_on_node` will find a node with the given title and center the graph over it when the **View Workflow** button is clicked. You can optionally set the zoom level by appending a pipe | and zoom factor.

| Example | Result |
| :---- | :---- |
| `none`, `off`, or empty | Disables the center on node function. |
| `Preview Image` | Center the graph over the node with the title "Preview Image". |
| `Preview Image\|1.4` | Center the graph over the node with title "Preview Image" and set the zoom level to 1.4. |

## Browser Add-on

The browser add-on allows the Python node to activate the browser tab when you click the **View Workflow** button in the toast. The button will not appear in the toast if the add-on is not installed.

### Installation

Install the add-on from your browser's add-on store.

* Chrome: not available yet.
* Edge: [https://microsoftedge.microsoft.com/addons/detail/comfyuiliebstoast/ighbjmihnndalcclfflgogbjemkkflbe](https://microsoftedge.microsoft.com/addons/detail/comfyuiliebstoast/ighbjmihnndalcclfflgogbjemkkflbe)
* Firefox: [https://addons.mozilla.org/en-US/firefox/addon/comfyui-liebs-toast/](https://addons.mozilla.org/en-US/firefox/addon/comfyui-liebs-toast/)

### Permissions

By default the add-on will only request permission to run on `http://127.0.0.1/*` and `http://localhost/*`. You must request additional permissions in the add-on's options to run the add-on on other domains.

## Limitations

* Currently only Windows is supported. Help to implement support for additional platforms would be appreciated.
