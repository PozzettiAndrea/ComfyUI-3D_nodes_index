# ComfyUI-CartesiaTTS

Nodo para **Cartesia Sonic-3** que llama al endpoint `/tts/bytes` y devuelve:
- `file_path`: ruta absoluta del archivo (wav/mp3/raw)
- `bytes`: audio en binario
- `url`: `file://...` o un link subido a tmpfiles.org (si activás `upload_to_tmpfiles`)

## Instalación
1. Cloná este repo dentro de `ComfyUI/custom_nodes/ComfyUI-CartesiaTTS/`
2. Reiniciá ComfyUI.

## Uso (inputs clave)
- `api_key`: tu Cartesia API Key
- `transcript`: texto a sintetizar
- `voice_id`: ID de voz
- Opcionales: `container` (wav/mp3/raw), `encoding` (pcm_f32le, etc.), `sample_rate` (44100), `gen_speed`, `gen_volume`
- `upload_to_tmpfiles`: si se activa, intenta subir el archivo y devolver un link público (best-effort).

## Flujo típico
```
[External Text transcript] → [Cartesia Sonic-3 TTS]
                       file_path / url / bytes
                 → (url) HeyGen /video/generate (voice.type="audio", audio_url=url)
                 → Poll → Download video
```

## Requisitos
- `requests`

## Licencia
MIT
