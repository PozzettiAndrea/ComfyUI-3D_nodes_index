# Gecco Discord Autosend

Gecco Discord Autosend is a set of custom nodes for ComfyUI that allows you to automatically send generated images to Discord channels. This project includes nodes for selecting Discord channels, saving images locally, and sending images to Discord.

## Features

- Select Discord channels from a predefined list

- Automatically send generated images to Discord channels

- Save generated images locally into a custom directory

- Simple integration of a Discord Nextcord Bot with ComfyUI workflows

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:

   ```
   cd /path/to/ComfyUI/custom_nodes

   git clone https://github.com/ExterminanzHS/Gecco-Discord-Autosend.git

   ```

2. Install the required dependencies:

   ```

   pip install -r Gecco-Discord-Autosend/requirements.txt

   ```

   I have not added torch to the requirements.txt file, since installing it requires to use a specific link from their website: https://pytorch.org/

3. Create a .env file in the ComfyUI root directory and add your Discord bot token:

   ```

   BOT_TOKEN=your_discord_bot_token_here

   ```

4. Edit the channellist.py file to add your Discord channel IDs.

## Discord Bot Setup

Before using the Gecco Discord Autosend nodes, you need to create a Discord bot and get its token. Follow these steps:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).

2. Click on "New Application" and give your application a name.

3. In the left sidebar, click on "Bot" and then "Add Bot" on the right.

4. Under the bot's username, you'll see a "Token" section. Click "Copy" to copy your bot token.

5. Paste this token into your .env file as described in the installation steps.

6. In the left sidebar, click on "OAuth2" and then "URL Generator".

7. In the "Scopes" section, check "bot".

8. In the "Bot Permissions" section, check "Send Messages" and "Attach Files".

9. Copy the generated URL at the bottom of the page.

10. Open this URL in a new tab and select the server you want to add the bot to.

Remember to keep your bot token secret and never share it publicly.

## Usage

After installation and bot setup, you'll find three new nodes in ComfyUI:

1. Gecco Select Channel: Use this node to select a Discord channel from your predefined list.

2. Gecco Autosend: This node sends the generated images to the selected Discord channel.

3. Gecco Image Save: Use this node to save generated images locally.

To use these nodes in your workflow:

1. Add the Gecco Select Channel node and choose a channel from the dropdown.

2. Connect the output of your image generation nodes to both Gecco Autosend and Gecco Image Save (if you want to save locally).

3. Connect the channel ID output from Gecco Select Channel to the channel_id input of Gecco Autosend.

4. Run your workflow, and the generated images will be sent to the selected Discord channel and/or saved locally.

## Configuration

To add or modify Discord channels, edit the channellist.py file. Add entries in the format:

```python

"channel_name": channel_id_as_integer,

```

To find a channel's ID in Discord:

1. Enable Developer Mode in Discord (User Settings > App Settings > Advanced > Developer Mode).

2. Right-click on the channel you want to add and select "Copy ID".

## Alternative Installation

You can also install this package directly using pip:
```

```bash

pip install git+https://github.com/ExterminanzHS/Gecco-Discord-Autosend.git

```

This will install the package and its dependencies in your Python environment.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for the awesome UI framework

- [Nextcord](https://github.com/nextcord/nextcord) for the Discord API wrapper

## Author

ExterminanzHS - [GitHub Profile](https://github.com/ExterminanzHS)


If you find yourself regularly using my nodes, why not buy me a coffee?
[BuyMeACoffee](https://buymeacoffee.com/cybersnacc)
