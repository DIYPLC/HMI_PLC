# -*- coding: utf-8 -*-

"""
Simple Modbus TCP Master
Modbus Master == TCP Client
Modbus function 3  read holding registers uint16
Modbus function 16 write multiple holding registers uint16
Modbus function 6  write single register
Learn more at: http://www.modbus.org/

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

import socket
import struct
import array

def MODBUS_TCP_client_read_holding_register_uint16(IP_address = '127.0.0.1', TCP_port = 502, MODBUS_address = 1, Register_address = 0):
    """MODBUS TCP MASTER READ REGISTER FROM PLC"""
    try:
        Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Client_socket.connect((IP_address, TCP_port))
        Tx_Transaction_ID = 1
        Tx_Protocol_ID = 0
        Tx_Message_length = 6
        Tx_MODBUS_address = MODBUS_address
        Tx_MODBUS_function = 3
        Tx_Register_address = Register_address
        Tx_Register_count = 1
        Tx_ADU = struct.pack(">HHHBBHH",Tx_Transaction_ID,Tx_Protocol_ID,Tx_Message_length,Tx_MODBUS_address,Tx_MODBUS_function,Tx_Register_address,Tx_Register_count)
        Client_socket.send(Tx_ADU)
        Rx_ADU = Client_socket.recv(1500)
        (Rx_Transaction_ID,Rx_Protocol_ID,Rx_Message_length,Rx_MODBUS_address,Rx_MODBUS_function,Rx_Byte_count,Rx_Register_value) = struct.unpack(">HHHBBBH",Rx_ADU)
        Client_socket.close()
        Client_socket.__del__()
        return Rx_Register_value
    except:
        print("ERROR: MODBUS_TCP_client_read_holding_register_uint16()")
        Client_socket.close()
        Client_socket.__del__()
        return 0

def MODBUS_TCP_client_write_multiple_holding_register_uint16(IP_address = '127.0.0.1', TCP_port = 502, MODBUS_address = 1, Register_address = 0, Register_value = 0):
    """MODBUS TCP MASTER WRITE REGISTER TO PLC"""
    try:
        Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Client_socket.connect((IP_address, TCP_port))
        Tx_Transaction_ID   = 0
        Tx_Protocol_ID      = 0
        Tx_Message_length   = 9
        Tx_MODBUS_address   = MODBUS_address
        Tx_MODBUS_function  = 16 #Write multiple holding registers
        Tx_Register_address = int(Register_address) & 0xFFFF #Limit address
        Tx_Register_count   = 1
        Tx_Byte_count       = 2
        Tx_Register_value   = int(Register_value) & 0xFFFF #Limit value
        Tx_ADU = struct.pack(">HHHBBHHBH",Tx_Transaction_ID,Tx_Protocol_ID,Tx_Message_length,Tx_MODBUS_address,Tx_MODBUS_function,Tx_Register_address,Tx_Register_count,Tx_Byte_count,Tx_Register_value)
        Client_socket.send(Tx_ADU)
        Rx_ADU = Client_socket.recv(1500)
        (Rx_Transaction_ID,Rx_Protocol_ID,Rx_Message_length,Rx_MODBUS_address,Rx_MODBUS_function,Rx_Register_address,Rx_Register_count) = struct.unpack(">HHHBBHH",Rx_ADU)
        Client_socket.close()
        Client_socket.__del__()
        return
    except:
        print("ERROR: MODBUS_TCP_client_write_multiple_holding_register_uint16()")
        Client_socket.close()
        Client_socket.__del__()
    return

class MODBUS_TCP_master(object):

    def __init__(self):
        self.MW = array.array('H', [0]*65536) #MW[0]...MW[65535] uint16
        self.Transaction_counter = 0
        return

    def Start_TCP_client(self, IP_address = '127.0.0.1', TCP_port = 502):
        self.Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Client_socket.connect((IP_address, TCP_port))
        return

    def Stop_TCP_client(self):
        self.Client_socket.close()
        self.Client_socket.__del__()
        return

    def Get_MW(self, MW_address):
        return self.MW[(MW_address & 0xFFFF)]

    def Set_MW(self, MW_address, MW_value):
        self.MW[(MW_address & 0xFFFF)] = MW_value & 0xFFFF
        return

    def Read_holding_register_uint16(self, MODBUS_address = 1, Register_address = 0):
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        Tx_Transaction_ID   = self.Transaction_counter
        Tx_Protocol_ID      = 0
        Tx_Message_length   = 6
        Tx_MODBUS_address   = MODBUS_address
        Tx_MODBUS_function  = 3 #Read holding registers
        Tx_Register_address = Register_address
        Tx_Register_count   = 1
        Tx_ADU = struct.pack(">HHHBBHH",
                             Tx_Transaction_ID,
                             Tx_Protocol_ID,
                             Tx_Message_length,
                             Tx_MODBUS_address,
                             Tx_MODBUS_function,
                             Tx_Register_address,
                             Tx_Register_count)
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 = Ethernet MTU size
        Error = (len(Rx_ADU) != 11) #11 byte OK
        if (Error == False):
            (Rx_Transaction_ID,
             Rx_Protocol_ID,
             Rx_Message_length,
             Rx_MODBUS_address,
             Rx_MODBUS_function,
             Rx_Byte_count,
             Rx_Register_value) = struct.unpack(">HHHBBBH",Rx_ADU)
            Error = Error or (Rx_Transaction_ID  != Tx_Transaction_ID         )
            Error = Error or (Rx_Protocol_ID     != Tx_Protocol_ID            )
            Error = Error or (Rx_Message_length  != Tx_Register_count * 2 + 3 )
            Error = Error or (Rx_MODBUS_address  != Tx_MODBUS_address         )
            Error = Error or (Rx_MODBUS_function != Tx_MODBUS_function        )
            Error = Error or (Rx_Byte_count      != Tx_Register_count * 2     )
            if (Error == False):
                Register_value = Rx_Register_value
            else:
                print("Error read holding register")
                print(Tx_ADU)
                print(Rx_ADU)
                Register_value = 0
        else:
            print("Error read holding register")
            print(Tx_ADU)
            print(Rx_ADU)
            Register_value = 0
        return Register_value

    def Read_holding_register_float32(self, MODBUS_address = 1, Register_address = 0):
        """use Register_address and Register_address + 1"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        Tx_Transaction_ID   = self.Transaction_counter
        Tx_Protocol_ID      = 0
        Tx_Message_length   = 6
        Tx_MODBUS_address   = MODBUS_address
        Tx_MODBUS_function  = 3 #Read holding registers
        Tx_Register_address = Register_address
        Tx_Register_count   = 2
        Tx_ADU = struct.pack(">HHHBBHH",
                             Tx_Transaction_ID,
                             Tx_Protocol_ID,
                             Tx_Message_length,
                             Tx_MODBUS_address,
                             Tx_MODBUS_function,
                             Tx_Register_address,
                             Tx_Register_count)
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 = Ethernet MTU size
        Error = (len(Rx_ADU) != 13) #13 byte OK
        if (Error == False):
            (Rx_Transaction_ID,
             Rx_Protocol_ID,
             Rx_Message_length,
             Rx_MODBUS_address,
             Rx_MODBUS_function,
             Rx_Byte_count,
             Rx_Register_value1,
             Rx_Register_value2) = struct.unpack(">HHHBBBHH",Rx_ADU)
            Error = Error or (Rx_Transaction_ID  != Tx_Transaction_ID         )
            Error = Error or (Rx_Protocol_ID     != Tx_Protocol_ID            )
            Error = Error or (Rx_Message_length  != Tx_Register_count * 2 + 3 )
            Error = Error or (Rx_MODBUS_address  != Tx_MODBUS_address         )
            Error = Error or (Rx_MODBUS_function != Tx_MODBUS_function        )
            Error = Error or (Rx_Byte_count      != Tx_Register_count * 2     )
            if (Error == False):
                Decode_float32 = struct.unpack(">f",struct.pack(">HH",Rx_Register_value2,Rx_Register_value1))
                Register_value = Decode_float32[0]
            else:
                print("Error read holding register")
                print(Tx_ADU)
                print(Rx_ADU)
                Register_value = 0.0
        else:
            print("Error read holding register")
            print(Tx_ADU)
            print(Rx_ADU)
            Register_value = 0.0
        return Register_value

    def Write_multiple_holding_register_uint16(self, MODBUS_address = 1, Register_address = 0, Register_value = 0):
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        Tx_Transaction_ID   = self.Transaction_counter
        Tx_Protocol_ID      = 0
        Tx_Message_length   = 9
        Tx_MODBUS_address   = MODBUS_address
        Tx_MODBUS_function  = 16 #Write multiple holding registers
        Tx_Register_address = Register_address
        Tx_Register_count   = 1
        Tx_Byte_count       = 2
        Tx_Register_value   = Register_value
        Tx_ADU = struct.pack(">HHHBBHHBH",
                             Tx_Transaction_ID,
                             Tx_Protocol_ID,
                             Tx_Message_length,
                             Tx_MODBUS_address,
                             Tx_MODBUS_function,
                             Tx_Register_address,
                             Tx_Register_count,
                             Tx_Byte_count,
                             Tx_Register_value)
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 Ethernet MTU size
        Error = (len(Rx_ADU) != 12) #12 byte OK
        if (Error == False):
            (Rx_Transaction_ID,
             Rx_Protocol_ID,
             Rx_Message_length,
             Rx_MODBUS_address,
             Rx_MODBUS_function,
             Rx_Register_address,
             Rx_Register_count) = struct.unpack(">HHHBBHH",Rx_ADU)
            Error = Error or (Rx_Transaction_ID  != Tx_Transaction_ID )
            Error = Error or (Rx_Protocol_ID     != Tx_Protocol_ID    )
            Error = Error or (Rx_Message_length  != 6                 )
            Error = Error or (Rx_MODBUS_address  != Tx_MODBUS_address )
            Error = Error or (Rx_MODBUS_function != Tx_MODBUS_function)
            Error = Error or (Rx_Register_count  != Tx_Register_count )
            if (Error == True):
                print("Error write multiple holding register")
                print(Tx_ADU)
                print(Rx_ADU)
        else:
            print("Error write multiple holding register")
            print(Tx_ADU)
            print(Rx_ADU)
            Error = True
        return Error

    def Write_multiple_holding_register_float32(self, MODBUS_address = 1, Register_address = 0, Register_value = 0.0):
        """use Register_address and Register_address + 1"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        Tx_Transaction_ID   = self.Transaction_counter
        Tx_Protocol_ID      = 0
        Tx_Message_length   = 11
        Tx_MODBUS_address   = MODBUS_address
        Tx_MODBUS_function  = 16 #Write multiple holding registers
        Tx_Register_address = Register_address
        Tx_Register_count   = 2
        Tx_Byte_count       = 4
        Tx_Register_value   = Register_value
        (Tx_Register_value2, Tx_Register_value1) = struct.unpack(">HH",struct.pack(">f",Register_value))
        Tx_ADU = struct.pack(">HHHBBHHBHH",
                             Tx_Transaction_ID,
                             Tx_Protocol_ID,
                             Tx_Message_length,
                             Tx_MODBUS_address,
                             Tx_MODBUS_function,
                             Tx_Register_address,
                             Tx_Register_count,
                             Tx_Byte_count,
                             Tx_Register_value1,
                             Tx_Register_value2)
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 Ethernet MTU size
        Error = (len(Rx_ADU) != 12) #12 byte OK
        if (Error == False):
            (Rx_Transaction_ID,
             Rx_Protocol_ID,
             Rx_Message_length,
             Rx_MODBUS_address,
             Rx_MODBUS_function,
             Rx_Register_address,
             Rx_Register_count) = struct.unpack(">HHHBBHH",Rx_ADU)
            Error = Error or (Rx_Transaction_ID  != Tx_Transaction_ID )
            Error = Error or (Rx_Protocol_ID     != Tx_Protocol_ID    )
            Error = Error or (Rx_Message_length  != 6                 )
            Error = Error or (Rx_MODBUS_address  != Tx_MODBUS_address )
            Error = Error or (Rx_MODBUS_function != Tx_MODBUS_function)
            Error = Error or (Rx_Register_count  != Tx_Register_count )
            if (Error == True):
                print("Error write multiple holding register")
                print(Tx_ADU)
                print(Rx_ADU)
        else:
            print("Error write multiple holding register")
            print(Tx_ADU)
            print(Rx_ADU)
            Error = True
        return Error

    def Write_single_register(self, MODBUS_address = 1, Register_address = 0, Register_value = 0):
        """uint16 Register_value"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        Tx_Transaction_ID   = self.Transaction_counter
        Tx_Protocol_ID      = 0
        Tx_Message_length   = 6
        Tx_MODBUS_address   = MODBUS_address
        Tx_MODBUS_function  = 6 #write_single_register
        Tx_Register_address = Register_address
        Tx_Register_value   = Register_value
        Tx_MBAP = struct.pack(">HHHB", Tx_Transaction_ID, Tx_Protocol_ID, Tx_Message_length, Tx_MODBUS_address)
        Tx_PDU = struct.pack(">BHH", Tx_MODBUS_function, Tx_Register_address, Tx_Register_value)
        Tx_ADU = Tx_MBAP + Tx_PDU
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 Ethernet MTU size
        Error = (len(Rx_ADU) != 12) #12 byte OK
        if (Error == False):
            Error = (Rx_ADU != Tx_ADU)
            if (Error == True):
                print("Error write single register")
                print(Tx_ADU)
                print(Rx_ADU)
        else:
            print("Error write single register")
            print(Tx_ADU)
            print(Rx_ADU)
            Error = True
        return Error

    def Read_holding_registers(self, MODBUS_address = 1, Register_address = 0, Register_count = 1):
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        Tx_Transaction_ID   = self.Transaction_counter
        Tx_Protocol_ID      = 0
        Tx_Message_length   = 6
        Tx_MODBUS_address   = MODBUS_address & 0xFF
        Tx_MODBUS_function  = 3 #Read holding registers
        Tx_Register_address = int(Register_address) & 0xFFFF
        Tx_Register_count   = int(Register_count) & 0xFF #1...127 Maximum
        Tx_MBAP = struct.pack(">HHHB", Tx_Transaction_ID, Tx_Protocol_ID, Tx_Message_length, Tx_MODBUS_address)
        Tx_PDU = struct.pack(">BHH", Tx_MODBUS_function, Tx_Register_address, Tx_Register_count)
        Tx_ADU = Tx_MBAP + Tx_PDU
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 Ethernet MTU size
        Error = (len(Rx_ADU) != Register_count * 2 + 9)#Check len ADU
        if(Error == False):
            Rx_Transaction_ID  = int((Rx_ADU[0] << 8 ) | Rx_ADU[1]) & 0xFFFF
            Rx_Protocol_ID     = int((Rx_ADU[2] << 8 ) | Rx_ADU[3]) & 0xFFFF
            Rx_Message_length  = int((Rx_ADU[4] << 8 ) | Rx_ADU[5]) & 0xFFFF
            Rx_MODBUS_address  = int(Rx_ADU[6]) & 0xFF
            Rx_MODBUS_function = int(Rx_ADU[7]) & 0xFF
            Rx_Byte_count      = int(Rx_ADU[8]) & 0xFF
            Error = Error or (Rx_Transaction_ID  != Tx_Transaction_ID         )
            Error = Error or (Rx_Protocol_ID     != Tx_Protocol_ID            )
            Error = Error or (Rx_Message_length  != Tx_Register_count * 2 + 3 )
            Error = Error or (Rx_MODBUS_address  != Tx_MODBUS_address         )
            Error = Error or (Rx_MODBUS_function != Tx_MODBUS_function        )
            Error = Error or (Rx_Byte_count      != Tx_Register_count * 2     )
            if(Error == False):
                for Counter in range(Tx_Register_count): #Counter = 0...Register_count
                    Hi_byte = int(Rx_ADU[9  + Counter * 2]) & 0xFF
                    Lo_byte = int(Rx_ADU[10 + Counter * 2]) & 0xFF
                    Register_value = int((Hi_byte << 8 ) | Lo_byte) & 0xFFFF
                    Reg_adr = int(Counter + Register_address) & 0xFFFF
                    self.MW[Reg_adr] = Register_value
            else:
                print("Error read holding register")
        else:
                print("Error read holding register")
        return

def Two_uint16_to_float32(Register_value1, Register_value2):
    tmp = struct.unpack(">f",struct.pack(">HH", Register_value2, Register_value1))
    return tmp[0]

def Unit_test():
    PLC1 = MODBUS_TCP_master()
    PLC1.Start_TCP_client(IP_address = '127.0.0.1')
    while True:
        MW7 = PLC1.Read_holding_register_uint16(Register_address = 7)
        print(MW7)
        MW7 = (MW7 + 1) & 0xFFFF
        MW7 = PLC1.Write_multiple_holding_register_uint16(Register_address = 7, Register_value = MW7)
    PLC1.Stop_TCP_client()

if (__name__ == '__main__'):
    Unit_test()

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
