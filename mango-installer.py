###MANGO-INSTALLER-0.0.0.0###
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
def setup(use_title):
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
            os.system("pause")
            exit()
        with open('mangocore.py', 'w') as core:
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
            os.system("pause")
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
        os.system("pause")
        exit()
    print("Imported Mango Core")
    pause = True
    print("Testing Mango Core...")
    try:
        mangocore.core_test()
    except:
        print("Test failed. Restart installation.")
        os.system("pause")
        exit()
    print("Testing Mango Configure...")
    try:
        from mangotools import mangoconfig
    except:
        print("Failed import!")
        print("Restart installation.")
        os.system("pause")
        exit()
    try:
        mangoconfig.config_test()
    except:
        print("Test failed. Restart installation.")
        os.system("pause")
        exit()
    os.system("pause")
import os
os.system("@mode con cols=34 lines=34")
if not os.path.exists("mangotools"):
    use_title = True
    setup(use_title)
else:
    print(title)
    print("Mango is already installed!")
    print("Reinstall Mango? [y/n]")
    reinstall = input("")
    if reinstall == "y":
        os.system("attrib -s -h mangotools")
        os.system("rmdir /S /Q mangotools")
        use_title = False
        setup(use_title)
    else:
        print("Exiting...")
        os.system("pause")
        exit()
