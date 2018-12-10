###MANGO-AUTO-0.0.2.6####
import os
import sys
import time
import platform
import shutil
import glob
try:
    run_var = sys.argv[1]
    term = True
except:
    run_var = "0"
    term = False
try:
    path_whl = sys.argv[2]
except:
    path_whl = ""
    pass
try:
    path_out = sys.argv[3]
except:
    pass
try:
    verb = sys.argv[4]
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
if not int(run_var) < 3:
    print("Invalid process.")
    exit()
title='''
  __  __                         
 |  \/  |Development 1210180086
 | \  / | __ _ _ __   __ _  ___  
 | |\/| |/ _` | '_ \ / _` |/ _ \ 
 | |  | | (_| | | | | (_| | (_) |
 |_|  |_|\__,_|_| |_|\__, |\___/
  ______________________/ | V.3
 |________________________| BET
'''
def clrslo(titlePrint):
    input()
    import platform
    import os
    if not "Windows" in (platform.platform()):
        os.system("clear")
        os.system("printf '\e[8;34;34t'")
        if titlePrint == True:
            print(title)
    else:
        os.system("cls")
        os.system("@mode con cols=34 lines=34")
        if titlePrint == True:
            print(title)
try:
    optionsDict = {}
    with open('mgsc.conf', 'r') as conf:
        set = conf.read()
        indOptions = set.split('|')
    del indOptions[0]
    for number,letter in enumerate(indOptions):
        if str(0) in letter:
            optionsDict["set{0}".format(number)]= False
        else:
            optionsDict["set{0}".format(number)]= True
#pauseAtNextInstruction = optionsDict.get('set0')
#autoSelectFirstFile = optionsDict.get('set1')
#printTitle = optionsDict.get('set2')
#printCoreSelfTestSimilarity = optionsDict.get('set3')
except:
    optionsDict = {
    'set0': False,
    'set1': False,
    'set2': True,
    'set3': False
    }
if (optionsDict.get('set2')) == True:
    titlePrint = True
else:
    titlePrint = False
if (optionsDict.get('set3')) == True:
    corePrint = True
else:
    corePrint = False
print("Performing core test...")
try:
    sys.path.insert(0, 'mangotools')
    os.chdir('mangotools')
    from mangotools import mangoconfig
    from mangotools import mangocore
except SyntaxError:
    print("Failed to import mangotools [0aFs]")
    print("Ensure no tools have been edited incorrectly.")
    time.sleep(1)
    exit()
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
mangocore.core_selftest(linux,corePrint)
os.chdir('..')
if term == False:
    clrslo(titlePrint)
menu = True
try:
    y = str(run_var)
    running = True
    pass
except:
    running = False
if running == True:
    if run_var == "1":
        mch = run_var
        menu = False
    if run_var == "2":
        mch = run_var
        menu = False
if menu == True:
    print("")
    print("Welcome to Mango!")
    print("1} Unpack .whl file")
    print("2} Prepare code")
    print("3} Create MangoScript")
    print("4} Mango settings")
    print("9} Exit")
    mch = input("")
if mch == "1":
    try:
        verbose = verb
    except:
        verbose = True
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
        while True:
            path_copy = input("Enter absolute path of code: ")
            if len(path_copy) == 0:
                print("No path given.")
                continue
            break
    currentpath = os.getcwd()
    try:
        os.chdir(path_copy)
    except:
        print("Invalid path given.")
        exit()
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
    if not "mangotools" in os.getcwd():
        try:
            os.chdir('mangotools')
        except:
            time.sleep(1)
            exit()
    if os.path.exists('output_temp'):
        os.chdir('output_temp')
        out_dir_current = os.getcwd()
    else:
        print("Unknown error")
        time.sleep(1)
        exit()
    in_output = glob.glob("*")
    if verbose == True:
        print("Scanned for files...")
    if "dist-info" in in_output[0]:
        name = in_output[1]
    else:
        name = in_output[0]
    print("Found package: " + name)
    os.chdir(name)
    packmove = os.getcwd()
    os.chdir(path_copy)
    try:
        shutil.copytree(packmove, name)
    except:
        try:
            shutil.rmtree(name, ignore_errors=True)
            shutil.copytree(packmove, name)
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
    try:
        os.chdir("mangotools")
        shutil.rmtree("output_temp", ignore_errors=True)
        try:
            shutil.rmtree((glob.glob("*.whl")))
        except:
            pass
        os.chdir('..')
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
if mch == "4":
    print("Your current Mango settings are:")
    raw = False
    mangoconfig.config_call(raw)
    setChanges = input("Make changes? [y/n]")
    if (setChanges.lower()) == "y":
        mangoconfig.config_edit()
else:
    exit()
