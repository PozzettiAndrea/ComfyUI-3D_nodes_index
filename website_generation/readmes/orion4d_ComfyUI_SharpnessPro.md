# SharpnessPro pour ComfyUI

Une collection de nœuds de haute qualité pour [ComfyUI](https://github.com/comfyanonymous/ComfyUI), dédiée à l'amélioration de la netteté, de la clarté et de la texture de vos images. Inspirés par les outils professionnels de logiciels comme Photoshop ou Lightroom, ces nœuds offrent un contrôle précis pour des résultats nets et sans artefacts.

Le pack est divisé en deux catégories :
*   **SharpnessPro/Sharpen (Netteté)** : Pour l'accentuation des détails fins.
*   **SharpnessPro/Tone (Tonalité)** : Pour l'ajustement du contraste local (Clarté, Texture).

<img width="575" height="1145" alt="image" src="https://github.com/user-attachments/assets/d78a1dab-65e8-4296-883c-8d933c3c61bf" />

## ✨ Installation

### Méthode 1 : Via le ComfyUI-Manager (Recommandé)

1.  Installez le [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) si ce n'est pas déjà fait.
2.  Dans ComfyUI, cliquez sur le bouton "Manager".
3.  Cliquez sur "Install Custom Nodes".
4.  Recherchez "SharpnessPro" et cliquez sur "Install".
5.  Redémarrez ComfyUI.

### Méthode 2 : Manuellement (Git Clone)

1.  Ouvrez un terminal ou une invite de commande.
2.  Naviguez jusqu'au répertoire d'installation de ComfyUI.
3.  Clonez le dépôt dans le dossier `custom_nodes` :
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/orion4d/ComfyUI_SharpnessPro.git
    ```
4.  Redémarrez ComfyUI.

---

## 🎨 Nœuds Incluídos

### Catégorie `SharpnessPro/Sharpen`

#### 🧠 SmartSharpen (Netteté optimisée)

Le nœud le plus avancé du pack. Il applique une netteté intelligente en se basant sur un filtre "edge-aware" (qui préserve les contours) plutôt qu'un simple flou gaussien. Idéal pour un résultat de haute qualité avec un minimum d'artefacts.

-   **`image`** : L'image d'entrée.
-   **`radius`** : Définit la taille des détails à accentuer. Un faible rayon cible les détails très fins.
-   **`amount`** : L'intensité de la netteté.
-   **`reduce_noise`** : Réduit l'amplification du bruit et des micro-détails indésirables. Très utile pour les images bruitées.
-   **`fade_shadows`** : Protège les zones sombres de l'image, évitant le "clipping" (perte de détails) et l'apparition de bruit dans les ombres.
-   **`fade_highlights`** : Protège les zones claires de l'image, évitant les halos et la perte de détails dans les hautes lumières.

**Conseil** : C'est le nœud de netteté à utiliser par défaut pour la plupart des images.

#### 🎭 UnsharpMaskSharpen (Masque flou - USM)

Implémentation du grand classique "Unsharp Mask" (Masque Flou). C'est un algorithme puissant et rapide, qui offre un excellent contrôle.

-   **`radius`** : Rayon du flou utilisé pour détecter les détails.
-   **`amount`** : Intensité de l'accentuation.
-   **`threshold`** : Seuil de contraste. Les détails dont le contraste est inférieur à ce seuil ne seront pas accentués. Augmentez cette valeur pour éviter de rendre le bruit ou le grain de l'image plus visible.
-   **`luma_only`** : Si "Yes", la netteté n'est appliquée qu'à la luminance, ce qui empêche l'apparition de franges colorées sur les contours.

**Conseil** : Utilisez ce nœud lorsque vous avez besoin d'un contrôle précis via le seuil (`threshold`).

#### LAYER HighPassSharpen (Passe-haut)

Une autre technique classique, très populaire dans le monde de la retouche photo. Elle isole les détails de l'image sur une couche grise (passe-haut) et la fusionne avec l'image originale.

-   **`radius`** : Définit la finesse des détails à isoler.
-   **`amount`** : Contrôle le contraste de la couche de détails avant la fusion.
-   **`blend_mode`** :
    -   `Overlay` : Mode de fusion standard, plus contrasté et puissant.
    -   `SoftLight` : Mode de fusion plus doux et subtil.
-   **`opacity`** : Opacité globale de l'effet.
-   **`work_on_luma`** : Si "Yes", la couche de détails est calculée à partir de la luminance uniquement, pour un résultat plus propre.

**Conseil** : Excellent pour un look "photographique" et pour contrôler l'effet via les modes de fusion.

### Catégorie `SharpnessPro/Tone`

#### 💪 Clarity (Clarté)

Ce nœud augmente le **contraste local** dans les tons moyens de l'image, donnant plus de "punch" et de présence à l'image sans affecter les ombres et les hautes lumières. C'est l'équivalent du curseur "Clarté" dans Lightroom.

-   **`radius`** : Utilise un rayon **large** pour cibler les variations de tons locales plutôt que les détails fins.
-   **`strength`** : Intensité de l'effet. Peut être négatif pour adoucir l'image.
-   **`midtone_softness`** : Contrôle la largeur de la plage des tons moyens ciblée. Une valeur plus faible resserre l'effet sur les tons moyens stricts.
-   **`luma_only`** : Applique l'effet sur la luminance pour préserver les couleurs.

**Conseil** : Ne pas confondre avec la netteté. La clarté donne une impression de relief et de profondeur.

#### 🕸️ Texture

Ce nœud accentue ou atténue les **détails très fins** et les textures de surface. C'est l'équivalent du curseur "Texture" dans Lightroom.

-   **`radius`** : Utilise un rayon **faible** pour cibler le micro-contraste.
-   **`strength`** : Intensité de l'effet. Une valeur positive accentue la texture, une valeur négative l'adoucit (effet de lissage de peau léger).
-   **`luma_only`** : Applique l'effet sur la luminance.

**Conseil** : Utilisez une valeur positive pour faire ressortir les détails du tissu, du bois ou de la roche. Utilisez une valeur négative pour adoucir subtilement la peau sur les portraits.

---

## 💡 Philosophie et Conseils d'Utilisation

-   **Différence entre Netteté et Tonalité** : Les nœuds de *Netteté* (`Sharpen`) sont conçus pour l'étape finale et affectent les contours et les détails les plus fins. Les nœuds de *Tonalité* (`Tone`) comme `Clarity` et `Texture` modifient le contraste local et peuvent être utilisés plus tôt dans le workflow pour sculpter la lumière et la matière.
-   **Ordre d'application** : Il est généralement recommandé d'appliquer la netteté (`SmartSharpen`, `USM`, etc.) en toute fin de workflow, juste avant la sauvegarde, pour éviter que les effets ultérieurs n'altèrent le résultat.
-   **Commencez doucement** : Les valeurs par défaut sont un bon point de départ. Il est facile d'en faire trop avec la netteté. Zoomez à 100% pour bien juger de l'effet.

## Licence

Ce projet est distribué sous la licence MIT. Voir le fichier `LICENSE` pour plus de détails.

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

