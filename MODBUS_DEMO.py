import socket, struct

Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client_socket.connect(('127.0.0.1', 502))

while True: #MODBUS TCP CLIENT
    Client_socket.send(struct.pack(">HHHBBHH",1,0,6,1,3,0,1))
    (Rx0,Rx1,Rx2,Rx3,Rx4,Rx5,R0) = struct.unpack(">HHHBBBH",Client_socket.recv(1500))
    print(R0)

# @COPYLEFT ALL WRONGS RESERVED :)
# Author: VA
# Contacts: DIY.PLC.314@gmail.com
# Date start LIB_PLC: 2014
# License: GNU GPL-2.0-or-later
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# https://www.youtube.com/watch?v=n1F_MfLRlX0
# https://www.youtube.com/@DIY_PLC
# https://github.com/DIYPLC/LIB_PLC
# https://oshwlab.com/diy.plc.314/PLC_HW1_SW1
# https://3dtoday.ru/3d-models/mechanical-parts/body/korpus-na-din-reiku
# https://t.me/DIY_PLC
