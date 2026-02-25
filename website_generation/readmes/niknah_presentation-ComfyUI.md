
This custom node turns a ComfyUI workflow into a normal website(nuxt / vue).
Turns a normal workflow into a simplier interface like A1111, forge, etc.

You can...
* Restrict which nodes the user has access to
* Allow mutiple user logins
* Accept payments

![Example](images/PresentationExample800.png)

## Install

(Install nodejs)[https://nodejs.org/en/download]

After installing the custom node.  On the first run, it'll install the nuxt web site into `output/presentation-site` which will take a few minutes.

## To use

* Get any workflow.
* Add a group.
* Put "PresentationTab" into that group.  
* Give it a name.
* Put into that group the nodes that you want the user to be able to use.
* If you only want the user access some of the inputs in a node, not all.  Use Primitive Int/String, string(multiline), Presentation Seed, Presentation Drop Down, Presentation File.  Connect it to the node and put them in the group.
* For output, use these nodes:  PreviewImage, PreviewAudio, VHS\_VideoCombine, SaveVideo, SaveImage, SaveAudio
* Click "save" on the "PresentationTab" node.
* Visit (http://[::1]:3000/)[http://[::1]:3000/]

(Video instructions)[https://youtu.be/M6HKBr5D-4s]

## How to use the nodes

|--|--|
| [Presentation File](https://youtu.be/XBlm1r7-xRY) | Used to pick models, loras, etc. |
| [Presentation Advanced](https://youtu.be/6CXKYp5A5YE) | Split the rest of the page into an advanced section. |
| [Presentation Audio / Video / Image](https://youtu.be/7hmaufjpKR0) | Load media |
| Presentation Drop down | A fixed selection.  Can be used in place of the Presentation File node when you only want people to select from a pre-defined range. |
| Presentation History | Queue History.  You can remove the normal history from MainPage.vue |
| Presentation Progress | Progress bar.  You can remove the normal progress bar from MainPage.vue |
| Presentation Add Queue | The queue button |
| Presentation Component | Add your own custom component |


## To style

Change the CSS style files...
`assets/css/Style.css`
`assets/css/Style.mobile.css`


## To remove a tab

Remove the folder & file `output/presentation-site/components/tabs/xxx/`
`output/presentation-site/components/tabs/xxx.vue`

In ComfyUI go to settings -> presentation -> rebuild


## Security

In the file `output/presentation-site/components/tabs/<tabname>/workflow.json`
There is `workflowIds`.  The server will only modify these node IDs.  These are the nodes inside the same group as `PresentationTab` in ComfyUI. If you add things to the UI that refers to other nodes, you have to add them here.


## Nodes...

You can plug this into most things that reads a file, models, loras, load image / audio / etc.

* In multi user mode, each users' files are stored in  `ComfyUI/output/username`
* The path should start with something like `input, output, checkpoints, loras, vae, text_encoders, diffusion_models, clip_vision, diffusers, upscale_models`.  Defined in ComfyUI/folder\_paths.py


## .env

### These settings are needed in the .env file for user logins.

| Name | Description |
| NUXT\_SESSION\_PASSWORD | Make a random string for this, at least 32 characters. Used by nuxt-auth-utils |
| GUEST\_ACCOUNT | The name of the guest account when no one is logged in "guest_account" |
| MONGODB\_URL | If you want multiple users, this is required. Can be a local db, or [Mongodb.com have a free teir](https://www.mongodb.com/pricing).  Example: mongodb+srv://username:password@yourcluster.mongodb.net |
| NUXT\_OAUTH\_GOOGLE\_CLIENT\_ID | For [Google auth logins](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid#get_your_google_api_client_id) |
| NUXT\_OAUTH\_GOOGLE\_CLIENT\_SECRET | Client secret for Google auth logins |
| NUXT\_OAUTH\_FACEBOOK\_CLIENT\_ID | For [facebook logins](https://help.vtex.com/tutorial/adding-a-client-id-and-a-client-secret-to-log-in-with-facebook--3R7rzXWG1GswWOIkYyy8SO) |
| NUXT\_OAUTH\_FACEBOOK\_CLIENT\_SECRET | Secret for facebook logins |

### Payments setup.  You will need user logins setup first before you can accept payments.

| Name | Description |
| STRIPE\_SECRET\_KEY | To accept payments.  Get an [API key](https://docs.stripe.com/keys) from Stripe  |
| STRIPE\_PUBLIC\_KEY |  |
| STRIPE\_WEBHOOK\_SECRET\_KEY | endpoint is https://YourWebSite/api/payment/stripeConfirm |


### Security.

If your website is in a different location to your ComfyUI

| Name | Description |
| -- | -- |
| COMFYUI\_USERNAME | ComfyUI Basic auth user name if you're using the [Basic auth custom node](https://github.com/fofr/comfyui-basic-auth) |
| COMFYUI\_PASSWORD | ComfyUI Basic auth password |
| COMFYUI\_URL | Where you have installed ComfyUI.  default: http://127.0.0.1:8188 |


## Debug

If anything goes wrong, in ComfyUI settings &#9654; presentation &#9654; restart button.

Also check that there aren't multiple node / nuxt process running on the same folder.  Terminate them if needed.

If you are restarting a lot.  The shortcut to the restart button is...
(http://localhost:8188/custom\_nodes/presentation-ComfyUI/restart)[http://localhost:8188/custom\_nodes/presentation-ComfyUI/restart]


# Public site

You can make your home computer's website accessible from the outside world via Cloudflare (Video Instructions)[https://youtu.be/KNeg4z9DhdY]

If you make a public site, tell me about it.  There can be a directory later on.
https://forms.gle/oqSXN4S1DAXU4ES79


# User Login

You will need to add `GUEST_ACCOUNT=guest_account` for users who have not logged in.  The files available to the guest account will be in `outputs/guest_account`.

Then add the client id + secret key to allow logins.


# Payments

Your site has to be public & allow user logins to receive payments.

(Video Instructions)[https://youtu.be/QVol1DW0WYI]


Supports Stripe.  Add the `STRIPE\_...` (environment variables)[#-env].
Restart.  The payment link is `https://YourWebSite/stripe?amount=3000`
`amount=` is in cents.

Stripe's test card number is 4242 4242 4242 4242

Check the license of the models you're using first.


## Add another user login provider...

Login uses (nuxt-auth-tools)[https://nuxt.com/modules/auth-utils#supported-oauth-providers]

To add a new login type from nuxt-auth-tools
* Add your login link in `components/PresentationLogin.vue`
* Add a new file in `server/api/auth/<authtype>.js`

