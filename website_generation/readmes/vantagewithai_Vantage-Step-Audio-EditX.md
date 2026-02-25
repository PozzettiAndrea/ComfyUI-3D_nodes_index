# Step‑Audio‑EditX Multi‑Voice Cloner Node 🎙️

This project is a custom node implementation built on top of Step-Audio-EditX. It adapts and extends EditX capabilities to support **multi‑speaker**, **long‑format**, **voice cloning**, and **emotion/style/speed editing**, enabling you to feed in a script with multiple speakers, inline pauses, paralinguistic cues (like laughter, breathing), and get a concatenated audio output — all in one pass.

---

## Description

The original Step‑Audio‑EditX model enables single‑speaker voice cloning and emotion/style editing given a reference prompt audio + text.  

This node extends that capability, allowing you to:

- Provide multiple “speaker” reference voices at once.  
- Write a simple script with speaker tags, inline pauses, and optionally emotion/style/speed tags.  
- Generate a **single contiguous audio file** with all voices, pauses, and editing applied.  
- Handle paralinguistic markers (like `[Laughter]`, `[Breathing]`, etc.) — these are preserved and synthesis attempts to reflect them as natural speech or silence, depending on your engine’s capabilities.  

In short: you can build multi‑voice dialogues, audio stories, podcasts, or voice‑over sequences in one go.

---

## Features

- Multi‑speaker support (map each speaker to a reference audio + prompt).  
- Inline speaker switching via `[speakerX]` tags.  
- Inline pauses via `[pause]N]` syntax (pause of N milliseconds).  
- Emotion / style / speed tags (e.g. `[happy]`, `[serious]`, `[faster]`) for each line.  
- Paralinguistic tag support — e.g. `[Laughter]`, `[Breathing]`, `[Sigh]`, `[Dissatisfaction-hnn]`, etc. Those tags remain in the output text.  
- Automatic concatenation of generated audio segments into one final waveform.  
- Progress reporting (with progress bar).  
- Graceful handling of missing speaker‑tags (defaults to first speaker).  

---

## How It Works

1. Parse the input script line by line.  
2. Detect tags:
   - `[speakerX]` — which reference voice/prompt to use.  
   - Optional leading tags like emotion, style, speed (e.g. `[happy]`, `[whisper]`, `[slower]`).  
   - Paralinguistic tags (preserved).  
   - `[pause]` tags — interpreted as “generate silence for N ms.”  
3. For each speech line, call `clone_from_tensor(...)` (and optionally repeated editing for emotion / style / speed).  
4. For pause lines, generate a tensor of zeros of the requested duration.  
5. Collect all segments (speech or silence), concatenate them, and return a single audio output.  

---

## Usage

Example usage in a ComfyUI flow:

```text
[speaker1][happy]Hello there!  
[pause]500  
[speaker2][sad][whisper]I’m not sure about this…  
[speaker1][Laughter]That’s hilarious!  
```

- Provide reference audios & prompts for each speaker.  
- Feed this script to the node.  
- Get a single AUDIO output: concatenated waveform with cloned voices, pauses, and editing.  

- **Emotion and Speaking Style Editing**
  - Remarkably effective iterative control over emotions and styles, supporting **dozens** of options for editing.
    - Emotion Editing : [ *Angry*, *Happy*, *Sad*, *Excited*, *Fearful*, *Surprised*, *Disgusted*, etc. ]
    - Speaking Style Editing: [ *Act_coy*, *Older*, *Child*, *Whisper*, *Serious*, *Generous*, *Exaggerated*, etc.]
    - Editing with more emotion and more speaking styles is on the way. **Get Ready!** 🚀
    

- **Paralinguistic Editing**
  -  Precise control over 10 types of paralinguistic features for more natural, human-like, and expressive synthetic audio.
  - Supporting Tags:
    - [ *Breathing*, *Laughter*, *Suprise-oh*, *Confirmation-en*, *Uhm*, *Suprise-ah*, *Suprise-wa*, *Sigh*, *Question-ei*, *Dissatisfaction-hnn* ]

