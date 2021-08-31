# LibreGaming
This a Python Program that downloads gaming required packages based on your Linux Distribution.

# Currently Supported Distribution:
1. Ubuntu
2. Arch Linux
3. Fedora

# Prerequisite:
* To run this LibreGaming script you need python3 installed if not already.

1. Install Python3 For Ubuntu:
```
sudo apt install python3
```
3. Install Python3 For Arch Linux:
```
sudo pacman install python
```
3. Install Python3 For Fedora:
```
sudo dnf install python3
```

# Installation:
* To install LibreGaming Script you need to enter these commands:
```
git clone https://github.com/Ahmed-Al-Balochi/LibreGaming.git LibreGaming/
cd LibreGaming/
```

# Usage:
* To run the LibreGaming Script to install both the Gaming packages and ProtonGE enter this command:
```
python3 LibreGaming.py -a
```
* To run the LibreGaming Script to only install ProtonGE enter this command:
```
python3 LibreGaming.py -p
```
* To run the LibreGaming Script to update ProtonGE enter this command:
```
python3 LibreGaming.py -pu
```
* To run the LibreGaming Script to only install the Gaming packages enter this command:
```
python3 LibreGaming.py -g
```

# Feedback:
* Tell me what distro to add if yours is not available.
* Also please report if there are any bugs in the script.