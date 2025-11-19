# 🚀 Warp Bypass - Identity Reset & Complete Removal Tools

<div align="center">

<!-- Main Stats -->
![GitHub stars](https://img.shields.io/github/stars/black12-ag/warp-bypass?style=for-the-badge&logo=github&color=gold)
![GitHub forks](https://img.shields.io/github/forks/black12-ag/warp-bypass?style=for-the-badge&logo=github&color=blue)
[![Repository Views](https://komarev.com/ghpvc/?username=black12-ag&repository=warp-bypass&color=brightgreen&style=for-the-badge&label=VIEWS)](https://github.com/black12-ag/warp-bypass)
![GitHub downloads](https://img.shields.io/github/downloads/black12-ag/warp-bypass/total?style=for-the-badge&logo=github&color=brightgreen)

<!-- Platform Support -->
![Python](https://img.shields.io/badge/python-3.6+-blue.svg?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-green.svg?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)

**Cross-platform Python tools for Warp terminal: Reset machine identity OR completely remove the app**

</div>

---

## 🎯 What is This?

**Warp Bypass** provides two tools to reset your Warp terminal identity:

- **🔄 Identity Reset** - Keeps app installed, resets machine identity
- **🗑️ Complete Removal** - Completely removes app and all traces

## 📊 Tools Comparison

<div align="center">

```mermaid
graph TB
    A[🚀 WARP MUNIR TOOLS] --> B[🔄 Identity Reset]
    A --> C[🗑️ Complete Removal]
    
    B --> D[✅ Keep App Installed]
    B --> E[⚡ Quick & Easy]
    
    C --> F[🗑️ Remove Application] 
    C --> G[🔄 Requires Reinstall]
    
    style A fill:#4CAF50,stroke:#333,stroke-width:3px,color:#fff
    style B fill:#2196F3,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#FF5722,stroke:#333,stroke-width:2px,color:#fff
```

</div>

| Feature | 🔄 Identity Reset | 🗑️ Complete Removal |
|---------|------------------|---------------------|
| **🏗️ App Installation** | ✅ **Preserved** | ❌ **Removed** |
| **⚡ Speed** | 🚀 **Fast** (30-60 sec) | 🐌 **Moderate** (2-5 min) |
| **📱 Ready to Use** | ✅ **Immediately** | ⬇️ **After Reinstall** |
| **🎯 Best For** | 🔧 **Quick Fix** | 🆕 **Fresh Start** |

## 🚀 Quick Start

### Prerequisites
- Python 3.6+ (pre-installed on macOS)
- Admin privileges (recommended)

### Installation
```bash
git clone https://github.com/black12-ag/warp-bypass.git
cd warp-bypass

# Identity Reset (Recommended)
python3 warp_id_reset.py   # macOS/Linux
python warp_id_reset.py    # Windows

# Complete Removal
python3 warp_remover.py    # macOS/Linux  
python warp_remover.py     # Windows
```



## 🐧 Linux Users - Standalone Scripts

### Quick One-Liner Commands

**Identity Reset (keep app installed):**
```bash
# Download and run identity reset
curl -sSL https://raw.githubusercontent.com/black12-ag/warp-bypass/main/linux_reset.sh | bash

# Or with wget
wget -qO- https://raw.githubusercontent.com/black12-ag/warp-bypass/main/linux_reset.sh | bash
```

**Complete Removal:**
```bash
# Download and run complete removal
curl -sSL https://raw.githubusercontent.com/black12-ag/warp-bypass/main/linux_remove.sh | bash

# Or with wget
wget -qO- https://raw.githubusercontent.com/black12-ag/warp-bypass/main/linux_remove.sh | bash
```

### Manual Method

```bash
# Clone the repository
git clone https://github.com/black12-ag/warp-bypass.git
cd warp-bypass

# Make scripts executable
chmod +x linux_reset.sh linux_remove.sh

# Run identity reset (keeps Warp installed)
./linux_reset.sh

# OR run complete removal
./linux_remove.sh
```

### What the Linux Scripts Do

**🔄 linux_reset.sh (Identity Reset)**
- Kills Warp processes
- Clears `~/.config/warp` (configuration)
- Clears `~/.local/share/warp` (application data)
- Clears `~/.cache/warp` (cache files)
- Clears `~/.local/state/warp` (state/logs)
- Removes temporary files in `/tmp` and `/run/user`
- Verifies Warp is still installed

**🗑️ linux_remove.sh (Complete Removal)**
- Everything from identity reset PLUS:
- Removes Warp from `/opt/Warp`, `/usr/local/bin`, `/usr/bin`
- Removes desktop entries
- Checks for package manager installations (Snap, Flatpak, APT, DNF/YUM)
- Verifies complete removal

### Linux File Locations

| Type | Location | Description |
|------|----------|-------------|
| **Config** | `~/.config/warp` | User preferences and settings |
| **Data** | `~/.local/share/warp` | Application data |
| **Cache** | `~/.cache/warp` | Temporary cache files |
| **State** | `~/.local/state/warp` | Runtime state and logs |
| **Binary** | `/opt/Warp` or `/usr/local/bin/warp` | Application installation |
| **Desktop** | `~/.local/share/applications/warp.desktop` | Desktop entry |

## 🪟 Windows Users - No Python? No Problem!

**[📥 Download windows_remove.bat](https://github.com/black12-ag/warp-bypass/raw/main/windows_remove.bat)**

Simply download the script above, right-click, and select **"Run as Administrator"**. 
It will clean everything (including browser data) without needing Python!

## 📚 How It Works

### 🔄 Identity Reset Process
1. 🔄 Stops Warp processes (keeps app installed)
2. 🧹 Clears user data and preferences
3. 🔑 Resets machine identity
4. ✅ Verifies app is still installed
5. 🎉 Ready to launch with fresh identity!

### 🗑️ Complete Removal Process
1. 🔫 Kills all Warp processes
2. 🗑️ Removes application completely
3. 🧹 Deep system cleanup (data, cache, registry)
4. 🔍 Verifies complete removal
5. ⬇️ Ready for fresh reinstall

## 🌍 Platform Support

| Feature | macOS | Windows | Linux |
|---------|-------|---------|-------|
| 🔫 Process Termination | ✅ | ✅ | ✅ |
| 🗑️ Application Removal | ✅ | ✅ | ✅ |
| 📁 Data Cleanup | ✅ | ✅ | ✅ |
| 📊 System DB Cleanup | ✅ | ✅ | ✅ |
| 🔍 Verification | ✅ | ✅ | ✅ |

## ⚠️ Important Notes

- **Backup first** - Tool permanently deletes files
- **Admin privileges** - Recommended for complete functionality
- **No undo** - Removal process cannot be reversed
- **Safe operation** - Graceful error handling

## 🔧 Troubleshooting

**Python not found:**
- macOS: Use `python3` instead of `python`
- Windows: Install from [python.org](https://python.org)

**Permission errors:**
- macOS: Run with `sudo python3 warp_remover.py`
- Linux: Run with `sudo ./linux_remove.sh` or `sudo python3 warp_remover.py`
- Windows: Run Command Prompt as Administrator

**Linux-specific notes:**
- The bash scripts (`linux_reset.sh`, `linux_remove.sh`) are Linux-only
- Python scripts work cross-platform
- If Warp was installed via package manager, uninstall with:
  - Snap: `sudo snap remove warp`
  - Flatpak: `flatpak uninstall dev.warp.Warp`
  - APT: `sudo apt remove warp`
  - DNF/YUM: `sudo dnf/yum remove warp`

## 📈 Repository Stats

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/black12-ag/warp-bypass?style=for-the-badge&logo=github&color=orange)
![GitHub last commit](https://img.shields.io/github/last-commit/black12-ag/warp-bypass?style=for-the-badge&logo=github)
![GitHub repo size](https://img.shields.io/github/repo-size/black12-ag/warp-bypass?style=for-the-badge&logo=github)

</div>

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Support

If this tool helped you, please give it a ⭐!

---

<div align="center">

**Made with ❤️ for the developer community**

</div>
