import socket
import os

HOST_TODAS_INTERFACES = '0.0.0.0'


def main():
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    try:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
        sniffer.bind((HOST_TODAS_INTERFACES, 0))

        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        habilita_modo_promiscuo_se_windows(sniffer)

        print(f'Escutando em {HOST_TODAS_INTERFACES}')

        ler_pacotes(sniffer)
    except socket.error as e:
        print(f'Erro de socket: {e}')
    finally:
        if 'sniffer' in locals():
            sniffer.close()


def habilita_modo_promiscuo_se_windows(sniffer):
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


def ler_pacotes(sniffer):
    try:
        while True:
            raw_buffer = sniffer.recvfrom(65565)
            print(f'Pacote recebido: {raw_buffer}')

    except KeyboardInterrupt:
        print('Encerrando a captura.')
        if os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == '__main__':
    main()
