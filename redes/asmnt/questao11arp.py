import scapy.all as scapy
from scapy.layers.l2 import Ether, ARP


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_mac_address(ip_address):
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request = ARP(pdst=ip_address)
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    if answered_list:
        return answered_list[0][1].hwsrc
    return None


def process_sniffed_packet(packet):
    print("buscando arp spoof na rede")
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        original_mac = get_mac_address(packet[ARP].psrc)
        response_mac = packet[ARP].hwsrc

        if original_mac and original_mac != response_mac:
            print("[*] ALERT!!! You are under attack, ARP table is being poisoned!")


if __name__ == '__main__':
    sniff("wlan0")
