###MANGO-CORE-0.0.0.4###
'''
'''
def core_test():
    print("Mango Core Response Successful.")
def core_unzip(linux,verbose):
    # Yes I know, I could've used a function for the failed import thing, but no.
    # Needlessly complex code makes it harder to clone... right?
    import time
    if linux == True:
        print("Linux mode still in development.")
        print("Please try again soon.")
        time.sleep(1)
        exit()
    try:
        import subprocess
        if verbose == True:
            print("Subprocess import successful")
    except:
        print("Failed import.")
        print("Exiting...")
        time.sleep(1)
        exit()
    try:
        import os
        if verbose == True:
            print("OS import successful")
    except:
        print("Failed import.")
        print("Exiting...")
        time.sleep(1)
        exit()
    try:
        import shutil
        if verbose == True:
            print("Shutil import successful")
    except:
        print("Failed import.")
        print("Exiting...")
        time.sleep(1)
        exit()
    try:
        import glob
        if verbose == True:
            print("Glob import successful")
    except:
        print("Failed import.")
        print("Exiting...")
        time.sleep(1)
        exit()
    try:
        import re
        if verbose == True:
            print("RE import sucessful")
    except:
        print("Failed import.")
        print("Exiting...")
        time.sleep(1)
        exit()
    if linux == False:
        if verbose == True:
            print("Using Windows.")
        try:
            os.chidr("mangotools")
            if verbose == True:
                print("Directory changed.")
        except:
            if verbose == True:
                print("No directory change needed.")
            pass
        movedir = (re.escape(os.getcwd()) + "\\\\output_final")
        try:
            os.chdir("mangotools")
        except:
            if "mangotools" in os.getcwd():
                pass
            else:
                print("Failed to find mangotools. [0cMg]")
                time.sleep(1)
                exit()
        currentdir = os.getcwd()
        if ' ' in currentdir:
            print("Directory name contains\nillegal characters. [0cIc]")
            time.sleep(1)
            exit()
        subdir = (currentdir)
        subdir = re.escape(subdir)
        subdir = (subdir + "\\\\unzip.bat")
        try:
            unzip = subprocess.Popen(subdir, stdout=subprocess.PIPE)
        except:
            print("Failed to find unzip.bat. [0cUf]")
            time.sleep(1)
            exit()
        unzip.communicate()
        if verbose == True:
            print("Unzip complete.")
        if os.path.exists("output_temp"):
            if verbose == True:
                print("output_temp exists")
            os.chdir("output_temp")
            if verbose == True:
                print("Switched to output_temp")
            files = glob.glob("*")
            if verbose == True:
                print("Testing for file exist...")
            if len(files) <1:
                print("Unzip failed [0cFm]. Please try again.")
                exit()
            if verbose == True:
                print("Assuming unzip was successful.")
            os.chdir('..')
            if verbose == True:
                print("Moved back out of output_temp")
            if verbose == True:
                print("Attempting to move files...")
            os.chdir('..')
            if os.path.exists("output_final"):
                print("Output from last job still exists.")
                print("Will be overwritten.")
                if linux == False:
                    os.system("rmdir /S /Q output_final")
            os.chdir('mangotools')
            try:
                shutil.copytree("output_temp", movedir)
            except:
                print("Unzip failed [0cMd]. Please try again.")
                time.sleep(1)
                exit()
            if verbose == True:
                print("Move successful.")
                print("Attempting to remove temp...")
            try:
                os.chdir("mangotools")
                os.rmdir("output_temp")
                os.chdir('..')
            except:
                print("Failed to remove temp file. [0cRm]")
                print("May cause future errors.")
                print("Manual removal recommended.")
            print("Finished unzipping.")
        else:
            print("Unzip failed [0cNf]. Please try again.")
            time.sleep(1)
            exit()
