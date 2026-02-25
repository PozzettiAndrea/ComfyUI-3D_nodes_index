# ComfyUI-HMT-Ultimate

Custom nodes cho ComfyUI với nhiều tính năng đặc biệt.
## Tính năng
1. Text to Speed
- **VieNeu TTS (Preset Voice)**: Chuyển văn bản tiếng Việt thành giọng nói với các giọng preset có sẵn
- **VieNeu TTS (Voice Clone)**: Clone giọng nói từ audio mẫu và tạo speech mới
- **VieNeu List Voices**: Liệt kê tất cả các giọng preset có sẵn

## Cài đặt

### Bước 1: Clone repository

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-repo/ComfyUI-HMT-Ultimate.git
```

### Bước 2: Cài đặt dependencies

#### Option 1: Tự động (Khuyến nghị)

```bash
cd ComfyUI-HMT-Ultimate
python install.py
```

Script sẽ tự động detect platform và cài đặt đúng dependencies.

#### Option 2: Thủ công

**Windows:**
```bash
cd ComfyUI-HMT-Ultimate
pip install vieneu --extra-index-url https://pnnbao97.github.io/llama-cpp-python-v0.3.16/cpu/
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
cd ComfyUI-HMT-Ultimate
pip install vieneu
pip install -r requirements.txt
```

### Bước 3: Khởi động lại ComfyUI

## Sử dụng

### 1. VieNeu TTS (Preset Voice)

Node này cho phép bạn chuyển văn bản tiếng Việt thành giọng nói sử dụng các giọng preset.

**Inputs:**
- `text`: Văn bản cần chuyển thành giọng nói (Vietnamese)
- `voice`: Chọn giọng từ danh sách preset
- `filename_prefix`: Tiền tố tên file output

**Outputs:**
- `audio`: Audio data
- `filepath`: Đường dẫn file audio đã lưu

### 2. VieNeu TTS (Voice Clone)

Node này cho phép clone giọng nói từ audio mẫu và tạo speech mới.

**Inputs:**
- `text`: Văn bản cần chuyển thành giọng nói
- `ref_audio_path`: Đường dẫn đến file audio mẫu (3-5s)
- `ref_text`: Transcript của audio mẫu
- `filename_prefix`: Tiền tố tên file output

**Outputs:**
- `audio`: Audio data
- `filepath`: Đường dẫn file audio đã lưu

### 3. VieNeu List Voices

Node này hiển thị danh sách tất cả các giọng preset có sẵn.

**Outputs:**
- `voices_list`: Danh sách các giọng preset

## Ví dụ

### Ví dụ 1: Tạo speech với preset voice

1. Thêm node "VieNeu TTS (Preset Voice)"
2. Nhập văn bản: "Xin chào, tôi là VieNeu TTS"
3. Chọn giọng từ dropdown
4. Run workflow

### Ví dụ 2: Clone giọng nói

1. Chuẩn bị file audio mẫu (3-5s) và transcript tương ứng
2. Thêm node "VieNeu TTS (Voice Clone)"
3. Nhập đường dẫn audio mẫu và transcript
4. Nhập văn bản cần tạo giọng nói
5. Run workflow

## Yêu cầu

- Python 3.8+
- PyTorch
- VieNeu SDK
- ComfyUI

## Hỗ trợ

Nếu bạn gặp vấn đề, vui lòng tạo issue trên GitHub repository.

## License

MIT License

## Credits

- VieNeu-TTS SDK: [pnnbao-ump/VieNeu-TTS](https://huggingface.co/pnnbao-ump)
- ComfyUI: [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)
