# CalbeNodes

A collection of custom nodes created for personal use and convenience.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Nodes](#nodes)
  - [Character Manager](#character-manager)
  - [Film Grain](#film-grain)
  - [Flip Flopper](#flip-flopper)
- [Contributing](#contributing)
- [License](#license)

## Installation

git clone this repository into your custom nodes folder

I tried to make it so all requirements come with comfy, so hopefully no installs needed.

## Usage

The nodes will appear under a calbenodes heading and can be searched

## Nodes

### Character Manager

The Character Manager node is a versatile tool for managing and applying character-specific attributes in your image generation pipeline. It allows you to create, select, and apply character settings, including LoRA models, face images, and textual descriptions.

#### Features:
- Create and manage multiple characters
- Apply character-specific LoRA models
- Select preferred face images for characters
- Generate random face selections
- Create face image grids
- Apply character-specific activation text and descriptions

#### Inputs:
- `model`: The base model to apply character settings to
- `clip`: The CLIP model for text processing
- `character`: Select from existing characters, create a new one, or choose randomly
- `lora_strength`: Strength of the LoRA application (-10.0 to 10.0)
- `seed`: Random seed for consistent results
- `new_name`: Name for creating a new character
- `lora_path`: Path to the character's LoRA file
- `face_images_dir`: Directory containing character face images
- `preferred_face_image`: Path to the preferred face image
- `activation_text`: Text to activate the character in prompts
- `description`: Character description
- `negative_prompt`: Negative prompt for the character

#### Outputs:
- `model`: Updated model with applied LoRA
- `clip`: Updated CLIP model
- `lora_activation`: Character activation text
- `description`: Character description
- `negative_prompt`: Character-specific negative prompt
- `preferred_face`: Preferred face image (as tensor)
- `random_face`: Randomly selected face image (as tensor)
- `face_grid`: Grid of all character face images (as tensor)
- `character_name`: Name of the selected or created character
- `seed`: The seed used for this execution

#### Usage:
1. Select an existing character or choose "New Character" to create one.
2. If creating a new character, provide necessary information like name, LoRA path, and face images directory.
3. Adjust the LoRA strength as needed.
4. The node will apply the character settings and return the updated model along with character-specific information and images.

### Film Grain

The Film Grain node adds a realistic film grain effect to images, simulating the appearance of traditional photographic film.

#### Features:
- Adds customizable film grain to images
- Supports batch processing of multiple images
- Adjustable grain intensity

#### Inputs:
- `image`: The input image or batch of images (IMAGE type)
- `intensity`: The strength of the film grain effect (FLOAT, range 0.01 to 1.0, default 0.07)

#### Outputs:
- `IMAGE`: The processed image(s) with added film grain

#### Usage:
1. Connect an image or batch of images to the "image" input.
2. Adjust the "intensity" parameter to control the strength of the film grain effect.
3. The node will output the processed image(s) with the film grain applied.

### Flip Flopper

The Flip Flopper node (Same Architecture) is an advanced sampling node that alternates between two models during the sampling process, allowing for unique and creative image generation.

#### Features:
- Alternates between two models during sampling
- Supports different VAEs for each model
- Customizable sampling parameters for each model
- Option to invert the order of model application

#### Inputs:
- `model1` and `model2`: The two models to alternate between
- `vae1` and `vae2`: VAEs corresponding to each model
- `add_noise`: Enable or disable noise addition
- `noise_seed`: Seed for noise generation
- `steps`: Total number of sampling steps
- `cfg1` and `cfg2`: CFG scales for each model
- `sampler_name1` and `sampler_name2`: Sampler types for each model
- `scheduler1` and `scheduler2`: Scheduler types for each model
- `positive1`, `negative1`, `positive2`, `negative2`: Conditioning for each model
- `latent_image`: Input latent image
- `denoise`: Denoising strength
- `chunks`: Number of steps per chunk
- `invert`: Option to invert the order of model application

#### Outputs:
- `LATENT`: The resulting latent image after sampling
- `FINAL_VAE`: The VAE used in the final iteration

#### Usage:
1. Connect two models, their corresponding VAEs, and other required inputs.
2. Set the sampling parameters for each model (CFG, sampler, scheduler, etc.).
3. Adjust the number of steps and chunks as needed.
4. The node will alternate between the two models during sampling, producing a unique result.

## Contributing

This project is primarily for personal use, but if you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

MIT
