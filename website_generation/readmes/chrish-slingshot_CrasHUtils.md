# CrasH Utils Custom Nodes

A collection of utility nodes and games for ComfyUI to enhance your workflow and keep you entertained during long generation times!

---

## 🎮 Games Collection

Play games directly in ComfyUI while waiting for image generation! All games run entirely in the browser with no external dependencies.

### Controls (All Games)
- **Click the game canvas** to activate keyboard input
- **Click outside the node** to release keyboard control
- This allows seamless switching between gaming and using ComfyUI

---

### 🐍 Snake Game

Classic Nokia-style snake game with retro green-screen graphics!

**Controls:** Arrow keys or WASD to move, Space to pause/restart

**Features:**
- Authentic Nokia 3210 aesthetic
- Wrap-around edges
- Score tracking
- Game over with instant restart

<img width="356" height="395" alt="image" src="https://github.com/user-attachments/assets/aedee4ce-15ff-433c-a877-35ff7e61da6e" />

---

### 🧱 Tetris Game

Classic block-stacking puzzle game!

**Controls:**
- Arrow Left/Right: Move piece
- Arrow Down: Soft drop
- Arrow Up: Rotate
- Space: Hard drop

**Features:**
- Standard Tetris mechanics
- Score and level progression
- Next piece preview
- Line clear animations

---

### 🦖 Dino Game

Chrome's famous offline dinosaur runner!

**Controls:** Space or Up Arrow to jump

**Features:**
- Endless runner gameplay
- Increasing difficulty
- Obstacle variety
- High score tracking

---

### 👾 Space Invaders

Classic arcade shooter!

**Controls:**
- Arrow Left/Right: Move ship
- Space: Shoot

**Features:**
- Wave-based gameplay
- Multiple enemy types
- Score tracking
- Classic arcade feel

---

### 🔫 DOOM

The legendary FPS - play the full DOOM Shareware in your browser!

#### 🎮 Automatic Setup (Recommended)

**Just add the node** - files download automatically!

- **First time**: Auto-downloads DOOM Shareware v1.9 (~2MB, 30-60 seconds)
- **Multiple sources**: Tries Doomworld, archive.org, and other mirrors automatically
- **After download**: DOOM launches automatically - no setup needed!
- **Legal**: Official free shareware version, completely legal to distribute

#### 📦 Manual Setup (Optional)

If auto-download fails, download manually from any of these sources:

1. **Download DOOM Shareware v1.9:**
   - Doomworld: https://www.doomworld.com/idgames/idstuff/doom/win95/doom19s
   - Archive.org: https://archive.org/details/DoomsharewareEpisode
   - Or search for "DOOM Shareware 1.9"

2. **Extract the files:** Find `DOOM.EXE` and `DOOM1.WAD` (or `DOOM.WAD`)

3. **Place files in:** `ComfyUI/custom_nodes/CrasHUtils/doom/`

4. **Restart:** Restart ComfyUI and refresh your browser

#### 🎹 DOOM Controls

Standard DOOM controls apply - arrow keys to move, Ctrl to shoot, Space to open doors, etc.

#### ⚠️ Troubleshooting

- If keyboard gets stuck: Click outside the node to release control
- If download fails: Try manual setup above
- Check browser console for detailed error messages

---

## 🖼️ Image Processing Nodes

### 🎨 Image Glitcher

Create authentic glitch art effects with chromatic aberration and scanlines!

