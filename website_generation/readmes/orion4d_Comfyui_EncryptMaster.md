# 🔐 ComfyUI EncryptMaster
<img width="1179" height="1199" alt="image" src="https://github.com/user-attachments/assets/22ee167a-70f0-4e8f-ba3a-0ea84db16bb9" />

Pack **ComfyUI** de nœuds pour **chiffrer** et **cacher** du texte ou des images.  

Sécurité : **AES-256-GCM** (authentifié) avec dérivation de clé **scrypt**.  
Stéganographie : **LSB** (PNG/TIFF) et **DCT/JPEG** (plus robuste aux recompressions).

---

## 📁 Contenu

Dossier : `ComfyUI/custom_nodes/Comfyui_EncryptMaster/`

- `text_cipher.py` — Text Cipher (chiffrer/déchiffrer une chaîne)
- `stego_text.py` — Stego Text (cacher/extraire du texte dans une image, LSB)
- `stego_capacity.py` — Stego Capacity Estimator (capacité d’une image en LSB)
- `image_cipher.py` — Image ⇄ Noise (image chiffrée rendue comme “bruit”)
- `stego_image_in_image.py` — Stego Image-in-Image (cacher une image dans une autre, compression avant chiffrement)
- `generate_passphrase.py` — Generate Passphrase (phrases de passe solides)

---

## ⚙️ Installation

1) Copier ce dépôt dans :

    ComfyUI/custom_nodes/Comfyui_EncryptMaster

2) Activer votre venv puis installer les dépendances :

    pip install cryptography pillow numpy

3) Relancer ComfyUI. Les nœuds « EncryptMaster — … » apparaissent dans la recherche.

Testé avec Python 3.10–3.12, ComfyUI ≥ 0.3.x, Windows / Linux.

---

## 🔑 Sécurité (résumé)

- **Chiffrement** : AES-256-GCM (authentifié).  
- **Dérivation** : scrypt (N=2^14, r=8, p=1) depuis une passphrase humaine.  
- **Associated Data (AAD)** : champ `associated_data` optionnel, non chiffré mais **authentifié**.  
  Si l’AAD ne correspond pas entre chiffrement et déchiffrement, le déchiffrement échoue.

---

## 🧩 Nœuds et usages
<img width="1192" height="1070" alt="image" src="https://github.com/user-attachments/assets/1f7f6853-1889-43bf-be98-0bbed14ca8e1" />
<img width="1376" height="1090" alt="image" src="https://github.com/user-attachments/assets/2918824f-6b16-4985-a9dd-7abd59f3ad0d" />
<img width="1079" height="808" alt="image" src="https://github.com/user-attachments/assets/c906c726-3b58-4205-aa21-9598bd59c49a" />
<img width="1928" height="1190" alt="image" src="https://github.com/user-attachments/assets/279a5fd7-641e-4e00-b637-2d60f5e1c3f2" />
<img width="1574" height="1030" alt="image" src="https://github.com/user-attachments/assets/023788a7-6d6d-4b64-b42a-c9677eea5647" />
<img width="1879" height="932" alt="image" src="https://github.com/user-attachments/assets/35d1ba84-9a68-4fa3-b815-e8db7d51e483" />

### 1) EncryptMaster — Text Cipher (AES-GCM)

- **Entrées**
  - `text` (STRING) : texte clair ou blob chiffré.
  - `passphrase` (STRING) : mot/phrase de passe.
  - `mode` (STRING) : "encrypt" ou "decrypt".
  - `associated_data` (STRING, optionnel).

- **Sorties**
  - `text` (STRING) : texte chiffré « armored » ou texte déchiffré.

- **Notes**
  - Parfait pour sécuriser prompts, JSON ou credentials avant stockage.

---

### 2) EncryptMaster — Stego Embed Text (AES-GCM) / Stego Extract Text

- **But** : cacher un texte chiffré dans les **bits de poids faible (LSB)** d’une image.

- **Entrées (Embed)**
  - `image` (IMAGE), `text` (STRING), `passphrase` (STRING)
  - `bits_per_channel` : 1 (discret) ou 2 (×2 capacité)
  - `associated_data` (STRING, optionnel)

- **Sorties (Embed)**
  - `image` (IMAGE) : même visuel, message caché.

- **Entrées (Extract)**
  - `image` (IMAGE), `passphrase` (STRING), `associated_data` (STRING, optionnel)

- **Sorties (Extract)**
  - `text` (STRING) : texte en clair.