- **Available Tags**
<table>
  <tr>
    <td rowspan="8" style="vertical-align: middle; text-align:center;" align="center">emotion</td>
    <td align="center"><b>happy</b></td>
    <td align="center">Expressing happiness</td>
    <td align="center"><b>angry</b></td>
    <td align="center">Expressing anger</td>
  </tr>
  <tr>
    <td align="center"><b>sad</b></td>
    <td align="center">Expressing sadness</td>
    <td align="center"><b>fear</b></td>
    <td align="center">Expressing fear</td>
  </tr>
  <tr>
    <td align="center"><b>surprised</b></td>
    <td align="center">Expressing surprise</td>
    <td align="center"><b>confusion</b></td>
    <td align="center">Expressing confusion</td>
  </tr>
  <tr>
    <td align="center"><b>empathy</b></td>
    <td align="center">Expressing empathy and understanding</td>
    <td align="center"><b>embarrass</b></td>
    <td align="center">Expressing embarrassment</td>
  </tr>
  <tr>
    <td align="center"><b>excited</b></td>
    <td align="center">Expressing excitement and enthusiasm</td>
    <td align="center"><b>depressed</b></td>
    <td align="center">Expressing a depressed or discouraged mood</td>
  </tr>
  <tr>
    <td align="center"><b>admiration</b></td>
    <td align="center">Expressing admiration or respect</td>
    <td align="center"><b>coldness</b></td>
    <td align="center">Expressing coldness and indifference</td>
  </tr>
  <tr>
    <td align="center"><b>disgusted</b></td>
    <td align="center">Expressing disgust or aversion</td>
    <td align="center"><b>humour</b></td>
    <td align="center">Expressing humor or playfulness</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td rowspan="17" style="vertical-align: middle; text-align:center;" align="center">speaking style</td>
    <td align="center"><b>serious</b></td>
    <td align="center">Speaking in a serious or solemn manner</td>
    <td align="center"><b>arrogant</b></td>
    <td align="center">Speaking in an arrogant manner</td>
  </tr>
  <tr>
    <td align="center"><b>child</b></td>
    <td align="center">Speaking in a childlike manner</td>
    <td align="center"><b>older</b></td>
    <td align="center">Speaking in an elderly-sounding manner</td>
  </tr>
  <tr>
    <td align="center"><b>girl</b></td>
    <td align="center">Speaking in a light, youthful feminine manner</td>
    <td align="center"><b>pure</b></td>
    <td align="center">Speaking in a pure, innocent manner</td>
  </tr>
  <tr>
    <td align="center"><b>sister</b></td>
    <td align="center">Speaking in a mature, confident feminine manner</td>
    <td align="center"><b>sweet</b></td>
    <td align="center">Speaking in a sweet, lovely manner</td>
  </tr>
  <tr>
    <td align="center"><b>exaggerated</b></td>
    <td align="center">Speaking in an exaggerated, dramatic manner</td>
    <td align="center"><b>ethereal</b></td>
    <td align="center">Speaking in a soft, airy, dreamy manner</td>
  </tr>
  <tr>
    <td align="center"><b>whisper</b></td>
    <td align="center">Speaking in a whispering, very soft manner</td>
    <td align="center"><b>generous</b></td>
    <td align="center">Speaking in a hearty, outgoing, and straight-talking manner</td>
  </tr>
  <tr>
    <td align="center"><b>recite</b></td>
    <td align="center">Speaking in a clear, well-paced, poetry-reading manner</td>
    <td align="center"><b>act_coy</b></td>
    <td align="center">Speaking in a sweet, playful, and endearing manner</td>
  </tr>
  <tr>
    <td align="center"><b>warm</b></td>
    <td align="center">Speaking in a warm, friendly manner</td>
    <td align="center"><b>shy</b></td>
    <td align="center">Speaking in a shy, timid manner</td>
  </tr>
  <tr>
    <td align="center"><b>comfort</b></td>
    <td align="center">Speaking in a comforting, reassuring manner</td>
    <td align="center"><b>authority</b></td>
    <td align="center">Speaking in an authoritative, commanding manner</td>
  </tr>
  <tr>
    <td align="center"><b>chat</b></td>
    <td align="center">Speaking in a casual, conversational manner</td>
    <td align="center"><b>radio</b></td>
    <td align="center">Speaking in a radio-broadcast manner</td>
  </tr>
  <tr>
    <td align="center"><b>soulful</b></td>
    <td align="center">Speaking in a heartfelt, deeply emotional manner</td>
    <td align="center"><b>gentle</b></td>
    <td align="center">Speaking in a gentle, soft manner</td>
  </tr>
  <tr>
    <td align="center"><b>story</b></td>
    <td align="center">Speaking in a narrative, audiobook-style manner</td>
    <td align="center"><b>vivid</b></td>
    <td align="center">Speaking in a lively, expressive manner</td>
  </tr>
  <tr>
    <td align="center"><b>program</b></td>
    <td align="center">Speaking in a show-host/presenter manner</td>
    <td align="center"><b>news</b></td>
    <td align="center">Speaking in a news broadcasting manner</td>
  </tr>
  <tr>
    <td align="center"><b>advertising</b></td>
    <td align="center">Speaking in a polished, high-end commercial voiceover manner</td>
    <td align="center"><b>roar</b></td>
    <td align="center">Speaking in a loud, deep, roaring manner</td>
  </tr>
  <tr>
    <td align="center"><b>murmur</b></td>
    <td align="center">Speaking in a quiet, low manner</td>
    <td align="center"><b>shout</b></td>
    <td align="center">Speaking in a loud, sharp, shouting manner</td>
  </tr>
  <tr>
    <td align="center"><b>deeply</b></td>
    <td align="center">Speaking in a deep and low-pitched tone</td>
    <td align="center"><b>loudly</b></td>
    <td align="center">Speaking in a loud and high-pitched tone</td>
  </tr>
  <tr>
  </tr>
  <tr>
  </tr>
  <tr>
    <td rowspan="5" style="vertical-align: middle; text-align:center;" align="center">paralinguistic</td>
    <td align="center"><b>Breathing</b></td>
    <td align="center">Breathing sound</td>
    <td align="center"><b>Laughter</b></td>
    <td align="center">Laughter or laughing sound</td>
  </tr>
  <tr>
    <td align="center"><b>Uhm</b></td>
    <td align="center">Hesitation sound: "Uhm"</td>
    <td align="center"><b>Sigh</b></td>
    <td align="center">Sighing sound</td>
  </tr>
  <tr>
    <td align="center"><b>Surprise-oh</b></td>
    <td align="center">Expressing surprise: "Oh"</td>
    <td align="center"><b>Surprise-ah</b></td>
    <td align="center">Expressing surprise: "Ah"</td>
  </tr>
  <tr>
    <td align="center"><b>Surprise-wa</b></td>
    <td align="center">Expressing surprise: "Wa"</td>
    <td align="center"><b>Confirmation-en</b></td>
    <td align="center">Confirming: "En"</td>
  </tr>
  <tr>
    <td align="center"><b>Question-ei</b></td>
    <td align="center">Questioning: "Ei"</td>
    <td align="center"><b>Dissatisfaction-hnn</b></td>
    <td align="center">Dissatisfied sound: "Hnn"</td>
  </tr>
