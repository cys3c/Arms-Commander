# coding=UTF-8

## NEW CHANGE NOTES BY CHANG TAN LISTER

## DUE TO THE INCREDIBLE LENGTH OF ALL OF THESE PROGRAMS, TECHNIQUES AND CODE, THE FILE Vault7.py will NOT be a primary program file.
## It is simply TOO LONG and unmaintainable
## As of March 8th, 2017, this python file will now point to and launch NEW, CLEAN, DEDICATED MODULES also located in the same Directory
## FURTHERMORE, if there is any additional variables that requires import from THIS FILE , then the python file will be IMPORTED in the first line of the requesting module

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

os.system('cat /root/ArmsCommander/bannerVault7.txt')

def main():
    opt_List = [
            '\n\t#1. Embedded Development Branch',
            '#2. Remote Development Branch',
            '#3. Operational Support Branch',
            '#4. Mobile Development Branch',
            '#5. Automated Implant Branch',
            '#6. Network Devices Branch',
            '#999. Preplanned Menu Directory Structure (For coding reference only)'
    ]

    print colored('Choose a CIA development branch to access known exploits','red','on_white')
    os.system('cat /root/ArmsCommander/disclaimerWikiLeaksCIA.txt')
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Pick a number: "))

    if opt_Choice == "1":
        os.system('clear')
        Embed_Dev_Branch_Menu()
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
    elif opt_Choice == "999":
        os.system('cat /root/ArmsCommander/V7REProjectDevelopmentStructure.txt')
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()

