#!/usr/bin/env python3
"""
Cross-Platform Warp Complete Removal Tool
==========================================

This tool completely removes Warp terminal from your system and makes it appear
as a new machine when you reinstall. Works on both macOS and Windows.

Usage:
    python warp_remover.py
    
or make it executable:
    chmod +x warp_remover.py
    ./warp_remover.py
"""

import os
import sys
import platform
import subprocess
import shutil
import glob
import time
from pathlib import Path


def show_banner():
    """Display simple banner with WARP over MUNIR"""
    print("\n" + "="*50)
    print("""    
██╗    ██╗█████╗ ██████╗ ██████╗ 
██║    ██║██╔══██╗██╔══██╗██╔══██╗
██░ █╗ ██║███████║██████╔╝██████╔╝
██░███╗██║██╔══██║██╔══██╗██╔═══╝ 
╚███╔███╔╝██║  ██║██║  ██║██║     
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     

███╗   ██╗██╗   ██╗███╗   ██╗██╗██████╗ 
████╗ ████║██║   ██║████╗  ██║██║██╔══██╗
██╔████╔██║██║   ██║██╔██╗ ██║██║██████╔╝
██║╚██╔╝██║██║   ██║██║╚██╗██║██║██╔══██╗
██║ ╚═╝ ██║╚█████╔╝██║ ╚████║██║██║  ██║
╚═╝     ╚═╝ ╚════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
""")
    print("="*50)
    print("║" + " "*10 + "🗑️ COMPLETE REMOVAL TOOL 🗑️" + " "*9 + "║")
    print("║ 👨‍💻 Munir Ayub © 2025                         ║")
    print("║ 🔗 github.com/black12-ag/warp-bypass         ║")
    print("║ 📺 youtube.com/@black-ai-fix                ║")
    print("="*50 + "\n")


