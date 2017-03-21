### RECOMMENDED OPERATING SYSTEMS ###

Highly recommended that this should be installed on specifically a Kali Linux Operating System or in a VM

This WILL WORK on Ubuntu and Debian, however it requires "a lot more work" to get what are basically, tools meant for Kali, functioning properly in any Debian or Debian Derivative

More patient users can wait for me to compile a specific VM image/Kali Kernel that has this PRE-INSTALLED

## EASY INSTALLATION INSTRUCTIONS (Kali Linux ONLY) ##

Download the zip file

Extract the entire folder

Open terminal and run the autoinstall script, FIRST, enable the script by...

'chmod 777 /$PATH/autoInstallLinux.sh' # to change permissions to executable on the installer script, where $PATH is the directory path for your operating system, 
# for example, for Ubuntu it would be, if your username is "Susan", 
'chmod 777 /home/Susan/Downloads/ArmsCommander/autoInstallLinux.sh'
'/$PATH/autoInstallLinux.sh' # to execute the installer
# Go to your desktop, rightclick on the new Launch Arms Commander icon and select Allow Executing File as Program
# Double click on it and it should automatically launch it
# First things first, update and/or installed the reqired toolkits, type 'INSTALL' at the main menu where it will automatically use sudo apt-get update/install to make sure you have everything you need

### MANUAL INSTALLATION INSTRUCTIONS ###

## Step #1: Unzip the entire contents of the zip file, INCLUDING the folder named "ArmsCommander" into your ##

/root directory 

## Step #2: Run the program the first time by opening your Linux Terminal typing... ##

'python /root/ArmsCommander/ArmsCommander.py'

WITHOUT the quotes

## Step #3: If this is your first time, you should begin the toolkit installation to ensure that all toolkits are installed and/or updated, type in the main menu ##

'INSTALL'

### Tool Information and Credits ###

Arms Commander v0.0.1 Alpha Release
Written by Chang Tan Lister in Python 2.7.13
March 2nd, 2017
ctlister@sigaint.onion

A fast, efficient menu meant to dramatically speed up the time it takes for the initial phases of penetration testing, 
Reconnaissance, Enumeration and a handful of Fuzzing Attacks

Mr. Lister does not officially claim credit for "Arms Commander", nor is "Arms Commander" meant to be any form of "Commercial Software".
You are more than free to develop and/or expand on the capabilities of "Arms Commander" to your own liking. 
All that He asks, is to use this to further enhance cybersecurity measures around the world, LEGALLY.

### Credits to Developers of the tools that A.C. Uses ###

Credit is retained by the creators of the individual toolkits and/or operating systems that Arms Commander relies on, including but not limited to...

	Offensive Security (Kali Linux 4.6.4)
	The Open Web Application Security Project (Zap Proxy)
	Debian Security Tools Packaging Team 
	Miroslav Stampar, who wrote SQLMap
	Gordon Lyon, who wrote NMap

	Among others...

### USAGE AGREEMENT, LEGAL USE AND "MISUSE" ###

By downloading and installation this software, you agree that you will not attack government, military, and/or political entities with this program. 
The author does not claim responsibilities for any subsequent criminal/civil actions filed against you, or arrest/conviction/incarceration as a result of that.

Please refer to Chapter 18 of the United States Code, Subsection 1030: Computer Fraud and Abuse Act

Note that 18 USC 1030 does not fully cover or encompass the extent of possible criminal acts that can arise from misuse of this program!

YOU HAVE BEEN WARNED!!!
