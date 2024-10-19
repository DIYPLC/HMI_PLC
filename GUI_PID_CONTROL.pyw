#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
import socket
import struct
import time

#IP_ADR_PLC = '192.168.1.84' #PLC DELTA
IP_ADR_PLC = '127.0.0.1' #SIMULATOR
MODBUS_ADR_PLC = 1
ADR_REG_HmiSP = 4506
ADR_REG_HmiPV = 4508
ADR_REG_HmiOP = 4510
ADR_REG_HmiSW = 4512
ADR_REG_HmiCW = 4513

class MODBUS_TCP_MASTER(object):

    def __init__(self):
        self.Transaction_counter = 0
        self.Client_socket = None
        return

    def Start_TCP_client(self, IP_address = '127.0.0.1', TCP_port = 502):
        self.Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Client_socket.connect((IP_address, TCP_port))
        return

    def Stop_TCP_client(self):
        self.Client_socket.close()
        return

    def Read_holding_register_uint16(self, MODBUS_address = 1, Register_address = 0):
        """Read 1 holding register 16 bit unsigned int. Return register value or 0 if error"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        Tx_Transaction_ID   = self.Transaction_counter
        Tx_Protocol_ID      = 0
        Tx_Message_length   = 6
        Tx_MODBUS_address   = MODBUS_address
        Tx_MODBUS_function  = 3 #Read holding registers
        Tx_Register_address = Register_address
        Tx_Register_count   = 1
        Tx_ADU = struct.pack(">HHHBBHH", Tx_Transaction_ID, Tx_Protocol_ID, Tx_Message_length, Tx_MODBUS_address, Tx_MODBUS_function, Tx_Register_address, Tx_Register_count)
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 = Ethernet MTU size
        Error = (len(Rx_ADU) != 11) #11 byte OK
        if not(Error):
            (Rx_Transaction_ID, Rx_Protocol_ID, Rx_Message_length, Rx_MODBUS_address, Rx_MODBUS_function, Rx_Byte_count, Rx_Register_value) = struct.unpack(">HHHBBBH",Rx_ADU)
            Error = Error or (Rx_Transaction_ID  != Tx_Transaction_ID         )
            Error = Error or (Rx_Protocol_ID     != Tx_Protocol_ID            )
            Error = Error or (Rx_Message_length  != Tx_Register_count * 2 + 3 )
            Error = Error or (Rx_MODBUS_address  != Tx_MODBUS_address         )
            Error = Error or (Rx_MODBUS_function != Tx_MODBUS_function        )
            Error = Error or (Rx_Byte_count      != Tx_Register_count * 2     )
            if not(Error):
                Register_value = Rx_Register_value
            else:
                print("Error 1 read holding register")
                Register_value = 0
        else:
            print("Error 2 read holding register")
            Register_value = 0
        return Register_value

    def Read_holding_register_float32(self, MODBUS_address = 1, Register_address = 0):
        """Read 2 holding register 16 bit unsigned int. Return register value or 0 if error"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        Tx_Transaction_ID   = self.Transaction_counter
        Tx_Protocol_ID      = 0
        Tx_Message_length   = 6
        Tx_MODBUS_address   = MODBUS_address
        Tx_MODBUS_function  = 3 #Read holding registers
        Tx_Register_address = Register_address
        Tx_Register_count   = 2
        Tx_ADU = struct.pack(">HHHBBHH", Tx_Transaction_ID, Tx_Protocol_ID, Tx_Message_length, Tx_MODBUS_address, Tx_MODBUS_function, Tx_Register_address, Tx_Register_count)
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 = Ethernet MTU size
        Error = (len(Rx_ADU) != 13) #13 byte OK
        if not(Error):
            (Rx_Transaction_ID, Rx_Protocol_ID, Rx_Message_length, Rx_MODBUS_address, Rx_MODBUS_function, Rx_Byte_count, Rx_Register_value1, Rx_Register_value2) = struct.unpack(">HHHBBBHH",Rx_ADU)
            Error = Error or (Rx_Transaction_ID  != Tx_Transaction_ID         )
            Error = Error or (Rx_Protocol_ID     != Tx_Protocol_ID            )
            Error = Error or (Rx_Message_length  != Tx_Register_count * 2 + 3 )
            Error = Error or (Rx_MODBUS_address  != Tx_MODBUS_address         )
            Error = Error or (Rx_MODBUS_function != Tx_MODBUS_function        )
            Error = Error or (Rx_Byte_count      != Tx_Register_count * 2     )
            if not(Error):
                Decode_float32 = struct.unpack(">f",struct.pack(">HH",Rx_Register_value2,Rx_Register_value1))
                Register_value = Decode_float32[0]
            else:
                print("Error 3 read holding register")
                Register_value = 0.0
        else:
            print("Error 4 read holding register")
            Register_value = 0.0
        return Register_value

    def Write_multiple_holding_register_uint16(self, MODBUS_address = 1, Register_address = 0, Register_value = 0):
        """Write 1 holding register 16 bit unsigned int. Return error flag"""
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
        Tx_ADU = struct.pack(">HHHBBHHBH", Tx_Transaction_ID, Tx_Protocol_ID, Tx_Message_length, Tx_MODBUS_address, Tx_MODBUS_function, Tx_Register_address, Tx_Register_count, Tx_Byte_count, Tx_Register_value)
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 Ethernet MTU size
        Error = (len(Rx_ADU) != 12) #12 byte OK
        if not(Error):
            (Rx_Transaction_ID, Rx_Protocol_ID, Rx_Message_length, Rx_MODBUS_address, Rx_MODBUS_function, Rx_Register_address, Rx_Register_count) = struct.unpack(">HHHBBHH",Rx_ADU)
            Error = Error or (Rx_Transaction_ID  != Tx_Transaction_ID )
            Error = Error or (Rx_Protocol_ID     != Tx_Protocol_ID    )
            Error = Error or (Rx_Message_length  != 6                 )
            Error = Error or (Rx_MODBUS_address  != Tx_MODBUS_address )
            Error = Error or (Rx_MODBUS_function != Tx_MODBUS_function)
            Error = Error or (Rx_Register_count  != Tx_Register_count )
            if (Error):
                print("Error 1 write multiple holding register")
        else:
            print("Error 2 write multiple holding register")
            Error = True
        return Error

    def Write_multiple_holding_register_float32(self, MODBUS_address = 1, Register_address = 0, Register_value = 0.0):
        """Write 2 holding register 16 bit unsigned int. Return error flag"""
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
        Tx_ADU = struct.pack(">HHHBBHHBHH", Tx_Transaction_ID, Tx_Protocol_ID, Tx_Message_length, Tx_MODBUS_address, Tx_MODBUS_function, Tx_Register_address, Tx_Register_count, Tx_Byte_count, Tx_Register_value1, Tx_Register_value2)
        self.Client_socket.send(Tx_ADU)
        Rx_ADU = self.Client_socket.recv(1500) #1500 Ethernet MTU size
        Error = (len(Rx_ADU) != 12) #12 byte OK
        if not(Error):
            (Rx_Transaction_ID, Rx_Protocol_ID, Rx_Message_length, Rx_MODBUS_address, Rx_MODBUS_function, Rx_Register_address, Rx_Register_count) = struct.unpack(">HHHBBHH",Rx_ADU)
            Error = Error or (Rx_Transaction_ID  != Tx_Transaction_ID )
            Error = Error or (Rx_Protocol_ID     != Tx_Protocol_ID    )
            Error = Error or (Rx_Message_length  != 6                 )
            Error = Error or (Rx_MODBUS_address  != Tx_MODBUS_address )
            Error = Error or (Rx_MODBUS_function != Tx_MODBUS_function)
            Error = Error or (Rx_Register_count  != Tx_Register_count )
            if (Error):
                print("Error 3 write multiple holding register")
        else:
            print("Error 4 write multiple holding register")
            Error = True
        return Error


