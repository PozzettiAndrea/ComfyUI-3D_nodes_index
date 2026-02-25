# Clip Reshaper

ComfyUI-ClipReshaper is a collection of custom nodes designed to solve dimension mismatch errors and metadata inconsistencies in ComfyUI workflows. These utilities enable inspection, validation, transformation, and metadata enforcement for conditioning tensors, particularly useful when working with different CLIP encoders (SD1.5 ↔️ SDXL), experimental adapters, or debugging "matrix multiplication shape" crashes.

Key capabilities:
- Inspect conditioning tensor shapes and metadata structure
- Assert expected dimensions to fail early with clear error messages
- Reshape embeddings via padding/slicing or learnable linear projection
- Ensure SDXL-compatible metadata (size fields, pooled_output)

Use cases:
Cross-model CLIP adapter workflows, dimension debugging, SDXL pipeline fixes, experimental embedding space transformations.

ComfyUI custom nodes for:
- Inspecting conditioning tensor dimensions
- Early dimension assertions (catch matmul errors sooner)
- Pad/slice last-dimension to match an expected D
- Linear projection D_in -> D_out (optionally load trained weights)
- Ensuring SDXL-style conditioning metadata (width/height/crop/target, pooled_output)

![comfy-csm](https://github.com/thezveroboy/ComfyUI-ClipReshaper/raw/main/image.jpg)

## CR_ConditioningInspect

English:
This node inspects a conditioning object and prints human‑readable information about each item, such as tensor shape, final embedding dimension, presence and shape of pooled_output, and which size‑related metadata keys are available. It is useful when debugging dimension mismatches, understanding what a particular text encoder is outputting, or checking whether downstream nodes receive the format they expect.

Русский:
Эта нода анализирует conditioning‑объект и выводит удобочитаемую информацию по каждому элементу: форму тензора, конечную размерность эмбеддинга, наличие и форму pooled_output, а также какие ключи метаданных, связанных с размером, присутствуют. Она полезна при отладке несовпадения размерностей, понимании того, что именно выдаёт конкретный текстовый энкодер, и проверке, в каком формате данные приходят в последующие ноды.

## CR_ConditioningAssertDim

English:
This node verifies that every conditioning tensor has the expected last‑dimension size and raises a clear error if any item differs. It is useful as a safety check early in the graph to fail fast with an explicit message, instead of letting the pipeline crash later in a matrix multiplication inside KSampler or another model node.

Русский:
Эта нода проверяет, что у каждого conditioning‑тензора последняя размерность совпадает с ожидаемой, и выбрасывает понятную ошибку, если хотя бы один элемент отличается. Она полезна как ранний «предохранитель» в графе, позволяя сразу упасть с ясным сообщением, а не ловить краш где‑то глубоко в матмуле KSampler или другой модельной ноды.

## CR_ConditioningPadOrSlice

English:
This node forcefully reshapes conditioning tensors by either slicing or zero‑padding the last dimension to match a specified target size. It is useful for experimental setups or simple vector math operations where only the dimensionality must match, but it should be used cautiously because blindly cutting or padding embeddings can degrade or distort the semantic information.

Русский:
Эта нода жёстко меняет размерность conditioning‑тензоров, либо обрезая, либо дополняя нулями последнюю размерность до указанного значения. Она полезна для экспериментальных графов или простых векторных операций, где важно лишь совпадение размерностей, но применять её нужно осторожно, потому что бездумное обрезание или дописывание эмбеддингов нулями может ухудшить или исказить их смысловое содержание.

## CR_ConditioningLinearProject

English:
This node applies a learnable linear layer that projects conditioning embeddings from their current last‑dimension size to a target size, optionally loading pre‑trained weights from disk. It is useful when you have or plan to train a dedicated adapter between two embedding spaces; without trained weights it mainly serves as an experimental tool or infrastructure for future CLIP‑to‑CLIP adapters.

Русский:
Эта нода применяет обучаемый линейный слой, который проецирует эмбеддинги conditioning из текущей размерности последней оси в целевую, с возможностью загрузить заранее обученные веса с диска. Она полезна, когда у тебя есть или планируется отдельный адаптер между двумя пространствами эмбеддингов; без обученных весов это в основном экспериментальный инструмент и заготовка под будущие CLIP‑to‑CLIP адаптеры.

## CR_SDXLMetadataEnsure

English:
This node ensures that conditioning items contain SDXL‑style metadata, such as width, height, crop coordinates, target sizes, and optionally a pooled_output vector derived from the sequence. It is useful when building or fixing SDXL pipelines that expect these fields to be present in the metadata, preventing errors or inconsistent behavior in SDXL‑specific nodes.

Русский:
Эта нода гарантирует наличие у conditioning‑элементов SDXL‑метаданных, таких как width, height, координаты кропа, целевые размеры, а также при необходимости вектора pooled_output, полученного из последовательности. Она полезна при сборке или починке SDXL‑пайплайнов, которые ожидают эти поля в метаданных, и помогает избежать ошибок или нестабильного поведения в SDXL‑специфичных нодах.

## Install

Clone into:
ComfyUI/custom_nodes/ClipReshaper

Restart ComfyUI.

## Notes

Pad/slice and untrained linear projection do not guarantee semantic correctness.
For real CLIP-to-CLIP conversion you need trained adapter weights.





