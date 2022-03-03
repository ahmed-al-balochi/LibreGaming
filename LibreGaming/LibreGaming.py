import os, subprocess, argparse, wget, requests


#TODO make an option to install specifc packages.

global distro
distro = ["apt","yay", "paru", "pacman", "dnf", "zypper"]
global PackageManager 
dir = os.path.dirname(__file__)
PKGmanScript = os.path.join(dir, 'getPackageManager.sh') # get the path to the package manager script
PackageManager = subprocess.getoutput("sh "+PKGmanScript)      # run the script

rootScript = os.path.join(dir, 'getRoot.sh') # get the path to the root script
global rootCommand
rootCommand = subprocess.getoutput("sh "+rootScript)      # gets the rootCommand like sudo doas if both dont exist it will fall back to su -

def installAllPkgs():
    BasicPkgs()
    Lutris()
    Heroic()
    Overlays()
    itch()


def BasicPkgs():
    if PackageManager == distro[0]:  #packages for Ubuntu and Ubuntu based distros
        print("\nNow installing Ubuntu Gaming Packages")
        ReleaseCodename = subprocess.getoutput("lsb_release -cs")
        Ubuntu = [
            rootCommand + " dpkg --add-architecture i386",
            "wget -nc https://dl.winehq.org/wine-builds/winehq.key",
            rootCommand + " apt-key add winehq.key",
            rootCommand + " add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ " + ReleaseCodename + " main' -y",
            rootCommand + " add-apt-repository multiverse -y",
            rootCommand + " apt update",
            rootCommand + " apt install --install-recommends winehq-staging -y",
            rootCommand + " apt install steam winetricks python3-pip gawk curl meson libsystemd-dev pkg-config ninja-build git libdbus-1-dev libinih-dev dbus-user-session libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386 -y"
            ]  
        for i in Ubuntu:
            os.system(i) #running each element in Ubuntu array 

    elif PackageManager == distro[1] or PackageManager == distro[2]:    #packages for Arch and Arch based distros
        print("\nNow installing Arch Gaming Packages")   #for those who have AUR(yay or paru) enabled
        Arch = PackageManager + " -Syu python-pip wine-staging winetricks steam gamemode giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader -y --needed --noconfirm"
        os.system(Arch)
    elif PackageManager == distro[3]:    
        print("\nNow installing Arch Gaming Packages")
        Arch = rootCommand + " pacman -Syu python-pip wine-staging winetricks steam gamemode giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader -y --needed --noconfirm"
        os.system(Arch)
    elif PackageManager == distro[4]:    #packages for Fedora
        print("\nNow installing Fedora Gaming Packages")
        os.system(rootCommand + " dnf install redhat-lsb-core -y")
        ReleaseNumber = int(subprocess.getoutput("lsb_release -rs"))
        if ReleaseNumber >= 33:                                           
            Fedora = [
            "wget  https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks", #installing winetricks here
            "chmod +x winetricks",
            rootCommand + " mv winetricks /usr/local/bin/",
            rootCommand + " dnf config-manager --add-repo https://dl.winehq.org/wine-builds/fedora/"+ str(ReleaseNumber) +"/winehq.repo",
            rootCommand + " dnf update -y",
            rootCommand + " dnf install python3-pip wine-staging gamemode steam alsa-plugins-pulseaudio.i686 glibc-devel.i686 glibc-devel libgcc.i686 libX11-devel.i686 freetype-devel.i686 libXcursor-devel.i686 libXi-devel.i686 libXext-devel.i686 libXxf86vm-devel.i686 libXrandr-devel.i686 libXinerama-devel.i686 mesa-libGLU-devel.i686 mesa-libOSMesa-devel.i686 libXrender-devel.i686 libpcap-devel.i686 ncurses-devel.i686 libzip-devel.i686 lcms2-devel.i686 zlib-devel.i686 libv4l-devel.i686 libgphoto2-devel.i686 cups-devel.i686 libxml2-devel.i686 openldap-devel.i686 libxslt-devel.i686 gnutls-devel.i686 libpng-devel.i686 flac-libs.i686 json-c.i686 libICE.i686 libSM.i686 libXtst.i686 libasyncns.i686 liberation-narrow-fonts.noarch libieee1284.i686 libogg.i686 libsndfile.i686 libuuid.i686 libva.i686 libvorbis.i686 libwayland-client.i686 libwayland-server.i686 llvm-libs.i686 mesa-dri-drivers.i686 mesa-filesystem.i686 mesa-libEGL.i686 mesa-libgbm.i686 nss-mdns.i686 ocl-icd.i686 pulseaudio-libs.i686 sane-backends-libs.i686 tcp_wrappers-libs.i686 unixODBC.i686 samba-common-tools.x86_64 samba-libs.x86_64 samba-winbind.x86_64 samba-winbind-clients.x86_64 samba-winbind-modules.x86_64 mesa-libGL-devel.i686 fontconfig-devel.i686 libXcomposite-devel.i686 libtiff-devel.i686 openal-soft-devel.i686 mesa-libOpenCL-devel.i686 opencl-utils-devel.i686 alsa-lib-devel.i686 gsm-devel.i686 libjpeg-turbo-devel.i686 pulseaudio-libs-devel.i686 pulseaudio-libs-devel gtk3-devel.i686 libattr-devel.i686 libva-devel.i686 libexif-devel.i686 libexif.i686 glib2-devel.i686 mpg123-devel.i686 mpg123-devel.x86_64 libcom_err-devel.i686 libcom_err-devel.x86_64 libFAudio-devel.i686 libFAudio-devel.x86_64 -y"
            ]
        else:
            print("Can't install wine-staging Because your Fedora version is less than 33. Installing wine from Fedora repo")
            Fedora = [
            "wget  https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks", #installing winetricks here
            "chmod +x winetricks",
            rootCommand + " mv winetricks /usr/local/bin/",
            rootCommand + " dnf update -y",
            rootCommand + " dnf install python3-pip wine gamemode steam alsa-plugins-pulseaudio.i686 glibc-devel.i686 glibc-devel libgcc.i686 libX11-devel.i686 freetype-devel.i686 libXcursor-devel.i686 libXi-devel.i686 libXext-devel.i686 libXxf86vm-devel.i686 libXrandr-devel.i686 libXinerama-devel.i686 mesa-libGLU-devel.i686 mesa-libOSMesa-devel.i686 libXrender-devel.i686 libpcap-devel.i686 ncurses-devel.i686 libzip-devel.i686 lcms2-devel.i686 zlib-devel.i686 libv4l-devel.i686 libgphoto2-devel.i686 cups-devel.i686 libxml2-devel.i686 openldap-devel.i686 libxslt-devel.i686 gnutls-devel.i686 libpng-devel.i686 flac-libs.i686 json-c.i686 libICE.i686 libSM.i686 libXtst.i686 libasyncns.i686 liberation-narrow-fonts.noarch libieee1284.i686 libogg.i686 libsndfile.i686 libuuid.i686 libva.i686 libvorbis.i686 libwayland-client.i686 libwayland-server.i686 llvm-libs.i686 mesa-dri-drivers.i686 mesa-filesystem.i686 mesa-libEGL.i686 mesa-libgbm.i686 nss-mdns.i686 ocl-icd.i686 pulseaudio-libs.i686 sane-backends-libs.i686 tcp_wrappers-libs.i686 unixODBC.i686 samba-common-tools.x86_64 samba-libs.x86_64 samba-winbind.x86_64 samba-winbind-clients.x86_64 samba-winbind-modules.x86_64 mesa-libGL-devel.i686 fontconfig-devel.i686 libXcomposite-devel.i686 libtiff-devel.i686 openal-soft-devel.i686 mesa-libOpenCL-devel.i686 opencl-utils-devel.i686 alsa-lib-devel.i686 gsm-devel.i686 libjpeg-turbo-devel.i686 pulseaudio-libs-devel.i686 pulseaudio-libs-devel gtk3-devel.i686 libattr-devel.i686 libva-devel.i686 libexif-devel.i686 libexif.i686 glib2-devel.i686 mpg123-devel.i686 mpg123-devel.x86_64 libcom_err-devel.i686 libcom_err-devel.x86_64 libFAudio-devel.i686 libFAudio-devel.x86_64 -y"
            ]
        for i in Fedora:
            os.system(i) #running each element in Fedora array
    elif PackageManager == distro[5]:    #packages for OpenSUSE
        print("\nNow installing OpenSUSE Gaming Packages")
        OpenSUSE = rootCommand + " zypper install steam wine-staging gamemode -y"       
        os.system(rootCommand + " zypper update -y")
        os.system(OpenSUSE)
    else:
        print("Your distro is not supported or was not found :(")
        exit()

