"""
Mitsubishi inverter protocol.
PU serial port control
Only one drive can be operated!
"""

import time
import struct

try: 
    import serial #RS232
except: #download from internet
    import os
    os.system("pip install pyserial") #python -m pip install pyserial
    import serial #RS232

class GlobalVar():
    SerialPort = serial.Serial() #19200Bod 8E2
GV = GlobalVar

def Init_COM_port():
    GV.SerialPort.port = 'COM1'
    GV.SerialPort.baudrate = 19200
    GV.SerialPort.bytesize = 8
    GV.SerialPort.parity = 'E'
    GV.SerialPort.stopbits = 2
    #GV.SerialPort.timeout = 1
    try:
        GV.SerialPort.open()
        print("Open",GV.SerialPort.name)
    except:
        print("ERROR COM RORT")
        exit()
    return

def Send_message(TxMessage):
    print(TxMessage, "len=", len(TxMessage))
    GV.SerialPort.write(TxMessage)
    return

def Receive_message():
    RxByte = GV.SerialPort.read() #Receiving the first byte
    RxMessage = RxByte
    while(RxByte != b'\r'): #Waiting for the end of the message symbol
        RxByte = GV.SerialPort.read() #Receiving a message by bytes
        RxMessage = RxMessage + RxByte
    print(RxMessage, "len=", len(RxMessage))
    #print(struct.unpack(">BBBB",RxMessage))
    return RxMessage

def Uint16_to_ASCII_Sumbol_lo_byte(Uint16):
    Uint16 = int(Uint16) & 0xF #0x00...0x0F
    if (Uint16 <= 9):
        result = Uint16 + 0x30 #0x30...0x39
    else:
        result = Uint16 + 0x37 #0x41...0x46
    return result

def Uint16_to_ASCII_Sumbol_hi_byte(Uint16):
    Uint16 = int(Uint16) & 0xF0
    Uint16 = Uint16 >> 4
    result = Uint16_to_ASCII_Sumbol_lo_byte(Uint16)
    return result

def Request_for_drive_power():
    ASCII_ENQ = 0x05
    STATION_NUMBER = 0x0
    ASCII_INVERTER_STATION_NUMBER_HI = Uint16_to_ASCII_Sumbol_hi_byte(STATION_NUMBER)
    ASCII_INVERTER_STATION_NUMBER_LO = Uint16_to_ASCII_Sumbol_lo_byte(STATION_NUMBER)
    COMMAND = 0x7D
    ASCII_INSTRUCTION_CODE_HI = Uint16_to_ASCII_Sumbol_hi_byte(COMMAND)
    ASCII_INSTRUCTION_CODE_LO = Uint16_to_ASCII_Sumbol_lo_byte(COMMAND)
    ASCII_DELAY_TIME = Uint16_to_ASCII_Sumbol_lo_byte(1)
    SUM = 0
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_HI) & 0xFF
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_LO) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_HI) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_LO) & 0xFF
    SUM = (SUM + ASCII_DELAY_TIME) & 0xFF
    ASCII_SUM_CHECK_HI = Uint16_to_ASCII_Sumbol_hi_byte(SUM)
    ASCII_SUM_CHECK_LO = Uint16_to_ASCII_Sumbol_lo_byte(SUM)
    ASCII_CR = 0x0D
    Message = struct.pack(">B",ASCII_ENQ)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_HI)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_LO)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_HI)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_LO)
    Message = Message + struct.pack(">B",ASCII_DELAY_TIME)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_HI)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_LO)
    Message = Message + struct.pack(">B",ASCII_CR)
    return Message