def CallBackEntrySP_Enter(self):
    value_local = float(EntrySP_value.get())
    PLC.Write_multiple_holding_register_float32(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiSP, Register_value = value_local)
    return

def CallBackEntryOP_Enter(self):
    value_local = float(EntryOP_value.get())
    PLC.Write_multiple_holding_register_float32(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiOP, Register_value = value_local)
    return

def CallBackButtonAUTO():
    PLC.Write_multiple_holding_register_uint16(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiCW, Register_value = 4)
    time.sleep(1.0)
    PLC.Write_multiple_holding_register_uint16(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiCW, Register_value = 0)
    return

def CallBackButtonMANUAL():
    PLC.Write_multiple_holding_register_uint16(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiCW, Register_value = 2)
    time.sleep(1.0)
    PLC.Write_multiple_holding_register_uint16(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiCW, Register_value = 0)
    return

def CallBackButtonSTOP():
    PLC.Write_multiple_holding_register_uint16(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiCW, Register_value = 1)
    time.sleep(1.0)
    PLC.Write_multiple_holding_register_uint16(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiCW, Register_value = 0)
    return

def CallBackButtonTREND():
    return

def CyclicTimeInterrypt():
    DIPcontrol.HmiSP_Prev = DIPcontrol.HmiSP
    DIPcontrol.HmiPV_Prev = DIPcontrol.HmiPV
    DIPcontrol.HmiOP_Prev = DIPcontrol.HmiOP
    Read_PLC_tags()
    if (DIPcontrol.HmiSP != DIPcontrol.HmiSP_Prev):
        EntrySP_value.set(Float32_to_string(Float32_value=DIPcontrol.HmiSP, Accuracy=2))
    if (DIPcontrol.HmiPV != DIPcontrol.HmiPV_Prev):
        EntryPV_value.set(Float32_to_string(Float32_value=DIPcontrol.HmiPV, Accuracy=2))
    if (DIPcontrol.HmiOP != DIPcontrol.HmiOP_Prev):
        EntryOP_value.set(Float32_to_string(Float32_value=DIPcontrol.HmiOP, Accuracy=2))
    if (DIPcontrol.HmiSW == 4): #AUTO MODE
        ButtonAUTO.configure(bg = 'yellow')
        EntryOP.configure(background = 'SystemButtonFace')
    else:
        ButtonAUTO.configure(bg = 'SystemButtonFace')
        EntryOP.configure(background = 'white')
    if (DIPcontrol.HmiSW == 2): #MANUAL MODE
        ButtonMANUAL.configure(bg = 'yellow')
    else:
        ButtonMANUAL.configure(bg = 'SystemButtonFace')
    if (DIPcontrol.HmiSW == 1): #STOP MODE
        ButtonSTOP.configure(bg = 'yellow')
    else:
        ButtonSTOP.configure(bg = 'SystemButtonFace')
    LabelMessage.configure(text=Error_message())
    root.after(500, CyclicTimeInterrypt) #delay call [ms].
    return

