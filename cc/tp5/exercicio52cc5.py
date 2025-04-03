import nmap
import argparse
import sys


def escaneamento_sincrono():
    parser = argparse.ArgumentParser(description='Asynchronous Nmap scanner')
    parser.add_argument("--host", dest="host", help="Target IP / domain", required=True)
    parsed_args = parser.parse_args()

    print("Iniciando escaneamento SINCRONO nas portas abertas e detalhes do sistema operacional...")
    host = parsed_args.host

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




class NmapScannerAsync:
    def __init__(self):
        self.portScannerAsync = nmap.PortScannerAsync()

    def scanning(self):
        while self.portScannerAsync.still_scanning():
            print("Scanning >>>")
            self.portScannerAsync.wait(5)

    def nmapScanAsync(self, hostname, port):
        try:
            print(f"Checking port {port} ..........")
            self.portScannerAsync.scan(hostname, arguments=f"-A -sV -p{port}", callback=self.callbackResult)
            self.scanning()
        except Exception as e:
            print(f"An error occurred: {e}")

    def callbackResult(self,host, scan_result):
        port_state = scan_result['scan'][host]['tcp']
        print("Command line:" + scan_result['nmap']['command_line'])
        for key, value in port_state.items():
            print('Port {0} --> {1}'.format(key, value))

def escanear_asincrono():
    parser = argparse.ArgumentParser(description='Asynchronous Nmap scanner')
    parser.add_argument("--host", dest="host", help="Target IP / domain", required=True)
    parser.add_argument("--ports", dest="ports", help="Target port(s) separated by comma [80,8080 by default]",
                        default="80,8080")
    parsed_args = parser.parse_args()

    port_list = parsed_args.ports.split(',')
    print(f"Iniciando escaneamento assincrono nas portas: {port_list}")
    host = parsed_args.host

    scanner = NmapScannerAsync()
    for port in port_list:
        scanner.nmapScanAsync(host, port)


opcao=input("""----
Iniciar escaneamento de portas via Nmap:
[1] Sincrono
[2] Assincrono
""")

if opcao == "1":
    escaneamento_sincrono()
elif opcao == "2":
    escanear_asincrono()
else:
    print("Opção inválida.")

