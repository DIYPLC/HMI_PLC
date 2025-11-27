"""
TCP Client for transmit file.
https://techexpert.tips/python/python-file-transfer-using-sockets/
"""
import socket


def send_file(file_transmit: str = "tx_file.txt", ip_client: str = "127.0.0.1", tcp_port: int = 50002):
    print("Start send file.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
        socket_tcp.connect((ip_client, tcp_port))
        with open(file_transmit, 'rb') as file_read:
            while True:
                data_transmit = file_read.read(1024)  # Buffer size for sending
                if not data_transmit:
                    break
                socket_tcp.sendall(data_transmit)
        print("File send successfully!")


send_file(file_transmit="file.txt", ip_client="192.168.88.18")
