# -*- coding: utf-8 -*-

"""
MODBUS ASCII MASTER
ЧЕРНОВИК
For DIY PLC ARDUINO NANO
Windows 10 pro 64bit
Python v3.9.5
"""

import struct
import ctypes #Для инверсии байта
import time #Для бутлоадера

try: 
    import serial #RS232
except: #download from internet
    import os
    os.system("pip install pyserial") #python -m pip install pyserial
    import serial #RS232

class GlobalVar():
    SerialPort = serial.Serial()
GV = GlobalVar

def Init_COM_port():
    GV.SerialPort.port = 'COM9'
    GV.SerialPort.baudrate = 9600
    GV.SerialPort.bytesize = 8
    GV.SerialPort.parity = 'N'
    GV.SerialPort.stopbits = 1
    #GV.SerialPort.timeout = 1
    try:
        GV.SerialPort.open()
        print("Open",GV.SerialPort.name)
    except:
        print("ERROR COM RORT")
        exit()
    return

def Send_message(TxMessage):
    #print(TxMessage, "len=", len(TxMessage))
    GV.SerialPort.write(TxMessage)
    return

def Receive_message():
    RxByte = GV.SerialPort.read() #Receiving the first byte
    RxMessage = RxByte
    while(RxByte != b'\n'): #Waiting for the end of the message symbol
        RxByte = GV.SerialPort.read() #Receiving a message by bytes
        RxMessage = RxMessage + RxByte
    #print(RxMessage, "len=", len(RxMessage))
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

def Ascii_to_int(ASCII):
    result = 0
    if(0x30 == ASCII):
        result = 0
    elif(0x31 == ASCII):
        result = 1
    elif(0x32 == ASCII):
        result = 2
    elif(0x33 == ASCII):
        result = 3
    elif(0x34 == ASCII):
        result = 4
    elif(0x35 == ASCII):
        result = 5
    elif(0x36 == ASCII):
        result = 6
    elif(0x37 == ASCII):
        result = 7
    elif(0x38 == ASCII):
        result = 8
    elif(0x39 == ASCII):
        result = 9
    elif(0x41 == ASCII):
        result = 10
    elif(0x42 == ASCII):
        result = 11
    elif(0x43 == ASCII):
        result = 12
    elif(0x44 == ASCII):
        result = 13
    elif(0x45 == ASCII):
        result = 14
    elif(0x46 == ASCII):
        result = 15
    return result

def PDU_TO_ADU(PDU):
    #CONVERT PDU TO ADU_HEX
    SLAVE_ADDRESS = 1
    ADU_HEX = struct.pack(">B", SLAVE_ADDRESS) + PDU
    #CALC LCR
    LCR = 0
    for i in range(len(ADU_HEX)):
        LCR = (LCR + ADU_HEX[i]) & 0xFF
    ui8 = ctypes.c_uint8(LCR)
    ui8.value = ~ui8.value
    LCR = ui8.value + 1
    ADU_HEX = ADU_HEX + struct.pack(">B",LCR)
    #ADU_HEX TO ADU_ASCII
    START_BYTE = 0x3A
    ADU_ASCII = struct.pack(">B",START_BYTE)
    for i in range(len(ADU_HEX)):
        HiByte = Uint16_to_ASCII_Sumbol_hi_byte(ADU_HEX[i])
        LoByte = Uint16_to_ASCII_Sumbol_lo_byte(ADU_HEX[i])
        ADU_ASCII = ADU_ASCII + struct.pack(">B", HiByte)
        ADU_ASCII = ADU_ASCII + struct.pack(">B", LoByte)
    STOP_BYTE1 = 0x0D
    STOP_BYTE2 = 0x0A
    ADU_ASCII = ADU_ASCII + struct.pack(">B", STOP_BYTE1)
    ADU_ASCII = ADU_ASCII + struct.pack(">B", STOP_BYTE2)
    return ADU_ASCII

def TX_MSG_READ_HOLDING_REGISTERS(REGISTER_ADDRESS = 4):
    FUNCTION_CODE = 3
    REGISTER_START = REGISTER_ADDRESS
    REGISTER_COUNT = 1
    PDU = (struct.pack(">B", FUNCTION_CODE) +
        struct.pack(">H", REGISTER_START) +
        struct.pack(">H", REGISTER_COUNT))
    return PDU_TO_ADU(PDU)

