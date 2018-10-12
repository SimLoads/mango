import os
import sys
import time
import platform
title='''
  __  __                         
 |  \/  |Development 0924180016                    
 | \  / | __ _ _ __   __ _  ___  
 | |\/| |/ _` | '_ \ / _` |/ _ \ 
 | |  | | (_| | | | | (_| | (_) |
 |_|  |_|\__,_|_| |_|\__, |\___/
  ______________________/ | V.0
 |________________________| ALP
'''
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
print("Clear function prepared.")
print("Performing core test...")
try:
    sys.path.insert(0, 'mangotools')
    os.chdir('mangotools')
    from mangotools import mangoconfig
    from mangotools import mangocore
except:
    print("Failed to import mangotools [0aFi]")
    print("Ensure mango was installed properly.")
    time.sleep(1)
    exit()
global linux
if "Windows" in platform.platform():
    linux = False
else:
    linux = True
mangocore.core_selftest(linux)
os.chdir('..')
clrslo()
