import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
        # os.system("gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/proxychainsTest.py; exec bash\"'")

os.system('cat /root/ArmsCommander/banner_BadUSB.txt')

def DuckyFlasher():
    opt_List = [
        '\n\t#0. Return to the Main Menu',
        '#1. Run DuckyFlasher',
        '#INSTALL. Install DuckyFlasher and DFU-Programmer'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Select a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        #placeholder to run Ducky-Flasher
        os.system('ducky-flasher')
        return
    elif opt_Choice == "INSTALL":
        #placeholder for INSTALLER
        print colored('Running APT-get Update','red','on_white')
        os.system('sudo apt-get update')
        print colored('Installing DFU-Programmer','red','on_white')
        os.system('sudo apt-get install dfu-programmer')
        print colored('Installing the setup-package for Ducky-Flasher','red','on_white')
        os.system('sudo python /root/ArmsCommander/ducky-flasher/setup.py')
        print colored('All done! Remember to read on how to set your USB Rubber Ducky into DFU Mode before proceeding to use Ducky-Flasher','red','on_white')
        return
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
    return

def main():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Run DONT PATCH ME BRO, to easily generate the inject.bin file for USB Rubber Duckies',
        '#2. Run Ducky-Flasher, to easily and safely flash your USB Rubber Ducky Firmware'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        os.system("gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/DPMB.py; exec bash\"'")
        main()
    elif opt_Choice == "2":
        #placeholder for the DuckyFlasher Setup script
        DuckyFlasher()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
    return
main()
