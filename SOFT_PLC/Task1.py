#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
from RTC import Rtc
from Write_to_Error_file import write_to_error_file


class Task1(object):
    
    def __init__(self) -> None:
        self.Time_sample_ns = int(0)
        self.Reset = bool(True)
        self.Stop_PLC = bool(False)
        self.User_timer_1_ns = int(0)
        self.User_timer_1_s = float(0.0)
        self.Rtc1 = Rtc()
        return
    
    def setup(self) -> None:
        write_to_error_file("[OK] START Task1.py")
        self.Rtc1()
        return
    
    def loop(self) -> None:
        self.Rtc1()
        time.sleep(1.0)
        self.Reset = False
        self.User_timer_1_ns = self.User_timer_1_ns + self.Rtc1.time_sample_ns
        self.User_timer_1_s = float(self.User_timer_1_ns / (10**9))
        print("[OK] User_timer_1_s", self.User_timer_1_s)
        return
    
    def __enter__(self) -> None: # with
        return
    
    def __call__(self) -> None: # ()
        return
    
    def __exit__(self) -> None:
        return
    
    def __del__(self) -> None: # del
        del self
        return


if __name__ == "__main__":
    print("[OK] UNIT TEST START")
    DbTask1 = Task1()
    DbTask1.setup()
    for i in range(10): # while True: test mode
        DbTask1.loop()
    print("[OK] UNIT TEST STOP")


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
