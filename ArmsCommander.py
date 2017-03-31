#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

global show_banner
global main_Opt_Choice
global scan_Target
global scan_Save
scan_Target = None
scan_Save = None

#def global_Banner():

#    global show_banner = True
#    return

#global_Banner()
show_banner = True

def bannerPage():
    os.system('cat /root/ArmsCommander/ACBanner.txt')
    print colored('Arms Commander v0.0.4 by Chang Tan Lister, Limited Release, Alpha Implementation','red','on_white')
    print """
    Welcome to "Arms Commander", the premier command console for preset initial hacking attacks on dedicated "Hacker Battleships".
    """
    print colored('New Features','red','on_white')
    print """
    Version v0.0.4
    !!!! Added BadUSB Attack Options
    !!!! DuckyFlasher is included in the suite
    !!!! DuckEncoder is included
    !!!! New Installer Scripts for DFU-Reprogramming for Malicious Thumbdrives

    Version v0.0.3
    !!!! Streamlined and reorganized Main Menu
    !!!! A Android APK malware injector and java signer, requires installation of the APKTool in your respective repo
    !!!! Linux Terminal Command to Start AC, type "ArmsCommander.py"
    !!!! Easy Installer Script, type "chmod 777 autoInstallerLinux.sh" and run the Script
    !!!! Icon Launcher that will be placed on Kali Linux Desktop
    """
    return



def batteryFive():
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/APKmalwareInjector.py; exec bash\"'")
    main_Menu()
    return

def batteryOne():
    B1_Target_URL = str(raw_input("Enter the URL you want to perform recon on: "))
    B1_Save_Output = str(raw_input("Enter the full path of the output file you want to save to: "))
    print colored('Scans Commencing, Do Not Interrupt until Completed! (The command prompt tells you completed)','red','on_white')
    #dig and Nslookup
    B1_cmd_str_1 = "dig {0} >> {1}".format(
                                str(B1_Target_URL),
                                str(B1_Save_Output)
                                )
    B1_cmd_str_2 = "nslookup {0} >> {1}".format(B1_Target_URL, B1_Save_Output)
    B1_cmd_str_3 = "whois {0} >> {1}".format(B1_Target_URL, B1_Save_Output)
    B1_cmd_str_4 = "fierce -dns {0} >> {1}".format(B1_Target_URL, B1_Save_Output)
    print colored('Running DIG and NSLookup','red','on_white')
    os.system(B1_cmd_str_1)
    print colored('Pulling WHOIS Records','red','on_white')
    os.system(B1_cmd_str_2)
    B1_cmd_str_3 = "whois {0} >> {1}".format(B1_Target_URL, B1_Save_Output)
    os.system(B1_cmd_str_3)
    B1_cmd_str_4 = "fierce -dns {0} >> {1}".format(B1_Target_URL, B1_Save_Output)
    os.system(B1_cmd_str_4)
    #Fierce

    #theharvester
    print colored('Running The Harvester to search for any public emails, ALL domains, this could take a while!','red','on_white')
    harvester_cmd_string = "theharvester -d {0} -l 500 -b all -h myresults.html >> {1}".format(str(B1_Target_URL), str(B1_Save_Output))
    os.system(harvester_cmd_string)
    #Completed
    print colored ('COMPLETED, check {0} for your reconnaissance scans','red','on_blue').format(str(B1_Save_Output))
    main_Menu()
    return

