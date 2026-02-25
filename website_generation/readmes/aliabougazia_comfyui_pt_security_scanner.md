# ComfyUI PT Security Scanner

A ComfyUI custom node that scans PyTorch model files (.pt, .pth, .ptc) for potential security vulnerabilities without executing them.

## 🔒 Features

- **Safe Analysis**: Examines pickle files WITHOUT loading or executing them
- **Directory Scanning**: Recursively scan entire directories for model files
- **Risk Detection**: Identifies dangerous imports (os, sys, subprocess, eval, exec, etc.)
- **Detailed Reports**: Human-readable reports plus JSON output for automation
- **Multiple Risk Levels**: LOW, HIGH, CRITICAL classifications

## 📦 Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/comfyui-pt-security-scanner.git
```

3. Restart ComfyUI

## 🚀 Usage

1. Add the **"PT Security Scanner 🔒"** node to your workflow (found in `utils/security` category)
2. Enter a directory path:
   - Relative: `models/` (from ComfyUI root)
   - Absolute: `/home/user/models/`
3. Enable/disable recursive scanning
4. Run to get a security report

## 📊 Outputs

- **report**: Human-readable security report
- **json_results**: Structured JSON data for automation
- **total_files**: Number of files scanned
- **low_risk**: Count of safe files (only standard PyTorch operations)
- **high_risk**: Count of suspicious files (unknown imports)
- **critical_risk**: Count of dangerous files (os, sys, subprocess, etc.)

## ⚠️ Risk Levels

- **LOW**: Only standard PyTorch operations detected (✓ Safe)
- **HIGH**: Unknown or suspicious module imports detected
- **CRITICAL**: Dangerous imports detected (os, sys, subprocess, eval, exec)

## 🛡️ How It Works

The scanner uses a custom `SafeUnpickler` that:
1. Intercepts all module imports during pickle loading
2. Never actually executes the loaded code
3. Compares imports against a whitelist of known safe PyTorch operations
4. Flags any suspicious or dangerous imports

## 📋 Example Output

```
================================================================================
PYTORCH MODEL SECURITY SCAN REPORT
================================================================================

Scanned Directory: /home/user/ComfyUI/models
Recursive: True

Total Files Scanned: 4
  ✓ LOW Risk: 4
  ⚠ HIGH Risk: 0
  🚨 CRITICAL Risk: 0
  ❌ Errors: 0

================================================================================
✓ All files appear safe - only standard PyTorch operations detected.
================================================================================

📋 ALL SCANNED FILES:
================================================================================
✓ [LOW     ] upscale_models/RealESRGAN_x2.pth
✓ [LOW     ] sam/sam3.pt
✓ [LOW     ] checkpoints/model.pth
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use in your own projects!

## ⚠️ Disclaimer

This tool provides a security analysis but is not a guarantee of complete safety. Always:
- Download models only from trusted sources
- Review model source code when available
- Keep your ComfyUI and dependencies updated

## 🔗 Links

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [Report Issues](https://github.com/YOUR_USERNAME/comfyui-pt-security-scanner/issues)

