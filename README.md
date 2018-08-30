# Welcome to Mango!
A python script launcher and module localizer. Here's what mango will be able to do...

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
Great, now your code knows where to look. However, it's  _not_ looking for .whl files, it's looking for .py files. Mango will then unzip the .whl file, using something like:
```
unzip foo.whl
```
Or, on Windows (subject to change, powershell is difficult): 
```
powershell.exe Expand-Archive foo.whl -DestinationPath path_to_modules
```
In essence, Mango automates the process of local module installation. Mango can also launch your Python scripts for you, and keep all their files and tangents organized in one neat folder. 

# Cross OS Support
Mango is able to run natively on any Python 3.x version on any operating system. Just download the installer and run it on either Windows, MacOSX or (probably any) Linux distribution (I personally use Debian for developing so I would assume thats the most stable release) and Mango will do the rest of the work for you. You can try this out yourself with the installer, it works on both platforms perfectly. It doesn't exactly do much right now but it works to demonstrate what it can do. 
