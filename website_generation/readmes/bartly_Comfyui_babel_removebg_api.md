<p align="left">
    <a href="README_CN.md">中文</a>&nbsp ｜ &nbspEnglish&nbsp 
</p>
<br><br>

## Project Introduction

- Commercial-grade portrait segmentation, hair-level matting, with excellent results.

- Import the Babel Removebg API into ComfyUI through an API.

- You can use my apikey and apisecret (already configured in config.json. It's a bit slow without authentication). There are still several thousand images left. If it works well for you, remember to give it a star.

- Human Body Removebg:
   - For images under 3MB, it costs ¥0.1 per image for all users. Minimum resolution is 50, and maximum resolution is 2000.
   - For images over 3MB, it costs ¥0.2 per image. Open to subscribers. Minimum resolution is 50, and maximum resolution is 5000.
- Privileges for subscribers:
   - Faster processing.
   - Supports high-resolution large images.
   - Supports high concurrency.

## Installation

- Please apply for an API first before using (Don't worry it. Just use mine for now. Remember to give it a star!!!).

- Add the Babel apikey and apisecret to the config.json file. They will be automatically loaded when running.

- It is recommended to install using the manager ComfyUI Manager.

- Manual installation:
    1. `cd custom_nodes`
    2. `git clone https://github.com/bartly/Comfyui_babel_removebg_api`
    3. Restart ComfyUI.


## Workflows

  - There is only one node, and it looks like this.

    ![workflow](https://idphoto-output.oss-cn-shanghai.aliyuncs.com/78cc153f-5d8e-48e2-82f9-d00e6b70b474.png?OSSAccessKeyId=LTAI5tNJqEmgZRuFR7AiSdC3&Expires=78981527611967&Signature=G2HpOOIhaVoTnEf5r77rAv1JaAk%3D)


## Credits

[ComfyUI-StableDiffusion3-API](https://github.com/ZHO-ZHO-ZHO/ComfyUI-StableDiffusion3-API)
