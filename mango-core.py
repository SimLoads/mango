###MANGO-CORE-0.0.0.1###
'''
Created on Fri Jul  6 14:25:30 2018
Written in Python 3.7
'''
def core(pause):
    print("Mango Core Call Success!")
    import os
    print("CD - " + os.getcwd())
    if pause == True:
        os.system("pause")

