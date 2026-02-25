# Prompt Generator 12-Columns

**The fastest, cleanest 12-column random prompt generator for ComfyUI**  
Made by **DemonNCoding**

![Preview Image](https://raw.githubusercontent.com/DemonNCoding/PromptGenerator12Columns/refs/heads/main/previewImage.png)

I got tired of slow, bloated, or limited random prompt nodes - so I built exactly what I always wanted:  
- Instant generation  
- 3 versions included 
- Pre filled with text
- Zero lag  
- Full control  

### Included Nodes

| Node Name                                  | Description                          | Titles? |
|--------------------------------------------|--------------------------------------|---------|
| `PromptGenerator12Columns_Empty`           | 100% blank — you fill everything     | No      |
| `PromptGenerator12Columns_Prefilled`       | Pre-filled SFW (safe for work)       | Yes     |
| `PromptGenerator12Columns_Prefilled_NSFW`  | Pre-filled NSFW (adult content)      | Yes     |

### How to Use (Super Simple)

1. **Connect the output** to any text input (CLIP Text Encode, KSampler prompt, etc.)  
2. **To see the prompt** → either:  
   - Use a **Show Text** node (like "Preview Text" or "Comfyui-custom-scripts")  
   - OR just look in the console — **DEBUG = True by default**, so every generated prompt is printed there automatically!  

That's it — no extra steps needed.

### Options Explained

| Option           | What It Does                                                                 |
|------------------|------------------------------------------------------------------------------|
| **Use Commas**   | ON → single-line prompt with commas<br>OFF → each item on a new line         |
| **Add Titles**   | Adds `Subject: `, `Lighting: `, etc. before each picked item                 |
| **Include Always**| Appends your "always_add" block (e.g. masterpiece, 8k, best quality, etc.)  |

**Pro tip:** You do **NOT** need to fill all 12 columns. Use 3, 7, or all 12 — whatever you want.

### SFW Version — Column Titles (12 total)

1. Subject  
2. Action  
3. Setting  
4. Style  
5. Mood  
6. Colors  
7. Composition  
8. Details  
9. Camera Style  
10. Time  
11. Lighting  
12. Quality  

### NSFW Version — Column Titles (12 total)

1. Subject  
2. Hair Type  
3. Hair Color  
4. Eyes  
5. Body Type  
6. Breasts  
7. Skin & Marks  
8. Expression  
9. NSFW Action  
10. Clothing  
11. Lighting  
12. Quality  

### Want Better or More Entries?

**Yes! Please help improve them!**  
All pre-filled lists are community-driven and AI-assisted.  
If you have better, funnier, or more creative entries — **fork the repo and send a Pull Request**!  
Even adding just 10–20 new lines per column makes a huge difference.

### How to Add Your Own Lists (Super Easy)

Just ask ChatGPT (or any LLM) something like:

**For SFW:**
> Give me 50 one-per-line examples of each of the following categories:
Subject
Action
Setting
Style
Mood
Colors
Composition
Details
Camera Style
Time
Lighting
Quality

**For NSFW:**
> Give me 50 one-per-line examples of each of the following categories:
Subject
Hair Type
Hair Color
Eyes
Body Type
Breasts
Skin & Marks
Expression
NSFW Action
Clothing
Lighting
Quality

Then copy-paste the result directly into any column. Done!

### Disclaimer

All pre-filled content was sourced from public datasets and AI generation.  
**I (DemonNCoding) did not write any of the entries by hand.**  
Use at your own risk - especially the NSFW version.

### Want to Contribute?

→ https://github.com/DemonNCoding/PromptGenerator12Columns  
Fork → Edit any `.py` file → Add your lines → Pull Request  
Every contribution is welcome and appreciated!

### Enjoy!

Click generate and watch the magic happen — instantly.

If this saves you time, consider giving the repo a star

Made with love for the ComfyUI community  
— **DemonNCoding**
