
# Welcome to Mango!
A Python module localizer, allowing for packages to be installed without the need for PIP or administrator / sudo privelages.

## PLEASE NOTE
### Mango is still in heavy development, and while many of the features are in place in the code, they may not actually work.
### Please bear with me, I'm working to fix all of the issues you may have with Mango.


## Current News:

10/31/18

Adding linux support as we speak. I mean, making linux work. It works to some extent on Ubuntu Trusty, currently patching all the problems I can with Debian, which should theoratically iron out the bugs in Ubuntu too. More to come.

10/21/18

Today I discovered how bad mangocore actually is at doing it's job. Sure, it does it, but it's trash. Huge overhaul has been made, hopefully it helps fix a few errors with directory changes. Also I think it reduces the size of the file a bit but don't quote me on that one.

Also I added a little thing to the append function that prints "Modified with Mango" when you start any file that has been modified. Plug myself much. That'll be something you can change with the configuration file, when I get around to making that a reality. 

10/18/18

Hello all, still working on mango, I just have some schoolwork to complete for now, so updates may slow slightly. Feel free to dump any issues because I'll get right on them if any pop up, but general updates may be a little slower now :)

10/16/18

Why does this repository have over 2,000,000 additions and deletions, you might be asking? That is down to the fact that I accidentally pushed my entire working directory to github, which included every file in Mango ever made, everything that PyGame comes with like 3 times over, and Pycryptodomex countless times. I then had to hurridly delete all of these, so that accounted for just over 4,000,000 total changes. Oops.

10/15/18

Recent testing has proved that Mango doesn't really work with Python 3.4 and most likely below. This is caused by some problems with directory variables, and they're being worked on. 

Direct terminal input is now available! See below for correct usage.

Beware of entering incorrect directories - Mango is now configured to delete targets much more agressively. While it shouldn't affect any of your files, be warned that anything in _any_ output_temp or output_final will be completely removed. 

## Using Mango
Mango has a set way of working. Here's how to use it.

### IF USING DEDICATED SCRIPT
1: Install mango using mango-installer.py (*DON'T TRY TO INSTALL MANUALLY. IT WON'T WORK.*). The installer will do all the work for you, and ensure all the tools work together. If you're working on a machine that isn't yours, use Restricted Access Install to ensure Mango will work. An option is also available to enable modification of the core. 


2: Launch mango.py and choose "Unpack .whl file". First, enter the directory of the wheel. If there is multiple wheels, Mango will prompt you to choose one. This will create a temporary folder with the unpacked wheel. 


3: Mango will then ask for another directory. Enter the directory containing the python file you want to append. In the target directory, you should now see a folder with the wheel name and a text file called "pkgs*N*.mgs". If you skip this step, Mango will most likely run into a fair few issues when trying to append your python file later on.


4: Mango will now append the python file in the chosen directory with a string that imports the wheel file locally, all without the need for pip. If there are multiple python files, Mango will prompt you to choose one. The procedure is now finished. If you need to append multiple python files, run mango.py again and choose "Prepare code". Enter the same directory at the prompt and choose another python file to append.

### IF USING TERMINAL INPUT (IN DEVELOPMENT)
1: Structure your command like this:
```
$~/mango.py <function [1/2]> <directory containing wheel> <directory containing code> <verbose [True/False]>
```
In the function section, use either 1 for a wheel unpack or 2 for code preperation. If everything is entered correctly, Mango _should_ finish the entire job automatically. Keep in mind this is in heavy development, so Mango may fail at points, or complete the job but not as entirely expected. Report issues on Github if you find any.

## About Mango
# No More Missing Modules!
Mango uses raw .whl files for modules and appends some code at the top of your script to allow it to find the modules. Running code on machines that aren't yours couldn't be easier. Since Mango only uses modules that are pre packaged with Python, installation is simple and very possible on other machines, and allows your program to use whatever modules you want on a machine that you may not be able to install them on ordinarily. 
### For Example...
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
Mango is able to run natively on any Python 3.x version on any operating system. Just download the installer and run it on either Windows, MacOSX or (probably any) Linux distribution (I personally use Debian for developing so I would assume thats the most stable release) and Mango will do the rest of the work for you. You can try this out yourself with the installer, it works on both platforms perfectly. It doesn't exactly do much right now but it works to demonstrate what it can do. 

# Powerful Flexibility
Mango was designed with every user in mind. As a result, there is a Restricted Access Install mode, which subverts the normal procedures Mango goes through when installing. While this is still in development, as is most of the stuff around Mango, it allows Mango to download necessary files with less risk of permission errors. Mango also uses a self checking system on the core, to prevent changes being made to the core. This is, of course, available to be disabled, but it is there to stop damaging changes being made. 

# Less Obscure Errors
If Mango ever encounters an issue, there is most likely a function to catch it. If the code hits a snag, it'll pause for you and give you and error code for later. I'm still working on indexing all of them, so if you keep hitting one, don't wait around for an index, just message me and I'll try and solve it.
