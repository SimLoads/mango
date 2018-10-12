
# Welcome to Mango!
A python script launcher and module localizer. 

## PLEASE NOTE
### Mango is still in heavy development, and while many of the features are in place in the code, they may not actually work.
### Please bear with me, I'm working to fix all of the issues you may have with Mango.

# No More Missing Modules!
Mango uses raw .whl files for modules and appends some code at the top of your script to allow it to find the modules. Running code on machines that aren't yours couldn't be easier. Since Mango only uses modules that are pre packaged with Python, installation is simple and very possible on other machines, and allows your program to use whatever modules you want on a machine that you may not be able to install them on ordinarily. 
### For Example...
Let's say your code is:
```
import foo
foo(x)
```
Now, 'foo' doesn't come with python, but is very clearly vitally important to your code. If you need to run this on a machine that isn't yours, you wouldn't be able to, as you'd need sudo / administrator privelages to install 'foo'. With Mango, all you need is your script, Mango, and the raw foo.whl file you can download on your own PC. First, Mango will append this to the top of your script:
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
