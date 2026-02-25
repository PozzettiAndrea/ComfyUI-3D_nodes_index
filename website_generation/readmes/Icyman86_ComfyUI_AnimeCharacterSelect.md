NOTE: This is a Direct copy of WAI-NSFW-illustrious-SDXL Dedicated Character Selector

Edits:    Trying to translate it all to English,
          Attempt to get it workingin ComfyUI,

Easy-to-use stable-diffusion-webui for WAI-NSFW-illustrious-SDXL
https://civitai.com/models/827184?modelVersionId=1183765

Related Dependencies

add-detail-xl
https://huggingface.co/PvDeep/Add-Detail-XL/blob/main/add-detail-xl.safetensors

Pony: People's Works - ponyv4_noob1_2_adamW-000017
https://civitai.green/models/856285/pony-peoples-works?modelVersionId=1036362

ChihunHentai
https://civitai.com/models/106586

SDXL VAE
https://civitai.com/models/296576?modelVersionId=333245

How to Install: Just install through the regular URL

To install: Go to the settings tab of stable-diffusion-webui, go to “install from url,” paste this URL, and click install:

Update!!!!! If new features don’t work, please delete and reinstall!!!!

4/13 Added 100 characters

2/23 Adjusted some defaults, added simple mobile mode

2/22 Character translations completed. I don’t really want to translate the actions part (not enough courage, don’t want people to catch me...), some prompt adjustments

2/20 Minor tweaks and translations, fixed crash bug caused by switching too fast, added separate random button

2/15 Updated AI features (default, you can apply for your own API key), corrected some character names, no extra file download needed, AI currently uses llama-3.3-70b-versatile

1/19 Updated AI features, corrected some character names, extended download timeout to 10 minutes

AI features support various APIs, e.g., groq llama-3.3-70b-versatile (free)

Setup method:

extensions\WAI-NSFW-illustrious-character-select\custom_settings.json

Set ai to true and enter your api_key (apply yourself at https://console.groq.com/)

Example:

json
Copy
Edit
{
    "ai": true,
    "base_url": "https://api.groq.com/openai/v1/chat/completions",
    "model": "llama-3.3-70b-versatile",
    "api_key": "gsk_UGQDzQaAxXrWx9ycd9OlW--------------------"
}
