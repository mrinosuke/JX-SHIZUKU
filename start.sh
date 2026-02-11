#!/bin/bash
# script for download important things

printf "\033[1;36m[+] Checking All things\033[0m\n"
sleep 1

if [ -d "/sdcard/Android" ]; then
    printf "\033[1;32m[✓] Storage Permission Allowed\033[0m\n"
else
    printf "\033[1;31m[×] Storage Permission not allowed\033[0m\n"
    termux-setup-storage
    sleep 3
fi
sleep 1

printf "\033[1;33m[!] Checking python\033[0m\n"
sleep 1
if command -v python3 >/dev/null 2>&1; then
    printf "\033[1;32m[✓] Python is installed\033[0m\n"
else
    printf "\033[1;31m[×] Python is not installed. Installing...\033[0m\n"
    pkg install python -y
fi
sleep 1

printf "\033[1;33m[!] Checking adb tool\033[0m\n"
sleep 1
if command -v adb >/dev/null 2>&1; then
    printf "\033[1;32m[✓] Adb tool is installed\033[0m\n"
else
    printf "\033[1;31m[×] Adb tool is not installed. Installing...\033[0m\n"
    pkg install android-tools -y
fi
sleep 1

printf "\n\033[1;36m[ ! ] Results -\033[0m\n"
sleep 1
printf "\033[1;32m[✓] Storage Permission\033[0m\n"
sleep 1
printf "\033[1;32m[✓] Python\033[0m\n"
sleep 1
printf "\033[1;32m[✓] Adb tool\033[0m\n"
sleep 1

if [ -n "$ZSH_VERSION" ]; then
    RC_FILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    RC_FILE="$HOME/.bashrc"
else
    RC_FILE="$HOME/.bashrc"
fi

if ! grep -q "alias jx_adb=" "$RC_FILE"; then
    echo "alias jx_adb='cd ~ && cd JX-SHIZUKU && python3 jx_shizuku.py'" >> "$RC_FILE"
    . ~/.bashrc
    printf "\033[1;32m[✓] Alias created in $RC_FILE\033[0m\n"
else
    printf "\033[1;33m[!] Alias already exists in $RC_FILE\033[0m\n"
fi
sleep 1

printf "\n\033[1;36mEnter command \"jx_adb\" for tool\033[0m\n"
