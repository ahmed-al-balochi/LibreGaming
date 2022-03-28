import os, subprocess, argparse, wget, requests
from LibreGaming.distro_pkgs.Arch import Arch 
from LibreGaming.distro_pkgs.Fedora import Fedora
from LibreGaming.distro_pkgs.OpenSUSE import OpenSUSE 
from LibreGaming.distro_pkgs.Ubuntu import Ubuntu 
from LibreGaming.distro_pkgs.Common_Pkgs import Common_Pkgs 

class LibreGaming:
    """
    Here is where all the magic gets done. 
   """

    PackageManager = ""
    distro = ["apt","yay", "paru", "pacman", "dnf", "zypper"]
    Arch_Object = Arch(None)
    Fedora_Object = Fedora()
    OpenSUSE_Object = OpenSUSE()
    Ubuntu_Object = Ubuntu()
    Common_Pkgs_Object = Common_Pkgs()

    def __init__(self):
        self.PackageManager = self.getPackageManager()
        self.Arch_Object = Arch(self.PackageManager)


    def getPackageManager(self):
        if subprocess.getoutput("$(command -v dnf)"):
            self.PackageManager =  "dnf"
        elif subprocess.getoutput("$(command -v yay)"):
            self.PackageManager =  "yay"
        elif subprocess.getoutput("$(command -v paru)"):
            self.PackageManager =  "paru"
        elif subprocess.getoutput("$(command -v pacman)"):
            self.PackageManager =  "pacman"
        elif subprocess.getoutput("$(command -v apt)"):
            self.PackageManager =  "apt"
        elif subprocess.getoutput("$(command -v zypper)"):
            self.PackageManager =  "zypper"
        else:
            print("Could not know your distro based on your Package Manager!")
        return self.PackageManager

    def installAllPkgs(self):
        BasicPkgs()
        Lutris()
        Heroic()
        Overlays()
        itch()

    def BasicPkgs(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            print("\nNow installing Ubuntu Gaming Packages")
            for i in Ubuntu_Object.Ubuntu_Basics():
                os.system(i) #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            print("\nNow installing Arch Gaming Packages")   #for those who have AUR(yay or paru) enabled
            os.system(self.Arch_Object.Arch_AUR_Basics())
        elif self.PackageManager == self.distro[3]:    
            print("\nNow installing Arch Gaming Packages")
            os.system(self.Arch_Object.Arch_Basics)
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            os.system("dnf install redhat-lsb-core -y") # used to get the release version of Fedora using "lsb_release -rs"
            ReleaseNumber = subprocess.getoutput("lsb_release -rs")
            print("\nNow installing Fedora " + ReleaseNumber +" Gaming Packages")
            if ReleaseNumber >= '33':                                           
                for i in self.Fedora_Object.Fedora_33_Basics:
                    os.system(i) #running each element in Fedora array from distro_pkgs/Fedora
            else:
                print("can't install wine-staging because your fedora version is less than 33. installing wine from fedora repo")
                for i in self.Fedora_Object.Fedora_32_Basics:
                    os.system(i) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
                print("\nNow installing OpenSUSE Gaming Packages")
                for i in OpenSUSE_Object.OpenSUSE_Basics:
                    os.system(i) #running each element in Ubuntu array 
        else:
            print("Your distro is not supported or was not found :(")
            exit()

    def Lutris(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            print("\ninstalling Lutris for Ubuntu")
            for i in Ubuntu_Object.Ubuntu_Lutris:
                os.system(i) #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2] or self.PackageManager == self.distro[3]:    
            print("\ninstalling Lutris for Arch")
            os.system(self.Arch_Object.Arch_Lutris())
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            print("\ninstalling Lutris for Fedora")
            os.system(self.Fedora_Object.Fedora_Lutris) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            print("\ninstalling Lutris for OpenSUSE")
            os.system(OpenSUSE_Object.OpenSUSE_Lutris)
        else:
            print("Your distro is not supported or was not found :(")
            exit()

    def Heroic(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            Ubuntu_Object.Ubuntu_Heroic() #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            print("\ninstalling Heroic for Arch")
            os.system(self.Arch_Object.Arch_AUR_Heroic())
        elif self.PackageManager == self.distro[3]:
            print("\nYou need to have AUR helpers like yay,paru to install Heroic")
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            for i in self.Fedora_Object.Fedora_Heroic:
                os.system(i) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            OpenSUSE_Object.OpenSUSE_Heroic() #running each element in Ubuntu array 
        else:
            print("Your distro is not supported or was not found :(")
            exit()

    def Overlays(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            print("\ninstalling Mangohud and Goverlay for Ubuntu")
            for i in Ubuntu_Object.Ubuntu_Overlay:
                os.system(i) #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            print("\ninstalling Mangohud and Goverlay for Arch")
            os.system(self.Arch_Object.Arch_AUR_Overlays())
        elif self.PackageManager == self.distro[3]:    
            print("\nYou need to have AUR helpers like yay,paru to install Mangohud and Goverlay")
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            print("\ninstalling Mangohud and Goverlay for Fedora")
            os.system(self.Fedora_Object.Fedora_Overlays) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            print("\ninstalling Mangohud and Goverlay for OpenSUSE")
            os.system(OpenSUSE_Object.OpenSUSE_Overlays)
        else:
            print("Your distro is not supported or was not found :(")
            exit()

    def STL(self):
        if self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            print("\ninstalling Steam Tinker Lanuch for Arch")
            os.system(self.Arch_Object.Arch_AUR_STL())
        elif self.PackageManager == self.distro[3]:    
            print("\nYou need to have AUR helpers like yay,paru to install Heroic")

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
    LibreGaming_Object = LibreGaming()
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
        LibreGaming_Object.installAllPkgs()
    if args.basic:
        LibreGaming_Object.BasicPkgs()
    if args.overlays:
        LibreGaming_Object.Overlays()
    if args.lutris:
        LibreGaming_Object.Lutris()
    if args.heroic:
        LibreGaming_Object.Heroic()
    if args.itch:
        LibreGaming_Object.Common_Pkgs_Object.itch()
    if args.stl:
        LibreGaming_Object.STL()
    if args.athenaeum:
        LibreGaming_Object.Common_Pkgs_Object.Athenaeum()

if __name__ == "__main__":
    main()
