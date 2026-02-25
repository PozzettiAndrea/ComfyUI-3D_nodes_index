# ComfyUI Telegram Bot Custom Nodes

This package provides custom nodes for ComfyUI that enable Telegram bot integration, allowing you to create workflows that can receive messages from Telegram and send responses back.

## Features

- **Telegram Listener**: A node that connects to a Telegram bot and listens for incoming messages
- **Save to Telegram**: A node that sends messages back to Telegram chats

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Go to Manager → Install Custom Nodes
3. Search for "Telegram Bot" and install

### Method 2: Manual Installation
1. Clone this repository into your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone <repository-url> ComfyUI-telegram-bot-node
   cd ComfyUI-telegram-bot-node
   ```

2. Install the required dependencies:
   ```bash
   # On Linux/Mac:
   ./install.sh
   # On Windows:
   install.bat
   ```

3. Restart ComfyUI

**Important**: Make sure the final directory structure looks like:
```
ComfyUI/
├── main.py (or comfyui_main.py)
├── custom_nodes/
│   └── ComfyUI-telegram-bot-node/
│       ├── __init__.py
│       ├── telegram_nodes.py
│       ├── requirements.txt
│       └── ... (other files)
└── ... (other ComfyUI files)
```

### Method 3: Manual Dependency Installation
If the install scripts don't work, manually install the dependencies:
```bash
pip install python-telegram-bot==20.7
```

## Setup

### Creating a Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Start a chat and send `/newbot`
3. Follow the instructions to create your bot
4. Save the bot token provided by BotFather

### Getting Your Chat ID

1. Start a chat with your bot
2. Send any message to your bot
3. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. Look for the `chat.id` field in the response

## Usage

### Telegram Listener Node

This node listens for incoming Telegram messages and outputs:
- **message_text**: The text content of the received message
- **chat_id**: The chat ID where the message came from

**Inputs:**
- `bot_token`: Your Telegram bot token from BotFather
- `timeout`: How long to wait for a message (in seconds)

### Save to Telegram Node

This node sends messages back to Telegram chats.

**Inputs:**
- `bot_token`: Your Telegram bot token from BotFather
- `chat_id`: The chat ID to send the message to (usually from Telegram Listener)
- `message`: The message text to send

**Output:**
- `status`: Status message indicating success or failure

## Example Workflow

1. Add a **Telegram Listener** node
2. Configure it with your bot token
3. Connect the `message_text` output to your text processing pipeline (e.g., to a prompt input)
4. Process your data (generate images, run text through AI, etc.)
5. Add a **Save to Telegram** node
6. Connect the `chat_id` from the listener to the `chat_id` input of the sender
7. Connect your processed result to the `message` input
8. Run the workflow - it will wait for Telegram messages and respond automatically

## Notes

- The bot will only respond to text messages (not images, files, etc.)
- Each Telegram Listener node runs its own bot instance
- The nodes handle async operations internally, so they work seamlessly with ComfyUI's execution model
- Chat IDs are preserved between the listener and sender nodes to enable proper responses

## Troubleshooting

- Make sure your bot token is correct
- Ensure the bot has been started by sending `/start` in the chat
- Check that the required dependencies are installed
- Verify that your firewall allows the connection to Telegram's servers

## Development

### Running Tests

The project includes comprehensive unit tests to ensure reliability:

```bash
# Run all tests
make test

# Run tests with verbose output
make test-verbose

# Run tests with coverage report
make test-coverage

# Using the test runner directly
python run_tests.py

# Run specific test module
python run_tests.py --specific telegram_nodes
```

### Code Quality

```bash
# Install development dependencies
make install-dev

# Run linting
make lint

# Format code
make format

# Run all checks
make check-all
```

### Test Coverage

The test suite covers:
- Node class structure validation
- Input/output type checking
- Error handling and validation  
- Integration between nodes
- Project structure compliance
- ComfyUI Manager compatibility

## License

MIT License
