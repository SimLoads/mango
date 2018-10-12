import sys
sys.path.insert(0, 'Cryptodome')
def func1():
    import subprocess
    execute = subprocess.Popen("unziptest.bat" ,
                            shell=True, stdout=subprocess.PIPE)
    execute.communicate()
    func2()
def func2():
    print("beans")
    os.system("pause")
    func1()
import os
func2()