class WarpRemover:
    def __init__(self):
        self.system = platform.system()
        self.home = Path.home()
        self.removed_count = 0
        
    def print_emoji(self, emoji, message):
        """Print message with emoji (works cross-platform)"""
        print(f"{emoji} {message}")
        
    def safe_remove(self, path_pattern):
        """Safely remove files/directories matching pattern"""
        if isinstance(path_pattern, str):
            paths = glob.glob(path_pattern)
        else:
            paths = [str(path_pattern)] if path_pattern.exists() else []
            
        for path in paths:
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    self.print_emoji("🗂️", f"Removed directory: {path}")
                elif os.path.isfile(path):
                    os.remove(path)
                    self.print_emoji("📄", f"Removed file: {path}")
                self.removed_count += 1
            except (OSError, PermissionError) as e:
                self.print_emoji("⚠️", f"Couldn't remove {path}: {e}")
                
    def kill_warp_processes(self):
        """Kill all Warp processes (cross-platform)"""
        self.print_emoji("🔫", "Killing Warp processes...")
        
        try:
            if self.system in ("Darwin", "Linux"):  # macOS or Linux
                subprocess.run(["pkill", "-f", "-i", "warp"], 
                             stderr=subprocess.DEVNULL, check=False)
            elif self.system == "Windows":
                subprocess.run(["taskkill", "/F", "/IM", "warp.exe"], 
                             stderr=subprocess.DEVNULL, check=False)
                subprocess.run(["taskkill", "/F", "/IM", "Warp.exe"], 
                             stderr=subprocess.DEVNULL, check=False)
            
            time.sleep(2)  # Give processes time to terminate
            self.print_emoji("✅", "Warp processes terminated")
            
        except Exception as e:
            self.print_emoji("⚠️", f"Process termination warning: {e}")
            
    def remove_macos_warp(self):
        """Remove Warp from macOS"""
        self.print_emoji("🍎", "Removing Warp from macOS...")
        
        # Main application
        self.print_emoji("🗑️", "Removing main application...")
        self.safe_remove("/Applications/Warp.app")
        
        # User data and configuration
        self.print_emoji("📁", "Removing user data and configuration...")
        
        # Application Support
        self.safe_remove(str(self.home / "Library/Application Support/*warp*"))
        self.safe_remove(str(self.home / "Library/Application Support/*Warp*"))
        
        # Preferences
        self.safe_remove(str(self.home / "Library/Preferences/*warp*"))
        self.safe_remove(str(self.home / "Library/Preferences/*Warp*"))
        
        # Caches
        self.safe_remove(str(self.home / "Library/Caches/*warp*"))
        self.safe_remove(str(self.home / "Library/Caches/*Warp*"))
        
        # Logs
        self.safe_remove(str(self.home / "Library/Logs/*warp*"))
        self.safe_remove(str(self.home / "Library/Logs/*Warp*"))
        
        # WebKit data
        self.safe_remove(str(self.home / "Library/WebKit/*warp*"))
        self.safe_remove(str(self.home / "Library/WebKit/*Warp*"))
        
        # Saved Application State
        self.safe_remove(str(self.home / "Library/Saved Application State/*warp*"))
        self.safe_remove(str(self.home / "Library/Saved Application State/*Warp*"))
        
        # HTTP Storage
        self.safe_remove(str(self.home / "Library/HTTPStorages/*warp*"))
        self.safe_remove(str(self.home / "Library/HTTPStorages/*Warp*"))
        
        # Downloads
        self.safe_remove(str(self.home / "Downloads/*warp*"))
        self.safe_remove(str(self.home / "Downloads/*Warp*"))
        
        # Clear Launch Services database
        self.print_emoji("📊", "Clearing Launch Services database...")
        try:
            lsregister_path = ("/System/Library/Frameworks/CoreServices.framework/"
                             "Frameworks/LaunchServices.framework/Support/lsregister")
            subprocess.run([lsregister_path, "-kill", "-r", "-domain", "local", 
                          "-domain", "system", "-domain", "user"], 
                         stderr=subprocess.DEVNULL, check=False)
        except Exception as e:
            self.print_emoji("⚠️", f"Launch Services warning: {e}")
            
    def remove_linux_warp(self):
        """Remove Warp from Linux"""
        self.print_emoji("🐧", "Removing Warp from Linux...")
        
        # Main application (common manual install locations)
        self.print_emoji("🗑️", "Removing main application (if present)...")
        self.safe_remove("/opt/Warp")
        self.safe_remove("/usr/local/bin/warp")
        self.safe_remove("/usr/bin/warp")
        self.safe_remove(str(self.home / ".local/bin/warp"))
        
        # User data and configuration (XDG base dirs)
        self.print_emoji("📁", "Removing user data and configuration...")
        xdg_config = Path(os.environ.get('XDG_CONFIG_HOME', self.home / '.config'))
        xdg_data = Path(os.environ.get('XDG_DATA_HOME', self.home / '.local/share'))
        xdg_cache = Path(os.environ.get('XDG_CACHE_HOME', self.home / '.cache'))
        xdg_state = Path(os.environ.get('XDG_STATE_HOME', self.home / '.local/state'))
        
        # Configuration
        self.safe_remove(str(xdg_config / 'warp'))
        self.safe_remove(str(xdg_config / 'Warp'))
        self.safe_remove(str(self.home / '.warp'))
        
        # Data
        self.safe_remove(str(xdg_data / 'warp'))
        self.safe_remove(str(xdg_data / 'Warp'))
        
        # Cache
        self.safe_remove(str(xdg_cache / 'warp'))
        self.safe_remove(str(xdg_cache / 'Warp'))
        
        # Logs/State
        self.safe_remove(str(xdg_state / 'warp'))
        
        # Desktop entries
        self.print_emoji("🗂️", "Removing desktop entries...")
        self.safe_remove(str(self.home / ".local/share/applications/warp.desktop"))
        self.safe_remove("/usr/share/applications/warp.desktop")
        
        # Runtime/temp
        try:
            uid = os.getuid()
        except AttributeError:
            uid = None
        if uid is not None:
            self.safe_remove(f"/run/user/{uid}/warp")
        self.safe_remove(f"/tmp/warp-{os.getenv('USER', '*')}")
        
        # Note: If installed via package manager, removal may require:
        #  - Snap: 'sudo snap remove warp'
        #  - Flatpak: 'flatpak uninstall dev.warp.Warp'
        #  - DEB/RPM: 'sudo apt/dnf/yum remove warp'
        # We don't run these automatically to avoid requiring root.

    def remove_windows_warp(self):
        """Remove Warp from Windows"""
        self.print_emoji("🪟", "Removing Warp from Windows...")
        
        # Common installation paths
        program_files = Path(os.environ.get('PROGRAMFILES', 'C:/Program Files'))
        program_files_x86 = Path(os.environ.get('PROGRAMFILES(X86)', 'C:/Program Files (x86)'))
        local_appdata = Path(os.environ.get('LOCALAPPDATA', str(self.home / 'AppData/Local')))
        appdata = Path(os.environ.get('APPDATA', str(self.home / 'AppData/Roaming')))
        
        # Main application installations
        self.print_emoji("🗑️", "Removing main application...")
        self.safe_remove(program_files / "Warp")
        self.safe_remove(program_files_x86 / "Warp")
        
        # User data and configuration
        self.print_emoji("📁", "Removing user data and configuration...")
        
        # AppData Local
        self.safe_remove(str(local_appdata / "*warp*"))
        self.safe_remove(str(local_appdata / "*Warp*"))
        
        # AppData Roaming
        self.safe_remove(str(appdata / "*warp*"))
        self.safe_remove(str(appdata / "*Warp*"))
        
        # Temp files
        temp_dir = Path(os.environ.get('TEMP', 'C:/Windows/Temp'))
        self.safe_remove(str(temp_dir / "*warp*"))
        self.safe_remove(str(temp_dir / "*Warp*"))
        
        # Downloads
        downloads_dir = self.home / "Downloads"
        self.safe_remove(str(downloads_dir / "*warp*"))
        self.safe_remove(str(downloads_dir / "*Warp*"))
        
        # Registry cleanup (requires admin privileges)
        self.print_emoji("📊", "Attempting registry cleanup...")
        try:
            import winreg
            # Clean up common registry locations
            registry_paths = [
                (winreg.HKEY_CURRENT_USER, "Software\\Warp"),
                (winreg.HKEY_LOCAL_MACHINE, "Software\\Warp"),
                (winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Warp"),
            ]
            
            for root, subkey in registry_paths:
                try:
                    winreg.DeleteKeyEx(root, subkey)
                    self.print_emoji("🔑", f"Removed registry key: {subkey}")
                except WindowsError:
                    pass  # Key doesn't exist or no permission
                    
        except ImportError:
            self.print_emoji("⚠️", "Registry cleanup requires Windows")
        except Exception as e:
            self.print_emoji("⚠️", f"Registry cleanup warning: {e}")
            
    def verify_removal(self):
        """Verify that Warp has been completely removed"""
        self.print_emoji("🔍", "Verifying complete removal...")
        
        # Count remaining Warp-related items
        search_paths = []
        
        if self.system == "Darwin":  # macOS
            search_paths = [
                str(self.home / "Library"),
                "/Applications"
            ]
        elif self.system == "Windows":
            search_paths = [
                str(self.home / "AppData"),
                str(Path(os.environ.get('PROGRAMFILES', 'C:/Program Files'))),
                str(Path(os.environ.get('PROGRAMFILES(X86)', 'C:/Program Files (x86)')))
            ]
        elif self.system == "Linux":
            search_paths = [
                str(self.home / ".config"),
                str(self.home / ".local/share"),
                str(self.home / ".cache"),
                str(self.home / ".local/state"),
                "/opt",
                "/usr/local/bin",
                "/usr/bin",
                str(self.home / ".local/bin"),
                str(self.home / ".local/share/applications"),
                "/usr/share/applications",
            ]
            
        remaining_items = 0
        for search_path in search_paths:
            if os.path.exists(search_path):
                try:
                    for root, dirs, files in os.walk(search_path):
                        for item in dirs + files:
                            if 'warp' in item.lower():
                                remaining_items += 1
                                self.print_emoji("👀", f"Found: {os.path.join(root, item)}")
                except (PermissionError, OSError):
                    pass  # Skip inaccessible directories
                    
        return remaining_items
        
    def run(self):
        """Main removal process"""
        print("=" * 60)
        self.print_emoji("🚀", "Starting Complete Warp Removal...")
        self.print_emoji("💻", f"Detected system: {self.system}")
        print("=" * 60)
        
        # Step 1: Kill processes
        self.kill_warp_processes()
        
        # Step 2: Platform-specific removal
        if self.system == "Darwin":  # macOS
            self.remove_macos_warp()
        elif self.system == "Windows":
            self.remove_windows_warp()
        elif self.system == "Linux":
            self.remove_linux_warp()
        else:
            self.print_emoji("❌", f"Unsupported system: {self.system}")
            self.print_emoji("💡", "This tool supports macOS, Windows, and Linux")
            return False
            
        # Step 3: Verification
        remaining = self.verify_removal()
        
        # Final report
        print("\n" + "=" * 60)
        self.print_emoji("✅", "WARP REMOVAL COMPLETE!")
        print(f"📈 Removed {self.removed_count} items")
        
        if remaining == 0:
            self.print_emoji("🎉", "Perfect! No Warp traces found.")
        else:
            self.print_emoji("⚠️", f"Found {remaining} remaining items (may be inaccessible)")
            
        self.print_emoji("🔄", "Your system will now appear as a NEW MACHINE to Warp.")
        self.print_emoji("⬇️", "You can safely reinstall Warp now.")
        print("=" * 60)
        
        return True


def main():
    """Entry point"""
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print(__doc__)
        return
    
    # Show banner and copyright
    show_banner()
        
    # Warn about admin privileges
    if platform.system() == "Windows":
        print("💡 Note: For complete removal on Windows, run as Administrator")
        print("   Right-click Command Prompt/PowerShell -> 'Run as Administrator'")
        print()
        
    # Confirm before proceeding
    response = input("⚠️  This will COMPLETELY remove Warp from your system. Continue? (y/N): ")
    if response.lower() not in ['y', 'yes']:
        print("❌ Cancelled by user")
        return
        
    # Run the removal
    remover = WarpRemover()
    success = remover.run()
    
    if success:
        print("\n🎯 Removal completed successfully!")
    else:
        print("\n❌ Removal failed or incomplete")
        sys.exit(1)


if __name__ == "__main__":
    main()
