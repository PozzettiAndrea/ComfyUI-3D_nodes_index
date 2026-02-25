# 🔔 ComfyUI NotificationBridge

A lightweight **notification bridge system** for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).  
Send alerts when a workflow completes — currently supports WhatsApp notifications via Twilio and Discord webhooks.

These nodes act as **bridges** between processing steps and the final output (like `[Save Image]`), making them easy to integrate at the tail end of any image pipeline.

---

## ✅ Features

- 📲 **WhatsApp Notifications (Twilio Sandbox)**
- 💬 **Discord Channel Alerts (Webhook-based)**

---

## 📦 Usage

After installing, two new nodes will appear in the ComfyUI node menu under **Notifications**:

### 📲 WhatsApp (Twilio) & 💬 Discord Notify

These nodes are designed to **act as bridges** between your decoder and the output step — such as `[Save Image]`.

For example:

```
[VAE Decode] → [💬 Discord Notify] → [Save Image]
[VAE Decode] → [📲 WhatsApp (Twilio)] → [Save Image]
```

---

### 💬 Discord Notify
Use this node to send a message to a Discord channel via webhook.

**Inputs:**
- `img`: bridge input from upstream (e.g., `[VAE Decode]`)
- `message`: text to send
- `webhook_url`: Discord channel webhook URL

---

### 📲 WhatsApp (Twilio)
Use this node to send a WhatsApp message via Twilio’s API.

**Inputs:**
- `img`: bridge input to maintain image flow
- `message`: message text
- `sid`: Twilio Account SID
- `token`: Twilio Auth Token
- `from_number`: `whatsapp:+14155238886` (Twilio Sandbox)
- `to_number`: your verified WhatsApp number

---

## 🛠 Installation

Clone this repo into your ComfyUI `custom_nodes` folder:

```bash
git clone https://github.com/INuBq8/ComfyUI-NotificationBridge.git
```

If you're using WhatsApp (Twilio), install the required Python package in the requirements.txt
Comfy should do this automatically on startup so you  don't need to worry most of the times
---

## 🧪 Notes

This is my first custom ComfyUI node — built on the fly as a learning hobby project.  
Feedback and ideas for improvement are welcome!

---

MIT Licensed – use freely and build on it.
