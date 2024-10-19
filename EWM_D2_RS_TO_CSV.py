"""
1. Чтение преобразователя сигналов тензодатчика ELHART через MODBUS RTU.
2. Запись веса каждую секунду в CSV файл.
3. TODO Запись веса каждую секунду в базу данный MS SQL Server.

VA 19-10-2023

ELHART EWM-D2-RS
RS485 MODBUS RTU, ADDRESS 1, 9600 Baud, 8N1
FUNCTION 3 READ HOLDING REGISTER
HOLDING REGISTER 0...8
"""

#import tkinter
#import socket
import struct
import time
import csv
#Импортируем библиотеку для подключения к MS SQL Server.
try:
    import pyodbc
except: #Eсли нет библиотеки качаем ее из интернета и пробуем еще раз.
    import os
    os.system("pip install pyodbc")
    import pyodbc
#Импортируем библиотеку для подключения по MODBUS RTU.
try: 
    import minimalmodbus
except: #Eсли нет библиотеки качаем ее из интернета и пробуем еще раз.
    import os
    os.system("pip install minimalmodbus") #python -m pip install minimalmodbus ?
    import minimalmodbus

class Global_var(): #Глобальные переменные и классы
    client = minimalmodbus.Instrument('com3', 1) # port, slave address
    """FOR Time_sampling()"""
    Time_cur_ns = 0
    Time_prev_ns = 0
    Time_sample_ns = 0
    Time_sample_max_ns = 0
    Uptime_ns = 0
    Uptime_s = 0.0
    Reset = False
    """FOR Read_MODBUS_RTU_slave_9_registers()"""
    MODBUS_RTU_SLAVE_HOLDING_REGISTER_0 = 0
    MODBUS_RTU_SLAVE_HOLDING_REGISTER_1 = 0
    MODBUS_RTU_SLAVE_HOLDING_REGISTER_2 = 0
    MODBUS_RTU_SLAVE_HOLDING_REGISTER_3 = 0
    MODBUS_RTU_SLAVE_HOLDING_REGISTER_4 = 0
    MODBUS_RTU_SLAVE_HOLDING_REGISTER_5 = 0
    MODBUS_RTU_SLAVE_HOLDING_REGISTER_6 = 0
    MODBUS_RTU_SLAVE_HOLDING_REGISTER_7 = 0
    MODBUS_RTU_SLAVE_HOLDING_REGISTER_8 = 0
    """FOR Driver_ELHART_EWM_D2_RS()"""
    ELHART_weight = 0.0 #Kg
    ELHART_weight_stable = False
    #DbWordToBits = FbWordToBits()

class FbWordToBits():
    #Входные переменные, сохраняемые.
    In = 0
    #Выходные переменные, сохраняемые.
    Out0 = False
    Out1 = False
    Out2 = False
    Out3 = False
    Out4 = False
    Out5 = False
    Out6 = False
    Out7 = False
    Out8 = False
    Out9 = False
    Out10 = False
    Out11 = False
    Out12 = False
    Out13 = False
    Out14 = False
    Out15 = False
    #Внутренние переменные, сохраняемые.
    def run(self):
        self.Out0  = bool(self.In & 0b0000000000000001)
        self.Out1  = bool(self.In & 0b0000000000000010)
        self.Out2  = bool(self.In & 0b0000000000000100)
        self.Out3  = bool(self.In & 0b0000000000001000)
        self.Out4  = bool(self.In & 0b0000000000010000)
        self.Out5  = bool(self.In & 0b0000000000100000)
        self.Out6  = bool(self.In & 0b0000000001000000)
        self.Out7  = bool(self.In & 0b0000000010000000)
        self.Out8  = bool(self.In & 0b0000000100000000)
        self.Out9  = bool(self.In & 0b0000001000000000)
        self.Out10 = bool(self.In & 0b0000010000000000)
        self.Out11 = bool(self.In & 0b0000100000000000)
        self.Out12 = bool(self.In & 0b0001000000000000)
        self.Out13 = bool(self.In & 0b0010000000000000)
        self.Out14 = bool(self.In & 0b0100000000000000)
        self.Out15 = bool(self.In & 0b1000000000000000)
        return

def RTC_label():
    #return str(time.ctime())
    return str(time.strftime("%d-%b-%Y %H:%M:%S"))

def Time_sampling(Reset = False):
    #t = time.time_ns() #Точнее
    t = time.monotonic_ns() #Надежнее
    #print(t)
    if(Reset): #Инициализация при сбросе
        GV.Time_cur_ns = t
        GV.Time_prev_ns = GV.Time_cur_ns
        GV.Uptime_ns = 0
        GV.Uptime_s = 0
    else:
        GV.Time_cur_ns = t
        if(GV.Time_cur_ns >= GV.Time_prev_ns): #Все идет хорошо
            GV.Time_sample_ns = GV.Time_cur_ns - GV.Time_prev_ns
            #print(GV.Time_sample_ns)
        GV.Time_prev_ns = GV.Time_cur_ns
        if(GV.Time_sample_ns > GV.Time_sample_max_ns): #Запомнить максимум
            GV.Time_sample_max_ns = GV.Time_sample_ns
            #print("Ts max:", GV.Time_sample_max_ns, "ns")
        GV.Uptime_ns = GV.Uptime_ns + GV.Time_sample_ns
        GV.Uptime_s = GV.Uptime_ns / 1000000000
    return