def Message_set_PU_mode():
    ASCII_ENQ = 0x05
    STATION_NUMBER = 0x64
    ASCII_INVERTER_STATION_NUMBER_HI = Uint16_to_ASCII_Sumbol_hi_byte(STATION_NUMBER)
    ASCII_INVERTER_STATION_NUMBER_LO = Uint16_to_ASCII_Sumbol_lo_byte(STATION_NUMBER)
    COMMAND = 0x85
    ASCII_INSTRUCTION_CODE_HI = Uint16_to_ASCII_Sumbol_hi_byte(COMMAND)
    ASCII_INSTRUCTION_CODE_LO = Uint16_to_ASCII_Sumbol_lo_byte(COMMAND)
    ASCII_DELAY_TIME = Uint16_to_ASCII_Sumbol_lo_byte(1) #WTF!?
    DATA_0 = 0x31
    DATA_1 = 0x30
    SUM = 0
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_HI) & 0xFF
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_LO) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_HI) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_LO) & 0xFF
    SUM = (SUM + ASCII_DELAY_TIME) & 0xFF
    SUM = (SUM + DATA_0) & 0xFF
    SUM = (SUM + DATA_1) & 0xFF
    ASCII_SUM_CHECK_HI = Uint16_to_ASCII_Sumbol_hi_byte(SUM)
    ASCII_SUM_CHECK_LO = Uint16_to_ASCII_Sumbol_lo_byte(SUM)
    ASCII_CR = 0x0D
    Message = struct.pack(">B",ASCII_ENQ)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_HI)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_LO)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_HI)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_LO)
    Message = Message + struct.pack(">B",ASCII_DELAY_TIME)
    Message = Message + struct.pack(">B",DATA_0)
    Message = Message + struct.pack(">B",DATA_1)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_HI)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_LO)
    Message = Message + struct.pack(">B",ASCII_CR)
    return Message

def Message_set_Frequency_Hz_x10(Set_frequency = 1234): #12.34Hz
    ASCII_ENQ = 0x05
    STATION_NUMBER = 0x64
    ASCII_INVERTER_STATION_NUMBER_HI = Uint16_to_ASCII_Sumbol_hi_byte(STATION_NUMBER)
    ASCII_INVERTER_STATION_NUMBER_LO = Uint16_to_ASCII_Sumbol_lo_byte(STATION_NUMBER)
    COMMAND = 0x85
    ASCII_INSTRUCTION_CODE_HI = Uint16_to_ASCII_Sumbol_hi_byte(COMMAND)
    ASCII_INSTRUCTION_CODE_LO = Uint16_to_ASCII_Sumbol_lo_byte(COMMAND)
    ASCII_DELAY_TIME = Uint16_to_ASCII_Sumbol_lo_byte(0x0)
    ASCII_TYPE_TX_DATA = Uint16_to_ASCII_Sumbol_lo_byte(0x3)
    ASCII_TYPE_RX_DATA = Uint16_to_ASCII_Sumbol_lo_byte(0x0)
    DATA_1_2 =  Set_frequency // 4096
    DATA_1_3 = (Set_frequency - DATA_1_2*4096) // 256
    DATA_2_0 = (Set_frequency - DATA_1_2*4096 - DATA_1_3*256) // 16
    DATA_2_1 = (Set_frequency - DATA_1_2*4096 - DATA_1_3*256 - DATA_2_0*16)
    ASCII_DATA_1_0 = Uint16_to_ASCII_Sumbol_lo_byte(0x0)
    ASCII_DATA_1_1 = Uint16_to_ASCII_Sumbol_lo_byte(0x0)
    ASCII_DATA_1_2 = Uint16_to_ASCII_Sumbol_lo_byte(DATA_1_2) #1= 40.96, 15 = 614.4
    ASCII_DATA_1_3 = Uint16_to_ASCII_Sumbol_lo_byte(DATA_1_3) #1 = 2.56, 15 = 38.4
    ASCII_DATA_2_0 = Uint16_to_ASCII_Sumbol_lo_byte(DATA_2_0) #1 = 0.16, 15 = 2.4
    ASCII_DATA_2_1 = Uint16_to_ASCII_Sumbol_lo_byte(DATA_2_1) #1 = 0.01, 15 = 0.15
    ASCII_DATA_2_2 = Uint16_to_ASCII_Sumbol_lo_byte(0x0)
    ASCII_DATA_2_3 = Uint16_to_ASCII_Sumbol_lo_byte(0x0)
    SUM = 0
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_HI) & 0xFF
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_LO) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_HI) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_LO) & 0xFF
    SUM = (SUM + ASCII_DELAY_TIME) & 0xFF
    SUM = (SUM + ASCII_TYPE_TX_DATA) & 0xFF
    SUM = (SUM + ASCII_TYPE_RX_DATA) & 0xFF
    SUM = (SUM + ASCII_DATA_1_0) & 0xFF
    SUM = (SUM + ASCII_DATA_1_1) & 0xFF
    SUM = (SUM + ASCII_DATA_1_2) & 0xFF
    SUM = (SUM + ASCII_DATA_1_3) & 0xFF
    SUM = (SUM + ASCII_DATA_2_0) & 0xFF
    SUM = (SUM + ASCII_DATA_2_1) & 0xFF
    SUM = (SUM + ASCII_DATA_2_2) & 0xFF
    SUM = (SUM + ASCII_DATA_2_3) & 0xFF
    ASCII_SUM_CHECK_HI = Uint16_to_ASCII_Sumbol_hi_byte(SUM)
    ASCII_SUM_CHECK_LO = Uint16_to_ASCII_Sumbol_lo_byte(SUM)
    ASCII_CR = 0x0D
    Message = struct.pack(">B",ASCII_ENQ)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_HI)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_LO)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_HI)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_LO)
    Message = Message + struct.pack(">B",ASCII_DELAY_TIME)
    Message = Message + struct.pack(">B",ASCII_TYPE_TX_DATA)
    Message = Message + struct.pack(">B",ASCII_TYPE_RX_DATA)
    Message = Message + struct.pack(">B",ASCII_DATA_1_0)
    Message = Message + struct.pack(">B",ASCII_DATA_1_1)
    Message = Message + struct.pack(">B",ASCII_DATA_1_2)
    Message = Message + struct.pack(">B",ASCII_DATA_1_3)
    Message = Message + struct.pack(">B",ASCII_DATA_2_0)
    Message = Message + struct.pack(">B",ASCII_DATA_2_1)
    Message = Message + struct.pack(">B",ASCII_DATA_2_2)
    Message = Message + struct.pack(">B",ASCII_DATA_2_3)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_HI)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_LO)
    Message = Message + struct.pack(">B",ASCII_CR)
    return Message

