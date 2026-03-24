#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
MODBUS UDP SERVER
Learn more at: http://www.modbus.org/
https://pyhub.ru/python-advanced/lecture-11-73-1034/
"""

import socket  # FOR UDP SERVER
import struct  # FOR MODBUS PROTOCOL
import array  # FOR MODBUS PROTOCOL

Register = array.array('H', [0] * 65536)  # holding Register


def modbus_limit(in1: int = 0, maximum: int = 65535, minimum: int = 0) -> int:
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


def modbus_read_register(register_address=0) -> int:
    """ Safe reading from an array """
    address = modbus_limit(in1=register_address, maximum=65535, minimum=0)
    return int(Register[address])


def modbus_write_register(register_address=0, register_value=0):
    """ Safe writing to an array """
    address = modbus_limit(in1=register_address, maximum=65535, minimum=0)
    value = modbus_limit(in1=register_value, maximum=65535, minimum=0)
    Register[address] = value
    return


def modbus_two_uint8_to_uint16(uint8_hi=0, uint8_lo=0) -> int:
    _uint8_hi = (int(uint8_hi) & 0xFF) << 8
    _uint8_lo = int(uint8_lo) & 0xFF
    _res = (_uint8_hi | _uint8_lo) & 0xFFFF
    return int(_res)


def modbus_server_fun_not_supported(rx_adu=b'') -> bytes:
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
    tx_adu = struct.pack(">BBBBBBBBB", tx_transaction_id_hi, tx_transaction_id_lo, tx_protocol_id_hi,
                         tx_protocol_id_lo, tx_message_length_hi, tx_message_length_lo, tx_modbus_address,
                         tx_modbus_function, tx_error_code)
    return tx_adu


def modbus_server_fun_3(rx_adu=b'') -> bytes:
    """ Read holding registers """
    len_rx = len(rx_adu)
    if len_rx == 12:  # CONST Len for uint16
        (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function,
         rx_register_address, rx_register_count) = struct.unpack(">HHHBBHH", rx_adu)
        if rx_register_count <= 127:  # limit size
            tx_transaction_id = rx_transaction_id
            tx_protocol_id = rx_protocol_id
            tx_message_length = (rx_register_count * 2) + 3
            tx_modbus_address = rx_modbus_address
            tx_modbus_function = rx_modbus_function
            tx_byte_count = rx_register_count * 2  # 1byte rx_register_count * 2
            tx_adu = struct.pack(">HHHBBB", tx_transaction_id, tx_protocol_id, tx_message_length,
                                 tx_modbus_address, tx_modbus_function, tx_byte_count)
            i_stop = modbus_limit(in1=rx_register_count, maximum=127, minimum=0)
            i = 0
            while i != i_stop:  # i=rx_register_count-1...0
                address = rx_register_address + i
                value = modbus_read_register(register_address=address)
                tx_adu = tx_adu + struct.pack(">H", value)
                i = i + 1
        else:
            print("[ERROR] FUN3")
            tx_adu = modbus_server_fun_not_supported(rx_adu)
    else:
        print("[ERROR] LEN FUN3")
        tx_adu = modbus_server_fun_not_supported(rx_adu)
    return tx_adu


def modbus_server_fun_16(rx_adu=b'') -> bytes:
    """ Write multiple holding registers """
    len_rx = len(rx_adu)
    rx_message_length = modbus_two_uint8_to_uint16(uint8_hi=rx_adu[4], uint8_lo=rx_adu[5])
    rx_register_count = modbus_two_uint8_to_uint16(uint8_hi=rx_adu[10], uint8_lo=rx_adu[11])
    rx_byte_count = rx_adu[12]
    if (rx_byte_count == rx_register_count * 2) and (rx_message_length + 6 == len_rx):  # Correct ADU
        rx_transaction_id = modbus_two_uint8_to_uint16(uint8_hi=rx_adu[0], uint8_lo=rx_adu[1])
        rx_protocol_id = modbus_two_uint8_to_uint16(uint8_hi=rx_adu[2], uint8_lo=rx_adu[3])
        rx_modbus_address = rx_adu[6]
        rx_modbus_function = rx_adu[7]
        rx_register_address = modbus_two_uint8_to_uint16(uint8_hi=rx_adu[8], uint8_lo=rx_adu[9])
        rx_byte_count = rx_adu[12]
        tx_transaction_id = rx_transaction_id
        tx_protocol_id = rx_protocol_id
        tx_message_length = 6
        tx_modbus_address = rx_modbus_address
        tx_modbus_function = rx_modbus_function
        tx_register_address = rx_register_address
        tx_register_count = rx_register_count
        tx_adu = struct.pack(">HHHBBHH", tx_transaction_id, tx_protocol_id, tx_message_length,
                             tx_modbus_address, tx_modbus_function, tx_register_address, tx_register_count)
        i_stop = modbus_limit(in1=rx_register_count, maximum=127, minimum=0)
        i = 0
        while i != i_stop:  # i=rx_register_count-1...0
            address = rx_register_address + i
            value = modbus_two_uint8_to_uint16(uint8_hi=rx_adu[13 + i * 2], uint8_lo=rx_adu[14 + i * 2])
            modbus_write_register(register_address=address, register_value=value)
            i = i + 1
    else:
        print("[ERROR] FUN16")
        tx_adu = modbus_server_fun_not_supported(rx_adu)
    return tx_adu


def modbus_server_protocol(rx_adu=b'', modbus_address=1) -> bytes:
    """ tx_adu = modbus_server_protocol(rx_adu) """
    rx_modbus_address = rx_adu[6]
    rx_modbus_function = rx_adu[7]
    if rx_modbus_address == modbus_address:  # Check MODBUS ADR
        if rx_modbus_function == 3:
            tx_adu = modbus_server_fun_3(rx_adu)
        elif rx_modbus_function == 16:
            tx_adu = modbus_server_fun_16(rx_adu)
        else:
            print("[ERROR] MODBUS FUN NUMBER")
            tx_adu = modbus_server_fun_not_supported(rx_adu)
    else:
        print("[ERROR] MODBUS ADR")
        tx_adu = modbus_server_fun_not_supported(rx_adu)
    return tx_adu


def modbus_udp_server_start(ip_address="0.0.0.0", udp_port=502, modbus_address=1):
    # https://pyhub.ru/python-advanced/lecture-11-73-1034/
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.bind((ip_address, udp_port))
            print("[OK] MODBUS UDP SERVER START:", (ip_address, udp_port))
            buffer_size = 1024
            while True:
                rx_msg, address = server_socket.recvfrom(buffer_size)
                print("[OK] rx:", address, rx_msg)
                tx_msg = modbus_server_protocol(rx_msg, modbus_address)
                server_socket.sendto(tx_msg, address)
                print("[OK] tx:", address, tx_msg)
    except BaseException as er_task_modbus_udp_server:
        print("[ERROR] task_modbus_udp_server()", er_task_modbus_udp_server)
    return


if __name__ == "__main__":
    modbus_udp_server_start()

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
