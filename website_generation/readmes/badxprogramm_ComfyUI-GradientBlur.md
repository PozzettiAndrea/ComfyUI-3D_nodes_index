**GradientBlurNode for ComfyUI**

**Описание проекта:**

GradientBlurNode — это пользовательский узел для ComfyUI, который позволяет создавать градиентное размытие изображений. Этот инструмент предоставляет точный контроль над направлением, интенсивностью и распределением размытия, что делает его идеальным для создания плавных переходов, фокусировки внимания на определённых частях изображения или добавления художественных эффектов.

**Основные возможности:**
- **Гибкость управления:** Выберите одно из предопределённых направлений (например, сверху вниз, слева направо) или задайте собственный центр градиента.
- **Параметр Bias:** Уникальная функция для регулировки баланса между светлыми и тёмными областями маски, позволяющая контролировать преобладание чёрного или белого цвета.
- **Предварительный просмотр градиента:** Второй выходной порт предоставляет маску градиента для наглядного контроля эффекта.
- **Поддержка всех каналов:** Работает с изображениями RGB, RGBA и одноканальными (чёрно-белыми).
- **Оптимизация производительности:** Минимальные вычисления при нулевой интенсивности размытия (`intensity = 0`).

**Использование:**
1. Подключите изображение к входному порту `image`.
2. Настройте параметры:
   - `intensity`: Сила размытия (от 0 до 100).
   - `direction`: Направление градиента (например, сверху вниз, слева направо).
   - `auto_center`: Автоматическое центрирование для пользовательского режима.
   - `center_x`/`center_y`: Пользовательские координаты центра градиента.
   - `sharp_edge`: Включение резких границ градиента.
   - `bias`: Смещение маски для увеличения или уменьшения области размытия.
3. Получите два выходных изображения:
   - Основной результат с применённым градиентным размытием.
   - Маска градиента для предварительного просмотра.

**Пример использования:**
- Создание фонового размытия для портретов.
- Добавление эффекта глубины к пейзажам.
- Фокусировка внимания на конкретной части изображения через направленное размытие.

**Лицензия:**
Этот проект распространяется под лицензией MIT. Вы можете свободно использовать, изменять и распространять код в соответствии с условиями лицензии.

**Автор:**
Badxprogramm

**Благодарности:**
- Сообщество ComfyUI за вдохновение и поддержку.
- Разработчики PyTorch за мощные инструменты для работы с тензорами и изображениями.

**Ссылки:**
- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)

---

**README.md:**

```markdown
# GradientBlurNode for ComfyUI

GradientBlurNode is a custom node for ComfyUI that enables gradient-based image blurring with precise control over direction, intensity, and distribution. This tool is perfect for creating smooth transitions, focusing attention on specific parts of an image, or adding artistic effects.

## Features

- **Flexible Control:** Choose from predefined directions (e.g., top-to-bottom, left-to-right) or define a custom center for the gradient.
- **Bias Parameter:** Unique feature to adjust the balance between light and dark areas of the mask, allowing you to control the dominance of black or white regions.
- **Gradient Preview:** A secondary output port provides the gradient mask for visual feedback.
- **Multi-Channel Support:** Works seamlessly with RGB, RGBA, and single-channel (grayscale) images.
- **Performance Optimization:** Minimal computations when blur intensity is zero (`intensity = 0`).

## Usage

1. Connect an image to the `image` input port.
2. Adjust parameters:
   - `intensity`: Blur strength (0 to 100).
   - `direction`: Gradient direction (e.g., top-to-bottom, left-to-right).
   - `auto_center`: Automatic centering for custom mode.
   - `center_x`/`center_y`: Custom gradient center coordinates.
   - `sharp_edge`: Enable sharp gradient edges.
   - `bias`: Mask bias to increase or decrease the blurred area.
3. Get two output images:
   - The main result with applied gradient blur.
   - The gradient mask for preview.

## Example Use Cases

- Background blur for portraits.
- Adding depth effects to landscapes.
- Focusing attention on specific parts of an image using directional blur.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code in accordance with the license terms.

## Author

Badxprogramm

## Acknowledgments

- The ComfyUI community for inspiration and support.
- PyTorch developers for powerful tools to work with tensors and images.

## Links

- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
```
