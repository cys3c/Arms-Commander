# coding=UTF-8

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

global yes_no_choice
global yes_or_no
Tool_List = [
        'whois',
        'sqlmap',
        'zaproxy', #owasp zap proxy
        'nmap',
        'theharvester',
        'tor',
        'proxychains',
        'burpsuite',
        'ngrep',
        'dsniff', #tcpkill
        'macchanger'
]

def toolkit_install():
    print colored('Entering toolkit installation','red','on_white')
    cmd_str = "sudo apt-get install %s" % ' '.join(map(str, Tool_List))
    #According to stack exchange, this remaps the entire list as strings, by its VALUES only, so it excludes the quotes and commas and brackets.
    #Then it adds a space between each list item
    #print colored(cmd_str,'red','on_white')
    #placeholder for os.system command
    os.system('sudo apt-get update')
    os.system(cmd_str)
    print colored('Installation complete, please restart Arms Commander','red','on_white')

def kali_full_install():
    print colored('Beginning a full toolkit installation of Kali-Linux-Full Complete System from Apt. Please do not interrupt this process','red','on_white')
    cmd_str = "sudo apt-get install kali-linux-full"
    #print colored(cmd_str,'red','on_white')
    #placeholder for os.system command
    os.system('sudo apt-get update')
    os.system(cmd_str)
    print colored('Installation complete, please fully reboot your computer to ensure that everything worked','red','on_white')
#def yes_or_no():
    #yes_no_choice = str(raw_input("Enter Y or N: "))


def main():
    print colored('What would you like to do?','red','on_white')
    opt_List = [
            "\n\t#1. Install JUST ONLY the required tools and/or update to latest version",
            "#2, if you are running this on Kali, simply begin the full install of Kali Linux to get everything out of the way without a upgrade/dist-upgrade"
    ]
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Select your install method: "))

    if opt_Choice == "1":
        print colored('You have selected, INSTALL ONLY THE REQUIRED TOOLS, are you sure? Y or N','blue','on_white')
        yes_no_choice = str(raw_input("Enter Y or N: "))
        if yes_no_choice == "Y":
            #Enter the tool install
            toolkit_install()
        elif yes_no_choice == "N":
            pass
        else:
            pass
    elif opt_Choice == "2":
        print colored('You have selected, Full Install of Kali Linux, are you sure? Y or N','blue','on_white')
        yes_no_choice = str(raw_input("Enter Y or N: "))
        if yes_no_choice == "Y":
        #Enter the Kali-Full-Install
            kali_full_install()
        elif yes_no_choice == "N":
            pass
        else:
            pass
    else:
        print "You have entered a invalid option"
    main()
main()