</table>

---

## Installation / Integration
```bash
   cd custom_nodes
   git clone https://github.com/vantagewithai/Vantage-Step-Audio-EditX.git
   cd Vantage-Step-Audio-EditX
   pip install -r requirements.txt
   ```  
4. Launch ComfyUI — the node should appear under category **`Vantage/Step-Audio-EditX`**.  

## Download Models
[Download](https://huggingface.co/vantagewithai/Step-Fun-EditX-ComfyUI)

After downloading the models, copy them into ComfyUI/models, you should have the following structure:
```
ComfyUI/
├── models/
│   ├── Step-Audio-EditX/
│   ├──── CosyVoice-300M-25Hz/
│   │     ├─── campplus.onnx
│   │     ├─── cosyvoice.yaml
│   │     ├─── flow.pt
│   │     └─── hift.pt
│   ├──── dengcunqin/
│   ├──── └─── speech_paraformer-large_asr_nat-zh-cantonese-en-16k-vocab8501-online/
│   │          ├─── am.mvn
│   │          ├─── config.yaml
│   │          ├─── configuration.json
│   │          ├─── model.pt
│   │          ├─── seg_dict
│   │          ├─── tokens.json
│   │          ├─── tokens.txt
│   │          └─── write_tokens_from_txt.py
│   ├── model.safetensors
│   └── speech_tokenizer_v1.onnx
```
---

## Script Syntax

| Tag Type | Syntax | Meaning |
|---------|--------|---------|
| Speaker switch | `[speakerX]` | Use speaker number X (1-based) |
| Pause / silence | `[pause]300` | Insert 300 ms of silence |
| Emotion | `[happy]`, `[sad]`, … | First valid emotion tag per line is applied |
| Style | `[whisper]`, `[serious]`, … | First valid style tag per line is applied |
| Speed modifier | `[faster]`, `[slower]`, … | First valid speed tag per line is applied |
| Paralinguistic cue | `[Laughter]`, `[Breathing]`, `[Sigh]`, … | Preserved in the text — not stripped. May be used for downstream effects. |

Tags **must** come before the actual text of the line (after `[speakerX]`).  

Example:

```
[speaker2][happy][whisper][slower]I am fine!  
[speaker1][Laughter]That was funny!  
[pause]500  
```

---

## Limitations & Notes

- The quality of voice cloning / emotion/style editing depends on the underlying `Step‑Audio‑EditX` engine and your reference audio & prompt.  
- Paralinguistic tags are preserved in the text passed to the engine — if the engine doesn’t support them, they may just render as silence or be ignored.  
- If sample rates of speakers vary, the node currently assumes uniform sample rate in the concatenation step.  
- Long scripts may consume significant VRAM / memory — monitor usage accordingly.  
- The node does **not** perform grammar or punctuation correction — script should be well‑formatted.  

---

## License & Credits

**License: MIT**

This project builds upon the original **Step‑Audio‑EditX** repository (see [https://github.com/stepfun-ai/Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX)).  

Please refer to the original repository for the base license.

