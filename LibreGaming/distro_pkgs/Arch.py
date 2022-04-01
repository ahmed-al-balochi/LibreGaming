import subprocess

class Arch:
    """ 
    Here are all the pkgs that LibreGaming installs for Arch Linux
    """

# Saves the Arch package manager or AUR helpers. For example: pacman, yay
    PackageManager = ""

# For installing Basic Packages like Steam, Wine, Gamemode. For those not using an AUR Helper
    Arch_Basics = ["pacman", "-Syu", "python-pip", "wine-staging", "winetricks", "steam", "gamemode", "giflib", "lib32-giflib", "libpng", "lib32-libpng", "libldap", "lib32-libldap", "gnutls", "lib32-gnutls", "mpg123", "lib32-mpg123", "openal", "lib32-openal", "v4l-utils", "lib32-v4l-utils", "libpulse", "lib32-libpulse", "libgpg-error", "lib32-libgpg-error", "alsa-plugins", "lib32-alsa-plugins", "alsa-lib", "lib32-alsa-lib", "libjpeg-turbo", "lib32-libjpeg-turbo", "sqlite", "lib32-sqlite", "libxcomposite", "lib32-libxcomposite", "libxinerama", "lib32-libgcrypt", "libgcrypt", "lib32-libxinerama", "ncurses", "lib32-ncurses", "opencl-icd-loader", "lib32-opencl-icd-loader", "libxslt", "lib32-libxslt", "libva", "lib32-libva", "gtk3", "lib32-gtk3", "gst-plugins-base-libs", "lib32-gst-plugins-base-libs", "vulkan-icd-loader", "lib32-vulkan-icd-loader", "-y", "--needed", "--noconfirm"]

# For installing Lutris
    def Arch_Lutris(self):
        Install_Lutris = [self.PackageManager, "-S", "python-evdev", "lutris", "-y", "--needed", "--noconfirm"]
        return Install_Lutris

    # The PackageManager variable uses the updated PackageManager only in functions. otherwise  its values will be blank
    def Arch_AUR_Basics(self):
        AUR_Basics = [self.PackageManager, "-Syu", "python-pip", "wine-staging", "winetricks", "steam", "gamemode", "giflib", "lib32-giflib", "libpng", "lib32-libpng", "libldap", "lib32-libldap", "gnutls", "lib32-gnutls", "mpg123", "lib32-mpg123", "openal", "lib32-openal", "v4l-utils", "lib32-v4l-utils", "libpulse", "lib32-libpulse", "libgpg-error", "lib32-libgpg-error", "alsa-plugins", "lib32-alsa-plugins", "alsa-lib", "lib32-alsa-lib", "libjpeg-turbo", "lib32-libjpeg-turbo", "sqlite", "lib32-sqlite", "libxcomposite", "lib32-libxcomposite", "libxinerama", "lib32-libgcrypt", "libgcrypt", "lib32-libxinerama", "ncurses", "lib32-ncurses", "opencl-icd-loader", "lib32-opencl-icd-loader", "libxslt", "lib32-libxslt", "libva", "lib32-libva", "gtk3", "lib32-gtk3", "gst-plugins-base-libs", "lib32-gst-plugins-base-libs", "vulkan-icd-loader", "lib32-vulkan-icd-loader", "-y", "--needed", "--noconfirm"]
        return AUR_Basics

# For installing Heroic
    def Arch_AUR_Heroic(self):
        AUR_Heroic = [self.PackageManager, "-S", "heroic-games-launcher-bin", "-y", "--needed", "--noconfirm"]
        return AUR_Heroic

# For installing The FPS programs and overlays
    def Arch_AUR_Overlays(self):
        AUR_Overlays = [self.PackageManager, "-S", "pkg-config", "cmake", "goverlay-bin", "-y", "--needed", "--noconfirm"]
        return AUR_Overlays

# For installing Steam Tinker Lanuch
    def Arch_AUR_STL(self):
        AUR_STL = [self.PackageManager, "-S", "steamtinkerlaunch", "-y", "--needed", "--noconfirm"]
        return AUR_STL

    def __init__(self, PackageManager):
        if PackageManager == "yay" or PackageManager == "paru":
            whoami = str(subprocess.getoutput("whoami"))
            if whoami == "root":
                print("\nPlease run LibreGaming without the sudo or doas command if you use an AUR Helper\n")
                exit(0)
            else:
                self.PackageManager = PackageManager
        else:
            self.PackageManager = PackageManager