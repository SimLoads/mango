###MANGO-INSTALLER-0.0.0.0-DEVELOPMENT###
'''
'''
title='''
  __  __                         
 |  \/  |Development 0910180001                    
 | \  / | __ _ _ __   __ _  ___  
 | |\/| |/ _` | '_ \ / _` |/ _ \ 
 | |  | | (_| | | | | (_| | (_) |
 |_|  |_|\__,_|_| |_|\__, |\___/
  ______________________/ | V.0
 |________________________| ALP
'''
'''
Hello User! Welcome to the Mango source code. Credits can be found either below or embedded with the code they are crediting.
Thanks for using Mango! 
'''
import time
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
    else:
        pass
    if reinstall == True:
        print("Module reinstall finished.")
    else:
        print("Module install finished.")
    print("Finalizing...")
    if linux == False:
        print("Creating Unzip Subprocess...")
        try:
            os.chdir('mangotools')
        except:
            pass
        with open('unizp.bat', 'a', newline='') as uw:
            uw.write("@@:: Script Credit - https://stackoverflow.com/questions/2609985/how-to-run-a-powershell-script-within-a-windows-batch-file\n")
            uw.write("@@setlocal\n")
            uw.write("@@set POWERSHELL_BAT_ARGS=%*\n")
            uw.write('@@if defined POWERSHELL_BAT_ARGS set POWERSHELL_BAT_ARGS=%POWERSHELL_BAT_ARGS:"=\"%\n')
            uw.write("@@PowerShell -Command Invoke-Expression $('$args=@(^&{$args} %POWERSHELL_BAT_ARGS%);'+[String]::Join([char]10,$((Get-Content '%~f0') -notmatch '^^@@'))) & goto :EOF\n")
            uw.write("$whl = Read-Host -Prompt 'Enter absolute path for .whl file'\n")
            uw.write('Set-Variable -Name "whlzip" -Value ($whl + ".zip")\n')
            uw.write('Rename-Item -path $whl -NewName $whlzip\n')
            uw.write('Expand-Archive -Force $whlzip -DestinationPath "output"\n')
            uw.write('Rename-Item -path $whlzip -NewName $whl\n')
            uw.close()
        print("Done.")
    os.chdir('..')
    clrslo()
    print("Mango has finished installing.")
    print("1} Launch dedicated script")
    print("2} Add Mango to $PATH")
    print("3} Exit without launching")
    launchin = input("")
    if launchin == "1":
        print("Launching...")
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
    clrslo()
    print("")
    try:
        if core_set_mod == True:
            print("1} Allow core modification *")
        else:
            print("1} Allow core modification")
    except:
        print("1} Allow core modification")
    print("2} Disable config dependancy")
    print("8} Ready to install")
    print("9} Discard changes")
    x = input("")
    if x == "1":
        core_set_mod = True
        print("Core modification allowed.")
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
        setup(use_title,reinstall,coremod)
    if x == "9":
        print("Installing with default settings...")
        use_title = False
        reinstall = False
        coremod = False
        setup(use_title,reinstall,coremod)
    else:
        install_set()
import os
import time
import urllib.request
try:
    test = urllib.request("https://www.google.com")
    response = urllib.request.urlopen(test)
except:
    print("Failed to establish connection.")
    print("Mango may crash during setup.")
reinstall = False
import platform
if not "Windows" in (platform.platform()):
    os.system("clear")
    os.system("printf '\e[8;34;34t'")
else:
    os.system("cls")
    os.system("@mode con cols=34 lines=34")
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
        time.sleep(0.5)
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
        install_set()
    else:
        print("Exiting...")
        exit()
