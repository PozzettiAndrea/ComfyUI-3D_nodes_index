# ComfyUI-klein4&9multiangle

![comfy-random](https://github.com/thezveroboy/ComfyUI-klein4-9multiangle/blob/main/image1.jpg)

## Installation
1. Clone into `ComfyUI/custom_nodes/`.
2. Restart ComfyUI.

## English

Klein4&9 MultiAngle Prompt is a ComfyUI node that lets you quickly set the camera angle and distance to the subject in your prompt without typing long descriptions manually.

What it does:
- Three camera heights: top angle, eye level, bottom angle
- Eight viewing directions: straight front, front-left (three-quarter), strict left profile, back-left, straight back, back-right, strict right profile, front-right
- Six zoom/distance options: extremely close-up, close-up, zoom in, neutral (model decides itself), zoom out, full body
- Everything is selected from dropdown menus — no manual text input required
- The node automatically creates clear, detailed descriptions that Flux, SD3, Pony, SDXL and other models understand very well
- The prompt is built cleanly: first the angle description, then the zoom description, then your main prompt text — each part on a new line, no extra commas
- There is a “neutral” option that adds absolutely nothing about distance
- The final prompt always ends with a newline (convenient for further prompt processing)

Important note: this node relies purely on the model's own training data and is not based on any LoRA. However, if you use a suitable LoRA for multi-angle or perspective control, it will work even more effectively.

## Русский

Klein4&9 MultiAngle Prompt — это нода для ComfyUI, которая позволяет быстро задавать ракурс и расстояние до объекта в промпте, не используя ручной ввод текста.

Что она делает:
- Три высоты камеры: сверху (top angle), на уровне глаз (eye level), снизу (bottom angle)
- Восемь направлений взгляда: прямо спереди, спереди-слева (три четверти), строго слева в профиль, сзади-слева, строго сзади, сзади-справа, строго справа в профиль, спереди-справа
- Шесть вариантов расстояния: очень крупный план, крупный план, приближение, без указания (модель сама решает), отъезд, полный рост
- Всё выбирается в выпадающих списках — никаких ручных текстов
- Нода сама составляет понятные, подробные описания, которые модели (Flux, SD3, Pony, SDXL и т.д.) хорошо понимают
- Промпт формируется аккуратно: сначала ракурс, потом зум, потом твой основной текст — каждая часть с новой строки, без лишних запятых
- Есть вариант «нейтрально» — вообще ничего не добавляет про расстояние
- В конце всегда добавляется новая строка (для удобства дальнейшей работы с промптом)

Важно отметить, что эта нода использует данные обучения самой модели и не основана на LoRA. Но при наличии нужной лоры будет работать ещё эффективнее.

## 中文

Klein4&9 MultiAngle Prompt 是 ComfyUI 的一个节点，它能让你快速在提示词中设置相机角度和物体距离，而无需手动输入长段文字。
它能做什么：

- 三种相机高度：俯视（top angle）、眼平视（eye level）、仰视（bottom angle）
- 八种视角方向：正前方、前左（四分之三视角）、严格左侧侧面、后左、正后方、后右、严格右侧侧面、前右
- 六种缩放/距离选项：极近特写、特写、拉近、中性（模型自行决定）、拉远、全身
- 全部通过下拉菜单选择——无需手动输入任何文字
- 节点会自动生成清晰、详细的描述文字，这些描述 Flux、SD3、Pony、SDXL 等模型都能很好理解
- 提示词结构干净：先角度描述 → 再缩放描述 → 最后你的主体提示词，每部分独立成行，没有多余的逗号
- 有“中性”选项，完全不添加任何关于距离的内容
- 最终提示词总是以换行符结尾（方便后续处理）

重要说明：这个节点完全依赖模型自身的训练数据，不依赖任何 LoRA。但如果你搭配合适的视角或多角度 LoRA，使用效果会更好。



