# ComfyUI Notifier


## 发送文件/消息到各种渠道

- [x] Telegram
- [x] Discord
- [x] yike [Alist](https://github.com/alist-org/alist.git) 
- [ ] Rclone ....
- [ ] [Telegraph-Image](https://github.com/cf-pages/Telegraph-Image.git)
- [ ] Minio，S3


<img width="907" alt="image" src="https://github.com/GentlemanHu/ComfyUI-Notifier/assets/34559079/e764aa8a-7682-495b-9e1e-876a6c410155">

---

> - 目前所有推送异步不阻塞ComfyUI流程，返回结果 `Result URL` 暂未实现
> - yike相册只支持 视频(<100M)和图片
> - 自动拆分消息体大小，分多次回复
> - Telegram文件<50M
> - Discord容易限频

## 配置 .env

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
DISCORD_WEBHOOK_URL=https://your.webhook.url
YIKE_BASE_URL=https://xxx
YIKE_TOKEN=your_token
```

---
---

# ComfyUI Notifier


## Send files/messages to various channels

- [x] Telegram
- [x] Discord
- [x] yike [Alist](https://github.com/alist-org/alist.git) 
- [ ] Rclone ....
- [ ] [Telegraph-Image](https://github.com/cf-pages/Telegraph-Image.git)


<img width="907" alt="image" src="https://github.com/GentlemanHu/ComfyUI-Notifier/assets/34559079/e764aa8a-7682-495b-9e1e-876a6c410155">

---

> - Currently, all push messages are asynchronous and do not block the ComfyUI process. The return result `Result URL` has not been implemented yet.
> - yike photo album only supports videos (<100M) and pictures
> - Automatically split the message body size and reply multiple times
> - Telegram files <50M
> - Discord is prone to rate limiting

## Configure .env

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
DISCORD_WEBHOOK_URL=https://your.webhook.url
YIKE_BASE_URL=https://xxx
YIKE_TOKEN=your_token
```
