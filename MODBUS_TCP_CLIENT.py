#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Simple Modbus TCP Master
Modbus Master == TCP Client
Modbus function 3  read holding registers uint16
Modbus function 16 write multiple holding registers uint16
Modbus function 6  write single register
Modbus function 4  read one input register
Learn more at: http://www.modbus.org/
"""

import socket
import struct
import array


def modbus_tcp_client_read_holding_register_uint16(ip_address='127.0.0.1', tcp_port=502, modbus_address=1,
                                                   register_address=0) -> int:
    """MODBUS TCP MASTER READ REGISTER FROM PLC"""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_address, tcp_port))
        tx_transaction_id = 1
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address
        tx_modbus_function = 3
        tx_register_address = register_address
        tx_register_count = 1
        tx_adu = struct.pack(">HHHBBHH", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                             tx_modbus_function, tx_register_address, tx_register_count)
        client_socket.send(tx_adu)
        rx_adu = client_socket.recv(1500)
        (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function, rx_byte_count,
         rx_register_value) = struct.unpack(">HHHBBBH", rx_adu)
        client_socket.close()
        client_socket.__del__()
        return rx_register_value
    except BaseException:
        print("ERROR: MODBUS_TCP_client_read_holding_register_uint16()")
        client_socket.close()
        client_socket.__del__()
        return 0


def modbus_tcp_client_write_multiple_holding_register_uint16(ip_address='127.0.0.1', tcp_port=502, modbus_address=1,
                                                             register_address=0, register_value=0) -> None:
    """MODBUS TCP MASTER WRITE REGISTER TO PLC"""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_address, tcp_port))
        tx_transaction_id = 0
        tx_protocol_id = 0
        tx_message_length = 9
        tx_modbus_address = modbus_address
        tx_modbus_function = 16  #Write multiple holding registers
        tx_register_address = int(register_address) & 0xFFFF  #Limit address
        tx_register_count = 1
        tx_byte_count = 2
        tx_register_value = int(register_value) & 0xFFFF  #Limit value
        tx_adu = struct.pack(">HHHBBHHBH", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                             tx_modbus_function, tx_register_address, tx_register_count, tx_byte_count,
                             tx_register_value)
        client_socket.send(tx_adu)
        rx_adu = client_socket.recv(1500)
        (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function,
         rx_register_address, rx_register_count) = struct.unpack(">HHHBBHH", rx_adu)
        client_socket.close()
        client_socket.__del__()
        return
    except BaseException:
        print("ERROR: MODBUS_TCP_client_write_multiple_holding_register_uint16()")
        client_socket.close()
        client_socket.__del__()
    return


def modbus_tcp_client_read_input_register_int16(ip_address='127.0.0.1', tcp_port=502, modbus_address=1,
                                                register_address=0) -> int:
    """MODBUS TCP MASTER READ REGISTER FROM PLC"""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_address, tcp_port))
        tx_transaction_id = 1
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address
        tx_modbus_function = 4  #read_input_register
        tx_register_address = register_address
        tx_register_count = 1
        tx_adu = struct.pack(">HHHBBHH", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                             tx_modbus_function, tx_register_address, tx_register_count)
        client_socket.send(tx_adu)
        rx_adu = client_socket.recv(1500)
        (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function, rx_byte_count,
         rx_register_value) = struct.unpack(">HHHBBBh", rx_adu)
        client_socket.close()
        client_socket.__del__()
        return rx_register_value
    except BaseException:
        print("ERROR: MODBUS_TCP_client_read_input_register_uint16()")
        client_socket.close()
        client_socket.__del__()
        return 0


def modbus_tcp_client_read_input_register_uint16(ip_address='127.0.0.1', tcp_port=502, modbus_address=1,
                                                 register_address=0) -> int:
    """MODBUS TCP MASTER READ REGISTER FROM PLC"""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_address, tcp_port))
        tx_transaction_id = 1
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address
        tx_modbus_function = 4  #read_input_register
        tx_register_address = register_address
        tx_register_count = 1
        tx_adu = struct.pack(">HHHBBHH", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                             tx_modbus_function, tx_register_address, tx_register_count)
        client_socket.send(tx_adu)
        rx_adu = client_socket.recv(1500)
        (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function, rx_byte_count,
         rx_register_value) = struct.unpack(">HHHBBBH", rx_adu)
        client_socket.close()
        client_socket.__del__()
        return rx_register_value
    except BaseException:
        print("ERROR: MODBUS_TCP_client_read_input_register_uint16()")
        client_socket.close()
        client_socket.__del__()
        return 0


class ModbusTcpMaster(object):

    def __init__(self) -> None:
        self.MW = array.array('H', [0] * 65536)  #MW[0]...MW[65535] uint16
        self.Transaction_counter = 0
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return

    def start_tcp_client(self, ip_address='127.0.0.1', tcp_port=502) -> None:
        self.client_socket.connect((ip_address, tcp_port))
        return

    def __del__(self) -> None:
        self.client_socket.close()
        self.client_socket.__del__()  # TODO
        del self  # TODO
        return

    def get_mw(self, mw_address) -> int:
        return self.MW[(mw_address & 0xFFFF)]

    def set_mw(self, mw_address, mw_value) -> None:
        self.MW[(mw_address & 0xFFFF)] = mw_value & 0xFFFF
        return

    def read_holding_register_uint16(self, modbus_address=1, register_address=0) -> int:
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        tx_transaction_id = self.Transaction_counter
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address
        tx_modbus_function = 3  #Read holding registers
        tx_register_address = register_address
        tx_register_count = 1
        tx_adu = struct.pack(">HHHBBHH",
                             tx_transaction_id,
                             tx_protocol_id,
                             tx_message_length,
                             tx_modbus_address,
                             tx_modbus_function,
                             tx_register_address,
                             tx_register_count)
        self.client_socket.send(tx_adu)
        rx_adu = self.client_socket.recv(1500)  #1500 = Ethernet MTU size
        error = (len(rx_adu) != 11)  #11 byte OK
        if not error:
            (rx_transaction_id,
             rx_protocol_id,
             rx_message_length,
             rx_modbus_address,
             rx_modbus_function,
             rx_byte_count,
             rx_register_value) = struct.unpack(">HHHBBBH", rx_adu)
            error = error or (rx_transaction_id != tx_transaction_id)
            error = error or (rx_protocol_id != tx_protocol_id)
            error = error or (rx_message_length != tx_register_count * 2 + 3)
            error = error or (rx_modbus_address != tx_modbus_address)
            error = error or (rx_modbus_function != tx_modbus_function)
            error = error or (rx_byte_count != tx_register_count * 2)
            if not error:
                register_value = rx_register_value
            else:
                print("error read holding register")
                print(tx_adu)
                print(rx_adu)
                register_value = 0
        else:
            print("error read holding register")
            print(tx_adu)
            print(rx_adu)
            register_value = 0
        return register_value

    def read_holding_register_float32(self, modbus_address=1, register_address=0) -> float:
        """use Register_address and Register_address + 1"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        tx_transaction_id = self.Transaction_counter
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address
        tx_modbus_function = 3  #Read holding registers
        tx_register_address = register_address
        tx_register_count = 2
        tx_adu = struct.pack(">HHHBBHH",
                             tx_transaction_id,
                             tx_protocol_id,
                             tx_message_length,
                             tx_modbus_address,
                             tx_modbus_function,
                             tx_register_address,
                             tx_register_count)
        self.client_socket.send(tx_adu)
        rx_adu = self.client_socket.recv(1500)  #1500 = Ethernet MTU size
        error = (len(rx_adu) != 13)  #13 byte OK
        if not error:
            (rx_transaction_id,
             rx_protocol_id,
             rx_message_length,
             rx_modbus_address,
             rx_modbus_function,
             rx_byte_count,
             rx_register_value1,
             rx_register_value2) = struct.unpack(">HHHBBBHH", rx_adu)
            error = error or (rx_transaction_id != tx_transaction_id)
            error = error or (rx_protocol_id != tx_protocol_id)
            error = error or (rx_message_length != tx_register_count * 2 + 3)
            error = error or (rx_modbus_address != tx_modbus_address)
            error = error or (rx_modbus_function != tx_modbus_function)
            error = error or (rx_byte_count != tx_register_count * 2)
            if not error:
                decode_float32 = struct.unpack(">f", struct.pack(">HH", rx_register_value2, rx_register_value1))
                register_value = decode_float32[0]
            else:
                print("error read holding register")
                print(tx_adu)
                print(rx_adu)
                register_value = 0.0
        else:
            print("error read holding register")
            print(tx_adu)
            print(rx_adu)
            register_value = 0.0
        return register_value

    def write_multiple_holding_register_uint16(self, modbus_address=1, register_address=0, register_value=0) -> bool:
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        tx_transaction_id = self.Transaction_counter
        tx_protocol_id = 0
        tx_message_length = 9
        tx_modbus_address = modbus_address
        tx_modbus_function = 16  #Write multiple holding registers
        tx_register_address = register_address
        tx_register_count = 1
        tx_byte_count = 2
        tx_register_value = register_value
        tx_adu = struct.pack(">HHHBBHHBH",
                             tx_transaction_id,
                             tx_protocol_id,
                             tx_message_length,
                             tx_modbus_address,
                             tx_modbus_function,
                             tx_register_address,
                             tx_register_count,
                             tx_byte_count,
                             tx_register_value)
        self.client_socket.send(tx_adu)
        rx_adu = self.client_socket.recv(1500)  #1500 Ethernet MTU size
        error = (len(rx_adu) != 12)  #12 byte OK
        if not error:
            (rx_transaction_id,
             rx_protocol_id,
             rx_message_length,
             rx_modbus_address,
             rx_modbus_function,
             rx_register_address,
             rx_register_count) = struct.unpack(">HHHBBHH", rx_adu)
            error = error or (rx_transaction_id != tx_transaction_id)
            error = error or (rx_protocol_id != tx_protocol_id)
            error = error or (rx_message_length != 6)
            error = error or (rx_modbus_address != tx_modbus_address)
            error = error or (rx_modbus_function != tx_modbus_function)
            error = error or (rx_register_count != tx_register_count)
            if error:
                print("error write multiple holding register")
                print(tx_adu)
                print(rx_adu)
        else:
            print("error write multiple holding register")
            print(tx_adu)
            print(rx_adu)
            error = True
        return error

    def write_multiple_holding_register_float32(self, modbus_address=1, register_address=0, register_value=0.0) -> bool:
        """use Register_address and Register_address + 1"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        tx_transaction_id = self.Transaction_counter
        tx_protocol_id = 0
        tx_message_length = 11
        tx_modbus_address = modbus_address
        tx_modbus_function = 16  #Write multiple holding registers
        tx_register_address = register_address
        tx_register_count = 2
        tx_byte_count = 4
        tx_register_value = register_value
        (tx_register_value2, tx_register_value1) = struct.unpack(">HH", struct.pack(">f", register_value))
        tx_adu = struct.pack(">HHHBBHHBHH",
                             tx_transaction_id,
                             tx_protocol_id,
                             tx_message_length,
                             tx_modbus_address,
                             tx_modbus_function,
                             tx_register_address,
                             tx_register_count,
                             tx_byte_count,
                             tx_register_value1,
                             tx_register_value2)
        self.client_socket.send(tx_adu)
        rx_adu = self.client_socket.recv(1500)  #1500 Ethernet MTU size
        error = (len(rx_adu) != 12)  #12 byte OK
        if not error:
            (rx_transaction_id,
             rx_protocol_id,
             rx_message_length,
             rx_modbus_address,
             rx_modbus_function,
             rx_register_address,
             rx_register_count) = struct.unpack(">HHHBBHH", rx_adu)
            error = error or (rx_transaction_id != tx_transaction_id)
            error = error or (rx_protocol_id != tx_protocol_id)
            error = error or (rx_message_length != 6)
            error = error or (rx_modbus_address != tx_modbus_address)
            error = error or (rx_modbus_function != tx_modbus_function)
            error = error or (rx_register_count != tx_register_count)
            if error:
                print("error write multiple holding register")
                print(tx_adu)
                print(rx_adu)
        else:
            print("error write multiple holding register")
            print(tx_adu)
            print(rx_adu)
            error = True
        return error

    def write_single_register(self, modbus_address=1, register_address=0, register_value=0) -> bool:
        """uint16 Register_value"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        tx_transaction_id = self.Transaction_counter
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address
        tx_modbus_function = 6  #write_single_register
        tx_register_address = register_address
        tx_register_value = register_value
        tx_mbap = struct.pack(">HHHB", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address)
        tx_pdu = struct.pack(">BHH", tx_modbus_function, tx_register_address, tx_register_value)
        tx_adu = tx_mbap + tx_pdu
        self.client_socket.send(tx_adu)
        rx_adu = self.client_socket.recv(1500)  #1500 Ethernet MTU size
        error = (len(rx_adu) != 12)  #12 byte OK
        if not error:
            error = (rx_adu != tx_adu)
            if error:
                print("error write single register")
                print(tx_adu)
                print(rx_adu)
        else:
            print("error write single register")
            print(tx_adu)
            print(rx_adu)
            error = True
        return error

    def read_holding_registers(self, modbus_address=1, register_address=0, register_count=1) -> None:
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        tx_transaction_id = self.Transaction_counter
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address & 0xFF
        tx_modbus_function = 3  #Read holding registers
        tx_register_address = int(register_address) & 0xFFFF
        tx_register_count = int(register_count) & 0xFF  #1...127 Maximum
        tx_mbap = struct.pack(">HHHB", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address)
        tx_pdu = struct.pack(">BHH", tx_modbus_function, tx_register_address, tx_register_count)
        tx_adu = tx_mbap + tx_pdu
        self.client_socket.send(tx_adu)
        rx_adu = self.client_socket.recv(1500)  #1500 Ethernet MTU size
        error = (len(rx_adu) != register_count * 2 + 9)  #Check len ADU
        if not error:
            rx_transaction_id = int((rx_adu[0] << 8) | rx_adu[1]) & 0xFFFF
            rx_protocol_id = int((rx_adu[2] << 8) | rx_adu[3]) & 0xFFFF
            rx_message_length = int((rx_adu[4] << 8) | rx_adu[5]) & 0xFFFF
            rx_modbus_address = int(rx_adu[6]) & 0xFF
            rx_modbus_function = int(rx_adu[7]) & 0xFF
            rx_byte_count = int(rx_adu[8]) & 0xFF
            error = error or (rx_transaction_id != tx_transaction_id)
            error = error or (rx_protocol_id != tx_protocol_id)
            error = error or (rx_message_length != tx_register_count * 2 + 3)
            error = error or (rx_modbus_address != tx_modbus_address)
            error = error or (rx_modbus_function != tx_modbus_function)
            error = error or (rx_byte_count != tx_register_count * 2)
            if not error:
                for Counter in range(tx_register_count):  #Counter = 0...Register_count
                    hi_byte = int(rx_adu[9 + Counter * 2]) & 0xFF
                    lo_byte = int(rx_adu[10 + Counter * 2]) & 0xFF
                    register_value = int((hi_byte << 8) | lo_byte) & 0xFFFF
                    reg_adr = int(Counter + register_address) & 0xFFFF
                    self.MW[reg_adr] = register_value
            else:
                print("error read holding register")
        else:
            print("error read holding register")
        return


