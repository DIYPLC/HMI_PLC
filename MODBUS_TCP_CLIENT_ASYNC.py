#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Simple Modbus TCP Master
Modbus Master == TCP Client
Modbus function 3  read holding registers uint16
Modbus function 16 write multiple holding registers uint16
Learn more at: http://www.modbus.org/
# https://docs-python.ru/standart-library/modul-asyncio-python/potoki-stream-modulja-asyncio/
# https://habr.com/ru/companies/wunderfund/articles/715126/
"""

import struct
import asyncio


async def modbus_tcp_client_read_holding_register_uint16_async(ip_address='127.0.0.1', tcp_port=502, modbus_address=1,
                                                               register_address=0) -> int:
    try:
        reader, writer = await asyncio.open_connection(ip_address, tcp_port)
        tx_transaction_id = 1
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address
        tx_modbus_function = 3
        tx_register_address = register_address
        tx_register_count = 1
        tx_adu = struct.pack(">HHHBBHH", tx_transaction_id, tx_protocol_id, tx_message_length,
                             tx_modbus_address, tx_modbus_function, tx_register_address, tx_register_count)
        writer.write(tx_adu)  # Запись байтового представления данных
        await writer.drain()  # Ожидание завершения передачи данных
        rx_adu = await reader.read(n=128)  # Стение байтового представления данных
        (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function, rx_byte_count,
         rx_register_value) = struct.unpack(">HHHBBBH", rx_adu)
        writer.close()  # Закрытие сокета
        await writer.wait_closed()  # Ожидание закрытия сокета
        return rx_register_value
    except BaseException as er1:
        print(er1)
        return


async def modbus_tcp_client_write_multiple_holding_register_uint16_async(ip_address='127.0.0.1', tcp_port=502,
                                                                         modbus_address=1, register_address=0,
                                                                         register_value=0) -> None:
    try:
        reader, writer = await asyncio.open_connection(ip_address, tcp_port)
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
        writer.write(tx_adu)  # Запись байтового представления данных
        await writer.drain()  # Ожидание завершения передачи данных
        rx_adu = await reader.read(n=128)  # Чтение байтового представления данных
        (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function,
         rx_register_address, rx_register_count) = struct.unpack(">HHHBBHH", rx_adu)
        writer.close()  # Закрытие сокета
        await writer.wait_closed()  # Ожидание закрытия сокета
        return
    except BaseException as er2:
        print(er2)
        return


def _unit_test_() -> None:
    print("TEST 1")
    print("modbus_tcp_client_write_multiple_holding_register_uint16()")
    mw0 = 333
    asyncio.run(modbus_tcp_client_write_multiple_holding_register_uint16_async(ip_address='127.0.0.1',
                                                                               tcp_port=502,
                                                                               modbus_address=1,
                                                                               register_address=0,
                                                                               register_value=mw0))
    print("send mw0 = ", mw0)
    print("modbus_tcp_client_read_holding_register_uint16()")
    mw0 = asyncio.run(modbus_tcp_client_read_holding_register_uint16_async(ip_address='127.0.0.1', register_address=0))
    print("receive mw0 = ", mw0)
    input("press any key for exit...")


if __name__ == "__main__":
    _unit_test_()

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