def Read_PLC_tags():
    DIPcontrol.HmiSP = PLC.Read_holding_register_float32(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiSP)
    DIPcontrol.HmiPV = PLC.Read_holding_register_float32(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiPV)
    DIPcontrol.HmiOP = PLC.Read_holding_register_float32(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiOP)
    DIPcontrol.HmiSW = PLC.Read_holding_register_uint16(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiSW)
    DIPcontrol.HmiCW = PLC.Read_holding_register_uint16(MODBUS_address = MODBUS_ADR_PLC, Register_address = ADR_REG_HmiCW)
    return

def Float32_to_string(Float32_value=0.0, Accuracy=2):
    return str(float(int(Float32_value * (10**Accuracy))) / (10**Accuracy))

def Error_message():
    msg = "No error."
    if (DIPcontrol.HmiSW & 1):
        msg = "Stop mode."
    if (DIPcontrol.HmiSW & 2):
        msg = "Manual mode."
    return msg

class StructPIDcontrol():
    HmiSP = 50.0
    HmiPV = 49.9
    HmiOP = 0.0
    HmiSW = 0
    HmiCW = 0
    HmiSP_Prev = 0.0
    HmiPV_Prev = 0.0
    HmiOP_Prev = 0.0

DIPcontrol = StructPIDcontrol()

