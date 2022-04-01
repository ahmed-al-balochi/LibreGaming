import subprocess, wget, requests

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

# For installing Heroic
    def OpenSUSE_Heroic(self): 
        whoami = str(subprocess.getoutput("whoami"))
        if whoami == "root":
           print("\nPlease run LibreGaming for OpenSUSE Heroic without sudo or doas command, so that it installs correctly\n")
        else:
            print('Downloading Heroic latest AppImage')
            url = 'https://api.github.com/repos/Heroic-Games-Launcher/HeroicGamesLauncher/releases/latest'
            r = requests.get(url).json()
            for i in r['assets']:
                if  i['name'].endswith('.AppImage'):
                    url= i['browser_download_url']
            wget.download(url, "heroic.AppImage")
            os.system("chmod +x heroic.AppImage && mv heroic.AppImage ~/Downloads && cd ~/Downloads && ./heroic.AppImage")