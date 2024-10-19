import os
import time
import ctypes

"""INIT C CODE"""
#LibPlc = ctypes.CDLL(os.path.abspath(os.path.join(os.path.dirname(__file__), "LibPlc.so")))
LibPlc = ctypes.CDLL("./LibPlc.so")
LibPlc.Read_float.restype = ctypes.c_float #return type for function.
LibPlc.Read_double.restype = ctypes.c_double #return type for function.

class StructDbFilterA(ctypes.Structure): #c struct
    """FbFilterA.h"""
    _fields_ = [
    ('In', ctypes.c_float),
    ('Tf', ctypes.c_float),
    ('Ts', ctypes.c_float),
    ('Out', ctypes.c_float) ]
LibPlc.FbFilterA.argtypes = [ ctypes.POINTER(StructDbFilterA) ] #input function pointer struct
DbFilterA = StructDbFilterA() #instance struct №1

class StructDbTask1(ctypes.Structure): #c struct
    """FbTask1.h"""
    _fields_ = [
    ('Ts_ms', ctypes.c_uint32),
    ('Reset', ctypes.c_bool) ]
LibPlc.FbTask1.argtypes = [ ctypes.POINTER(StructDbTask1) ] #input function pointer struct
DbTask1 = StructDbTask1() #instance struct №1

def loop():
    """CALL C CODE"""
    #      DbTask1
    #    +---------+
    #    | FbTask1 |
    # ->-|Ts_ms    |
    # ->-|Reset    |
    #    +---------+
    DbTask1.Ts_ms = 100;
    DbTask1.Reset = False;
    LibPlc.FbTask1(ctypes.byref(DbTask1))
    ###
    print(LibPlc.Read_bool())
    print(LibPlc.Read_uint8_t())
    print(LibPlc.Read_uint16_t())
    print(LibPlc.Read_uint32_t())
    print(LibPlc.Read_uint64_t())
    print(LibPlc.Read_int8_t())
    print(LibPlc.Read_int16_t())
    print(LibPlc.Read_int32_t())
    print(LibPlc.Read_int64_t())
    print(LibPlc.Read_float())
    print(LibPlc.Read_double())
    ###
    LibPlc.Write_bool(True)
    LibPlc.Write_uint8_t(8)
    LibPlc.Write_uint16_t(16)
    LibPlc.Write_uint32_t(32)
    LibPlc.Write_uint64_t(64)
    LibPlc.Write_int8_t(-8)
    LibPlc.Write_int16_t(-16)
    LibPlc.Write_int32_t(-32)
    LibPlc.Write_int64_t(-64)
    LibPlc.Write_float(ctypes.c_float(3.2))
    LibPlc.Write_double(ctypes.c_double(6.4))
    #Фильтр апериодический.
    #      DbFilterA
    #    +-----------+
    #    | FbFilterA |
    # ->-|In      Out|->-
    #   -|Tf         |
    #   -|Ts         |
    #    +-----------+
    DbFilterA.In = 3.14
    DbFilterA.Tf = 0.0
    DbFilterA.Ts = 0.1
    LibPlc.FbFilterA(ctypes.byref(DbFilterA))
    print(DbFilterA.Out)
    return

if(__name__ == "__main__"):
    loop()
    
#input("Press any key.")

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