def two_uint16_to_float32(register_value1: int = 0, register_value2: int = 0) -> float:
    tmp = struct.unpack(">f", struct.pack(">HH", register_value2, register_value1))
    return float(tmp[0])


def _unit_test_() -> None:
    print("TEST 1")
    print("modbus_tcp_client_write_multiple_holding_register_uint16()")
    mw0 = 333
    modbus_tcp_client_write_multiple_holding_register_uint16(ip_address='127.0.0.1', tcp_port=502, modbus_address=1,
                                                             register_address=0, register_value=mw0)
    print("send mw0 = ", mw0)
    print("modbus_tcp_client_read_holding_register_uint16()")
    mw0 = modbus_tcp_client_read_holding_register_uint16(ip_address='127.0.0.1', tcp_port=502, modbus_address=1,
                                                         register_address=0)
    print("receive mw0 = ", mw0)
    print("TEST 2")
    print("TODO modbus_tcp_client_read_input_register_int16()")  # TODO
    print("TODO modbus_tcp_client_read_input_register_uint16()")  # TODO
    print("TODO ModbusTcpMaster.write_single_register()")  # TODO
    plc1 = ModbusTcpMaster()
    plc1.start_tcp_client(ip_address='127.0.0.1')
    print("TEST 3")
    mw1 = 777
    print("ModbusTcpMaster.write_multiple_holding_register_uint16()")
    plc1.write_multiple_holding_register_uint16(register_address=1, register_value=mw1)
    print("send mw1 =", mw1)
    print("ModbusTcpMaster.read_holding_register_uint16()")
    mw1 = plc1.read_holding_register_uint16(register_address=1)
    print("receive mw1 =", mw1)
    print("TEST 4")
    mw2mw3 = -555.0
    print("ModbusTcpMaster.write_multiple_holding_register_float32()")
    plc1.write_multiple_holding_register_float32(register_address=2, register_value=mw2mw3)
    print("send mw2mw3 =", mw2mw3)
    print("ModbusTcpMaster.read_holding_register_float32()")
    mw2mw3 = plc1.read_holding_register_float32(register_address=2)
    print("receive mw2mw3 =", mw2mw3)
    print("TEST 5")
    print("ModbusTcpMaster.write_single_register()")
    mw4 = 1234
    mw5 = 4321
    print("send mw4 =", mw4)
    print("send mw5 =", mw5)
    print("ModbusTcpMaster.write_multiple_holding_register_uint16()")
    plc1.write_multiple_holding_register_uint16(register_address=4, register_value=mw4)
    plc1.write_multiple_holding_register_uint16(register_address=5, register_value=mw5)
    plc1.read_holding_registers(register_address = 4, register_count = 2)
    print("receive mw4 =", plc1.MW[4])
    print("receive mw5 =", plc1.MW[5])
    input("press any key for exit...")


