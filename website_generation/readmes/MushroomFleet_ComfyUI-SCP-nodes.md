# SaveImageSCP - ComfyUI Custom Node

A custom ComfyUI node that automatically saves generated images locally and uploads them to a remote server via SCP (Secure Copy Protocol).

## Features

- 🖼️ Saves images locally in ComfyUI's output directory
- 🚀 Automatic SCP upload to predefined server locations
- 📁 Multiple profile support for different remote paths
- 🔐 Secure authentication via .env file
- ⚡ Easy profile switching via dropdown menu
- 🎛️ Optional upload toggle

## Installation

### 1. Install the Node

Copy the files to your ComfyUI custom nodes directory:

```bash
cd ComfyUI/custom_nodes
mkdir SaveImageSCP
cd SaveImageSCP

# Copy these files:
# - SaveImageSCP.py
# - config.json
# - requirements.txt
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install paramiko python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in your **ComfyUI root directory** (not in the custom_nodes folder):

```bash
cd /path/to/ComfyUI
nano .env
```

Add your SCP credentials:

```env
SCP_HOST=your.server.com
SCP_PORT=22
SCP_USERNAME=your_username
SCP_PASSWORD="your_password"
```

**Security Note:** For production use, consider using SSH keys instead of passwords.

### 4. Configure Profiles

Edit `config.json` in the SaveImageSCP directory to define your upload profiles:

```json
{
  "profiles": {
    "default": "/var/www/html/images/",
    "portfolio": "/home/user/portfolio/images/",
    "testing": "/tmp/comfyui/test/",
    "production": "/var/www/production/gallery/",
    "backup": "/mnt/backup/images/"
  }
}
```

Each profile maps a name to a remote server path.

## Usage

### In ComfyUI Workflow

1. Add the **Save Image (SCP Upload)** node to your workflow
2. Connect an image output to the node's input
3. Configure the node parameters:
   - **filename_prefix**: Prefix for saved files (default: "ComfyUI")
   - **profile**: Select from your configured profiles
   - **upload_enabled**: Toggle SCP upload on/off

### Node Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| images | IMAGE | Input images to save/upload |
| filename_prefix | STRING | Prefix for filenames (e.g., "myproject") |
| profile | DROPDOWN | Select upload destination profile |
| upload_enabled | BOOLEAN | Enable/disable SCP upload |

### Example Workflow

```
[Image Generation] → [SaveImageSCP]
                      ├─ filename_prefix: "artwork"
                      ├─ profile: "portfolio"
                      └─ upload_enabled: ✓
```

## File Naming

Images are saved with sequential numbering:
- `artwork_00001.png`
- `artwork_00002.png`
- `artwork_00003.png`

## Troubleshooting

### Upload Failed

**Problem:** "Upload failed" error in console

**Solutions:**
1. Check `.env` credentials are correct
2. Verify server is reachable: `ping your.server.com`
3. Test SSH access: `ssh user@your.server.com`
4. Ensure remote directory exists and is writable
5. Check firewall rules allow port 22 (or your custom SSH port)

### SCP Configuration Incomplete

**Problem:** "SCP configuration incomplete" warning

**Solution:** Verify all required fields in `.env` are set:
- SCP_HOST
- SCP_USERNAME
- SCP_PASSWORD

### Profile Not Found

**Problem:** Profile doesn't appear in dropdown

**Solutions:**
1. Check `config.json` syntax is valid JSON
2. Restart ComfyUI after modifying `config.json`
3. Ensure profile name doesn't contain special characters

### Permission Denied

**Problem:** "Permission denied" during upload

**Solutions:**
1. Verify remote directory permissions
2. Check user has write access to target directory
3. Try creating the directory manually first: `mkdir -p /remote/path`

## Security Considerations

### Using SSH Keys (Recommended)

For better security, use SSH key authentication instead of passwords:

1. Generate SSH key pair (if you don't have one):
```bash
ssh-keygen -t rsa -b 4096
```

2. Copy public key to server:
```bash
ssh-copy-id user@your.server.com
```

3. Modify `SaveImageSCP.py` to use key authentication:

```python
# In _upload_via_scp method, replace password auth with:
ssh.connect(
    hostname=self.scp_host,
    port=self.scp_port,
    username=self.scp_username,
    key_filename='/path/to/private/key'  # Add this line
)
```

### File Permissions

Ensure `.env` file has restricted permissions:
```bash
chmod 600 .env
```

### Network Security

- Use VPN or SSH tunneling for remote servers
- Consider using non-standard SSH ports
- Enable fail2ban on server to prevent brute force attacks
- Use strong passwords or preferably SSH keys

## Advanced Configuration

### Custom Port

If your SSH server uses a non-standard port, update `.env`:
```env
SCP_PORT=2222
```

### Automatic Directory Creation

The node automatically creates remote directories if they don't exist. Ensure your user has permission to create directories in the parent path.

### Multiple Servers

To support multiple servers, you can:
1. Create separate profile groups in `config.json`
2. Prefix profile names with server identifier: `server1_default`, `server2_production`

## Development

### Extending the Node

You can extend functionality by modifying `SaveImageSCP.py`:

- Add image format options (JPEG, WebP)
- Include compression settings
- Add metadata embedding
- Implement retry logic for failed uploads
- Add notification webhooks

## License

This is a custom node for ComfyUI. Use freely in your projects.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review ComfyUI logs for detailed error messages
3. Verify your server configuration
4. Test SCP connectivity independently

## Changelog

### Version 1.0.0
- Initial release
- Basic save and SCP upload functionality
- Profile support via config.json
- Environment-based authentication
- Automatic directory creation


## 📚 Citation

### Academic Citation

If you use this codebase in your research or project, please cite:

```bibtex
@software{comfyui-scp-nodes,
  title = {ComfyUI SCP nodes: Save and Upload to webservers automatically with Secure Copy},
  author = {[Drift Johnson]},
  year = {2025},
  url = {https://github.com/MushroomFleet/ComfyUI-SCP-nodes},
  version = {1.0.0}
}
```

### Donate:


[![Ko-Fi](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/driftjohnson)