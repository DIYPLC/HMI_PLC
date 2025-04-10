#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
SOFT PLC
Python 3.12.2
Windows 10 Pro x64
Ubuntu 20.04.6 LTS + Python 3.8.10
08-04-2025
"""

#import tkinter # TODO in ubuntu not work
import time
import socket,struct,array,ctypes
import gc,importlib,os
from RTC import Rtc
from Write_to_Error_file import write_to_error_file


def error_generator():
    return 0 / 0


class GlobalVar(object):
    
    def __init__(self) -> None:
        """ SYSTEM VARIABLES """
        self.time_sample_ns = int(0)
        self.Reset = bool(True)
        self.Stop_PLC = bool(False)
        return
    
    def __del__(self) -> None:
        del self
        return


class Task_cyclic(object):
    
    def __init__(self) -> None:
        self.time_sample_ns = int(0)
        self.reset = bool(False)
        self.user_timer_1_ns = int(0)
        self.user_timer_1_s = float(0.0)
        return
    
    def __call__(self) -> None:
        self.user_timer_1_ns = self.user_timer_1_ns + self.time_sample_ns
        self.user_timer_1_s = float(self.user_timer_1_ns / (10**9))
        print("user_timer_1_s", self.user_timer_1_s)
        return
    
    def __del__(self) -> None:
        del self
        return


def main() -> None:  # GCC style.
    rtc()
    GV.time_sample_ns = rtc.time_sample_ns
    GV.Reset = True
    Task_cyclic1.time_sample_ns = GV.time_sample_ns
    Task_cyclic1.reset = True
    Task_cyclic1()
    while True:
        time.sleep(0.5)  # TODO DEBUG
        rtc()
        GV.time_sample_ns = rtc.time_sample_ns
        GV.Reset = False
        Task_cyclic1.time_sample_ns = GV.time_sample_ns
        Task_cyclic1.reset = False
        Task_cyclic1()
        if GV.Stop_PLC:
            write_to_error_file("OK SOFT PLC STOP")
            break


def auto_restart_plc() -> None:
    """" Этот метод работает но приводит к утечке памяти. """
    """ Возможно лучше перезагрузить OS. """
    print("auto_restart_plc()")
    if (os.name == 'posix'):
        os.system("python3 __main__.py")
    else: # os.name == 'nt'
        os.system("__main__.py")
    return


def reboot_windows() -> None:
    import os
    import time
    print("shutdown /r /f /t 60")
    time.sleep(5*60)
    os.system("shutdown /r /f /t 60") #60s delay
    time.sleep(90)
    return


if __name__ == "__main__":
    try:
        write_to_error_file("OK SOFT PLC START")
        rtc = Rtc()
        GV = GlobalVar()
        Task_cyclic1 = Task_cyclic()
        main()
    except BaseException as error:
        print("ERROR delay")
        write_to_error_file("ERROR __main__.py " + str(error))
        del rtc
        del GV
        del Task_cyclic1
        del main
        importlib.reload(socket)
        gc.collect()
        time.sleep(5)
        auto_restart_plc()


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
