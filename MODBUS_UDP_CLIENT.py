#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import struct


def modbus_udp_client_read_holding_register_uint16(ip_address='127.0.0.1', upd_port=502,
                                                   modbus_address=1, register_address=0) -> int:
    """ MODBUS UDP MASTER READ REGISTER FROM PLC """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            timeout_seconds = 1.0
            client_socket.settimeout(timeout_seconds)
            tx_transaction_id = 1
            tx_protocol_id = 0
            tx_message_length = 6
            tx_modbus_address = modbus_address
            tx_modbus_function = 3
            tx_register_address = register_address
            tx_register_count = 1
            tx_adu = struct.pack(">HHHBBHH", tx_transaction_id, tx_protocol_id, tx_message_length,
                                 tx_modbus_address, tx_modbus_function, tx_register_address, tx_register_count)
            client_socket.sendto(tx_adu, (ip_address, upd_port))
            buffer_size = 1024
            rx_adu, address = client_socket.recvfrom(buffer_size)
            (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function,
             rx_byte_count, rx_register_value) = struct.unpack(">HHHBBBH", rx_adu)
        return rx_register_value
    except BaseException as er_modbus_udp_client_read_holding_register_uint16:
        print("[ERROR] modbus_udp_client_read_holding_register_uint16()",
              er_modbus_udp_client_read_holding_register_uint16)
        return 0


def modbus_udp_client_write_multiple_holding_register_uint16(ip_address='127.0.0.1', upd_port=502, modbus_address=1,
                                                             register_address=0, register_value=0):
    """ MODBUS UDP MASTER WRITE REGISTER TO PLC """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            timeout_seconds = 1.0
            client_socket.settimeout(timeout_seconds)
            tx_transaction_id = 0
            tx_protocol_id = 0
            tx_message_length = 9
            tx_modbus_address = modbus_address
            tx_modbus_function = 16  # Write multiple holding registers
            tx_register_address = int(register_address) & 0xFFFF  # Limit address
            tx_register_count = 1
            tx_byte_count = 2
            tx_register_value = int(register_value) & 0xFFFF  # Limit value
            tx_adu = struct.pack(">HHHBBHHBH", tx_transaction_id, tx_protocol_id, tx_message_length,
                                 tx_modbus_address, tx_modbus_function, tx_register_address, tx_register_count,
                                 tx_byte_count, tx_register_value)
            client_socket.sendto(tx_adu, (ip_address, upd_port))
            buffer_size = 1024
            rx_adu, address = client_socket.recvfrom(buffer_size)
            (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function,
             rx_register_address, rx_register_count) = struct.unpack(">HHHBBHH", rx_adu)
            return
    except BaseException as er_modbus_udp_client_write_multiple_holding_register_uint16:
        print("[ERROR] modbus_udp_client_write_multiple_holding_register_uint16()",
              er_modbus_udp_client_write_multiple_holding_register_uint16)
    return


def __unit_test__():
    print("[OK] TEST 1")
    print("[OK] modbus_udp_client_write_multiple_holding_register_uint16()")
    mw0 = 777
    modbus_udp_client_write_multiple_holding_register_uint16(register_address=0, register_value=mw0)
    print("[OK] send mw0 = ", mw0)
    print("[OK] modbus_udp_client_read_holding_register_uint16()")
    mw0 = modbus_udp_client_read_holding_register_uint16(register_address=0)
    print("[OK] receive mw0 = ", mw0)
    input("press any key for exit...")
    return


if __name__ == "__main__":
    __unit_test__()

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
