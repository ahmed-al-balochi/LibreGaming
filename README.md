# LibreGaming
Python Program that downloads gaming required packages based on your Linux Distribution.

[![Downloads](https://static.pepy.tech/personalized-badge/libregaming?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/libregaming)

Table of contents
=================

 - [Distributions](#Distributions)
 - [Prerequisites](#Prerequisites)
     - [Dependencies](#Dependencies)
 - [Packages](#Packages)
 - [Installation](#Installation)
 - [Usage](#Usage)
 - [VideoDemo](#VideoDemo)
 - [Feedback](#Feedback)
 - [Credits](#Credits)


# Distributions:
* I tested this script on these three distributions. but it should also work on their derivatives too.
1. Ubuntu.
2. Arch Linux.
3. Fedora.
4. OpenSUSE Tumbleweed.

# Prerequisites:
* To run this LibreGaming script you need python3 installed if not already. to install python3 click [Here](https://github.com/Ahmed-Al-Balochi/LibreGaming#dependencies).
* Also you need to enable nonfree packages if you are using Fedora to install steam.
* You can find the commands to enable nonfree packages for Fedora in this [website](https://docs.fedoraproject.org/en-US/quick-docs/setup_rpmfusion/#proc_enabling-the-rpmfusion-repositories-using-command-line-utilities_enabling-the-rpmfusion-repositories):

* Or you can enter these commands that I copied for the above website
To enable free and nonfree packages on Fedora enter these command:
```
sudo dnf install \
  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
```
To enable nonfree packages on Fedora enter these command:
```
sudo dnf install \
  https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```
* now you need to refreash the repos:
```
sudo dnf group update core
```
## Dependencies:
* git
1. Install git For Ubuntu:
```
sudo apt install git
```
2. Install git For Arch Linux:
```
sudo pacman -S git
```
3. Install git For Fedora:
```
sudo dnf install git
```
4. Install git For OpenSUSE Tumbleweed:
```
sudo zypper install git
```

* python3
1. Install Python3 For Ubuntu:
```
sudo apt install python3
```
3. Install Python3 For Arch Linux:
```
sudo pacman -S python
```
3. Install Python3 For Fedora:
```
sudo dnf install python3
```
4. Install Python3 For OpenSUSE Tumbleweed:
```
sudo zypper install python3
```

* python3-pip.
1. Install python3-pip For Ubuntu:
```
sudo apt install python3-pip
```
2. Install python3-pip For Arch Linux:
```
sudo pacman -S python-pip
```
3. Install python3-pip For Fedora:
```
sudo dnf install python3-pip
```
4. Install python3-pip For OpenSUSE Tumbleweed:
```
sudo zypper install python3-pip
```

* [flatpak](https://flatpak.org/setup/) is needed for installing Athenaeum.

# Packages:
1. Steam.
2. Wine
3. Gamemode
4. [ProtonGE](https://github.com/GloriousEggroll/proton-ge-custom)(Optional).
5. [Lutris](https://github.com/lutris/lutris.git).
6. [Heroic](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher.git) (Needs AUR enabled on Arch Linux)
7. [Athenaeum](https://gitlab.com/librebob/athenaeum.git) Launcher for FOSS games.
8. [mangohud](https://github.com/flightlessmango/MangoHud.git) and [goverlay](https://github.com/benjamimgois/goverlay.git).

# Installation:
* You can install LibreGaming using pip if you have it installed. click [Here](https://github.com/Ahmed-Al-Balochi/LibreGaming#dependencies) to install pip3:
```
pip3 install LibreGaming
```
* Or you can install LibreGaming script by entering these commands:
```
git clone https://github.com/Ahmed-Al-Balochi/LibreGaming.git LibreGaming/ 
cd LibreGaming/
python3 setup.py install --user

```
* LibreGaming: command not found. 

This error can be solved by setting up the PATH in your shell you can do this by entering these lines in your shell file(.bashrc or .zshrc)
* Note that the LibreGaming Script is saved in ~/.local/bin directory by default.
```
### PATH

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi
```

# Usage:
* To run the LibreGaming Script to install both the Gaming packages and ProtonGE enter this command:
Please note that this command installs everytning except Athenaeum.
```
LibreGaming -a
```
* To run the LibreGaming Script to only install ProtonGE enter this command:
```
LibreGaming -p
```
* To run the LibreGaming Script to only install the Gaming packages enter this command:
```
LibreGaming -g
```
* To run the LibreGaming Script to only install Athenaeum Launcher enter this command:
```
LibreGaming -ath
```
* To run the LibreGaming Script to install gaming packages, ProtonGE, and Athenaeum Launcher enter this command:
```
LibreGaming -a -ath
```

# VideoDemo:
* This a my video demonstrating LibreGaming in [English](https://www.youtube.com/watch?v=F9GP5Et12qo). And click here for [Arabic](https://www.youtube.com/watch?v=QI8Ai8BTMwo)
* This is a video demonstrating LibreGaming made by TechHut:
https://www.youtube.com/watch?v=2f2zdViFDYg

# Feedback:
* Tell me what distro to add if yours is not available. And what features you'd like to see.
* Also please report if there are any bugs in the script.
* Your feedback is always welcome.

# Credits:
* Thanks to [GloriousEggroll](https://github.com/GloriousEggroll/) for ProtonGE.
* Thanks to [AUNaseef](https://github.com/AUNaseef/) protonup for making it easier to install ProtonGE.
* Thanks to [flightlessmango](https://github.com/flightlessmango/) for mangohud.
* Thanks to [benjamimgois](https://github.com/benjamimgois/) for goverlay.
* Thanks to anyone who downloads this script, and to everyone who gives me feedback.  
