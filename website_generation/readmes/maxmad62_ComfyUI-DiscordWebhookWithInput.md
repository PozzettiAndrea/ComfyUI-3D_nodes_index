# ComfyUI-DiscordWebhookWithInput

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to send **an image + a message (e.g. your prompt)** to a Discord channel via a webhook.

This is based on the original Discord webhook node, with one key improvement:  
👉 you can connect a text input directly into the node (instead of only typing fixed text inside the node).

---

## ✨ Features
- Send an image and a message to a Discord webhook.
- Optional: send only text, only image, or both.
- Message input can be connected to your workflow (e.g. the same prompt you pass to CLIP).
- Handles batched images (splits into multiple messages if needed).
- Automatically resizes images >20 MB to respect Discord’s limits.
- 2000-character message limit (Discord restriction).

---

## 📦 Installation

In your `ComfyUI/custom_nodes` directory:

```bash
git clone https://github.com/maxmad62/ComfyUI-DiscordWebhookWithInput.git
````

Then restart ComfyUI.

---

## 🔧 Usage

1. **Set Discord Webhook**

   * Add the node `Set Discord Webhook` and paste your Discord webhook URL.
   * Run it once — it will save your webhook URL locally (see below).

2. **Use Discord Webhook (+message input)**

   * Add the node `Use Discord Webhook (+message input)`.
   * Plug an **image** into `image`.
   * Plug a **string** (prompt, seed info, metadata…) into `message`.
   * Toggle:

     * `send_Image = true/false`
     * `send_Message = true/false`

3. **Run the workflow**

   * The bot posts your message and/or image in the chosen Discord channel.

---

## 🔐 Security / Secrets setup (manual method)

This version does **not** store your webhook URL inside the workflow or PNG metadata, preventing accidental leaks when sharing files.

To make it work, you must create a small local secrets file once:

1. Go to

   ```
   ComfyUI/custom_nodes/ComfyUI-DiscordWebhookWithInput/
   ```
2. Create a new folder called:

   ```
   secrets
   ```
3. Inside, create a file:

   ```
   webhook.txt
   ```
4. Paste your full Discord webhook URL inside (one line only), for example:

   ```
   https://discord.com/api/webhooks/XXXXXXXXX/YYYYYYYYYYYYYYYY
   ```

✅ That’s it — the node will automatically read this file on each run.
🔒 The folder `secrets/` is ignored by Git and safe to keep locally.

---

## 📋 Notes

* Make sure to install the dependency if missing:

  ```bash
  pip install discord-webhook
  ```

  (or `python_embeded\python.exe -m pip install discord-webhook` if using portable ComfyUI on Windows.)

* Discord message length is limited to 2000 characters.

* Images larger than 20 MB are resized automatically.

---

## 📜 License

MIT License – feel free to use and modify.

---

## 🙌 Credits

* Original base node by **Dayuppy**
* Modifications and safe secret handling by **maxmad62**

````
Souhaites-tu que je te génère à la suite un petit badge GitHub “ComfyUI Node” et “Discord Ready” (visuel en haut du README) ?
