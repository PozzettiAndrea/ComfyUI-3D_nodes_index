# ComfyUI Discord Rich Presence

Show your ComfyUI generation status in Discord. Displays model name, step progress, queue info, and a live progress ring — all configurable from ComfyUI settings.

<img width="450" height="182" alt="image" src="https://github.com/user-attachments/assets/496edda5-25c4-4f09-bcc0-200d3548aa78" />

<img width="472" height="194" alt="image" src="https://github.com/user-attachments/assets/3bb2c4b9-da9e-4b71-a386-d23b346ec1c0" />


---

## Features

### 📊 Status Display
| | |
|---|---|
| **Live progress ring** | Animated icon showing generation percentage (0–100%) |
| **Model name** | Currently loaded checkpoint or UNET model |
| **Step counter** | Current step and total, e.g. `Step 12/20` |
| **Node tracking** | Which node is currently executing |
| **Queue info** | Remaining items when queue has multiple prompts |
| **Elapsed timer** | How long you've been generating or idle |

### ⚙️ Customization
| | |
|---|---|
| **Quick toggle** | Enable/disable directly from the toolbar button |
| **Privacy mode** | Hide model name and generation details |
| **Custom idle text** | Set your own status text when not generating |

### 🔧 Under the Hood
| | |
|---|---|
| **Auto-reconnect** | Handles Discord restarts gracefully |
| **Zero nodes** | Pure service extension, nothing added to your workflow |

## Installation

> [!TIP]
> The easiest way to install is through ComfyUI Manager.

### ComfyUI Manager (Recommended)

Search for `Discord Rich Presence` in ComfyUI Manager and install.

### Manual

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/davehornik/ComfyUI-Discord-RPC.git
pip install pypresence
```

> [!IMPORTANT]
> Restart ComfyUI after installation.

## Setup

1. Install the extension and restart ComfyUI
2. Make sure Discord desktop app is running
3. The extension connects automatically — you should see your status in Discord within a few seconds

> [!NOTE]
> Discord mobile and web don't support Rich Presence. The desktop app is required.

## Settings

<img width="781" height="96" alt="image" src="https://github.com/user-attachments/assets/88214e26-6666-4b4b-b2ec-1c4e2c9b1d03" />



### All settings are accessible in **ComfyUI Settings > Discord Rich Presence**.
<br>
<img width="774" height="777" alt="image" src="https://github.com/user-attachments/assets/611fe18d-7eed-4c6e-84de-5379f9adcc41" />
<br>
<br>

| Setting | Default | Description |
|---|---|---|
| Enable Discord RPC | `On` | Master toggle for the extension |
| Show Model Name | `On` | Display checkpoint/UNET name in status |
| Show Queue Info | `On` | Show remaining queue count |
| Show Node Name | `Off` | Show the currently executing node |
| Show Step Progress | `On` | Display step counter (e.g. Step 12/20) |
| Show Elapsed Time | `On` | Show elapsed time timer |
| Custom Idle Text | ` ` | Custom text when idle (default: "Idle") |
| Privacy Mode | `Off` | Hides model name and details |
| Debug Logging | `Off` | Log events to console for troubleshooting |

> [!TIP]
> Enable **Privacy Mode** to hide your model name and workflow details from other Discord users.

## Requirements

- **ComfyUI Desktop** or standalone ComfyUI
- **Discord desktop app** (Rich Presence is not supported on mobile/web)
- **Python package:** `pypresence >= 4.3.0` (installed automatically via ComfyUI Manager)

> [!WARNING]
> If Discord is not running when ComfyUI starts, the extension will retry connecting in the background. No action needed — it will connect automatically once Discord is launched.

## Troubleshooting

If something isn't working, enable **Debug Logging** in **Settings → Discord RPC → Advanced** and reproduce the issue. The console will show `[Discord RPC]` messages with event details.

When [reporting an issue](https://github.com/davehornik/ComfyUI-Discord-RPC/issues/new/choose), please include the debug log output — it helps diagnose the problem much faster.

## License

MIT
