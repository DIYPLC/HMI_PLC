#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

print("Загружаем библиотеки через интернет.")

if (os.name == 'nt'):
    print("Программа запущена на Windows.")
    os.system("python.exe -m pip install --upgrade pip")

if (os.name == 'posix'):
    print("Программа запущена на Linux.")
    os.system("sudo apt update")

print("Библиотека MODBUS RTU MASTER")
try:
    import minimalmodbus
except:
    os.system("pip3 install minimalmodbus")

print("Библиотека OPC UA CLIENT / SERVER")
try:
    from opcua import Client
except:
    print("pip3 install freeopcua")
    os.system("pip3 install freeopcua")
    print("pip3 install opcua-client")
    os.system("pip3 install opcua-client")

print("Библиотека для подключение к MS SQL SERVER")
try:
    import pyodbc
except:
    print("pip3 install pyodbc")
    os.system("pip3 install pyodbc")

print("Библиотека для доступа к RS232/RS485")
try:
    import serial
except:
    print("pip3 install pyserial")
    os.system("pip3 install pyserial")

print("Библиотека для подключения к PLC SIEMENS S7-300")
try:
    import snap7
except:
    print("pip install python-snap7")
    #print("COPY FILE!!! C:\Windows\System32\snap7.dll C:\Windows\System32\snap7.lib")
    os.system("pip install python-snap7")

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
