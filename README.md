
# Welcome to Mango!
A Python module localizer, allowing for packages to be installed without the need for PIP or administrator / sudo privelages.

## PLEASE NOTE
### Mango is still in heavy development, and while many of the features are in place in the code, they may not actually work.
### Please bear with me, I'm working to fix all of the issues you may have with Mango.

## See the wiki for updates and news.

## Using Mango
Mango has a set way of working. Here's how to use it.

First, install mango using mango-installer.py (*DON'T TRY TO INSTALL MANUALLY. IT WON'T WORK.*). The installer will do all the work for you, and ensure all the tools work together. If you're working on a machine that isn't yours, use Restricted Access Install to ensure Mango will work. An option is also available to enable modification of the core. 

### IF USING DEDICATED SCRIPT
1: Launch mango.py and choose "Unpack .whl file". First, enter the directory of the wheel. If there is multiple wheels, Mango will prompt you to choose one. This will create a temporary folder with the unpacked wheel. 


2: Mango will then ask for another directory. Enter the directory containing the python file you want to append. In the target directory, you should now see a folder with the wheel name and a text file called "pkgs*N*.mgs". If you skip this step, Mango will most likely run into a fair few issues when trying to append your python file later on.


3: Mango will now append the python file in the chosen directory with a string that imports the wheel file locally, all without the need for pip. If there are multiple python files, Mango will prompt you to choose one. The procedure is now finished. If you need to append multiple python files, run mango.py again and choose "Prepare code". Enter the same directory at the prompt and choose another python file to append.

### IF USING TERMINAL INPUT (IN DEVELOPMENT)
1: Structure your command like this:
```
$~/python3 mango.py <function [1/2]> <directory containing wheel> <directory containing code> <verbose [True/False]>
```
In the function section, use either 1 for a wheel unpack or 2 for code preperation. You won't need a directory containing a wheel if you're preparing code. If everything is entered correctly, Mango _should_ finish the entire job automatically. Keep in mind this is in heavy development, so Mango may fail at points, or complete the job but not as entirely expected. Report issues on Github if you find any.

## About Mango
# No More Missing Modules!
Mango uses raw .whl files for modules and appends some code at the top of your script to allow it to find the modules. Running code on machines that aren't yours couldn't be easier. Since Mango only uses modules that are pre packaged with Python, installation is simple and very possible on other machines, and allows your program to use whatever modules you want on a machine that you may not be able to install them on ordinarily. 
# For Example...
Let's say your code is:
```
import foo
foo(x)
```
Now, 'foo' doesn't come with python, but is very clearly vitally important to your code. If you need to run this on a machine that isn't yours, you wouldn't be able to, as you'd need sudo / administrator privelages to install 'foo'. With Mango, all you need is your script, Mango, and the raw foo.whl file you can download from the internet. First, Mango will append this to the top of your script:
```
import sys
sys.path.insert(0, "path_to_modules")
```
Making it:
```
import sys
sys.path.insert(0, "path_to_modules")
import foo
foo(x)
```
Great, now your code knows where to look. However, it's  _not_ looking for .whl files, it's looking for .py files. Mango will then unzip the .whl file, using the Python module _Zipfile_.

In essence, Mango automates the process of local module installation, and allows modules to be used without the need for PIP. Mango can also launch your Python scripts for you, and keep all their files and tangents organized in one neat folder. 

# Cross OS Support
Mango is able to run natively on any Python 3.x version on any operating system. Just download the installer and run it on either Windows, MacOSX or (probably any) Linux distribution (I personally use Debian for developing so I would assume Mango is most stable on it) and Mango will do the rest of the work for you. 

# Powerful Flexibility
Mango was designed with every user in mind. As a result, there is a Restricted Access Install mode, which edits the normal procedures Mango goes through when installing. While this is still in development, it allows Mango to download necessary files with less risk of permission errors. Mango also uses a self checking system on the core, to prevent changes being made to the core. This can be disabled, but it is there to stop damaging changes being made.

# Less Obscure Errors
If Mango ever encounters an issue, there is most likely a function to catch it. If the code hits a snag, it'll pause for you and give you and error code for later. I'm still working on indexing all of them, so if you keep hitting one, don't wait around for a complete index, create an issue and I'll get right on it.