def Lutris():
    if PackageManager == distro[0]:  #packages for Ubuntu and Ubuntu based distros
        print("\ninstalling Lutris for Ubuntu")
        Ubuntu = [
            rootCommand + " dpkg --add-architecture i386",
            rootCommand + " add-apt-repository ppa:lutris-team/lutris -y",
            rootCommand + " apt update",
            rootCommand + " apt install lutris -y"
            ]  
        for i in Ubuntu:
            os.system(i) #running each element in Ubuntu array 
    elif PackageManager == distro[1] or PackageManager == distro[2] or PackageManager == distro[3]:    
        print("\ninstalling Lutris for Arch")
        Arch = rootCommand + " pacman -S python-evdev lutris -y --needed --noconfirm"
        os.system(Arch)
    elif PackageManager == distro[4]:    #packages for Fedora
        print("\ninstalling Lutris for Fedora")
        Fedora = rootCommand + " dnf install lutris -y"
        os.system(Fedora) #running each element in Fedora array
    elif PackageManager == distro[5]:    #packages for OpenSUSE
        print("\ninstalling Lutris for OpenSUSE")
        OpenSUSE = rootCommand + " zypper install lutris -y"       
        os.system(OpenSUSE)
    else:
        print("Your distro is not supported or was not found :(")
        exit()

