# LibreGaming
Python Program that downloads gaming required packages based on your Linux Distribution.


Table of contents
=================

 - [Distributions](#Distributions)
 - [Prerequisites](#Prerequisites)
 - [Packages:](#Packages)
    - [Dependencies](#Dependencies)
 - [Installation](#Installation)
 - [Usage](#Usage)
 - [Feedback](#Feedback)
 - [Credits](#Credits)


# Distributions:
* I tested this script on these three distributions. but it should also work on their derivatives too.
1. Ubuntu.
2. Arch Linux.
3. Fedora.

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

# Packages:
1. Steam.
2. Wine
3. Gamemode
4. [ProtonGE](https://github.com/GloriousEggroll/proton-ge-custom)(Optional).
5. [Lutris](https://github.com/lutris/lutris.git).
6. [mangohud](https://github.com/flightlessmango/MangoHud.git) and [goverlay](https://github.com/benjamimgois/goverlay.git).

## Dependencies:
* git

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
* python3-pip is needed to install [AUNaseef](https://github.com/AUNaseef/protonup.git)'s protonup which is already inlcuded in the script so you don't have to install it yourself.

# Installation:
* You can install LibreGaming using pip:
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
