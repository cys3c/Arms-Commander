	#scan_Cmd_String = "proxychains nmap -v -O %s %s -f %s -S %s -e %s -T4 -F --version-light --traceroute --spoofmac %s -oN %s" %
#We have the following variables that can be set as a class attribute

    #(scan_Type,
    #scan_Ping_Yes_No,
    #scan_Fragment_Amt,
    #scan_Spoof_IP,
    #scan_Interface,
    #scan_Spoof_MAC,
    #scan_Target,
    #scan_Output_Location)

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen


print colored('USER FRIENDLINESS WARNING:','red','on_white')
print """ There are hundreds of NMap scan varieties. All of them could be custom-tailored to trigger a response from a particular server. Because of this reason,
I highly recommend reading up on the NMap Help Manual (NMap -h) or the Manpage (man nmap).

This menu DOES ask you a few questions in an effort to "introduce" you to the more advanced NMap Options. But these questions are usually beyond the familiarity of a "casual user".

The questions are...

1. The type of scan, (TCP Scan examples, sS = TCP SYN, -sF = TCP FIN, -sI = Idle/Zombie Scan)
2. Whether or not you want to ping the host, sometimes excluding pings (-Pn) would trigger the victim to respond
3. The byte size of the packets
4. A OTHER IP you would like to spoof (like the IP of a machine that you are certain your victim will respond to)
5. The source interface. Basically, YOUR NETWORK CARD.
6. The level of aggressiveness of your scan-timing.
7. The intensity of your Operating-System Detection
8. The MAC address you want to spoof (certain places use certain routers with similar MAC headers)
9. The TARGET IP (finally)
10. The OUTPUT FILE you want to save to, ENTIRE PATH, like... (/root/Documents/customScan.txt)
"""
#Create a overview of the class and what datafields are there
class ScanParameters(object):
    #define a template for the class basically, te fields will alwyas fill in this order from the initialize function
    def __init__ (self, scantype, ping, fragment, spoof_IP, interface, TimingMode, Intensity, spoof_MAC, target_IP, output_File): #the problem is that it is stored in EXACLTLY this order in syntax
        self.scantype = scantype # Apparently it is NOT easily done to have a dictionary associated with a class
        self.ping = ping
        self.fragment = fragment
        self.spoof_IP = spoof_IP
        self.interface = interface
        self.TimingMode = TimingMode
        self.Intensity = Intensity
        self.spoof_MAC = spoof_MAC
        self.target_IP = target_IP
        self.output_File = output_File

    #define the user input part of the class for each field
    #this is your chance to make it "user-friendly"
    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input('SCAN TYPE (-sS = SYN scan, -sF = FIN scan, -sX = Christmas Scan -sU = UDP Scan): ')),
            str(raw_input('PING SCAN? Type -Pn=No Ping or Leave BLANK: ')),
            str(raw_input('PACKET FRAGMENTATION? (e.g. 50000, 5000): ')),
            str(raw_input('IP TO SPOOF: ')),
            str(raw_input('SOURCE INTERFACE (eth0=Internal Eternet, wlan0=Internal Wifi): ')),
            str(raw_input('TIMING MODE (0=SNEAKY, 5=AGGRESSIVE): ')),
            str(raw_input('OS DETECTION INTENSITY (0=LIGHT, 9=INTENSE): ')),
            str(raw_input('MAC TO SPOOF: ')),
            str(raw_input('TARGET IP: ')),
            str(raw_input('OUTPUT FILE, FULL DIRECTORY: '))
        )

#Mandatory to be able to call the values back
CustomScan = ScanParameters.from_input()
#To call upon a value entered by user it is CustomScan.AttributeField


scan_Cmd_String = "proxychains nmap -v -O %s %s -f %s -S %s -e %s -T%s -F --version-intensity %s --traceroute --spoof-mac %s %s -oN %s" % (CustomScan.scantype,
                                                                                                                                CustomScan.ping,
                                                                                                                                CustomScan.fragment,
                                                                                                                                CustomScan.spoof_IP,
                                                                                                                                CustomScan.interface,
                                                                                                                                CustomScan.TimingMode,
                                                                                                                                CustomScan.Intensity,
                                                                                                                                CustomScan.spoof_MAC,
                                                                                                                                CustomScan.target_IP,
                                                                                                                                CustomScan.output_File)
print colored(scan_Cmd_String,'red','on_white')
os.system(scan_Cmd_String)