if __name__ == "__main__":
    _unit_test_()

"""

********************************************************************************************************************

Hardware old:
+-------------------------------------+
| HMI                                 |
| +---------------------------------+ |
| | TCP client                      | |
| | +-----------------------------+ | |
| | | Modbus Master               | | |
| | | +-------------------------+ | | |
| | | | Read holding registers  | | | |
| | | | Write holding registers | | | |
| | | | Data type uint16        | | | |
| | | | Address MW0...MW65535   | | | |
| | | +-------------------------+ | | |
| | +-----------------------------+ | |
| +---------------------------------+ |
+---+---------------------------------+
    |
    | Ethernet (MODBUS TCP)
    |
+---+--------------------------------+
| Ethernet to RS485 MODBUS convertor |
| +--------------------------------+ |
| | TCP server                     | |
| | IP address = 162.168.13.128    | |
| | TCP port = 502                 | |
| +--------------------------------+ |
+---+--------------------------------+
    |
    | RS485 (MODBUS RTU or MODBUS ASCII)
    |
+---+---------------------------+
| PLC (old)                     |
| +---------------------------+ |
| | Modbus Slave address 1    | |
| | +-----------------------+ | |
| | | Holding registers     | | |
| | | Data type uint16      | | |
| | | Address MW0...MW65535 | | |
| | +-----------------------+ | |
| +---------------------------+ |
+-------------------------------+

Hardware new:
+-------------------------------------+
| HMI                                 |
| +---------------------------------+ |
| | TCP client                      | |
| | +-----------------------------+ | |
| | | Modbus Master               | | |
| | | +-------------------------+ | | |
| | | | Read holding registers  | | | |
| | | | Write holding registers | | | |
| | | | Data type uint16        | | | |
| | | | Address MW0...MW65535   | | | |
| | | +-------------------------+ | | |
| | +-----------------------------+ | |
| +---------------------------------+ |
+---+---------------------------------+
    |
    | Ethernet (MODBUS TCP)
    |
+---+-------------------------------+
| PLC (new)                         |
| +-------------------------------+ |
| | TCP server                    | |
| | IP address = 162.168.13.128   | |
| | TCP port = 502                | |
| | +---------------------------+ | |
| | | Modbus Slave address 1    | | |
| | | +-----------------------+ | | |
| | | | Holding registers     | | | |
| | | | Data type uint16      | | | |
| | | | Address MW0...MW65535 | | | |
| | | +-----------------------+ | | |
| | +---------------------------+ | |
| +-------------------------------+ |
+-----------------------------------+

********************************************************************************************************************

Read one holding register from PLC
Example MODBUS TCP request:
     |-ADU-----------------------------| (ADU = Application Data Unit)
     |-MBAP---------------|-PDU--------| (MBAP = MODBUS Application Protocol) (PDU = Protocol Data Unit)
     00 01 02 03 04 05 06 07 08 09 10 11 (Byte number   DEC)
HMI: 00 01 00 00 00 06 01 03 00 02 00 01 (Transmit byte HEX)
      |  |  |  |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |  |  |  +-MODBUS TCP PDU Register count low byte
      |  |  |  |  |  |  |  |  |  |  +----MODBUS TCP PDU Register count high byte
      |  |  |  |  |  |  |  |  |  +-------MODBUS TCP PDU Register start address low byte
      |  |  |  |  |  |  |  |  +----------MODBUS TCP PDU Register start address high byte
      |  |  |  |  |  |  |  +-------------MODBUS TCP PDU Modbus function code
      |  |  |  |  |  |  +----------------MODBUS TCP MBAP Modbus slave address
      |  |  |  |  |  +-------------------MODBUS TCP MBAP Message length low byte (after this)
      |  |  |  |  +----------------------MODBUS TCP MBAP Message length high byte
      |  |  |  +-------------------------MODBUS TCP MBAP Protocol Identifier low byte (constant)
      |  |  +----------------------------MODBUS TCP MBAP Protocol Identifier high byte (constant)
      |  +-------------------------------MODBUS TCP MBAP Transaction Identifier low byte (counter)
      +----------------------------------MODBUS TCP MBAP Transaction Identifier high byte (counter)
Example MODBUS TCP response:
     |-ADU--------------------------| (ADU = Application Data Unit)
     |-MBAP---------------|-PDU-----| (MBAP = MODBUS Application Protocol) (PDU = Protocol Data Unit)
     00 01 02 03 04 05 06 07 08 09 10 (Byte number   DEC)
PLC: 00 01 00 00 00 05 01 03 02 00 FF (Receive  byte HEX)
      |  |  |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |  |  +-MODBUS TCP PDU Register value low byte
      |  |  |  |  |  |  |  |  |  +----MODBUS TCP PDU Register value high byte
      |  |  |  |  |  |  |  |  +-------MODBUS TCP PDU Byte count (after this)
      |  |  |  |  |  |  |  +----------MODBUS TCP PDU Modbus function code
      |  |  |  |  |  |  +-------------MODBUS TCP MBAP Modbus slave address
      |  |  |  |  |  +----------------MODBUS TCP MBAP Message length low byte (after this)
      |  |  |  |  +-------------------MODBUS TCP MBAP Message length high byte
      |  |  |  +----------------------MODBUS TCP MBAP Protocol Identifier low byte (constant)
      |  |  +-------------------------MODBUS TCP MBAP Protocol Identifier high byte (constant)
      |  +----------------------------MODBUS TCP MBAP Transaction Identifier low byte (counter)
      +-------------------------------MODBUS TCP MBAP Transaction Identifier high byte (counter)

********************************************************************************************************************

Write one holding register from PLC
Example MODBUS TCP request:
     |-ADU--------------------------------------| (ADU = Application Data Unit)
     |-MBAP---------------|-PDU-----------------| (MBAP = MODBUS Application Protocol) (PDU = Protocol Data Unit)
     00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 (Byte number   DEC)
HMI: 00 01 00 00 00 09 01 10 00 02 00 01 02 00 FF (Transmit byte HEX)
      |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |  |  |  |  |  |  +-MODBUS TCP PDU Register value low byte
      |  |  |  |  |  |  |  |  |  |  |  |  |  +----MODBUS TCP PDU Register value high byte
      |  |  |  |  |  |  |  |  |  |  |  |  +-------MODBUS TCP PDU Byte count (after this)
      |  |  |  |  |  |  |  |  |  |  |  +----------MODBUS TCP PDU Register count low byte
      |  |  |  |  |  |  |  |  |  |  +-------------MODBUS TCP PDU Register count high byte
      |  |  |  |  |  |  |  |  |  +----------------MODBUS TCP PDU Register start address low byte
      |  |  |  |  |  |  |  |  +-------------------MODBUS TCP PDU Register start address high byte
      |  |  |  |  |  |  |  +----------------------MODBUS TCP PDU Modbus function code
      |  |  |  |  |  |  +-------------------------MODBUS TCP MBAP Modbus slave address
      |  |  |  |  |  +----------------------------MODBUS TCP MBAP Message length low byte (after this)
      |  |  |  |  +-------------------------------MODBUS TCP MBAP Message length high byte
      |  |  |  +----------------------------------MODBUS TCP MBAP Protocol Identifier low byte (constant)
      |  |  +-------------------------------------MODBUS TCP MBAP Protocol Identifier high byte (constant)
      |  +----------------------------------------MODBUS TCP MBAP Transaction Identifier low byte (counter)
      +-------------------------------------------MODBUS TCP MBAP Transaction Identifier high byte (counter)
Example MODBUS TCP response:
     |-ADU-----------------------------| (ADU = Application Data Unit)
     |-MBAP---------------|-PDU--------| (MBAP = MODBUS Application Protocol) (PDU = Protocol Data Unit)
     00 01 02 03 04 05 06 07 08 09 10 11 (Byte number   DEC)
PLC: 00 01 00 00 00 06 01 10 00 02 00 01 (Receive  byte HEX)
      |  |  |  |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |  |  |  +-MODBUS TCP PDU Register count low byte
      |  |  |  |  |  |  |  |  |  |  +----MODBUS TCP PDU Register count high byte
      |  |  |  |  |  |  |  |  |  +-------MODBUS TCP PDU Register start address low byte
      |  |  |  |  |  |  |  |  +----------MODBUS TCP PDU Register start address high byte
      |  |  |  |  |  |  |  +-------------MODBUS TCP PDU Modbus function code
      |  |  |  |  |  |  +----------------MODBUS TCP MBAP Modbus slave address
      |  |  |  |  |  +-------------------MODBUS TCP MBAP Message length low byte (after this)
      |  |  |  |  +----------------------MODBUS TCP MBAP Message length high byte
      |  |  |  +-------------------------MODBUS TCP MBAP Protocol Identifier low byte (constant)
      |  |  +----------------------------MODBUS TCP MBAP Protocol Identifier high byte (constant)
      |  +-------------------------------MODBUS TCP MBAP Transaction Identifier low byte (counter)
      +----------------------------------MODBUS TCP MBAP Transaction Identifier high byte (counter)

********************************************************************************************************************
"""

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

