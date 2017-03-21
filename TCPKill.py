# coding=UTF-8

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen


print """


████████╗ ██████╗██████╗     ██╗  ██╗██╗██╗     ██╗
╚══██╔══╝██╔════╝██╔══██╗    ██║ ██╔╝██║██║     ██║
   ██║   ██║     ██████╔╝    █████╔╝ ██║██║     ██║
   ██║   ██║     ██╔═══╝     ██╔═██╗ ██║██║     ██║
   ██║   ╚██████╗██║         ██║  ██╗██║███████╗███████╗
   ╚═╝    ╚═════╝╚═╝         ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝

 ██╗██╗  ██╗██╗██╗     ██╗     ███████╗     ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗ ██████╗ ███╗   ██╗███████╗██╗
██╔╝██║ ██╔╝██║██║     ██║     ██╔════╝    ██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝╚██╗
██║ █████╔╝ ██║██║     ██║     ███████╗    ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║   ██║   ██║██╔██╗ ██║███████╗ ██║
██║ ██╔═██╗ ██║██║     ██║     ╚════██║    ██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║   ██║   ██║██║╚██╗██║╚════██║ ██║
╚██╗██║  ██╗██║███████╗███████╗███████║    ╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║   ╚██████╔╝██║ ╚████║███████║██╔╝
 ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝


"""

opt_List = [
            '\n\t#1. Terminate a connection to a host, website, or IP', #requires only the name/URL/IP address
            #tcpkill host <192.168.x.x> or URL
            '#2. Terminate a connection to a specified port', #requires both the interface and the port
            #tcpkill -i eth0 port 21 kills all outbound connections
            '#3. Selectively exclude two IPs from, to TERMINATE, and to NOT TERMINATE'
            #tcpkill ip host 192.168.1.2 and not 192.168.1.111
]

def main():
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter your CHOICE: "))

    if opt_Choice == "1":
        print colored('Selected %s','red','on_white') % opt_List[0]
        kill_host = str(raw_input("The URL/Hostname/IP Address of connection you want to kill: "))
        kill_cmd = "tcpkill host %s" % kill_host
        os.system(kill_cmd)

    elif opt_Choice == "2":
        print colored('Selected %s','red','on_white') % opt_List[1]
        interface = str(raw_input("The network interface where the offender resides that you want to kill connection to: "))
        kill_port = str(raw_input("The port number or range you want to kill: "))
        kill_cmd = "tcpkill -i %s port %s" % (interface, kill_port)
        os.system(kill_cmd)

    elif opt_Choice == "3":
        print colored('Selected %s','red','on_white') % opt_List[2]
        kill_host = str(raw_input("The IP addr of the device you want to KILL: "))
        exclude_host = str(raw_input("The IP addr of the device you want to EXCLUDE: "))
        kill_cmd = "tcpkill ip host %s and not %s" % (kill_host, exclude_host)
        os.system(kill_cmd)

    else:
        print colored('You have entered a invalid option','red','on_white')
main()
