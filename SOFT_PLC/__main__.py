#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
SOFT PLC
Python 3.12.2
Windows 10 pro x64
18 apr 2024
"""

import tkinter
import time
import socket
import struct
import array
from RTC import FbRTC
from Write_to_Error_file import write_to_error_file


def error_generator():
    return 0 / 0


def nop():
    return


class GlobalVar(object):
    """Глобальные переменные и классы."""

    def __init__(self) -> None:  # Auto init VAR
        """ Инициализация глобальных переменных. """
        self.Ts_ns: int = 0  # Шаг дискретизации по времени [нс].
        self.Reset: bool = False  # Сброс при перезагрузке.
        """MODBUS TCP CLIENT"""
        self.ADR1_MW0: int = 0  # MODBUS TCP Holding register int16
        """ Инициализация глобальных классов. """
        try:  # RTC
            self.RTC = FbRTC()
        except BaseException:
            write_to_error_file("ERROR Global_var __init__ FbRTC()")


def task_cyclic(reset: bool = False, ts_ns: int = 0) -> None:
    print("OK Uptime_s =", GV.RTC.Uptime_s)
    return


def setup():  # Arduino style.)
    # RST
    GV.Reset = True
    # Задача вызывается циклически.
    task_cyclic(reset=True, ts_ns=0)  # Задача 1 LIB_PLC style.)
    return


def loop():  # Arduino style.)
    # RTC
    GV.RTC()
    GV.Ts_ns = GV.RTC.Ts_ns
    # RST
    GV.Reset = False
    # Ts Расчет времени скана программного ПЛК.
    # Задача вызывается циклически.
    task_cyclic(reset=False, ts_ns=GV.RTC.Ts_ns)  # Задача 1 LIB_PLC style.)
    # DELAY
    time.sleep(0.1)  # 0.1s задержка чтоб меньше грузить процессор.
    return


if __name__ == "__main__":
    write_to_error_file("OK START")
    """Безопасная инициализация глобальных переменных с повтором при ошибке"""
    flag_error: bool = True
    while flag_error:
        try:
            GV = GlobalVar()
            flag_error = False
        except BaseException:
            write_to_error_file("ERROR __main__ Global_var()")
            print("ERROR delay 10s")
            time.sleep(10)  # second
            flag_error = True
    """Безопасный вызов первого скана с повтором при ошибке"""
    setup()
    flag_error: bool = True
    while flag_error:
        try:
            setup()
            flag_error = False
        except BaseException:
            write_to_error_file("ERROR __main__ setup()")
            print("ERROR delay 10s")
            time.sleep(10)  # second
            flag_error = True
    # if(1): #FOR DEBUG
    while 1:
        """Безопасный вызов скана программы с повтором при ошибке"""
        try:
            loop()
        except BaseException:
            write_to_error_file("ERROR __main__ loop()")
            print("ERROR delay 10s")
            time.sleep(10)  # second
    print("OK STOP", RTC_label())
    # input("Press any key...")

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
#
# https://www.youtube.com/@DIY_PLC
# https://github.com/DIYPLC

# Спасибо за лекции.
# https://www.youtube.com/@unx7784/playlists
# https://www.youtube.com/@tkhirianov/playlists
