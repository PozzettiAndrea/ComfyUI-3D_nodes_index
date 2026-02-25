# 💰 ComfyUI Credit Tracker

Simple UI extension to track Modal GPU credits in real-time.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📸 Preview

Displays a simple `$80.00` button in the header bar that updates every second.

## ✨ Features

- 💵 Simple dollar amount display in header
- ⚡ Real-time tracking (updates per second)
- 💾 Persistent across restarts
- 🎮 Auto GPU detection
- 📊 Click to view details
- 🎨 Color-coded: Green (>50%), Yellow (20-50%), Red (<20%)

## 📦 Installation

### Quick Install

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/ComfyUI-ModalCredits.git
```

Restart ComfyUI.

### Manual Install

1. **Create folder:**
```bash
cd ComfyUI/custom_nodes/
mkdir ComfyUI-ModalCredits
cd ComfyUI-ModalCredits
mkdir js
```

2. **Copy files:**
   - `__init__.py` (root)
   - `config.json` (root)
   - `js/creditTracker.js` (in js folder)

3. **Restart ComfyUI**

## ⚙️ Configuration

Edit `config.json` to set your GPU costs:

```json
{
  "starting_balance": 80.00,
  "gpu_costs_per_hour": {
    "NVIDIA H100": 3.95,
    "NVIDIA A100-SXM4-80GB": 2.50,
    "NVIDIA A100-SXM4-40GB": 2.10,
    "NVIDIA A10G": 1.10,
    "Tesla T4": 0.59
  },
  "gpu_count": 1
}
```

## 🚀 Usage

1. **Start ComfyUI** - The credit display appears in the header automatically
2. **View balance** - See remaining credits (e.g., `$79.50`)
3. **Click for details** - Shows GPU type, cost/hour, time remaining
4. **Color changes** - Green → Yellow → Red as credits decrease

## 💾 Data Storage

Balance is saved to `balance.json` in the extension folder:

```json
{
  "last_updated": "2025-10-21T12:00:00Z",
  "remaining_balance": 75.40
}
```

## 🔄 Reset Balance

### API Method:
```bash
curl -X POST http://localhost:8188/credit_tracker/reset
```

### Manual Method:
Delete `balance.json` and restart ComfyUI.

## 📁 File Structure

```
ComfyUI-ModalCredits/
├── __init__.py              # Backend API
├── config.json              # GPU costs configuration
├── balance.json             # Auto-generated balance file
├── js/
│   └── creditTracker.js     # Frontend UI
└── README.md
```

## 🔧 API Endpoints

- `GET /credit_tracker/config` - Get configuration
- `GET /credit_tracker/balance` - Get current balance
- `POST /credit_tracker/balance` - Update balance
- `GET /credit_tracker/gpu_info` - Get GPU information
- `POST /credit_tracker/reset` - Reset to starting balance

## 🛠️ Troubleshooting

### Display not showing?
- Clear browser cache (Ctrl+Shift+R)
- Check browser console (F12) for errors
- Verify files are in correct locations
- Restart ComfyUI completely

### Wrong GPU detected?
- Check `nvidia-smi` command works
- Manually edit GPU name in `config.json`
- Add your GPU model to the cost list

### Balance not saving?
- Check write permissions on folder
- Look for `balance.json` file
- Check server console for errors

## 💡 Tips

- Update `config.json` costs to match your Modal pricing
- Click the display to see detailed breakdown
- Balance auto-saves every 10 seconds
- Color changes warn when credits are low

## 📄 License

MIT License - Free to use and modify

## 🤝 Contributing

Issues and PRs welcome!

---

**Made for the ComfyUI community** ❤️
