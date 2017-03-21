import os
import socket
import operator
from termcolor import colored

ip_addr_target = None

def scan_fin():
		ip_addr_target = str(raw_input("IP Address or Subnet Range: "))
		save_To_Directory = str(raw_input("Enter the FULL PATH that you want to save to: "))
		nmap_cmd_string = "proxychains nmap -v -O -sF -Pn -T4 -O -F --version-light --traceroute %s -oG %s" % (ip_addr_target, save_To_Directory)
		os.system(nmap_cmd_string)
		return

def scan_xmas():
		ip_addr_target = str(raw_input("IP Address or Subnet Range: "))
		save_To_Directory = str(raw_input("Enter the FULL PATH that you want to save to: "))
		nmap_cmd_string = "proxychains nmap -v -O -sX -Pn -T4 -O -F --version-light --traceroute %s -oG %s" % (ip_addr_target, save_To_Directory)
		os.system(nmap_cmd_string)
		return

def scan_comp():
		ip_addr_target = str(raw_input("IP Address or Subnet Range: "))
		save_To_Directory = str(raw_input("Enter the FULL PATH that you want to save to: "))
		nmap_cmd_string = "proxychains nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script default or (discovery and safe) %s -oG %s" % (ip_addr_target, save_To_Directory)
		os.system(nmap_cmd_string)
		return

def scan_tcp():
		ip_addr_target = str(raw_input("IP Address or Subnet Range: "))
		save_To_Directory = str(raw_input("Enter the FULL PATH that you want to save to: "))
		nmap_cmd_string = "proxychains nmap -p 1-65535 -T4 -A -v --version-light --traceroute %s -oG %s" % (ip_addr_target, save_To_Directory)
		os.system(nmap_cmd_string)

		return

def scan_udp():
		ip_addr_target = str(raw_input("IP Address or Subnet Range: "))
		save_To_Directory = str(raw_input("Enter the FULL PATH that you want to save to: "))
		nmap_cmd_string = "proxychains nmap -p 1-65535 -T4 -A -v --version-light --traceroute %s -oG %s" % (ip_addr_target, save_To_Directory)
		os.system(nmap_cmd_string)

		return

def scan_pn():
		ip_addr_target = str(raw_input("IP Address or Subnet Range: "))
		save_To_Directory = str(raw_input("Enter the FULL PATH that you want to save to: "))
		nmap_cmd_string = "proxychains nmap -sS -Pn -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script default or (discovery and safe) %s -oG %s" % (ip_addr_target, save_To_Directory)
		os.system(nmap_cmd_string)

		return

def scan_Idle():
	return



def NMap_Scan():
			## Add Suboptions All of this must be proxychained
	print "0\tReturn to Main Menu:"
	print "1\tPerform a NMap FIN Scan (Gets past firewalls, usually)"
	print "2\tPerform a NMap Xmas Scan (More intrusive than a FIN scan but still can get past firewalls"
	print "3\tPerform a Comprehensive Scan"
	print "4\tPerform a Scan on TCP ports ONLY"
	print "5\tPerform a Scan on UDP ports ONLY"
	print "6\tPerform a No Ping Scan (Host is not responding to ping probes"
	print "7\tPerform the IDLE/Zombie Scan"
	print colored('8\tPerform a ENTIRELY CUSTOMIZED SCAN with IDS/Firewall Evasion Options, USER UNFRIENDLY ALERT!!!','red','on_white')
	nmap_scan_list = [scan_fin,
										scan_xmas,
										scan_comp,
										scan_tcp,
										scan_udp,
										scan_pn]
	nmap_scan_choice = str(raw_input("Selection: "))

	if  nmap_scan_choice == "1":
		scan_fin()
	elif nmap_scan_choice == "2":
		scan_xmas()
	elif nmap_scan_choice == "3":
		scan_comp()
	elif nmap_scan_choice == "4":
		scan_tcp()
	elif nmap_scan_choice == "5":
		scan_udp()
	elif nmap_scan_choice == "6":
		scan_pn()
	elif nmap_scan_choice == "7":
		scan_Idle()
	elif nmap_scan_choice == "8":
		os.system("gnome-terminal -e 'bash -c \"python /root/ChairForce/CustomNMap.py; exec bash\"'")
	else:
		print "Invalid option selected"
	return
NMap_Scan()
