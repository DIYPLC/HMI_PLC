#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

class FbReadRTC():
    Year    = 0 #Текущее время- Год 20xx.
    Month   = 0 #Текущее время- Месяц 1...12.
    Day     = 0 #Текущее время- День 1...31.
    Hour    = 0 #Текущее время- Час 0...23.
    Minute  = 0 #Текущее время- Минута 0...59.
    Second  = 0 #Текущее время- Секунда 0...61?.
    Weekday = 0 #Текущее время- День недели 0...6 пн...вс.
    Yearday = 0 #Текущее время- День в году 1...366.
    def Run(self):
        RTC_struct = time.localtime()
        self.Year    = RTC_struct.tm_year #Текущее время- Год 20xx.
        self.Month   = RTC_struct.tm_mon  #Текущее время- Месяц 1...12.
        self.Day     = RTC_struct.tm_mday #Текущее время- День 1...31.
        self.Hour    = RTC_struct.tm_hour #Текущее время- Час 0...23.
        self.Minute  = RTC_struct.tm_min  #Текущее время- Минута 0...59.
        self.Second  = RTC_struct.tm_sec  #Текущее время- Секунда 0...61?.
        self.Weekday = RTC_struct.tm_wday #Текущее время- День недели 0...6 пн...вс.
        self.Yearday = RTC_struct.tm_yday #Текущее время- День в году 1...366.
        return

def RTC_label(): #Текстовая метка времени.
    #return str(time.ctime())
    return str(time.strftime("%d-%b-%Y %H:%M:%S"))

class FbCalcScanTime(): #Расчет времени скана программного ПЛК.
    #Входные переменные, сохраняемые.
    Reset = False
    #Выходные переменные, сохраняемые.
    Ts_ns = 0
    Ts_ns_max = 0
    Uptime_ns = 0
    Uptime_s = 0
    #Внутренние переменные, сохраняемые.
    Time_cur_ns = 0
    Time_prev_ns = 0
    Time_sample_ns = 0
    def Run(self):
        #t = time.time_ns() #Точнее
        t = time.monotonic_ns() #Надежнее
        if(self.Reset): #Инициализация при сбросе
            self.Time_cur_ns = t
            self.Time_prev_ns = self.Time_cur_ns
            self.Uptime_ns = 0
            self.Uptime_s = 0
        else:
            self.Time_cur_ns = t
            if(self.Time_cur_ns >= self.Time_prev_ns): #Все идет хорошо
                self.Time_sample_ns = self.Time_cur_ns - self.Time_prev_ns
                #print(self.Time_sample_ns)
            self.Time_prev_ns = self.Time_cur_ns
            if(self.Time_sample_ns > self.Ts_ns_max): #Запомнить максимум
                self.Ts_ns_max = self.Time_sample_ns
                #print("Ts max:", self.Ts_ns_max, "ns")
            self.Uptime_ns = self.Uptime_ns + self.Time_sample_ns
            self.Uptime_s = self.Uptime_ns / 1000000000
        self.Ts_ns = self.Time_sample_ns #Более короткое имя
        return

def Unit_test():
    print("Unit test read PC RTC")
    DbReadRTC = FbReadRTC()
    DbReadRTC.Run()
    print("Year:", DbReadRTC.Year)
    print("Month:", DbReadRTC.Month)
    print("Day:", DbReadRTC.Day)
    print("Hour:", DbReadRTC.Hour)
    print("Minute:", DbReadRTC.Minute)
    print("Second:", DbReadRTC.Second)
    print("Weekday:", DbReadRTC.Weekday)
    print("Yearday:", DbReadRTC.Yearday)
    print(RTC_label())
    return

if (__name__ == "__main__"):
    Unit_test()
    input("press any key for exit...")

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
# Date: 2014 - 2024
# License: GNU GPL-2.0-or-later
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# https://www.youtube.com/watch?v=n1F_MfLRlX0
#
# See also:
# https://www.youtube.com/@DIY_PLC
# https://github.com/DIYPLC/LIB_PLC
# https://oshwlab.com/diy.plc.314/PLC_HW1_SW1
# https://3dtoday.ru/3d-models/mechanical-parts/body/korpus-na-din-reiku
# https://t.me/DIY_PLC
