# coding=UTF-8

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

B7_One_Opt_List = [
        '\n\t#1. TCPKill',
        '#2. NGrep',
        '#3. Fuser'
]
def TCPKill():
    return
def NGrep():
    return
def Fuser():
    return

def B7_One():
    print ("\n\t".join(B7_One_Opt_List))
    Opt_Choice = str(raw_input("Enter a Option: "))

    if Opt_Choice == "1":
        TCPKill()
    elif Opt_Choice == "2":
        NGrep()
    elif Opt_Choice == "3":
        Fuser()
    else:
        print colored('You have entered a invalid option: ')
    main() #so u could call a function that has been declared later

B7_Two_Opt_List = [
        '#1. vBooter, so far this is the ONLY option'
]

def vBooter():
    return

def B7_Two():
    print ("\n\t".join(B7_Two_Opt_List))
    Opt_Choice = str(raw_input("Enter a Option: "))
    if Opt_Choice == "1":
        vBooter()
    elif Opt_Choice == "2":
        return
    else:
        print colored('You have entered a invalid option: ')
    main()

B7_Three_Opt_List = [
        '\n\t#1. LOIC, Low-Orbit Ion Cannon, can be used against individual IPs to disrupt service',
        '#2. HOIC, High-Orbit Ion Cannon, specifically a HTTP-Attack Method. Has no other purpose.'
]

def LOIC(): #Research how to safely implement this without introducing malware to downloaders
    return
def HOIC():
    return

def B7_Three():
    print ("\n\t".join(B7_Three_Opt_List))
    Opt_Choice = str(raw_input("Enter a option: "))
    if Opt_Choice == "1":
        LOIC()
    elif Opt_Choice == "2":
        HOIC()
    else:
        print colored('You have entered a invalid option','red','on_white')
    main()
    
B7_Four_Opt_List = [
        '\n\t#1. Suggested IP Stressers',
        '#2. Ways to Acquire BitCoin, universally accepted'
]

def B7_Four_1():
    return
def B7_Four_2():
    return

def B7_Four():
    print ("\n\t".join(B7_Four_Opt_List))
    return

B7_Opt_List = [
        '\n\t#1. Solo Booting Options',
        '#2. Free Booting Options (vBooter)',
        '#3. Community-Driven Booting Options (LOIC)',
        '#4. Paid-For Stresser Services'
]

def main():
    print ("\n\t".join(B7_Opt_List))
    B7_Opt_Choice = str(raw_input("Enter a CHOICE: "))
    if B7_Opt_Choice == "1":
        B7_One()
    elif B7_Opt_Choice == "2":
        B7_Two()
    elif B7_Opt_Choice == "3":
        B7_Three()
    elif B7_Opt_Choice == "4":
        B7_Four()
    else:
        print colored('You have entered a invalid option','red','on_white')
    main()
main()
