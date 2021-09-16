# LibreGaming
Python Program that downloads gaming required packages based on your Linux Distribution.

[![Downloads](https://static.pepy.tech/personalized-badge/libregaming?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/libregaming) ![PyPI](https://img.shields.io/pypi/v/libregaming?color=ge&label=Version) [![Support me on Patreon](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.vercel.app%2Fapi%3Fusername%3Duser%3Fu%3D42792180%26type%3Dpatrons&style=flat)](https://patreon.com/user?u=42792180)

Table of contents
=================

 - [Distributions](#Distributions)
 - [Prerequisites](#Prerequisites)
     - [Dependencies](#Dependencies)
 - [Packages](#Packages)
 - [Installation](#Installation)
 - [Usage](#Usage)
     - [ProtonupCommands](#ProtonupCommands)
 - [VideoDemo](#VideoDemo)
 - [Feedback](#Feedback)
 - [Credits](#Credits)


# Distributions:
* I tested this script on these distributions. but it should also work on their derivatives too.
1. Ubuntu.
2. Arch Linux.
3. Fedora.
4. OpenSUSE Tumbleweed.

# Prerequisites:
* You need your drivers installed beforehand for maximum performance under Linux. you can install them by going to this [page](https://github.com/lutris/docs/blob/master/InstallingDrivers.md)

* To run this LibreGaming script you need python3 installed if not already. to install python3 click [Here](https://github.com/Ahmed-Al-Balochi/LibreGaming#dependencies).
* Also you need to enable free and nonfree packages if you are using Fedora to install steam. You can find the commands to enable free and nonfree packages for Fedora [here](https://docs.fedoraproject.org/en-US/quick-docs/setup_rpmfusion/#proc_enabling-the-rpmfusion-repositories-using-command-line-utilities_enabling-the-rpmfusion-repositories):

* For OpenSUSE Tumbleweed you need to enable packman repos to install Steam and other packages. You can find that [here](https://en.opensuse.org/Additional_package_repositories)

* If you are using Arch Linux or an Arch based system you need to enable 32bit packages found in multilib repo you can enable it by going to this [Arch wiki page](https://wiki.archlinux.org/title/official_repositories#multilib).

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

* [Flatpak](https://flatpak.org/setup/) is needed for installing Athenaeum.

# Packages:
1. Steam.
2. Wine-Staging.
3. [Gamemode](https://github.com/FeralInteractive/gamemode).
4. [ProtonGE](https://github.com/GloriousEggroll/proton-ge-custom)(You Must run Steam at least once before installing ProtonGE).
5. [Lutris](https://github.com/lutris/lutris.git).
6. [Heroic](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher.git) (Needs AUR enabled on Arch Linux)
7. [Athenaeum](https://gitlab.com/librebob/athenaeum.git) Launcher for FOSS games.
8. [mangohud](https://github.com/flightlessmango/MangoHud.git) and [goverlay](https://github.com/benjamimgois/goverlay.git)(Needs AUR enabled on Arch Linux).
9. [Protonup](https://github.com/AUNaseef/protonup).

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
* To update LibreGaming when there is a new release enter this command:
```
pip install LibreGaming -U
```

* LibreGaming: command not found. 

This error can be solved by setting up the PATH in your shell you can do this by entering these lines in your shell file(.bashrc or .zshrc) and by default your shell file is hidden by default. 
* Note that the LibreGaming Script is saved in ~/.local/bin directory by default.
```
### PATH

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi
```

# Usage:
* Note: you can also run this script using ```libregaming``` command if you don't like ```LibreGaming```. Both can be used, so choose what you prefer.
* To install all the Gaming packages mentioned in the packages section enter this command:
```
LibreGaming -g
```
* To install Basic Packages(Wine, Steam, Gamemode):
```
LibreGaming -b
```
* To only install ProtonGE enter this command:
```
LibreGaming -p
```
* To only install Athenaeum Launcher enter this command:
```
LibreGaming -ath
```
* To install gaming packages, ProtonGE, and Athenaeum Launcher enter this command:
```
LibreGaming -g -p -ath
```
## ProtonupCommands
* To list all the available releases of ProtonGE enter this command:
```
LibreGaming -r
```
* To list all the installed verions of ProtonGE enter this command:
```
LibreGaming -l
```
* To install a specfic release of ProtonGE enter this command:
for example:
```
LibreGaming -t 6.13-GE-1
```
* To delete a specfic release of ProtonGE enter this command:
for example:
```
LibreGaming -rm 6.13-GE-1
```

# VideoDemo:
* This a my video demonstrating LibreGaming in [English](https://www.youtube.com/watch?v=F9GP5Et12qo). And click here for [Arabic](https://www.youtube.com/watch?v=QI8Ai8BTMwo)
* This is a video demonstrating LibreGaming made by TechHut:
https://www.youtube.com/watch?v=2f2zdViFDYg
* This is a video demonstrating LibreGaming made by @BrodieRobertson:
https://www.youtube.com/watch?v=sOch-qZMLq0&t=309s

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
