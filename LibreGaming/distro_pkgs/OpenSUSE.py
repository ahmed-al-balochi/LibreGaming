class OpenSUSE:
    """
    Here are all the pkgs that LibreGaming installs for OpenSUSE
    """

# For installing Basic Packages like Steam, Wine, Gamemode 
    OpenSUSE_Basics = [
        " zypper addrepo https://download.opensuse.org/repositories/games:tools/openSUSE_Tumbleweed/games:tools.repo",
        " zypper refresh",
        " zypper install -y steam wine-staging gamemode",
        " zypper update -y"
    ]

# For installing Lutris
    OpenSUSE_Lutris = " zypper install -y lutris"       

# For installing The FPS programs and overlays
    OpenSUSE_Overlays = " zypper install -y goverlay"

# For installing Heroic
    def OpenSUSE_Heroic(): 
        print('Downloading Heroic latest AppImage')
        url = 'https://api.github.com/repos/Heroic-Games-Launcher/HeroicGamesLauncher/releases/latest'
        r = requests.get(url).json()
        for i in r['assets']:
            if  i['name'].endswith('.AppImage'):
                url= i['browser_download_url']
        wget.download(url, "heroic.AppImage")
        os.system("chmod +x heroic.AppImage && mv heroic.AppImage ~/Downloads && cd ~/Downloads && ./heroic.AppImage")