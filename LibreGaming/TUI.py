#!/usr/bin/env python3

import os, subprocess, argparse, wget, requests
import npyscreen

class LibreGamingTUI(npyscreen.Form):
    def create(self):
        self.options = self.add(npyscreen.TitleMultiSelect, scroll_exit=True, name='options', values = [
        'Option 1: will install Wine=staging,Steam,Gamemode,Lutris,Heroic Launcher,Mangohud & Goverlay',
        'Option 2: will install Wine=staging,Steam,Gamemode',
        'Option 3: will install/Update ProtonGE',
        'Option 4: will install Athenaeum Launcher',
        'Option 5: will install itch.io Launcher',
        'Option 6: will install Steam Tinker Launch(For Arch Linux only)',
        ])
def myFunction(*args):
    Form = LibreGamingTUI(name = "LibreGaming TUI")
    Form.edit()
    Option = str(Form.options.get_selected_objects())
    numbers = []
    for item in Option:
        for subitem in item.split():
            if(subitem.isdigit()):
                numbers.append(subitem)
    return numbers 

def main(): 
    Option = (npyscreen.wrapper_basic(myFunction))
    print("You Selected " + str(Option))
    for i in Option:
        if i == "1":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming -g")
            continue
        elif i == "2":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming -b")
            continue
        elif i == "3":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("protonup")
            continue
        elif i == "4":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming -ath")
            continue
        elif i == "5":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming --itch")
            continue
        elif i == "6":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming --stl")
            continue
        else:
            print("Sorry could not execute. Please check your input")

if __name__ == "__main__":
    main()