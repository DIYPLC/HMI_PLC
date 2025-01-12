#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
OPC UA client
Connect to PLC cMT-CTRL01
Windows10 pro x64 Python3.11.3
Windows7 pro x32 Python3.7
Ubuntu 22.04.3 LTS x64 Python3.10.12
Connect to PLC cMT-CTRL01
date 21-12-2023
Веб конфигуратор в ПЛК:
http://10.234.16.13/admin/features/opcua
"""

import time

try:
    from opcua import Client
except: #Eсли нет библиотеки качаем ее из интернета и пробуем еще раз.
    import os
    print("python.exe -m pip install --upgrade pip")
    os.system("python.exe -m pip install --upgrade pip")
    print("pip3 install freeopcua")
    os.system("pip3 install freeopcua")
    print("pip3 install opcua-client")
    os.system("pip3 install opcua-client")
    from opcua import Client


def CallOpcUaExplorer():
    #Данная функция оказалась блокирующей пока не закроется браузер переменных.
    import os
    os.system("opcua-client")
    return


def OpcUaCleintReadPlcTag() -> float:
    """Подключение"""
    try:
        PLC_URL = "opc.tcp://10.234.16.13:4840/cMT-CTRL"
        Client1 = Client(PLC_URL)
        Client1.connect()
    except:
        print("ERROR OPC UA connect PLC")
        time.sleep(1)
    """Чтение данных из ПЛК"""
    try:
        PLC_TAG_NAME = "ns=2;s=Weintek Built-in CODESYS.Tags.Application.GV.Uptime_s"
        #ns - адресное пространство имён.
        Node1 = Client1.get_node(PLC_TAG_NAME)
        PLC_Value1 = Node1.get_value()
    except:
        print("ERROR OPC UA read PLC")
        PLC_Value1 = float('nan')
        #PLC_Value1 = 0.0
        time.sleep(1)
    """Отключение"""
    try:
        Client1.disconnect()
    except:
        print("ERROR OPC UA disconnect PLC")
        time.sleep(1)
    #print("PLC_Value1 =", PLC_Value1)
    return float(PLC_Value1)


def Unit_test():
    print("Unit test start")
    while(1):
    #for i in range(3):
        Uptime_s = OpcUaCleintReadPlcTag()
        print("PLC TAG Uptime_s =", Uptime_s)
        time.sleep(1)
    return


if (__name__ == "__main__"):
    Unit_test()
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

#----------------------------------------------------------------------
"""
Read me:
https://zhevak.wordpress.com/2019/07/22/%D0%B0-%D0%BD%D0%B5-%D0%BF%D0%BE%D1%89%D1%83%D0%BF%D0%B0%D1%82%D1%8C-%D0%BB%D0%B8-%D0%BD%D0%B0%D0%BC-opc-ua-%D0%BD%D0%B0-%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B5/
"""
#----------------------------------------------------------------------

"""
volotage-serv.py
#!/usr/bin/env python3
 
'''
voltage_serv.py
 
Сервер напряжения.
Иммитирует измерение напряжения и предоставляет значение для клиентов.
'''
 
 
URL = "opc.tcp://0.0.0.0:4840"
 
 
import sys
import random
import time
 
from opcua import Server
 
 
if __name__ == "__main__":
  server = Server()
  server.set_endpoint(URL)
 
  objects   = server.get_objects_node()
  ns        = server.register_namespace("Мои понятия")
  voltmeter = objects.add_object(ns, "Вольтметр")    
  voltage   = voltmeter.add_variable(ns, "Напряжение", 0.0)
 
  server.start()
     
  V = 220.0
  while True:            
    V = random.uniform(190.0, 240.0)
    print("{:8.1f} В".format(V))
    voltage.set_value(V)
     
    time.sleep(0.33)
 
  server.stop()
"""

#----------------------------------------------------------------------

"""
voltage-cli.py
#!/usr/bin/env python3
 
'''
voltage_cli.py
 
Напряжёметр -- клиент удалённого вольтметра.
'''
 
 
URL = "opc.tcp://localhost:4840"
 
 
import time
from opcua import Client
 
 
if __name__ == "__main__":
  client = Client(URL)
  client.connect()
   
  voltNode = client.get_node("ns=2;i=2")
   
  while True:
    voltage = voltNode.get_value()
     
    print("{0:.1f} В".format(voltage))
     
    time.sleep(1)
"""

#----------------------------------------------------------------------