Based on the HTML image glitcher by Felix Turner ([original demo](https://www.airtightinteractive.com/demos/js/imageglitcher/)).

![image](https://github.com/chrish-slingshot/ComfyUI-ImageGlitcher/assets/117188274/b7b509a4-026e-4b03-98f3-70c10ec54a19)

**Parameters:**
- **glitchiness** (0-100): Controls glitch corruption and chromatic aberration intensity
- **brightness** (0-100): Brightens the image, useful with scanlines enabled
- **scanlines** (toggle): Adds authentic CRT TV scanlines

**Usage:** Simply connect an image input and adjust parameters to taste.

![ComfyUI_temp_cknmh_000362_](https://github.com/chrish-slingshot/ComfyUI-ImageGlitcher/assets/117188274/386ed082-d551-4520-ab9e-2c8fd4063f81)

---

### 🌈 Color Stylizer

Selective color isolation - pick a single color and desaturate everything else!

Perfect for creating dramatic color pop effects like in *Sin City* or *Schindler's List*.

![srg_sdxl_preview_temp_utykd_00003_](https://github.com/chrish-slingshot/CrasHUtils/assets/117188274/828fe8f6-c225-490d-be60-820cfc73d1dd) ![ComfyUI_temp_tsubu_00004_](https://github.com/chrish-slingshot/CrasHUtils/assets/117188274/7faea8aa-b931-46f3-86b8-7b17432ad46e)

**Parameters:**
- **target_color**: The color to preserve (hex or RGB)
- **tolerance**: How closely colors must match to be preserved
- **desaturation**: How much to desaturate non-matching colors

**Usage:** Connect an image and specify which color to keep while everything else becomes grayscale.

---

## 🤖 AI & Utility Nodes

### 💬 Query Local LLM

Send queries to OpenAI-compatible APIs and get text responses in your workflow!

Perfect for prompt generation, image description, or any text processing task.

![image](https://github.com/chrish-slingshot/CrasHUtils/assets/117188274/c7070ce1-9823-48ba-ac13-135c5449b74a)

**Features:**
- Compatible with OpenAI API and local LLMs (LM Studio, Ollama, text-generation-webui, etc.)
- Customizable endpoints
- System and user message support
- Temperature and token control

**Usage:**
1. Set your API endpoint (default: OpenAI)
2. Configure your prompt
3. Get text output to use in your workflow

**Supported Backends:**
- OpenAI API
- LM Studio (local)
- Ollama (local)
- text-generation-webui (local)
- Any OpenAI-compatible API

---

## 📐 SDXL Workflow Nodes

### 📏 SDXL Resolution Picker

Choose from **all** pre-trained SDXL resolutions in one convenient dropdown!

Unlike other resolution pickers, this includes the **complete** list of SDXL-trained resolutions for optimal quality.

![image](https://github.com/chrish-slingshot/CrasHUtils/assets/117188274/4ac8d27c-4a6c-4ec0-b5c0-5e70ae7738ee) ![image](https://github.com/chrish-slingshot/CrasHUtils/assets/117188274/6e919da0-9f00-423d-b2da-6f7eabf11b62)

**Features:**
- All official SDXL resolutions (1024×1024, 1152×896, 1216×832, etc.)
- Aspect ratio labels
- Portrait, landscape, and square formats
- Single selection output

**Why use this?** SDXL was trained on specific resolutions - using them gives better results than arbitrary sizes!

---

### ✂️ SDXL Resolution Split

Split SDXL Resolution output into separate width and height values.

![image](https://github.com/chrish-slingshot/CrasHUtils/assets/117188274/9b3cb55f-ecc8-444d-8657-74cf652c2fba)

**Purpose:** Reduces workflow clutter by passing resolution as a single connection, then splitting where needed.

**Usage:**
1. Connect SDXL Resolution Picker output to this node
2. Get separate width and height outputs
3. Connect to your Empty Latent Image or other nodes

**Benefit:** One connection instead of two = cleaner workflow graphs!

---

## 📥 Installation

! Recommended ! - Install through ComfyUI Manager, search for "CrasH Utils".

Manual:

1. Clone this repo into your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/chrish-slingshot/CrasHUtils.git
   ```

2. Restart ComfyUI

3. The nodes will appear in the "CrasH Utils" category

No additional dependencies required - everything runs out of the box!

---

## 🎯 Categories

Nodes are organized into categories in ComfyUI:

- **CrasH Utils/Games** - All game nodes
- **CrasH Utils/Image** - Image processing nodes
- **CrasH Utils/AI** - LLM and AI nodes
- **CrasH Utils/SDXL** - SDXL workflow helpers
- **CrasH Utils/Loaders** - Checkpoint utilities

---

## 🐛 Issues & Contributions

Found a bug or have a feature request? Open an issue on GitHub!

Pull requests welcome - especially for new games or utility nodes!

---

## 📝 Credits

- **Image Glitcher** based on work by [Felix Turner](https://www.airtightinteractive.com/demos/js/imageglitcher/)
- **DOOM** powered by [js-dos](https://js-dos.com/) emulator
- **DOOM Shareware** © id Software (free shareware version)

---

## ⚖️ License

MIT License - feel free to use, modify, and distribute!

DOOM Shareware is distributed under id Software's original shareware license.
