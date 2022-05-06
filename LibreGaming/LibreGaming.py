import subprocess, argparse, wget, requests, json, urllib.request, pip
from pip._internal.operations.freeze import freeze
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

    # Initialize the Program
    def __init__(self):
        self.PackageManager = self.getPackageManager()

    # Initialize distro objects
        self.Arch_Object = Arch(self.PackageManager)
        self.Fedora_Object = Fedora()
        self.OpenSUSE_Object = OpenSUSE()
        self.Ubuntu_Object = Ubuntu()
        self.Common_Pkgs_Object = Common_Pkgs()            

    # Gets the package manager by running $(command -v dnf)
    def getPackageManager(self):
        if subprocess.getoutput("command -v dnf"):
            self.PackageManager =  "dnf"
        elif subprocess.getoutput("command -v yay"):
            self.PackageManager =  "yay"
        elif subprocess.getoutput("command -v paru"):
            self.PackageManager =  "paru"
        elif subprocess.getoutput("command -v pacman"):
            self.PackageManager =  "pacman"
        elif subprocess.getoutput("command -v apt"):
            self.PackageManager =  "apt"
        elif subprocess.getoutput("command -v zypper"):
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
                subprocess.run(i) #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            self.whoami(False)
            print("\n\tNow Installing Arch Gaming Packages")   #for those who have AUR(yay or paru) enabled
            subprocess.run(self.Arch_Object.Arch_AUR_Basics())
        elif self.PackageManager == self.distro[3]:    
            self.whoami(True)
            print("\n\tNow Installing Arch Gaming Packages")
            subprocess.run(self.Arch_Object.Arch_Basics)
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            self.whoami(True)
            subprocess.run(["dnf", "install", "redhat-lsb-core", "-y"]) # used to get the release version of Fedora using "lsb_release -rs"
            ReleaseNumber = subprocess.getoutput("lsb_release -rs")
            print("\n\tNow Installing Fedora " + ReleaseNumber +" Gaming Packages")
            if ReleaseNumber >= '33':                                           
                for i in self.Fedora_Object.Fedora_33_Basics:
                    subprocess.run(i) #running each element in Fedora array from distro_pkgs/Fedora
            else:
                print("can't install wine-staging because your fedora version is less than 33. installing wine from fedora repo")
                for i in self.Fedora_Object.Fedora_32_Basics:
                    subprocess.run(i) #running each element in Fedora array from distro_pkgs/Fedora
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            self.whoami(True)
            print("\n\nNow Installing OpenSUSE Gaming Packages")
            for i in self.OpenSUSE_Object.OpenSUSE_Basics:
                subprocess.run(i) #running each element in OpenSUSE array 
        else:
            print("\n\tYour distro is not supported or was not found :(")
            exit()

    #Used to install Lutris 
    def Lutris(self):
        if self.PackageManager == self.distro[0]:  #packages for Ubuntu and Ubuntu based distros
            self.whoami(True)
            print("\n\tInstalling Lutris for Ubuntu")
            for i in self.Ubuntu_Object.Ubuntu_Lutris:
                subprocess.run(i) #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:
            self.whoami(False)
            print("\n\tInstalling Lutris for Arch using an AUR helper")
            subprocess.run(self.Arch_Object.Arch_Lutris())
        elif self.PackageManager == self.distro[3]:    
            self.whoami(True)
            print("\n\tInstalling Lutris for Arch")
            subprocess.run(self.Arch_Object.Arch_Lutris())
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            self.whoami(True)
            print("\n\tInstalling Lutris for Fedora")
            subprocess.run(self.Fedora_Object.Fedora_Lutris)
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            self.whoami(True)
            print("\n\tInstalling Lutris for OpenSUSE")
            subprocess.run(self.OpenSUSE_Object.OpenSUSE_Lutris)
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
            subprocess.run(self.Arch_Object.Arch_AUR_Heroic())
        elif self.PackageManager == self.distro[3]:
            self.whoami(True)
            print("\n\tYou need to have AUR helpers like yay,paru to install Heroic")
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            self.whoami(True)
            for i in self.Fedora_Object.Fedora_Heroic:
                subprocess.run(i) #running each element in Fedora array from distro_pkgs/Fedora
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
                subprocess.run(i) #running each element in Ubuntu array 
        elif self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            self.whoami(False)
            print("\n\tinstalling Mangohud and Goverlay for Arch")
            subprocess.run(self.Arch_Object.Arch_AUR_Overlays())
        elif self.PackageManager == self.distro[3]:    
            self.whoami(True)
            print("\n\tYou need to have AUR helpers like yay,paru to install Mangohud and Goverlay")
        elif self.PackageManager == self.distro[4]:    #packages for Fedora
            self.whoami(True)
            print("\n\tinstalling Mangohud and Goverlay for Fedora")
            subprocess.run(self.Fedora_Object.Fedora_Overlays) #running each element in Fedora array
        elif self.PackageManager == self.distro[5]:    #packages for OpenSUSE
            self.whoami(True)
            print("\n\tinstalling Mangohud and Goverlay for OpenSUSE")
            subprocess.run(self.OpenSUSE_Object.OpenSUSE_Overlays)
        else:
            print("\n\tYour distro is not supported or was not found :(")
            exit()

    #Used to install Steam Tinker Lanuch for Arch Linux(AUR) 
    def STL(self):
        self.whoami(False)
        if self.PackageManager == self.distro[1] or self.PackageManager == self.distro[2]:    #packages for Arch and Arch based distros
            print("\n\tinstalling Steam Tinker Lanuch for Arch")
            subprocess.run(self.Arch_Object.Arch_AUR_STL())
        elif self.PackageManager == self.distro[3]:    
            print("\n\tYou need to have AUR helpers like yay,paru to install Heroic")
