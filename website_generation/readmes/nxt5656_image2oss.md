# comfyui_image2oss

## 功能
### 获取图片
1. image2oss  保存图片到阿里云oss上,使用自建服务阿里云AK&SK&Token
2. image2oss-sts-service 保存图片到阿里云oss上,使用自建服务获取阿里云AK&SK&Token
3. image2oss-tag 保存图片到阿里云oss上,并添加"Ai生成"的水印,使用阿里云AK&SK(支持ststoken)
4. image2oss-tag-sts-service 保存图片到阿里云oss上,并添加"Ai生成"的水印,使用自建服务阿里云AK&SK&Token
5. oss2image 从阿里云oss上获取图片,使用阿里云AK&SK(支持ststoken)
6. oss2image-sts-service 从阿里云oss上获取图片,使用自建服务阿里云AK&SK&Token
7. url2image 从url获取图片



## Quickstart

1. 安装 [ComfyUI](https://docs.comfy.org/get_started).
2. 安装 [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
3. 运行`comfy node registry-install image2oss` 或[直接下载](https://registry.comfy.org/publishers/nxt5656/nodes/image2oss)插件到comfyui的custom_nodes目录
4. 重启 ComfyUI.

## 参数说明
### filename
格式为字符串列表,这个列表中每个字符串是图片在oss时的对象名称,必须包含完整oss路径.
注意:保存图片到oss时,这里是个列表,可以通过image输入多张图片,与filename列表数量保持一致

### access_key_id
阿里云ak

### access_key_secret
阿里云ak对应的密钥

### security_token
阿里云STS安全令牌

### sts_service_url
获取阿里云ak信息的地址
返回数据格式为:
```json
{
  "requestId": "非必要",
  "success": true,
  "errorMessage": "",
  "data": {
    "accessKeyId": "阿里云AK",
    "accessKeySecret": "阿里云SK",
    "securityToken": "阿里云STS安全令牌",
    "expiration": "2025-04-29T14:37:56Z",
    "arn": "非必要",
    "assumedRoleId": "非必要"
  }
}
```

### bucket_name
阿里云 bucket 名称

### endpoint
[oss的endpoing](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)

## AI标记
中国法规要求,ai生成内容必须添加ai相关标记,标准如下:

[网络安全技术 人工智能生成合成内容标识方法](https://www.tc260.org.cn/upload/2025-03-15/1742009439794081593.pdf)
