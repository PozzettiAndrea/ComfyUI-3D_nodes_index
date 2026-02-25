# ComfyUI-SopranoTTS

ComfyUI custom nodes for [Soprano TTS](https://github.com/ekwek1/soprano) - a fast, lightweight text-to-speech model.

## Features

- **SopranoLoader**: Load the TTS model once, reuse across multiple generations
- **SopranoTTS**: Generate speech from a single text input
- **SopranoTTSBatch**: Process multiple texts efficiently in batch
- **SopranoTTSStream**: Streaming generation (lmdeploy backend only)

## Installation

### Option 1: ComfyUI Manager (Recommended)

Search for "SopranoTTS" in ComfyUI Manager and click Install.

### Option 2: Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/jo-nike/ComfyUI-SopranoTTS.git
   ```

3. Install dependencies:
   ```bash
   cd ComfyUI-SopranoTTS
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

## Usage

### Basic Workflow

1. Add a **Soprano TTS Loader** node
2. Connect it to a **Soprano TTS** node
3. Enter your text
4. Connect the audio output to a **SaveAudio** node

### Nodes

#### Soprano TTS Loader

Loads the SopranoTTS model. The model is cached, so subsequent runs reuse the loaded model.

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| backend | COMBO | transformers | Model backend: `transformers` (recommended for newer GPUs), `lmdeploy`, or `auto` |
| cache_size_mb | INT | 10 | LMDeploy KV cache size in MB |
| decoder_batch_size | INT | 1 | Batch size for audio decoder |

#### Soprano TTS

Generate speech from text.

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| model | SOPRANO_MODEL | - | Model from SopranoLoader |
| text | STRING | - | Text to synthesize |
| temperature | FLOAT | 0.3 | Generation temperature (0.0-2.0) |
| top_p | FLOAT | 0.95 | Nucleus sampling parameter |
| repetition_penalty | FLOAT | 1.2 | Penalty for repeated tokens |

#### Soprano TTS Batch

Process multiple texts (one per line) in a single batch.

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| texts | STRING | - | Multiple texts separated by newlines |
| (other params same as SopranoTTS) | | | |

#### Soprano TTS Stream

Streaming generation with lower latency. **Only works with lmdeploy backend.**

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| chunk_size | INT | 1 | Tokens per audio chunk |
| (other params same as SopranoTTS) | | | |

## GPU Compatibility

- **RTX 5080 / Blackwell GPUs**: Use `backend: transformers` (lmdeploy doesn't support compute capability 12.0 yet)
- **RTX 40xx / Ada GPUs**: Either backend works
- **RTX 30xx / Ampere GPUs**: Either backend works

## Audio Output

- **Sample Rate**: 32,000 Hz
- **Channels**: Mono
- **Format**: ComfyUI AUDIO type (compatible with SaveAudio, PreviewAudio, etc.)

## Example Workflows

See the `workflows/` folder for example workflow JSON files.

## License

MIT
