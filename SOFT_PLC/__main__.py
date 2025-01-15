#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
SOFT PLC
Python 3.12.2
Windows 10 Pro x64
Ubuntu 20.04.6 LTS + Python 3.8.10
15 jan 2025
"""

#import tkinter # TODO in ubuntu not work
import time
import socket
import struct
import array
from RTC import Rtc
from Write_to_Error_file import write_to_error_file

def error_generator():
    return 0 / 0

class GlobalVar(object):

    def __init__(self) -> None:  # Auto init VAR
        """ GLOBAL VAR """
        self.Ts_ns: int = 0
        self.Reset: bool = False
        """ TODO MODBUS TCP CLIENT """
        self.ADR1_MW0: int = 0  # MODBUS TCP Holding register int16
        """ GLOBAL CLASS """
        try:
            self.rtc = Rtc()
        except BaseException:
            write_to_error_file("ERROR Global_var __init__ FbRTC()")

class Task(object):

    def __init__(self) -> None:
        self.Reset :bool = False
        self.time_sample_ns :int = 0
        self.timer_1_ns :int = 0
        return

    def __call__(self) -> None:
        self.timer_1_ns = self.timer_1_ns + self.time_sample_ns
        timer1_s :float = float(self.timer_1_ns) / 1000000000.0
        print("timer1_s =", timer1_s, GV.rtc.rtc_label)
        return

    def __del__(self) -> None:
        del self
        return

def setup() -> None:  # Arduino style.)
    GV.Reset = True
    Task1.Reset = True
    Task1.time_sample_ns = GV.rtc.time_sample_ns
    Task1()
    return

def loop() -> None:  # Arduino style.)
    GV.Reset = False
    GV.rtc()
    GV.Ts_ns = GV.rtc.time_sample_ns
    Task1.Reset = False
    Task1.time_sample_ns = GV.rtc.time_sample_ns
    Task1()
    time.sleep(0.1)  # TODO DEBUG 0.1s.
    return

if __name__ == "__main__":
    """
    # DEBUG MODE WITH ERRORS
    GV = GlobalVar()
    Task1 = Task()S
    setup()
    while True:
        loop()
    """
    write_to_error_file("OK SOFT PLC START")
    flag_error :bool = True
    while flag_error:
        try:
            GV = GlobalVar()
            Task1 = Task()
            flag_error = False
        except BaseException:
            write_to_error_file("ERROR __main__ Global_var()")
            print("ERROR delay 10s")
            time.sleep(10)  # second
            flag_error = True
    flag_error :bool = True
    while flag_error:
        try:
            setup()
            flag_error = False
        except BaseException:
            write_to_error_file("ERROR __main__ setup()")
            print("ERROR delay 10s")
            time.sleep(10)  # second
            flag_error = True
    while True:
        try:
            loop()
        except BaseException:
            write_to_error_file("ERROR __main__ loop()")
            print("ERROR delay 10s")
            time.sleep(10)  # second

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
