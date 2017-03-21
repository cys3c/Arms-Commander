# coding=UTF-8

import os
import socket
import operator
from termcolor import colored
import sys
import importlib
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

class menuParameters(object):
    def __init__ (self, opt_List, opt_Dict):
        self.opt_List = opt_List
        self.opt_Dict = opt_Dict


    @classmethod
    def Embedded_Dev_Branch(cls):
        return cls(
            [
                        '\n\t#1. ExitBootServices/UEFI-Hooking',
                        '#2. Python Scripts',
                        '#3. SQRL, or "Secret Squirrel"',
                        '#4. "QuarkMatter", or EFI Enabled Persistence for Mac OSX (Arbitrary Kernel Implants)',
                        '#5. "Weeping Angel", a series of toolkits and scripts that ultimately allows the CIA to wiretap some sort of Television',
                        '#6. "Hive", a "Redirector" used by the CIA COG (Computer Operations Group) in "Remote Network Operatios"',
                        '#7. "Maddening Whispers", toolkit that gives remote access to a "Vanguard-Based Device"',
                        '#8. "BaldEagle", Privilege Escalation Exploit using the Hardware Abstraction Layer Daemon',
                        '#9. "Bee Sting", or a toolkit that enables iFrame Injection, in other words, "Click-Jacking" Attacks'
                        ],
            {
                '1': opt_1_EDB(),
                '2': 'opt_2_EDB()',
                '3': 'opt_3_EDB()',
                '4': 'opt_4_EDB()'
            },
        )
    def Remote_Dev_Branch(cls):

        return cls(
            [
                        '\n\t#1. Install 3rd party Python Libraries for "DART testing"',
                        '#2. Wiretapping Capabilities from Source Dumps of Italian Firm "Hacking Team"',
                        '#3. Wiping Locked Files with Shamoon Malware',
                        '#4. Webcam Capture with DirectShow and VFW',
                        '#5. Keyloggers (DirectInput, WindowsAPI, and Windows-Hook)',
                        '#6. Module Persistence',
                        '#7. APC Injection (Ansynchronous Procedure Calls) into the Kernel',
                        '#8. PSP Detection, Anti-Debugging/Fuzzing, and Anti-Reverse-Engineering a proprietary program',
                        '#9. Stealth by DLL Injection Methods',
                        '#10. ShoulderSurfer, Extracts data from Exchange Databases versions 1.0, 1.1, and 2010',
                        '#11. Reforge Scripting, Overview of Encryption Process for CIA proprietary code'

                        ]

        )
    def Op_Support_Branch(cls):
        return cls(

        )
    def Auto_Implant_Branch(cls):
        return cls(

        )

    def Mobile_Device_Branch(cls):
        return cls(

        )
    def Net_Device_Branch(cls):
        return cls(

        )
def opt_1_EDB():
    print colored('UEFI Hook Selected','red','on_white')#UEFI Hook
    return
def opt_2_EDB(): #Python scripts
    return
def opt_3_EDB(): #Squirrel
    return
def opt_4_EDB(): #QuarkMatter
    return
def opt_5_EDB(): #Weeping Angel
    return
def opt_6_EDB(): #Hive
     return
def opt_7_EDB(): #Maddening Whispers
    return
def opt_8_EDB(): #Baldeagle
    return
def opt_9_EDB(): #Bee Sting
    return


def main():
    opt_List = [
            '\n\t#1. Embedded Development Branch',
            '#2. Remote Development Branch',
            '#3. Operational Support Branch',
            '#4. Mobile Development Branch',
            '#5. Automated Implant Branch',
            '#6. Network Devices Branch'
    ]

    print colored('Choose a CIA development branch to access known exploits','red','on_white')
    os.system('cat /root/ArmsCommander/disclaimerWikiLeaksCIA.txt')
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Pick a number: "))

    if opt_Choice == "1":
        os.system('clear')
        Branch = menuParameters.Embedded_Dev_Branch()
        print Branch.opt_List
        print ("\n\t".join(Branch.opt_List))
        opt_Choice = str(raw_input("Enter a option from the list: "))
        if opt_Choice in Branch.opt_Dict:
            print "Running %s" % Branch.opt_Dict[opt_Choice]
            function_String = Branch.opt_Dict[opt_Choice]
            #This wont work either because I have a separate function. The dictionary item are STRINGS.
            function_Call = getattr(Branch.opt_Dict, Branch.opt_Dict[opt_Choice])
            print function_Call
            function_Call()
            #dictFile[inputVariable]
            #function_Call = Branch.opt_Dict[opt_Choice]
            # function_Call = "{0}[{1}]".format(
            #                     Branch.opt_Dict,
            #                     opt_Choice
            # )
            # print function_Call
            # function_Call()
        else:
            print 'You entered a invalid option'
            main()

    elif opt_Choice == "2":
        os.system('clear')
        Remote_Dev_Branch_Menu()
    elif opt_Choice == "3":
        os.system('clear')
        Op_Support_Branch_Menu()
    elif opt_Choice == "4":
        os.system('clear')
        Auto_Implant_Branch_Menu()
    elif opt_Choice == "5":
        os.system('clear')
        Mob_Dev_Branch_Menu()
    elif opt_Choice == "6":
        os.system('clear')
        Net_Devices_Branch_Menu()
    elif opt_Choice == "0":
        main_Menu()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
    return
main()
