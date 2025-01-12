# -*- coding: utf-8 -*-

"""
Пререводим коды ацп плк сименс в понятный диаппазон 0...100%
"""

import struct

def char_hex_to_int(char = "f"):
    """Конвертор шеснадцатиричного символа в десядичное число"""
    integer = 0
    if (char == "0"):
        integer = 0
    elif (char == "1"):
        integer = 1
    elif (char == "2"):
        integer = 2
    elif (char == "3"):
        integer = 3
    elif (char == "4"):
        integer = 4
    elif (char == "5"):
        integer = 5
    elif (char == "6"):
        integer = 6
    elif (char == "7"):
        integer = 7
    elif (char == "8"):
        integer = 8
    elif (char == "9"):
        integer = 9
    elif ((char == "A") or (char == "a")):
        integer = 10
    elif ((char == "B") or (char == "b")):
        integer = 11
    elif ((char == "C") or (char == "c")):
        integer = 12
    elif ((char == "D") or (char == "d")):
        integer = 13
    elif ((char == "E") or (char == "e")):
        integer = 14
    elif ((char == "F") or (char == "f")):
        integer = 15
    return integer

def string_to_uint16(string = "ffff"):
    """Шеснадцатиричную строку введенную с клавы превращаем в десятиричное число"""
    uint16  = 0
    hex1    = 0
    hex16   = 0
    hex256  = 0
    hex4069 = 0
    if(len(string) == 4): #Строка в 4 символа.
        hex1    = char_hex_to_int(string[3])
        hex16   = char_hex_to_int(string[2])
        hex256  = char_hex_to_int(string[1])
        hex4069 = char_hex_to_int(string[0])
    elif(len(string) == 3): #Строка в 3 символа.
        hex256   = char_hex_to_int(string[2])
        hex16  = char_hex_to_int(string[1])
        hex1 = char_hex_to_int(string[0])
    elif(len(string) == 2): #Строка в 2 символа.
        hex16  = char_hex_to_int(string[1])
        hex1 = char_hex_to_int(string[0])
    elif(len(string) == 1): #Строка в 1 символа.
        hex1 = char_hex_to_int(string[0])
    elif(len(string) > 4):
        print("Error input")
    uint16 = hex1 * 1 + hex16 * 16 + hex256 * 256 + hex4069 * 4096
    return uint16

def uint16_to_int16(uint16 = 0):
    """Смотрим на 16бит число без знака как на число с знаком"""
    int16  = 0
    pack_bytes = struct.pack(">H",uint16)
    int16 = struct.unpack(">h",pack_bytes)
    return int16[0]

print("SIMATIC ANALOG INPUT CALC.")
print("ERROR ADC CODE = 0x7FFF OR ADC = 0x8000")
print(" 4[mA] =     0[ADC] = 0x0000[ADC] =   0[%]")
print("12[mA] = 13824[ADC] = 0x3600[ADC] =  50[%]")
print("20[mA] = 27648[ADC] = 0x6C00[ADC] = 100[%]")

Input_string = input("INPUT ADC HEX CODE 0000...ffff = ")
Input_uint16 = string_to_uint16(Input_string)
Input_int16 = uint16_to_int16(Input_uint16)
ADC = Input_int16
PERCENT = (100 * ADC) / 27648
I = ((16 * ADC) / 27648) + 4
SENSOR_MIN = 0.0
SENSOR_MAX = 6.0
SENSOR_UNIT = "Bar"
SENSOR_VALUE = ( (ADC / 27648) * (SENSOR_MAX - SENSOR_MIN) ) + SENSOR_MIN

print()
print("ADC =", hex(Input_uint16), "HEX")
print("ADC =", ADC, "DEC")
print("PERCENT =", PERCENT, "%")
print("I =", I, "mA")
print("SENSOR =", SENSOR_VALUE, SENSOR_UNIT)
print("SENSOR 4...20 mA -> "+str(SENSOR_MIN)+"..."+str(SENSOR_MAX), SENSOR_UNIT)
print()
print("Ver 02-12-2022 DIY.PLC.314@gmail.com GNU GPL v2")
input("press any key for exit...")

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
