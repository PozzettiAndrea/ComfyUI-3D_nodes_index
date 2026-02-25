# ComfyUI Charly FitToAspectNode

Un nodo personalizado para ComfyUI que ajusta imágenes a diferentes relaciones de aspecto manteniendo las proporciones originales.

## Características

- **Ajuste proporcional**: Redimensiona la imagen solo si es más grande que el objetivo, manteniendo las proporciones originales
- **Padding inteligente**: Calcula automáticamente el padding necesario para centrar la imagen en el tamaño objetivo
- **Múltiples relaciones de aspecto**: Soporta 11 relaciones de aspecto diferentes
- **Fondo negro**: Rellena las áreas vacías con color negro

## Relaciones de Aspecto Soportadas

| Relación | Resolución Objetivo |
|----------|-------------------|
| 1:1      | 1024 x 1024      |
| 16:9     | 1392 x 752       |
| 21:9     | 1568 x 672       |
| 3:2      | 1248 x 832       |
| 2:3      | 832 x 1248       |
| 4:5      | 944 x 1104       |
| 5:4      | 1104 x 944       |
| 3:4      | 880 x 1184       |
| 4:3      | 1184 x 880       |
| 9:16     | 752 x 1392       |
| 9:21     | 672 x 1568       |

## Uso

### Entradas
- **image**: Imagen de entrada (formato IMAGE)
- **aspect_ratio**: Relación de aspecto deseada (seleccionable desde la lista)

### Salidas
- **image**: Imagen ajustada al tamaño objetivo con padding
- **pad_top**: Padding superior en píxeles
- **pad_bottom**: Padding inferior en píxeles
- **pad_left**: Padding izquierdo en píxeles
- **pad_right**: Padding derecho en píxeles

## Ejemplo de Uso

1. Conecta una imagen al nodo "Fit To Aspect Node"
2. Selecciona la relación de aspecto deseada
3. El nodo devolverá:
   - La imagen ajustada al tamaño objetivo
   - Los valores de padding aplicados en cada borde

## Categoría

El nodo se encuentra en la categoría **"image/resize"** en ComfyUI.

## Instalación

1. Copia esta carpeta a `ComfyUI/custom_nodes/`
2. Reinicia ComfyUI
3. El nodo aparecerá en la categoría "image/resize"

## Requisitos

- ComfyUI
- PyTorch
- NumPy
- Pillow (PIL)
