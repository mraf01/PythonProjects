from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.http import HTTPRequest
from scapy.layers.http import HTTPResponse

iPkt=0

def process_pkt(pkt):
    global iPkt
    iPkt+=1
    print(f"Ho ricevuto pacchetto {iPkt} lungo {pkt[IP].len}")

sniff(iface="eth0", filter="tcp", prn=process_pkt)