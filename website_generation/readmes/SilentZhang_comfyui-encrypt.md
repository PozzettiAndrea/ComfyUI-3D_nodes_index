# comfyui-encrypt (RSA Edition)

这个仓库提供一个工具，用于在 ComfyUI 中对输入图像使用 RSA 算法加密。主要目标是把 RSA 加密逻辑封装为库函数，并提供可以直接在 ComfyUI 中使用的自定义节点与 Script 节点示例。

要点：
- 使用 RSA-2048（或 RSA-4096）非对称加密，接收端只需公钥即可加密。
- 提供密钥生成、加密、解密等函数。
- 使用 `cryptography` 库处理所有加密操作。

## 安装依赖

在仓库根目录下：

```powershell
pip install -r requirements.txt
```

## 基本用法（库函数 / 独立脚本）

生成密钥对：

```python
from rsa_encrypt import generate_rsa_keypair

private_pem, public_pem = generate_rsa_keypair(key_size=2048)
# private_pem, public_pem 都是 bytes 格式的 PEM 编码密钥
# 保存到文件中以供后续使用
with open("private_key.pem", "wb") as f:
    f.write(private_pem)
with open("public_key.pem", "wb") as f:
    f.write(public_pem)
```

加密图像：

```python
from PIL import Image
from rsa_encrypt import encrypt_image

# 读取公钥
with open("public_key.pem", "rb") as f:
    public_key_pem = f.read()

# 打开图像
img = Image.open("test_image.png")

# 加密
encrypted_bytes = encrypt_image(img, public_key_pem)

# 保存加密结果
with open("encrypted_image.rsa", "wb") as f:
    f.write(encrypted_bytes)
```

解密图像：

```python
from rsa_encrypt import decrypt_image

# 读取私钥
with open("private_key.pem", "rb") as f:
    private_key_pem = f.read()

# 读取加密文件
with open("encrypted_image.rsa", "rb") as f:
    encrypted_bytes = f.read()

# 解密
img = decrypt_image(encrypted_bytes, private_key_pem)
img.show()
```

## ComfyUI 中的使用

### 方式 1：使用自定义节点（推荐）


将 `rsa_encrypt.py`、`nodes.py` 和 `__init__.py` 整个文件夹（如 `comfyui-encrypt` 文件夹）复制到 ComfyUI 的 `custom_nodes` 目录下：

```
ComfyUI/custom_nodes/comfyui-encrypt/
├── __init__.py
├── nodes.py
└── rsa_encrypt.py
```

重启 ComfyUI 后，你会在 "Encryption" 分类中看到两个新节点：
- **RSAEncryptNode**：输入 IMAGE 和 RSA 公钥（PEM 字符串），输出加密文件路径
- **RSAKeyGeneratorNode**：生成 RSA 密钥对（2048 或 4096 位），可选保存到磁盘


### 方式 2：Script 节点自定义调用

你也可以在 Script 节点中直接调用核心库：

```python
from comfyui_encrypt.rsa_encrypt import encrypt_image

# 读取公钥（假设保存在某处）
with open("public_key.pem", "rb") as f:
    public_key_pem = f.read()

# image 是 ComfyUI 传入的 IMAGE 对象（PIL Image/numpy array）
enc_bytes = encrypt_image(image, public_key_pem)

# 保存
with open("encrypted_image.rsa", "wb") as f:
    f.write(enc_bytes)
```

## 测试

运行单元测试：

```powershell
pytest -q
```


## 关键文件说明

- `rsa_encrypt.py` — 核心库：密钥生成、加密/解密函数
- `nodes.py` — ComfyUI 自定义节点定义（两个节点类）
- `__init__.py` — 节点注册入口，供 ComfyUI 自动发现
- `requirements.txt` — Python 依赖清单
- `tests/test_rsa_encrypt.py` — pytest 单元测试

## 工作流例子

在 ComfyUI 中：
1. 使用 **RSAKeyGeneratorNode** 生成密钥对（或提前生成好）
2. 读取图像（LoadImage 节点或其它）
3. 使用 **RSAEncryptNode** 输入 IMAGE 和公钥进行加密
4. 输出加密文件路径，可链接到保存节点或后续处理

## 安全建议

- 保管好私钥！不要泄露私钥文件或其内容。
- 使用 RSA-4096（而不是 2048）以获得更强的安全性。
- 将密钥存放在安全的地方（如加密存储或受权限保护的目录）。