# class BatteryTwo_Parameters(object):
#     def __init__(self, network_Interface, source_IP, target_IP, IDS_PacketCount, SQL_verbosity, SQL_URL, SQL_Detection_Level, SQL_Detection_Risk, SQL_Brute_Force_Checks, SQL_Traffic_File, SQL_SaveConfig):
#         self.network_Interface = network_Interface
#         self.source_IP = source_IP
#         self.target_IP = target_IP
#         self.IDS_PacketCount = IDS_PacketCount
#         self.SQL_verbosity = SQL_verbosity
#         self.SQL_URL = SQL_URL
#         self.SQL_Detection_Level = SQL_Detection_Level
#         self.SQL_Detection_Risk = SQL_Detection_Risk
#         self.SQL_Brute_Force_Checks = SQL_Brute_Force_Checks
#         self.SQL_Traffic_File = SQL_Traffic_File
#         self.SQL_SaveConfig = SQL_SaveConfig
#
#     @classmethod
#     def from_input(cls):
#         return cls(
#             str(raw_input("IDS FLOODER - Enter your network interface: ")),
#             str(raw_input("IDS FLOODER - Enter your source IP (Local LAN IP address): ")),
#             str(raw_input("IDS FLOODER - Enter the IP address of your target: ")),
#             int(raw_input("IDS FLOODER - Enter the amount of fake packets you want to send: ")),
#             str(raw_input("SQLMap - Enter the level of verbosity from 0 to 6: ")),
#             str(raw_input("SQLMap - Enter the URL of website that you are attacking: ")),
#             str(raw_input("SQLMap - Enter the detection level from 1 to 5: ")),
#             str(raw_input("SQLMap - Enter the risk level of tests from 1 to 3: ")),
#             str(raw_input("SQLMap - Enter the type of brute force checks, either or both '--common-tables' or '--common-columns': ")),
#             str(raw_input("SQLMap - Enter the path you want to save the traffic file (*.txt): ")),
#             str(raw_input("SQLMap - Enter the path you want to save the config file (*.ini): "))
#         )
#
def batteryTwo():
    batteryTwo_Options = [
            '\n\t#1. Combine IDS Flood with SQLMap',
            '#2. Combine IDS Flood with OWASP Zap',
            '#3. Run BurpSuite and perform connection-by-connection recon including finding the real IP address of a webhost and testing payloads'
    ]
    print ("\n\t".join(batteryTwo_Options))

    batteryTwo_Opt_Choice = str(raw_input("Select a option: "))
    if batteryTwo_Opt_Choice == "1":
        os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/IDS_flood.py; exec bash\"'")
        os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/SQLMapCustom.py; exec bash\"'")
    elif batteryTwo_Opt_Choice == "2":
        os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/IDS_flood.py; exec bash\"'")
        os.system("gnome-terminal -e 'bash -c \"zaproxy; exec bash\"'")
    elif batteryTwo_Opt_Choice == "0":
        main_Menu()
    elif batteryTwo_Opt_Choice == "3":
        os.system("gnome-terminal -e 'bash -c \"burpsuite; exec bash\"'")
    else:
        print colored('You have entered a invalid option','red','on_white')
    main_Menu()
    return
#     Battery_Two = BatteryTwo_Parameters.from_input()
#     print colored('Launching Flooding Attack against Intrusion Detection Systems','red','on_white')
#
# #IDS Flood code
#
#     #
#     #os.system("gnome-terminal -e 'bash -c \"%s; exec bash\"'") % IDS_Flood_cmd_string
#     #os.system("gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/10-idsFoil.py -i %s -s %s -t %s -c %d; exec bash\"'") % (
#         #Battery_Two.network_Interface,
#         #Battery_Two.source_IP,
#         #Battery_Two.target_IP,
#         #int(Battery_Two.IDS_PacketCount)
#
#     IDS_Flood_cmd_string = "sudo python /root/ArmsCommander/10-idsFoil.py -i %s -s %s -t %s -c %d" % (
#                             Battery_Two.network_Interface,
#                             Battery_Two.source_IP,
#                             Battery_Two.target_IP,
#                             Battery_Two.IDS_PacketCount
#                             )
#     print colored(IDS_Flood_cmd_string,'red','on_white')
#     #os.system(IDS_Flood_cmd_string)
#     os.system("gnome-terminal -e 'bash -c \"%s; exec bash\"'") % IDS_Flood_cmd_string
#     #.format(
#                         #Battery_Two.network_Interface,
#                         #Battery_Two.source_IP,
#                         #Battery_Two.target_IP,
#                         #Battery_Two.IDS_PacketCount
#     #)
#
#     #execfile('10-idsFoil.py -i {0} -s {1} -t {2} -c {3}').format(
#                         #Battery_Two.network_Interface,
#                         #Battery_Two.source_IP,
#                         #Battery_Two.target_IP,
#                         #Battery_Two.IDS_PacketCount
#                         #)
# #SQLMAP code
#     print colored('Running SQLMAP with Tor proxychaining','red','on_white')
#
#     os.system("gnome-terminal -e 'bash -c \"sudo tor; exec bash\"'")
#     os.system("gnome-terminal -e 'bash -c \"sudo sqlmap -u {0} -v {1} --tor --check-tor -o --level={2} --risk={3} {4} -t {5} --save={6} --beep --dependencies; exec bash\"'").format(
#                         SQL_URL,
#                         SQL_verbosity,
#                         SQL_Detection_Level,
#                         SQL_Detection_Risk,
#                         SQL_Brute_Force_Checks,
#                         SQL_Traffic_File,
#                         SQL_SaveConfig
#     )
#     main_Menu()
#     return