def core_selftest(linux):
    import time
    import os
    from difflib import SequenceMatcher
    with open('mangocore.py', 'r') as core:
        core_content = core.read()
        core_mod_query = core_content.splitlines()
        core.close()
    if ("'##MOD##'") in core_mod_query[0]:
        print("Core self test disabled.")
        return ("")
    import urllib.request
    try:
        update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/mango/mango-tools/mango-core.py')
        response = urllib.request.urlopen(update)
        newcode = response.read()
        master = newcode.decode()
    except:
        print("Failed to connect.")
        print("Self test failed. [2cSt]")
        return ("")
    similar = SequenceMatcher(None, master, core_content).ratio()
    if similar < 0.94740:
        print("Modification detected!")
        print("Resetting Core...")
        with open('mangocore.py', 'w', newline='') as recore:
            recore.write(master)
            recore.close()
            print("Core reset.")
            print("Please restart.")
            time.sleep(1)
            exit()
    else:
        print("Core self test complete.")
        return ("")
def core_codeprepare(codedir,verbose,linux):
    import os
    import sys
    import time
    import glob
    import re
    import shutil
    if linux == True:
        print("Linux mode still in development.")
        print("Please try again soon.")
        time.sleep(1)
        exit()
    if verbose == True:
        print("Mango core code prepare ready.")
    if verbose == True:
        print("Preparing to append...")
    currentdir = os.getcwd()
    if not os.path.exists("output_final"):
        print("No output detected.")
        print("Unzip a .whl file before trying to import it.")
        exit()
    print("Output found!")
    os.chdir('output_final')
    if verbose == True:
        print("Switched Directories")
    in_output = glob.glob("*")
    if verbose == True:
        print("Scanned for files...")
    if "dist-info" in in_output[0]:
        name = in_output[1]
    else:
        name = in_output[0]
    if verbose == True:
        print("Package name selected.")
    print("Package: " + name)
    source = re.escape(os.getcwd())
    source_package = (source + "\\\\" + name)
    if verbose == True:
        print("Prepared package source")
    try:
        os.chdir(codedir)
        if verbose == True:
            print("Switched directories")
    except:
        print("Invalid code directory. [1cId]")
        time.sleep(1)
        exit()
    codedir = (codedir + "\\\\" + name)
    if verbose == True:
        print("Prepared destination")
    if os.path.exists(codedir):
        print("Package already exists. [1cPe]")
        time.sleep(1)
        print("Overwriting...")
        shutil.rmtree(codedir, ignore_errors=True)
    try:
        shutil.copytree(source_package, codedir)
    except:
        print("Failed to copy directory. [1cFd]")
        time.sleep(1)
        exit()
    print("Copy Successful.")
    pyfiles = glob.glob("*.py")
    if verbose == True:
        print("Scanned for .py files")
    if len(pyfiles) == 0:
        print("No .py files found. [1cNp]")
        time.sleep(1)
        exit()
    if len(pyfiles) > 1:
        print("Multiple .py files found!")
        for number, letter in enumerate(pyfiles):
            trnu = number + 1
            trnus = str(trnu)
            print(trnus + ":", letter)
        while True:
            pyfile_choice = input("Select file to append: ")
            try:
                pyfile_choice = int(pyfile_choice)
                if verbose == True:
                    print("Converted input")
                pyc_c = (pyfile_choice - 1)
                pyc = pyfiles[pyc_c]
                if verbose == True:
                    print("Set file variable")
                break
            except:
                print("Invalid choice.")
    else:
        pyc = pyfiles[0]
    string = ("sys.path.insert(0, '" + name + "')\n")
    if verbose == True:
        print("Prepared sys string")
    try:
        with open(pyc, 'r') as r_f:
            contents = r_f.read()
            if verbose == True:
                print("Read file contents")
            r_f.close()
    except:
        print("Failed to open .py file. [1cPf]")
        time.sleep(1)
        exit()
    try:
        os.remove(pyc)
        if verbose == True:
            print("Removed original file")
    except:
        print("Failed to remove .py file. [1cRf]")
        time.sleep(1)
        exit()
    try:
        with open(pyc, 'a') as a_f:
            a_f.write("import sys\n")
            if verbose == True:
                print("Wrote import sys")
            a_f.write(string)
            if verbose == True:
                print("Wrote import package string")
            a_f.write(contents)
            if verbose == True:
                print("Rewrote contents")
            a_f.close()
    except:
        print("Failed to append. [1cAf]")
        time.sleep(1)
        exit()
    print("Append successful.")
    print("File ready.")
