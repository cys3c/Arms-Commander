# coding=UTF-8
import os
import socket
import operator
import sys
from termcolor import colored
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

print"""


███╗   ██╗ ██████╗ ██████╗ ███████╗██████╗
████╗  ██║██╔════╝ ██╔══██╗██╔════╝██╔══██╗
██╔██╗ ██║██║  ███╗██████╔╝█████╗  ██████╔╝
██║╚██╗██║██║   ██║██╔══██╗██╔══╝  ██╔═══╝
██║ ╚████║╚██████╔╝██║  ██║███████╗██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝

 ██╗██╗███╗   ██╗██╗   ██╗███████╗███████╗████████╗██╗ ██████╗  █████╗ ████████╗███████╗     ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗██╗
██╔╝██║████╗  ██║██║   ██║██╔════╝██╔════╝╚══██╔══╝██║██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝╚██╗
██║ ██║██╔██╗ ██║██║   ██║█████╗  ███████╗   ██║   ██║██║  ███╗███████║   ██║   █████╗      ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗ ██║
██║ ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ╚════██║   ██║   ██║██║   ██║██╔══██║   ██║   ██╔══╝      ██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║ ██║
╚██╗██║██║ ╚████║ ╚████╔╝ ███████╗███████║   ██║   ██║╚██████╔╝██║  ██║   ██║   ███████╗    ╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║██╔╝
 ╚═╝╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝



"""

class NGrepParameters(object):
    def __init__(self,options,word_Match,dump_Format,output_Pcap,network_Device):
        self.options = options
        self.word_Match = word_Match
        self.dump_Format = dump_Format
        self.output_Pcap = output_Pcap
        self.network_Device = network_Device

    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input('ADDITIONAL OPTIONS (see "ngrep -h" for details): ')),
            str(raw_input('WORD/TERM TO MATCH: ')),
            str(raw_input('DUMP FORMAT (normal|byline|single|none): ')),
            str(raw_input('OUTPUT FILE PATH (/root/ngrepCaptureFile.pcap): ')),
            str(raw_input('NETWORK INTERFACE TO CAPTURE (eth0|wlan0): '))
        )

customNGrep = NGrepParameters.from_input()

ngrep_Cmd_String = "ngrep -iNT%s -w %s -W %s -O %s -d %s" % (customNGrep.options,
                                                            customNGrep.word_Match,
                                                            customNGrep.dump_Format,
                                                            customNGrep.output_Pcap,
                                                            customNGrep.network_Device)
os.system(ngrep_Cmd_String)
