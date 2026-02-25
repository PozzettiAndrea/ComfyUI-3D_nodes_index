# ComfyUI String Similarity Node

A comprehensive text comparison node for ComfyUI that provides multiple algorithms to measure string similarity, useful for OCR validation, text comparison, and quality assessment workflows.

![String Similarity Example](https://github.com/gabe-init/ComfyUI-String-Similarity/blob/main/string%20similarity.png?raw=true)

## Features

- Multiple similarity algorithms in one node
- Detailed comparison metrics
- Support for both character-level and semantic similarity
- Useful for OCR accuracy assessment
- Compatible with ComfyUI's text processing pipeline

## Supported Algorithms

1. **Levenshtein Distance**: Edit distance between strings
2. **SequenceMatcher**: Python's built-in sequence matching
3. **Jaccard Similarity**: Set-based word comparison
4. **Cosine Similarity**: Vector space model comparison
5. **Word Error Rate (WER)**: Word-level accuracy metric
6. **Character Error Rate (CER)**: Character-level accuracy metric
7. **SentenceTransformer-MPNET**: Deep learning semantic similarity
8. **SentenceTransformer-MiniLM**: Lightweight semantic similarity

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-String-Similarity
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Restart ComfyUI

## Usage

1. Add the "String Similarity Node" to your workflow
2. Connect two text inputs (actual_text and ocr_text)
3. Select the comparison algorithm
4. The node outputs a formatted string with similarity metrics

### Input Parameters

- **actual_text**: The reference or ground truth text
- **ocr_text**: The text to compare (e.g., OCR output)
- **algorithm**: Choose from 8 different similarity algorithms

### Output

- **STRING**: Formatted result showing the similarity score and additional metrics

## Algorithm Details

### Distance-Based Metrics

- **Levenshtein**: Minimum edits needed to transform one string to another
- **SequenceMatcher**: Ratio of matching subsequences
- **CER/WER**: Error rates at character and word levels

### Similarity Metrics

- **Jaccard**: Intersection over union of word sets
- **Cosine**: Angle between text vectors

### Semantic Similarity

- **SentenceTransformers**: Neural models that understand meaning
  - MPNET: More accurate but slower
  - MiniLM: Faster with good accuracy

## Use Cases

1. **OCR Quality Assessment**: Compare OCR output with ground truth
2. **Text Validation**: Check if generated text matches expected output
3. **Duplicate Detection**: Find similar text passages
4. **Content Matching**: Semantic similarity for paraphrases

## Example Output

```
Actual Text: 'Hello World'
OCR Text: 'Helo World'

Levenshtein Distance: 1
Levenshtein Similarity: 0.91
```

## Performance Notes

- Simple algorithms (Levenshtein, Jaccard) are fast
- SentenceTransformers require model downloading on first use
- Models are cached after initial download

## Troubleshooting

- **Import errors**: Ensure all requirements are installed
- **Model download fails**: Check internet connection
- **Memory issues**: Use MiniLM for lower memory usage

## Requirements

- ComfyUI
- Python packages: Levenshtein, scikit-learn, numpy, sentence-transformers

## License

MIT License

Copyright (c) 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.