## 📦 Package : **ComfyUI_FMJ_LLM**
> **Auteur** : FMJ  
> **Description** : Nœuds avancés pour l’interaction avec **Ollama** (texte, vision, édition d’image), avec gestion dynamique des prompts via CSV.
<img width="1163" height="1209" alt="Capture d’écran du 2025-11-10 13-50-10" src="https://github.com/user-attachments/assets/91e2b3b6-f1b8-42bb-829c-d06b63daa545" />
# 🧠 **ComfyUI FMJ LLM** — Intégration Ollama native dans ComfyUI

> **Générez, améliorez, analysez et décrivez vos prompts avec l’IA locale — directement dans ComfyUI.**

Ce pack de nœuds personnalisés permet d’**intégrer Ollama** (modèles comme `llama3`, `qwen3`, `moondream`, `llava`, etc.) **directement dans vos workflows ComfyUI**, sans dépendance externe ni service cloud. Tout reste **100 % local**.

---

## 🌟 Fonctionnalités principales

### 🔹 1. **Génération de prompts textuels avancés** (`🦙FMJ Ollama Prompt Generator`)
Générez des réponses avancées à partir de n’importe quel modèle Ollama (notamment **Qwen3**, Llama 3.2, Mistral, etc.) en combinant un **texte d’entrée** avec un **prompt système personnalisé** chargé depuis un fichier CSV ou saisi manuellement. Idéal pour automatiser des tâches comme la réécriture, le résumé, la traduction, l’analyse de texte, ou toute interaction structurée avec un LLM.

> ✅ Compatible avec tous les modèles **chat-based** via l’endpoint `/api/chat` d’Ollama  
> ✅ Optimisé pour **Qwen3** (y compris les modèles *thinking models*)  
> ✅ Supporte les prompts système dynamiques via CSV  
> ✅ Intégration transparente dans **ComfyUI**

---

## 📥 Entrées

| Nom | Type | Description |
|-----|------|-------------|
| **`text`** *(obligatoire)* | `STRING` | Le texte à traiter par le modèle (ex: un paragraphe à résumer, une phrase à corriger, une question à répondre). Doit être connecté depuis un nœud en amont. |
| **`prompt_style`** | `LIST` | Sélectionnez un style de prompt prédéfini depuis vos fichiers CSV (dossier `csv/`). Chaque style correspond à une instruction système spécifique (ex: "résumé", "correction", "création de scénario"). |
| **`model_name`** | `STRING` | Nom du modèle Ollama à utiliser. Ex: `qwen3:2b`, `llama3.2`, `mistral`, `phi3`, etc. **Doit être présent localement** (`ollama list`). |
| **`ollama_url`** | `STRING` | URL de l’API Ollama. Par défaut : `http://localhost:11434`. Modifiez si Ollama tourne sur une autre machine ou un port personnalisé. |
| **`max_tokens`** | `INT` | Nombre maximum de tokens à générer. Valeur typique : `256` à `2048`. Pour Qwen3, des valeurs élevées (jusqu’à `16384`) sont possibles. |
| **`temperature`** | `FLOAT` | Contrôle la créativité de la réponse. `0.0` = déterministe, `0.7` = équilibré, `1.0+` = très créatif. |
| **`seed`** | `INT` | Graine aléatoire pour la reproductibilité. `0` = aléatoire à chaque appel. |
| **`keep_alive`** | `INT` | Durée (en minutes) pendant laquelle le modèle reste en mémoire après utilisation. `-1` = toujours chargé, `0` = décharger immédiatement. |
| **`request_timeout`** | `INT` | **(Nouveau)** Délai maximal d’attente (en secondes) avant d’abandonner la requête. **Crucial pour Qwen3** (mode raisonnement lent). Valeur recommandée : `300` (5 min). |
| **`override_prompt`** *(facultatif)* | `STRING` | Remplace entièrement le prompt système sélectionné. Si ce champ n’est **pas vide**, il ignore `prompt_style`. Utile pour des instructions ponctuelles. |
| **`disable_thinking`** *(facultatif)* | `BOOLEAN` | **(Nouveau)** Si activé (**ON**), désactive la trace de raisonnement intermédiaire de Qwen3 (`think: false`). **Recommandé** pour obtenir une réponse directe sans balises `<think>...<think>`. |

---

## 📤 Sorties

