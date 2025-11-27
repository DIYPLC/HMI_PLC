"""
TCP Server for receive file.
https://techexpert.tips/python/python-file-transfer-using-sockets/
"""
import socket


def receive_file(file_receive: str = "rx_file.txt", ip_server: str = "0.0.0.0", tcp_port: int = 50002):
    buffer_size = 1024  # Buffer size for receiving
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
        socket_tcp.bind((ip_server, tcp_port))
        socket_tcp.listen(1)  # Number of TCP clients
        print("Waiting for connection ip=", ip_server, ",port=", tcp_port)
        connection_server, ip_adr = socket_tcp.accept()
        with connection_server:
            print("Connected by", ip_adr)
            with open(file_receive, 'wb') as file_write:
                while True:
                    data_receive = connection_server.recv(buffer_size)
                    if not data_receive:
                        break
                    file_write.write(data_receive)
            print("File received successfully!")


receive_file(file_receive="file.txt")
