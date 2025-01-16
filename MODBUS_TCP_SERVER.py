#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
MODBUS TCP SERVER
Learn more at: http://www.modbus.org/
http://www.binarytides.com/python-socket-server-code-example/
"""

import socket  # FOR TCP SERVER
import select  # FOR TCP SERVER
import struct  # FOR MODBUS PROTOCOL
import array  # FOR MODBUS PROTOCOL

ip_address = "0.0.0.0"
tcp_port = 502
modbus_address = 1
Register = array.array('H', [0] * 65536)  # holding Register


def debug_test_init_registers() -> None:
    """Test init registers value"""
    for i in range(65536):  # i = 0...65536-1
        Register[i] = i
    return


def limit(in1: int = 0, maximum: int = 65535, minimum: int = 0) -> int:
    """ Limit to a safe value """
    _in = int(in1)
    _out = int(0)
    if _in >= maximum:
        _out = maximum
    else:
        if _in <= minimum:
            _out = minimum
        else:
            _out = _in
    return _out


def read_register(register_address=0):
    """ Safe reading from an array """
    address = limit(in1=register_address, maximum=65535, minimum=0)
    return Register[address]


def write_register(register_address=0, register_value=0):
    """ Safe writing to an array """
    address = limit(in1=register_address, maximum=65535, minimum=0)
    value = limit(in1=register_value, maximum=65535, minimum=0)
    Register[address] = value
    return


def two_uint8_to_uint16(uint8_hi=0, uint8_lo=0):
    _uint8_hi = (int(uint8_hi) & 0xFF) << 8
    _uint8_lo = int(uint8_lo) & 0xFF
    _res = (_uint8_hi | _uint8_lo) & 0xFFFF
    return _res


def error_function_not_supported(rx_adu):
    """ Error function not supported """
    tx_transaction_id_hi = rx_adu[0]
    tx_transaction_id_lo = rx_adu[1]
    tx_protocol_id_hi = rx_adu[2]
    tx_protocol_id_lo = rx_adu[3]
    tx_message_length_hi = 0
    tx_message_length_lo = 3
    tx_modbus_address = rx_adu[6]
    tx_modbus_function = rx_adu[7] | 0b10000000
    tx_error_code = 1
    tx_adu = struct.pack(">BBBBBBBBB", tx_transaction_id_hi, tx_transaction_id_lo, tx_protocol_id_hi, tx_protocol_id_lo,
                         tx_message_length_hi, tx_message_length_lo, tx_modbus_address, tx_modbus_function,
                         tx_error_code)
    return tx_adu


def modbus_tcp_server_fun_3(rx_adu):
    """ Read holding registers """
    len_rx = len(rx_adu)
    if len_rx == 12:  # CONST Len for uint16
        (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function,
         rx_register_address, rx_register_count) = struct.unpack(">HHHBBHH", rx_adu)
        if rx_register_count <= 127:  #limit size
            tx_transaction_id = rx_transaction_id
            tx_protocol_id = rx_protocol_id
            tx_message_length = (rx_register_count * 2) + 3
            tx_modbus_address = rx_modbus_address
            tx_modbus_function = rx_modbus_function
            tx_byte_count = rx_register_count * 2  #1byte rx_register_count * 2
            tx_adu = struct.pack(">HHHBBB", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                                 tx_modbus_function, tx_byte_count)
            i_stop = limit(in1=rx_register_count, maximum=127, minimum=0)
            i = 0
            while i != i_stop:  # i=rx_register_count-1...0
                address = rx_register_address + i
                value = read_register(register_address=address)
                tx_adu = tx_adu + struct.pack(">H", value)
                i = i + 1
        else:
            print("ERROR FUN3")
            tx_adu = error_function_not_supported(rx_adu)
    else:
        print("ERROR LEN FUN3")
        tx_adu = error_function_not_supported(rx_adu)
    return tx_adu


def modbus_tcp_server_fun_16(rx_adu):
    """ Write multiple holding registers """
    len_rx = len(rx_adu)
    rx_message_length = two_uint8_to_uint16(uint8_hi=rx_adu[4], uint8_lo=rx_adu[5])
    rx_register_count = two_uint8_to_uint16(uint8_hi=rx_adu[10], uint8_lo=rx_adu[11])
    rx_byte_count = rx_adu[12]
    if (rx_byte_count == rx_register_count * 2) and (rx_message_length + 6 == len_rx):  #Correct ADU
        rx_transaction_id = two_uint8_to_uint16(uint8_hi=rx_adu[0], uint8_lo=rx_adu[1])
        rx_protocol_id = two_uint8_to_uint16(uint8_hi=rx_adu[2], uint8_lo=rx_adu[3])
        rx_modbus_address = rx_adu[6]
        rx_modbus_function = rx_adu[7]
        rx_register_address = two_uint8_to_uint16(uint8_hi=rx_adu[8], uint8_lo=rx_adu[9])
        rx_byte_count = rx_adu[12]
        tx_transaction_id = rx_transaction_id
        tx_protocol_id = rx_protocol_id
        tx_message_length = 6
        tx_modbus_address = rx_modbus_address
        tx_modbus_function = rx_modbus_function
        tx_register_address = rx_register_address
        tx_register_count = rx_register_count
        tx_adu = struct.pack(">HHHBBHH", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                             tx_modbus_function, tx_register_address, tx_register_count)
        i_stop = limit(in1=rx_register_count, maximum=127, minimum=0)
        i = 0
        while i != i_stop:  # i=rx_register_count-1...0
            address = rx_register_address + i
            value = two_uint8_to_uint16(uint8_hi=rx_adu[13 + i * 2], uint8_lo=rx_adu[14 + i * 2])
            write_register(register_address=address, register_value=value)
            i = i + 1
    else:
        print("ERROR FUN16")
        tx_adu = error_function_not_supported(rx_adu)
    return tx_adu


def protocol_modbus_tcp_server(rx_adu):
    """ tx_adu = protocol_modbus_tcp_server(rx_adu) """
    rx_modbus_address = rx_adu[6]
    rx_modbus_function = rx_adu[7]
    if rx_modbus_address == modbus_address:  #Check MODBUS ADR
        if rx_modbus_function == 3:
            tx_adu = modbus_tcp_server_fun_3(rx_adu)
        elif rx_modbus_function == 16:
            tx_adu = modbus_tcp_server_fun_16(rx_adu)
        else:
            print("ERROR FUN NUMBER")
            tx_adu = error_function_not_supported(rx_adu)
    else:
        print("ERROR MODBUS ADR")
        tx_adu = error_function_not_supported(rx_adu)
    return tx_adu


def task_modbus_tcp_server():
    connection_list = []  # list of socket clients
    recv_buffer = 1024  # Byte receive buffer size
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ip_address, tcp_port))
    server_socket.listen(8)  # Number of TCP clients
    connection_list.append(server_socket)
    print("TCP server started")
    while True:
        # Get the list sockets which are ready to be read through select
        read_sockets, write_sockets, error_sockets = select.select(connection_list, [], [])
        for sock in read_sockets:
            # New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                connection_list.append(sockfd)
                print("Client online", addr)
            # Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    # In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    rx_adu = sock.recv(recv_buffer)
                    #
                    tx_adu = protocol_modbus_tcp_server(rx_adu)
                    if rx_adu:
                        sock.send(tx_adu)
                # client disconnected, so remove from socket list
                except BaseException:
                    #broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print("Client offline", addr)
                    sock.close()
                    connection_list.remove(sock)
                    continue
    server_socket.close()
    return


if __name__ == "__main__":
    #debug_test_init_registers()
    task_modbus_tcp_server()

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

