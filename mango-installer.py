###MANGO-INSTALLER-0.0.0.8###
'''
'''
title='''
  __  __                         
 |  \/  |Development 1031180041              
 | \  / | __ _ _ __   __ _  ___  
 | |\/| |/ _` | '_ \ / _` |/ _ \ 
 | |  | | (_| | | | | (_| | (_) |
 |_|  |_|\__,_|_| |_|\__, |\___/
  ______________________/ | V.2
 |________________________| BET
'''
'''
Hello User! Welcome to the Mango source code. Credits can be found either below or embedded with the code they are crediting.
Thanks for using Mango! 
'''
import time
def rai_prep(coremod,linux):
    print("Requesting Mangocore from github...")
    try:
        update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/mango/mango-tools/mango-core.py')
        response = urllib.request.urlopen(update)
        newcode = response.read()
        master = newcode.decode()
    except:
        print("Failed to connect.")
        print("Please connect to the\ninternet and try again.")
        time.sleep(5)
        exit()
    with open('mangocore.py', 'w', newline='') as core:
        if coremod == True:
            print("Core modification allowed")
            if linux == True:
                core.write(master)
                core.close()
                time.sleep(1)
                os.system("sed -i '1i##MOD##' mangocore.py")
            if linux == False:
                core.write("'##MOD##'\n")
                core.close()
                time.sleep(1)
                with open('mangocore.py', 'a', newline='') as corex:
                    corex.write(master)
                    corex.close()
                core.close()
        else:
            core.write(master)
            core.close()
    print("Created mangocore.py")
    try:
        update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/mango/mango-tools/mangomanual')
        response = urllib.request.urlopen(update)
        newcode = response.read()
        master = newcode.decode()
    except:
        print("Failed to connect.")
        print("Please connect to the\ninternet and try again.")
        time.sleep(5)
        exit()
    with open('mangomanual.py', 'w', newline='') as tool:
        tool.write(master)
        tool.close()
    print("Script created.")
    print("Launching...")
    try:
        os.startfile("mangomanual.py")
    except:
        pass
    exit()
def clrs():
    import platform
    import os
    if not "Windows" in (platform.platform()):
        os.system("clear")
        os.system("printf '\e[8;34;34t'")
    else:
        os.system("cls")
        os.system("@mode con cols=34 lines=34")
def clrslo():
    import platform
    import os
    if not "Windows" in (platform.platform()):
        os.system("clear")
        os.system("printf '\e[8;34;34t'")
        print(title)
    else:
        os.system("cls")
        os.system("@mode con cols=34 lines=34")
        print(title)
