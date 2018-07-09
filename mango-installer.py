###MANGO-INSTALLER-0.0.0.0-DEVELOPMENT###
'''
'''
title='''
  __  __                         
 |  \/  |                        
 | \  / | __ _ _ __   __ _  ___  
 | |\/| |/ _` | '_ \ / _` |/ _ \ 
 | |  | | (_| | | | | (_| | (_) |
 |_|  |_|\__,_|_| |_|\__, |\___/
  ______________________/ | V.0
 |________________________| ALP
'''
def setup(use_title,reinstall,coremod):
    print("Determining OS...")
    if "Windows" in (platform.platform()):
        linux = False
    else:
        linux = True
    if linux == True:
        if use_title == True:
            os.system("clear")
    if linux == False:
        if use_title == True:
            os.system("cls")
    if use_title == True:
        print(title)
    print("Preparing Mango...")
    import sys
    print("Sys import")
    import shutil
    print("Shutil Import")
    import urllib.request
    print("Urllib.request Import")
    if not os.path.exists("mangotools"):
        os.mkdir("mangotools")
        print("Created mangotools")
    os.chdir("mangotools")
    print("Changed Directory")
    if linux == True:
        print("Detected Linux usage...")
        print("Preparing...")
        with open("shelltools_pause.sh", 'w') as sh:
            sh.write("#!/bin/bash \nread -p 'Press any key to continue...'")
            sh.write('')
            sh.close()
        os.system("chmod u+x shelltools_pause.sh")
        Linux = True
    if not os.path.exists("__init__.py"):
        os.system("echo '' >> __init__.py")
        print("Created __init__.py")
    if not os.path.exists("mangocore"):
        print("Requesting tools from github...")
        try:
            update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/mango/mango-tools/mango-core.py')
            response = urllib.request.urlopen(update)
            newcode = response.read()
            master = newcode.decode()
        except:
            print("Failed to connect.")
            exit()
        with open('mangocore.py', 'w') as core:
            if coremod == True:
                print("Core modification allowed")
                core.write(master)
                core.close()
                time.sleep(1)
                if linux == True:
                    os.system("sed -i '1i##MOD##' mangocore.py")
                if linux == False:
                    os.system("echo '##MOD##' >> coretemp.txt")
                    os.system("move /y coretemp.txt mangocore.py")
                    os.remove("coretemp.txt")
                    core.close()
            else:
                core.write(master)
                core.close()
        print("Created mangocore.py")
        try:
            update_C = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/mango/mango-tools/mangoconfig.py')
            response_C = urllib.request.urlopen(update_C)
            newcode_C = response_C.read()
            master_C = newcode_C.decode()
        except:
            print("Failed to connect.")
            exit()
        with open('mangoconfig.py', 'w') as config:
            config.write(master_C)
            config.close()
        print("Created mangoconfig.py")
    os.chdir('..')
    sys.path.insert(0, 'mangotools')
    print("Preparing for import...")
    try:
        from mangotools import mangocore
    except:
        print("Failed import!")
        print("Restart installation.")
        exit()
    print("Imported Mango Core")
    pause = True
    print("Testing Mango Core...")
    try:
        mangocore.core_test()
    except:
        print("Test failed. Restart installation.")
        exit()
    print("Testing Mango Configure...")
    try:
        from mangotools import mangoconfig
    except:
        print("Failed import!")
        print("Restart installation.")
        exit()
    try:
        mangoconfig.config_test()
    except:
        print("Test failed. Restart installation.")
        exit()
    if linux == True:
        os.chdir('mangotools')
        os.system("bash shelltools_pause.sh")
        os.chdir('..')
    else:
        os.system("pause")
    if reinstall == True:
        print("Module reinstall finished.")
    else:
        print("Module install finished.")
    print("Setting up launcher...")
    exit()
def install_set():
    global linux_set
    global core_set_mod
    print("")
    print("1} Allow core modification")
    print("2} Disable config dependancy")
    print("8} Ready to install")
    print("9} Discard changes")
    x = input("")
    if x == "1":
        core_set_mod = True
        print("Core modification allowed.")
        install_set()
    if x == "8":
        use_title = True
        reinstall = False
        try:
            if core_set_mod == True:
                coremod = True
            if core_set_mod == False:
                coremod = False
        except:
            coremod = False
        setup(use_title,reinstall,coremod)
    if x == "9":
        print("Installing with default settings...")
        use_title = False
        reinstall = False
        coremod = False
        setup(use_title,reinstall,coremod)
import os
import time
reinstall = False
os.system("clear")
os.system("printf '\e[8;34;34t'")
import platform
if not os.path.exists("mangotools"):
    print(title)
    print("----------------------------------")
    print("Welcome to Mango!")
    print("1} Install now")
    print("2} Modify installation")
    print("3} Exit")
    choice = input("")
    if choice == "1":
        use_title = True
        coremod = False
        setup(use_title,reinstall,coremod)
    if choice == "2":
        install_set()
    else:
        print("Exiting...")
        exit()
else:
    print(title)
    print("Mango is already installed!")
    print("Reinstall Mango? [y/n]")
    reinstall = input("")
    if reinstall == "y":
        if not "Windows" in (platform.platform()):
            linux = True
            os.system("clear")
        else:
            linux = False
            os.system("cls")
        if linux == False:
            os.system("attrib -s -h mangotools")
        if linux == False:
            os.system("rmdir /S /Q mangotools")
        else:
            os.system("rm -rf mangotools")
        use_title = False
        reinstall = True
        coremod = False
        setup(use_title,reinstall,coremod)
    else:
        print("Exiting...")
        exit()
