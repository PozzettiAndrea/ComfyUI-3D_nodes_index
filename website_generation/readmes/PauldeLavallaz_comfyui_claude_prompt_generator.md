# Claude Prompt Generator para ComfyUI

Este nodo personalizado para ComfyUI genera prompts utilizando la API de Anthropic Claude.

## Características

- Genera prompts de alta calidad para generación de imágenes.
- Personaliza el prompt del sistema y la entrada del usuario.
- Integra la API de Anthropic Claude.

## Instalación

Puedes instalar este nodo personalizado de dos maneras:

### A través de ComfyUI Manager

1. Abre ComfyUI Manager.
2. Busca "Claude Prompt Generator" en la lista de nodos disponibles.
3. Haz clic en "Instalar".
4. Reinicia ComfyUI.

### Instalación Manual

1. Clona este repositorio en el directorio `custom_nodes` de tu instalación de ComfyUI:

   ```bash
   cd path/to/ComfyUI/custom_nodes
   git clone https://github.com/tu_usuario/comfyui_claude_prompt_generator.git

Instala las dependencias:

bash
Copy code
pip install -r comfyui_claude_prompt_generator/requirements.txt
Reinicia ComfyUI.

Uso
Obtén una clave API de Anthropic y configúrala como variable de entorno ANTHROPIC_API_KEY, o proporciónala directamente en la entrada del nodo.
En ComfyUI, encuentra el nodo "Claude Prompt Generator" en la categoría "Prompt Generation".
Conecta el nodo en tu flujo de trabajo.
Configura el system_prompt y el user_input según tus necesidades.
Ejecuta el flujo de trabajo.
Configuración de la Clave API
Variable de Entorno: Establece ANTHROPIC_API_KEY en tu entorno.

En Windows (CMD):

cmd
Copy code
set ANTHROPIC_API_KEY=tu_clave_api
En Unix/Linux (bash):

bash
Copy code
export ANTHROPIC_API_KEY=tu_clave_api
Entrada Directa: Puedes proporcionar la clave API directamente en el nodo en el campo api_key.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
