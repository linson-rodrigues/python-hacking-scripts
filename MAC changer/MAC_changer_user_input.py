#!/usr/bin/env python

import subprocess
import optparse 

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC addrress")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()


interface = input ("interface > ") 
new_mac = input ("New MAC > ")

print("[+] Changing MAC address for " + interface + "to" + new_mac)



#subprocess.call("ifconfig wlan0 down", shell=True)
#subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55:66", shell=True)
#subprocess.call("ifconfig wlan0 up", shell=True)

#subprocess.call("ifconfig" + interface + "down", shell=True)
#subprocess.call("ifconfig" + interface + "hw ether" + new_mac, shell=True)
#subprocess.call("ifconfig" + interface + "up", shell=True)

#more secure commands 
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])