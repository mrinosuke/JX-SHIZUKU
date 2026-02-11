# A script from Mr. Inosuke for remove phantom process in Android phone 
import os
import time
import sys
import subprocess
import shutil

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
B = '\033[1;34m'
M = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
RESET = '\033[0m'

HOME = os.environ['HOME']
JX_DIR = os.path.join(HOME, 'jx_adb')
DOCS_DIR = '/sdcard/Documents'
DOWNLOAD_DIR = '/sdcard/Download'
RISH_PATH = os.path.join(JX_DIR, 'rish')
RISH_ID = "com.termux"

def run_rish(cmd):
    full_cmd = f'RISH_APPLICATION_ID={RISH_ID} {RISH_PATH} -c "{cmd}"'
    try:
        return subprocess.check_output(full_cmd, shell=True, stderr=subprocess.STDOUT).decode('utf-8').strip()
    except:
        return None

def is_shizuku_running():
    return run_rish("echo 1") == "1"

def header():
    os.system('clear')
    print(f"{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{W}                    JX-SHIZUKU v1.0")
    print(f"{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def setup_files():
    if not os.path.exists(JX_DIR):
        print(f"{M}[+] Create \"jx_adb\" folder{RESET}")
        os.makedirs(JX_DIR)
        time.sleep(1)
    
    files_to_copy = ['rish', 'rish_shizuku.dex']
    files_needed = False
    
    for f in files_to_copy:
        if not os.path.exists(os.path.join(JX_DIR, f)):
            files_needed = True
            break
            
    if files_needed:
        print(f"{M}[+] Copy file from Documents...{RESET}")
        time.sleep(1)
        for f in files_to_copy:
            target = os.path.join(JX_DIR, f)
            source = os.path.join(DOCS_DIR, f)
            if not os.path.exists(source):
                source = os.path.join(DOWNLOAD_DIR, f)
            
            if os.path.exists(source):
                shutil.copy(source, target)
                os.chmod(target, 0o755)
            else:
                print(f"{R}[!] Error: {f} not found in Documents or Download!{RESET}")
                sys.exit()
        
        print(f"{M}[+] All done !{RESET}")
        time.sleep(1)

def main_menu():
    while True:
        header()
        print(f"{C} [ OPTIMIZATION ]             [ ADVANCED CONTROL ]")
        print(f"{M} 1. Disable Phantom Proc      11. Set Refresh Rate")
        print(f"{M} 2. Enable Phantom Proc       12. Change DPI (Res)")
        print(f"{G} 3. Disable Sys Updates       13. Reset DPI Default")
        print(f"{G} 4. Enable Sys Updates        14. Reboot Recovery")
        print(f"{G} 5. Clear Apps Cache          15. Reboot Bootloader")
        print(f"{G} 6. Kill Background Tasks     16. Record Screen (30s)")
        print(f"{G} 7. Battery Diagnostics       17. Take Screenshot")
        print(f"")
        print(f"{C} [ APP MANAGER ]              [ SYSTEM TOOLS ]")
        print(f"{G} 8. List 3rd Party Apps       18. Real-time Logcat")
        print(f"{G} 9. Force Stop All Apps       19. Hardware Specs")
        print(f"{G} 10. Uninstall Bloatware      20. Connectivity Ping")
        print(f"")
        print(f"{C} [ SHELL ACCESS ]             {R} 0. EXIT TOOL")
        print(f"{G} 99. Interactive Shell{RESET}")
        print(f"{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        
        choice = input(f"{Y}JX-SHIZUKU Selection >>> {RESET}").strip()

        if choice == '1':
            os.system('clear')
            print(f"{M}[*] Disabling Phantom Process Limit...{RESET}")
            run_rish("device_config put activity_manager max_phantom_processes 2147483647")
            run_rish("settings put global settings_enable_monitor_phantom_procs false")
            print(f"{G}[✓] Phantom Limit Removed!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '2':
            os.system('clear')
            print(f"{M}[*] Enabling Phantom Process Limit...{RESET}")
            run_rish("device_config put activity_manager max_phantom_processes 32")
            run_rish("settings put global settings_enable_monitor_phantom_procs true")
            print(f"{G}[✓] Defaults Restored!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '3':
            os.system('clear')
            print(f"{Y}[*] Disabling System Updates...{RESET}")
            run_rish("pm disable-user com.google.android.gms/.update.phone.SettingsReceiver")
            print(f"{G}[✓] System Updates Disabled!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '4':
            os.system('clear')
            print(f"{Y}[*] Enabling System Updates...{RESET}")
            run_rish("pm enable com.google.android.gms/.update.phone.SettingsReceiver")
            print(f"{G}[✓] System Updates Enabled!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '5':
            os.system('clear')
            print(f"{Y}[*] Trimming Caches...{RESET}")
            run_rish("pm trim-caches 999G")
            print(f"{G}[✓] Cache Cleared!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '6':
            os.system('clear')
            print(f"{Y}[*] Killing Background Tasks...{RESET}")
            run_rish("am kill-all")
            print(f"{G}[✓] Background Tasks Killed!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '7':
            os.system('clear')
            print(f"{C}[*] Fetching Battery Diagnostics...{RESET}\n")
            print(f"{W}{run_rish('dumpsys battery')}")
            input(f"\n{B}Press Enter to return...{RESET}")
            
        elif choice == '8':
            os.system('clear')
            print(f"{C}[*] Listing 3rd Party Apps...{RESET}\n")
            print(f"{W}{run_rish('pm list packages -3 | cut -f 2 -d \':\'')}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '9':
            os.system('clear')
            print(f"{Y}[*] Force Stopping All User Apps...{RESET}")
            pkgs = run_rish("pm list packages -3 | cut -f 2 -d ':'")
            for p in pkgs.split('\n'):
                if p:
                    run_rish(f"am force-stop {p}")
            print(f"{G}[✓] All User Apps Stopped!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '10':
            os.system('clear')
            pkg = input(f"{Y}Enter Package Name to Uninstall: {RESET}")
            if pkg:
                print(f"{Y}[*] Uninstalling {pkg}...{RESET}")
                run_rish(f"pm uninstall --user 0 {pkg}")
                print(f"{G}[✓] Uninstalled!{RESET}")
                input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '11':
            os.system('clear')
            hz = input(f"{Y}Enter Hz (60/90/120): {RESET}")
            run_rish(f"settings put system peak_refresh_rate {hz}")
            run_rish(f"settings put system min_refresh_rate {hz}")
            print(f"{G}[✓] Refresh Rate Set to {hz}Hz!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '12':
            os.system('clear')
            dpi = input(f"{Y}Enter New DPI: {RESET}")
            run_rish(f"wm density {dpi}")
            print(f"{G}[✓] DPI Updated to {dpi}!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '13':
            os.system('clear')
            print(f"{Y}[*] Resetting DPI to Default...{RESET}")
            run_rish("wm density reset")
            print(f"{G}[✓] DPI Reset!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '14':
            os.system('clear')
            print(f"{R}[*] Rebooting to Recovery...{RESET}")
            run_rish("reboot recovery")
            break
        
        elif choice == '15':
            os.system('clear')
            print(f"{R}[*] Rebooting to Bootloader...{RESET}")
            run_rish("reboot bootloader")
            break

        elif choice == '16':
            os.system('clear')
            print(f"{Y}[*] Recording 30s to /sdcard/jx_rec.mp4...{RESET}")
            run_rish("screenrecord --time-limit 30 /sdcard/jx_rec.mp4")
            print(f"{G}[✓] Recording Saved to SDCard!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '17':
            os.system('clear')
            print(f"{Y}[*] Taking Screenshot...{RESET}")
            run_rish("screencap -p /sdcard/jx_shot.png")
            print(f"{G}[✓] Screenshot Saved to SDCard!{RESET}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '18':
            os.system('clear')
            print(f"{R}[!] Streaming Logs... Press Ctrl+C to stop{RESET}")
            time.sleep(1)
            os.system(f"RISH_APPLICATION_ID={RISH_ID} {RISH_PATH} -c 'logcat'")

        elif choice == '19':
            os.system('clear')
            print(f"{C}[*] Fetching Hardware Specs...{RESET}\n")
            specs = f"Model: {run_rish('getprop ro.product.model')}\nChipset: {run_rish('getprop ro.board.platform')}\nRAM:\n{run_rish('free -h | grep Mem')}"
            print(f"{W}{specs}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '20':
            os.system('clear')
            print(f"{C}[*] Pinging Google...{RESET}\n")
            print(f"{W}{run_rish('ping -c 4 google.com')}")
            input(f"\n{B}Press Enter to return...{RESET}")

        elif choice == '99':
            os.system('clear')
            print(f"{G}[*] Entering Shizuku Shell...{RESET}")
            os.system(f"RISH_APPLICATION_ID={RISH_ID} {RISH_PATH}")

        elif choice == '0':
            os.system('clear')
            print(f"{R}[!] Session Terminated. Goodbye!{RESET}")
            break
        else:
            print(f"{R}[!] Invalid selection!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    if not os.path.exists('/sdcard/Documents'):
        os.system("termux-setup-storage")
    
    os.system('clear')
    print(f"{G}[+] JX-SHIZUKU started{RESET}")
    time.sleep(1)
    
    setup_files()
    
    print(f"{Y}[+] Checking Shizuku....{RESET}")
    time.sleep(1)

    if is_shizuku_running():
        print(f"{G}[+] Shizuku running....{RESET}")
        time.sleep(1)
        main_menu()
    else:
        print(f"{R}[!] Shizuku not running!{RESET}")
        print(f"{W}Please start Shizuku and authorize Termux.{RESET}")
        sys.exit()
