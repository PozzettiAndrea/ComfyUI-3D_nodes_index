# Papcorns ComfyUI Custom Nodes 🍿

A collection of custom nodes for ComfyUI that enhances image processing and cloud storage capabilities.

## English

### Features

This package includes the following custom nodes:

#### 1. **Papcorns - Aspect Resize**
- **Category**: `Papcorns🍿`
- **Description**: Advanced image resizing with aspect ratio control
- **Modes**:
  - **Aspect Fill**: Zoom in and crop to exact target dimensions
  - **Aspect Fit**: Scale to fit within target dimensions and add padding
- **Padding Options**: Black or white padding for aspect fit mode

#### 2. **Upload Image To GCS**
- **Category**: `Papcorns🍿`
- **Description**: Upload images directly to Google Cloud Storage from ComfyUI
- **Features**: Automatic file naming, public URL generation, error handling

### Installation

1. Clone or download this repository to your ComfyUI custom nodes directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   git clone https://github.com/your-username/Papcorns-Comfyui-Custom-Nodes.git
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Restart ComfyUI

### Usage

#### Aspect Resize Node
1. Add the "Papcorns - Aspect Resize" node to your workflow
2. Connect an image input
3. Set your desired width and height
4. Choose resize mode:
   - **aspect_fill**: Image will be zoomed and cropped to exact dimensions
   - **aspect_fit**: Image will be scaled to fit with padding added
5. For aspect_fit mode, choose padding color (black or white)

#### GCS Upload Node
1. Add the "Upload Image To GCS" node to your workflow
2. Connect an image input
3. Set your Google Cloud Storage bucket name
4. Provide the path to your service account JSON file
5. The node will return a public URL of the uploaded image

### Requirements

- ComfyUI
- Python 3.7+
- PIL (Pillow)
- google-cloud-storage (for GCS upload node)
- Valid Google Cloud Storage credentials (for GCS upload node)

### GCS Setup

For the GCS upload node, you need:
1. A Google Cloud Storage bucket
2. A service account with Storage Admin permissions
3. Downloaded service account JSON key file

---

## Türkçe

### Özellikler

Bu paket aşağıdaki özel node'ları içerir:

#### 1. **Papcorns - Aspect Resize**
- **Kategori**: `Papcorns🍿`
- **Açıklama**: En-boy oranı kontrolü ile gelişmiş görüntü yeniden boyutlandırma
- **Modlar**:
  - **Aspect Fill**: Yakınlaştır ve tam hedef boyutlara kırp
  - **Aspect Fit**: Hedef boyutlara sığdır ve kenarları doldur
- **Dolgu Seçenekleri**: Aspect fit modu için siyah veya beyaz dolgu

#### 2. **Upload Image To GCS**
- **Kategori**: `Papcorns🍿`
- **Açıklama**: ComfyUI'den doğrudan Google Cloud Storage'a görüntü yükleme
- **Özellikler**: Otomatik dosya adlandırma, genel URL oluşturma, hata yönetimi

### Kurulum

1. Bu repository'yi ComfyUI özel node'lar dizininize klonlayın veya indirin:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   git clone https://github.com/your-username/Papcorns-Comfyui-Custom-Nodes.git
   ```

2. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. ComfyUI'yi yeniden başlatın

### Kullanım

#### Aspect Resize Node
1. "Papcorns - Aspect Resize" node'unu iş akışınıza ekleyin
2. Bir görüntü girişi bağlayın
3. İstediğiniz genişlik ve yüksekliği ayarlayın
4. Yeniden boyutlandırma modunu seçin:
   - **aspect_fill**: Görüntü yakınlaştırılacak ve tam boyutlara kırpılacak
   - **aspect_fit**: Görüntü sığdırılacak ve kenarlar doldurulacak
5. Aspect_fit modu için dolgu rengini seçin (siyah veya beyaz)

#### GCS Upload Node
1. "Upload Image To GCS" node'unu iş akışınıza ekleyin
2. Bir görüntü girişi bağlayın
3. Google Cloud Storage bucket adınızı ayarlayın
4. Servis hesabı JSON dosyanızın yolunu belirtin
5. Node, yüklenen görüntünün genel URL'sini döndürecektir

### Gereksinimler

- ComfyUI
- Python 3.7+
- PIL (Pillow)
- google-cloud-storage (GCS yükleme node'u için)
- Geçerli Google Cloud Storage kimlik bilgileri (GCS yükleme node'u için)

### GCS Kurulumu

GCS yükleme node'u için şunlara ihtiyacınız var:
1. Bir Google Cloud Storage bucket'ı
2. Storage Admin izinlerine sahip bir servis hesabı
3. İndirilmiş servis hesabı JSON anahtar dosyası

---

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.