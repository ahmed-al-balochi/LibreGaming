import subprocess

class Fedora:
    """
    Here are all the pkgs that LibreGaming installs for Fedora 
    """

# For fedora 33 and above
# For installing Basic Packages like Steam, Wine, Gamemode 
# ReleaseNumber Saves the Fedora release number. For example: Fedora 35
    Fedora_33_Basics = [
        ["wget", "https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks"], #installing winetricks here
        ["chmod", "-744", "winetricks"],
        ["mv", "winetricks", "/usr/local/bin/"],
        ["dnf", "config-manager", "--add-repo", "https://dl.winehq.org/wine-builds/fedora/"+ str(subprocess.getoutput("lsb_release -rs")) +"/winehq.repo"],
        ["dnf", "update", "-y"],
        ["dnf", "install", "python3-pip", "wine-staging", "gamemode", "steam", "alsa-plugins-pulseaudio.i686", "glibc-devel.i686", "glibc-devel", "libgcc.i686", "libX11-devel.i686", "freetype-devel.i686", "libXcursor-devel.i686", "libXi-devel.i686", "libXext-devel.i686", "libXxf86vm-devel.i686", "libXrandr-devel.i686", "libXinerama-devel.i686", "mesa-libGLU-devel.i686", "mesa-libOSMesa-devel.i686", "libXrender-devel.i686", "libpcap-devel.i686", "ncurses-devel.i686", "libzip-devel.i686", "lcms2-devel.i686", "zlib-devel.i686", "libv4l-devel.i686", "libgphoto2-devel.i686", "cups-devel.i686", "libxml2-devel.i686", "openldap-devel.i686", "libxslt-devel.i686", "gnutls-devel.i686", "libpng-devel.i686", "flac-libs.i686", "json-c.i686", "libICE.i686", "libSM.i686", "libXtst.i686", "libasyncns.i686", "liberation-narrow-fonts.noarch", "libieee1284.i686", "libogg.i686", "libsndfile.i686", "libuuid.i686", "libva.i686", "libvorbis.i686", "libwayland-client.i686", "libwayland-server.i686", "llvm-libs.i686", "mesa-dri-drivers.i686", "mesa-filesystem.i686", "mesa-libEGL.i686", "mesa-libgbm.i686", "nss-mdns.i686", "ocl-icd.i686", "pulseaudio-libs.i686", "sane-backends-libs.i686", "tcp_wrappers-libs.i686", "unixODBC.i686", "samba-common-tools.x86_64", "samba-libs.x86_64", "samba-winbind.x86_64", "samba-winbind-clients.x86_64", "samba-winbind-modules.x86_64", "mesa-libGL-devel.i686", "fontconfig-devel.i686", "libXcomposite-devel.i686", "libtiff-devel.i686", "openal-soft-devel.i686", "mesa-libOpenCL-devel.i686", "opencl-utils-devel.i686", "alsa-lib-devel.i686", "gsm-devel.i686", "libjpeg-turbo-devel.i686", "pulseaudio-libs-devel.i686", "pulseaudio-libs-devel", "gtk3-devel.i686", "libattr-devel.i686", "libva-devel.i686", "libexif-devel.i686", "libexif.i686", "glib2-devel.i686", "mpg123-devel.i686", "mpg123-devel.x86_64", "libcom_err-devel.i686", "libcom_err-devel.x86_64", "libFAudio-devel", "-y"]
        ]

# For fedora 32 and less 
# For installing Basic Packages like Steam, Wine, Gamemode 
    Fedora_32_Basics = [
        ["wget", "https://raw.githubusercontent.com/winetricks/winetricks/master/src/winetricks"], #installing winetricks here
        ["chmod", "-744", "winetricks"],
        ["mv", "winetricks", "/usr/local/bin/"],
        ["dnf", "update", "-y"],
        ["dnf", "install", "python3-pip", "wine", "gamemode", "steam", "alsa-plugins-pulseaudio.i686", "glibc-devel.i686", "glibc-devel", "libgcc.i686", "libx11-devel.i686", "freetype-devel.i686", "libxcursor-devel.i686", "libxi-devel.i686", "libxext-devel.i686", "libxxf86vm-devel.i686", "libxrandr-devel.i686", "libxinerama-devel.i686", "mesa-libglu-devel.i686", "mesa-libosmesa-devel.i686", "libxrender-devel.i686", "libpcap-devel.i686", "ncurses-devel.i686", "libzip-devel.i686", "lcms2-devel.i686", "zlib-devel.i686", "libv4l-devel.i686", "libgphoto2-devel.i686", "cups-devel.i686", "libxml2-devel.i686", "openldap-devel.i686", "libxslt-devel.i686", "gnutls-devel.i686", "libpng-devel.i686", "flac-libs.i686", "json-c.i686", "libice.i686", "libsm.i686", "libxtst.i686", "libasyncns.i686", "liberation-narrow-fonts.noarch", "libieee1284.i686", "libogg.i686", "libsndfile.i686", "libuuid.i686", "libva.i686", "libvorbis.i686", "libwayland-client.i686", "libwayland-server.i686", "llvm-libs.i686", "mesa-dri-drivers.i686", "mesa-filesystem.i686", "mesa-libegl.i686", "mesa-libgbm.i686", "nss-mdns.i686", "ocl-icd.i686", "pulseaudio-libs.i686", "sane-backends-libs.i686", "tcp_wrappers-libs.i686", "unixodbc.i686", "samba-common-tools.x86_64", "samba-libs.x86_64", "samba-winbind.x86_64", "samba-winbind-clients.x86_64", "samba-winbind-modules.x86_64", "mesa-libgl-devel.i686", "fontconfig-devel.i686", "libxcomposite-devel.i686", "libtiff-devel.i686", "openal-soft-devel.i686", "mesa-libopencl-devel.i686", "opencl-utils-devel.i686", "alsa-lib-devel.i686", "gsm-devel.i686", "libjpeg-turbo-devel.i686", "pulseaudio-libs-devel.i686", "pulseaudio-libs-devel", "gtk3-devel.i686", "libattr-devel.i686", "libva-devel.i686", "libexif-devel.i686", "libexif.i686", "glib2-devel.i686", "mpg123-devel.i686", "mpg123-devel.x86_64", "libcom_err-devel.i686", "libcom_err-devel.x86_64", "libFAudio-devel", "-y"]
        ]

# For installing Lutris
    Fedora_Lutris = ["dnf", "install", "lutris", "-y"]


# For installing Heroic
    Fedora_Heroic = [
        ["dnf", "copr", "enable", "atim/heroic-games-launcher", "-y"],
        ["dnf", "update", "-y"],
        ["dnf", "install", "heroic-games-launcher-bin", "-y"]
    ]
# For installing The FPS programs and overlays
    Fedora_Overlays = ["dnf","install", "goverlay", "-y"]