| Nom | Type | Description |
|-----|------|-------------|
| **`response`** | `STRING` | La réponse générée par le modèle, prête à être utilisée dans d’autres nœuds (ex: sauvegarde, affichage, traitement ultérieur). |
| **`debug_info`** | `STRING` | Informations de débogage : statut, modèle utilisé, timeout, style de prompt. Utile pour diagnostiquer les erreurs (ex: réponse vide, modèle non trouvé, timeout). |

---

## 📁 Configuration : Fichiers CSV

Le nœud charge automatiquement **tous les fichiers `.csv`** dans le sous-dossier `csv/` situé **au même niveau que ce script**.

Chaque fichier CSV doit avoir **exactement deux colonnes** :

- `prompt_style` : nom unique du style (affiché dans le menu déroulant)
- `system_prompt` : instruction système complète envoyée au LLM

### Exemple de fichier : `csv/writing_prompts.csv`

```csv
prompt_style,system_prompt
qwen_edit,Tu es un éditeur expert. Corrige, améliore et reformule le texte suivant pour plus de clarté, de fluidité et de professionnalisme. Ne rajoute rien.
qwen_summary,Résume le texte suivant en 2-3 phrases maximum, en français, en conservant les idées essentielles.
creative_story,Écris une courte histoire créative (50 mots) basée sur le thème suivant :
```

> 💡 Ajoutez autant de fichiers CSV que vous voulez (`seo.csv`, `code.csv`, etc.). Le nœud les fusionne automatiquement.

---

## ⚠️ Remarques importantes

- **Qwen3 est lent** : Augmentez `request_timeout` si vous obtenez des erreurs de timeout.
- **Pas de réponse ?** Vérifiez :
  1. Que le modèle est bien installé (`ollama list`)
  2. Que le CSV contient bien le `prompt_style` sélectionné
  3. Que `disable_thinking` est **activé** (**ON**) pour éviter les sorties vides dues au parsing de `<think>`
- **Le nœud utilise `/api/chat`**, pas `/api/generate` → il **ne fonctionne pas avec des modèles non-chat** (ex: anciens modèles GGUF sans template de chat).

---

## 🧪 Exemple d’utilisation dans ComfyUI

1. Connectez un nœud **Text** à `text`.
2. Sélectionnez `qwen_edit` dans `prompt_style`.
3. Laissez `model_name = qwen3:2b`.
4. Activez `disable_thinking = ON`.
5. Réglez `request_timeout = 300`.
6. La sortie `response` contiendra le texte édité par Qwen3.

---
---

### 🔹 2. **Analyse d’image par IA vision** (`👁️ FMJ Llm Ollama Vision`)

Analysez des images avec des modèles multimodaux d’Ollama (**Qwen3-VL**, Llava, BakLLaVA, etc.) en combinant une **image d’entrée** avec une **instruction système personnalisée** chargée depuis un fichier CSV ou saisie manuellement. Générez des descriptions détaillées, du texte alternatif, des analyses artistiques, ou toute autre interprétation visuelle pilotée par LLM.

> ✅ Compatible avec tous les modèles **multimodaux via `/api/chat`**  
> ✅ Optimisé pour **Qwen3-VL** (y compris son *mode raisonnement*)  
> ✅ Supporte les instructions système dynamiques via CSV  
> ✅ Intégration transparente dans **ComfyUI**

---

## 📥 Entrées

| Nom | Type | Description |
|-----|------|-------------|
| **`image`** *(obligatoire)* | `IMAGE` | L’image à analyser, provenant d’un nœud d’image en amont (ex: Load Image, KSampler, etc.). |
| **`description_type`** | `LIST` | Sélectionnez un type d’analyse prédéfini depuis vos fichiers CSV (dossier `csvv/`). Chaque type correspond à une instruction système spécifique (ex: "description détaillée", "texte alternatif"). |
| **`model_name`** | `STRING` | Nom du modèle multimodal Ollama. Ex: `qwen3-vl:2b`, `llava`, `bakllava`, etc. **Doit être installé localement** (`ollama list`). |
| **`ollama_url`** | `STRING` | URL de l’API Ollama. Par défaut : `http://localhost:11434`. Modifiez en cas d’hébergement distant. |
| **`max_tokens`** | `INT` | Nombre maximum de tokens à générer. Valeur typique : `256–1024`. Qwen3-VL supporte jusqu’à `16384`. |
| **`temperature`** | `FLOAT` | Contrôle la créativité. `0.0` = déterministe, `0.7` = équilibré. |
| **`seed`** | `INT` | Graine aléatoire pour la reproductibilité. `0` = aléatoire. |
| **`keep_alive`** | `INT` | Durée (en minutes) de mise en cache du modèle. `-1` = toujours en mémoire, `0` = décharger après usage. |
| **`request_timeout`** | `INT` | **(Nouveau)** Délai maximal d’attente (en secondes). **Très important pour Qwen3-VL** (peut être lent). Valeur recommandée : `300` (5 min). |
| **`override_prompt`** *(facultatif)* | `STRING` | Remplace l’instruction système sélectionnée. Si non vide, ignore `description_type`. |
| **`disable_thinking`** *(facultatif)* | `BOOLEAN` | **(Nouveau)** Si **ON**, désactive la trace de raisonnement de Qwen3-VL (`think: false`). **Fortement recommandé** pour obtenir une réponse directe sans balises `\<think>`. |

