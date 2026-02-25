# 🧩 ComfyUI Dummy Node Pack

![License](https://img.shields.io/badge/License-MIT-green.svg) ![Platform](https://img.shields.io/badge/Platform-ComfyUI-blue)

[Español](README.md) | [English](docs/README_EN.md) | [Deutsch](docs/README_DE.md) | [Русский](docs/README_RU.md) | [中文](docs/README_CN.md) | [日本語](docs/README_JP.md)

---

**Recupera el control de tus Workflows.**

Este paquete de nodos personalizados crea "Nodos Fake" (simulados) para reemplazar aquellos nodos antiguos, eliminados o específicos de servicios en la nube (como A1111, Cloud, etc.) que impiden cargar un flujo de trabajo en ComfyUI.

> ⚠️ **IMPORTANTE:** Estos nodos **NO procesan imágenes**. Son *placeholders* (marcadores de posición) que permiten cargar el gráfico visualmente sin errores, conservando las conexiones (cables) para que puedas sustituirlos por nodos nativos funcionales.

---

## 🚀 ¿Por qué usar esto?

Cuando cargas un workflow antiguo y te faltan nodos, ComfyUI a menudo rompe la interfaz o impide la ejecución.
Este pack soluciona el problema del "Huevo y la Gallina":
1.  Carga los nodos faltantes como "Dummies".
2.  Te permite ver dónde iban los cables.
3.  Te da la oportunidad de conectar nodos nativos (`Load Checkpoint`, `KSampler`, etc.).
4.  Una vez reparado, puedes borrar los dummies.

### Ejemplo Visual

![Ejemplo de flujo de trabajo cargado con nodos Dummy (resaltados en rojo), manteniendo las conexiones.](Ejemplo.jpg)
*Ejemplo de flujo de trabajo cargado con nodos Dummy (resaltados en los recuadros rojos), manteniendo las conexiones originales para facilitar su reemplazo.*

---

## 📋 Nodos Soportados Actuales

Si tu flujo pide alguno de estos nodos, este pack lo cargará automáticamente como un nodo 🛑 **DUMMY**.

| Nombre del Nodo Perdido (ID) | Descripción / Uso Original | Solución (Reemplazar con Nativos) |
| :--- | :--- | :--- |
| `ECHOCheckpointLoaderSimple` | Cargador de modelos simple | **Load Checkpoint** |
| `KSampler_A1111` | Sampler estilo Automatic1111 | **KSampler** (Copia los valores seed/steps) |

---

## 🛠️ Instalación

1.  Ve a tu carpeta `ComfyUI/custom_nodes/`.
2.  Clona este repositorio:
    ```bash
    git clone [https://github.com/TU_USUARIO/ComfyUI-Dummy_Node_Pack.git](https://github.com/TU_USUARIO/ComfyUI-Dummy_Node_Pack.git)
    ```
3.  Reinicia ComfyUI.

---

## 🧑‍💻 Guía de Desarrollo: Cómo añadir más nodos

La estructura está diseñada para ser **modular**. Si descargas un flujo nuevo y te falta un nodo diferente (ej. `SuperUpscaler`), sigue estos pasos para añadirlo a tu pack local:

### Paso 1: Definir el Nodo
Abre el archivo `nodes.py`. Copia la plantilla del final y adáptala. Lo importante es definir los `INPUT_TYPES` para que coincidan con los cables que necesitas rescatar.

```python
# En nodes.py
class Fake_SuperUpscaler:
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        # Define aquí las entradas que tenía el nodo original
        return {"required": { "image": ("IMAGE",), "scale": ("FLOAT", {"default": 1.5}) }}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "do_nothing"
    CATEGORY = "Dummy Pack"

    def do_nothing(self, **kwargs): return (None,)
```

### Paso 2: Registrar el Nodo
Abre el archivo __init__.py, importa tu nueva clase y añádela al mapeo:

```python
# En __init__.py
from .nodes import Fake_ECHOCheckpointLoaderSimple, Fake_KSampler_A1111, Fake_SuperUpscaler # <--- 1. Importar

NODE_CLASS_MAPPINGS = {
    "ECHOCheckpointLoaderSimple": Fake_ECHOCheckpointLoaderSimple,
    "KSampler_A1111": Fake_KSampler_A1111,
    "SuperUpscaler": Fake_SuperUpscaler # <--- 2. Mapear el nombre exacto que falta
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SuperUpscaler": "🛑 DUMMY SuperUpscaler" # <--- 3. Nombre visible en UI
}
```

### Paso 3: Aplicar
Reinicia ComfyUI y carga tu flujo. ¡Listo!

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Eres libre de usarlo, modificarlo y compartirlo.

