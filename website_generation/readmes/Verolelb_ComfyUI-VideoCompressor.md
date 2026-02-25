\# ComfyUI Video Compressor Node



Un node personnalisé pour ComfyUI qui permet de compresser des fichiers vidéo en utilisant FFmpeg, en visant une taille de fichier cible spécifique.



&nbsp;<!-- Mettez une capture d'écran ici ! -->



\## 🌟 Fonctionnalités



\-   \*\*Entrée Vidéo Simple\*\* : Prend en entrée un chemin vers un fichier vidéo (parfait pour être chaîné après un node "Video Combine").

\-   \*\*Contrôle de la Taille\*\* : Un slider simple pour définir le poids final souhaité de la vidéo en Mégaoctets (MB).

\-   \*\*Choix du Codec\*\* : Choisissez entre `libx264` (H.264, très compatible) et `libx265` (H.265/HEVC, plus efficace).

\-   \*\*Sortie Organisée\*\* : Les vidéos compressées sont sauvegardées dans `ComfyUI/output/compressed\_videos/`.



\## ⚙️ Installation



\### 1. Prérequis : FFmpeg



\*\*Ce node nécessite que FFmpeg soit installé sur votre système et accessible depuis le terminal.\*\*



\-   \*\*Windows\*\* : Téléchargez depuis \[gyan.dev](https://www.gyan.dev/ffmpeg/builds/) et suivez un tutoriel pour ajouter le dossier `bin` à votre variable d'environnement PATH.

\-   \*\*MacOS\*\* : Installez avec Homebrew : `brew install ffmpeg`

\-   \*\*Linux\*\* : Utilisez votre gestionnaire de paquets : `sudo apt update \&\& sudo apt install ffmpeg`



Pour vérifier que l'installation a réussi, ouvrez un terminal et tapez `ffmpeg -version`. Vous devriez voir les informations de version s'afficher.



\### 2. Installation du Node



La méthode la plus simple est d'utiliser `git`.



1\.  Ouvrez un terminal.

2\.  Naviguez jusqu'au répertoire des nodes personnalisés de ComfyUI : `cd ComfyUI/custom\_nodes/`

3\.  Clonez ce dépôt : `git clone https://github.com/VOTRE\_NOM\_UTILISATEUR/ComfyUI-VideoCompressor.git` <!-- REMPLACEZ PAR VOTRE URL GITHUB -->

4\.  Redémarrez ComfyUI.



Le node devrait maintenant apparaître dans le menu "Add Node" sous la catégorie `🎥Video Utils`.



\## 🚀 Utilisation



1\.  Générez une séquence d'images et combinez-les en une vidéo avec un node comme "Video Combine".

2\.  Connectez la sortie `video` (le chemin du fichier) de ce node à l'entrée `video` du node `🎬 Compress Video (FFmpeg)`.

3\.  Ajustez le slider `target\_mb` à la taille désirée (par ex. 8 MB pour Discord).

4\.  Lancez le workflow. La vidéo compressée sera disponible à la sortie `compressed\_video\_path` et sera enregistrée sur votre disque.



\## 📄 Licence



Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