def RX_MSG_READ_HOLDING_REGISTERS(ADU):
    if(15 == len(ADU)):
        (START_BYTE,
        SLAVE_ADDRESS_B1,
        SLAVE_ADDRESS_B2,
        FUNCTION_CODE_B1,
        FUNCTION_CODE_B2,
        BYTE_COUNT_B1,
        BYTE_COUNT_B2,
        REGISTER_DATA_B1,
        REGISTER_DATA_B2,
        REGISTER_DATA_B3,
        REGISTER_DATA_B4,
        LCR_B1,
        LCR_B2,
        STOP_BYTE1,
        STOP_BYTE2) = struct.unpack(">BBBBBBBBBBBBBBB",ADU)
        DATA1 = Ascii_to_int(REGISTER_DATA_B1)
        DATA2 = Ascii_to_int(REGISTER_DATA_B2)
        DATA3 = Ascii_to_int(REGISTER_DATA_B3)
        DATA4 = Ascii_to_int(REGISTER_DATA_B4)
        DATA = (DATA1 << 12) | (DATA2 << 8) | (DATA3 << 4) | DATA4
    return DATA

def ReadMW(RegisterAddress = 0):
    Send_message(TX_MSG_READ_HOLDING_REGISTERS(RegisterAddress))
    Msg = Receive_message()
    HR = RX_MSG_READ_HOLDING_REGISTERS(Msg)
    return HR

def main():
    print("MW0 =", ReadMW(0))
    return

if(__name__ == "__main__"):
    Init_COM_port()
    time.sleep(1.0) #Delay for boot loader m328p
    while(1):
        main()
        time.sleep(0.1)
    GV.SerialPort.close()
    print("Close COM port")

"""
//READ HOLDING REGISTERS
//Example MODBUS ASCII request:
//     |-ADU--------------------------------------------| (ADU = Application Data Unit)
//                 |-PDU--------------------|             (PDU = Protocol Data Unit)
//HMI: 3A 30 31 30 33 30 30 30 32 30 30 30 31 46 39 0D 0A //Rx message ASCII HEX
//CNT  01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17
//HMI:  :  0  1  0  3  0  0  0  2  0  0  0  1  F  9 CR LF //Rx message string
//HMI: 3A    01    03    00    02    00    01    F9 0D 0A //Rx message HEX
//      |     |     |     |     |     |     |     |  |  |
//      |     |     |     |     |     |     |     |  |  +- Stop byte LF
//      |     |     |     |     |     |     |     |  +---- Stop byte CR
//      |     |     |     |     |     |     |     +------- Checksum LCR
//      |     |     |     |     |     |     +------------- PDU Register count low byte
//      |     |     |     |     |     +------------------- PDU Register count high byte
//      |     |     |     |     +------------------------- PDU Register start address low byte
//      |     |     |     +------------------------------- PDU Register start address high byte
//      |     |     +------------------------------------- PDU Modbus function code
//      |     +------------------------------------------- Modbus slave address
//      +------------------------------------------------- Start byte ":"
//HMI: 3A    01    03    00    02    00    01    F9 0D 0A //Rx message HEX
//LCR =  not(01 +  03 +  00 +  02 +  00 +  01)+1=F9
//
//Example MODBUS ASCII response:
//     |-ADU--------------------------------------| (ADU = Application Data Unit)
//                 |-PDU--------------|             (PDU = Protocol Data Unit)
//PLC: 3A 30 31 30 33 30 32 30 30 30 30 46 41 0D 0A //Tx message ASCII HEX
//CNT  01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
//PLC:  :  0  1  0  3  0  2  0  0  0  0  F  A CR LF //Tx message ASCII string
//PLC: 3A    01    03    02    00    00    FA 0D 0A //Tx message ASCII HEX
//      |     |     |     |     |     |     |  |  |
//      |     |     |     |     |     |     |  |  +- Stop byte LF
//      |     |     |     |     |     |     |  +---- Stop byte CR
//      |     |     |     |     |     |     +------- Checksum LCR
//      |     |     |     |     |     +------------- PDU Register value low byte
//      |     |     |     |     +------------------- PDU Register value high byte
//      |     |     |     +------------------------- PDU Byte count (after this)
//      |     |     +------------------------------- PDU Modbus function code
//      |     +------------------------------------- Modbus slave address
//      +------------------------------------------- Start byte ":"
//PLC: 3A    01    03    02    00    00    FA 0D 0A //Tx message ASCII HEX
//LCR =  not(01 +  03 +  02 +  00 +  00)+1=FA
"""

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