root = tkinter.Tk()
root.title("2PIRC16 PID control")
root.resizable(False,False)

FrameValue = tkinter.Frame(root)
FrameValue.grid(column=0, row=0, padx=5, pady=5, sticky="news")

EntrySP_value = tkinter.StringVar()
EntrySP = tkinter.Entry(FrameValue, background = 'white')
EntrySP.configure(textvariable = EntrySP_value)
EntrySP.bind("<Return>", CallBackEntrySP_Enter) #Press "Enter"
EntrySP.grid(column=0, row=0, sticky="w")

LabelSP = tkinter.Label(FrameValue, text="Set point 0..100[unit]")
LabelSP.grid(column=1, row=0, sticky="w")

CircleSP = tkinter.Canvas(FrameValue, width=16, height=16, bg='SystemButtonFace')
CircleSP.create_oval(2, 2, 17, 17, fill='blue', outline='black')
CircleSP.grid(column=3, row=0)

EntryPV_value = tkinter.StringVar()
EntryPV = tkinter.Entry(FrameValue, background = 'SystemButtonFace')
EntryPV.configure(textvariable = EntryPV_value)
EntryPV.grid(column=0, row=1, sticky="w")

LabelPV = tkinter.Label(FrameValue, text="Process value 0..100[unit]")
LabelPV.grid(column=1, row=1, sticky="w")

CirclePV = tkinter.Canvas(FrameValue, width=16, height=16, bg='SystemButtonFace')
CirclePV.create_oval(2, 2, 17, 17, fill='green', outline='black')
CirclePV.grid(column=3, row=1)

EntryOP_value = tkinter.StringVar()
EntryOP = tkinter.Entry(FrameValue, background = 'SystemButtonFace')
EntryOP.configure(textvariable = EntryOP_value)
EntryOP.bind("<Return>", CallBackEntryOP_Enter) #Press "Enter"
EntryOP.grid(column=0, row=2, sticky="w")

LabelOP = tkinter.Label(FrameValue, text="Output power 0..100[unit]")
LabelOP.grid(column=1, row=2, sticky="w")

CircleOP = tkinter.Canvas(FrameValue, width=16, height=16, bg='SystemButtonFace')
CircleOP.create_oval(2, 2, 17, 17, fill='red', outline='black')
CircleOP.grid(column=3, row=2)

FrameButton = tkinter.Frame(root)
FrameButton.grid(column=0, row=1, padx=5, pady=5, sticky="news")

ButtonAUTO = tkinter.Button(FrameButton, text=("AUTO"), width=8, command=CallBackButtonAUTO)
ButtonAUTO.grid(column=0, row=0)

ButtonMANUAL = tkinter.Button(FrameButton, text=("MANUAL"), width=8, command=CallBackButtonMANUAL)
ButtonMANUAL.grid(column=1, row=0)

ButtonSTOP = tkinter.Button(FrameButton, text=("STOP"), width=8, command=CallBackButtonSTOP)
ButtonSTOP.grid(column=2, row=0)

ButtonTREND = tkinter.Button(FrameButton, text=("TREND"), width=8, command=CallBackButtonTREND)
ButtonTREND.grid(column=3, row=0)

FrameMessage = tkinter.Frame(root)
FrameMessage.grid(column=0, row=2, padx=5, pady=5, sticky="news")

LabelMessage = tkinter.Label(FrameMessage)
LabelMessage.grid(column=0, row=0, sticky="w")

PLC = MODBUS_TCP_MASTER()
PLC.Start_TCP_client(IP_address = IP_ADR_PLC, TCP_port = 502)
Read_PLC_tags()
EntrySP_value.set(Float32_to_string(Float32_value=DIPcontrol.HmiSP, Accuracy=2))
EntryPV_value.set(Float32_to_string(Float32_value=DIPcontrol.HmiPV, Accuracy=2))
EntryOP_value.set(Float32_to_string(Float32_value=DIPcontrol.HmiOP, Accuracy=2))

CyclicTimeInterrypt()
root.mainloop()
PLC.Stop_TCP_client()

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
