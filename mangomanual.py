import sys
import time
def scr_prep():
    codedir = input("Enter directory... ")
    verb_test = input("Use Verbose mode? [y/n]")
    if verb_test == "y" or "Y":
        verbose = True
    else:
        verbose = False
    mangocore.core_codeprepare(codedir,verbose)
def whl_prep():
    import platform
    if not "Windows" in platform.platform():
        linux = True
    else:
        linux = False
    verb_test = input("Use Verbose mode? [y/n]")
    if verb_test == "y" or "Y":
        verbose = True
    else:
        verbose = False
    mangocore.core_unzip(linux,verbose)
try:
    sys.path.insert(0, 'mangotools')
    from mangotools import mangocore
except:
    print("Welcome to Mango's RAI mode!")
    print("This is a fallback for users on restricted machines.")
    print("This means you'll have to setup Mango manually.")
    print("Create a directory in this folder called 'mangotools'")
    print("Then drag and drop 'mangocore.py' into it.")
    print("If there is an 'unzip.bat', copy that in too.")
    print("After, restart this script. It's called 'mangomanual'.")
    import time
    while True:
        time.sleep(10)
        continue
path = input("Prepare [w]heel or prepare [s]cript? ")
if path == "w":
    whl_prep()
if path == "s":
    scr_prep()
else:
    print("Only use w or s.")
    exit()
