#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Real time for soft PLC
"""

import time

def _get_system_time_ns_() -> int:
    # system_time_ns = time.time_ns() # Точнее
    system_time_ns = time.monotonic_ns()  # Надежнее
    return int(system_time_ns)

class Rtc(object):

    def __init__(self) -> None:
        """ Time sample ns. """
        self._time_current_ns_ = int(_get_system_time_ns_())
        self._time_previous_ns_ = int(self._time_current_ns_)
        self.time_sample_ns = int(self._time_current_ns_ - self._time_previous_ns_)
        self.time_sample_max_ns = int(0)
        """ Uptime PLC """
        self.Uptime_ns = int(0)
        self.Uptime_s = int(0)
        self.Uptime_day = int(0)
        """ PC RTC. """
        rtc_struct = time.localtime()
        self.Year     = int(rtc_struct.tm_year) #Текущее время- Год 20xx.
        self.Month    = int(rtc_struct.tm_mon)  #Текущее время- Месяц 1...12.
        self.Day      = int(rtc_struct.tm_mday) #Текущее время- День 1...31.
        self.Hour     = int(rtc_struct.tm_hour) #Текущее время- Час 0...23.
        self.Minutes  = int(rtc_struct.tm_min)  #Текущее время- Минута 0...59.
        self.Seconds  = int(rtc_struct.tm_sec)  #Текущее время- Секунда 0...61?.
        self.Weekday  = int(rtc_struct.tm_wday) #Текущее время- День недели 0...6 пн...вс.
        self.Yearday  = int(rtc_struct.tm_yday) #Текущее время- День в году 1...366.
        self.rtc_label  = str(time.strftime("%d-%b-%Y %H:%M:%S"))
        return

    def __call__(self) -> None:
        """ Time sample ns. """
        self._time_current_ns_ = _get_system_time_ns_()
        if self._time_current_ns_ >= self._time_previous_ns_:
            self.time_sample_ns = self._time_current_ns_ - self._time_previous_ns_
        else:
            self.time_sample_ns = 0
            print("ERROR CALC TIME SAMPLE")
        self._time_previous_ns_ = self._time_current_ns_
        if self.time_sample_ns > self.time_sample_max_ns:
            self.time_sample_max_ns = self.time_sample_ns
        """ Uptime PLC """
        self.Uptime_ns = self.Uptime_ns + self.time_sample_ns
        self.Uptime_s = self.Uptime_ns // (10**9)
        self.Uptime_day = self.Uptime_s // (60*60*24)
        """ PC RTC. """
        rtc_struct = time.localtime()
        self.Year    = rtc_struct.tm_year #Текущее время- Год 20xx.
        self.Month   = rtc_struct.tm_mon  #Текущее время- Месяц 1...12.
        self.Day     = rtc_struct.tm_mday #Текущее время- День 1...31.
        self.Hour    = rtc_struct.tm_hour #Текущее время- Час 0...23.
        self.Minutes  = rtc_struct.tm_min  #Текущее время- Минута 0...59.
        self.Seconds  = rtc_struct.tm_sec  #Текущее время- Секунда 0...61?.
        self.Weekday = rtc_struct.tm_wday #Текущее время- День недели 0...6 пн...вс.
        self.Yearday = rtc_struct.tm_yday #Текущее время- День в году 1...366.
        self.rtc_label: str = str(time.strftime("%d-%b-%Y %H:%M:%S"))
        return

    def __del__(self) -> None:
        del self
        return

def _unit_test_() -> None:
    print("Test start time", Rtc1.rtc_label)
    Rtc1()
    print("Rtc1.time_sample_ns =", Rtc1.time_sample_ns)
    input("press any key...")

if __name__ == "__main__":
    Rtc1 = Rtc()
    _unit_test_()


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
