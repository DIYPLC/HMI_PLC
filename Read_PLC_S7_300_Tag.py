
"""
Обертка для библиотеки snap7:
https://pypi.org/project/python-snap7/#description
Для утановки библиотеки ввести в командную строку:
pip install python-snap7
Саму библиотеку скачать из:
http://snap7.sourceforge.net/
https://sourceforge.net/projects/snap7/files/
Скопировать файлы на компьютер:
C:\Windows\System32\snap7.dll
C:\Windows\System32\snap7.lib
В питоне 3.11 приседания с файлами не нужны.
На ПЛК в хардваре не должно стоять пароля.
Протестировано с PLC S7-300,S7-400.
"""

try: #импортируем библиотеку
    import snap7 #Для подключения к PLC S7-300(400)
except: #если нет библиотеки качаем ее из интернета и пробуем еще раз
    import os #Для запросов к операционной системе
    os.system("pip install python-snap7")
    input("COPY FILE!!! C:\Windows\System32\snap7.dll C:\Windows\System32\snap7.lib")
    import snap7 #Для подключения к PLC S7-300(400)

def Read_real_value_from_PLC_DB(DB_Number = 1, Adr_start_byte_in_db = 0): #Чтение REAL тега из ПЛК
    Size_byte = 4 #32bit 4byte for REAL
    RawDB = PLC.db_read(DB_Number, Adr_start_byte_in_db, Size_byte) #get 4byte
    Value = snap7.util.get_real(RawDB,0) #convert 4byte to float
    return float(Value)

def Read_int_value_from_PLC_DB(DB_Number = 1, Adr_start_byte_in_db = 0): #Чтение INT тега из ПЛК
    Size_byte = 2 #16bit 2byte for INT
    RawDB = PLC.db_read(DB_Number, Adr_start_byte_in_db, Size_byte) #get 2byte
    Value = snap7.util.get_int(RawDB,0) #convert 2byte to int
    return int(Value)

def Read_dword_value_from_PLC_DB(DB_Number = 1, Adr_start_byte_in_db = 0): #Чтение DWORD тега из ПЛК
    Size_byte = 4 #32bit 4byte for DWORD
    RawDB = PLC.db_read(DB_Number, Adr_start_byte_in_db, Size_byte) #get 4byte
    Value = snap7.util.get_dword(RawDB,0) #convert 4byte to dword
    return int(Value)

#Подключение к PLC S7-300(400)
PLC = snap7.client.Client()
PLC.connect('192.168.13.128', 0, 3) #(PLC_IP,PLC_Rack,PLC_Slot)
PLC_Tag = Read_real_value_from_PLC_DB(DB_Number = 64, Adr_start_byte_in_db = 0)
print("IP=192.168.13.128 R=0 S=3 DB64.DBD0 READ REAL PLC Tag = ", PLC_Tag)

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
