#!/usr/bin/python
# -*- coding: utf-8 -*-

# Преобразование 16 бит в слово.
#      DbBitsToWord
#    +--------------+
#    | FbBitsToWord |
# ->-|In0        Out|->-
# ->-|In1           |
# ->-|In2           |
# ->-|In3           |
# ->-|In4           |
# ->-|In5           |
# ->-|In6           |
# ->-|In7           |
# ->-|In8           |
# ->-|In9           |
# ->-|In10          |
# ->-|In11          |
# ->-|In12          |
# ->-|In13          |
# ->-|In14          |
# ->-|In15          |
#    +--------------+


class FbBitsToWord():
    def __init__(self): #Auto init VAR
        #Входные переменные, сохраняемые.
        self.In0 = False
        self.In1 = False
        self.In2 = False
        self.In3 = False
        self.In4 = False
        self.In5 = False
        self.In6 = False
        self.In7 = False
        self.In8 = False
        self.In9 = False
        self.In10 = False
        self.In11 = False
        self.In12 = False
        self.In13 = False
        self.In14 = False
        self.In15 = False
        #Выходные переменные, сохраняемые.
        self.Out = 0
        #Внутренние переменные, сохраняемые.
        return
    def Run(self):
        self.Out = 0
        if (self.In0):
            self.Out = (self.Out | 0b0000_0000_0000_0001)
        if (self.In1):
            self.Out = (self.Out | 0b0000_0000_0000_0010)
        if (self.In2):
            self.Out = (self.Out | 0b0000_0000_0000_0100)
        if (self.In3):
            self.Out = (self.Out | 0b0000_0000_0000_1000)
        if (self.In4):
            self.Out = (self.Out | 0b0000_0000_0001_0000)
        if (self.In5):
            self.Out = (self.Out | 0b0000_0000_0010_0000)
        if (self.In6):
            self.Out = (self.Out | 0b0000_0000_0100_0000)
        if (self.In7):
            self.Out = (self.Out | 0b0000_0000_1000_0000)
        if (self.In8):
            self.Out = (self.Out | 0b0000_0001_0000_0000)
        if (self.In9):
            self.Out = (self.Out | 0b0000_0010_0000_0000)
        if (self.In10):
            self.Out = (self.Out | 0b0000_0100_0000_0000)
        if (self.In11):
            self.Out = (self.Out | 0b0000_1000_0000_0000)
        if (self.In12):
            self.Out = (self.Out | 0b0001_0000_0000_0000)
        if (self.In13):
            self.Out = (self.Out | 0b0010_0000_0000_0000)
        if (self.In14):
            self.Out = (self.Out | 0b0100_0000_0000_0000)
        if (self.In15):
            self.Out = (self.Out | 0b1000_0000_0000_0000)
        return
    def Set_In0(self, Value = 0):
        self.In0 = Value
        return
    def Set_In1(self, Value = 0):
        self.In1 = Value
        return
    def Set_In2(self, Value = 0):
        self.In2 = Value
        return
    def Set_In3(self, Value = 0):
        self.In3 = Value
        return
    def Set_In4(self, Value = 0):
        self.In4 = Value
        return
    def Set_In5(self, Value = 0):
        self.In5 = Value
        return
    def Set_In6(self, Value = 0):
        self.In6 = Value
        return
    def Set_In7(self, Value = 0):
        self.In7 = Value
        return
    def Set_In8(self, Value = 0):
        self.In8 = Value
        return
    def Set_In9(self, Value = 0):
        self.In9 = Value
        return
    def Set_In10(self, Value = 0):
        self.In10 = Value
        return
    def Set_In11(self, Value = 0):
        self.In11 = Value
        return
    def Set_In12(self, Value = 0):
        self.In12 = Value
        return
    def Set_In13(self, Value = 0):
        self.In13 = Value
        return
    def Set_In14(self, Value = 0):
        self.In14 = Value
        return
    def Set_In15(self, Value = 0):
        self.In15 = Value
        return
    def Get_Out(self):
        return self.Out

def Unit_test():
    print("Unit test start")
    from FbWordToBits import FbWordToBits
    DbWordToBits = FbWordToBits()
    DbBitsToWord = FbBitsToWord()
    Error_flag = False
    for i in range(65536):
        DbWordToBits.In = i
        DbWordToBits.Run()
        DbBitsToWord.In0 = DbWordToBits.Out0
        DbBitsToWord.In1 = DbWordToBits.Out1
        DbBitsToWord.In2 = DbWordToBits.Out2
        DbBitsToWord.In3 = DbWordToBits.Out3
        DbBitsToWord.In4 = DbWordToBits.Out4
        DbBitsToWord.In5 = DbWordToBits.Out5
        DbBitsToWord.In6 = DbWordToBits.Out6
        DbBitsToWord.In7 = DbWordToBits.Out7
        DbBitsToWord.In8 = DbWordToBits.Out8
        DbBitsToWord.In9 = DbWordToBits.Out9
        DbBitsToWord.In10 = DbWordToBits.Out10
        DbBitsToWord.In11 = DbWordToBits.Out11
        DbBitsToWord.In12 = DbWordToBits.Out12
        DbBitsToWord.In13 = DbWordToBits.Out13
        DbBitsToWord.In14 = DbWordToBits.Out14
        DbBitsToWord.In15 = DbWordToBits.Out15
        DbBitsToWord.Run()
        #print(hex(i), hex(DbBitsToWord.Out), hex(DbWordToBits.In))
        if (DbBitsToWord.Out != DbWordToBits.In):
            Error_flag = True
    if (Error_flag):
        print("Test ERROR")
    else:
        print("Test OK")
    return

if (__name__ == "__main__"):
    Unit_test()
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

