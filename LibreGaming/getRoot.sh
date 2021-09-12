#!/bin/sh

if  [ -x "$(command -v doas)" ]; then echo 'doas' 
elif  [ -x "$(command -v sudo)" ]; then echo 'sudo'
else echo "su -"; fi
