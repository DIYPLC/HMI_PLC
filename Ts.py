#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

#Real time
def Task1(Reset = False, Ts_ns = 0):
    global Timer1
    Ts = float(Ts_ns) / 1000000000.0 #[s]
    Timer1 = Timer1 + Ts
    time.sleep(1) #DEBUG BIG DELAY!
    print(int(Timer1))
    return 0

Timer1 = 0.0 #[s]
Unix_time_ns  = time.time_ns()
Unix_time_ns_previous = Unix_time_ns
Ts_ns = 0
Task1(Reset = True, Ts_ns = 0)

while True:
    Unix_time_ns = time.time_ns()
    Ts_ns = Unix_time_ns - Unix_time_ns_previous
    Unix_time_ns_previous = Unix_time_ns
    Task1(Reset = False, Ts_ns = Ts_ns)

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
