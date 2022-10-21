import socket, struct

Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client_socket.connect(('127.0.0.1', 502))

while True: #MODBUS TCP CLIENT
    Client_socket.send(struct.pack(">HHHBBHH",1,0,6,1,3,0,1))
    (Rx0,Rx1,Rx2,Rx3,Rx4,Rx5,R0) = struct.unpack(">HHHBBBH",Client_socket.recv(1500))
    print(R0)

#  +---------+
#  | GNU GPL |
#  +---------+
#  |
#  |
#  .= .-_-. =.
# ((_/)o o(\_))
#  `-'(. .)`-'
#  |/| \_/ |\
#  ( |     | )
#  /"\_____/"\
#  \__)   (__/
# @COPYLEFT ALL WRONGS RESERVED :)
# Author: VA
# Contacts: DIY.PLC.314@gmail.com
# License: GNU GPL v2
