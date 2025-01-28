#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
import socket
import struct
import time

class ModbusTcpMaster(object):

    def __init__(self):
        self.Transaction_counter = 0
        self.Client_socket = None
        self.Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return

    def start_tcp_client(self, ip_address='127.0.0.1', tcp_port=502) -> None:
        self.Client_socket.connect((ip_address, tcp_port))
        return

    def __del__(self) -> None:
        self.Client_socket.close()
        del self
        return

    def read_holding_register_uint16(self, modbus_address=1, register_address=0) -> int:
        """Read 1 holding register 16 bit unsigned int. Return register value or 0 if error"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        tx_transaction_id = self.Transaction_counter
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address
        tx_modbus_function = 3  #Read holding registers
        tx_register_address = register_address
        tx_register_count = 1
        tx_adu = struct.pack(">HHHBBHH", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                             tx_modbus_function, tx_register_address, tx_register_count)
        self.Client_socket.send(tx_adu)
        rx_adu = self.Client_socket.recv(1500)  #1500 = Ethernet MTU size
        error = (len(rx_adu) != 11)  #11 byte OK
        if not error:
            (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function, rx_byte_count,
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
                print("error 1 read holding register")
                register_value = 0
        else:
            print("error 2 read holding register")
            register_value = 0
        return register_value

    def read_holding_register_float32(self, modbus_address=1, register_address=0) -> float:
        """Read 2 holding register 16 bit unsigned int. Return register value or 0 if error"""
        self.Transaction_counter = (self.Transaction_counter + 1) & 0xFFFF
        tx_transaction_id = self.Transaction_counter
        tx_protocol_id = 0
        tx_message_length = 6
        tx_modbus_address = modbus_address
        tx_modbus_function = 3  #Read holding registers
        tx_register_address = register_address
        tx_register_count = 2
        tx_adu = struct.pack(">HHHBBHH", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                             tx_modbus_function, tx_register_address, tx_register_count)
        self.Client_socket.send(tx_adu)
        rx_adu = self.Client_socket.recv(1500)  #1500 = Ethernet MTU size
        error = (len(rx_adu) != 13)  #13 byte OK
        if not error:
            (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function, rx_byte_count,
             rx_register_value1, rx_register_value2) = struct.unpack(">HHHBBBHH", rx_adu)
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
                print("error 3 read holding register")
                register_value = 0.0
        else:
            print("error 4 read holding register")
            register_value = 0.0
        return register_value

    def write_multiple_holding_register_uint16(self, modbus_address=1, register_address=0, register_value=0) -> bool:
        """Write 1 holding register 16 bit unsigned int. Return error flag"""
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
        tx_adu = struct.pack(">HHHBBHHBH", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                             tx_modbus_function, tx_register_address, tx_register_count, tx_byte_count,
                             tx_register_value)
        self.Client_socket.send(tx_adu)
        rx_adu = self.Client_socket.recv(1500)  #1500 Ethernet MTU size
        error = (len(rx_adu) != 12)  #12 byte OK
        if not error:
            (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function,
             rx_register_address, rx_register_count) = struct.unpack(">HHHBBHH", rx_adu)
            error = error or (rx_transaction_id != tx_transaction_id)
            error = error or (rx_protocol_id != tx_protocol_id)
            error = error or (rx_message_length != 6)
            error = error or (rx_modbus_address != tx_modbus_address)
            error = error or (rx_modbus_function != tx_modbus_function)
            error = error or (rx_register_count != tx_register_count)
            if error:
                print("error 1 write multiple holding register")
        else:
            print("error 2 write multiple holding register")
            error = True
        return error

    def write_multiple_holding_register_float32(self, modbus_address=1, register_address=0, register_value=0.0) -> bool:
        """Write 2 holding register 16 bit unsigned int. Return error flag"""
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
        tx_adu = struct.pack(">HHHBBHHBHH", tx_transaction_id, tx_protocol_id, tx_message_length, tx_modbus_address,
                             tx_modbus_function, tx_register_address, tx_register_count, tx_byte_count,
                             tx_register_value1, tx_register_value2)
        self.Client_socket.send(tx_adu)
        rx_adu = self.Client_socket.recv(1500)  #1500 Ethernet MTU size
        error = (len(rx_adu) != 12)  #12 byte OK
        if not error:
            (rx_transaction_id, rx_protocol_id, rx_message_length, rx_modbus_address, rx_modbus_function,
             rx_register_address, rx_register_count) = struct.unpack(">HHHBBHH", rx_adu)
            error = error or (rx_transaction_id != tx_transaction_id)
            error = error or (rx_protocol_id != tx_protocol_id)
            error = error or (rx_message_length != 6)
            error = error or (rx_modbus_address != tx_modbus_address)
            error = error or (rx_modbus_function != tx_modbus_function)
            error = error or (rx_register_count != tx_register_count)
            if error:
                print("error 3 write multiple holding register")
        else:
            print("error 4 write multiple holding register")
            error = True
        return error


def call_back_entry_sp_enter(self) -> None:
    value_local = float(GUI.EntrySP_value.get())
    PLC.write_multiple_holding_register_float32(register_address=GV.ADR_REG_HmiSP, register_value=value_local)
    return


def call_back_entry_op_enter(self) -> None:
    value_local = float(GUI.EntryOP_value.get())
    PLC.write_multiple_holding_register_float32(register_address=GV.ADR_REG_HmiOP, register_value=value_local)
    return


def call_back_button_auto() -> None:
    PLC.write_multiple_holding_register_uint16(register_address=GV.ADR_REG_HmiCW, register_value=4)
    time.sleep(1.0)
    PLC.write_multiple_holding_register_uint16(register_address=GV.ADR_REG_HmiCW, register_value=0)
    return


def call_back_button_manual() -> None:
    PLC.write_multiple_holding_register_uint16(register_address=GV.ADR_REG_HmiCW, register_value=2)
    time.sleep(1.0)
    PLC.write_multiple_holding_register_uint16(register_address=GV.ADR_REG_HmiCW, register_value=0)
    return


def call_back_button_stop() -> None:
    PLC.write_multiple_holding_register_uint16(register_address=GV.ADR_REG_HmiCW, register_value=1)
    time.sleep(1.0)
    PLC.write_multiple_holding_register_uint16(register_address=GV.ADR_REG_HmiCW, register_value=0)
    return


def call_back_cyclic_time() -> None:
    GV.HmiSP_Prev = GV.HmiSP
    GV.HmiPV_Prev = GV.HmiPV
    GV.HmiOP_Prev = GV.HmiOP
    read_plc_tags()
    if GV.HmiSP != GV.HmiSP_Prev:
        GUI.EntrySP_value.set(float32_to_string(float32_value=GV.HmiSP, accuracy=2))
    if GV.HmiPV != GV.HmiPV_Prev:
        GUI.EntryPV_value.set(float32_to_string(float32_value=GV.HmiPV, accuracy=2))
    if GV.HmiOP != GV.HmiOP_Prev:
        GUI.EntryOP_value.set(float32_to_string(float32_value=GV.HmiOP, accuracy=2))
    if GV.HmiSW == 4:  #AUTO MODE
        GUI.ButtonAUTO.configure(bg='yellow')
        GUI.EntryOP.configure(background=GUI.color_bg_1)
    else:
        GUI.ButtonAUTO.configure(bg=GUI.color_bg_1)
        GUI.EntryOP.configure(background='white')
    if GV.HmiSW == 2:  #MANUAL MODE
        GUI.ButtonMANUAL.configure(bg='yellow')
    else:
        GUI.ButtonMANUAL.configure(bg=GUI.color_bg_1)
    if GV.HmiSW == 1:  #STOP MODE
        GUI.ButtonSTOP.configure(bg='yellow')
    else:
        GUI.ButtonSTOP.configure(bg=GUI.color_bg_1)
    GUI.LabelMessage.configure(text=error_message())
    GUI.root.after(500, call_back_cyclic_time)  #delay call [ms].
    return


def read_plc_tags() -> None:
    GV.HmiSP = PLC.read_holding_register_float32(register_address=GV.ADR_REG_HmiSP)
    GV.HmiPV = PLC.read_holding_register_float32(register_address=GV.ADR_REG_HmiPV)
    GV.HmiOP = PLC.read_holding_register_float32(register_address=GV.ADR_REG_HmiOP)
    GV.HmiSW = PLC.read_holding_register_uint16(register_address=GV.ADR_REG_HmiSW)
    GV.HmiCW = PLC.read_holding_register_uint16(register_address=GV.ADR_REG_HmiCW)
    return


def float32_to_string(float32_value=0.0, accuracy=2) -> str:
    return str(float(int(float32_value * (10 ** accuracy))) / (10 ** accuracy))


def error_message() -> str:
    msg = "No error."
    if GV.HmiSW & 1:
        msg = "Stop mode."
    if GV.HmiSW & 2:
        msg = "Manual mode."
    return msg


class GlobalVar(object):
    def __init__(self) -> None:
        self.HmiSP = 50.0
        self.HmiPV = 49.9
        self.HmiOP = 0.0
        self.HmiSW = 0
        self.HmiCW = 0
        self.HmiSP_Prev = 0.0
        self.HmiPV_Prev = 0.0
        self.HmiOP_Prev = 0.0
        self.ADR_REG_HmiSP = 4506
        self.ADR_REG_HmiPV = 4508
        self.ADR_REG_HmiOP = 4510
        self.ADR_REG_HmiSW = 4512
        self.ADR_REG_HmiCW = 4513
        return


class GlobalVarGui(object):

    def __init__(self) -> None:
        self.color_bg_1 = "#D4D0C8"
        self.root = tkinter.Tk()
        self.root.title("2PIRC16 PID control")
        self.root.resizable(False, False)
        # FrameValue
        self.FrameValue = tkinter.Frame(self.root)
        self.FrameValue.grid(column=0, row=0, padx=5, pady=5, sticky="news")
        # EntrySP
        self.EntrySP_value = tkinter.StringVar()
        self.EntrySP = tkinter.Entry(self.FrameValue, background='white')
        self.EntrySP.configure(textvariable=self.EntrySP_value)
        self.EntrySP.bind("<Return>", call_back_entry_sp_enter)  # Press "Enter"
        self.EntrySP.grid(column=0, row=0, sticky="w")
        # LabelSP
        self.LabelSP = tkinter.Label(self.FrameValue, text="Set point 0..100[unit]")
        self.LabelSP.grid(column=1, row=0, sticky="w")
        # EntryPV
        self.EntryPV_value = tkinter.StringVar()
        self.EntryPV = tkinter.Entry(self.FrameValue, background=self.color_bg_1)
        self.EntryPV.configure(textvariable=self.EntryPV_value)
        self.EntryPV.grid(column=0, row=1, sticky="w")
        # LabelPV
        self.LabelPV = tkinter.Label(self.FrameValue, text="Process value 0..100[unit]")
        self.LabelPV.grid(column=1, row=1, sticky="w")
        # EntryOP
        self.EntryOP_value = tkinter.StringVar()
        self.EntryOP = tkinter.Entry(self.FrameValue, background=self.color_bg_1)
        self.EntryOP.configure(textvariable=self.EntryOP_value)
        self.EntryOP.bind("<Return>", call_back_entry_op_enter)  # Press "Enter"
        self.EntryOP.grid(column=0, row=2, sticky="w")
        # LabelOP
        self.LabelOP = tkinter.Label(self.FrameValue, text="Output power 0..100[unit]")
        self.LabelOP.grid(column=1, row=2, sticky="w")
        # FrameButton
        self.FrameButton = tkinter.Frame(self.root)
        self.FrameButton.grid(column=0, row=1, padx=5, pady=5, sticky="news")
        # ButtonAUTO
        self.ButtonAUTO = tkinter.Button(self.FrameButton, text="AUTO", width=8, command=call_back_button_auto)
        self.ButtonAUTO.grid(column=0, row=0)
        # ButtonMANUAL
        self.ButtonMANUAL = tkinter.Button(self.FrameButton, text="MANUAL", width=8, command=call_back_button_manual)
        self.ButtonMANUAL.grid(column=1, row=0)
        # ButtonSTOP
        self.ButtonSTOP = tkinter.Button(self.FrameButton, text="STOP", width=8, command=call_back_button_stop)
        self.ButtonSTOP.grid(column=2, row=0)
        # FrameMessage
        self.FrameMessage = tkinter.Frame(self.root)
        self.FrameMessage.grid(column=0, row=2, padx=5, pady=5, sticky="news")
        # LabelMessage
        self.LabelMessage = tkinter.Label(self.FrameMessage)
        self.LabelMessage.grid(column=0, row=0, sticky="w")
        return

    def __del__(self) -> None:
        del self
        return


if __name__ == "__main__":
    GV = GlobalVar()
    GUI = GlobalVarGui()
    PLC = ModbusTcpMaster()
    PLC.start_tcp_client(ip_address='192.168.1.84') # Connect to PLC
    #PLC.start_tcp_client() # Connect to simulator
    read_plc_tags()
    GUI.EntrySP_value.set(float32_to_string(float32_value=GV.HmiSP, accuracy=2))
    GUI.EntryPV_value.set(float32_to_string(float32_value=GV.HmiPV, accuracy=2))
    GUI.EntryOP_value.set(float32_to_string(float32_value=GV.HmiOP, accuracy=2))
    call_back_cyclic_time()
    GUI.root.mainloop()

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

# Спасибо за лекции.
# https://www.youtube.com/@unx7784/playlists
# https://www.youtube.com/@tkhirianov/playlists
