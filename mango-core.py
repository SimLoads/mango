###MANGO-CORE-0.0.2.4###
ver = '1021180076'
def core_test():
    print("Mango Core Response Successful.")
def core_unzip(linux,verbose,termpath):
    # Yes I know, I could've used a function for the failed import thing, but no.
    # Needlessly complex code makes it harder to clone... right?
    import time
    if verbose == "RAI":
        print("Core restricted mode")
        print("Performing functions manually")
        time.sleep(1)
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
        import zipfile
        if verbose == True:
            print("Zipfile import successful")
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
    if verbose == True:
        print("Using Windows.")
    movedir = (re.escape(os.getcwd()) + "\\\\output_final")
    try:
        os.chdir("mangotools")
    except:
        if "mangotools" in os.getcwd():
            pass
        if verbose == "RAI":
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
    if '-' in currentdir:
        print("Directory name contains\nillegal characters. [0cIc]")
        time.sleep(1)
        exit()
    if verbose == "RAI":
        print("Please move the wheel to the current directory manually.")
        while True:
            print("Press enter to verify.")
            input()
            if len(glob.glob('*.whl')) == 0:
                print("No wheel found. Ensure it's in the current working directory.")
                continue
            if len(glob.glob('*.whl')) > 1:
                print("Please only use one wheel.")
                continue
            else:
                print("Found wheel.")
                break
        print("Unzipping wheel...")
        try:
            # What even are variables
            os.rename(((glob.glob("*.whl"))[0]), (((glob.glob("*.whl"))[0]) + ".zip"))
        except:
            print("Auto rename failed.")
            aurnm = False
        if len(glob.glob("*.zip")) == 1:
            print("Auto rename success!")
            aurnm = True
        else:
            if aurnm == False:
                pass
            print("Auto rename failed.")
            aurnm = False
        if aurnm == False:
            while True:
                print("Add .zip to the end of the wheel, to make it a zip file.")
                print("Press enter to verify.")
                input()
                if len(glob.glob("*.zip")) == 1:
                    print("Rename successful.")
                    break
                else:
                    print("Rename failed.")
                    continue
        print("Attempting to unzip...")
        whluzp = zipfile.ZipFile(((glob.glob("*.zip"))[0]), 'r')
        whluzp.extractall(os.getcwd())
        whluzp.close()
        found = (os.listdir(os.getcwd()))
        guesslist = []
        for number,letter in enumerate(found):
            if "." in letter:
                continue
            if "dist-info" in letter:
                continue
            guesslist.append(letter)
        if len(guesslist) == 1:
            print("Assuming package is " + guesslist[0])
            pointer = guesslist[0]
        else:
            choice = False
            while choice == False:
                for number,letter in enumerate(guesslist):
                    print("Is the package '" + letter + "'?")
                    pa_ch = input("[y/n] ")
                    if pa_ch == "y":
                        pointer = letter
                        choice = True
                        break
                    else:
                        continue
        print("Place the python file to append in the current directory.")
        while True:
            print("Press enter to verify.")
            input()
            pys = [f for f in glob.glob("*.py")]
            if len(pys) == 0:
                print("Failed to find any .py files.")
                continue
            if len(pys) > 1:
                templist = []
                for number,letter in enumerate(pys):
                    if "mango" in letter:
                        continue
                    templist.append(letter)
                if len(templist) == 1:
                    pys.clear()
                    pys.append(templist[0])
                else:
                    print("Please only use one .py file.")
                    continue
            if len(pys) == 1:
                string = ("sys.path.insert(0, '" + pointer + "')\n")
                try:
                    with open(pys[0], 'r') as r_f:
                        contents = r_f.read()
                        if verbose == True:
                            print("Read file contents")
                        r_f.close()
                except:
                    print("Failed to open .py file. [1cPf]")
                    time.sleep(1)
                    exit()
                try:
                    os.remove(pys[0])
                    if verbose == True:
                        print("Removed original file")
                except:
                    print("Failed to remove .py file. [1cRf]")
                    time.sleep(1)
                    exit()
                print("Appending to " + pys[0])
                try:
                    with open(pys[0], 'a') as a_f:
                        a_f.write("print('Mango Import Begin')\n")
                        if verbose == True:
                            print("Wrote Mango status print")
                        a_f.write("import sys\n")
                        if verbose == True:
                            print("Wrote import sys")
                        a_f.write(string)
                        if verbose == True:
                            print("Wrote import package string")
                        a_f.write("print('Mango Import Success')\n")
                        if verbose == True:
                            print("Wrote Mango status print")
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
                print("Mango Manual success.")
                time.sleep(1)
                exit()
    while True:
        if termpath == "":
            whlsource = input("Enter absolute path containing .whl: ")
        else:
            whlsource = termpath
        if len(whlsource) == 0:
            print("Invalid Directory")
            if termpath == "":
                continue
            else:
                exit()
        try:
            os.chdir(whlsource)
            os.chdir(currentdir)
        except:
            print("Invalid Directory")
            if termpath == "":
                continue
            else:
                exit()
            continue
        os.chdir(whlsource)
        wheels = glob.glob("*.whl")
        if len(wheels) == 0:
            print("No wheels found.")
            print("Invalid Directory.")
            continue
        if len(wheels) > 1:
            print("Multiple wheels found!")
            for letter,number in enumerate(wheels):
                letter = letter + 1
                letter = str(letter)
                print(letter + ":", number)
            chwhl = input("Select wheel: ")
            try:
                unzipwhl = wheels[(int(chwhl) - 1)]
            except:
                print("Invalid choice")
                continue
        if len(wheels) == 1:
            unzipwhl = wheels[0]
        try:
            shutil.copy2(unzipwhl, currentdir)
        except:
            print("Copy failed. [0cCf]")
            time.sleep(1)
            continue
        if verbose == True:
            print("Copied wheel to mangotools")
        os.chdir(currentdir)
        if verbose == True:
            print("Moved to mangotools")
        try:
            os.rename(unzipwhl, (unzipwhl + ".zip"))
            if verbose == True:
                print("Renamed wheel")
        except:
            print("Failed to rename wheel. [0cFr]")
            time.sleep(1)
            continue
        if verbose == True:
            print("Attempting to unzip...")
        try:
            whluzp = zipfile.ZipFile((unzipwhl + ".zip"), 'r')
            if verbose == True:
                print("Selected zip")
            if not os.path.exists('output_temp'):
                os.mkdir('output_temp')
                if verbose == True:
                    print("Created output_temp")
            whluzp.extractall("output_temp")
            if verbose == True:
                print("Unzipped.")
            whluzp.close()
        except:
            print("Unzip Failed. [0cUf]")
            time.sleep(1)
            continue
        try:
            os.rename((unzipwhl + ".zip"), unzipwhl)
            if verbose == True:
                print("Renamed wheel")
        except:
            print("Failed to rename wheel. [0cFr]")
            time.sleep(1)
            continue
        time.sleep(1)
        break
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
            print("Unzip failed [0cFm].\nPlease try again.")
            exit()
        if verbose == True:
            print("Assuming unzip was successful.")
        os.chdir('..')
        if verbose == True:
            print("Moved back out of output_temp")
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
        return()
    import urllib.request
    try:
        update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/mango/mango-tools/mango-core.py')
        response = urllib.request.urlopen(update)
        newcode = response.read()
        master = newcode.decode()
    except:
        print("Failed to connect.")
        print("Self test failed. [2cSt]")
        return()
    similar = SequenceMatcher(None, master, core_content).ratio()
    similarconv = float(similar * 100)
    similarconv = int(similarconv)
    print("Test returned a " + str(similarconv) + "% Similarity")
    if similar < 0.91:
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
def core_codeprepare(codedir,verbose,linux,source):
    import os
    import sys
    import time
    import glob
    import re
    import shutil
    if verbose == True:
        print("Mango core code prepare ready.")
    if verbose == True:
        print("Preparing to append...")
    currentdir = os.getcwd()
    if not os.path.exists(source):
        print("No output detected.")
        print("Unzip a .whl file before trying to import it.")
        exit()
    print("Output found!")
    in_output = glob.glob("*")
    if verbose == True:
        print("Scanned for files...")
    if verbose == True:
        print("Package name selected.")
    name_delim = re.escape(os.getcwd())
    source = re.escape(source)
    name = source.replace(name_delim, '')
    name = name.replace('\\', '')
    print("Package: " + name)
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
    pyfiles = glob.glob("*.py")
    if verbose == True:
        print("Scanned for .py files")
    if len(pyfiles) == 0:
        print("No .py files found. [1cNp]")
        print("Ensure there are .py files in the chosen directory,\nthen run 'Prepare Code' on the directory again.")
        time.sleep(5)
        exit()
    if len(pyfiles) > 1:
        temppyfiles = []
        for number, letter in enumerate(pyfiles):
            if 'mango' in letter:
                continue
            temppyfiles.append(letter)
        if len(temppyfiles) > 1:
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
        if len(temppyfiles) == 0:
            print("No .py files found. [1cNp]")
            time.sleep(1)
            exit()
        pyc = temppyfiles[0]
    else:
        pyc = pyfiles[0]
    print("Appending file " + pyc)
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
        printer = ('print("Modified using Mango ' + ver + '")\n')
        with open(pyc, 'a') as a_f:
            a_f.write(printer)
            if verbose == True:
                print("Wrote printer")
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
    print("Cleaning up...")
    try:
        if os.path.exists("pkg1.mgs"):
            print("Deleting pointer...")
            os.remove('pkg1.mgs')
        else:
            pass
    except:
        pass
