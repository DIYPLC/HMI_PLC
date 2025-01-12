#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import pyodbc

def Read_from_MS_SQL_Tid_float_Value(Tid = 0): #Чтение данных из MS SQL Server
    SQL_CLI_READ ="SELECT TOP 1 [ID] ,[Tid] ,[Value] ,[QC] ,[DateTime] ,[RecDateTime] FROM [Data_Base].[dbo].[PV] WHERE [Tid]=" + str(Tid) + " ORDER BY [RecDateTime] DESC;"
    print(SQL_CLI_READ)
    cursor.execute(SQL_CLI_READ) #Отправить SQL команду
    print("MS SQL Server:")
    row = cursor.fetchone()
    print("ID = "         , row[0])
    print("Tid = "        , row[1])
    print("Value = "      , row[2])
    print("QC = "         , row[3])
    print("DateTime = "   , row[4])
    print("RecDateTime = ", row[5])
    return float(row[2])

#Подключение к базе данных MS SQL через ODBC (DB API 2.0)
cnxn = pyodbc.connect("Driver={SQL Server};Server=192.168.1.3;Database=Data_Base;uid=user_name;pwd=user_password")
cursor = cnxn.cursor() #Курсор

value = Read_from_MS_SQL_Tid_float_Value(Tid = 22)
print(value)

time.sleep(30.0)

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
