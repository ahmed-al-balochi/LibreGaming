import subprocess, wget, requests

class Ubuntu:
    """
    Here are all the pkgs that LibreGaming installs for Ubuntu
    """

# Saves the Ubuntu release codename. For example: focal fossa 
    ReleaseCodename =  ""

# For installing Lutris
    Ubuntu_Lutris = [
        ["dpkg", "--add-architecture", "i386"],
        ["add-apt-repository", "ppa:lutris-team/lutris", "-y"],
        ["apt", "update"],
        ["apt", "install", "lutris", "-y"]
        ]

# For installing The FPS programs and overlays
    Ubuntu_Overlay = [
        ["dpkg", "--add-architecture", "i386"],
        ["add-apt-repository", "ppa:flexiondotorg/mangohud", "-y"],
        ["apt", "update"],
        ["apt", "install", "goverlay", "-y"]
        ]

# For installing Basic Packages like Steam, Wine, Gamemode 
    def Ubuntu_Basics(self):
        basic_pkgs = [
        ["dpkg", "--add-architecture", "i386"],
        ["wget", "-nc", "https://dl.winehq.org/wine-builds/winehq.key"],
        ["apt-key", "add", "winehq.key"],
        ["add-apt-repository", "deb https://dl.winehq.org/wine-builds/ubuntu/ "+ self.ReleaseCodename +" main", "-y"],
        ["add-apt-repository", "multiverse", "-y"],
        ["apt", "update"],
        ["apt", "install", "--install-recommends", "winehq-staging", "-y"],
        ["apt", "install", "steam", "winetricks", "python3-pip", "gawk", "curl", "meson", "libsystemd-dev", "zstd", "pkg-config", "ninja-build", "git", "libdbus-1-dev", "libinih-dev", "dbus-user-session", "libgnutls30:i386", "libgpg-error0:i386", "libxml2:i386", "libasound2-plugins:i386", "libsdl2-2.0-0:i386", "libfreetype6:i386", "libdbus-1-3:i386", "libsqlite3-0:i386", "-y"]
        ]
        return basic_pkgs 

# For installing Heroic
    def Ubuntu_Heroic(self):
        print('Downloading Heroic latest dpkg')
        url = 'https://api.github.com/repos/Heroic-Games-Launcher/HeroicGamesLauncher/releases/latest'
        r = requests.get(url).json()
        for i in r['assets']:
            if  i['name'].endswith('.deb'):
                url= i['browser_download_url']
        wget.download(url, "heroic.deb")
        subprocess.run(["dpkg", "-i", "heroic.deb"])

    def __init__(self):
        distroName = subprocess.getoutput("lsb_release -is")
        if distroName == "Ubuntu":
            self.ReleaseCodename = str(subprocess.getoutput("lsb_release -cs"))
        elif distroName == "Pop":
            self.ReleaseCodename = str(subprocess.getoutput("lsb_release -cs"))
        elif distroName == "Linuxmint":
            self.ReleaseCodename = str(subprocess.getoutput("grep -oP '(?<=DISTRIB_CODENAME=)\w+' /etc/upstream-release/lsb-release"))