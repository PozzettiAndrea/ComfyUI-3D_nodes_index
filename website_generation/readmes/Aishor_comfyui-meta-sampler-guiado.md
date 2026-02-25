# Meta-Sampler Guiado (Seed-WAN)
Implementación del sampler híbrido que fusiona WAN 2.2 con SeedVR2 para outpainting de video

## Descripción
Este nodo personalizado implementa el "Meta-Sampler Guiado" (también conocido como Seed-WAN), un sampler híbrido que unifica un modelo generativo de video (como WAN 2.2) con un modelo de restauración y súper-resolución (como SeedVR2) a nivel de espacio latente. 

En lugar de un pipeline secuencial (generar y luego restaurar), nuestro método utiliza la salida de SeedVR2 como un "ancla latente" de alta fidelidad. En cada paso del bucle de denoising del modelo generativo (WAN), inyectamos forzosamente estos latentes de guía pre-procesados en el área del contenido original. Esto obliga al modelo generativo a enfocar toda su inferencia creativa (guiada por prompts de texto) únicamente en la región de outpainting, asegurando una transición de costura perfecta y una coherencia temporal heredada del modelo de restauración.

## Instalación
1. Coloque esta carpeta en el directorio `custom_nodes` de ComfyUI
2. Reinicie ComfyUI
3. El nodo estará disponible en la categoría "sampling"

## Uso
El nodo requiere los siguientes inputs:
- `model`: El modelo WAN 2.2
- `seed`: Semilla para la generación
- `steps`: Número de pasos de muestreo
- `cfg`: Escala del guía de clasificación
- `positive`: Conditioning positivo
- `negative`: Conditioning negativo
- `video_original`: Latente del video original
- `video_latente_guia`: Latente del video procesado con SeedVR2
- `mascara`: Máscara indicando la región de outpainting
- `sampler_name`: Nombre del sampler a usar
- `scheduler`: Scheduler para el muestreo
- `denoise`: Factor de ruido
- `VAE_WAN` (opcional): VAE específico para WAN 2.2
- `feather_mask_pixels` (opcional): Número de píxeles para difuminar la máscara (evitar artefactos de borde)

## Funcionalidades
- Inyección de latentes de restauración en cada paso del muestreo
- Compatible con diferentes schedulers y samplers
- Feathering de máscara para transiciones suaves
- Preservación de coherencia temporal
- Control total mediante prompts de texto
- Manejo de videos de diferentes tamaños

## Requisitos
- ComfyUI
- Modelos WAN 2.2 y SeedVR2
- (Opcional) VAE compatible con WAN 2.2

## Notas
Este nodo implementa la metodología descrita en el documento "Meta-Sampler Guiado.txt", fusionando los procesos de muestreo para lograr outpainting de video temporalmente coherente.