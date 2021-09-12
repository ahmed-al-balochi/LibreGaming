#!/bin/sh

if [ -x "$(command -v dnf)" ]; then echo "dnf"
elif [ -x "$(command -v yay)" ]; then echo "yay"
elif [ -x "$(command -v paru)" ]; then echo "paru"
elif [ -x "$(command -v pacman)" ]; then echo "pacman"
elif [ -x "$(command -v apt)" ]; then echo "apt"
elif [ -x "$(command -v zypper)" ]; then echo "zypper"
else echo "FAILED TO INSTALL PACKAGE: Package manager not found."; fi