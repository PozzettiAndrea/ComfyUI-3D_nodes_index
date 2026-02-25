![ComfyUI_temp_cyezl_00012_](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE/assets/140084057/e1a13978-1221-47c5-bdb6-6297be88fc02)

# ComfyUI SegMoE

Unofficial implementation of SegMoE for ComfyUI

![Dingtalk_20240205032816](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE/assets/140084057/3f2caec1-be8a-4091-a533-024da2503841)


## 项目介绍 | Info

- 对[SegMoE](https://github.com/segmind/segmoe)的非官方实现
  
- 版本：V1.0


## 节点说明 | Features

- 模型加载 | 🎩SegMoE Model Loader
    - 支持 [SegMoE 2x1](https://huggingface.co/segmind/SegMoE-2x1-v0)、[SegMoE 4x2](https://huggingface.co/segmind/SegMoE-4x2-v0)、[SegMoE SD 4x2](https://huggingface.co/segmind/SegMoE-sd-4x2-v0) 模型，输入模型名称（如：SegMoE 4x2）即可，会自动下载

- SegMoE 生成 | 🎩SegMoE Generation
    - pipe：接入模型
    - positivet、negative：正负提示词
    - step：步数，官方默认30步
    - guidance_scale：提示词相关度，一般默认为5
    - width、height：宽度、高度
    - seed：种子

 
## 安装 | Install

- 推荐使用管理器 ComfyUI Manager 安装（On the Way）

- 手动安装：
    1. `cd custom_nodes`
    2. `git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE.git`
    3. `cd custom_nodes/ComfyUI-SegMoE`
    4. `pip install -r requirements.txt`
    5. 重启 ComfyUI


## 使用注意 | Note

- 对显存要求较高，建议 VRAM > 20GB


## 工作流 | Workflows

V1.0

- [V1.0 SegMoE](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE/blob/main/SEGMOE%20WORKFLOWS/SegMoE%20V1.0%E3%80%90Zho%E3%80%91.json)
  
  ![Dingtalk_20240205034132](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE/assets/140084057/f09b11b1-1259-4f99-9870-c092dd7348c1)


## 更新日志

- 20240205

  创建项目 V1.0


## 速度实测 | Speed

- V1.0 

    - A100 50步 17s

    ![Dingtalk_20240205030707](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE/assets/140084057/bad1a00a-b943-43b8-b88f-faed6252d9b1)



## Stars 

[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/ComfyUI-SegMoE&type=Date)](https://star-history.com/#ZHO-ZHO-ZHO/ComfyUI-SegMoE&Date)


## 关于我 | About me

📬 **联系我**：
- 邮箱：zhozho3965@gmail.com
- QQ 群：839821928

🔗 **社交媒体**：
- 个人页：[-Zho-](https://jike.city/zho)
- Bilibili：[我的B站主页](https://space.bilibili.com/484366804)
- X（Twitter）：[我的Twitter](https://twitter.com/ZHOZHO672070)
- 小红书：[我的小红书主页](https://www.xiaohongshu.com/user/profile/63f11530000000001001e0c8?xhsshare=CopyLink&appuid=63f11530000000001001e0c8&apptime=1690528872)

💡 **支持我**：
- B站：[B站充电](https://space.bilibili.com/484366804)
- 爱发电：[为我充电](https://afdian.net/a/ZHOZHO)


## Credits

[SegMoE](https://github.com/segmind/segmoe)
