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

    # Initialize objects
    Arch_Object = Arch(None)
    Fedora_Object = Fedora()
    OpenSUSE_Object = OpenSUSE()
    Ubuntu_Object = Ubuntu()
    Common_Pkgs_Object = Common_Pkgs()

    # Initialize the Program
    def __init__(self):
        self.PackageManager = self.getPackageManager()
        self.Arch_Object = Arch(self.PackageManager)

    # Gets the package manager 
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

    # To check if LibreGaming is executed with root or not 
    def whoami(self, authorize):
        whoami = str(subprocess.getoutput("whoami"))
        if whoami == "root" and authorize == False:
           print("\nPlease run LibreGaming without sudo or doas command for this flag")
           exit(0)
        elif whoami != "root" and authorize == True:
           print("\nPlease run LibreGaming with sudo or doas command for this flag")
           exit(0)

    # Used to install all packages 
    def installAllPkgs(self):
        self.BasicPkgs()
        self.Lutris()
        self.Heroic()
        self.Overlays()

    #Used to install Steam, Wine-Staging, Gamemode
    def BasicPkgs(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            self.whoami(True)
            print("\n\tNow Installing Ubuntu Gaming Packages")
            for i in self.Ubuntu_Object.Ubuntu_Basics():
                os.system(i) #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            self.whoami(False)
            print("\n\tNow Installing Arch Gaming Packages")   #for those who have AUR(yay or paru) enabled
            os.system(self.Arch_Object.Arch_AUR_Basics())
        elif self.PackageManager == self.distro[3]:    
            self.whoami(True)
            print("\n\tNow Installing Arch Gaming Packages")
            os.system(self.Arch_Object.Arch_Basics)
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            self.whoami(True)
            os.system("dnf install redhat-lsb-core -y") # used to get the release version of Fedora using "lsb_release -rs"
            ReleaseNumber = subprocess.getoutput("lsb_release -rs")
            print("\n\tNow Installing Fedora " + ReleaseNumber +" Gaming Packages")
            if ReleaseNumber >= '33':                                           
                for i in self.Fedora_Object.Fedora_33_Basics:
                    os.system(i) #running each element in Fedora array from distro_pkgs/Fedora
            else:
                print("can't install wine-staging because your fedora version is less than 33. installing wine from fedora repo")
                for i in self.Fedora_Object.Fedora_32_Basics:
                    os.system(i) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            self.whoami(True)
            print("\n\nNow Installing OpenSUSE Gaming Packages")
            for i in self.OpenSUSE_Object.OpenSUSE_Basics:
                os.system(i) #running each element in OpenSUSE array 
        else:
            print("\n\tYour distro is not supported or was not found :(")
            exit()

    #Used to install Lutris 
    def Lutris(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            self.whoami(True)
            print("\n\tInstalling Lutris for Ubuntu")
            for i in self.Ubuntu_Object.Ubuntu_Lutris:
                os.system(i) #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:
            self.whoami(False)
            print("\n\tInstalling Lutris for Arch using an AUR helper")
            os.system(self.Arch_Object.Arch_Lutris())
        elif self.PackageManager == self.distro[3]:    
            self.whoami(True)
            print("\n\tInstalling Lutris for Arch")
            os.system(self.Arch_Object.Arch_Lutris())
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            self.whoami(True)
            print("\n\tInstalling Lutris for Fedora")
            os.system(self.Fedora_Object.Fedora_Lutris) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            self.whoami(True)
            print("\n\tInstalling Lutris for OpenSUSE")
            os.system(self.OpenSUSE_Object.OpenSUSE_Lutris)
        else:
            print("\n\tYour distro is not supported or was not found :(")
            exit()

    #Used to install Heroic 
    def Heroic(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            self.whoami(True)
            self.Ubuntu_Object.Ubuntu_Heroic() #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            self.whoami(False)
            print("\n\tInstalling Heroic for Arch")
            os.system(self.Arch_Object.Arch_AUR_Heroic())
        elif self.PackageManager == self.distro[3]:
            self.whoami(True)
            print("\n\tYou need to have AUR helpers like yay,paru to install Heroic")
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            self.whoami(True)
            for i in self.Fedora_Object.Fedora_Heroic:
                os.system(i) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            self.OpenSUSE_Object.OpenSUSE_Heroic() #running each element in OpenSUSE array 
        else:
            print("\n\tYour distro is not supported or was not found :(")
            exit()

    #Used to install MangoHud and Goverlay 
    def Overlays(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            self.whoami(True)
            print("\n\tinstalling Mangohud and Goverlay for Ubuntu")
            for i in self.Ubuntu_Object.Ubuntu_Overlay:
                os.system(i) #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            self.whoami(False)
            print("\n\tinstalling Mangohud and Goverlay for Arch")
            os.system(self.Arch_Object.Arch_AUR_Overlays())
        elif self.PackageManager == self.distro[3]:    
            self.whoami(True)
            print("\n\tYou need to have AUR helpers like yay,paru to install Mangohud and Goverlay")
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            self.whoami(True)
            print("\n\tinstalling Mangohud and Goverlay for Fedora")
            os.system(self.Fedora_Object.Fedora_Overlays) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            self.whoami(True)
            print("\n\tinstalling Mangohud and Goverlay for OpenSUSE")
            os.system(self.OpenSUSE_Object.OpenSUSE_Overlays)
        else:
            print("\n\tYour distro is not supported or was not found :(")
            exit()

    #Used to install Minigalaxy
    def Minigalaxy(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            self.whoami(True)
            print("\n\tinstalling Minigalaxy for Ubuntu")
            os.system(self.Ubuntu_Object.Ubuntu_Minigalaxy)
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            self.whoami(False)
            print("\n\tinstalling Minigalaxy for Arch")
            os.system(self.Arch_Object.Arch_AUR_Minigalaxy())
        elif self.PackageManager == self.distro[3]:    
            self.whoami(True)
            print("\n\tYou need to have AUR helpers like yay,paru to install Minigalaxy")
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            self.whoami(True)
            print("\n\tinstalling Minigalaxy for Fedora")
            os.system(self.Fedora_Object.Fedora_Minigalaxy) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            self.whoami(True)
            print("\n\tinstalling Minigalaxy for OpenSUSE")
            os.system(OpenSUSE_Object.OpenSUSE_Minigalaxy)
        else:
            print("\n\tYour distro is not supported or was not found :(")
            exit()

    #Used to install Steam Tinker Lanuch for Arch Linux(AUR) 
    def STL(self):
        self.whoami(False)
        if self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            print("\n\tinstalling Steam Tinker Lanuch for Arch")
            os.system(self.Arch_Object.Arch_AUR_STL())
        elif self.PackageManager == self.distro[3]:    
            print("\n\tYou need to have AUR helpers like yay,paru to install Heroic")

    #Used to install to install the latest ProtonGE release
    def protonup_Install_Latest(self):
        self.whoami(False)
        os.system("protonup")

    #Used to install to show the ProtonGE releases
    def protonup_Show_Releases(Self):
        self.whoami(False)
        os.system("protonup --releases")

    #Used to install to list all installed ProtonGE on your system
    def protonup_List(Self):
        self.whoami(False)
        os.system("protonup -l")

    #Used to install a specific ProtonGE
    def protonup_Install_Specific(Self):
        self.whoami(False)
        os.system("protonup -t " + args.tag)

    #Used to remove a specific ProtonGE
    def protonup_Remove(Self):
        self.whoami(False)
        os.system("protonup -r " + args.rem)
