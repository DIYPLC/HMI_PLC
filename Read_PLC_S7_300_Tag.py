import time
import snap7

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
"""

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

#Подключение к PLC S7-300
PLC = snap7.client.Client()
PLC.connect('192.168.0.2', 0, 2) #(PLC_IP,PLC_Rack,PLC_Slot)

PLC_Tag = Read_dword_value_from_PLC_DB(DB_Number = 2, Adr_start_byte_in_db = 4)
print("PLC_Tag = ", PLC_Tag)

time.sleep(30.0)
