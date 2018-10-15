###MANGO-AUTO-0.0.1.6####
import os
import sys
import time
import platform
import shutil
import glob
try:
    run_var = sys.argv[1]
except:
    run_var = ""
    term = False
try:
    path_whl = sys.argv[2]
except:
    path_whl = ""
    pass
try:
    path_out = sys.argv[3]
    verb = sys.argv[4]
    term = True
except:
    pass
if run_var.lower() == "help":
    if path_whl.lower() == "all":
        print("Mango terminal help")
        print("Usage: mango.py <choice> <wheel dir> <code dir> <verbose [True/False]>")
        exit()
    if path_whl.lower() == "choice":
        print("<choice> :: Which function to call. 1: Prepare wheel. 2: Prepare code.")
        exit()
    if path_whl.lower() == "error":
        try:
            with open("Error_Code_Lookup.txt" , 'r') as errors:
                x = errors.read()
                errors.close()
            print(x)
            exit()
        except:
            print("Refer to github page.")
            exit()
    else:
        print("Invalid help topic.")
        print("Usage: help <all / choice / error>")
        exit()
title='''
  __  __                         
 |  \/  |Development 1015180046                   
 | \  / | __ _ _ __   __ _  ___  
 | |\/| |/ _` | '_ \ / _` |/ _ \ 
 | |  | | (_| | | | | (_| | (_) |
 |_|  |_|\__,_|_| |_|\__, |\___/
  ______________________/ | V.1
 |________________________| BET
'''
def clrslo():
    input()
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
    from mangotools import mangocores
except SyntaxError:
    print("Failed to import mangotools [0aFs]")
    print("Ensure no tools have been edited incorrectly.")
    time.sleep(1)
except ImportError:
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
if term == False:
    clrslo()
menu = True
try:
    if run_var < 3:
        mch = run_var
        menu = False
    else:
        print("Invalid choice")
        time.sleep(1)
        exit()
except:
    pass
if menu == True:
    print("")
    print("Welcome to Mango!")
    print("1} Unpack .whl file")
    print("2} Prepare code")
    print("3} Create MangoScript")
    print("4} Exit")
    mch = input("")
if mch == "1":
    try:
        verbose = verb
    except:
        verbose = False
    try:
        termpath = path_whl
    except:
        termpath = ""
    print("Working...")
    mangocore.core_unzip(linux,verbose,termpath)
    print("")
    try:
        path_copy = path_out
    except:
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
                shutil.rmtree('output_temp', ignore_errors=True)
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
                shutil.rmtree(name, ignore_errors=True)
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
                shutil.rmtree('output_temp', ignore_errors=True)
            except:
                pass
        if os.path.exists("output_final"):
            try:
                shutil.rmtree("output_final", ignore_errors=True)
            except:
                pass
        mch = "2"
        codedir = os.getcwd()
if mch == "2":
    try:
        os.chdir(codedir)
    except:
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
    else:
        paks = []
        for number, letter in enumerate(pkgslst):
            with open(pkgslst[number], 'r') as b:
                varout = b.read()
                b.close()
            paks.append(varout)
        while True:
            sourcedef = False
            for number, letter in enumerate(paks):
                temppaks = paks[number].split('\\')
                name = temppaks[-1]
                print("Select pacakge " + name + "?")
                ch_pks = input("[y/n]")
                if ch_pks.lower() == "y":
                    source = paks[number]
                    sourcedef = True
                    break
                continue
            if sourcedef == False:
                continue
            else:
                break
    if not os.path.exists(source):
        print("No .whl unpack found. [2aNw]")
        print("Ensure unpack is in same folder as code")
        time.sleep(1)
        exit()
    os.chdir(cu_dr)
    verbose = False
    mangocore.core_codeprepare(codedir,verbose,linux,source)
else:
    exit()