- **Conseils**
  - Sauvegarder en **PNG/TIFF** (sans perte).  
  - Éviter toute recompression/redimensionnement après l’embed.

---

### 3) EncryptMaster — Stego Capacity Estimator

- **But** : estimer la **capacité maximale** (octets et nombre de caractères) d’une image pour l’embed LSB.

- **Entrées**
  - `image` (IMAGE), `bits_per_channel` (1/2)

- **Sorties**
  - `capacity_bytes` (INT), `capacity_chars` (INT), `report` (STRING)

- **Rappel rapide**
  - Capacité brute ≈ `largeur × hauteur × 3 × bpc / 8` octets.

---

### 4) EncryptMaster — Image Cipher → Noise (AES-GCM)  
###    EncryptMaster — Image Decipher ← Noise (AES-GCM)
- **But** : chiffrer **tous les pixels** d’une image et produire une image de **bruit aléatoire** (réversible).

- **Entrées (Cipher)**
  - `image` (IMAGE), `passphrase` (STRING)
  - `associated_data` (STRING, optionnel)
  - `preserve_width` (BOOLEAN) : conserve la largeur; la hauteur s’ajuste si nécessaire.

- **Sorties (Cipher)**
  - `image` (IMAGE bruitée), `out_width` (INT), `out_height` (INT)

- **Entrées (Decipher)**
  - `image` (IMAGE bruitée), `passphrase` (STRING), `associated_data` (STRING, optionnel)

- **Sorties (Decipher)**
  - `image` (IMAGE originale), `report` (STRING)

- **Important**
  - Toujours **sauver en PNG/TIFF**. Le JPEG détruit des octets → déchiffrement impossible.

---

### 5) EncryptMaster — Stego Embed Image (LSB/AES-GCM) / Stego Extract Image

- **But** : cacher une **image secrète** B dans une **image porteuse** A (LSB), en **compressant** le secret **avant chiffrement**.

- **Entrées (Embed)**
  - `cover_image` (IMAGE), `secret_image` (IMAGE), `passphrase` (STRING)
  - `bits_per_channel` : 1 ou 2
  - `secret_encode` : "jpeg" (recommandé) ou "png"
  - `jpeg_quality` (50–95) : qualité du secret si "jpeg"
  - `resize_secret_to_cover` (BOOLEAN) : redimensionner le secret à la cover
  - `associated_data` (STRING, optionnel)

- **Sorties (Embed)**
  - `image` (IMAGE), `report` (STRING)

- **Entrées (Extract)**
  - `image` (IMAGE), `passphrase` (STRING), `associated_data` (STRING, optionnel)

- **Sorties (Extract)**
  - `image` (secret reconstruit), `report` (STRING)

- **Capacité (ordre de grandeur)**
  - Cover 1216×1600 @ 1 bpc ≈ ~712 KiB ; @ 2 bpc ≈ ~1.42 MiB.  
  - Secret 1216×1600 en **JPEG q85** ≈ 200–400 Ko → OK avec 2 bpc.  
  - Mode **PNG** lossless souvent plus volumineux → nécessitera une cover plus grande ou 2 bpc.

- **Format de sortie**
  - Sauver la cover modifiée en **PNG/TIFF** (pas de recompression JPEG après embed).

---

### 6) EncryptMaster — Generate Passphrase

- **But** : générer une phrase de passe robuste (type Diceware).
- **Astuce** : viser ≥ 24 caractères ou 8–9 mots aléatoires.

---

## 🧪 Workflows types

### A) Cacher un texte chiffré dans une image (PNG)

    [Text Box] -> [Text Cipher (encrypt)] -> [Stego Embed Text] -> [Save Image (PNG)]

### B) Cacher une image dans une autre

    [Load Cover] + [Load Secret] -> [Stego Embed Image (secret_encode=jpeg, bpc=2)] -> [Save Image (PNG)]

### C) Chiffrer une image en « bruit » (réversible)

    [Load Image] -> [Image Cipher → Noise] -> [Save Image (PNG)]
    [Load Noise] -> [Image Decipher ← Noise] -> [Preview]
---

## ✅ Bonnes pratiques

- Utiliser **Generate Passphrase** pour des passphrases solides.  
- Renseigner un **`associated_data`** stable (ex. `project=EncryptMaster;v=1`) et le réutiliser à l’extraction.  
- Ne pas compresser les images codées, format export png ou tiff, ne pas réenregister les images en jpeg, beaucoup de réseaux sociaux réencodent les images (cryptage infonctionnel).

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

