#!/usr/bin/env python3
"""
Warp Machine ID Reset Tool
===========================

This tool resets Warp's machine identity without removing the application.
After running this tool, Warp will think you're on a completely new machine
while keeping all your app installations intact.

Usage:
    python warp_id_reset.py
    
or make it executable:
    chmod +x warp_id_reset.py
    ./warp_id_reset.py
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
    print("║" + " "*13 + "🚀 IDENTITY RESET TOOL 🚀" + " "*12 + "║")
    print("║ 👨‍💻 Munir Ayub © 2025                         ║")
    print("║ 🔗 github.com/black12-ag/warp-bypass         ║")
    print("║ 📺 youtube.com/@black-ai-fix                ║")
    print("="*50 + "\n")


class WarpIdentityReset:
    def __init__(self):
        self.system = platform.system()
        self.home = Path.home()
        self.reset_count = 0
        
    def print_emoji(self, emoji, message):
        """Print message with emoji (works cross-platform)"""
        print(f"{emoji} {message}")
        
    def safe_remove(self, path_pattern, description=""):
        """Safely remove files/directories matching pattern"""
        if isinstance(path_pattern, str):
            try:
                paths = glob.glob(path_pattern)
            except Exception as e:
                self.print_emoji("⚠️", f"Error during glob operation for {path_pattern}: {e}")
                return
        else:
            paths = [str(path_pattern)] if path_pattern.exists() else []
            
        for path in paths:
            # Safety check: Don't delete the script's own directory or current working directory
            try:
                path_obj = Path(path).resolve()
                cwd = Path.cwd().resolve()
                script_dir = Path(__file__).parent.resolve()
                if path_obj == cwd or path_obj == script_dir or cwd.is_relative_to(path_obj) or script_dir.is_relative_to(path_obj):
                    self.print_emoji("🛡️", f"Skipping project/script directory: {path}")
                    continue
            except Exception:
                pass

            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    self.print_emoji("🗂️", f"Reset {description}: {os.path.basename(path)}")
                elif os.path.isfile(path):
                    os.remove(path)
                    self.print_emoji("📄", f"Reset {description}: {os.path.basename(path)}")
                self.reset_count += 1
            except PermissionError:
                self.print_emoji("❌", f"Permission denied to remove {path}. Try running as administrator.")
            except FileNotFoundError:
                self.print_emoji("🤷", f"File not found to remove: {path}")
            except OSError as e:
                self.print_emoji("⚠️", f"Could not remove {path}: {e}")
                
    def kill_warp_processes(self):
        """Kill all Warp processes to ensure clean reset"""
        self.print_emoji("🔄", "Stopping Warp processes for identity reset...")
        
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
            self.print_emoji("✅", "Warp processes stopped")
            
        except Exception as e:
            self.print_emoji("⚠️", f"Process stop warning: {e}")
            
    def reset_macos_identity(self):
        """Reset Warp identity on macOS - keeps app installed"""
        self.print_emoji("🍎", "Resetting Warp identity on macOS...")
        
        # Note: We DON'T remove /Applications/Warp.app - that stays!
        
        # User identity and session data
        self.print_emoji("🔑", "Clearing user identity data...")
        
        # Application Support - user data, settings, machine ID
        self.safe_remove(str(self.home / "Library/Application Support/*warp*"), "user data")
        self.safe_remove(str(self.home / "Library/Application Support/*Warp*"), "user data")
        
        # Preferences - user preferences and machine-specific settings
        self.print_emoji("⚙️", "Clearing preferences and settings...")
        self.safe_remove(str(self.home / "Library/Preferences/*warp*"), "preferences")
        self.safe_remove(str(self.home / "Library/Preferences/*Warp*"), "preferences")
        
        # Caches - temporary files that might contain machine info
        self.print_emoji("🧹", "Clearing cache files...")
        self.safe_remove(str(self.home / "Library/Caches/*warp*"), "cache")
        self.safe_remove(str(self.home / "Library/Caches/*Warp*"), "cache")
        
        # Logs - might contain machine identification
        self.print_emoji("📋", "Clearing log files...")
        self.safe_remove(str(self.home / "Library/Logs/*warp*"), "logs")
        self.safe_remove(str(self.home / "Library/Logs/*Warp*"), "logs")
        
        # WebKit data - browser data that might have machine fingerprints
        self.print_emoji("🌐", "Clearing web data...")
        self.safe_remove(str(self.home / "Library/WebKit/*warp*"), "web data")
        self.safe_remove(str(self.home / "Library/WebKit/*Warp*"), "web data")
        
        # Saved Application State - window states and session info
        self.print_emoji("💾", "Clearing application state...")
        self.safe_remove(str(self.home / "Library/Saved Application State/*warp*"), "app state")
        self.safe_remove(str(self.home / "Library/Saved Application State/*Warp*"), "app state")
        
        # HTTP Storage - might contain session tokens
        self.print_emoji("🔐", "Clearing HTTP storage...")
        self.safe_remove(str(self.home / "Library/HTTPStorages/*warp*"), "HTTP storage")
        self.safe_remove(str(self.home / "Library/HTTPStorages/*Warp*"), "HTTP storage")
        
        # Group Containers - shared data
        self.print_emoji("📦", "Clearing group containers...")
        self.safe_remove(str(self.home / "Library/Group Containers/*warp*"), "group containers")
        self.safe_remove(str(self.home / "Library/Group Containers/*Warp*"), "group containers")
        self.safe_remove(str(self.home / "Library/Group Containers/2BBY89MBSN.dev.warp"), "group containers")

        # Application Scripts
        self.safe_remove(str(self.home / "Library/Application Scripts/*warp*"), "app scripts")
        self.safe_remove(str(self.home / "Library/Application Scripts/*Warp*"), "app scripts")
        self.safe_remove(str(self.home / "Library/Application Scripts/2BBY89MBSN.dev.warp"), "app scripts")

        # Comet Browser/App Data (Warp related)
        self.print_emoji("🌐", "Clearing Comet browser data...")
        self.safe_remove(str(self.home / "Library/Application Support/Comet/*/IndexedDB/https_app.warp.dev*"), "Comet DB")
        self.safe_remove(str(self.home / "Library/Application Support/Comet/*/Extensions/*warp*"), "Comet Ext")
        self.safe_remove(str(self.home / "Library/Application Support/Comet/*/Extensions/mjdcklhepheaaemphcopihnmjlmjpcnh"), "Comet Warp Ext")

        # Sentry Crash Reports
        self.safe_remove(str(self.home / "Library/Caches/SentryCrash/Warp"), "crash reports")
        self.safe_remove(str(self.home / "Library/Caches/SentryCrash/dev.warp.Warp-Stable"), "crash reports")
        
        # Clear Launch Services database (helps reset file associations)
        self.print_emoji("📊", "Updating system database...")
        try:
            lsregister_path = ("/System/Library/Frameworks/CoreServices.framework/"
                             "Frameworks/LaunchServices.framework/Support/lsregister")
            subprocess.run([lsregister_path, "-kill", "-r", "-domain", "local", 
                          "-domain", "system", "-domain", "user"], 
                         stderr=subprocess.DEVNULL, check=False)
        except Exception as e:
            self.print_emoji("⚠️", f"Database update warning: {e}")
            
    def reset_linux_identity(self):
        """Reset Warp identity on Linux - keeps app installed"""
        self.print_emoji("🐧", "Resetting Warp identity on Linux...")
        
        # XDG Base Directory paths
        xdg_config = Path(os.environ.get('XDG_CONFIG_HOME', self.home / '.config'))
        xdg_data = Path(os.environ.get('XDG_DATA_HOME', self.home / '.local/share'))
        xdg_cache = Path(os.environ.get('XDG_CACHE_HOME', self.home / '.cache'))
        xdg_state = Path(os.environ.get('XDG_STATE_HOME', self.home / '.local/state'))
        
        # User identity and session data
        self.print_emoji("🔑", "Clearing user identity data...")
        
        # Configuration files
        self.safe_remove(str(xdg_config / 'warp'), "config")
        self.safe_remove(str(xdg_config / 'Warp'), "config")
        self.safe_remove(str(self.home / '.warp'), "legacy config")
        
        # Application data
        self.print_emoji("📁", "Clearing application data...")
        self.safe_remove(str(xdg_data / 'warp'), "app data")
        self.safe_remove(str(xdg_data / 'Warp'), "app data")
        
        # Cache files
        self.print_emoji("🧹", "Clearing cache files...")
        self.safe_remove(str(xdg_cache / 'warp'), "cache")
        self.safe_remove(str(xdg_cache / 'Warp'), "cache")
        
        # State and logs
        self.print_emoji("📋", "Clearing state and logs...")
        self.safe_remove(str(xdg_state / 'warp'), "state")
        self.safe_remove(str(xdg_state / 'warp' / 'logs'), "logs")
        
        # Temporary/runtime files
        self.print_emoji("🗑️", "Clearing temporary/runtime files...")
        try:
            uid = os.getuid()
        except AttributeError:
            uid = None
        if uid is not None:
            self.safe_remove(f"/run/user/{uid}/warp", "runtime")
        self.safe_remove(f"/tmp/warp-{os.getenv('USER', '*')}", "temp files")

    def reset_windows_identity(self):
        """Reset Warp identity on Windows - keeps app installed"""
        self.print_emoji("🪟", "Resetting Warp identity on Windows...")
        
        local_appdata = Path(os.environ.get('LOCALAPPDATA', str(self.home / 'AppData/Local')))
        appdata = Path(os.environ.get('APPDATA', str(self.home / 'AppData/Roaming')))
        
        # User identity and session data
        self.print_emoji("🔑", "Clearing user identity data...")
        self.safe_remove(str(local_appdata / 'dev.warp.Warp-stable'), "user data")
        self.safe_remove(str(appdata / 'dev.warp.Warp-stable'), "user data")
        self.safe_remove(str(local_appdata / 'Warp'), "user data")
        self.safe_remove(str(appdata / 'Warp'), "user data")

        # Temp files
        self.print_emoji("🧹", "Clearing temporary files...")
        temp_dir = Path(os.environ.get('TEMP', 'C:/Windows/Temp'))
        self.safe_remove(str(temp_dir / "*WarpSetup.exe"), "temp files")

        # Start Menu link
        self.print_emoji("🔗", "Removing Start Menu link...")
        start_menu = Path(os.environ.get('APPDATA', str(self.home / 'AppData/Roaming'))) / "Microsoft/Windows/Start Menu/Programs"
        self.safe_remove(str(start_menu / "Warp.lnk"))

        # Registry cleanup - remove machine-specific registry entries
        self.print_emoji("📊", "Resetting registry entries...")
        try:
            import winreg
            # Clean up user-specific registry locations (not system-wide)
            registry_paths = [
                (winreg.HKEY_CURRENT_USER, "Software\\Warp"),
                (winreg.HKEY_CURRENT_USER, "Software\\dev.warp.Warp-stable"),
            ]
            
            for root, subkey in registry_paths:
                try:
                    winreg.DeleteKeyEx(root, subkey)
                    self.print_emoji("🔑", f"Reset registry: {subkey}")
                except FileNotFoundError:
                    self.print_emoji("🤷", f"Registry key not found, skipping: {subkey}")
                except PermissionError:
                    self.print_emoji("❌", f"Permission denied to delete registry key: {subkey}")
                except OSError as e:
                    self.print_emoji("⚠️", f"Error deleting registry key {subkey}: {e}")
                    
        except ImportError:
            self.print_emoji("⚠️", "Registry reset requires Windows")
        except Exception as e:
            self.print_emoji("⚠️", f"Registry reset warning: {e}")
            
    def verify_app_still_installed(self):
        """Verify that Warp app is still installed"""
        self.print_emoji("🔍", "Verifying Warp installation...")
        
        app_exists = False
        
        if self.system == "Darwin":  # macOS
            app_path = "/Applications/Warp.app"
            self.print_emoji("ℹ️", f"Checking for Warp at: {app_path}")
            app_exists = os.path.exists(app_path)
            if app_exists:
                self.print_emoji("✅", f"Warp app still installed: {app_path}")
            else:
                self.print_emoji("❌", "Warp app not found - may not be installed")
                
        elif self.system == "Windows":
            # Check common Windows installation paths
            program_files = Path(os.environ.get('PROGRAMFILES', 'C:/Program Files'))
            program_files_x86 = Path(os.environ.get('PROGRAMFILES(X86)', 'C:/Program Files (x86)'))
            local_appdata = Path(os.environ.get('LOCALAPPDATA', str(self.home / 'AppData/Local')))

            possible_paths = [
                program_files / "Warp/Warp.exe",
                program_files_x86 / "Warp/Warp.exe",
                local_appdata / "Warp/Warp.exe",
            ]
            
            for path in possible_paths:
                self.print_emoji("ℹ️", f"Checking for Warp at: {path}")
                if path.exists():
                    app_exists = True
                    self.print_emoji("✅", f"Warp app still installed: {path}")
                    break
                    
            if not app_exists:
                self.print_emoji("❌", "Warp app not found - may not be installed")
        elif self.system == "Linux":
            # Try to find the 'warp' binary or installation directories
            binary = shutil.which("warp")
            possible_paths = [
                Path("/opt/Warp"),
                Path("/usr/local/bin/warp"),
                Path("/usr/bin/warp"),
                self.home / ".local" / "bin" / "warp",
            ]
            if binary:
                app_exists = True
                self.print_emoji("✅", f"Warp binary found: {binary}")
            else:
                for path in possible_paths:
                    if Path(path).exists():
                        app_exists = True
                        self.print_emoji("✅", f"Warp found at: {path}")
                        break
            if not app_exists:
                self.print_emoji("❌", "Warp app not found - may not be installed")
                
        return app_exists
        
    def is_admin(self):
        """Check for admin privileges"""
        try:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False

    def run(self):
        """Main identity reset process"""
        print("=" * 70)
        self.print_emoji("🔄", "Starting Warp Machine Identity Reset...")
        self.print_emoji("💻", f"Detected system: {self.system}")
        self.print_emoji("🎯", "App will remain installed - only identity data will be reset")
        print("=" * 70)

        if self.system == "Windows" and not self.is_admin():
            self.print_emoji("❌", "This tool requires administrator privileges on Windows.")
            self.print_emoji("💡", "Please re-run this script from a Command Prompt or PowerShell with 'Run as Administrator'.")
            return False
        
        # Step 1: Stop processes
        self.kill_warp_processes()
        
        # Step 2: Platform-specific identity reset
        if self.system == "Darwin":  # macOS
            self.reset_macos_identity()
        elif self.system == "Windows":
            self.reset_windows_identity()
        elif self.system == "Linux":
            self.reset_linux_identity()
        else:
            self.print_emoji("❌", f"Unsupported system: {self.system}")
            self.print_emoji("💡", "This tool supports macOS, Windows, and Linux")
            return False
            
        # Step 3: Verify app is still there
        app_still_there = self.verify_app_still_installed()
        
        # Final report
        print("\n" + "=" * 70)
        self.print_emoji("✅", "WARP IDENTITY RESET COMPLETE!")
        print(f"📈 Reset {self.reset_count} identity items")
        
        if app_still_there:
            self.print_emoji("🎉", "Perfect! Warp app is still installed")
            self.print_emoji("🆔", "Your machine now has a fresh identity to Warp")
            self.print_emoji("🚀", "Launch Warp - it will see you as a new user/machine")
        else:
            self.print_emoji("⚠️", "Warp app not detected - you may need to install it")
            
        self.print_emoji("🔄", "Next: Open Warp and enjoy your fresh machine identity!")
        print("=" * 70)
        
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
        print("💡 Note: For complete reset on Windows, run as Administrator")
        print("   Right-click Command Prompt/PowerShell -> 'Run as Administrator'")
        print()
        
    print("🔄 WARP MACHINE IDENTITY RESET")
    print("================================")
    print("This tool will:")
    print("✅ Keep Warp app installed")
    print("🔄 Reset your machine identity") 
    print("🗑️  Clear user data and preferences")
    print("🆔 Make Warp see you as a new user")
    print()
    
    # Confirm before proceeding
    response = input("⚠️  Reset Warp machine identity? Your app will stay installed (y/N): ")
    if response.lower() not in ['y', 'yes']:
        print("❌ Cancelled by user")
        return
        
    # Run the reset
    reset_tool = WarpIdentityReset()
    success = reset_tool.run()
    
    if success:
        print("\n🎯 Identity reset completed successfully!")
        print("🚀 Launch Warp to start fresh!")
    else:
        print("\n❌ Identity reset failed or incomplete")
        sys.exit(1)


if __name__ == "__main__":
    main()
