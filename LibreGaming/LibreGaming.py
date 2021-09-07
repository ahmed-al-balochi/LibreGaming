import os, subprocess
import argparse

global distro
distro = ["apt","yay", "paru", "pacman", "dnf"]
global PackageManager 
dir = os.path.dirname(__file__)
script = os.path.join(dir, 'getPackageManager.sh') # get the path to the package manager script
PackageManager = subprocess.getoutput("sh "+script)      # run the script 
#print (PackageManager)

def installPkgs():
    if PackageManager == distro[0]:  #packages for Ubuntu and Ubuntu based distros
        print("\nNow installing Ubuntu Gaming Packages")
        ReleaseCodename = subprocess.getoutput("lsb_release -cs")
        Ubuntu = [
            "wget -nc https://dl.winehq.org/wine-builds/winehq.key",
            "sudo apt-key add winehq.key",
            "sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ " + ReleaseCodename + " main' -y",
            "sudo add-apt-repository ppa:lutris-team/lutris -y",
            "sudo add-apt-repository multiverse -y",
            "sudo add-apt-repository ppa:flexiondotorg/mangohud -y",
            "sudo apt update",
            "sudo apt install --install-recommends winehq-staging -y",
            "sudo apt install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386 -y",
            "sudo apt install winetricks lutris python3-pip meson libsystemd-dev pkg-config ninja-build git libdbus-1-dev libinih-dev dbus-user-session steam goverlay -y"
            ]  
        for i in Ubuntu:
            os.system(i) #running each element in Ubuntu array 

    elif PackageManager == distro[1] or PackageManager == distro[2]:    #packages for Arch and Arch based distros
        print("\nNow installing Arch Gaming Packages")   #for those who have AUR(yay or paru) enabled
        Arch = PackageManager+" -S goverlay-bin python-pip wine-staging winetricks giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader lutris steam gamemode --needed --noconfirm"
        os.system(Arch)
    elif PackageManager == distro[3]:    
        print("\nNow installing Arch Gaming Packages")
        Arch = "pacman -S python-pip wine-staging winetricks giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader lutris steam gamemode --needed --noconfirm"
        os.system(Arch)
    elif PackageManager == distro[4]:    #packages for Fedora
        print("\nNow installing Fedora Gaming Packages")                                            
        Fedora = [
        "wget  https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks", #installing winetricks here
        "chmod +x winetricks",
        "sudo mv winetricks /usr/local/bin/",
        "sudo dnf install python3-pip wine lutris gamemode goverlay steam alsa-plugins-pulseaudio.i686 glibc-devel.i686 glibc-devel libgcc.i686 libX11-devel.i686 freetype-devel.i686 libXcursor-devel.i686 libXi-devel.i686 libXext-devel.i686 libXxf86vm-devel.i686 libXrandr-devel.i686 libXinerama-devel.i686 mesa-libGLU-devel.i686 mesa-libOSMesa-devel.i686 libXrender-devel.i686 libpcap-devel.i686 ncurses-devel.i686 libzip-devel.i686 lcms2-devel.i686 zlib-devel.i686 libv4l-devel.i686 libgphoto2-devel.i686 cups-devel.i686 libxml2-devel.i686 openldap-devel.i686 libxslt-devel.i686 gnutls-devel.i686 libpng-devel.i686 flac-libs.i686 json-c.i686 libICE.i686 libSM.i686 libXtst.i686 libasyncns.i686 liberation-narrow-fonts.noarch libieee1284.i686 libogg.i686 libsndfile.i686 libuuid.i686 libva.i686 libvorbis.i686 libwayland-client.i686 libwayland-server.i686 llvm-libs.i686 mesa-dri-drivers.i686 mesa-filesystem.i686 mesa-libEGL.i686 mesa-libgbm.i686 nss-mdns.i686 ocl-icd.i686 pulseaudio-libs.i686 sane-backends-libs.i686 tcp_wrappers-libs.i686 unixODBC.i686 samba-common-tools.x86_64 samba-libs.x86_64 samba-winbind.x86_64 samba-winbind-clients.x86_64 samba-winbind-modules.x86_64 mesa-libGL-devel.i686 fontconfig-devel.i686 libXcomposite-devel.i686 libtiff-devel.i686 openal-soft-devel.i686 mesa-libOpenCL-devel.i686 opencl-utils-devel.i686 alsa-lib-devel.i686 gsm-devel.i686 libjpeg-turbo-devel.i686 pulseaudio-libs-devel.i686 pulseaudio-libs-devel gtk3-devel.i686 libattr-devel.i686 libva-devel.i686 libexif-devel.i686 libexif.i686 glib2-devel.i686 mpg123-devel.i686 mpg123-devel.x86_64 libcom_err-devel.i686 libcom_err-devel.x86_64 libFAudio-devel.i686 libFAudio-devel.x86_64 -y"
        ]
        for i in Fedora:
            os.system(i) #running each element in Fedora array
    else:
        print("Your distro is not supported or was not found :(")
        exit()
           
def parse_arguments():
    #Parse commandline arguments
    parser = argparse.ArgumentParser(usage="%(prog)s", description="Install Gaming Packages with ease",
                                     epilog="GPLv3 - Repo : https://github.com/Ahmed-Al-Balochi/LibreGaming.git")
    parser.add_argument('-a', '--all', action='store_true', help='Install both ProtonGE and Gaming Packages')
    parser.add_argument('-p', '--proton', action='store_true', help='Install/Update ProtonGE')
    parser.add_argument('-g', '--gaming', action='store_true', help='Install Gaming Packages only')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.proton:
        os.system("protonup")
    if args.gaming:
        installPkgs()
    if args.all:
        installPkgs()
        os.system("protonup")

if __name__ == "__main__":
    main()
