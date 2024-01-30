#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

print("Загружаем библиотеки через интернет.")

if (os.name == 'nt'):
    print("Программа запущена на Windows.")
    print("python.exe -m pip install --upgrade pip")
    os.system("python.exe -m pip install --upgrade pip")


if (os.name == 'posix'):
    print("Программа запущена на Linux.")
    print("python3 -m pip install --upgrade pip")
    os.system("sudo apt-get install python3-pip")
    os.system("python.exe -m pip install --upgrade pip")
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
    os.system("sudo apt-get install gcc")
    os.system("sudo apt-get install g++")
    os.system("sudo apt-get install make")
    os.system("sudo apt-get install git")
    os.system("sudo apt-get install vim")
    os.system("sudo apt-get install nmap")
    os.system("sudo apt-get install net-tools")
    os.system("sudo apt-get install htop")
    os.system("sudo apt-get install cmatrix")
    os.system("sudo apt-get install mc")
    os.system("sudo apt-get install tmux")
    os.system("sudo apt-get install dosbox")
    os.system("git clone https://github.com/DIYPLC/LIB_PLC.git")
    os.system("git clone https://github.com/DIYPLC/DIY_PLC.git")
    os.system("git clone https://github.com/DIYPLC/HMI_PLC.git")
    os.system("git clone https://github.com/DIYPLC/Tests.git")


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


print("Библиотека математики и графиков")
try:
    import numpy
    import matplotlib.pyplot
except:
    print("pip3 install matplotlib")
    os.system("pip3 install matplotlib")


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
# License: GNU GPL v2
#
# https://www.youtube.com/@DIY_PLC
# https://github.com/DIYPLC

# Спасибо за лекции.
# https://www.youtube.com/@unx7784/playlists
# https://www.youtube.com/@tkhirianov/playlists
