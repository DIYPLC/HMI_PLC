#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
MODBUS TCP SERVER
http://www.binarytides.com/python-socket-server-code-example/
"""

import socket #FOR TCP SERVER
import select #FOR TCP SERVER
import struct #FOR MODBUS PROTOCOL
import array  #FOR MODBUS PROTOCOL

IP_ADDRESS = "0.0.0.0"
TCP_PORT = 502
MODBUS_ADDRESS = 1
Register = array.array('H',[0]*65536) #holding Register

def Debug_test_init_registers():
    """Test init regesters value"""
    for i in range(65536): #i = 0...65536-1
        Register[i] = i
    return

def Limit(In = 0, Max = 65535, Min = 0):
    """Limit to a safe value"""
    _In = int(In)
    _Out = int(0)
    if (_In >= Max):
        _Out = Max
    else:
        if (_In <= Min):
            _Out = Min
        else:
            _Out = _In
    return _Out

def Read_register(Register_address = 0):
    """Safe reading from an array"""
    address = Limit(In = Register_address, Max = 65535, Min = 0)
    return Register[ address ]

def Write_register(Register_address = 0, Register_value = 0):
    """Safe writing to an array"""
    address = Limit(In = Register_address, Max = 65535, Min = 0)
    value   = Limit(In = Register_value, Max = 65535, Min = 0)
    Register[ address ] = value
    return

def Two_uint8_to_uint16(uint8_hi = 0, uint8_lo = 0):
    _uint8_hi = (int(uint8_hi) & 0xFF) << 8
    _uint8_lo = int(uint8_lo) & 0xFF
    _res = (_uint8_hi | _uint8_lo) & 0xFFFF
    return _res

def Error_function_not_supported(Rx_ADU):
    """Error function not supported"""
    Tx_Transaction_ID_hi = Rx_ADU[0]
    Tx_Transaction_ID_lo = Rx_ADU[1]
    Tx_Protocol_ID_hi    = Rx_ADU[2]
    Tx_Protocol_ID_lo    = Rx_ADU[3]
    Tx_Message_length_hi = 0
    Tx_Message_length_lo = 3
    Tx_MODBUS_address    = Rx_ADU[6]
    Tx_MODBUS_function   = Rx_ADU[7] | 0b10000000
    Tx_Error_code        = 1
    Tx_ADU = struct.pack(">BBBBBBBBB",Tx_Transaction_ID_hi,Tx_Transaction_ID_lo,Tx_Protocol_ID_hi,Tx_Protocol_ID_lo,Tx_Message_length_hi,Tx_Message_length_lo,Tx_MODBUS_address,Tx_MODBUS_function,Tx_Error_code)
    return Tx_ADU

def MODBUS_TCP_SERVER_FUN_3(Rx_ADU):
    """Read holding registers"""
    len_rx = len(Rx_ADU)
    if (len_rx == 12): #CONST Len for uint16
        (Rx_Transaction_ID,Rx_Protocol_ID,Rx_Message_length,Rx_MODBUS_address,Rx_MODBUS_function,Rx_Register_address,Rx_Register_count) = struct.unpack(">HHHBBHH", Rx_ADU)
        if (Rx_Register_count <= 127): #limit size
            Tx_Transaction_ID =  Rx_Transaction_ID
            Tx_Protocol_ID =     Rx_Protocol_ID
            Tx_Message_length =  (Rx_Register_count * 2) + 3
            Tx_MODBUS_address =  Rx_MODBUS_address
            Tx_MODBUS_function = Rx_MODBUS_function
            Tx_Byte_count =      Rx_Register_count * 2  #1byte Rx_Register_count * 2
            Tx_ADU = struct.pack(">HHHBBB",Tx_Transaction_ID,Tx_Protocol_ID,Tx_Message_length,Tx_MODBUS_address,Tx_MODBUS_function,Tx_Byte_count)
            i_stop = Limit(In = Rx_Register_count, Max = 127, Min = 0)
            i = 0
            while (i != i_stop): #i=Rx_Register_count-1...0
                address = Rx_Register_address + i
                value = Read_register(Register_address = address)
                Tx_ADU = Tx_ADU + struct.pack(">H",value)
                i = i + 1
        else:
            print("ERROR FUN3")
            Tx_ADU = Error_function_not_supported(Rx_ADU)
    else:
        print("ERROR LEN FUN3")
        Tx_ADU = Error_function_not_supported(Rx_ADU)
    return Tx_ADU

def MODBUS_TCP_SERVER_FUN_16(Rx_ADU):
    """Write multiple holding registers"""
    len_rx = len(Rx_ADU)
    Rx_Message_length = Two_uint8_to_uint16(uint8_hi = Rx_ADU[4], uint8_lo = Rx_ADU[5])
    Rx_Register_count   = Two_uint8_to_uint16(uint8_hi = Rx_ADU[10], uint8_lo = Rx_ADU[11])
    Rx_Byte_count = Rx_ADU[12]
    if (Rx_Byte_count == Rx_Register_count*2) and (Rx_Message_length + 6 == len_rx): #Correct ADU
        Rx_Transaction_ID = Two_uint8_to_uint16(uint8_hi = Rx_ADU[0], uint8_lo = Rx_ADU[1])
        Rx_Protocol_ID    = Two_uint8_to_uint16(uint8_hi = Rx_ADU[2], uint8_lo = Rx_ADU[3])
        Rx_MODBUS_address  = Rx_ADU[6]
        Rx_MODBUS_function = Rx_ADU[7]
        Rx_Register_address = Two_uint8_to_uint16(uint8_hi = Rx_ADU[8], uint8_lo = Rx_ADU[9])
        Rx_Byte_count = Rx_ADU[12]
        Tx_Transaction_ID   = Rx_Transaction_ID
        Tx_Protocol_ID      = Rx_Protocol_ID
        Tx_Message_length   = 6
        Tx_MODBUS_address   = Rx_MODBUS_address
        Tx_MODBUS_function  = Rx_MODBUS_function
        Tx_Register_address = Rx_Register_address
        Tx_Register_count   = Rx_Register_count
        Tx_ADU = struct.pack(">HHHBBHH",Tx_Transaction_ID,Tx_Protocol_ID,Tx_Message_length,Tx_MODBUS_address,Tx_MODBUS_function,Tx_Register_address,Tx_Register_count)
        i_stop = Limit(In = Rx_Register_count, Max = 127, Min = 0)
        i = 0
        while (i != i_stop): #i=Rx_Register_count-1...0
            address = Rx_Register_address + i
            value   = Two_uint8_to_uint16(uint8_hi = Rx_ADU[13 + i * 2], uint8_lo = Rx_ADU[14 + i * 2])
            Write_register(Register_address = address, Register_value = value) 
            i = i + 1
    else:
        print("ERROR FUN16")
        Tx_ADU = Error_function_not_supported(Rx_ADU)
    return Tx_ADU

def PROTOCOL_MODBUS_TCP_SERVER(Rx_ADU):
    """Tx_ADU = MODBUS_TCP_SERVER_PROCESSING_ADU(Rx_ADU)"""
    Rx_MODBUS_address  = Rx_ADU[6]
    Rx_MODBUS_function = Rx_ADU[7]
    if (Rx_MODBUS_address == MODBUS_ADDRESS): #Check MODBUS ADR
        if  (Rx_MODBUS_function == 3):
            Tx_ADU = MODBUS_TCP_SERVER_FUN_3(Rx_ADU)
        elif(Rx_MODBUS_function == 16):
            Tx_ADU = MODBUS_TCP_SERVER_FUN_16(Rx_ADU)
        else:
            print("ERROR FUN NUMBER")
            Tx_ADU = Error_function_not_supported(Rx_ADU)
    else:
        print("ERROR MODBUS ADR")
        Tx_ADU = Error_function_not_supported(Rx_ADU)
    return Tx_ADU

def Task_MODBUS_TCP_SEREVER():
    CONNECTION_LIST = []    # list of socket clients
    RECV_BUFFER = 1024 #Byte recive byffer size
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((IP_ADDRESS, TCP_PORT))
    server_socket.listen(8) #Number of TCP clients
    CONNECTION_LIST.append(server_socket)
    print( "TCP server started")
    while True:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print( "Client online" , addr)
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    Rx_ADU = sock.recv(RECV_BUFFER)
                    #
                    Tx_ADU = PROTOCOL_MODBUS_TCP_SERVER(Rx_ADU)
                    if Rx_ADU:
                        sock.send(Tx_ADU)
                # client disconnected, so remove from socket list
                except:
                    #broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print( "Client offline", addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
    server_socket.close()
    return

if __name__ == "__main__":
    Debug_test_init_registers()
    Task_MODBUS_TCP_SEREVER()

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
# Date: 2014 - 2024
# License: GNU GPL-2.0-or-later
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# https://www.youtube.com/watch?v=n1F_MfLRlX0
#
# See also:
# https://www.youtube.com/@DIY_PLC
# https://github.com/DIYPLC/LIB_PLC
# https://oshwlab.com/diy.plc.314/PLC_HW1_SW1
# https://3dtoday.ru/3d-models/mechanical-parts/body/korpus-na-din-reiku
# https://t.me/DIY_PLC

# Спасибо за лекции.
# https://www.youtube.com/@unx7784/playlists
# https://www.youtube.com/@tkhirianov/playlists