def setup(use_title,reinstall,coremod,rai):
    if rai == True:
        print("Attempting RAI...")
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
    if rai == False:
        if not os.path.exists("mangotools"):
            os.mkdir("mangotools")
            print("Created mangotools")
    else:
        print("Skipped directory creation")
    if rai == False:
        os.chdir("mangotools")
        print("Changed Directory")
    if rai == False:
        if not os.path.exists("__init__.py"):
            os.system("echo '' >> __init__.py")
            print("Created __init__.py")
    else:
        print("Skipped module prep")
        print("A seperate script will be created\nto use Mango.")
        rai_prep(coremod,linux)
    if not os.path.exists("mangocore"):
        print("Requesting tools from github...")
        try:
            update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/mango/mango-tools/mango-core.py')
            response = urllib.request.urlopen(update)
            newcode = response.read()
            master = newcode.decode()
        except:
            print("Failed to connect.")
            print("Please connect to the\ninternet and try again.")
            time.sleep(1)
            exit()
        with open('mangocore.py', 'w', newline='') as core:
            if coremod == True:
                print("Core modification allowed")
                if linux == True:
                    core.write(master)
                    core.close()
                    time.sleep(1)
                    os.system("sed -i '1i##MOD##' mangocore.py")
                if linux == False:
                    core.write("'##MOD##'\n")
                    core.close()
                    time.sleep(1)
                    with open('mangocore.py', 'a', newline='') as corex:
                        corex.write(master)
                        corex.close()
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
            time.sleep(1)
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
        time.sleep(1)
        exit()
    print("Imported Mango Core")
    pause = True
    print("Testing Mango Core...")
    try:
        mangocore.core_test()
    except:
        print("Test failed. Restart installation.")
        time.sleep(1)
        exit()
    print("Testing Mango Configure...")
    try:
        from mangotools import mangoconfig
    except:
        print("Failed import!")
        print("Restart installation.")
        time.sleep(1)
        exit()
    try:
        mangoconfig.config_test()
    except:
        print("Test failed. Restart installation.")
        time.sleep(1)
        exit()
    else:
        pass
    if reinstall == True:
        print("Module reinstall finished.")
    else:
        print("Module install finished.")
    print("Finalizing...")
    print("Creating mango.py...")
    try:
        update_C = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/mango/mango-tools/mangoauto.py')
        response_C = urllib.request.urlopen(update_C)
        newcode_C = response_C.read()
        master_C = newcode_C.decode()
    except:
        print("Failed to connect.")
        time.sleep(1)
        exit()
    with open('mango.py', 'w') as config:
        config.write(master_C)
        config.close()
    clrslo()
    print("Mango has finished installing.")
    print("1} Launch dedicated script")
    print("2} Add Mango to $PATH")
    print("3} Exit without launching")
    launchin = input("")
    if launchin == "1":
        print("Launching...")
        if linux == True:
            print("Please use 'python3 mango.py'\nto launch.")
            time.sleep(1)
            exit()
        try:
            os.startfile("mango.py")
        except:
            pass
        exit()
    if launchin == "2":
        print("This feature is currently in heavy development.")
        print("Come back later!")
        print("Mango will now close.")
        time.sleep(5)
        exit()
    else:
        print("Exiting...")
        time.sleep(2)
        exit()
def install_set():
    global linux_set
    global core_set_mod
    global core_rai_mod
    clrslo()
    print("")
    try:
        if core_set_mod == True:
            print("1} Allow core modification *")
        else:
            print("1} Allow core modification")
    except:
        print("1} Allow core modification")
    try:
        if core_rai_mod == True:
            print("2} Restricted Access Install *")
        else:
            print("2} Restricted Access Install")
    except:
        print("2} Restricted Access Install")
    print("8} Ready to install")
    print("9} Discard changes")
    x = input("")
    if x == "1":
        try:
            if core_set_mod == True:
                core_set_mod = False
                print("Core modification disallowed.")
                time.sleep(1)
                install_set()
        except:    
            core_set_mod = True
            print("Core modification allowed.")
            time.sleep(1)
            install_set()
    if x == "2":
        try:
            if core_rai_mod == True:
                core_rai_mod = False
                print("RAI Disabled.")
                time.sleep(1)
                install_set()
        except:
            core_rai_mod = True
            print("RAI Enabled.")
            time.sleep(1)
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
        try:
            if core_rai_mod == True:
                rai = True
            if core_rai_mod == False:
                rai = False
        except:
            rai = False
        setup(use_title,reinstall,coremod,rai)
    if x == "9":
        print("Installing with default settings...")
        use_title = False
        reinstall = False
        coremod = False
        rai = False
        setup(use_title,reinstall,coremod,rai)
    else:
        install_set()
import os
import time
import urllib.request
reinstall = False
import platform
import shutil
clrs()
if not os.path.exists("mangotools"):
    while True:
        clrs()
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
            rai = False
            setup(use_title,reinstall,coremod,rai)
            break
        if choice == "2":
            install_set()
            break
        else:
            continue
else:
    while True:
        clrs()
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
            shutil.rmtree('mangotools', ignore_errors=True)
            install_set()
            break
        else:
            print("Exiting...")
            time.sleep(1)
            exit()
            break
