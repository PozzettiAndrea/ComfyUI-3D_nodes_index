# ComfyUI PDF Nodes

Ce dépôt contient un ensemble de nœuds personnalisés pour [ComfyUI](https://github.com/comfyanonymous/ComfyUI) permettant de charger, manipuler, extraire des informations et prévisualiser des fichiers PDF directement dans vos workflows.

![image](https://github.com/user-attachments/assets/aa87b5b2-751d-47d3-ad65-49199b8c0baf)

![image](https://github.com/user-attachments/assets/786e038b-a0fc-4a97-b943-1e5aee9cabe2)


## Fonctionnalités

*   **Charger des PDF** : Chargez des documents PDF, y compris ceux protégés par mot de passe.
*   **Fusionner des PDF** : Combinez plusieurs listes de pages PDF en une seule.
*   **Sélectionner et Extraire du Texte** : Sélectionnez une page spécifique et extrayez son contenu textuel.
*   **Extraire du Texte de Plusieurs Pages** : Extrayez le texte d'une sélection de pages (ex: "1,3-5,all").
*   **Obtenir le Nombre de Pages** : Récupérez le nombre total de pages d'un document PDF chargé.
*   **Rotation de Pages** : Faites pivoter les pages sélectionnées par incréments de 90 degrés.
*   **Prévisualisation d'une Page PDF** : Rendez une page PDF spécifique en tant qu'image pour la prévisualiser dans ComfyUI.
*   **Convertir des Pages PDF en Images (Batch)** : Rendez une sélection de pages PDF en un batch d'images. Seules les pages ayant des dimensions identiques (après rendu au DPI spécifié) seront incluses dans le batch.
*   **Sauvegarder en PDF** : Enregistrez les pages PDF manipulées dans un nouveau fichier PDF.

## Installation

1.  **Cloner le dépôt** :
    Naviguez jusqu'au dossier `custom_nodes` de votre installation ComfyUI et clonez ce dépôt :
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/orion4d/ComfyUI_pdf_nodes.git
    ```

2.  **Installer les dépendances** :
    Ces nœuds nécessitent des bibliothèques Python spécifiques. Assurez-vous qu'elles sont installées dans l'environnement Python utilisé par ComfyUI.
    
    Activez votre environnement virtuel ComfyUI (si vous en utilisez un), puis naviguez dans le dossier des nœuds clonés et installez les dépendances :
    ```bash
    cd comfyui_pdf_nodes 
    pip install -r requirements.txt
    ```
    Si vous préférez, vous pouvez aussi installer les paquets individuellement :
    ```bash
    pip install pypdf PyMuPDF Pillow
    ```

3.  **Redémarrer ComfyUI** :
    Après l'installation, redémarrez ComfyUI. Les nouveaux nœuds devraient apparaître dans la catégorie "PDF" du menu d'ajout de nœuds.

## Nœuds Disponibles

Voici une description de chaque nœud et de ses principales entrées/sorties.

---

### 📄 Load PDF (`PDFLoad`)
Charge un fichier PDF à partir d'un chemin spécifié.
*   **Entrées** :
    *   `pdf_path` (STRING) : Chemin vers le fichier PDF.
    *   `password` (STRING, optionnel) : Mot de passe si le PDF est chiffré.
*   **Sorties** :
    *   `pdf_pages` (PDF_PAGES) : Une liste d'objets page du PDF.
    *   `page_count` (INT) : Le nombre total de pages dans le PDF.

---

### ➕📄 Merge PDFs (`PDFMerge`)
Fusionne deux listes de pages PDF.
*   **Entrées** :
    *   `pdf_pages_a` (PDF_PAGES) : Première liste de pages.
    *   `pdf_pages_b` (PDF_PAGES) : Deuxième liste de pages.
*   **Sorties** :
    *   `pdf_pages` (PDF_PAGES) : Liste combinée des pages.

---

### 🎯📄 Select Page & Extract Text (`PDFSelectPageAndExtractText`)
Sélectionne une seule page par son index (0-indexé) et extrait son texte.
*   **Entrées** :
    *   `pdf_pages` (PDF_PAGES) : La liste des pages PDF.
    *   `page_index` (INT) : L'index de la page à sélectionner.
*   **Sorties** :
    *   `selected_page_as_pdf_pages` (PDF_PAGES) : Une liste contenant uniquement la page sélectionnée.
    *   `extracted_text` (STRING) : Le texte extrait de la page sélectionnée.

---

### 🔍📄 Extract Text from Pages (`PDFExtractTextFromPages`)
Extrait le texte d'une sélection de pages spécifiée par une chaîne de caractères.
*   **Entrées** :
    *   `pdf_pages` (PDF_PAGES) : La liste des pages PDF.
    *   `page_selection` (STRING) : Chaîne de sélection des pages (ex: "1,3-5,all", 1-indexé).
    *   `separator` (STRING, optionnel) : Séparateur à insérer entre le texte de chaque page.
*   **Sorties** :
    *   `STRING` : Le texte combiné des pages sélectionnées.

---

### #️⃣📄 Get PDF Page Count (`PDFGetPageCount`)
Retourne le nombre de pages dans une liste `PDF_PAGES`.
*   **Entrées** :
    *   `pdf_pages` (PDF_PAGES) : La liste des pages PDF.
*   **Sorties** :
    *   `INT` : Le nombre de pages.

---

### 🔄📄 Rotate PDF Pages (`PDFRotatePages`)
Fait pivoter les pages sélectionnées d'un PDF.
*   **Entrées** :
    *   `pdf_pages` (PDF_PAGES) : La liste des pages PDF.
    *   `page_selection` (STRING) : Chaîne de sélection des pages (ex: "1,3-5,all", 1-indexé).
    *   `rotation_angle` (INT) : Angle de rotation (0, 90, 180, 270 degrés).
*   **Sorties** :
    *   `pdf_pages` (PDF_PAGES) : La liste des pages PDF avec les rotations appliquées.

---

### 🖼️📄 Preview PDF Page (Single) (`PDFPreviewPage`)
Rend une seule page PDF en tant qu'image pour prévisualisation. Nécessite `PyMuPDF` et `Pillow`.
*   **Entrées** :
    *   `pdf_pages` (PDF_PAGES) : La liste des pages PDF.
    *   `page_index` (INT) : Index (0-indexé) de la page à prévisualiser.
    *   `dpi` (INT) : Résolution de l'image rendue (points par pouce).
*   **Sorties** :
    *   `IMAGE` : L'image de la page rendue.

---

### 🖼️📄🎞️ PDF Pages to Images (Batch) (`PDFPagesToImages`)
Rend une sélection de pages PDF en un batch d'images. Nécessite `PyMuPDF` et `Pillow`.
*   **Entrées** :
    *   `pdf_pages` (PDF_PAGES) : La liste des pages PDF.
    *   `page_selection` (STRING) : Chaîne de sélection des pages (ex: "1,3-5,all", 1-indexé).
    *   `dpi` (INT) : Résolution des images rendues.
    *   `max_pages_to_render` (INT) : Nombre maximum de pages à inclure dans le batch (limité à 100).
*   **Sorties** :
    *   `IMAGE` : Un batch d'images. Seules les pages ayant des dimensions identiques après rendu seront incluses. Les pages de tailles différentes seront ignorées pour le batch.

---

### 💾📄 Save PDF (`PDFSave`)
Sauvegarde une liste de pages PDF dans un nouveau fichier.
*   **Entrées** :
    *   `pdf_pages` (PDF_PAGES) : La liste des pages PDF à sauvegarder.
    *   `output_directory` (STRING) : Dossier de sortie.
    *   `filename_prefix` (STRING) : Préfixe du nom de fichier.
    *   `overwrite_existing` (STRING: "enable" ou "disable") : Si "disable" et que le fichier existe, un suffixe numérique sera ajouté.
*   **Sorties** :
    *   `saved_pdf_path` (STRING) : Le chemin complet du fichier PDF sauvegardé.

## Utilisation de la Sélection de Pages

Plusieurs nœuds (`Extract Text from Pages`, `Rotate PDF Pages`, `PDF Pages to Images`) utilisent un champ `page_selection` qui accepte une chaîne de caractères pour spécifier les pages (1-indexé) :
*   **Pages individuelles** : `1,3,5` (sélectionne les pages 1, 3 et 5).
*   **Plages de pages** : `2-6` (sélectionne les pages 2, 3, 4, 5 et 6).
*   **Combinaison** : `1,3-5,8` (sélectionne les pages 1, 3, 4, 5 et 8).
*   **Toutes les pages** : `all` ou laisser le champ vide (si c'est la valeur par défaut).

## Problèmes Connus / Limitations

*   Le nœud `PDF Pages to Images (Batch)` ne peut créer un batch qu'avec des images ayant exactement les mêmes dimensions (hauteur, largeur, canaux) après rendu. Les pages PDF de tailles ou d'orientations différentes dans la sélection entraîneront l'exclusion de certaines pages du batch résultant. Un avertissement sera affiché dans la console pour les pages ignorées.
*   La performance pour le rendu de nombreuses pages en images peut varier en fonction de la complexité des PDF et du DPI choisi.

## Contribuer

Les contributions, suggestions et rapports de bugs sont les bienvenus ! N'hésitez pas à ouvrir une "issue" ou une "pull request".

## Licence

Ce projet est sous licence [MIT](LICENSE).

### 🌟 **Soutenez le projet**

Si ce projet vous a été utile, pensez à lui laisser une ⭐ sur GitHub !

**Fait avec ❤️ pour la communauté open source**  
**par Orion4D**

[![Offrez-moi un café](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/orion4d)

</div>

