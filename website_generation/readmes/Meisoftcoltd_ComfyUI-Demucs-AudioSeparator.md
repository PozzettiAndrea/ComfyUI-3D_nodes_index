# ComfyUI-Demucs-AudioSeparator

Nodo personalizado para ComfyUI que permite la separación de fuentes de audio utilizando la tecnología **Meta Demucs (v4)**. Ideal para extraer voces, baterías, bajos y otros instrumentos con alta fidelidad.

## Características

- **Soporte Demucs v4**: Incluye modelos Hybrid Transformer (HTDemucs).
- **Separación de hasta 6 pistas**: Voces, Batería, Bajo, Otros, y soporte para Guitarra y Piano (en modelos compatibles).
- **Aceleración CUDA**: Aprovecha la potencia de la GPU para procesos ultrarrápidos.
- **Descarga Automática**: Los modelos se descargan automáticamente a `ComfyUI/models/demucs`.
- **Estabilidad Mejorada**: Opción `split` para evitar errores de memoria (OOM) en audios largos.

## Instalación

### Vía ComfyUI Manager (Recomendado)
1. Busca `ComfyUI-Demucs-AudioSeparator` en el Manager.
2. Haz clic en Install.
3. Reinicia ComfyUI.

### Instalación Manual
1. Clona este repositorio en tu carpeta `custom_nodes`:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/usuario/ComfyUI-Demucs-AudioSeparator
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Reinicia ComfyUI.

## Parámetros del Nodo

- **audio**: El clip de audio a procesar.
- **model**:
  - `htdemucs`: Modelo estándar de 4 pistas.
  - `htdemucs_ft`: Versión fine-tuned del modelo estándar.
  - `htdemucs_6s`: Modelo de 6 pistas (incluye Guitarra y Piano).
  - `hdemucs_mmi`: Basado en HDemucs con mejoras.
  - `mdx` / `mdx_extra`: Modelos basados en Music Demixing Challenge.
- **device**: `cuda` para usar la GPU o `cpu`.
- **precision**: `float32`, `bfloat16`, `float16`. `bfloat16` es recomendado para arquitecturas Ampere (RTX 3090/4090).
- **shifts**: Número de predicciones aleatorias (mayor valor = mayor calidad, pero más lento). Recomendado: 1-5.
- **overlap**: Solapamiento entre ventanas de procesamiento. Por defecto: 0.25.
- **split**: Divide el audio en segmentos para ahorrar VRAM. Imprescindible para tarjetas con menos de 8GB o audios largos.
- **stems**: Activa o desactiva las salidas específicas para cada instrumento.

## Recomendaciones de Hardware

Para un rendimiento óptimo, se recomienda el uso de GPUs con aceleración CUDA:
- **VRAM**: Se recomienda al menos 8GB para modelos `htdemucs`. Si encuentras errores de memoria, asegúrate de tener activada la opción `split`.

## Reporte de Errores
Si encuentras algún problema, por favor abre un *Issue* en el repositorio de GitHub detallando tu sistema operativo, modelo de GPU y el error obtenido.

---
*Desarrollado para la comunidad de ComfyUI por un Senior Python Developer especializado en IA Multimedia (⚡ Bolt Edition).*
