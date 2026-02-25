# 🧩 StudioFury
### Dirección artística de IA profesional y suite de flujo de trabajo avanzado para ComfyUI

<p align="center">
  <a href="README.md"><b>Español 🇪🇸</b></a> | 
  <a href="README_EN.md"><b>English 🇺🇸</b></a> | 
  <a href="https://github.com/FuryNocturn/StudioFury/wiki"><b>Documentation / Wiki 📖</b></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.12%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/ComfyUI-Custom_Node_Suite-green" alt="ComfyUI">
  <img src="https://img.shields.io/github/license/FuryNocturn/StudioFury" alt="License">
  <img src="https://img.shields.io/badge/version-2.0.0-orange" alt="Version">
</p>

---

**ComfyUI-Studio-Fury** es una suite de nodos personalizados para [ComfyUI](https://github.com/comfyanonymous/ComfyUI) diseñada para añadir versatilidad y potencia a tus flujos de trabajo. Enfocado en la organización, el soporte multi-idioma y una interfaz visual mejorada.

> *Nodos custom al estilo Fury: potencia, control y simplicidad.*

---

## ✨ Características Principales
* **🌐 Compatibilidad multilingüe nativa:** Los nodos detectan automáticamente el idioma de su sistema. Las etiquetas y descripciones se ajustan al español o al inglés según corresponda.
* **🚌 Arquitectura SF_LINK (Bus Cargado):** Elimine el cableado desordenado. Nuestro sistema de bus de datos transporta modelos, CLIP, VAE y metadatos de entidades a través de un único flujo consolidado.
* **📂 Arquitectura modular:** Los nodos se organizan en categorías especializadas (`prompts`, `dataset`, `director`, etc.) para mantener su espacio de trabajo profesional y ordenado.
* **🚀 Gestión inteligente de activos:** La sincronización automática de recursos web (JS/CSS) garantiza que la interfaz visual esté siempre actualizada y sin conflictos.

---

## 📦 Nodos Incluidos

### 📝 Categoría: Prompts
Herramientas avanzadas para la construcción y gestión de textos para modelos de difusión.

| Nodo | Descripción |
| :--- | :--- |
| **Advanced Prompt** 📝| Constructor de prompts modular. Divide el flujo en `Calidad`, `Estilo`, `Cámara`, `Sujeto` y `Entorno`. Incluye sanitización automática para evitar errores de sintaxis en el prompt final. |
| **Embeddings Selector** 💉 | **¡Interfaz Visual!** Muestra una tabla interactiva con todos tus *embeddings*. Permite clasificarlos como Positivos (P) o Negativos (N) con un clic, eliminando la necesidad de escribir rutas manualmente. |

### 📦 Categoría: Dataset & Project
Gestión de activos, persistencia de datos y organización del proyecto.

| Nodo | Descripción |
| :--- | :--- |
| **Project Manager** 📂 | El nodo raíz. Inicializa el bus de datos (`SF_LINK`), define el nombre del proyecto y centraliza el VAE y CLIP para mantener la consistencia en todo el flujo. |
| **Add Entity** 👤 | Registra personajes o escenas en el bus. Permite configurar el `Aspect Ratio` y codifica los prompts inmediatamente para ser procesados por el motor del director. |
| **Smart Saver** 💾 | Gestión de exportación. Guarda tus resultados en formato técnico `.fury` (preservando tensores y latentes) y genera una previsualización `.png` organizada por categorías. |
| **Asset Loader** 📥 | Recupera activos guardados. Carga tanto la imagen como el espacio latente original de archivos `.fury` para realizar refinamientos, inpainting o variaciones. |

### 🎬 Categoría: Director
Motor de ejecución y herramientas de composición artística de alta fidelidad.

| Nodo | Descripción |
| :--- | :--- |
| **Director Engine** 🧠 | El cerebro de renderizado masivo. Procesa todas las entidades del bus secuencialmente, gestionando la VRAM y liberando memoria automáticamente para evitar errores de sistema. |
| **Fury Sampler** 🎨 | Sampler optimizado con inyección de bus. Permite generar IDs específicos de entidades de forma individual, integrando metadatos de renderizado en el flujo de trabajo. |
| **Scene Composer** 🖼️ | Herramienta de montaje de precisión. Coloca personajes sobre fondos con control total de `Escala`, `Coordenadas X/Y` y `Opacidad` mediante blending de tensores en GPU. |
| **Action Animator** 📽️ | Generador de flujos de video. Convierte composiciones estáticas en batches latentes, aplicando máscaras de `Motion Freedom` para restringir el movimiento a áreas específicas. |

---

## 🛠️ Instalación

### Opción A: ComfyUI Manager (Recomendado)
1.  Busca **"ComfyUI-Studio-Fury"** en la lista de nodos personalizados.
2.  Haz clic en **Install**.
3.  Reinicia ComfyUI.

### Opción B: Instalación Manual (Git)
Si prefieres la línea de comandos, clona este repositorio dentro de tu carpeta `custom_nodes`:

```bash

cd ComfyUI/custom_nodes/
git clone [https://github.com/FuryNocturn/ComfyUI-Studio-Fury.git](https://github.com/FuryNocturn/ComfyUI-Studio-Fury.git) 
```
Luego reinicia tu ComfyUI.

---

## 📂 Estructura del Proyecto
Este pack utiliza una estructura de archivos híbrida para facilitar el desarrollo y la estabilidad:

```

ComfyUI-Studio-Fury/
├── prompts/           # Nodos relacionados con texto, construcción de prompts y gestión de embeddings.
├── Core/              # Lógica central del sistema: gestión de archivos (I/O), serialización .fury y bus SF_LINK.
├── dataset/           # Gestión de proyectos, persistencia de activos (Smart Saver) y carga de recursos.
├── director/          # Motores de renderizado (Engine), samplers personalizados y control de flujo secuencial.
├── images/            # (Próximamente) Nodos de composición visual, mezcla de tensores y post-procesado.
├── Interface/         # Recursos Javascript globales, menús de sistema (Restart/Shutdown) y extensiones visuales.
└── __init__.py        # Cargador dinámico inteligente y punto de entrada para el registro de nodos en la API.

```
---
## ⚙️ Herramientas de Sistema
Studio Fury extiende el menú de control de ComfyUI para mejorar la gestión del servidor:

🔄 Restart Server: Reinicia la instancia de ComfyUI para refrescar nodos o liberar memoria del sistema sin cerrar la terminal de comandos.

🛑 Shutdown Server: Realiza un apagado seguro y controlado de la instancia activa del servidor.

---

## 🤝 Contribuir
¡Las contribuciones son bienvenidas! Si tienes una idea para un nuevo nodo o una mejora:

1. Haz un Fork del proyecto.

2. Crea una nueva rama (git checkout -b feature/NuevaCaracteristica).

3. Añade tu nodo en la carpeta de categoría correspondiente (ej: prompts/).

4. Haz Commit y Push.

5. Abre un Pull Request.

---

## 📄 Licencia
Este proyecto está bajo la licencia MIT.

---

Creado con ❤️ por FuryNocturnTV
