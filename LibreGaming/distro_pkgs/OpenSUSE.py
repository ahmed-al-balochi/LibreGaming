import subprocess, wget, requests, os

class OpenSUSE:
    """
    Here are all the pkgs that LibreGaming installs for OpenSUSE
    """

# For installing Basic Packages like Steam, Wine, Gamemode 
    OpenSUSE_Basics = [
        ["zypper", "install", "-y", "steam", "wine-staging", "gamemoded", "libgamemode0", "libgamemode0-32bit"],
        ["zypper", "update", "-y"]
        ]

# For installing Lutris
    OpenSUSE_Lutris = ["zypper", "install", "-y", "lutris"]

# For installing The FPS programs and overlays
    OpenSUSE_Overlays = ["zypper", "install", "-y", "goverlay"]