---

## 📤 Sorties

| Nom | Type | Description |
|-----|------|-------------|
| **`description`** | `STRING` | Le texte généré par le modèle à partir de l’image et de l’instruction. Prêt pour affichage, sauvegarde ou traitement ultérieur. |
| **`debug_info`** | `STRING` | Informations de diagnostic : statut, modèle utilisé, type d’analyse, timeout. Utile en cas d’erreur ou de réponse vide. |

---

## 📁 Configuration : Fichiers CSV

Le nœud charge automatiquement tous les fichiers `.csv` du sous-dossier **`csvv/`** situé au même niveau que ce script.

Chaque fichier doit contenir **exactement deux colonnes** :

- `description_type` : nom du type d’analyse (affiché dans le menu déroulant)
- `system_prompt` : instruction système complète pour guider l’analyse visuelle

### Exemple : `csvv/vision_prompts.csv`

```csv
description_type,system_prompt
detailed_vision,Donne une description détaillée, objective et complète de l'image. Mentionne les objets, les couleurs, les actions, le contexte et l'humeur.
alt_text,Génère un texte alternatif concis (max 120 caractères) pour l'accessibilité web.
art_analysis,Analyse cette œuvre comme un critique d'art : style, composition, émotion, époque possible.
product_caption,Écris une légende marketing engageante pour ce produit (max 20 mots).
```

> 💡 Vous pouvez créer plusieurs fichiers (`accessibility.csv`, `art.csv`, etc.). Le nœud les fusionne automatiquement.

---

## ⚠️ Remarques importantes

- **Qwen3-VL est lent** : Augmentez `request_timeout` si vous obtenez des erreurs de timeout.
- **Pas de description ?** Vérifiez :
  1. Que le modèle est bien installé (`ollama list`)
  2. Que le fichier CSV contient le `description_type` sélectionné
  3. Que `disable_thinking` est **activé (ON)** — c’est essentiel pour éviter les réponses vides dues au mode *reasoning*.
- Ce nœud utilise **`/api/chat`**, pas `/api/generate` → il **ne fonctionne pas avec des modèles non-chat ou non-multimodaux**.

---

## 🧪 Exemple d’utilisation dans ComfyUI

1. Connectez une image à `image`.
2. Sélectionnez `alt_text` dans `description_type`.
3. Utilisez `model_name = qwen3-vl:2b`.
4. Activez `disable_thinking = ON`.
5. Réglez `request_timeout = 300`.
6. La sortie `description` contiendra un texte alternatif prêt pour le web.

---

---

### 🔹 3. **Gestion centralisée d’Ollama** (`⚙️ FMJ Llm Config`)
- Sélectionnez **l’URL d’Ollama** (par défaut : `http://localhost:11434`)
- Liste **dynamique des modèles installés** → choisissez celui à utiliser
- Branchez la sortie vers les autres nœuds → configuration **unifiée et modulaire**

---

### 🔹 4. **Nettoyage mémoire à la demande** (`🧹 FMJ Unload All LLM`)
- **Décharge tous les modèles** d’Ollama de la mémoire → libère la RAM/VRAM
- Idéal **avant un long workflow** ou pour **changer de modèle lourd**
- Aucun risque de rechargement automatique

---

## 📦 Compatibilité

- ✅ **Ollama ≥ v0.13** (testé sur Linux, Windows)

---

> 💡 **Tout tourne en local.** Vos images, vos prompts, vos données restent **sur votre machine**.
> 💡 **Installer Ollama avant le node. https://ollama.com/