def batteryThree():
    B3_Options = [
                '\n\t#0 Return to the main menu',
                '#1. Run a series of NMap scan, gradually increasing in intensity/intrusiveness. First with a unintrusive scan that can get past firewalls, eventually reaching a full comprehensive scan',
                '#2. Use a completely customized scan'
    ]

    print ("\n\t".join(B3_Options))
    B3_Opt_Choice = str(raw_input("Enter a scan choice: "))

    if B3_Opt_Choice == "1":
        scan_Target = str(raw_input("Either enter a specific IP address, or a entire IP address range: "))
        scan_Save = str(raw_input("Enter the full path of the save file location: "))
        print colored('Beginning a stealthy FIN Scan. This may be quick, depending on how many machines you are scanning. Usually gets past firewalls','red','on_white')
        nmap_cmd_string = "sudo proxychains nmap -v -O -sF -Pn -T4 -O -F --version-light --traceroute %s -oG %s" % (scan_Target, scan_Save)
        print colored(nmap_cmd_string,'red','on_white')
        os.system(nmap_cmd_string)
        print colored('Following up with a slightly more intrusive XMas Scan. The information returned usually is exactly the same as before','red','on_white')
        nmap_cmd_string = "sudo proxychains nmap -v -O -sX -Pn -T4 -O -F --version-light --traceroute %s -oG %s" % (scan_Target, scan_Save)
        print colored(nmap_cmd_string,'red','on_white')
        os.system(nmap_cmd_string)
        print colored('Now finalizing with a Comprehensive NMap scan','red','on_white')
        nmap_cmd_string = "sudo proxychains nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script default %s -oG %s" % (scan_Target, scan_Save)
        print colored(nmap_cmd_string,'red','on_white')
        os.system(nmap_cmd_string)
        print colored('Scans complete, find your scans at %s','red','on_white') % scan_Save
        main_Menu()
    elif B3_Opt_Choice == "2":
        os.system("gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/CustomNMap.py; exec bash\"'")
    elif B3_Opt_Choice == "0":
        main_Menu()
    else:
        print colored('You have entered a invalid option','red','on_white')
    main_Menu()
    return
def batteryFour():
    B4_Options = [
                '\n\t#0 Return to the main menu',
                '#1. Activate Tor + Proxychains, concealing your IP address whenever a command is run with a "proxychains" prefix',
                '#2. Activate Network Monitoring Tools',
                '#3. Cover your tracks, clear bash history and thumbnails immediately.'

    ]
    print ("\n\t".join(B4_Options))

    B4_Opt_Choice = str(raw_input("Enter a choice: "))

    if B4_Opt_Choice == "1":
    #os.system("gnome-terminal -e 'bash -c \"python /root/ChairForce/proxychainsTest.py; exec bash\"'")
        os.system("gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/proxychainsTest.py; exec bash\"'")
    elif B4_Opt_Choice == "2":
        #IDS
        print colored('Launching Intrusion Detection System','red','on_white')
        os.system("gnome-terminal -e 'bash -c \"sudo /root/ArmsCommander/IDS.sh; exec bash\"'")

        #p0f
        print colored('Starting p0f, passive OS fingerprinter','red','on_white')
        os.system("gnome-terminal -e 'bash -c \"sudo p0f; exec bash\"'")
        #viewActiveConnections
        print colored('Listing Real Time Active Connections','red','on_white')
        os.system("gnome-terminal -e 'bash -c \"sudo /root/ArmsCommander/viewActiveConnections.sh; exec bash\"'")
    elif B4_Opt_Choice == "0":
        main_Menu()
    elif B4_Opt_Choice == "3":
        cover_tracks()
        print colored('Both your bash shell history and your thumbnails cache has been WIPED. Warning, the data can still be recovered, you must overwrite the disk with zeroes using the Kali Installer to fully eliminate forensic recovery','red','on_white')
        print"""
        Furthermore, using this does not completely eliminate the need to...

        1. Delete your trash
        2. Clean out your auth logs

        This only prevents LE from finding the most incriminating information in five minutes
        """
        print colored('Retain a lawyer before you resort to doing anything bad','red','on_white')

    else:
        print colored('You have entered a invalid option','red','on_white')
        batteryFour()
    main_Menu()
