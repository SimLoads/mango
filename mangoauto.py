###MANGO-AUTO-0.0.0.2####
import os
import sys
import time
import platform
import shutil
import glob
title='''
  __  __                         
 |  \/  |Development 0925180026                    
 | \  / | __ _ _ __   __ _  ___  
 | |\/| |/ _` | '_ \ / _` |/ _ \ 
 | |  | | (_| | | | | (_| | (_) |
 |_|  |_|\__,_|_| |_|\__, |\___/
  ______________________/ | V.0
 |________________________| ALP
'''
if os.path.exists('mango-installer.py'):
    try:
        time.sleep(1)
        os.remove('mango-installer.py')
    except:
        pass
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
print("")
print("Welcome to Mango!")
print("1} Unpack .whl file")
print("2} Prepare code")
print("3} Create MangoScript")
print("4} Exit")
mch = input("")
if mch == "1":
    verbose = False
    mangocore.core_unzip(linux,verbose)
    print("")
    path_copy = input("Enter absolute path of code: ")
    if len(path_copy) == 0:
        print("No path given.")
        print("Job successful.")
        exit()
    else:
        currentpath = os.getcwd()
        try:
            os.chdir(path_copy)
        except:
            print("Invalid path given.")
        if len(glob.glob("*.py")) == 0:
            print("No .py files found.")
            cont_j = input("Continue job? [y/n")
            #Q: Why didn't you use an OR statement?
            #A: Because for some reason it never works
            # And returns false regardless if the input is
            # x OR y
            if not cont_j == "y":
                exit()
            if not cont_j == "Y":
                exit()
        os.chdir(currentpath)
        if "mangotools" in os.getcwd():
            os.chdir('..')
        try:
            shutil.copytree("output_final", path_copy)
        except:
            print("Failed to copy output [1aFc]")
            time.sleep(1)
            exit()
        print("Copy successful.")
        print("Job successful.")
        exit()
if mch == "2":
    codedir = os.getcwd()
    verbose = False
    mangocore.core_codeprepare(codedir,verbose,linux)
else:
    exit()
