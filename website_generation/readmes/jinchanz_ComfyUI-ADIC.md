# ComfyUI 图片翻译 API 节点

这是一个用于在 ComfyUI 中调用图片翻译 API 的自定义节点集合。

## 功能特性

- 支持批量图片翻译
- 支持多种源语言和目标语言
- Bearer Token 认证
- 完整的错误处理和日志记录
- 提供URL构建器和结果提取器辅助节点

## 安装

1. 将插件文件夹放置在 ComfyUI 的 `custom_nodes` 目录下
2. 重启 ComfyUI
3. 确保已安装 `requests` 库：`pip install requests`

## 节点说明

### 1. 图片翻译 API (ImageTranslateAPI)
**主要的图片翻译节点，调用翻译API**

#### 输入参数
**必需参数：**
- `params`: 翻译参数（JSON字符串格式，包含params数组）
- `api_key`: API密钥（用于Bearer认证）
- `api_endpoint`: API端点URL

#### 输出
- `response`: 完整的API响应结果（JSON字符串）

#### params参数格式
```json
{
  "params": [
    {
      "sourceLanguage": "zh",
      "targetLanguage": "en", 
      "url": "https://example.com/image1.jpg"
    },
    {
      "sourceLanguage": "zh",
      "targetLanguage": "fr",
      "url": "https://example.com/image2.jpg"
    }
  ]
}
```

#### 支持的语言
**源语言：**
- `auto`: 自动检测
- `zh`: 中文
- `en`: 英文
- `tr`: 土耳其语

**目标语言：**
- `es`: 西班牙语
- `fr`: 法语
- `pt`: 葡萄牙语
- `ko`: 韩语
- `en`: 英语

### 2. 图片翻译参数构建器 (ImageTranslateParamsBuilder)
**便于构建符合API要求的params参数**

#### 输入参数
**必需参数：**
- `url1`: 第一个图片URL

**可选参数：**
- `source_language1`: 第一张图片的源语言（zh/en/tr，留空则不指定）
- `target_language1`: 第一张图片的目标语言（es/fr/pt/ko/en，默认为en）
- `url2`: 第二个图片URL
- `source_language2`: 第二张图片的源语言
- `target_language2`: 第二张图片的目标语言
- `url3`: 第三个图片URL
- `source_language3`: 第三张图片的源语言
- `target_language3`: 第三张图片的目标语言

#### 输出
- `params_json`: 符合API要求的params JSON字符串

### 3. 图片翻译结果提取器 (ImageTranslateResultExtractor)
**从API响应中提取特定数据**

#### 输入参数
**必需参数：**
- `api_response`: API响应的JSON字符串

**可选参数：**
- `extract_type`: 提取类型（all/result_urls/result_jsons/source_info，默认为result_urls）
- `index`: 索引（当前未使用，预留功能）

#### 输出
- `extracted_data`: 提取到的数据

#### 提取类型说明
- **all**: 返回完整的数据列表
- **result_urls**: 提取所有翻译后的图片URL
- **result_jsons**: 提取所有翻译结果的JSON数据
- **source_info**: 提取源信息（原URL和语言信息）

## 使用示例

### API请求格式
根据Swagger文档，节点会构建如下格式的请求：
```json
{
  "params": [
    {
      "url": "https://example.com/image1.jpg",
      "sourceLanguage": "zh",
      "targetLanguage": "en"
    },
    {
      "url": "https://example.com/image2.jpg",
      "sourceLanguage": "zh", 
      "targetLanguage": "en"
    }
  ]
}
```

### API响应格式
成功响应示例：
```json
{
  "code": 200,
  "success": true,
  "message": "成功",
  "data": [
    {
      "url": "https://example.com/image1.jpg",
      "sourceLanguage": "zh",
      "targetLanguage": "en",
      "resultUrl": "https://result.com/translated1.jpg",
      "resultJson": "{\"translations\": [...]}"
    }
  ],
  "debugInfo": null
}
```

## 使用场景

### 场景一：单张图片翻译
1. 直接在 **图片翻译 API** 节点输入单个URL
2. 设置源语言和目标语言
3. 配置API密钥

### 场景二：批量图片翻译
1. 使用 **参数构建器** 节点输入多个图片URL和语言设置
2. 将输出连接到 **图片翻译 API** 节点
3. 使用 **结果提取器** 节点提取翻译后的图片URL

### 场景三：工作流组合
```
参数构建器 → 图片翻译API → 结果提取器 → 后续处理节点
```

## 注意事项

1. 需要有效的API密钥才能正常使用
2. 图片URL必须是公开可访问的HTTP/HTTPS地址
3. API有请求频率和并发限制，请合理使用
4. 支持的语言组合有限，请参考文档说明
5. 翻译结果的质量依赖于原图片的清晰度和文字质量

## 错误处理

节点包含完整的错误处理机制：
- 网络请求错误
- JSON解析错误
- API业务错误
- URL格式验证错误

错误信息会在ComfyUI控制台中输出，并返回包含错误信息的JSON。

## API文档

此节点基于以下Swagger API规范实现：
- 接口地址：`/open/api/v1/ai/imageTranslate`
- 认证方式：Bearer Token
- 请求方法：POST
- 内容类型：application/json 