def cover_tracks():
	os.system('rm -rf /root/.bash_history')
	os.system('rm -rf /root/.cache/thumbnails')

def fuser():

    opt_List = [
                '\n\t#1. LOOKUP all process IDs of a port and protocol',
                '#2. Terminate all connections of a port/protocol'
    ]
    if opt_Choice == "1":
        fuser_port = str(raw_input("Enter a PORT: "))
        fuser_protocol = str(raw_input("Enter a PROTOCOL(TCP/UDP): "))
        fuser_cmd_string = "fuser %s/%s" % (fuser_port, fuser_protocol)
        os.system(fuser_cmd_string)
    elif opt_Choice == "2":
        fuser_port = str(raw_input("Enter a PORT: "))
        fuser_protocol = str(raw_input("Enter a PROTOCOL(TCP/UDP): "))
        fuser_cmd_string = "fuser -k %s/%s" % (fuser_port, fuser_protocol)
        os.system(fuser_cmd_string)
    else:
        print colored('You have entered a invalid option','red','on_white')
    main_Menu()

def batterySix():
    B6_Options = [
            '\n\t#0 Return to the main menu',
            '#1. Use TCP Kill to directly sent reset packets against a offending host or port',
            '#2. Use NGrep to further investigate traffic between you and a offender',
            '#3. Use MACChanger to immediately change you MAC address and furthermore terminate any active connections',
            '#4. Use Fuser to identify and/or kill a port range'
    ]

    print ("\n\t".join(B6_Options))
    B6_Opt_Choice = str(raw_input("Enter a choice: "))

    if B6_Opt_Choice == "1":
        os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/TCPKill.py; exec bash\"'")
        #Write the TCP Kill Program first and then insert the execution code here
    elif B6_Opt_Choice == "2":
        os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/NGrepCustom.py; exec bash\"'")
        #You can port the NGrep module
    elif B6_Opt_Choice == "3":
        os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/macChanger.py; exec bash\"'")
        #YOu can port the macchanger module here
    elif B6_Opt_Choice == "4":
        fuser()
    elif B6_Opt_Choice == "0":
        pass
    else:
        print colored('You have entered a invalid option','red','on_white')
    main_Menu()
    return
Tool_List = [
        '\n\tDig',
        'NSLookup',
        'Whois',
        'SQLMap',
        'OWASP ZAP Proxy',
        'NMap',
        'The Harvester',
        'Tor',
        'Proxychains',
        'BurpSuite',
        'NGrep',
        'TCPKill',
        'macchanger'
]

def open_Installer():
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/AC_Installer.py; exec bash\"'")
    main_Menu()
    return

def installer():
    print colored('DISCLAIMER','red','on_white')
    print """
    Arms Commander is written by the author with the assumption that you have a copy of Kali Linux 4.6 or higher, with a Linux Kernel of 4.6.4 or higher.

    Many of the commands and software that A.C. requires, are indeed available for different Debian distros like Ubuntu,
    however your mileage may vary in succesful installation and use. Most of the required tools require system-level root to work properly.

    Personally, the author finds the "insecurity" of System-Level Root to be exagerrated, as compromising a Linux machine could be as easy as adding another user with full privileges,

    Furthermore, Arms Commander already assumes that you know how to properly use the following tools... as the purpose of A.C. is meant to dramatically speed up the
    initial process of penetration testing reconnaissance and enumeration.

    Given the lack of "user-friendliness", I would highly recommend just installing Kali as a Virtual Machine and loading Arms Commander from there,
    or simply wait for one of my custom VM images to be available, which is a coming-soon project, with a customized Kali VM + Arms Commander + All Required Tools Pre-Installed
    """
    print ("\n\t".join(Tool_List))
    print colored('Type CONTINUE to proceed with the installation','red','on_white')

    continue_Question = str(raw_input(""))
    if continue_Question == "CONTINUE":
        open_Installer()
    else:
        main_Menu()
