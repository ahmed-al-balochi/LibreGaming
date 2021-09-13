#!/bin/bash
printf "Hey man, how are you doin' today?\nPlease select which distro you are using...Also make sure you already have AUR and multilib enabled <https://low-orbit.net/arch-linux-how-to-enable-multilib>\n"
printf "This script is a rewrite of: https://github.com/Ahmed-Al-Balochi/LibreGaming and rewritten by https://github.com/EsmailELBoBDev2. because why not\n\n"
printf "1) Arch-Based Distro (thats what i use btw)\n2) Debian-Based Distro\n\n"
read -p 'Type here: ' distroOpt
printf "\n"

arch () {
  printf "Oh you use arch btw too? noice\n"
  printf "Now, hear me out. I need you to tell me which packages you want to install. Is it just protonge or steam or you want ALL OF THEM (evil laugh in background)\n\nSo I Am Once Again Asking for Your Financial Support, i mean which packages do you want to install? [it's a meme <https://knowyourmeme.com/memes/i-am-once-again-asking-for-your-financial-support>]\n\n"
  printf "1) ALL OF THEM (don't be greedy man)\n2) Steam (ew closed source games?)\n3) Wine (i play gta using wine)\n4) Gamemode(idk what the hell is that is -- here it's link: https://github.com/FeralInteractive/gamemode)\n5) ProtonGE and Protonup(why just don't use stock proton? weirdo)\n6) Lutris(yeah sure, using FOSS launcher does not mean you will run away playing closed source games)\n7) Athenaeum (ew using flatpak -- wait it seems a Launcher for FOSS games)\n8) mangohud and goverlay (don't know what that is)\n9) Heroic (The FOSS version of epic game launcher)\n\n"
  read -p 'Type here: ' packOpt

    case $packOpt in
    "1") # Yes im using || (or) instead of using if to check -- sue me
        yay -Syu python-pip goverlay-bin heroic-games-launcher-bin wine-staging winetricks lutris steam gamemode giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader || paru -Syu python-pip goverlay-bin heroic-games-launcher-bin wine-staging winetricks lutris steam gamemode giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader && sudo pacman -Syu python-pip wine-staging winetricks lutris steam gamemode giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader || doas pacman -Syu python-pip wine-staging winetricks lutris steam gamemode giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs 
        ;;
    "2")
        sudo pacman -Syu steam || doas pacman -Syu steam
        ;;
    "3")
        yay -Syu python-pip   wine-staging winetricks giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader || paru -Syu python-pip   wine-staging winetricks    giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader && sudo pacman -Syu python-pip wine-staging winetricks    giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader || doas pacman -Syu python-pip wine-staging winetricks    giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader
        ;;
    "4")
        sudo pacman -Syu gamemode lib32-gamemode || doas pacman -Syu gamemode lib32-gamemode
        ;;
    "5")
        printf "Well, to make sure you get latest proton ge, go to: https://github.com/GloriousEggroll/proton-ge-custom/releases and type it's version so i can download it inside your Downloads folder\n"
        read -p "Type the version here(usually will be something like 6.16-GE-1): " protongeVer
        cd ~/Downloads || mkdir ~/Downloads && wget https://github.com/GloriousEggroll/proton-ge-custom/releases/download/${protongeVer}/Proton-${protongeVer}.tar.gz
        if [ ! -d "~/.steam/root/compatibilitytools.d" ] 
        then
            mkdir ~/.steam/root/compatibilitytools.d 
        fi
        cd ~/Downloads
        tar -xf Proton-${protongeVer}.tar.gz -C ~/.steam/root/compatibilitytools.d/
        rm Proton-${protongeVer}.tar.gz
        printf "\nNow restart steam and follow: https://github.com/GloriousEggroll/proton-ge-custom#enabling to enable your new proton :)\n\n" && yay -Syu protonup-git

        ;;
    "6")
       sudo pacman -Syu lutris || doas pacman -Syu lutris
        ;;
    "7") 
        sudo pacman -Syu athenaeum-git  || doas pacman -Syu athenaeum-git
        ;;
    "8")
        sudo pamac install goverlay-bin && yay -Syu mangohud-git lib32-mangohud-git || doas pamac install goverlay-bin && yay -Syu mangohud-git lib32-mangohud-git
        ;;
    "9")
        yay -Syu heroic-games-launcher-bin || paru -Syu heroic-games-launcher-bin
        ;;
    *)
        printf "someone wanna be dead i guess -- SELECT A VAILD NUMBER FROM THE LIST ABOVE"
        ;;
    esac

}

if [[ $distroOpt = "1" ]]; then
    arch
elif [[ $distroOpt = "2" ]]; then
    printf "Debain\ Debian Based? ew"
else 
    printf "You had one job, one simple job and you ruined it! -- SELECT A VAILD NUMBER FROM THE LIST ABOVE\nLuke smith is running after you now\n"
fi
