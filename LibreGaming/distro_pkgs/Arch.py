class Arch:
    """ 
    Here are all the pkgs that LibreGaming installs for Arch Linux
    """

    PackageManager = ""

# For installing Basic Packages like Steam, Wine, Gamemode 
    Arch_AUR_Basics = PackageManager + " -Syu python-pip wine-staging winetricks steam gamemode giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader -y --needed --noconfirm"
    Arch_Basics = " pacman -Syu python-pip wine-staging winetricks steam gamemode giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader -y --needed --noconfirm"

# For installing Lutris
    Arch_Lutris = " pacman -S python-evdev lutris -y --needed --noconfirm"

# For installing Heroic
    Arch_AUR_Heroic = PackageManager + " -S heroic-games-launcher-bin -y --needed --noconfirm"

# For installing The FPS programs and overlays
    Arch_AUR_Overlays = PackageManager + " -S goverlay-bin -y --needed --noconfirm"

# For installing Steam Tinker Lanuch
    Arch_AUR_STL = PackageManager + " -S steamtinkerlaunch -y --needed --noconfirm"

def __init__(self):
    distro = ["apt","yay", "paru", "pacman", "dnf", "zypper"]
    PackageManager = ""
    dir = os.path.dirname(__file__)
    PKGmanScript = os.path.join(dir, 'getPackageManager.sh') # get the path to the package manager script
    PackageManager = subprocess.getoutput("sh "+PKGmanScript)      # run the script
