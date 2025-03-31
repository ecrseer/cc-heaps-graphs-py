import nmap
import sys
import argparse


def escaneamento_sincrono():
    command = "nmap_operating_system.py <IP_address>"

    if len(sys.argv) == 1:
        print(command)
        sys.exit()

    parser = argparse.ArgumentParser(description='Asynchronous Nmap scanner')
    parser.add_argument("--host", dest="host", help="Target IP / domain", required=True)

    print("Iniciando escaneamento SINCRONO nas portas abertas e detalhes do sistema operacional...")
    host = sys.argv[1]
    portScanner = nmap.PortScanner()
    open_ports_dict = portScanner.scan(host, arguments="-O -v")

    if open_ports_dict is not None:
        open_ports_dict = open_ports_dict.get("scan", {}).get(host, {}).get("tcp", {})

        print("Open port --> Service")
        port_list = open_ports_dict.keys()

        for port in port_list:
            print(port, "-->", open_ports_dict[port]['name'])

        print("\n--- Operating System details ----\n")

        try:
            osmatch = portScanner[host]['osmatch'][0]['osclass'][0]
            print("Details about the scanned host are:\t", osmatch.get('cpe', 'N/A'))
            print("Operating system family is:\t\t", osmatch.get('osfamily', 'N/A'))
            print("Type of OS is:\t\t\t\t", osmatch.get('type', 'N/A'))
            print("Generation of Operating System:\t", osmatch.get('osgen', 'N/A'))
            print("Operating System Vendor is:\t\t", osmatch.get('vendor', 'N/A'))
            print("Accuracy of detection is:\t\t", osmatch.get('accuracy', 'N/A'))
        except (KeyError, IndexError):
            print("OS details could not be determined.")


escaneamento_sincrono()