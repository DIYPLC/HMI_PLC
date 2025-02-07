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
import ctypes
from RTC import Rtc
from Write_to_Error_file import write_to_error_file


def error_generator():
    return 0 / 0


class GlobalVar(object):

    def __init__(self) -> None:
        """ GLOBAL VAR """
        self.time_sample_ns = int(0)
        self.Reset = bool(True)
        """ TODO MODBUS TCP CLIENT """
        self.ADR1_MW0 = int(0)  # MODBUS TCP Holding register int16
        """ USER VARIABLES """
        self.user_timer_1_ns = int(0)
        """ GLOBAL CLASS """
        try:
            self.rtc = Rtc()
        except BaseException as error:
            write_to_error_file("ERROR GlobalVar __init__ Rtc()", error)

    def __call__(self) -> None:
        self.Reset = False
        self.rtc()
        self.time_sample_ns = self.rtc.time_sample_ns
        return

    def __del__(self) -> None:
        del self
        return


def task_cyclic(reset: bool = False, time_sample_ns: int = 0) -> None: # LIB_PLC style.
    GV.user_timer_1_ns = GV.user_timer_1_ns + time_sample_ns
    user_timer_1_s = float(GV.user_timer_1_ns / (10**9))
    print("user_timer_1_s", user_timer_1_s)
    return


def main() -> None:  # GCC style.
    task_cyclic(reset=GV.Reset, time_sample_ns=GV.rtc.time_sample_ns)
    while True:
        time.sleep(0.5)  # TODO DEBUG
        GV()  # Update sample time and reset flag
        task_cyclic(reset=GV.Reset, time_sample_ns=GV.rtc.time_sample_ns)


if __name__ == "__main__":
    debug_mode: bool = False  # TODO DEBUG
    if debug_mode:
        GV = GlobalVar()
        main()
    else:
        while True:
            try:
                write_to_error_file("OK SOFT PLC START")
                GV = GlobalVar()
                main()
            except BaseException as error:
                print("ERROR delay 10s", error)
                write_to_error_file("ERROR __main__.py")
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
