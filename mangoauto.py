###MANGO-AUTO-0.0.0.4####
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
            os.chdir("output_final")
        except:
            print("Failed to find output file. [1aFo]")
            time.sleep(1)
            exit()
        out_dir_current = os.getcwd()
        os.chdir(path_copy)
        if os.path.exists("output_temp"):
            print("Output_temp already exists.")
            print("Will be overwritten.")
            try:
                os.system("rmdir /S /Q output_temp")
            except:
                if os.path.exists("output_temp"):
                    print("Failed to delete.")
                    print("Please delete manually\nand retry.")
                    time.sleep(1)
                    exit()
                pass
        try:
            shutil.copytree(out_dir_current, (os.getcwd() + "\\output_temp"))
        except:
            print("Failed to copy output [1aFc]")
            time.sleep(1)
            exit()
        print("Copy successful.")
        os.chdir('output_temp')
        in_output = glob.glob("*")
        if verbose == True:
            print("Scanned for files...")
        if "dist-info" in in_output[0]:
            name = in_output[1]
        else:
            name = in_output[0]
        print("Found package: " + name)
        os.chdir('..')
        try:
            shutil.copytree(("output_temp//" + name), ((os.getcwd()) + "\\" + name))
        except:
            try:
                os.system("rmdir /S /Q " + name)
                shutil.copytree(("output_temp//" + name), ((os.getcwd()) + "\\" + name))
            except:
                print("Failed to move package. [1aFm]")
                print("Please remove '" + name + "' manually.")
                time.sleep(1)
                exit()
        print("Job successful.")
        pkgpointers = glob.glob("*.mgs")
        pkgnm = ("pkg" + str((len(pkgpointers) + 1)) + ".mgs")
        with open(pkgnm, 'w') as pointer:
            pointer.write(((os.getcwd()) + "\\" + name))
            pointer.close()
        print("Cleaning up...")
        if os.path.exists("output_temp"):
            try:
                os.system("rmdir /S /Q output_temp")
            except:
                pass
        if os.path.exists("output_final"):
            try:
                os.system("rmdir /S /Q output_final")
            except:
                pass
        exit()
if mch == "2":
    codedir = input("Enter absolute path of code:")
    cu_dr = os.getcwd()
    try:
        os.chdir(codedir)
    except:
        print("Invalid directory")
        time.sleep(1)
        exit()
    pkgslst = glob.glob("*.mgs")
    if len(pkgslst) == 0:
        print("No .whl unpack found. [2aNw]")
        print("Ensure unpack is in same folder as code")
        time.sleep(1)
        exit()
    if len(pkgslst) == 1:
        with open(pkgslst[0], 'r') as pointer:
            source = pointer.read()
            pointer.close()        
    if not os.path.exists(source):
        print("No .whl unpack found. [2aNw]")
        print("Ensure unpack is in same folder as code")
        time.sleep(1)
        exit()
    os.chdir(cu_dr)
    verbose = False
    mangocore.core_codeprepare(codedir,verbose,linux)
else:
    exit()
