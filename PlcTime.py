#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Real time for soft PLC
"""
import time


class PlcTime(object):

    def __init__(self) -> None:
        """ Time sample ns. """
        self._time_current_ns_ :int = self._get_system_time_ns_()
        self._time_previous_ns_ :int = self._time_current_ns_
        self.time_sample_ns :int = self._time_current_ns_ - self._time_previous_ns_
        self.time_sample_max_ns :int = 0
        """ Uptime PLC """
        self.Uptime_ns :int = 0
        self.Uptime_s :int = 0
        self.Uptime_day :int = 0
        """ PC RTC. """
        rtc_struct = time.localtime()
        self.Year    :int = rtc_struct.tm_year #Текущее время- Год 20xx.
        self.Month   :int = rtc_struct.tm_mon  #Текущее время- Месяц 1...12.
        self.Day     :int = rtc_struct.tm_mday #Текущее время- День 1...31.
        self.Hour    :int = rtc_struct.tm_hour #Текущее время- Час 0...23.
        self.Minutes  :int = rtc_struct.tm_min  #Текущее время- Минута 0...59.
        self.Seconds  :int = rtc_struct.tm_sec  #Текущее время- Секунда 0...61?.
        self.Weekday :int = rtc_struct.tm_wday #Текущее время- День недели 0...6 пн...вс.
        self.Yearday :int = rtc_struct.tm_yday #Текущее время- День в году 1...366.
        self.rtc_label :str = str(time.strftime("%d-%b-%Y %H:%M:%S"))
        return

    def __call__(self) -> None:
        """ Time sample ns. """
        self._time_current_ns_ = self._get_system_time_ns_()
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
        self.Uptime_s = self.Uptime_ns // 10**9
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

    @staticmethod
    def _get_system_time_ns_() -> int:
        #system_time_ns :int = time.time_ns() # Точнее
        system_time_ns :int = time.monotonic_ns()  # Надежнее
        return system_time_ns

    def __del__(self) -> None:
        del self
        return


class Task(object):

    def __init__(self) -> None:
        self.Reset :bool = False
        self.time_sample_ns :int = 0
        self.timer_1_ns :int = 0
        return

    def __call__(self) -> None:
        self.timer_1_ns = self.timer_1_ns + self.time_sample_ns
        timer1_s :float = float(self.timer_1_ns) / 1000000000.0
        print("timer1_s =", timer1_s, PlcTime1.rtc_label)
        time.sleep(0.5)  # DEBUG
        return

    def __del__(self) -> None:
        del self
        return

def setup() -> None:
    Task1.Reset = True
    Task1.time_sample_ns = PlcTime1.time_sample_ns
    Task1()
    return

def loop() -> None:
    PlcTime1()
    Task1.Reset = False
    Task1.time_sample_ns = PlcTime1.time_sample_ns
    Task1()
    return

def unit_test() -> None:
    setup()
    #if True:
    while True:
        loop()

if __name__ == "__main__":
    PlcTime1 = PlcTime()
    Task1 = Task()
    unit_test()


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