def Read_MODBUS_RTU_slave_9_registers():
    response = GV.client.read_registers(0, 9) #adr, count
    if response is None:
        print("ERROR 1 READ MODBUS RTU SLAVE")
    else:
        #print("OK READ MODBUS RTU SLAVE R0...8 =", response)
        GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_0 = response[0]
        GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_1 = response[1]
        GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_2 = response[2]
        GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_3 = response[3]
        GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_4 = response[4]
        GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_5 = response[5]
        GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_6 = response[6]
        GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_7 = response[7]
        GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_8 = response[8]
    return

def two_int16_to_int32(In_LO = 0, In_HI = 0):
    WORD_LO = In_LO
    WORD_HI = In_HI
    DWORD = struct.pack(">hh", WORD_HI, WORD_LO)
    Out = struct.unpack(">i", DWORD)
    return Out[0]

def Driver_ELHART_EWM_D2_RS():
    Net_weight_lo   = 0 #int32 R0+R1 Вес нетто.
    Net_weight_hi   = 0 #int32 R0+R1 Вес нетто.
    Gross_weight_lo = 0 #int32 R2+R3 Вес брутто.
    Gross_weight_hi = 0 #int32 R2+R3 Вес брутто.
    Product_counter = 0 #int16 R4 Счетчик изделий.
    Status1         = 0 #int16 R5 Статус преобразователя.
    Status2         = 0 #int16 R6 Статус преобразователя.
    Scale           = 0 #int16 R7 Процент нагрузки тензодатзика от номинального веса.
    Offset          = 0 #int16 R8 Смещение процента нагрузки тензодатзика.
    Net_weight_lo   = GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_0
    Net_weight_hi   = GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_1
    Gross_weight_lo = GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_2
    Gross_weight_hi = GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_3
    Product_counter = GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_4
    Status1         = GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_5
    Status2         = GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_6
    Scale           = GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_7
    Offset          = GV.MODBUS_RTU_SLAVE_HOLDING_REGISTER_8
    #Вес на тензо платформе [Кг].
    weight_int32 = two_int16_to_int32(In_LO = Net_weight_lo, In_HI = Net_weight_hi)
    GV.ELHART_weight = float(weight_int32) * 0.1
    #Флаг стабильности веса.
    Stat1 = FbWordToBits()
    Stat1.In = Status1
    Stat1.run()
    GV.ELHART_weight_stable = Stat1.Out0
    #print(GV.ELHART_weight_stable)
    return

def Write_csv_file():
    Kg_str = str(GV.ELHART_weight)
    Kg_str = Kg_str.replace('.', ',')
    Uptime_s_str = str(GV.Uptime_s)
    Uptime_s_str = Uptime_s_str.replace('.', ',')
    with open('Trend_Kg.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([Kg_str, Uptime_s_str, RTC_label()])
    csvfile.close()
    return

def Task1s(Reset = False, Ts_ns = 0): #Выполняется каждую 1 секунду (приблизительно).
    #Чтение регистров ELHART EWM-D2-RS по сети.
    try:
        Read_MODBUS_RTU_slave_9_registers()
    except:
        print("Error read 2")
    #Драйвер устройства ELHART EWM-D2-RS
    Driver_ELHART_EWM_D2_RS()
    #Запись веса в файл.
    try:
        Write_csv_file()
    except:
        print("ERROR Ошибка записи в csv файл")
    print("OK Вес = ", GV.ELHART_weight, "Кг", RTC_label())
    return

def Task1m(Reset = False, Ts_h = 1): #Выполняется каждую 1 минуту по RTC.
    return

def Task1h(Reset = False, Ts_h = 1): #Выполняется каждый 1 час по RTC.
    return

def Task12h(Reset = False, Ts_h = 12): #Выполняется каждые 12 час по RTC.
    return

def setup(): #Arduino style.)
    #MODBUS RTU INIT
    GV.client.serial.baudrate = 9600
    GV.client.serial.bytesize = 8
    GV.client.serial.parity = minimalmodbus.serial.PARITY_NONE
    GV.client.serial.stopbits = 1
    GV.client.serial.timeout = 1
    #GV.client.serial.timeout  = 0.05          # seconds
    #Задача 1
    Time_sampling(Reset = True) #Время скана программного ПЛК.
    GV.Reset = True
    Task1s(Reset = True, Ts_ns = 0) #Задача 1 в стиле LIB_PLC
    return

def loop(): #Arduino style.)
    time.sleep(1.0) #s
    Time_sampling(Reset = False) #Время скана программного ПЛК.
    GV.Reset = False
    Task1s(Reset = False, Ts_ns = GV.Time_sample_ns) #Задача 1 в стиле LIB_PLC
    #print("OK Ts_ns =", GV.Time_sample_ns)
    return

if __name__ == "__main__":
    print("OK START", RTC_label())
    GV = Global_var()
    setup()
    #if(1): #FOR DEBUG
    while(1):
        loop()
    GV.client.serial.close()
    print("OK STOP", RTC_label())
    #input("Press any key...")

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
