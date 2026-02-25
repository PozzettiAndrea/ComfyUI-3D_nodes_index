# ComfyUiRagCustomNodes

Этот пакет содержит кастомные ноды для [ComfyUI](https://github.com/comfyanonymous/ComfyUI):

- Генерация изображений с помощью Stable Diffusion и LLM
- Загрузка и поиск изображений через Qdrant и MinIO (S3)
- Интеграция с CLIP, Ollama, и другими инструментами

## Структура

- `custom_ksampler.py` — кастомный KSampler с поддержкой RAG
- `llm_node.py` — нода для работы с LLM (Ollama)
- `db_load_node.py` — загрузка изображений из базы
- `s3_utils.py` — утилиты для работы с MinIO/S3
- `load_images_utils.py` — утилиты для поиска и загрузки изображений

## Установка

Скопируйте папку в директорию `custom_nodes` вашего ComfyUI.

## Требования

- Python 3.10+
- ComfyUI
- MinIO/S3
- Qdrant
- Ollama

## Поддержка Ollama

Для использования LLM ноды необходимо установить [Ollama](https://ollama.ai).

---

### Установка Ollama

Windows/MacOS/Linux: скачайте [установщик](https://ollama.com/download) с официального сайта

### Установка LLM

LLM нода работает с моделью qwen2:7b, для ее установки:

```bash
ollama pull qwen2:7b
```

## Использование

Добавьте ноды через интерфейс ComfyUI и настройте параметры согласно вашим задачам.


## Примеры

В папке testFlows содержатся примеры применения кастомных pipelines.
Для их корректной работы необходимо установить дополнительный репозиторий:
[ComfyUI_IPAdapter_plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus) 