def batterySeven():
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/batterySeven.py; exec bash\"'")
    main_Menu()

def batteryEight():
    opt_List = [
        '\n\t#0 Return to Main Menu',
        '#1. Metasploit Framework',
        '#2. Armitage',
        '#3. Easy-Peasey, MSFVenom Payload Generator',
        '#4. Veil-Evasion',
        '#5. Social Engineers Toolkit'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input(""))

    if opt_Choice == "1":
        os.system('clear')
        metasploit()
    elif opt_Choice == "2":
        os.system('clear')
        armitage()
    elif opt_Choice == "3":
        os.system('clear')
        msfvenom()
    elif opt_Choice == "4":
        os.system('clear')
        veilevasion()
    elif opt_Choice == "5":
        os.system('clear')
        socialengineertoolkit()
    elif opt_Choice == "0":
        main_Menu()
    else:
        print colored('You have entered a invalid option','red','on_white')
        batteryEight()
    return

def metasploit():
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/Metasploit.py; exec bash\"'")


def armitage():
    os.system("gnome-terminal -e 'bash -c \"proxychains armitage; exec bash\"'")


def msfvenom():
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/EZPZ.py; exec bash\"'")
    return

def veilevasion():
    os.system("gnome-terminal -e 'bash -c \"veil-evasion; exec bash\"'")


def socialengineertoolkit():
    os.system("gnome-terminal -e 'bash -c \"set; exec bash\"'")

def batteryNine():
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/BadUSBAttacks.py; exec bash\"'")
    main_Menu()
    return

def main_Menu_Decision_Loop():
    main_Opt_Choice = str(raw_input("CHOICE: "))
    if main_Opt_Choice == "1":
        os.system('clear')
        batteryOne()
    elif main_Opt_Choice == "2":
        os.system('clear')
        batteryTwo()
    elif main_Opt_Choice == "3":
        os.system('clear')
        batteryThree()
    elif main_Opt_Choice == "4":
        os.system('clear')
        batteryFour()
    elif main_Opt_Choice == "5":
        os.system('clear')
        batteryFive()
    elif main_Opt_Choice == "6":
        os.system('clear')
        batterySix()
    elif main_Opt_Choice == "7":
        os.system('clear')
        batterySeven()
    elif main_Opt_Choice == "8":
        os.system('clear')
        batteryEight()
    elif main_Opt_Choice == "9":
        os.system('clear')
        batteryNine()
    elif main_Opt_Choice == "INSTALL":
        os.system('clear')
        installer()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main_Menu()
    return


if show_banner:
    bannerPage()
    show_banner = False
else:
    pass
main_Opt_List = [
                '\n\t#1. Battery One: URL RECON, Recon a webpage, Dig + Nslookup + Fierce DNS + Whois Lookup',
                '#2. Battery Two: LOCATE WEBAPP WEAKNESSES, Pop a smoke screen by flooding their Intrusion Detection System while simultaneously running a SQLMap and OWASP scanner attack',
                '#3. Battery Three: IP RECON via Port Scan using NMap and other tools',
                '#4. Battery Four: STANDARD DEFENSIVE MEASURES, activate Tor and Proxychains, all required monitoring tools',
                '#5. Battery Five: ANDROID APK MALWARE INJECTION, Inject a Metasploit Meterpreter Payload into a Android APK Installer File.',
                '#6. Battery Six: ACTVE NETWORK DEFENSES, terminate connections with NGrep and TCPKill, change your MAC address',
                '#7. Battery Seven: BOOTERS',
                '#8. Battery Eight: REMOTE EXPLOITATION, Metasploit, MSFVenom, Armitage, Veil-Evasion, Social Engineer Tookit',
                '#9. Battery Nine: BAD USB ATTACKS, Use the BadUSB Vulnerability to deliver undetectable attacks by thumbdrive',
                'Type INSTALL in ALL CAPS if you require a installation of the toolkit'
]

def main_Menu():
    print colored('Choose your artillery','red','on_white')
    print ("\n\t".join(main_Opt_List))
    main_Menu_Decision_Loop()
    return
main_Menu()