def Embed_Dev_Branch_Menu():
    opt_List = [
                '\n\t#1. ExitBootServices/UEFI-Hooking',
                '#2. Python Scripts',
                '#3. SQRL, or "Secret Squirrel"',
                '#4. "QuarkMatter", or EFI Enabled Persistence for Mac OSX (Arbitrary Kernel Implants)',
                '#5. "Weeping Angel", a series of toolkits and scripts that ultimately allows the CIA to wiretap some sort of Television',
                '#6. "Hive", a "Redirector" used by the CIA COG (Computer Operations Group) in "Remote Network Operatios"',
                '#7. "Maddening Whispers", toolkit that gives remote access to a "Vanguard-Based Device"',
                '#8. "BaldEagle", Privilege Escalation Exploit using the Hardware Abstraction Layer Daemon',
                '#9. "Bee Sting", or a toolkit that enables iFrame Injection, in other words, "Click-Jacking" Attacks'
                ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a exploit to use: "))
    if opt_Choice == "1":
        opt_1_EDB()
    elif opt_Choice == "2":
        opt_2_EDB()
    elif opt_Choice == "3":
        opt_3_EDB()
    elif opt_Choice == "4":
        opt_4_EDB()
    elif opt_Choice == "5":
        opt_5_EDB()
    elif opt_Choice == "6":
        opt_6_EDB()
    elif opt_Choice == "7":
        opt_7_EDB()
    elif opt_Choice == "8":
        opt_8_EDB()
    elif opt_Choice == "9":
        opt_9_EDB()
    elif opt_Choice == "0":
        main()
    else:
        print colored('You have entered a invalid option','red','on_white')
        Embed_Dev_Branch_Menu()
def opt_1_EDB(): #UEFI Hook
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
def Remote_Dev_Branch_Menu():
    opt_List = [
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
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a exploit to use: "))

    if opt_Choice == "1":
        opt_1_RDB()
    elif opt_Choice == "2":
        opt_2_RDB()
    elif opt_Choice == "3":
        opt_3_RDB()
    elif opt_Choice == "4":
        opt_4_RDB()
    elif opt_Choice == "5":
        opt_5_RDB()
    elif opt_Choice == "6":#Module Persistence
        opt_6_RDB()
    elif opt_Choice == "7":
        opt_7_RDB()
    elif opt_Choice == "8":
        opt_8_RDB()
    elif opt_Choice == "9":
        opt_9_RDB()
    elif opt_Choice == "10":
        opt_10_RDB()
    elif opt_Choice == "11":
        opt_11_RDB()
    elif opt_Choice == "0":
        main()
def opt_1_RDB(): #DART testing libraries
    return
def opt_2_RDB(): #Italian firm code leak
    return
def opt_3_RDB(): #Shamoon
    return
def opt_4_RDB(): ##4. Webcam Capture with DirectShow and VFW
#Warning this requires a LEGITIMATE copy of the DarkComet RAT project which was discontinued
#THere maybe malware-laden source code everywhere
#It is really hard to find this shit. Nothing but malware everywhere
    return
def opt_5_RDB(): #Keyloggers (DirectInput, WindowsAPI, and Windows-Hook
    return
def opt_6_RDB(): #Module Persistence

    print colored('Information derived here. Please enter a number to select a option, first = 1 for OPTION','red','on_white')
    opt_List = [
        '\n\t#1. Persistence by compromising the Volume Boot Record before Microsoft POST-BOOT detection services start up',
        '#2. .... By using a image file to inject a registry key into a Windows Machine',
        '#3. .... By placing a customized DLL file, FIRST by using a rootkit called "Hikit"to bypass security measures',
        '#4. .... By injecting a fake DLL file relating to the Windows Fax Server File',
        '#5. .... By taking advantage of a Windows Explorer Extension Shell DLL ("COM DLL")'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a option/method: "))
#According to the WikiLeaked documents, there are at least five different methods to gain persistance

# First. Volume Boot Record Persistance https://wikileaks.org/ciav7p1/cms/page_9535670.html
    if opt_Choice == "1":
        return
    #Requires original carberp source code on github
    #Then requires Stolen Goods 2.0 with carberp (modified) to get persistent ma;ware
    #Correction, "Stolen Goods" is a modification of "carberp"

# Second. Image File execution
    elif opt_Choice == "2":
        return
    #Inject a registry key (that I saved in the /`/ArmsCommander/CIA_V7_Source_Code_And_Programs`directory)

# Third. The OCI.DLL vulnerability
    elif opt_Choice == "3":
        return
    #Requires Hikit to permit the payload to go off
    #We are dropping our custom DLL "payload" into the C:\Windows\System32\wbem\oci.dll directory
    #Warning, the Hikit toolkit is considered to be "APT-Malware", in other words it Advanced Persistent Threat (not the Linux package installer lol)
    #This and darkcomet were found on a Github account named "Lunde" https://github.com/lunde/RATs
    #File is RATs-master, RAT = Remote Administration Tool
    #Cloning website wite HTTrack site ripper March 8th, 2017

# Fourth.
    elif opt_Choice == "4":
        return
    #
    # # This is a simple DLL hijacking attack that we have successfully tested against Windows XP,Vista and 7.
    # A DLL named fxsst.dll normally resides in
    # \Windows\System32 and is loaded by explorer.exe.
    # Placing a new DLL with this name in \Windows results in this being loaded into explorer instead of the original DLL.
    # On Windows Vista and above, the DLL‘s reference count must be increased by calling LoadLibrary on itself to avoid being unloaded.
    # #
    # # This achieves persistence, stealth, and (in some cases) PSP avoidance.
    # HOWEVER, it MUST be combined with a UAC (User Account Control) Breaching Exploit, or else Windows 7 and up will prompt the user for creds
    # In other words, this program cannot run as Administrator by itself
    elif opt_Choice == "5":#Windows Explorer Extension Shell
        #https://wikileaks.org/ciav7p1/cms/page_2621765.html
        #Apparently not the best option to maintain persistence
        #also this bug was found back int he Windows XP days
        return
    else:
        print colored('You have entered a invalid option','red','on_white')

def opt_7_RDB(): #APC Injection
    return
def opt_8_RDB(): ##8. PSP Detection, Anti-Debugging/Fuzzing, and Anti-Reverse-Engineering a proprietary program
    return
def opt_9_RDB(): ##9. Stealth by DLL Injection Methods
    return
def opt_10_RDB():#10. ShoulderSurfer, Extracts data from Exchange Databases versions 1.0, 1.1, and 2010
    return
def opt_11_RDB():#11. Reforge Scripting, Overview of Encryption Process for CIA proprietary code
    return

def Op_Support_Branch_Menu():
    opt_List = [
                '\n\t'
                ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a exploit to use: "))
#     ##if opt_Choice == ""
#     ###el#if opt_Choice == ""
#
#     elif opt_Choice == "0"
#         main()
#     else:
#         print colored('You have entered a invalid option','red','on_white')
#         Op_Support_Branch_Menu()
def Mob_Dev_Branch_Menu():
    opt_List = [
                '\n\t'
                ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a exploit to use: "))
#     #if opt_Choice == ""
#
#     ##el#if opt_Choice == ""
#
#     elif opt_Choice == "0"
#         main()
#     else:
#         print colored('You have entered a invalid option','red','on_white')
#         Mob_Dev_Branch_Menu()
#
def Auto_Implant_Branch_Menu():
    opt_List = [
                '\n\t'
                ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a exploit to use: "))
#     #if opt_Choice == ""
#
#     ##el#if opt_Choice == ""
#
#     elif opt_Choice == "0"
#         main()
#     else:
#         print colored('You have entered a invalid option','red','on_white')
#         Auto_Implant_Branch_Menu()
def Net_Devices_Branch_Menu():
    opt_List = [
                '\n\t'
                ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a exploit to use: "))
#     #if opt_Choice == ""
#
#     ##el#if opt_Choice == ""
#
#     elif opt_Choice == "0"
#         main()
#     else:
#         print colored('You have entered a invalid option','red','on_white')
#         Net_Devices_Branch_Menu()
main()
