# gadzoinks_ComfyUI
gadzoinks custom node for ComfyUI


Gadzoinks is a iPhone App for managing and sharing AI Images, with this node you can upload your images directly to Gadzoinks cloud. You can also find an image you like in the app and use the link control to create a worksheet to build the image.

https://apps.apple.com/us/app/gadzoinks-com/id6476454277

In the App you will create an account (or subaccount) with a handle (username) and authkey. Use Settings->Gadzoinks in comfyui to set your handle and authkey

Then add the Gadzoinks node to your workflow, the same as you would add 'Save Image' node (you can use both to save locally and to gadzoinks cloud).

Node Options

upload image - if false don't upload . useful if you are just playing around
private storage - your image will only be visible to you.

age - we ask that you rate your image 4,12,17 (G,PG,R)

set_name - (optional) sets are used to organize a batch of images that are created together. In the app you can easily view just a set, mark the ones to keep and remove the rest with a click.

