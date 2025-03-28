from scapy.all import Ether, ARP, srp

def arp_scan(ip_range):

    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range)

    answered, _ = srp(arp_request, timeout=2, verbose=0)

    print("Hosts ativos na rede local:")
    print("--------------------------")
    for sent, received in answered:
        print(f"IP: {received.psrc} - MAC: {received.hwsrc}")

if __name__ == "__main__":
    rede_local = "192.168.1.0/24"
    arp_scan(rede_local)