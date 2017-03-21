# coding=UTF-8
import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

print """


██╗██████╗ ███████╗    ███████╗██╗      ██████╗  ██████╗ ██████╗ ███████╗██████╗
██║██╔══██╗██╔════╝    ██╔════╝██║     ██╔═══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██║██║  ██║███████╗    █████╗  ██║     ██║   ██║██║   ██║██║  ██║█████╗  ██████╔╝
██║██║  ██║╚════██║    ██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██╗
██║██████╔╝███████║    ██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝███████╗██║  ██║
╚═╝╚═════╝ ╚══════╝    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝



"""
## Need to add input strings so users can specify parameters
#usage %prog -i <iface> -s <src> -t <target> -c <count>
IDS_Interface = str(raw_input("Enter your network interface (e.g. Ethernet=eth0, Wireless=wlan0, etc.): "))
IDS_Source = str(raw_input("Enter SOURCE IP (e.g. 10.0.1.2): "))
IDS_Target = str(raw_input("Enter TARGET IP (e.g. 199.204.53.23)): "))
IDS_PacketCount = int(raw_input("Enter the amount of packets you want to send (e.g. 50000): "))
IDS_cmd_string = "python /root/ArmsCommander/10-idsFoil.py -i %s -s %s -t %s -c %d" % (IDS_Interface, IDS_Source, IDS_Target, IDS_PacketCount)
#this one is bugged. FIXED, had to state full path
os.system(IDS_cmd_string)
