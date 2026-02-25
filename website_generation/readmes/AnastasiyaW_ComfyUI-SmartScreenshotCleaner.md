# ComfyUI Smart Screenshot Cleaner

Ноды для очистки скриншотов от UI элементов.

## Ноды

### 1. SmartScreenshotCleaner
Находит UI элементы (иконки, кнопки, текст) и замазывает их в цвет окружения.

**Параметры:**
- `expand_mask` — расширить маску UI для лучшей заливки (0-30px)
- `confidence` — порог уверенности YOLO детекции (0.05-0.9)

**Выходы:**
- `image` — очищенное изображение (размер не меняется)
- `ui_mask` — маска найденных UI элементов

### 2. AutoBorderCrop
Обрезает однотонные рамки (тёмные/светлые) с краёв изображения.

**Параметры:**
- `sensitivity` — чувствительность детекции рамки
- `min_border_size` — минимальный размер рамки для обрезки

## Установка

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/AnastasiyaW/ComfyUI-SmartScreenshotCleaner.git comfy_image_preprocessor
cd comfy_image_preprocessor
pip install -r requirements.txt
```

## Модели

- **YOLO**: Microsoft OmniParser v2.0 — детекция UI элементов
- **LaMa**: simple-lama-inpainting — инпеинтинг

## Лицензия

MIT
