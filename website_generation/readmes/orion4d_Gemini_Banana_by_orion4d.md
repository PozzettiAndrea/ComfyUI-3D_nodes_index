# 🍌 Gemini Nano Banana for ComfyUI
<img width="1270" height="1255" alt="image" src="https://github.com/user-attachments/assets/e4f3f93f-692d-4dc0-9223-758635e2c6e4" />
<img width="1572" height="1067" alt="image" src="https://github.com/user-attachments/assets/afaccacc-3e77-4b47-b6ec-afcb97ecfe51" />
<img width="1963" height="668" alt="image" src="https://github.com/user-attachments/assets/e35b2b8e-4bbe-4661-90e5-c32140de13c4" />
<img width="1358" height="969" alt="image" src="https://github.com/user-attachments/assets/8b9c74e9-0185-45e0-a67e-72359f118cb3" />
<img width="866" height="885" alt="image" src="https://github.com/user-attachments/assets/7e31cffb-dbc4-4404-b62a-7362f3fd364f" />

Ce projet est un custom node pour [ComfyUI](https://github.com/comfyanonymous/ComfyUI) qui intègre la puissance de l'API **Google Gemini 2.5 Flash Image ("Nano Banana")**.  
Il fournit un node unique et polyvalent, le **Gemini Nano Banana**, qui permet de réaliser des opérations de génération et d'édition d'images directement dans vos workflows.

👉 [Open the Nano Banana Prompt Guide](https://orion4d.github.io/Gemini_Banana_by_orion4d/nano_banana_prompt_guide_en.html)

---

## ✨ Caractéristiques

- **Node Universel** : Un seul node pour gouverner toutes les tâches !
  - **Text-to-Image** : Générez des images à partir d'un simple prompt texte.
  - **Image-to-Image** : Transformez une image existante en suivant vos instructions.
  - **Fusion Multi-Image** : Envoyez jusqu'à 4 images pour des opérations de fusion, de mélange de styles ou de composition complexes.
- **Sécurité de la Clé API** : Votre clé API est lue depuis un fichier local `apikey.txt` et n'est **jamais** sauvegardée dans les métadonnées de vos images ou les fichiers de workflow, garantissant un partage sécurisé.
- **Upscaler Intégré** : Améliorez la qualité de vos générations directement à la sortie du node en utilisant vos modèles d'upscale ComfyUI préférés (ESRGAN, etc.).
- **Sortie Texte** : En plus de l'image, le node fournit une sortie texte pour afficher les réponses ou les messages du modèle Gemini, facilitant le débogage et le prompt engineering.

---

## 🚀 Installation

### 1. Prérequis

Assurez-vous d'avoir ComfyUI à jour. Ce node nécessite la librairie Python de Google.

Ouvrez un terminal, naviguez jusqu'à votre dossier **ComfyUI**, activez votre environnement virtuel (`venv`) et lancez la commande suivante :

```bash
pip install google-generativeai opencv-python
```

---

### 2. Installation du Node

**Méthode avec Git :**  
Naviguez dans votre dossier `ComfyUI/custom_nodes/` et clonez ce dépôt :

```bash
git clone https://github.com/orion4d/Gemini_Banana_by_orion4d.git
```

**Méthode Manuelle :**  
Téléchargez ce projet en tant que fichier ZIP et extrayez-le dans votre dossier `ComfyUI/custom_nodes/`.

---

### 3. Configuration de la Clé API (Très Important !)

Ce node utilise un fichier local pour stocker votre clé API de manière sécurisée.

1. Allez dans le dossier du node : `ComfyUI/custom_nodes/ComfyUI_Gemini_Nano/`.
2. Créez un nouveau fichier texte nommé `apikey.txt`.
3. Ouvrez ce fichier et collez-y **votre clé API Google**, et rien d'autre.
4. Sauvegardez le fichier.

---

### 4. Redémarrage

Redémarrez **ComfyUI** pour que le nouveau node soit chargé.

---

## 🎨 Utilisation

Une fois installé, vous trouverez le node **« 🍌 Gemini Nano Studio »** dans la catégorie **« Gemini Banana »**.

### Mode Text-to-Image

Pour générer une image à partir de texte, **ne connectez aucune image aux entrées**.  
Écrivez simplement votre prompt.

---

### Mode Image-to-Image / Fusion

Connectez une ou plusieurs images pour les éditer ou les combiner.

- **Édition simple** : Connectez une image à `image1` et décrivez la modification dans le prompt.
- **Fusion** : Connectez plusieurs images et décrivez comment les fusionner.

---

## 🔧 Dépannage

- **Erreur 429 (Quota Exceeded)** : Vous avez fait trop de requêtes à l'API trop rapidement. Attendez 2-3 minutes avant de relancer une génération.
- **Node non trouvé** : Assurez-vous d'avoir bien redémarré ComfyUI après l'installation.
- **Erreur « Fichier `apikey.txt` non trouvé »** : Vérifiez que le fichier `apikey.txt` est bien présent à la racine du dossier du node et qu'il n'est pas vide.
- **Note à propos de l'upscale : le coefficient multiplicateur s'applique si le modèle est sur "none", sinon ce sera en fonction du modèle d'upscale choisi (certains sont en 8x d'autres en 2x)
---
<div align="center">

<h3>🌟 <strong>Show Your Support</strong></h3>
<p>If this project helped you, please consider giving it a ⭐ on GitHub!</p>
<p><strong>Made with ❤️ for the ComfyUI community</strong></p>
<p><strong>by Orion4D</strong></p>
<a href="https://ko-fi.com/orion4d">
<img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Buy Me A Coffee" height="41" width="174">
</a>

</div>