def Message_drive_forward():
    ASCII_ENQ = 0x05
    STATION_NUMBER = 0x64
    ASCII_INVERTER_STATION_NUMBER_HI = Uint16_to_ASCII_Sumbol_hi_byte(STATION_NUMBER)
    ASCII_INVERTER_STATION_NUMBER_LO = Uint16_to_ASCII_Sumbol_lo_byte(STATION_NUMBER)
    COMMAND = 0x85
    ASCII_INSTRUCTION_CODE_HI = Uint16_to_ASCII_Sumbol_hi_byte(COMMAND)
    ASCII_INSTRUCTION_CODE_LO = Uint16_to_ASCII_Sumbol_lo_byte(COMMAND)
    ASCII_DELAY_TIME = Uint16_to_ASCII_Sumbol_lo_byte(0x2) #WTF!?
    ASCII_DATA_1_0 = Uint16_to_ASCII_Sumbol_lo_byte(0xF)
    ASCII_DATA_1_1 = Uint16_to_ASCII_Sumbol_lo_byte(0x0)
    SUM = 0
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_HI) & 0xFF
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_LO) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_HI) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_LO) & 0xFF
    SUM = (SUM + ASCII_DELAY_TIME) & 0xFF
    SUM = (SUM + ASCII_DATA_1_0) & 0xFF
    SUM = (SUM + ASCII_DATA_1_1) & 0xFF
    ASCII_SUM_CHECK_HI = Uint16_to_ASCII_Sumbol_hi_byte(SUM)
    ASCII_SUM_CHECK_LO = Uint16_to_ASCII_Sumbol_lo_byte(SUM)
    ASCII_CR = 0x0D
    Message = struct.pack(">B",ASCII_ENQ)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_HI)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_LO)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_HI)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_LO)
    Message = Message + struct.pack(">B",ASCII_DELAY_TIME)
    Message = Message + struct.pack(">B",ASCII_DATA_1_0)
    Message = Message + struct.pack(">B",ASCII_DATA_1_1)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_HI)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_LO)
    Message = Message + struct.pack(">B",ASCII_CR)
    return Message

