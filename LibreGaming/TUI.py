#!/usr/bin/env python3
# TODO Make a TUI

import os, subprocess, argparse, wget, requests

import npyscreen

class LibreGaming(npyscreen.Form):
    def create(self):
        self.desc1= self.add(npyscreen.TitleFixedText,name ="desc One",value="1. LibreGaming -g will install Wine,Steam,Gamemode,Mangohud,Heroic Launcher")
        self.desc2= self.add(npyscreen.TitleFixedText,name ="desc One",value="2. LibreGaming -b will install Wine,Steam,Gamemode")
        self.desc3= self.add(npyscreen.TitleFixedText,name ="desc one",value="3. LibreGaming -p will install ProtonGE")
        self.options = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='options', values = [' -g', ' -b', ' -p'])
def myFunction(*args):
    F = LibreGaming(name = "LibreGaming Wizard")
    F.edit()
    s = (str(F.options.get_selected_objects()))[2:-2]
    return s 
if __name__ == '__main__':
    s= (npyscreen.wrapper_basic(myFunction))
    os.system("LibreGaming"+s)