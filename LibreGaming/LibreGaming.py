import os, subprocess, argparse, wget, requests

from LibreGaming.distro_pkgs.Arch import Arch 
from LibreGaming.distro_pkgs.Fedora import Fedora
from LibreGaming.distro_pkgs.OpenSUSE import OpenSUSE 
from LibreGaming.distro_pkgs.Ubuntu import Ubuntu 

global distro
distro = ["apt","yay", "paru", "pacman", "dnf", "zypper"]
global PackageManager 
dir = os.path.dirname(__file__)
PKGmanScript = os.path.join(dir, 'getPackageManager.sh') # get the path to the package manager script
PackageManager = subprocess.getoutput("sh "+PKGmanScript)      # run the script

rootScript = os.path.join(dir, 'getRoot.sh') # get the path to the root script
global rootCommand
rootCommand = subprocess.getoutput("sh "+rootScript)      # gets the rootCommand like sudo doas if both dont exist it will fall back to su -

Arch_Object = Arch(PackageManager)
Fedora_Object = Fedora()
OpenSUSE_Object = OpenSUSE()
Ubuntu_Object = Ubuntu()

def installAllPkgs():
    BasicPkgs()
    Lutris()
    Heroic()
    Overlays()
    itch()


def BasicPkgs():
    if PackageManager == distro[0]:  #packages for Ubuntu and Ubuntu based distros
        print("\nNow installing Ubuntu Gaming Packages")
        for i in Ubuntu_Object.Ubuntu_Basics():
            os.system(i) #running each element in Ubuntu array 
    elif PackageManager == distro[1] or PackageManager == distro[2]:    #packages for Arch and Arch based distros
        print("\nNow installing Arch Gaming Packages")   #for those who have AUR(yay or paru) enabled
        os.system(Arch_Object.Arch_AUR_Basics())
    elif PackageManager == distro[3]:    
        print("\nNow installing Arch Gaming Packages")
        os.system(Arch_Object.Arch_Basics)
    elif PackageManager == distro[4]:    #packages for Fedora
        os.system("dnf install redhat-lsb-core -y") # used to get the release version of Fedora using "lsb_release -rs"
        ReleaseNumber = subprocess.getoutput("lsb_release -rs")
        print("\nNow installing Fedora " + ReleaseNumber +" Gaming Packages")
        if ReleaseNumber >= '33':                                           
            for i in Fedora_Object.Fedora_33_Basics:
                os.system(i) #running each element in Fedora array from distro_pkgs/Fedora
        else:
            print("can't install wine-staging because your fedora version is less than 33. installing wine from fedora repo")
            for i in getattr(Fedora_Object,'Fedora_32_Basics'):
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
        for i in Ubuntu_Object.Ubuntu_Lutris:
            os.system(i) #running each element in Ubuntu array 
    elif PackageManager == distro[1] or PackageManager == distro[2] or PackageManager == distro[3]:    
        print("\ninstalling Lutris for Arch")
        os.system(Arch_Object.Arch_Lutris)
    elif PackageManager == distro[4]:    #packages for Fedora
        print("\ninstalling Lutris for Fedora")
        os.system(getattr(Fedora_Object,'Fedora_Lutris')) #running each element in Fedora array
    elif PackageManager == distro[5]:    #packages for OpenSUSE
        print("\ninstalling Lutris for OpenSUSE")
        OpenSUSE = rootCommand + " zypper install lutris -y"       
        os.system(OpenSUSE)
    else:
        print("Your distro is not supported or was not found :(")
        exit()

def Heroic():
    if PackageManager == distro[0]:  #packages for Ubuntu and Ubuntu based distros
        Ubuntu_Object.Ubuntu_Heroic() #running each element in Ubuntu array 
    elif PackageManager == distro[1] or PackageManager == distro[2]:    #packages for Arch and Arch based distros
        print("\ninstalling Heroic for Arch")
        os.system(Arch_Object.Arch_AUR_Heroic())
    elif PackageManager == distro[3]:
        print("\nYou need to have AUR helpers like yay,paru to install Heroic")
    elif PackageManager == distro[4]:    #packages for Fedora
       for i in getattr(Fedora_Object,'Fedora_Heroic'):
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
        for i in Ubuntu_Object.Ubuntu_Overlay:
            os.system(i) #running each element in Ubuntu array 
    elif PackageManager == distro[1] or PackageManager == distro[2]:    #packages for Arch and Arch based distros
        print("\ninstalling Mangohud and Goverlay for Arch")
        os.system(Arch_Object.Arch_AUR_Overlays())
    elif PackageManager == distro[3]:    
        print("\nYou need to have AUR helpers like yay,paru to install Mangohud and Goverlay")
    elif PackageManager == distro[4]:    #packages for Fedora
        print("\ninstalling Mangohud and Goverlay for Fedora")
        os.system(getattr(Fedora_Object,'Fedora_Overlays')) #running each element in Fedora array
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
    parser.add_argument('-g', '--gaming', action='store_true', help='Install all the Gaming Packages')
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
        if PackageManager == distro[1] or PackageManager == distro[2]:    #packages for Arch and Arch based distros
            print("\ninstalling Steam Tinker Lanuch for Arch")
            os.system(PackageManager + " -S steamtinkerlaunch -y --needed --noconfirm")
        elif PackageManager == distro[3]:    
            print("\nYou need to have AUR helpers like yay,paru to install Heroic")
    if args.athenaeum:
        os.system("flatpak install flathub com.gitlab.librebob.Athenaeum -y")

if __name__ == "__main__":
    main()
