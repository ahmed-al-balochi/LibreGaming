import os, subprocess

class Common_Pkgs:
    """
    Here are all the pkgs that are distro agnostic
    """

    # installation for Itch.io store
    def itch(self):
        whoami = str(subprocess.getoutput("whoami"))
        if whoami == "root":
            print("Please run LibreGaming without the sudo or doas command to install itch correctly")
        else:
            print('Downloading itch.io')
            os.system("wget 'https://itch.io/app/download?platform=linux' -O itch-setup")
            os.system("chmod +x itch-setup && ./itch-setup")

    # installation for Athenaeum store For FOSS games
    def Athenaeum(self):
        whoami = str(subprocess.getoutput("whoami"))
        if whoami == "root":
            print("Please run LibreGaming without the sudo or doas command to install Athenaeum correctly")
        else:
            os.system("flatpak install flathub com.gitlab.librebob.Athenaeum -y")
