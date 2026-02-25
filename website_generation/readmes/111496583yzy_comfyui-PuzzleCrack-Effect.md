# Jigsaw Puzzle Effect Plugin

## Overview

The Jigsaw Puzzle Effect plugin provides a unique puzzle effect for image processing. By dividing an image into multiple puzzle pieces and optionally adding missing pieces, users can easily create artistic puzzle effects.

## Features

- **Puzzle Piece Size**: Users can customize the size of the puzzle pieces, ranging from 20 to 200 pixels.
- **Missing Puzzle Pieces**: Users can choose the number of missing puzzle pieces, up to 20.
- **Border Opacity**: Users can adjust the opacity of the puzzle piece borders.
- **Emboss Effect**: Users can add shadows and highlights to the puzzle pieces.

## Usage

1. **Install Dependencies**: Ensure the following libraries are installed:
   - `numpy`
   - `Pillow`
   - `torch`

2. **Import the Plugin**: Import the `JigsawPuzzleEffect` and `RegionBoundaryEffect` classes into your project.

3. **Apply the Effect**: Use the `apply_effect` method to generate an image with the puzzle effect.

## Example

![Example Image](examples/workflow.png)