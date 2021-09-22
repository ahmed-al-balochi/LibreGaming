#!/usr/bin/env python3

import os, subprocess, argparse, wget, requests
import npyscreen

class LibreGamingTUI(npyscreen.Form):
    def create(self):
        self.options = self.add(npyscreen.TitleMultiSelect, scroll_exit=True, name='options', values = [
        'Option 1: will install Wine-staging,Steam,Gamemode,Lutris,Heroic Launcher,Mangohud & Goverlay',
        'Option 2: will install Wine-staging,Steam,Gamemode',
        'Option 3: will install/Update ProtonGE(You must run Steam once before installing ProtonGE)',
        'Option 4: will install Athenaeum Launcher',
        'Option 5: will install itch.io Launcher',
        'Option 6: will install Steam Tinker Launch(For Arch Linux only)',
        'Option 7: Start the Wizard for Individual installations',
        ])

def TUI(*args):
    Form = LibreGamingTUI(name = "LibreGaming TUI")
    Form.edit()
    SelectedOption = str(Form.options.get_selected_objects())
    numbers = []
    for item in SelectedOption:
        for subitem in item.split():
            if(subitem.isdigit()):
                numbers.append(subitem)
    return numbers   

class LibreGamingWizard(npyscreen.Form):
    def create(self):
        self.apps = self.add(npyscreen.TitleMultiSelect, scroll_exit=True, name='apps', values = [
        'Option 1: will install Wine-staging,Steam,Gamemode',
        'Option 2: will install Lutris',
        'Option 3: will install Heroic Launcher',
        'Option 4: will install Mangohud & Goverlay',
        'Option 5: will install/Update ProtonGE(You must run Steam once before installing ProtonGE)',
        'Option 6: will install Athenaeum Launcher',
        'Option 7: will install itch.io Launcher',
        'Option 8: will install Steam Tinker Launch(For Arch Linux only)',
        'Option 9: Go Back To the Previous Screen',
        ])

def WizardScreen(*args):
    Form = LibreGamingWizard(name = "Wizard")
    Form.edit()
    SelectedApps = str(Form.apps.get_selected_objects())
    numbers = []
    for item in SelectedApps:
        for subitem in item.split():
            if(subitem.isdigit()):
                numbers.append(subitem)
    return numbers 

def installingApps(installApps):
    print("You Selected " + str(installApps))
    for i in installApps:
        if i == "1":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming -b")
            continue
        elif i == "2":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming --lutris")
            continue
        elif i == "3":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming --heroic")
            continue
        elif i == "4":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming -o")
            continue
        elif i == "5":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("protonup")
            continue
        elif i == "6":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming -ath")
            continue
        elif i == "7":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming --itch")
            continue
        elif i == "8":
            print("\n==>> Executing Option " + str(i) + "\n")
            os.system("libregaming --stl")
            continue
        elif i == "9":
            MainForm()
            continue
        else:
            print("Sorry could not execute. Please check your input")

def MainForm(): 
    installOption = (npyscreen.wrapper_basic(TUI))
    print("You Selected " + str(installOption))
    for i in installOption:
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
        elif i == "7":
            installApps= (npyscreen.wrapper_basic(WizardScreen))
            installingApps(installApps)
            continue
        else:
            print("Sorry could not execute. Please check your input")

def main(): 
    MainForm()

if __name__ == "__main__":
    main()