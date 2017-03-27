# Arms-Commander
Malware Suite/Menu designed for "Speedy and No-Mistakes Penetration Testing", written in Python 2.7.13 and tested on Kali Linux 4.6, originally intended to only perform the Reconnaissance and Enumeration Stages (it's role is dramatically expanded now). Requires Python 2.7 + Pip + Termcolor Module. All code is entirely free to be used in your own projects. To install, you can either run the "autoInstallLinux.sh" script after "chmod 777" first, OR you can manually create the /root/ArmsCommander directory, copy everything in there, and then type "python /root/ArmsCommander/ArmsCommander.py"

# Installing Dependencies
#This will ensure that your version of Python is at least 2.7.13 and that Pip and Termcolor Modules are installed

Unzip the Arms-Commander.zip file
Navigate to directory
type "chmod 777 dependencyInstall.sh"
type "./dependencyInstall.sh"

# Installing the Malware Suite
#This will add a Desktop Launcher, as well as copy the main launcher into /usr/local/bin
#You will be able to run Arms-Commander by typing "ArmsCommander.py" in terminal

Unzip
Navigate to directory
type "chmod 777 autoInstallLinux.sh"
type "./autoInstallLinux.sh"
Run AC by typing "ArmsCommander.py" in Terminal
The main directory is /root/ArmsCommander

# DISCLAIMER
#This is tested in Kali Linux ONLY
#For Ubuntu and other Debian Derivatives, a lot of commands that AC runs will not work in the first place because it requires System-Level Root
#For example, Metasploit requires root permissions or else you would get vague errors (try typing "route -n" as a regular user, and then as Root)

# Other Dependencies
#For reasons of your personal preference and security, I did not make it mandatory to install APKTools, Java or Ruby
#You will have to install them yourself if you want to use the APK Malware Injection Toolkit
#However, it's just a apt-get install away, and the required scripts and Java Signing Utilities are including in ArmsCommander regardless.
