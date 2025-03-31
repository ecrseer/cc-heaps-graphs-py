import nmap
import argparse


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

    def callbackResult(host, scan_result):
        # print(host, scan_result)
        port_state = scan_result['scan'][host]['tcp']
        print("Command line:" + scan_result['nmap']['command_line'])
        for key, value in port_state.items():
            print('Port {0} --> {1}'.format(key, value))


if __name__ == "__main__":
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
