# 🎬 ComfyUI-Gemini-VAE-Fix (Universal Smart VAE Decode)

![Version](https://img.shields.io/badge/Version-6.0.0-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Category](https://img.shields.io/badge/Category-Latent/Video-red)

**Najbardziej zaawansowany i precyzyjny węzeł (node) do dekodowania VAE w ComfyUI, stworzony we współpracy człowieka z wieloma modelami AI (Gemini, Claude, Grok).**

## 🌟 Dlaczego ten Node?

Standardowe dekodery VAE często borykają się z dwoma problemami:
1. **OOM (Out of Memory):** Wybuchają przy próbie dekodowania długich filmów w wysokiej rozdzielczości.
2. **Audio Desync (Błąd Płotu):** Przy dekodowaniu kawałkami (chunking), większość implementacji gubi lub dodaje klatki na łączeniach, co powoduje rozjeżdżanie się obrazu z dźwiękiem.

Ten projekt naprawia oba te problemy dzięki **matematycznej precyzji** i **dynamicznemu zarządzaniu zasobami**.

## 🚀 Kluczowe Funkcje

### 1. 🎵 Audio Sync Fix (Gemini Precision)
W przeciwieństwie do innych rozwiązań, nasz algorytm eliminuje tzw. **Fencepost Error**. Dzięki precyzyjnemu obliczaniu "valid core" każdego kawałka wideo, finalna liczba klatek zawsze zgadza się z osią czasu audio. Co do jednej klatki.

### 2. 🛡️ Tryb "God Mode" (Crash-Proof)
Node posiada trzystopniowy system ratunkowy w przypadku braku pamięci VRAM:
* **Stage 1:** Automatyczne włączenie Tilingu (dzielenie obrazu na płytki).
* **Stage 2:** Dynamiczne zmniejszanie Batchu (ilości klatek procesowanych naraz).
* **Stage 3:** Zmniejszanie rozmiaru kafelka (Tile Size).
*Wszystko to dzieje się w locie, bez przerywania Twojego workflow.*

### 3. 🧠 Inteligentna Autodetekcja (Temporal Scale)
Node automatycznie wykrywa, czy używasz modelu wideo wymagającego skalowania czasowego (np. **LTX-Video** (8x) czy **CogVideoX** (4x)), wykonując mikro-testy na pierwszych klatkach.

## 🛠️ Instalacja

1. Wejdź do folderu `custom_nodes` w swoim ComfyUI:
   ```bash
   cd ComfyUI/custom_nodes
   git clone [https://github.com/uczensokratesa/ComfyUI-Gemini-VAE-Fix](https://github.com/uczensokratesa/ComfyUI-Gemini-VAE-Fix)
   Zrestartuj ComfyUI.
   
###   ⚙️ Parametry
   
   Parametr,Opis
frames_per_batch,"Docelowa liczba klatek w jednym cyklu. Im więcej, tym szybciej (ale więcej VRAM)."
overlap_frames,Zakładka między kawałkami dla płynnych przejść (zalecane: 2).
force_time_scale,"Ręczne wymuszenie skali (0 = Auto). Ustaw 8 dla LTX, 1 dla SVD/AnimateDiff."
enable_tiling,Ręczne włączenie tilingu (node i tak włączy go sam przy OOM).
### 🤝 Historia powstania (AI Ensemble)
Ten projekt jest unikalny – powstał jako proces iteracyjny prowadzony przez użytkownika z udziałem trzech modeli AI:

Claude: Zadbał o architekturę i stabilność produkcji.

Grok: Wprowadził innowacyjne dynamiczne pętle i systemy odzyskiwania VRAM.

Gemini (Pro): Wykrył krytyczny błąd matematyczny w synchronizacji audio i dostarczył ostateczną poprawkę "Audio Sync".


   
