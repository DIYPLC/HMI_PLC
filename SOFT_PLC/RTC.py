#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python 3.12.2
Windows 10 pro x64
27-Mar-2024
Real Time Clock LIB
"""

import time


class FbRTC(object):
    """
    1. Чтение часов реального времени на компьютере.
    2. Расчет времени скана для SOFT PLC.
    3. Текстовая метка времени.
    """

    def __init__(self) -> None:
        """Вызывается автоматически один раз при инициализации."""
        # Выходные переменные, сохраняемые.
        """Чтение часов реального времени"""
        rtc_struct = time.localtime()
        self.Year: int = rtc_struct.tm_year  # Текущее время- Год 20xx.
        self.Month: int = rtc_struct.tm_mon  # Текущее время- Месяц 1...12.
        self.Day: int = rtc_struct.tm_mday  # Текущее время- День 1...31.
        self.Hour: int = rtc_struct.tm_hour  # Текущее время- Час 0...23.
        self.Minute: int = rtc_struct.tm_min  # Текущее время- Минута 0...59.
        self.Second: int = rtc_struct.tm_sec  # Текущее время- Секунда 0...61?.
        self.Weekday: int = rtc_struct.tm_wday  # Текущее время- День недели 0...6 пн...вс.
        self.Yearday: int = rtc_struct.tm_yday  # Текущее время- День в году 1...366.
        self.Ts_ns: int = 0  # Шаг дискретизации по времени [нс].
        self.Ts_ns_max: int = 0  # Максимальное время скана [нс].
        self.Uptime_ns: int = 0  # Время в работе [нс].
        self.Uptime_s: float = 0  # Время в работе [с].
        # Внутренние переменные, сохраняемые.
        """Вычисление времени скана в нано секундах"""
        # t :int = time.time_ns() # Точнее
        t: int = time.monotonic_ns()  # Надежнее
        self.Time_cur_ns: int = t
        self.Time_prev_ns: int = self.Time_cur_ns
        return

    def __call__(self) -> None:
        """Вызывается циклически ОДИН раз в скан."""
        """Чтение часов реального времени"""
        rtc_struct = time.localtime()
        self.Year = rtc_struct.tm_year  # Текущее время- Год 20xx.
        self.Month = rtc_struct.tm_mon  # Текущее время- Месяц 1...12.
        self.Day = rtc_struct.tm_mday  # Текущее время- День 1...31.
        self.Hour = rtc_struct.tm_hour  # Текущее время- Час 0...23.
        self.Minute = rtc_struct.tm_min  # Текущее время- Минута 0...59.
        self.Second = rtc_struct.tm_sec  # Текущее время- Секунда 0...61?.
        self.Weekday = rtc_struct.tm_wday  # Текущее время- День недели 0...6 пн...вс.
        self.Yearday = rtc_struct.tm_yday  # Текущее время- День в году 1...366.
        """Вычисление времени скана в нано секундах"""
        # t :int = time.time_ns() # Точнее
        t: int = time.monotonic_ns()  # Надежнее
        self.Time_cur_ns = t
        if self.Time_cur_ns >= self.Time_prev_ns:  # Все идет хорошо
            self.Ts_ns = self.Time_cur_ns - self.Time_prev_ns
        self.Time_prev_ns = self.Time_cur_ns
        """Максимальное время скана"""
        if self.Ts_ns > self.Ts_ns_max:
            self.Ts_ns_max = self.Ts_ns
        """Время в работе"""
        self.Uptime_ns = self.Uptime_ns + self.Ts_ns
        self.Uptime_s = self.Uptime_ns / 1000000000
        return

    def timestamp(self) -> str:
        """Текстовая метка времени."""
        # return str(time.ctime())
        return str(time.strftime("%d-%b-%Y %H:%M:%S"))


def unit_test():
    print("Unit test read PC RTC")
    rtc = FbRTC()
    print("Year    :", rtc.Year)
    print("Month   :", rtc.Month)
    print("Day     :", rtc.Day)
    print("Hour    :", rtc.Hour)
    print("Minute  :", rtc.Minute)
    print("Second  :", rtc.Second)
    print("Weekday :", rtc.Weekday)
    print("Yearday :", rtc.Yearday)
    print(rtc.timestamp())
    while rtc.Uptime_s <= 2:  # Работаем 2 секунды в тестовом режиме.
        rtc()
        print("Ts_ns:", rtc.Ts_ns, "ns")
        time.sleep(0.1)  # Задержка 100мс чтоб сильно не грузить процессор.
    help(rtc)
    input("press any key for exit...")
    return


if __name__ == "__main__":
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
