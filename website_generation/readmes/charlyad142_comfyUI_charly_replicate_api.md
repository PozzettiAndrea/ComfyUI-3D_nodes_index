# ComfyUI Replicate Image Generation & Edit

Este nodo de ComfyUI permite usar varios modelos de Replicate para generar y editar imágenes:

- **Qwen Image Edit Plus (Multi-Image)**: Usa `qwen/qwen-image-edit-plus` para editar múltiples imágenes basándose en poses de referencia
- **Qwen Image Edit (Single Image)**: Usa `qwen/qwen-image-edit` para editar una sola imagen con instrucciones de texto
- **SeedEdit 3.0 (ByteDance)**: Usa `bytedance/seededit-3.0` para edición avanzada de imágenes con control de adherencia al prompt
- **Seedream 4.0 (ByteDance)**: Usa `bytedance/seedream-4` para generación de imágenes de alta calidad con múltiples resoluciones

## Características

### Qwen Image Edit Plus (Multi-Image)
- **Edición de múltiples imágenes**: Acepta 1-5 imágenes, la primera como referencia de pose
- **Edición basada en poses**: Las demás imágenes adoptan la pose de la primera imagen
- **Flexibilidad**: Puedes usar entre 1 y 5 imágenes según tus necesidades

### Qwen Image Edit (Single Image)
- **Edición de imagen única**: Acepta una sola imagen para editar
- **Instrucciones de texto**: Usa prompts de texto para describir cómo editar la imagen
- **Simplicidad**: Ideal para ediciones directas con instrucciones claras

### SeedEdit 3.0 (ByteDance)
- **Edición avanzada**: Modelo especializado de ByteDance para edición de imágenes
- **Control de adherencia**: Parámetro `guidance_scale` para controlar qué tan literal es el resultado
- **Alta calidad**: Optimizado para ediciones precisas y detalladas

### Seedream 4.0 (ByteDance)
- **Generación de imágenes**: Modelo de ByteDance para generar imágenes desde texto
- **Múltiples resoluciones**: Soporte para 1K, 2K, 4K y dimensiones personalizadas
- **Generación secuencial**: Opción para generar múltiples imágenes relacionadas
- **Image-to-image**: Soporte para generación basada en imágenes de entrada

### Características generales
- **Integración con Replicate API**: Utiliza la API oficial de Replicate
- **Configuración flexible**: Soporte para múltiples parámetros de configuración
- **Manejo de errores robusto**: Gestión completa de errores y timeouts

## Instalación

1. Coloca este nodo en la carpeta `custom_nodes` de ComfyUI
2. Instala las dependencias necesarias:
   ```bash
   pip install replicate requests pillow
   ```

## Configuración

### Opción 1: Variable de entorno (Recomendado)
```bash
export REPLICATE_API_TOKEN="tu_token_aqui"
```

### Opción 2: Archivo de configuración
Edita el archivo `config.ini` y reemplaza `tu_token_aqui` con tu token de API de Replicate.

### Opción 3: Token en el nodo
Puedes ingresar el token directamente en el campo `api_token` del nodo.

## Uso

### Qwen Image Edit Plus (Multi-Image)
1. **images**: Una o más imágenes (mínimo 1, máximo 5). La primera imagen se usa como referencia de pose, las demás se editan.
2. **prompt**: Descripción de cómo quieres que se edite la imagen (ej: "The person in the second image adopts the pose from the first image")
3. **api_token**: Token de API de Replicate (opcional si está configurado en variables de entorno)

### Qwen Image Edit (Single Image)
1. **image**: Una sola imagen para editar
2. **prompt**: Instrucciones de texto sobre cómo editar la imagen (ej: "Make the person wear a red shirt", "Change the background to a beach")
3. **api_token**: Token de API de Replicate (opcional si está configurado en variables de entorno)

### SeedEdit 3.0 (ByteDance)
1. **image**: Una sola imagen para editar
2. **prompt**: Instrucciones de texto sobre cómo editar la imagen
3. **api_token**: Token de API de Replicate (opcional si está configurado en variables de entorno)

### Seedream 4.0 (ByteDance)
1. **prompt**: Descripción de la imagen que quieres generar
2. **api_token**: Token de API de Replicate (opcional si está configurado en variables de entorno)
3. **image_input** (opcional): Imagen de referencia para generación image-to-image

### Parámetros opcionales

#### Para Qwen Image Edit Plus y Qwen Image Edit:
- **seed**: Semilla aleatoria para generación reproducible (-1 para aleatorio)
- **go_fast**: Ejecutar predicciones más rápidas con optimizaciones adicionales (por defecto: True)
- **aspect_ratio**: Proporción de aspecto para la imagen generada (por defecto: "match_input_image")
- **output_format**: Formato de salida (por defecto: "webp")
- **output_quality**: Calidad de salida de 0 a 100 (por defecto: 95)
- **disable_safety_checker**: Deshabilitar el verificador de seguridad (por defecto: False)

#### Para SeedEdit 3.0:
- **seed**: Semilla aleatoria para generación reproducible (-1 para aleatorio)
- **guidance_scale**: Control de adherencia al prompt (1.0-10.0, por defecto: 5.5)
  - Valores más altos = más literal al prompt
  - Valores más bajos = más creativo/artístico

#### Para Seedream 4.0:
- **size**: Resolución de la imagen (1K, 2K, 4K, custom)
- **width**: Ancho personalizado (1024-4096, solo cuando size='custom')
- **height**: Alto personalizado (1024-4096, solo cuando size='custom')
- **max_images**: Número máximo de imágenes a generar (1-15)
- **aspect_ratio**: Proporción de aspecto de la imagen
- **sequential_image_generation**: Modo de generación (disabled, auto)

## Salidas

- **image**: Imagen editada como tensor de ComfyUI
- **output_url**: URL de la imagen generada en Replicate

## Ejemplos de uso

### Qwen Image Edit Plus (Multi-Image)
1. Carga una o más imágenes en el campo `images` (mínimo 1, máximo 5)
2. La primera imagen se usa como referencia de pose
3. Las demás imágenes se editarán para adoptar la pose de la primera
4. Escribe un prompt descriptivo como "The person in the second image adopts the pose from the first image"
5. Configura tu token de API
6. Ejecuta el nodo

### Qwen Image Edit (Single Image)
1. Carga una imagen en el campo `image`
2. Escribe instrucciones claras como "Make the person wear a red shirt" o "Change the background to a beach"
3. Configura tu token de API
4. Ejecuta el nodo

### SeedEdit 3.0 (ByteDance)
1. Carga una imagen en el campo `image`
2. Escribe instrucciones detalladas sobre cómo editar la imagen
3. Ajusta el `guidance_scale` según necesites más o menos adherencia al prompt
4. Configura tu token de API
5. Ejecuta el nodo

### Seedream 4.0 (ByteDance)
1. Escribe un prompt descriptivo de la imagen que quieres generar
2. Selecciona la resolución (1K, 2K, 4K o custom)
3. Si usas 'custom', configura width y height
4. Opcionalmente conecta una imagen de referencia en `image_input`
5. Configura tu token de API
6. Ejecuta el nodo

## Obtener token de API

1. Ve a [https://replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)
2. Crea una cuenta o inicia sesión
3. Genera un nuevo token de API
4. Copia el token y configúralo según una de las opciones anteriores

## Notas

- El nodo convierte las imágenes de entrada a formato base64 para enviarlas a la API
- La imagen de salida se descarga automáticamente y se convierte al formato de tensor de ComfyUI
- El nodo incluye manejo de errores completo y mensajes informativos
