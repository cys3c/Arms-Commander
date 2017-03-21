import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

opt_List = [
    '\n\t#1. List Priority: 1 Alerts',
    '#2 .... Priority: 2 Alerts',
    '#3 .... Priority: 3 Alerts'
]

print ("\n\t".join(opt_List))
opt_Choice = str(raw_input("Enter a option: "))
        # pattern = str(raw_input("Enter a STRING: "))
        # directory = str(raw_input("Enter a DIRECTORY to search in: "))
        # cmd_String = "egrep -i -r '*\%s\*' %s --color" % (pattern, directory)
        # print colored('Here are your RESULTS for GREP COMMAND','red','on_white')
        # os.system(cmd_String)
        # return
## apparently I need to setup a conf file for output
if opt_Choice == "1":
    pattern = "Priority: 1"
    cmd_String = "egrep -i -r '*\%s\*' /var/log/snort --color" % (pattern)
    os.system(cmd_String)
elif opt_Choice == "2":
    pattern = "Priority: 2"
    cmd_String = "egrep -i -r '*\%s\*' /var/log/snort" % (pattern)
    os.system(cmd_String)
elif opt_Choice == "3":
    pattern = "Priority: 3"
    cmd_String = "egrep -i -r '*\%s\*' /var/log/snort" % (pattern)
    os.system(cmd_String)
else:
    print colored('You have entered a invalid option')
