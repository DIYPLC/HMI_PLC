import socket, struct

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 502))

while True: # MODBUS TCP CLIENT
    client_socket.send(struct.pack(">HHHBBHH",1,0,6,1,3,0,1))
    (rx0,rx1,rx2,rx3,rx4,rx5,r0) = struct.unpack(">HHHBBBH",Client_socket.recv(1500))
    print(r0)

