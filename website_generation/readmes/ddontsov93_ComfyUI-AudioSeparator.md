# 🎧 ComfyUI Audio Separator

[English](#english) | [Русский](#русский)

---

## <a id="english"></a>English

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that integrates the powerful [audio-separator](https://github.com/karaokenerds/python-audio-separator) library (based on UVR5).  
It allows you to separate audio stems (vocals vs instrumental), remove background noise, and fix audio artifacts using GPU acceleration directly within your workflows.

### ✨ Features
*   **GPU Acceleration:** Uses your NVIDIA card (CUDA) for fast processing.
*   **UVR5 Architecture:** Supports MDX-Net and VR Architecture models.
*   **Local Models:** Automatically scans the `ComfyUI/models/UVR` folder for `.pth` and `.onnx` models.
*   **Flexible Settings:** Adjustable Window Size, Aggression, and Batch Size.

### 📥 Installation

1.  Clone this repository into your `custom_nodes` folder:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/ddontsov93/ComfyUI-AudioSeparator
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    *(If using the portable version of ComfyUI, run this command using the embedded python: `python_embeded\python.exe -m pip install -r requirements.txt`)*

### 🤖 Models Setup (Important!)

This node requires UVR models to work.
1.  The node will automatically create a folder: `ComfyUI/models/UVR`.
2.  You need to download model files (`.pth` or `.onnx`) and place them into this folder.

**Recommended Model for Denoising / Removing Artifacts:**
*   **1_HP-UVR.pth** (Great for removing tonal artifacts and noise):
    👉 [Download Link](https://huggingface.co/seanghay/uvr_models/resolve/main/1_HP-UVR.pth?download=true)

*Other popular models (UVR-MDX-NET-Inst_HQ_3, etc.) can also be used.*

### 🚀 Usage

1.  Add the node: **Audio** -> **Processing** -> **Audio Separator**.
2.  Connect your Audio input (e.g., from `Load Audio` or TTS node).
3.  Select the model from the list.
4.  **Outputs:**
    *   `Vocals (Clean)`: Usually contains the clean voice.
    *   `Instrumental (Noise)`: Contains the removed noise/music.

---

## <a id="русский"></a>Русский

Кастомная нода для [ComfyUI](https://github.com/comfyanonymous/ComfyUI), внедряющая мощную библиотеку [audio-separator](https://github.com/karaokenerds/python-audio-separator) (основанную на UVR5).  
Позволяет разделять аудио на дорожки (голос/минус), удалять фоновый шум и артефакты генерации, используя ускорение видеокарты (GPU) прямо внутри ваших воркфлоу.

### ✨ Возможности
*   **GPU Ускорение:** Использует видеокарту NVIDIA (CUDA) для быстрой обработки.
*   **Архитектура UVR5:** Поддержка моделей MDX-Net и VR Architecture.
*   **Локальные модели:** Автоматически сканирует папку `ComfyUI/models/UVR` на наличие файлов `.pth` и `.onnx`.
*   **Гибкие настройки:** Настройка размера окна (Window Size), агрессии (Aggression) и размера батча.

### 📥 Установка

1.  Склонируйте репозиторий в папку `custom_nodes`, нужно выполнить в ерминале comfy:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/ddontsov93/ComfyUI-AudioSeparator
    ```

2.  Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
    *(Если используете портативную версию ComfyUI, выполняйте команду через встроенный python: `python_embeded\python.exe -m pip install -r requirements.txt`)*

### 🤖 Настройка моделей (Важно!)

Для работы ноды требуются файлы моделей UVR.
1.  При первом запуске нода создаст папку: `ComfyUI/models/UVR`.
2.  Вам нужно скачать файлы моделей (`.pth` или `.onnx`) и положить их в эту папку.

**Рекомендуемая модель для шумоподавления / удаления артефактов:**
*   **1_HP-UVR.pth** (Отлично удаляет тональные писки и шум):
    👉 [Ссылка на скачивание](https://huggingface.co/seanghay/uvr_models/resolve/main/1_HP-UVR.pth?download=true)

*Вы также можете использовать любые другие модели UVR (UVR-MDX-NET-Inst_HQ_3 и т.д.).*

### 🚀 Использование

1.  Добавьте ноду: **Audio** -> **Processing** -> **Audio Separator**.
2.  Подключите аудио (например, от `Load Audio` или TTS ноды).
3.  Выберите модель из списка.
4.  **Выходы:**
    *   `Vocals (Clean)`: Обычно содержит чистый голос.
    *   `Instrumental (Noise)`: Содержит удаленный шум/музыку.