def Heroic():
    if PackageManager == distro[0]:  #packages for Ubuntu and Ubuntu based distros
        print('Downloading Heroic latest dpkg')
        url = 'https://api.github.com/repos/Heroic-Games-Launcher/HeroicGamesLauncher/releases/latest'
        r = requests.get(url).json()
        for i in r['assets']:
            if  i['name'].endswith('.deb'):
                url= i['browser_download_url']
        wget.download(url, "heroic.deb")
        os.system(rootCommand + " dpkg -i heroic.deb")

    elif PackageManager == distro[1] or PackageManager == distro[2]:    #packages for Arch and Arch based distros
        print("\ninstalling Heroic for Arch")
        Arch = PackageManager + " -S heroic-games-launcher-bin -y --needed --noconfirm"
        os.system(Arch)
    elif PackageManager == distro[3]:    
        print("\nYou need to have AUR helpers like yay,paru to install Heroic")
    elif PackageManager == distro[4]:    #packages for Fedora
        Fedora = [
        rootCommand + " dnf copr enable atim/heroic-games-launcher -y",
        rootCommand + " dnf update -y",
        rootCommand + " dnf install heroic-games-launcher-bin -y"
            ]
        for i in Fedora:
            os.system(i) #running each element in Fedora array
    elif PackageManager == distro[5]:    #packages for OpenSUSE
        print('Downloading Heroic latest AppImage')
        url = 'https://api.github.com/repos/Heroic-Games-Launcher/HeroicGamesLauncher/releases/latest'
        r = requests.get(url).json()
        for i in r['assets']:
            if  i['name'].endswith('.AppImage'):
                url= i['browser_download_url']
        wget.download(url, "heroic.AppImage")
        os.system("chmod +x heroic.AppImage && mv heroic.AppImage ~/Downloads && cd ~/Downloads && ./heroic.AppImage")
    else:
        print("Your distro is not supported or was not found :(")
        exit()

