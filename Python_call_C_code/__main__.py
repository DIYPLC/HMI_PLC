#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python call c code for SOFT_PLC.
For strart cd directory and enter command make
Ubuntu 20.04.6 LTS + Python 3.8.10 + gcc 9.4.0 + GNU Make 4.2.1 test OK
"""

import os 
import time
import ctypes

"""INIT C CODE"""
#LibPlc = ctypes.CDLL(os.path.abspath(os.path.join(os.path.dirname(__file__), "LibPlc.so")))
LibPlc = ctypes.CDLL("./LibPlc.so") # Alternative short
#LibPlc.Read_float.restype = ctypes.c_float # specific call
#LibPlc.Read_double.restype = ctypes.c_double # specific call


class DbPyTask(ctypes.Structure): #c struct
    """ ./LIB_PLC/FbPyTask.h struct DbPyTask """
    _fields_ = [
    ('Ts', ctypes.c_float),
    ('Ts_ms', ctypes.c_uint32),
    ('Reset', ctypes.c_bool),
    ('MW0', ctypes.c_int16),
    ('MW1', ctypes.c_int16),
    ('MW2', ctypes.c_int16) ]
LibPlc.FbPyTask.argtypes = [ ctypes.POINTER(DbPyTask) ] #input function pointer struct
DbPyTask1 = DbPyTask() #instance c struct


def setup():
    DbPyTask1.Ts_ms = 0
    DbPyTask1.Reset = True
    LibPlc.FbPyTask(ctypes.byref(DbPyTask1))
    DbPyTask1.MW0 = -5
    DbPyTask1.MW1 = 3
    return

def loop():
    """CALL C CODE"""
    # Example two way interface
    DbPyTask1.Ts_ms = 100
    DbPyTask1.Reset = False
    LibPlc.FbPyTask(ctypes.byref(DbPyTask1))
    print("MW2=", DbPyTask1.MW2)
    # Example one way interface
    #print(LibPlc.Read_int8_t()) # not specific call
    #LibPlc.Write_int8_t(-8) # not specific call
    #LibPlc.Write_float(ctypes.c_float(3.2)) # specific call
    #LibPlc.Write_double(ctypes.c_double(6.4)) # specific call
    return

if(__name__ == "__main__"):
    setup()
    if(True):
    #while(True):
        loop()
		

#input("Press any key.")

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