def Message_drive_stop():
    ASCII_ENQ = 0x05
    STATION_NUMBER = 0x64
    ASCII_INVERTER_STATION_NUMBER_HI = Uint16_to_ASCII_Sumbol_hi_byte(STATION_NUMBER)
    ASCII_INVERTER_STATION_NUMBER_LO = Uint16_to_ASCII_Sumbol_lo_byte(STATION_NUMBER)
    COMMAND = 0x85
    ASCII_INSTRUCTION_CODE_HI = Uint16_to_ASCII_Sumbol_hi_byte(COMMAND)
    ASCII_INSTRUCTION_CODE_LO = Uint16_to_ASCII_Sumbol_lo_byte(COMMAND)
    ASCII_DELAY_TIME = Uint16_to_ASCII_Sumbol_lo_byte(0x4) #WTF!?
    ASCII_DATA_1_0 = Uint16_to_ASCII_Sumbol_lo_byte(0xF)
    ASCII_DATA_1_1 = Uint16_to_ASCII_Sumbol_lo_byte(0x0)
    SUM = 0
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_HI) & 0xFF
    SUM = (SUM + ASCII_INVERTER_STATION_NUMBER_LO) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_HI) & 0xFF
    SUM = (SUM + ASCII_INSTRUCTION_CODE_LO) & 0xFF
    SUM = (SUM + ASCII_DELAY_TIME) & 0xFF
    SUM = (SUM + ASCII_DATA_1_0) & 0xFF
    SUM = (SUM + ASCII_DATA_1_1) & 0xFF
    ASCII_SUM_CHECK_HI = Uint16_to_ASCII_Sumbol_hi_byte(SUM)
    ASCII_SUM_CHECK_LO = Uint16_to_ASCII_Sumbol_lo_byte(SUM)
    ASCII_CR = 0x0D
    Message = struct.pack(">B",ASCII_ENQ)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_HI)
    Message = Message + struct.pack(">B",ASCII_INVERTER_STATION_NUMBER_LO)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_HI)
    Message = Message + struct.pack(">B",ASCII_INSTRUCTION_CODE_LO)
    Message = Message + struct.pack(">B",ASCII_DELAY_TIME)
    Message = Message + struct.pack(">B",ASCII_DATA_1_0)
    Message = Message + struct.pack(">B",ASCII_DATA_1_1)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_HI)
    Message = Message + struct.pack(">B",ASCII_SUM_CHECK_LO)
    Message = Message + struct.pack(">B",ASCII_CR)
    return Message

def main():
    Send_message(Request_for_drive_power())
    Receive_message()
    Send_message(Message_set_PU_mode())
    Receive_message()
    Send_message(Message_set_Frequency_Hz_x10(Set_frequency = 314)) #3.14Hz
    Receive_message()
    Send_message(Message_drive_forward())
    Receive_message()
    time.sleep(1.0) #1s
    Send_message(Message_drive_stop())
    Receive_message()
    return

if(__name__ == "__main__"):
    Init_COM_port()
    main()
    GV.SerialPort.close()
    print("Close COM port")

"""
Invertor: MITSUBISHI FR-A840-00250-E2-60 (7.5Kwt)
Hardware: Intel core i3 64bit + COM port RS232
Software: Windows 10 pro 64bit + Python 3.9 64bit
Software: https://www.serial-port-monitor.org/
Data (version): 30.11.2021
License: GNU GLP v2

Interface cable PU to RS232 Beijer SC-FRPC
Default inverter parameters.

PU interface RJ45 (RS422)
PIN1 SG   
PIN2 5V   
PIN3 RDA+ (RS422)
PIN4 SDB- (RS422)
PIN5 SDA+ (RS422)
PIN6 RDB- (RS422)
PIN7 SG   
PIN8 5V   

PCB MITSUBISHI FR-DU08 RS422 to RS485
PIN1 <-connect to-> PIN7 SG
PIN2 <-connect to-> PIN8 5V
PIN3 <-connect to-> PIN5 RS485 A+
PIN4 <-connect to-> PIN6 RS485 A-

CLI:
Open COM1
b'\x05007D10C\r' len= 9
b'\x0200    75\x034C\r' len= 13
b'\x05648511069\r' len= 11
b'\x0664\r' len= 4
b'\x05648503000013A00FF\r' len= 19
b'\x0664\r' len= 4
b'\x0564852F07F\r' len= 11
b'\x0664\r' len= 4
b'\x0564854F081\r' len= 11
b'\x0664\r' len= 4
Close COM port
"""
