# FANTA GameBox

A collection of game nodes for ComfyUI, currently featuring:

- 🎱 Billiards Game
- 🐍 Snake Game
- 🐦 Flappy Bird
- 🧱 Brick Breaker

## Billiards Game
- Click near the white cue ball to start aiming
- Hold and drag the mouse to adjust direction and power
- Release to shoot
- Score and shot count tracking
- Shows total shots when all balls are pocketed
- Click "Reset Game" to start over

## Snake Game
- Use arrow keys to control the snake
- Press space to pause/resume
- Press enter to restart
- Click canvas to start
- Score display and game status indicators

## Flappy Bird
- Remember to maximize the window for best experience
- Use space bar to control the bird
- Press enter to start/restart
- Click canvas to control the bird
- Score display and game status indicators

## Brick Breaker
- Use arrow keys or mouse to control the paddle
- Press enter to start/restart
- Score and lives display
- Special brick effects:
  - Red bricks: Requires 3 hits
  - Yellow bricks: Requires 2 hits
  - Green bricks: Bonus points
  - Purple bricks: Creates double ball effect
- Pause/resume support
- Difficulty increases with score

## Installation

1. Clone this repository to ComfyUI's `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ComfyUI-aki-v1.6/ComfyUI-FANTA-GameBox.git
```

2. Restart ComfyUI

## Usage

1. Find the "Games" category in ComfyUI's node menu
2. Select the desired game node
3. Add the node to your workflow
4. Start playing!

## Notes

- Game nodes don't require any inputs or outputs
- Game state is automatically saved
- Multiple game nodes can run simultaneously
- Game interface automatically adjusts to node size

## Changelog

### v1.2.1 Billiards Game Update
1. Gameplay Improvements
   - Increased pocket detection range (from 1.5x to 2x ball radius)
   - Added shot path prediction line
   - Optimized power system with cross-window support

2. Control Experience
   - Improved mouse control logic with out-of-window power control
   - Added dotted path display with boundary collision prediction
   - Optimized power calculation and display

3. Visual Feedback
   - Added semi-transparent shot path line
   - Enhanced aiming line display
   - Improved power indicator visualization

### v1.2.0
- Added Billiards Game
- Mouse control for direction and power
- Score and shot count tracking
- Complete physics collision system
- Game over summary screen

### v1.1.0
- Added Brick Breaker game
- Mouse and keyboard controls
- Score and lives display
- Special brick effects
- Multi-ball mode support

## License

MIT License
