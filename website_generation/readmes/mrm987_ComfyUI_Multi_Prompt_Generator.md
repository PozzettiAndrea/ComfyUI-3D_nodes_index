# ComfyUI Multi Prompt Generator

[English](#english) | [한국어](#한국어)

---

## English

A ComfyUI custom node that processes a list of prompts in a single run to generate multiple images.
Includes upscaling, LUT application, and real-time preview.

### Features

- **Batch Generation** — Process line-separated prompt list at once
- **2-Pass Upscale** — Upscale model + img2img refinement
- **Size Alignment** — 64/8 pixel alignment to prevent edge artifacts
- **LUT Support** — Apply .cube LUT files
- **Real-time Preview** — Check results during generation, cancel if needed
- **Auto Save** — Automatic filename based on first tag

### Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/mrm987/ComfyUI_Multi_Prompt_Generator.git
```
Restart ComfyUI.

### Nodes

### 1. Multi Prompt Generator
Generate multiple images with local models (SD, SDXL, etc.)

### 2. NAI Multi Prompt Generator  
Generate multiple images using NovelAI API + local upscale

**Setup for NAI node:**
1. Create `.env` file in ComfyUI root folder
2. Add your token: `NAI_ACCESS_TOKEN=your_token_here`

**NAI Node Features:**
- V4.5 model support with T5 encoder
- Auto-retry on server errors (429, 500, 502, 503, 504)
- `free_only` option for Opus subscribers (forces 1MP, 28 steps)
- Interrupt support (cancel during batch)
- SMEA/DYN for high-resolution generation

---

## Usage (Multi Prompt Generator)

1. Search node: **"Multi Prompt Generator"**
2. Connect: Model, CLIP, VAE, Empty Latent, Upscale Model
3. Enter prompt list — separate with blank lines:
```
# Lines starting with # are comments
# Start with - to skip

smile, happy, bright eyes,
looking at viewer

-angry, furrowed brow,
clenched teeth, glaring

sad, downcast eyes, frown
```

### Inputs

#### Required

| Input | Type | Description |
|-------|------|-------------|
| model | MODEL | Checkpoint model |
| clip | CLIP | CLIP model |
| vae | VAE | VAE model |
| latent | LATENT | Empty Latent Image |
| upscale_model | UPSCALE_MODEL | Upscale model (e.g., 2x-AnimeSharp) |
| base_prompt | STRING | Base prompt (combined with each line) |
| negative_prompt | STRING | Negative prompt |
| prompt_list | STRING | Prompt list (line-separated) |
| seed | INT | Seed |
| random_seed_per_image | BOOL | Use different random seed for each image |
| steps | INT | Sampling steps (default: 30) |
| cfg | FLOAT | CFG scale (default: 5.0) |
| sampler_name | COMBO | Sampler (euler_ancestral, etc.) |
| scheduler | COMBO | Scheduler (normal, karras, etc.) |
| enable_upscale | BOOL | Enable upscale (default: True) |
| save_prefix | STRING | Output folder name (default: "MultiPrompt") |

#### Optional

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| skip_indices | STRING | "" | Prompt numbers to skip (e.g. "3,4,7") |
| downscale_ratio | FLOAT | 0.7 | Downscale ratio after upscale |
| upscale_steps | INT | 15 | 2nd pass steps |
| upscale_cfg | FLOAT | 5.0 | 2nd pass CFG |
| upscale_denoise | FLOAT | 0.5 | 2nd pass denoise |
| size_alignment | COMBO | "none" | Size alignment (none / 8 / 64) |
| lut_name | COMBO | "None" | LUT file selection |
| lut_strength | FLOAT | 0.3 | LUT strength |
| enable_preview | BOOL | True | Real-time preview |

### Output

```
output/[save_prefix]/01_smile_00001.png
output/[save_prefix]/02_angry_00001.png
output/[save_prefix]/03_sad_00001.png
...
```

Filename format: `[index]_[first_tag]_[counter].png`

### Pipeline

```
For each prompt:
  1. Combine base_prompt + current line
  2. KSampler (1st pass)
  3. Show preview
  4. Upscale Model → Size alignment → KSampler (2nd pass)
  5. Apply LUT
  6. Update preview
  7. Save
```

### Notes

- **Prompt format**: Separate prompts with blank lines. Lines starting with `#` are comments. Start first line with `-` to skip that block
- **size_alignment**: 64 is safest. Use 64 if you see white edges
- **LUT files**: Auto-detected from `comfyui-propost/LUTs/` or `models/luts/` folder
- **Preview**: Check 1st pass result, cancel with Cancel button if not satisfied
- **Metadata**: Workflow info saved in PNG, can drag back into ComfyUI

---

## Usage (NAI Multi Prompt Generator)

1. Search node: **"NAI Multi Prompt Generator"**
2. Connect: Upscale Model (optional)
3. Enter prompt list — same format as above

### NAI Inputs

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| base_prompt | STRING | | Base prompt |
| negative_prompt | STRING | | Negative prompt |
| prompt_list | STRING | | Prompt list (line-separated) |
| width | INT | 832 | Image width |
| height | INT | 1216 | Image height |
| seed | INT | 0 | Seed (0 = random) |
| random_seed_per_image | BOOL | False | Use different random seed for each image |
| steps | INT | 28 | Sampling steps |
| cfg | FLOAT | 5.0 | CFG scale |
| sampler | COMBO | k_euler | Sampler |
| scheduler | COMBO | native | Scheduler |
| smea | COMBO | none | SMEA mode (none/SMEA/SMEA+DYN) |
| variety | BOOL | False | Enable variety (diverse compositions) |
| decrisper | BOOL | False | Dynamic thresholding (for high CFG) |
| free_only | BOOL | True | Force Opus free conditions |
| reference_image | IMAGE | None | Character reference image |
| char_ref_style_aware | BOOL | True | Copy style along with identity |
| char_ref_fidelity | FLOAT | 1.0 | How strictly to match the character |
| enable_upscale | BOOL | True | Enable local upscale |
| save_prefix | STRING | "NAI" | Output folder name |

### NAI Recommended Settings

**Resolution (free_only=True):**
- Portrait: 832×1216
- Landscape: 1216×832
- Square: 1024×1024
- Must be ≤1MP (1,048,576 pixels)

**Sampler/Scheduler:**
- `k_euler` + `native` — Stable, recommended
- `k_euler_ancestral` + `native` — More variety

**CFG:** 4~6 for V4.5 (lower works well)

**SMEA:** 
- `none` for ≤1MP
- `SMEA` or `SMEA+DYN` for higher resolutions

### Multi-Character Prompting

Use `|` to separate base prompt and character prompts:
```
2girls, scene, background | 1girl, blonde hair, smile | 1girl, black hair, angry
```
- First part = scene/style (base_caption)
- Following parts = each character (char_captions)
- Up to 6 characters supported
- Negative prompt also supports `|` for per-character negatives

---

## 한국어

프롬프트 리스트를 한 번에 처리해서 여러 이미지를 생성하는 ComfyUI 커스텀 노드.
업스케일, LUT 적용, 실시간 프리뷰 기능 포함.

### 기능

- **다중 프롬프트 배치 생성** — 줄바꿈으로 구분된 프롬프트 리스트를 한 번에 처리
- **2-Pass 업스케일** — 업스케일 모델 + img2img 리파인
- **크기 정렬** — 64/8배수 정렬로 테두리 아티팩트 방지
- **LUT 적용** — .cube LUT 파일 지원
- **실시간 프리뷰** — 생성 중 결과 확인, 마음에 안 들면 취소 가능
- **자동 저장** — 첫 태그 기반 파일명 자동 생성

### 설치

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/mrm987/ComfyUI_Multi_Prompt_Generator.git
```
ComfyUI 재시작.

### 노드 목록

### 1. Multi Prompt Generator
로컬 모델(SD, SDXL 등)로 다중 이미지 생성

### 2. NAI Multi Prompt Generator  
NovelAI API로 이미지 생성 + 로컬 업스케일

**NAI 노드 설정:**
1. ComfyUI 루트 폴더에 `.env` 파일 생성
2. 토큰 추가: `NAI_ACCESS_TOKEN=your_token_here`

**NAI 노드 특징:**
- V4.5 모델 지원 (T5 인코더)
- 서버 에러 자동 재시도 (429, 500, 502, 503, 504)
- `free_only` 옵션으로 Opus 무료 조건 강제 (1MP, 28 steps)
- 인터럽트 지원 (배치 중 취소 가능)
- 고해상도 생성용 SMEA/DYN

---

## 사용법 (Multi Prompt Generator)

1. 노드 검색: **"Multi Prompt Generator"**
2. 연결: Model, CLIP, VAE, Empty Latent, Upscale Model
3. 프롬프트 리스트 입력 — 빈 줄로 구분:
```
# #으로 시작하는 줄은 주석
# -로 시작하면 스킵

smile, happy, bright eyes,
looking at viewer

-angry, furrowed brow,
clenched teeth, glaring

sad, downcast eyes, frown
```

### 입력

#### 필수

| Input | Type | Description |
|-------|------|-------------|
| model | MODEL | 체크포인트 모델 |
| clip | CLIP | CLIP 모델 |
| vae | VAE | VAE 모델 |
| latent | LATENT | Empty Latent Image |
| upscale_model | UPSCALE_MODEL | 업스케일 모델 (예: 2x-AnimeSharp) |
| base_prompt | STRING | 기본 프롬프트 (각 줄과 결합됨) |
| negative_prompt | STRING | 네거티브 프롬프트 |
| prompt_list | STRING | 프롬프트 리스트 (줄바꿈 구분) |
| seed | INT | 시드 |
| random_seed_per_image | BOOL | 각 이미지마다 다른 랜덤 시드 사용 |
| steps | INT | 샘플링 스텝 (기본: 30) |
| cfg | FLOAT | CFG 스케일 (기본: 5.0) |
| sampler_name | COMBO | 샘플러 (euler_ancestral 등) |
| scheduler | COMBO | 스케줄러 (normal, karras 등) |
| enable_upscale | BOOL | 업스케일 활성화 (기본: True) |
| save_prefix | STRING | 저장 폴더명 (기본: "MultiPrompt") |

#### 선택

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| skip_indices | STRING | "" | 스킵할 프롬프트 번호 (예: "3,4,7") |
| downscale_ratio | FLOAT | 0.7 | 업스케일 후 다운스케일 비율 |
| upscale_steps | INT | 15 | 2차 샘플링 스텝 |
| upscale_cfg | FLOAT | 5.0 | 2차 CFG |
| upscale_denoise | FLOAT | 0.5 | 2차 디노이즈 |
| size_alignment | COMBO | "none" | 크기 정렬 (none / 8 / 64) |
| lut_name | COMBO | "None" | LUT 파일 선택 |
| lut_strength | FLOAT | 0.3 | LUT 강도 |
| enable_preview | BOOL | True | 실시간 프리뷰 |

### 출력

```
output/[save_prefix]/01_smile_00001.png
output/[save_prefix]/02_angry_00001.png
output/[save_prefix]/03_sad_00001.png
...
```

파일명: `[순번]_[첫태그]_[카운터].png`

### 파이프라인

```
각 프롬프트마다:
  1. base_prompt + 현재 줄 결합
  2. KSampler (1차)
  3. 프리뷰 표시
  4. Upscale Model → 크기 정렬 → KSampler (2차)
  5. LUT 적용
  6. 프리뷰 업데이트
  7. 저장
```

### 참고

- **프롬프트 형식**: 빈 줄로 프롬프트 구분. `#`으로 시작하는 줄은 주석. 첫 줄이 `-`로 시작하면 해당 블록 스킵
- **size_alignment**: 64가 가장 안전. 흰 테두리 생기면 64 사용
- **LUT 파일**: `comfyui-propost/LUTs/` 또는 `models/luts/` 폴더의 .cube 파일 자동 인식
- **프리뷰**: 1차 결과 확인 후 마음에 안 들면 Cancel로 중단 가능
- **메타데이터**: 워크플로우 정보가 PNG에 저장되어 ComfyUI에 다시 드래그 가능

---

## 사용법 (NAI Multi Prompt Generator)

1. 노드 검색: **"NAI Multi Prompt Generator"**
2. 연결: Upscale Model (선택)
3. 프롬프트 리스트 입력 — 위와 동일한 형식

### NAI 입력

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| base_prompt | STRING | | 기본 프롬프트 |
| negative_prompt | STRING | | 네거티브 프롬프트 |
| prompt_list | STRING | | 프롬프트 리스트 (줄바꿈 구분) |
| width | INT | 832 | 이미지 너비 |
| height | INT | 1216 | 이미지 높이 |
| seed | INT | 0 | 시드 (0 = 랜덤) |
| random_seed_per_image | BOOL | False | 각 이미지마다 다른 랜덤 시드 사용 |
| steps | INT | 28 | 샘플링 스텝 |
| cfg | FLOAT | 5.0 | CFG 스케일 |
| sampler | COMBO | k_euler | 샘플러 |
| scheduler | COMBO | native | 스케줄러 |
| smea | COMBO | none | SMEA 모드 (none/SMEA/SMEA+DYN) |
| variety | BOOL | False | 다양성 모드 (구도 다양화) |
| decrisper | BOOL | False | Dynamic Thresholding (고CFG용) |
| free_only | BOOL | True | Opus 무료 조건 강제 |
| reference_image | IMAGE | None | 캐릭터 레퍼런스 이미지 |
| char_ref_style_aware | BOOL | True | 스타일도 함께 복사 |
| char_ref_fidelity | FLOAT | 1.0 | 캐릭터 일치도 (높을수록 정확) |
| enable_upscale | BOOL | True | 로컬 업스케일 활성화 |
| save_prefix | STRING | "NAI" | 저장 폴더명 |

### NAI 권장 설정

**해상도 (free_only=True):**
- 세로: 832×1216
- 가로: 1216×832
- 정사각: 1024×1024
- 반드시 ≤1MP (1,048,576 pixels)

**샘플러/스케줄러:**
- `k_euler` + `native` — 안정적, 권장
- `k_euler_ancestral` + `native` — 더 다양한 결과

**CFG:** V4.5는 4~6 권장 (낮아도 잘 나옴)

**SMEA:** 
- 1MP 이하는 `none`
- 고해상도는 `SMEA` 또는 `SMEA+DYN`

### 멀티 캐릭터 프롬프팅

`|`로 베이스 프롬프트와 캐릭터 프롬프트 구분:
```
2girls, 장면, 배경 | 1girl, 금발, 미소 | 1girl, 검은 머리, 화남
```
- 첫 번째 = 장면/스타일 (base_caption)
- 이후 = 각 캐릭터 (char_captions)
- 최대 6명 지원
- 네거티브도 `|`로 캐릭터별 지정 가능

---

## License

MIT