def Overlays():
    if PackageManager == distro[0]:  #packages for Ubuntu and Ubuntu based distros
        print("\ninstalling Mangohud and Goverlay for Ubuntu")
        Ubuntu = [
            rootCommand + " dpkg --add-architecture i386",
            rootCommand + " add-apt-repository ppa:flexiondotorg/mangohud -y",
            rootCommand + " apt update",
            rootCommand + " apt install goverlay -y"
            ]  
        for i in Ubuntu:
            os.system(i) #running each element in Ubuntu array 
    elif PackageManager == distro[1] or PackageManager == distro[2]:    #packages for Arch and Arch based distros
        print("\ninstalling Mangohud and Goverlay for Arch")
        Arch = PackageManager + " -S goverlay-bin -y --needed --noconfirm"
        os.system(Arch)
    elif PackageManager == distro[3]:    
        print("\nYou need to have AUR helpers like yay,paru to install Mangohud and Goverlay")
    elif PackageManager == distro[4]:    #packages for Fedora
        print("\ninstalling Mangohud and Goverlay for Fedora")
        Fedora = rootCommand + " dnf install goverlay -y"
        os.system(Fedora) #running each element in Fedora array
    elif PackageManager == distro[5]:    #packages for OpenSUSE
        print("\ninstalling Mangohud and Goverlay for OpenSUSE")
        OpenSUSE = rootCommand + " zypper install goverlay -y"       
        os.system(OpenSUSE)
    else:
        print("Your distro is not supported or was not found :(")
        exit()

def itch():
        print('Downloading itch.io')
        os.system("wget 'https://itch.io/app/download?platform=linux' -O itch-setup")
        os.system("chmod +x itch-setup && ./itch-setup && wget 'https://itch.io/app/download?platform=linux' -o itch-setup")

def parse_arguments():
    #Parse commandline arguments
    parser = argparse.ArgumentParser(usage="%(prog)s <arguments>", description="Install Gaming Packages with ease",
                                     epilog="GPLv3 - Repo : https://github.com/Ahmed-Al-Balochi/LibreGaming.git")
    parser.add_argument('-g', '--gaming', action='store_true', help='Install Gaming Packages ')
    parser.add_argument('-b', '--basic', action='store_true', help='Install Basic Gaming Packages')
    parser.add_argument('-ath', '--athenaeum', action='store_true', help='Install Athenaeum Launcher')
    parser.add_argument('-o', '--overlays', action='store_true', help='Install Mangohud & Goverlay')
    parser.add_argument('-p', '--proton', action='store_true', help='Install/Update ProtonGE(You must run Steam once before installing ProtonGE)')
    parser.add_argument('-l', '--list', action='store_true', help='List installed ProtonGE Releases')
    parser.add_argument('-t', '--tag', action='store',type=str, default=None, help='Install a specific ProtonGE Release')
    parser.add_argument('-r', '--rem', action='store', type=str, default=None, metavar='TAG', help='remove a specific ProtonGE Release')
    parser.add_argument('--releases', action='store_true', help='List ProtonGE Releases')
    parser.add_argument('--tui', action='store_true', help='use a Terminal User Interface to install Packages ')
    parser.add_argument('--heroic', action='store_true', help='Install Heroic Launcher')
    parser.add_argument('--lutris', action='store_true', help='Install lutris Launcher')
    parser.add_argument('--itch', action='store_true', help='Install itch.io Launcher')
    parser.add_argument('--stl', action='store_true', help='Install Steam Tinker Launch(For Arch Linux only)')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.tui:
        dir = os.path.dirname(__file__)
        tui = os.path.join(dir, 'TUI.py') # get the path to the package manager script
        os.system("python3 "+tui)
    if args.proton:
        os.system("protonup")
    if args.releases:
        os.system("protonup --releases")
    if args.list:
        os.system("protonup -l")
    if args.tag:
        os.system("protonup -t " + args.tag)
    if args.rem:
        os.system("protonup -r " + args.rem)
    if args.gaming:
        installAllPkgs()
    if args.basic:
        BasicPkgs()
    if args.overlays:
        Overlays()
    if args.lutris:
        Lutris()
    if args.heroic:
        Heroic()
    if args.itch:
        itch()
    if args.stl:
        os.system(PackageManager + " -S steamtinkerlaunch -y --needed --noconfirm")      ##gawk git unzip wget xdotool xxd yad
    if args.athenaeum:
        os.system("flatpak install flathub com.gitlab.librebob.Athenaeum -y")

if __name__ == "__main__":
    main()
