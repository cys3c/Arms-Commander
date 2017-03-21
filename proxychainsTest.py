import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

print "Your REAL IP address is..."
os.system('dig TXT +short o-o.myaddr.l.google.com @ns1.google.com')
print "Your proxychained IP address is..."
os.system('tor')
os.system('proxychains dig TXT +short o-o.myaddr.l.google.com @ns1.google.com')
