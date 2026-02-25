# FireRedTTS-ComfyUI
a custom node for [FireRedTTS](https://github.com/FireRedTeam/FireRedTTS),you can find [workflow here](./doc/base_workflow.json)

## Weights
weights will be download from hf automaticily,对于国内用户你可以下载解压后把FireRedTTS整个文件夹放到ComfyUI/models/AIFSH目录下面，[下载链接](https://pan.quark.cn/s/5f2d4fa74fa2)

## 一键包
- [演示视频](https://www.bilibili.com/video/BV1ka2dYHEGi)
- [一键包，内含hallo2,JoyHallo,F5-TTS,FireRedTTS四个节点，持续更新中...](https://b23.tv/Zm3kPNP)

## Example
|text|prompt_wav|out_wav|
|--|--|--|
|`《三体》是刘慈欣创作的长篇科幻小说系列，由《三体》《三体2：黑暗森林》《三体3：死神永生》组成，第一部于2006年5月起在《科幻世界》杂志上连载，第二部于2008年5月首次出版，第三部则于2010年11月出版。作品讲述了地球人类文明和三体文明的信息交流、生死搏杀及两个文明在宇宙中的兴衰历程。其第一部经过刘宇昆翻译后获得了第73届雨果奖最佳长篇小说奖，第三部英文版获得2017年轨迹奖最佳长篇科幻小说奖。2019年，列入“新中国70年70部长篇小说典藏”。2022年9月，《三体》入选2021十大年度国家IP。`|<video src="https://github.com/user-attachments/assets/9489ce1b-6896-40aa-b2fc-71f5e78194da"/> |<video src="https://github.com/user-attachments/assets/500040d5-d544-4f41-9425-ba3af77d3225"/>|

## Features
- speed control
- auto split text
- text normalize
- Windows 10 or later surport
